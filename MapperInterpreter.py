import sys
import copy
from logging import exception

from mpi4py.futures.aplus import catch
from numpy import roots
from pygments.lexer import include
from antlr4 import ParseTreeListener
from xdg.Mime import get_type

import scope_tree
from ErrorListener import MapperErrorListener
from PyQt5.QtCore import right
from antlr4 import *
from hamcrest import instance_of
from vtk.numpy_interface.algorithms import condition
from scope_tree import TreeNode
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

class Types:
    NUMBER = int
    BOOL = bool
    TILE = Tile
    BLEND = Blend
    ROAD = Road
class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value
class VariableDeclarationListener(ParseTreeListener):
    def __init__(self):
        #self.var_types = {}  # Słownik przechowujący zmienne i ich typy -> zmiana koncepcji
        #self.var_types_scoped = [{}]  # lista słowników, pierwszy to globalny kolejne są młodsze
        #self.all_var_types = {}

        self.root = TreeNode() #korzen drzewa
        self.current_node: TreeNode = self.root #obecny node
        self.var_tree = self.root #drzewo przechowujące zmienne i ich typy
        self.errors = []     # Lista błędów (redeklaracje)



    def enterScope(self):
        #self.var_types_scoped.append({})
        new_child = TreeNode(self.current_node)
        self.current_node.add_child(new_child)
        print("added child")
        self.current_node = self.current_node.move_in()

    def exitScope(self):
        self.current_node = self.current_node.move_out()

        #for name, vartype in current_scope.items():
        #    self.all_var_types[name] = vartype


    def enterBlock(self,ctx):
        self.enterScope()
        for stmt in ctx.statement():
            self.enterEveryRule(stmt)

    def exitBlock(self,ctx):
        self.exitScope()

    # def nameExists(self,name):
    #     for scope in self.var_types_scoped:
    #         if name in scope:
    #             return True
    #     return False
    # def getTypeOfName(self,ctx,name):
    #     for scope in reversed (self.var_types_scoped):
    #         if name in scope:
    #             return scope[name]

    def enterAssignment(self, ctx: MapperParser.AssignmentContext):

        if ctx.numberAssign():
            var_name = ctx.numberAssign().IDENTIFIER().getText()
            var_type = Types.NUMBER

        elif ctx.boolAssign():
            var_name = ctx.boolAssign().IDENTIFIER().getText()
            var_type = Types.BOOL

        elif ctx.tileAssign():
            var_name = ctx.tileAssign().IDENTIFIER().getText()
            var_type = Types.TILE

        elif ctx.blendAssign():
            var_name = ctx.blendAssign().IDENTIFIER().getText()
            var_type = Types.BLEND

        elif ctx.noValueAssign():
            var_name = ctx.noValueAssign().IDENTIFIER().getText()
            var_type = ctx.noValueAssign().type_().getText()

        else:
            return
 
        # Now store in dictionary
        if self.current_node.var_name_is_declared(var_name):
            token = ctx.start  # safer way to get token position
            line = token.line
            column = token.column
            raise RuntimeError(f"line: {line}, column: {column} Redeclaration of variable '{var_name}' in the scope raised in listener")
        else:
            self.current_node.add_type(var_name,var_type)
            # print(f"Declared {var_type} {var_name}")

    def enterRoadStart(self, ctx:MapperParser.RoadStartContext):
        var_name = ctx.IDENTIFIER().getText()
        var_type = Types.ROAD
        # Now store in dictionary
        if self.current_node.var_name_is_declared(var_name):
            token = ctx.start  # safer way to get token position
            line = token.line
            column = token.column
            raise RuntimeError(f"line: {line}, column: {column} Redeclaration of variable '{var_name}' in the scope raised in listener")
        else:
            self.current_node.add_type(var_name, var_type)

    def enterRoadEnd(self, ctx:MapperParser.RoadEndContext):
        var_name = ctx.IDENTIFIER().getText()
        var_type = Types.ROAD
        # Now store in dictionary
        if not self.current_node.name_Exists_up(var_name):
            token = ctx.start  # safer way to get token position
            line = token.line
            column = token.column
            raise RuntimeError(
                f"line: {line}, column: {column} the road '{var_name}' you are trying to end doesnt start in this or the parent scope!")


    def raiseError(self, ctx, msg):
        token = ctx.IDENTIFIER().getSymbol()
        line = token.line
        column = token.column
        raise RuntimeError(f"line: {line}, column: {column} {msg}")


    def get_type(self,ctx,type_str: str):
        print("entered ")
        type_map = {
            "number": Types.NUMBER,
            "bool": Types.BOOL,
            "tile": Types.TILE,
            "blend": Types.BLEND,
            "road": Types.ROAD,
        }
        if type_str not in type_map:
            self.raiseError(ctx,f"Unknown type: {type_str}")
        return type_map[type_str]

    # Enter a parse tree produced by MapperParser#functionDecl.
    def enterFunctionDecl(self, ctx: MapperParser.FunctionDeclContext):
        function_name = ctx.IDENTIFIER().getText()
        if function_name in self.current_node.functions:
            self.raiseError(ctx,f"function {function_name} already exists in this scope")
        params = []
        seen_names = set()
        statements = ctx.statement()  # List of statements in the function body


        for param in ctx.param():
            return_type = self.get_type(ctx,ctx.children[0].getText())
            print(f"return type {return_type}")
            param_type = param.type_().getText()
            param_identifier = param.IDENTIFIER().getText()
            print(param_type)
            print(param_identifier)
            # Store both TYPE and IDENTIFIER for each parameter
            param_type = self.get_type(ctx,param_type)  # assuming TYPE is defined as 'number', 'tile', etc.
            print(f"resolved type:{param_type}")
            if param_identifier in seen_names:
                self.raiseError(ctx,f"{param_identifier} multiple occurences in function declaration")
            seen_names.add(param_identifier)
            params.append({'type': param_type, 'identifier': param_identifier})

        # Store the function definition
        self.root.functions[function_name] = {
            'params': params,
            'statements': statements,
            'return_type': return_type
        }


        print(f"Function '{function_name}' declared with parameters {params}")
    # Exit a parse tree produced by MapperParser#functionDecl.
    def exitFunctionDecl(self, ctx: MapperParser.FunctionDeclContext):
        pass

    # Enter a parse tree produced by MapperParser#functionCall.
    def enterFunctionCall(self, ctx: MapperParser.FunctionCallContext):
        print("fun call listener")
        function_name = ctx.IDENTIFIER().getText()
        expr_list = [self.enterEveryRule(expr) for expr in ctx.exprList().expr()] if ctx.exprList() else []

        if function_name == "print":
            pass

        if function_name not in self.root.functions:
            self.raiseError(ctx,f"function'{function_name}' isnt declared!")

        function = self.root.functions[function_name]
        params = function['params']
        statements = function['statements']

        if len(expr_list) != len(params):
            self._raise_error(
                f"❌ Błąd: Funkcja '{function_name}' oczekuje {len(params)} argumentów, a otrzymała {len(expr_list)}!")
        self.enterScope()

        for param, value in zip(params, expr_list):
            param_identifier = param['identifier']
            param_type = param['type']
            print(f"value {value}")
            self.current_node.add_type(param_identifier, param_type)
            #self.current_node.add_var(param_identifier, value)

        result = None
        # for stmt in statements:
        #     result = self.visit(stmt)

        self.exitScope()
        # return result

    # Exit a parse tree produced by MapperParser#functionCall.
    def exitFunctionCall(self, ctx: MapperParser.FunctionCallContext):
        pass




class MapperInterpreter(MapperVisitor):
    DEBUG = True  # Flaga debugowania - ustaw na True, aby włączyć printy, False, aby wyłączyć
    SHOW_ERRORS = True  # Flaga błędów - True włącza rzucanie wyjątków, False je ignoruje

    def __init__(self, types_tree, renderer=None, logger=None):

        self.root = types_tree.get_root() #korzen drzewa
        self.current_node = self.root #obecny node
        #self.variables = {}         # Przechowuje wartości zmiennych
        self.functions = {}         # Przechowuje funkcje
        self.renderer = renderer or MapperRenderer()
        self.roads = {}
        self.logger = logger  # Logger do rejestrowania komunikatów



    def raiseError(self, ctx, msg):
        token = ctx.IDENTIFIER().getSymbol()
        line = token.line
        column = token.column
        raise RuntimeError(f"line: {line}, column: {column} {msg}")

    #scope functions
    def enterScope(self):
        #self.var_types_scoped.append({})
        new_child = TreeNode(self.current_node)
        self.current_node.add_child(new_child)
        self.current_node = self.current_node.move_in()
    def exitScope(self):
        self.current_node = self.current_node.move_out()
    def visitBlock(self,ctx):
        self.enterScope()
        for stmt in ctx.statement():
            self.visit(stmt)
        self.exitScope()


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
    

    def visitTileAssign(self, ctx):
        # Name of tile
        self._debug_print('tile assign')
        name = ctx.IDENTIFIER().getText()
        if not self.current_node.name_Exists_up(name):
            self.raiseError(ctx, f"Assignment of undeclared number '{name}'")

        tile = self.visitTileSum(ctx.tileSum())  # Get the tile type (e.g., sand, grass)
        self.current_node.add_var(name,tile,Types.TILE)


    def visitBlendAssign(self, ctx):

        self._debug_print('visted blend assign')
        blend_name = ctx.IDENTIFIER().getText()  # Get the blend name
        blend_options = []  # List to store the blend options
        if not self.current_node.name_Exists_up(blend_name):
            self.raiseError(ctx, f"Assignment of undeclared number '{blend_name}'")


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
                if(self.current_node.name_Exists_up(identifier)  and isinstance(self.getVariableOfName(ctx,identifier), Tile)):
                    tile = self.getVariableOfName(ctx,identifier)
                else:
                    tile = Tile([identifier])
            else:
                self._raise_error("❌ Błąd: Nieznany typ opcji blendu!")
            
            percentage = int(option_ctx.INT().getText())
            blend_options.append((tile, percentage))
        self.current_node.add_var(blend_name,Blend(figure, blend_options),Types.BLEND)

    
    def l_r_type(self,ctx):
        # to nie dziala i przechodzi number a = false
        name = ctx.IDENTIFIER().getText()
        print("checking lr type")
        lval = self.current_node.type_search_up(name)
        expr = ctx.expr()
        if not expr:
            self._debug_print("Error: ctx.expr() is None!")
            return None
        rval = self.visit(expr)
        print(rval)
        rtype = type(rval)
        print(f"type: {lval} rtype: {rtype}")
        if  rtype!=lval:
            self.raiseError(ctx, f"{lval} '{name}' cannot be {rtype.__name__}")
        return rval

    def visitNumberAssign(self, ctx):
        self._debug_print(f"handling: {ctx.getText()}")
        name = ctx.IDENTIFIER().getText()
        self._debug_print(f"Assigning number: {name}")


        if not self.current_node.name_Exists_up(name):
            self.raiseError(ctx, f"Assignment of undeclared number '{name}'")
        value = self.l_r_type(ctx)

        self._debug_print(f"Evaluated value: {value}")
        self.current_node.add_var(name,value,Types.NUMBER)
        self._debug_print(f"Number assigned: {name} = {value}")

    def visitBoolAssign(self, ctx):
        print('visiting bool assign')
        name = ctx.IDENTIFIER().getText()
        if not self.current_node.name_Exists_up(name):
            self.raiseError(ctx, f"Assignment of undeclared number '{name}'")
        value = self.l_r_type(ctx)
        # except error:
        #     self.raiseError(ctx, f"invalid value for boolean '{name}'")

        if ctx.expr():
            try:
                value = bool(self.visit(ctx.expr()))
                print(f"xd {value}")
            except ValueError:
                self.raiseError(ctx, "expected sth convertible to boolean")
        elif ctx.exprComp():
            value = self.visit(ctx.exprComp())

        self.current_node.add_var(name, value,Types.BOOL)

        self._debug_print(f"Boolean assigned: {name} = {value}")
        return value

    def getVariableOfName(self,ctx,name):
        val = self.current_node.value_search_up(name)
        if val!=None:
            return val
        self.raiseError(ctx,f"variable of name {name} isn't initialized")

    def visitIncrement(self, ctx):
        name = ctx.IDENTIFIER().getText()
        self._debug_print(f"🆔 name: {name}")
        if not self.current_node.name_Exists_up:
            self.raiseError(ctx, f"Use of undeclared variable '{name}'")

        current_value = self.getVariableOfName(ctx,name)
        op = ctx.getChild(1).getText()
        if op in ('+=', '-='):
            value = self.visit(ctx.expr())
            if isinstance(current_value, int):
                delta = int(value)
                if op == '+=':
                    self._debug_print(f"🔄 {name} = {current_value} + {delta}")
                    self.current_node.scope[name].obj += delta
                else:
                    self._debug_print(f"🔄 {name} = {current_value} - {delta}")
                    self.current_node.scope[name].obj -= delta
            elif isinstance(current_value, Tile):
                if op == '+=':
                    self._debug_print(f"🧱 Dodaję do Tile: {name}.add_obj({value})")
                    self.current_node.add_var(name,value)
                else:
                    self._raise_error(f"❌ Tile nie obsługuje '-=': {name}")
            else:
                self._raise_error(f"❌ Nieobsługiwany typ dla {op}: {type(current_value).__name__}")
        elif op in ('++', '--'):
            if not isinstance(current_value, int):
                self._raise_error(f"❌ Operator '{op}' działa tylko na liczbach całkowitych")
            if op == '++':
                self._debug_print("++")
                self.current_node.scope[name].obj += 1
            else:
                self.current_node.scope[name].obj -= 1
            self._debug_print(f"🔢 {name} po '{op}': {self.current_node.scope[name].obj}")
        return self.getVariableOfName(ctx,name)

    def get_type_string(self, value):
        if isinstance(value, int) or isinstance(value, float):
            return "number"
        elif isinstance(value, bool):
            return "bool"
        elif isinstance(value, str):
            return "tile"
        elif isinstance(value,Road):
            return "road"
        elif isinstance(value,Tile):
            return "tile"
        elif isinstance(value,Blend):
            return "blend"
        else:
            return "unknown"
    def visitReasignment(self, ctx):
        self._debug_print("Reassignment detected")
        name = ctx.IDENTIFIER().getText()
        if not self.current_node.name_Exists_up(name):
            self.raiseError(ctx, f"Undeclared variable '{name}'")
        if ctx.expr():

            value = self.l_r_type(ctx)
            print(value)
           # value = self.visit(ctx.expr())
           #  previous_type = self.current_node.type_search_up(name)
           #  new_type = self.get_type_string(value)
           #  if  new_type != previous_type:
           #      self.raiseError(ctx, f"'reassignment of {previous_type} '{name}' to {new_type} you have to constrain to previous type!'")
            self.current_node.var_change_up(name,value)
            self._debug_print(f"Reassigned: {name} = {value}")
            return value
        else:
            self.raiseError(ctx, f"expression not resolved")

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
        if self.current_node.name_Exists_up(name):
            self.raiseError(ctx, f"variable '{name}' already exists!")
        self.current_node.add_var(name,None)

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
                if(self.current_node.name_Exists_up(arg)):
                    self.renderer.draw_tile(self.getVariableOfName(ctx,arg))
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
        # self._debug_print("fun decl")
        # function_name = ctx.IDENTIFIER().getText()
        # self._debug_print(function_name)
        #
        # params = []
        #
        # statements = ctx.statement()  # List of statements in the function body
        # self._debug_print(f"dir: {dir(ctx)}")
        #
        # for param in ctx.param():
        #     self._debug_print(param.type_().getText())
        #     self._debug_print(param.IDENTIFIER())
        #     # Store both TYPE and IDENTIFIER for each parameter
        #     param_type = param.type_().getText() # assuming TYPE is defined as 'number', 'tile', etc.
        #     param_identifier = param.IDENTIFIER().getText()
        #     params.append({'type': param_type, 'identifier': param_identifier})
        #
        # # Store the function definition
        # self.functions[function_name] = {
        #     'params': params,
        #     'statements': statements
        # }
        #
        # self._debug_print(f"Function '{function_name}' declared with parameters {params}")
        pass
    def get_type(self,ctx,type_str: str):
        print("entered ")
        type_map = {
            "number": Types.NUMBER,
            "bool": Types.BOOL,
            "tile": Types.TILE,
            "blend": Types.BLEND,
            "road": Types.ROAD,
        }
        if type_str not in type_map:
            self.raiseError(ctx,f"Unknown type: {type_str}")
        return type_map[type_str]
    def visitFunctionCall(self, ctx):
        self._debug_print("fun call")
        function_name = ctx.IDENTIFIER().getText()
        expr_list = [self.visit(expr) for expr in ctx.exprList().expr()] if ctx.exprList() else []

        if function_name == "print":
            self._debug_print(*expr_list)
            return None

        if function_name not in self.root.functions:
            self._raise_error(f"❌ Błąd: Funkcja '{function_name}' nie jest zadeklarowana!")

        function = self.root.functions[function_name]
        params = function['params']
        statements = function['statements']
        print("here")
        return_type = function['return_type']
        print({return_type})

        if len(expr_list) != len(params):
            self._raise_error(
                f"❌ Błąd: Funkcja '{function_name}' oczekuje {len(params)} argumentów, a otrzymała {len(expr_list)}!")
        self.enterScope()

        for param, value in zip(params, expr_list):
            param_identifier = param['identifier']
            param_type = param['type']

            lval = param_type
            rvalue = value
            rtype=type(value)
            print(f"type: {lval} rtype: {rtype}")
            if rtype != lval:
                self.raiseError(ctx, f"{lval} '{param_identifier}' cannot be {rtype.__name__}")
            self.current_node.add_type(param_identifier, param_type)
            self.current_node.add_var(param_identifier, value)

        try:
            for stmt in statements:
                self.visit(stmt)
        except ReturnValue as rv:
            self.exitScope()
            value = rv.value
            fun_value = return_type
            val_type = type(value)
            if return_type!=val_type:
                self.raiseError(ctx,f"return type '{val_type.__name__}' should be function return type: '{fun_value.__name__}'")
            return value
        self.exitScope()
        return None



    def visitReturnStatement(self, ctx):
        value = self.visit(ctx.expr()) if ctx.expr() else None
        raise ReturnValue(value)
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
            return int(left / right)
        else:
            raise RuntimeError(f"Unknown operator: {op}")
    def visitExprParens(self, ctx):
        self._debug_print("Processing parenthesized expression")
        return self.visit(ctx.expr())

    def visitExprVar(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        #self._debug_print(f"Processing variable reference: {var_name}: value: {self.variables.get(var_name)}")
        if not self.current_node.name_Exists_up(var_name):
            self.raiseError(ctx, f"Use of undeclared variable '{var_name}'")
        return self.getVariableOfName(ctx,var_name)

    def visitExprInt(self, ctx):
        value = int(ctx.INT().getText())
        self._debug_print(f"Processing integer literal: {value}")
        return value

    def visitExprBool(self, ctx):
        print("looking at bool in expr")
        value = ctx.BOOL().getText().lower() == 'true'
        self._debug_print(f"Processing boolean literal: {value}")
        return value



    # Visit a parse tree produced by MapperParser#roadStart.
    def visitRoadStart(self, ctx: MapperParser.RoadStartContext):
        name = ctx.IDENTIFIER().getText()
        self._debug_print(f"Starting road: {name}")
        self.current_node.add_var(name, Road(Position(self.renderer.pointer_x, self.renderer.pointer_y)),Types.ROAD)


    # Visit a parse tree produced by MapperParser#roadEnd.
    def visitRoadEnd(self, ctx: MapperParser.RoadEndContext):
        name = ctx.IDENTIFIER().getText()
        self._debug_print(f"Ending road {name}")
        if not self.current_node.name_Exists_up:
            self.raiseError(ctx,f"road '{name}' doesnt have a starting point!")
        else:
            pos = Position(self.renderer.pointer_x, self.renderer.pointer_y)
            self.current_node.end_road_up(name,pos,self.renderer)


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
        var_listener.root.reset_scope_counter()
        # print("Registered variables:", var_listener.var_types)  # Debugowanie

        # Sprawdzenie błędów redeklaracji
        if var_listener.errors:
            for error in var_listener.errors:
                print(error)
            sys.exit(1)

        # Drugi przebieg: interpretacja programu
        interpreter = MapperInterpreter(var_listener.root)
        interpreter.visit(tree)

        # print("Starting Pygame loop...")
        interpreter.renderer.run()

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

