import sys
import copy
from pygments.lexer import include
from antlr4 import ParseTreeListener
from ErrorListener import MapperErrorListener
from PyQt5.QtCore import right
from antlr4 import *
from hamcrest import instance_of
from vtk.numpy_interface.algorithms import condition

from Blend import Blend
from MapperListener import MapperListener
from Road import Road
from Road import Position
from Tile import Tile
from Figure import Figure
from MapperLexer import MapperLexer
from MapperParser import MapperParser
from MapperVisitor import MapperVisitor
from MapperRenderer import MapperRenderer

class VariableDeclarationListener(ParseTreeListener):
    def __init__(self):
        self.var_types = {}  # Słownik przechowujący zmienne i ich typy
        self.errors = []     # Lista błędów (redeklaracje)

    def enterAssignment(self, ctx: MapperParser.AssignmentContext):

        if ctx.numberAssign():
            var_name = ctx.numberAssign().IDENTIFIER().getText()
            var_type = 'number'

        elif ctx.boolAssign():
            var_name = ctx.boolAssign().IDENTIFIER().getText()
            var_type = 'bool'

        elif ctx.tileAssign():
            var_name = ctx.tileAssign().IDENTIFIER().getText()
            var_type = 'tile'

        elif ctx.blendAssign():
            var_name = ctx.blendAssign().IDENTIFIER().getText()
            var_type = 'blend'

        elif ctx.noValueAssign():
            var_name = ctx.noValueAssign().IDENTIFIER().getText()
            var_type = ctx.noValueAssign().type_().getText()

        else:
            return
 
        # Now store in dictionary
        if var_name in self.var_types:
            token = ctx.start  # safer way to get token position
            line = token.line
            column = token.column
            raise RuntimeError(f"line: {line}, column: {column} Redeclaration of variable '{var_name}'")
        else:
            self.var_types[var_name] = var_type
            # print(f"Declared {var_type} {var_name}")
        

class MapperInterpreter(MapperVisitor):
    DEBUG = False  # Flaga debugowania - ustaw na True, aby włączyć printy, False, aby wyłączyć
    SHOW_ERRORS = True  # Flaga błędów - True włącza rzucanie wyjątków, False je ignoruje

    def __init__(self, var_types, renderer=None, logger=None):
        self.var_types = var_types  # Słownik z typami zmiennych z pierwszego przebiegu
        self.variables = {}         # Przechowuje wartości zmiennych
        self.functions = {}         # Przechowuje funkcje
        self.renderer = renderer or MapperRenderer()
        self.roads = {}
        self.logger = logger  # Logger do rejestrowania komunikatów

    def raiseError(self, ctx, msg):
        token = ctx.IDENTIFIER().getSymbol()
        line = token.line
        column = token.column
        raise RuntimeError(f"line: {line}, column: {column} {msg}")
    
    def visitPrintStatement(self, ctx: MapperParser.PrintStatementContext):
        self._debug_print("Handling print statement")
        if ctx.exprList():
            expr_values = [self.visit(expr) for expr in ctx.exprList().expr()]
            if(self.logger):
                self.logger.log(" ".join(map(str, expr_values)))
            print(*expr_values)  # Wypisz wszystkie wartości, oddzielone spacjami
            self._debug_print(f"Printed: {expr_values}")
        else:
            print()  # Pusty print dla print;
            self._debug_print("Printed empty line")

    # Metoda pomocnicza do debugowania
    def _debug_print(self, *args, **kwargs):
        if self.DEBUG:
            print(*args, **kwargs)
        
     # Metoda pomocnicza do rzucania błędów
    def _raise_error(self, message):
        if self.SHOW_ERRORS:
            raise RuntimeError(message)
        
    # Idenfitfies the type of object
    backgroundObjects = ['grass', 'soil', 'sand', 'water', 'rocks']
    foregroundObjects = ['tree', 'bush', 'stones', 'mountain', 'cabin', 'church']


    # this handles tile assignment: 
    # ex. grass + tree + bush + sand = Tile(background = sand, foreground = bush)
    def visitTileSum(self, ctx):
        self._debug_print("Visiting tile sum...")
        tile = Tile()
        for arg in ctx.IDENTIFIER():
            tile.add_obj(arg.getText())
        return tile
    
    #
    # def visitTileAssign(self, ctx):
    #     # Name of tile
    #     self._debug_print('tile assign')
    #     name = ctx.IDENTIFIER().getText()
    #     tile = self.visitTileSum(ctx.tileSum())  # Get the tile type (e.g., sand, grass)
    #
    #     self.variables[name] = tile

    def visitBlendAssign(self, ctx):

        self._debug_print('visted blend assign')
        blend_name = ctx.IDENTIFIER().getText()  # Get the blend name
        blend_options = []  # List to store the blend options
        self.var_types[blend_name] = 'blend' 

        self._debug_print(f"figuretext: {ctx.figure().getText()}")  # Debugging

        if ctx.figure().getText().startswith('circle'): 
            radius = int(ctx.figure().INT(0).getText())
            figure = Figure('circle', {'radius': radius})

        elif ctx.figure().getText().startswith('rectangle'):
            width = int(ctx.figure().INT(0).getText())
            height = int(ctx.figure().INT(1).getText())
            figure = Figure('rectangle', {'width': width, 'height': height})
        else:
            self._raise_error("❌ Błąd: Nieznany typ figury!")

        # Iterate through the blend options (ctx.blendOption())
        for option_ctx in ctx.blendOption():
            # allows syntax: blend blendName = circle 10 grass + tree 20%
            if(option_ctx.tileSum()):
                tile = self.visitTileSum(option_ctx.tileSum())

            # allows syntax: 
            # tile grassBush = grass + bush
            # blend blendName = circle 10 grassBush 20%
            # and 
            # blend blendName = circle 10 grass 20%
            elif (option_ctx.IDENTIFIER()):
                identifier = option_ctx.IDENTIFIER().getText()
                if(identifier in self.variables and isinstance(self.variables[identifier], Tile)):
                    tile = self.variables[identifier]
                else:
                    tile = Tile([identifier])
            else:
                self._raise_error("❌ Błąd: Nieznany typ opcji blendu!")
            
            percentage = int(option_ctx.INT().getText())
            blend_options.append((tile, percentage))

        self.variables[blend_name] = Blend(figure, blend_options)  # Store the blend in variables
    

    def visitNumberAssign(self, ctx):
        self._debug_print(f"handling: {ctx.getText()}")
        name = ctx.IDENTIFIER().getText()

        self._debug_print(f"Assigning number: {name}")
        self._debug_print(self.var_types)

        if name not in self.var_types:
            self.raiseError(ctx, f"Assignment of undeclared number '{name}'")

        expr = ctx.expr()
        if not expr:
            self._debug_print("Error: ctx.expr() is None!")
            return None
        value = self.visit(expr)
        self._debug_print(f"Evaluated value: {value}")
        self.variables[name] = value
        self._debug_print(f"Number assigned: {name} = {value}")

    def visitBoolAssign(self, ctx):
        print('visiting bool assign')
        name = ctx.IDENTIFIER().getText()
        if name not in self.var_types:
            self.raiseError(ctx, f"Assignment of undeclared boolean '{name}'")

        if ctx.expr():
            value = bool(self.visit(ctx.expr()))
        elif ctx.exprComp():
            value = self.visit(ctx.exprComp())


        self.variables[name] = value
        self._debug_print(f"Boolean assigned: {name} = {value}")
        return value

    def visitIncrement(self, ctx):
        name = ctx.IDENTIFIER().getText()
        self._debug_print(f"🆔 name: {name}")
        if name not in self.var_types:
            self.raiseError(ctx, f"Use of undeclared variable '{name}'")
        if name not in self.variables:
            self._raise_error(f"❌ Błąd: Zmienna '{name}' nie została zainicjalizowana!")
        current_value = self.variables[name]
        op = ctx.getChild(1).getText()
        if op in ('+=', '-='):
            value = self.visit(ctx.expr())
            if isinstance(current_value, int):
                delta = int(value)
                if op == '+=':
                    self._debug_print(f"🔄 {name} = {current_value} + {delta}")
                    self.variables[name] += delta
                else:
                    self._debug_print(f"🔄 {name} = {current_value} - {delta}")
                    self.variables[name] -= delta
            elif isinstance(current_value, Tile):
                if op == '+=':
                    self._debug_print(f"🧱 Dodaję do Tile: {name}.add_obj({value})")
                    self.variables[name].add_obj(value)
                else:
                    self._raise_error(f"❌ Tile nie obsługuje '-=': {name}")
            else:
                self._raise_error(f"❌ Nieobsługiwany typ dla {op}: {type(current_value).__name__}")
        elif op in ('++', '--'):
            if not isinstance(current_value, int):
                self._raise_error(f"❌ Operator '{op}' działa tylko na liczbach całkowitych")
            if op == '++':
                self._debug_print("++")
                self.variables[name] += 1
            else:
                self.variables[name] -= 1
            self._debug_print(f"🔢 {name} po '{op}': {self.variables[name]}")
        return self.variables[name]

    def visitReasignment(self, ctx):
        self._debug_print("Reassignment detected")
        name = ctx.IDENTIFIER().getText()
        if name not in self.var_types:
            self.raiseError(ctx, f"Undeclared variable '{name}'")
        if ctx.expr():
            value = self.visit(ctx.expr())

        self.variables[name] = value
        self._debug_print(f"Reassigned: {name} = {value}")
        return value


    def visitAssignment(self, ctx):
        self._debug_print("⚠️ Visiting assignment...")  # Debug
        if ctx.tileAssign():
            self._debug_print("✅ Tile assignment detected!")
            return self.visitTileAssign(ctx.tileAssign())
        elif ctx.numberAssign():
            self._debug_print("✅ Number assignment detected!")
            return self.visitNumberAssign(ctx.numberAssign())
        elif ctx.boolAssign():
            self._debug_print("✅ Boolean assignment detected!")
            return self.visitBoolAssign(ctx.boolAssign())
        elif ctx.increment():
            self._debug_print("✅ Increament assignment detected!")
            return self.visitIncrement(ctx.increment())
        elif ctx.blendAssign():
            self._debug_print("✅ Blend assignment detected!")
            return self.visitBlendAssign(ctx.blendAssign())
        elif ctx.noValueAssign():
            self._debug_print("✅ No value assignment detected!")
            return self.visitNoValueAssign(ctx.noValueAssign())
        else:
            self._debug_print("❌ Unknown assignment type!")

    def visitNoValueAssign(self, ctx): 
        self._debug_print("No value assignment detected")
        name = ctx.IDENTIFIER().getText()
        if name in self.variables:
            self._raise_error(f"❌ Błąd: Zmienna '{name}' już istnieje!")
        self.variables[name] = None

    def visitMove(self, ctx):
        direction = ctx.getChild(1).getText()
        value_expr = ctx.getChild(2)
        value = self.visit(value_expr)

        if direction == 'up':
            self.renderer.move_pointer(0, -value)
        elif direction == 'down':
            self.renderer.move_pointer(0, value)
        elif direction == 'left':
            self.renderer.move_pointer(-value, 0)
        elif direction == 'right':
            self.renderer.move_pointer(value, 0)
        self._debug_print(f"Pointer moved {direction} by {value}. New position: ({self.renderer.pointer_x}, {self.renderer.pointer_y})")


    def visitDraw(self, ctx):

        self._debug_print("drawing..")
        # if it is not Tile or Blend, make a Tile from given arguments (tree, bush, sand, etc.)
        if ctx.IDENTIFIER():
            self._debug_print("ctx")
            args = []
            counter = 0
            while(ctx.IDENTIFIER(counter)):
                args.append(ctx.IDENTIFIER(counter).getText())
                counter += 1
                
            for arg in args:
                if(arg in self.variables):
                    self.renderer.draw_tile(self.variables[arg])
                    return


            self.renderer.draw_tile(Tile(args=args))


        elif ctx.INT():  # Rysowanie z promieniem
            radius = int(ctx.INT().getText())
            percentages = []
            for pair in ctx.percentagePair():
                percent = int(pair.INT().getText())
                tile_type = pair.IDENTIFIER().getText()
                percentages.append((percent, tile_type))

            self._debug_print(f"Drawing radius {radius} with: {percentages}")
            blend = Blend(radius,percentages)
            self.renderer.draw_tile(blend)
        else:
            self._debug_print("ERROR: Invalid draw command!")


    def visitErrorHandling(self, ctx):
        message = ctx.STRING().getText()
        self._debug_print(f"Error: {message}")



    
    def visitWhileLoop(self, ctx):
        self._debug_print("Handling while loop")
        # Get condition expression
        condition_expr = ctx.exprComp()
        self._debug_print(f"Loop condition: {condition_expr.getText()}")

        # Evaluate condition
        while self.visit(condition_expr):  # Keep looping while condition is true
            self._debug_print("Loop body execution...")

            # Visit each statement inside the loop
            for stmt in ctx.statement():
                self._debug_print(f"Executing statement: {stmt.getText()}")
                self.visit(stmt)  # Execute statement
        self._debug_print("Exiting loop")

    def visitForLoop(self, ctx):
        self._debug_print("Handling for loop")
        number_assign = ctx.numberAssign()
        self.visit(number_assign)  # Execute the number assignment statement
        self._debug_print(f"Initialized: {number_assign.getText()}")

        # Get condition expression
        condition_expr = ctx.exprComp()
        self._debug_print(f"Loop condition: {condition_expr.getText()}")

        # Get increment expression
        increment_expr = ctx.increment()
        self._debug_print(f"Increment expression: {increment_expr.getText()}")

        # Loop execution
        while self.visit(condition_expr):  # Loop condition
            self._debug_print("Loop body execution...")

            # Visit each statement inside the loop
            for stmt in ctx.statement():
                self._debug_print(f"Executing statement: {stmt.getText()}")
                self.visit(stmt)  # Execute statement
            self._debug_print("trying to enter increment logic")
            # Evaluate the increment
            self.visit(increment_expr)
            self._debug_print(f"Increment executed?: {increment_expr.getText()}")
            
        self._debug_print("Exiting for loop")

    def visitLoop(self, ctx):
        if(ctx.forLoop()):
            return self.visitForLoop(ctx.forLoop())
        elif(ctx.whileLoop()):
            return self.visitWhileLoop(ctx.whileLoop())

    def visitRoadPlacement(self, ctx):
        if(ctx.roadStart()):
            return self.visitRoadStart(ctx.roadStart())
        elif(ctx.roadEnd()):
            return self.visitRoadEnd(ctx.roadEnd())

    def visitConditional(self, ctx:MapperParser.ConditionalContext):
        self._debug_print(f"Handling if statement: {ctx.getText()}")  # Debugging output

        # Extract and evaluate the condition
        if ctx.exprComp():
            condition_value = self.visit(ctx.exprComp())  # Should return True/False
            self._debug_print(f"Condition evaluated to: {condition_value}")
        elif ctx.expr():
            condition_value = bool(self.visit(ctx.expr()))


        if condition_value:
            self.visitIfConditionStatements(ctx.ifConditionStatements())
        else:
            if ctx.elseConditionStatements():
                self.visitElseConditionStatements(ctx.elseConditionStatements())

    def visitIfConditionStatements(self, ctx:MapperParser.IfConditionStatementsContext):
        self._debug_print("Handling if condition statement")
        # Visit each statement inside the if block
        for stmt in ctx.statement():
            self._debug_print(f"Executing statement: {stmt.getText()}")
            self.visit(stmt)

    def visitElseConditionStatements(self, ctx:MapperParser.ElseConditionStatementsContext): 
        self._debug_print("Handling else condition statement")
        # Visit each statement inside the else block
        for stmt in ctx.statement():
            self._debug_print(f"Executing statement: {stmt.getText()}")
            self.visit(stmt)


    def visitFunctionDecl(self, ctx):
        self._debug_print("fun decl")
        function_name = ctx.IDENTIFIER().getText()
        self._debug_print(function_name)

        params = []

        statements = ctx.statement()  # List of statements in the function body
        self._debug_print(f"dir: {dir(ctx)}")

        for param in ctx.param():
            self._debug_print(param.type_().getText())
            self._debug_print(param.IDENTIFIER())
            # Store both TYPE and IDENTIFIER for each parameter
            param_type = param.type_().getText() # assuming TYPE is defined as 'number', 'tile', etc.
            param_identifier = param.IDENTIFIER().getText()
            params.append({'type': param_type, 'identifier': param_identifier})

        # Store the function definition
        self.functions[function_name] = {
            'params': params,
            'statements': statements
        }

        self._debug_print(f"Function '{function_name}' declared with parameters {params}")

    def visitFunctionCall(self, ctx):
        self._debug_print("fun call")
        function_name = ctx.IDENTIFIER().getText()
        expr_list = [self.visit(expr) for expr in ctx.exprList().expr()] if ctx.exprList() else []

        if function_name == "print":
            self._debug_print(*expr_list)
            return None

        if function_name not in self.functions:
            self._raise_error(f"❌ Błąd: Funkcja '{function_name}' nie jest zadeklarowana!")

        function = self.functions[function_name]
        params = function['params']
        statements = function['statements']

        if len(expr_list) != len(params):
            self._raise_error(
                f"❌ Błąd: Funkcja '{function_name}' oczekuje {len(params)} argumentów, a otrzymała {len(expr_list)}!")

        # Here we ensure that each parameter is paired with its corresponding argument
        local_vars = {}
        local_var_types = {}
        for param, expr in zip(params, expr_list):
            self._debug_print(f"expr: {expr}")
            param_identifier = param['identifier']
            param_type = param['type']
            # You may want to add type-checking here if needed, e.g. ensure the type matches
            local_var_types[param_identifier] = param_type  # Update var_types with the parameter type
            local_vars[param_identifier] = expr

        original_vars = copy.deepcopy(self.variables)
        original_var_types = copy.deepcopy(self.var_types)
        self.var_types.update(local_var_types)
        self.variables.update(local_vars)

        self._debug_print(f"Local variables: {local_vars}")

        result = None
        for stmt in statements:
            result = self.visit(stmt)

        self.variables = original_vars
        self.var_types = original_var_types
        return result

    def visitExprComp(self, ctx):
        self._debug_print("Processing comparison expression")
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.children[1].getText()
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '==':
            return left == right
        elif op == '!=':
            return left != right
        elif op == '<':
            return left < right
        elif op == '>':
            return left > right
        elif op == '<=':
            return left <= right
        elif op == '>=':
            return left >= right
        else:
            raise Exception(f"Unknown comparison operator: {op}")

    def visitExprAddSub(self, ctx):
        self._debug_print("Processing addition/subtraction expression")
        left = self.visit(ctx.expr(0))  # Evaluate left expression
        right = self.visit(ctx.expr(1))  # Evaluate right expression
        op = ctx.children[1].getText()  # Get the operator ('+' or '-')

        # Perform the actual operation
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        else:
            raise RuntimeError(f"Unknown operator: {op}")

    def visitExprMulDiv(self, ctx):
        self._debug_print("Processing multiplication/division expression")
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.children[1].getText()
        if op == '*':
            return left * right
        elif op == '/':
            return left / right
        else:
            raise RuntimeError(f"Unknown operator: {op}")
    def visitExprParens(self, ctx):
        self._debug_print("Processing parenthesized expression")
        return self.visit(ctx.expr())

    def visitExprVar(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        self._debug_print(f"Processing variable reference: {var_name}: value: {self.variables.get(var_name)}")
        if var_name not in self.var_types:
            self.raiseError(ctx, f"Use of undeclared variable '{var_name}'")
        return self.variables.get(var_name)

    def visitExprInt(self, ctx):
        value = int(ctx.INT().getText())
        self._debug_print(f"Processing integer literal: {value}")
        return value

    def visitExprBool(self, ctx):
        self._debug_print("looking at bool in expr")
        value = ctx.BOOL().getText().lower() == 'true'
        self._debug_print(f"Processing boolean literal: {value}")
        return value



    # Visit a parse tree produced by MapperParser#roadStart.
    def visitRoadStart(self, ctx: MapperParser.RoadStartContext):
        name = ctx.IDENTIFIER().getText()
        if name in self.variables.keys():
            self._debug_print("this must be a new road")
        else:
            self._debug_print(f"Starting road: {name}")
            self.variables[name] = Road(Position(self.renderer.pointer_x , self.renderer.pointer_y))

    # Visit a parse tree produced by MapperParser#roadEnd.
    def visitRoadEnd(self, ctx: MapperParser.RoadEndContext):
        name = ctx.IDENTIFIER().getText()
        self._debug_print(f"Ending road {name}")
        if name not in self.variables.keys():
            self._debug_print("the road you are refering to doesnt exist")
        else:
            self.variables[name].end(Position(self.renderer.pointer_x, self.renderer.pointer_y), self.renderer)


if __name__ == "__main__":
    try:
        import sys
        input_stream = FileStream(sys.argv[1])
        lexer = MapperLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = MapperParser(token_stream)

        parser.removeErrorListeners()
        parser.addErrorListener(MapperErrorListener())

        tree = parser.program()

        # Pierwszy przebieg: rejestracja zmiennych
        var_listener = VariableDeclarationListener()
        walker = ParseTreeWalker()
        walker.walk(var_listener, tree)
        # print("Registered variables:", var_listener.var_types)  # Debugowanie

        # Sprawdzenie błędów redeklaracji
        if var_listener.errors:
            for error in var_listener.errors:
                print(error)
            sys.exit(1)

        # Drugi przebieg: interpretacja programu
        interpreter = MapperInterpreter(var_listener.var_types)
        interpreter.visit(tree)

        # print("Starting Pygame loop...")
        interpreter.renderer.run()

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)