import sys

from PyQt5.QtCore import right
from antlr4 import *
from hamcrest import instance_of
from vtk.numpy_interface.algorithms import condition

from Blend import Blend
from Road import Road
from Road import Position
from Tile import Tile
from Figure import Figure
from MapperLexer import MapperLexer
from MapperParser import MapperParser
from MapperVisitor import MapperVisitor
from MapperRenderer import MapperRenderer
class MapperInterpreter(MapperVisitor):
    def __init__(self):
        self.variables = {}  # Przechowuje zmienne
        self.functions = {}  # Przechowuje funkcje
        self.renderer = MapperRenderer()
        self.roads = {}
        
    # Idenfitfies the type of object
    backgroundObjects = ['grass', 'soil', 'sand', 'water', 'rocks']
    foregroundObjects = ['tree', 'bush', 'stones', 'mountain', 'cabin', 'church']


    # this handles tile assignment: 
    # ex. grass + tree + bush + sand = Tile(background = sand, foreground = bush)
    def visitTileSum(self, ctx):
        print("Visiting tile sum...")
        tile = Tile()
        for arg in ctx.IDENTIFIER():
            tile.add_obj(arg.getText())
        return tile
    

    def visitTileAssign(self, ctx):
        # Name of tile
        print('tile assign')
        name = ctx.IDENTIFIER().getText()
        tile = self.visitTileSum(ctx.tileSum())  # Get the tile type (e.g., sand, grass)
        
        self.variables[name] = tile

    def visitBlendAssign(self, ctx):

        print('visted blend assign')
        blend_name = ctx.IDENTIFIER().getText()  # Get the blend name
        blend_options = []  # List to store the blend options

        print(f"figuretext: {ctx.figure().getText()}")  # Debugging

        if ctx.figure().getText().startswith('circle'): 
            radius = int(ctx.figure().INT(0).getText())
            figure = Figure('circle', {'radius': radius})

        elif ctx.figure().getText().startswith('rectangle'):
            width = int(ctx.figure().INT(0).getText())
            height = int(ctx.figure().INT(1).getText())
            figure = Figure('rectangle', {'width': width, 'height': height})
        else:
            raise RuntimeError("❌ Błąd: Nieznany typ figury!")

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
                raise RuntimeError("❌ Błąd: Nieznany typ opcji blendu!")
            
            percentage = int(option_ctx.INT().getText())
            blend_options.append((tile, percentage))

        self.variables[blend_name] = Blend(figure, blend_options)  # Store the blend in variables
    
    def visitVarAssign(self, ctx:MapperParser.VarAssignContext):
        print("handling var assignment")
        name = ctx.IDENTIFIER().getText()
        if name not in self.variables:
            raise Exception(f"❌ Błąd: Zmienna '{name}' nie została zadeklarowana!")
        op = ctx.getChild(1).getText()
        expr = ctx.expr()
        print(f"{name} {op} {expr}")
        expr_value = self.visit(expr)
        print(f"expr v{expr_value}")

        self.variables[name] = expr_value


    def visitNumberAssign(self, ctx):
        print(f"handling: {ctx.getText()}")  # Debugging
        name = ctx.IDENTIFIER().getText()  # Get variable name

        # Debugging: check if expr() exists
        expr = ctx.expr()
        if not expr:
            print("Error: ctx.expr() is None!")
            return None

        value = self.visit(expr)


        print(f"Evaluated value: {value}")
        self.variables[name] = value
        print(f"Number assigned: {name} = {value}")

    def visitBoolAssign(self, ctx):
        name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expr())  # Parsowanie wyrażenia logicznego
        self.variables[name] = value
        print(f"Boolean assigned: {name} = {value}")
        return value

    def visitIncrement(self, ctx):
        name = ctx.IDENTIFIER().getText()
        print(f"🆔 name: {name}")
        if name not in self.variables:
            raise RuntimeError(f"❌ Błąd: Nieznana zmienna '{name}'!")
        current_value = self.variables[name]
        op = ctx.getChild(1).getText()  # '+=' | '-=' | '++' | '--'
        if op in ('+=', '-='):
            value = self.resolve_if_variable_number(ctx.expr())
            if isinstance(current_value, int):
                delta = int(value)
                if op == '+=':
                    print(f"🔄 {name} = {current_value} + {delta}")
                    self.variables[name] += delta
                else:
                    print(f"🔄 {name} = {current_value} - {delta}")
                    self.variables[name] -= delta

            elif isinstance(current_value, Tile):
                if op == '+=':
                    print(f"🧱 Dodaję do Tile: {name}.add_obj({value})")
                    self.variables[name].add_obj(value)
                else:
                    raise RuntimeError(f"❌ Tile nie obsługuje '-=': {name}")
            else:
                raise RuntimeError(f"❌ Nieobsługiwany typ dla {op}: {type(current_value).__name__}")

        # Obsługa ++ i --
        elif op in ('++', '--'):
            if not isinstance(current_value, int):
                raise RuntimeError(f"❌ Operator '{op}' działa tylko na liczbach całkowitych")
            if op == '++':
                print("++")
                self.variables[name] += 1
            else:
                self.variables[name] -= 1
            print(f"🔢 {name} po '{op}': {self.variables[name]}")

        return self.variables[name]

    def visitAssignment(self, ctx):
        print("⚠️ Visiting assignment...")  # Debug
        if ctx.tileAssign():
            print("✅ Tile assignment detected!")
            return self.visitTileAssign(ctx.tileAssign())
        elif ctx.numberAssign():
            print("✅ Number assignment detected!")
            return self.visitNumberAssign(ctx.numberAssign())
        elif ctx.boolAssign():
            print("✅ Boolean assignment detected!")
            return self.visitBoolAssign(ctx.boolAssign())
        elif ctx.increment():
            print("✅ Increament assignment detected!")
            return self.visitIncrement(ctx.increment())
        elif ctx.blendAssign():
            print("✅ Blend assignment detected!")
            return self.visitBlendAssign(ctx.blendAssign())
        elif ctx.varAssign():
            return self.visitVarAssign(ctx.varAssign())
        else:
            print("❌ Unknown assignment type!")

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
        print(f"Pointer moved {direction} by {value}. New position: ({self.renderer.pointer_x}, {self.renderer.pointer_y})")


    def visitDraw(self, ctx):

        print("drawing..")
        # if it is not Tile or Blend, make a Tile from given arguments (tree, bush, sand, etc.)
        if ctx.IDENTIFIER():
            print("ctx")
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

            print(f"Drawing radius {radius} with: {percentages}")
            blend = Blend(radius,percentages)
            self.renderer.draw_tile(blend)
        else:
            print("ERROR: Invalid draw command!")


    def visitErrorHandling(self, ctx):
        message = ctx.STRING().getText()
        print(f"Error: {message}")



    
    def visitWhileLoop(self, ctx):
        print("Handling while loop")
        # Get condition expression
        condition_expr = ctx.exprComp()
        print(f"Loop condition: {condition_expr.getText()}")

        # Evaluate condition
        while self.visit(condition_expr):  # Keep looping while condition is true
            print("Loop body execution...")

            # Visit each statement inside the loop
            for stmt in ctx.statement():
                print(f"Executing statement: {stmt.getText()}")
                self.visit(stmt)  # Execute statement
        print("Exiting loop")

    def visitForLoop(self, ctx):
        print("Handling for loop")
        number_assign = ctx.numberAssign()
        self.visit(number_assign)  # Execute the number assignment statement
        print(f"Initialized: {number_assign.getText()}")

        # Get condition expression
        condition_expr = ctx.exprComp()
        print(f"Loop condition: {condition_expr.getText()}")

        # Get increment expression
        increment_expr = ctx.increment()
        print(f"Increment expression: {increment_expr.getText()}")

        # Loop execution
        while self.visit(condition_expr):  # Loop condition
            print("Loop body execution...")

            # Visit each statement inside the loop
            for stmt in ctx.statement():
                print(f"Executing statement: {stmt.getText()}")
                self.visit(stmt)  # Execute statement
            print("trying to enter increment logic")
            # Evaluate the increment
            self.visit(increment_expr)
            print(f"Increment executed?: {increment_expr.getText()}")
            
        print("Exiting for loop")

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
        print(f"Handling if statement: {ctx.getText()}")  # Debugging output

        # Extract and evaluate the condition
        condition_value = self.visit(ctx.expr())  # Should return True/False
        print(f"Condition evaluated to: {condition_value}")

        if condition_value:
            print("Executing if branch...")
            statements = ctx.statement()  # Get statements inside the block
            print(f"Statements inside if: {len(statements)}")

            for statement_ctx in statements:
                print(f"Visiting statement: {statement_ctx.getText()}")
                self.visit(statement_ctx)

        print("Exiting if statement")

    def visitFunctionDecl(self, ctx):
        print("fun decl")
        function_name = ctx.IDENTIFIER().getText()
        print(function_name)

        params = []

        statements = ctx.statement()  # List of statements in the function body
        print(f"dir: {dir(ctx)}")

        for param in ctx.param():
            print(param.type_().getText())
            print(param.IDENTIFIER())
            # Store both TYPE and IDENTIFIER for each parameter
            param_type = param.type_() # assuming TYPE is defined as 'number', 'tile', etc.
            param_identifier = param.IDENTIFIER().getText()
            params.append({'type': param_type, 'identifier': param_identifier})

        # Store the function definition
        self.functions[function_name] = {
            'params': params,
            'statements': statements
        }

        print(f"Function '{function_name}' declared with parameters {params}")

    def visitFunctionCall(self, ctx):
        print("fun call")
        function_name = ctx.IDENTIFIER().getText()
        expr_list = [self.visit(expr) for expr in ctx.exprList().expr()] if ctx.exprList() else []

        if function_name == "print":
            print(*expr_list)
            return None

        if function_name not in self.functions:
            raise RuntimeError(f"❌ Błąd: Funkcja '{function_name}' nie jest zadeklarowana!")

        function = self.functions[function_name]
        params = function['params']
        statements = function['statements']

        if len(expr_list) != len(params):
            raise RuntimeError(
                f"❌ Błąd: Funkcja '{function_name}' oczekuje {len(params)} argumentów, a otrzymała {len(expr_list)}!")

        # Here we ensure that each parameter is paired with its corresponding argument
        local_vars = {}
        for param, expr in zip(params, expr_list):
            print(f"expr: {expr}")
            param_identifier = param['identifier']
            param_type = param['type']
            # You may want to add type-checking here if needed, e.g. ensure the type matches

            local_vars[param_identifier] = expr

        original_vars = self.variables
        self.variables = original_vars.copy()
        self.variables.update(local_vars)

        result = None
        for stmt in statements:
            result = self.visit(stmt)

        self.variables = original_vars
        return result

    def visitExprComp(self, ctx):
        print("Processing comparison expression")
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.children[1].getText()
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
#test
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
        print("Processing addition/subtraction expression")
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
        print("Processing multiplication/division expression")
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
        print("Processing parenthesized expression")
        return self.visit(ctx.expr())

    def visitExprVar(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        print(f"Processing variable reference: {var_name}: value: {self.variables.get(var_name)}")
        return self.variables.get(var_name)

    def visitExprInt(self, ctx):
        value = int(ctx.INT().getText())
        print(f"Processing integer literal: {value}")
        return value

    def visitExprBool(self, ctx):
        value = ctx.BOOL().getText().lower() == 'true'
        print(f"Processing boolean literal: {value}")
        return value



    # Visit a parse tree produced by MapperParser#roadStart.
    def visitRoadStart(self, ctx: MapperParser.RoadStartContext):
        name = ctx.IDENTIFIER().getText()
        if name in self.variables.keys():
            print("this must be a new road")
        else:
            print(f"Starting road: {name}")
            self.variables[name] = Road(Position(self.renderer.pointer_x , self.renderer.pointer_y))

    # Visit a parse tree produced by MapperParser#roadEnd.
    def visitRoadEnd(self, ctx: MapperParser.RoadEndContext):
        name = ctx.IDENTIFIER().getText()
        print(f"Ending road {name}")
        if name not in self.variables.keys():
            print("the road you are refering to doesnt exist")
        else:
            self.variables[name].end(Position(self.renderer.pointer_x, self.renderer.pointer_y), self.renderer)





# Uruchomienie interpretera
if __name__ == "__main__":
    input_stream = FileStream(sys.argv[1])
    lexer = MapperLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MapperParser(token_stream)
    tree = parser.program()
    
    interpreter = MapperInterpreter()
    interpreter.visit(tree)

    print("Starting Pygame loop...")
    interpreter.renderer.run() 
