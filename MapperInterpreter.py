import sys
from antlr4 import *
from vtk.numpy_interface.algorithms import condition

from Blend import Blend
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
    
    def visitNumberAssign(self, ctx):
        print(f"handling: {ctx.getText()}")  # Debugging

        name = ctx.IDENTIFIER().getText()  # Get variable name

        # Debugging: check if expr() exists
        expr_ctx = ctx.expr()
        if not expr_ctx:
            print("Error: ctx.expr() is None!")
            return None
        value = int(expr_ctx.getText())
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
        print(f"name {name}")
        value = ctx.expr().getText()# Pobierz wartość po +=
        if name not in self.variables:
            raise RuntimeError(f"❌ Błąd: Nieznana zmienna '{name}'!")
        if isinstance(self.variables[name],int):
            print(f"🔄 Aktualizuję {name}: {int(self.variables[name])} += {int(value)}")
            self.variables[name] +=int( value)  # Dodaj wartość do zmiennej
        print(self.variables[name])
        if isinstance(self.variables[name],Tile):
            self.variables[name].add_obj(value)
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
        # if it is not Tile or Blend, make a Tile from given arguments (tree, bush, sand, etc.) 
        if ctx.IDENTIFIER():
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
        condition_expr = ctx.expr()
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
        condition_expr = ctx.expr()
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
            
            # Evaluate the increment
            self.visit(increment_expr)
            print(f"Increment executed: {increment_expr.getText()}")
            
        print("Exiting for loop")

    def visitLoop(self, ctx):
        if(ctx.forLoop()):
            return self.visitForLoop(ctx.forLoop())
        elif(ctx.whileLoop()):
            return self.visitWhileLoop(ctx.whileLoop())


    def visitRoadStart(self, ctx):
        # roadIdentifier = ctx.IDENTIFIER().getText()
        # startPosition = self.renderer.pointer_x, self.renderer.pointer_y
        # self.variables[roadIdentifier]  =  # Store the road start position

        return
    
    def visitRoadEnd(self, ctx):
        return

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
        function_name = ctx.IDENTIFIER().getText()
        param_list = [param.getText() for param in ctx.paramList().IDENTIFIER()] if ctx.paramList() else []
        statements = ctx.statement()  # List of statements in the function body

        # Store the function definition
        self.functions[function_name] = {
            'params': param_list,
            'statements': statements
        }
        print(f"Function '{function_name}' declared with parameters {param_list}")

    def visitFunctionCall(self, ctx):
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
            raise RuntimeError(f"❌ Błąd: Funkcja '{function_name}' oczekuje {len(params)} argumentów, a otrzymała {len(expr_list)}!")

        local_vars = dict(zip(params, expr_list))
        original_vars = self.variables
        self.variables = original_vars.copy()
        self.variables.update(local_vars)

        result = None
        for stmt in statements:
            result = self.visit(stmt)

        self.variables = original_vars
        return result
    def visitExpr(self, ctx):
        print(f"Visiting expr: {ctx.getText()}")

        # Single value (number, boolean, or identifier)
        if ctx.getChildCount() == 1:
            value = ctx.getChild(0).getText()
            if value.isdigit():
                return int(value)
            elif value in ('true', 'false'):
                return value == 'true'
            elif value in self.variables:
                return self.variables[value]
            else:
                raise Exception(f"Undefined variable or value: {value}")

        # Binary operation
        elif ctx.getChildCount() == 3:
            left = self.visit(ctx.expr(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.expr(1))

            if op == "+": return left + right
            elif op == "-": return left - right
            elif op == "*": return left * right
            elif op == "/":
                if right == 0: raise Exception("❌ Błąd: Dzielenie przez zero!")
                return left / right
            elif op == "<": return left < right
            elif op == ">": return left > right
            elif op == "==": return left == right
            elif op == "!=": return left != right
            elif op == "<=": return left <= right
            elif op == ">=": return left >= right

        # Parenthesized expression
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expr(0))

        raise Exception(f"Invalid expression: {ctx.getText()}")
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
