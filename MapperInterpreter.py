import sys
from antlr4 import *
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
        base = ctx.IDENTIFIER(1).getText()
        
        if ctx.IDENTIFIER(2):  # Jeśli jest drugi obiekt (np. "trawa = grass + tree")
            obj = ctx.IDENTIFIER(2).getText()
            value = f"{base} + {obj}"
        else:
            value = base

        self.variables[name] = value
        print(f"Tile assigned: {name} = {value}")

    def visitNumberAssign(self, ctx):
        name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expr())
        self.variables[name] = value
        print(f"Number assigned: {name} = {value}")

    def visitBoolAssign(self, ctx):
        name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expr())  # Parsowanie wyrażenia logicznego
        self.variables[name] = value
        print(f"Boolean assigned: {name} = {value}")

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
        tile_name = ctx.IDENTIFIER().getText()
        print(f"visit draw inter'{tile_name}' at ({self.renderer.pointer_x}, {self.renderer.pointer_y})")
        self.renderer.draw_tile(tile_name)


    def visitErrorHandling(self, ctx):
        message = ctx.STRING().getText()
        print(f"Error: {message}")

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
