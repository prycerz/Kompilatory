import sys
from antlr4 import *
from vtk.numpy_interface.algorithms import condition

from Blend import Blend
from Tile import Tile
from MapperLexer import MapperLexer
from MapperParser import MapperParser
from MapperVisitor import MapperVisitor
from MapperRenderer import MapperRenderer
class MapperInterpreter(MapperVisitor):
    def __init__(self):
        self.variables = {}  # Przechowuje zmienne
        self.renderer = MapperRenderer()
        
    def visitTileAssign(self, ctx):
        name = ctx.IDENTIFIER(0).getText()
        background = ctx.IDENTIFIER(1).getText()
        
        if ctx.IDENTIFIER(2):  # Jeśli jest drugi obiekt (np. "trawa = grass + tree")
            foreground = ctx.IDENTIFIER(2).getText()
            tile = Tile(background, foreground)
        else:
            tile = Tile(background)

        self.variables[name] = tile
        print(f"Tile assigned: {name} = background: {tile.background} foreground: {tile.foreground}")

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
            self.variables[name].foreground = value
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
            print("incrementing")
            return self.visitIncrement(ctx.increment())
        else:
            print("❌ Unknown assignment type!")
    def visitMove(self, ctx):
        direction = ctx.getChild(1).getText()
        value = int(ctx.getChild(2).getText())
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
        if ctx.IDENTIFIER():
            tile_name = ctx.IDENTIFIER().getText()
            print(f"visit draw {tile_name} at ({self.renderer.pointer_x}, {self.renderer.pointer_y})")
            if tile_name in self.variables:
                self.renderer.draw_tile(self.variables[tile_name])
            self.renderer.draw_tile(tile_name)
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

    def visitLoop(self, ctx: MapperParser.LoopContext):
        print("Handling loop")

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

    def visitExpr(self, ctx):
        print(f"Visiting expr: {ctx.getText()}")
        print(f"Child count: {ctx.getChildCount()}")

        for i in range(ctx.getChildCount()):
            print(f"Child {i}: {ctx.getChild(i).getText()}")

        if ctx.getChildCount() == 1:  # Single value (number or identifier)
            value = ctx.getChild(0).getText()

            # Check if it's a number
            if value.isdigit():
                return int(value)  # Convert to int
            elif value in self.variables:  # Check if it's a variable
                return int (self.variables[value])  # Return stored value
            else:
                raise Exception(f"Undefined variable: {value}")  # Handle unknown var

        elif ctx.getChildCount() == 3:  # Binary expressions (e.g., i < 3)
            left = self.visit(ctx.getChild(0))  # Evaluate left operand
            op = ctx.getChild(1).getText()  # Operator
            right = self.visit(ctx.getChild(2))  # Evaluate right operand

            print(f"Evaluating: {left} {op} {right}")

            if op == "<":
                return left < right
            elif op == ">":
                return left > right
            elif op == "==":
                return left == right
            # Add other operators as needed

        return None


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
    interpreter.renderer.run()  # 🚀 Keep the window open!
