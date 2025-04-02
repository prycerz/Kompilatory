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
        self.variables = {}  
        self.functions = {}  
        self.renderer = MapperRenderer()
        self.roads = {}
        self.errors = []  

    backgroundObjects = ['grass', 'soil', 'sand', 'water', 'rocks']
    foregroundObjects = ['tree', 'bush', 'stones', 'mountain', 'cabin', 'church']

    def report_error(self, message):
        """Dodaje błąd do listy i wypisuje go od razu."""
        error_msg = f"❌ Błąd: {message}"
        self.errors.append(error_msg)
        print(error_msg)
 
    def visitTileSum(self, ctx):
        print("Visiting tile sum...")
        tile = Tile()
        
        if not ctx.IDENTIFIER():
            self.report_error("Brak obiektów w definicji sumy kafelków")
        
        for arg in ctx.IDENTIFIER():
            obj = arg.getText()
    
            if obj not in self.backgroundObjects and obj not in self.foregroundObjects:
                self.report_error(f"Nieznany obiekt '{obj}' w definicji kafelka")
            tile.add_obj(obj)  
        
        return tile
    
    def visitTileAssign(self, ctx):
     
        print('tile assign')
       
        if not ctx.IDENTIFIER():
            self.report_error("Brak nazwy zmiennej w przypisaniu kafelka")
            return
        
        name = ctx.IDENTIFIER().getText()
        
        if name in self.variables and not isinstance(self.variables[name], Tile):
            self.report_error(f"Nazwa '{name}' jest już używana dla zmiennej innego typu niż 'tile'")
        
        tile = self.visitTileSum(ctx.tileSum())  
        
        if tile is None:
            self.report_error(f"Nie udało się utworzyć kafelka dla zmiennej '{name}'")
        
        self.variables[name] = tile  

    def visitBlendAssign(self, ctx):
        try:
            print('visted blend assign')
            blend_name = ctx.IDENTIFIER().getText()  
            blend_options = []  

            print(f"figuretext: {ctx.figure().getText()}")  

            if ctx.figure().getText().startswith('circle'): 
                radius = int(ctx.figure().INT(0).getText())
                figure = Figure('circle', {'radius': radius})

            elif ctx.figure().getText().startswith('rectangle'):
                width = int(ctx.figure().INT(0).getText())
                height = int(ctx.figure().INT(1).getText())
                figure = Figure('rectangle', {'width': width, 'height': height})
            else:
                raise RuntimeError("❌ Błąd: Nieznany typ figury!")

            for option_ctx in ctx.blendOption():
                try:
                    if(option_ctx.tileSum()):
                        tile = self.visitTileSum(option_ctx.tileSum())

                    elif (option_ctx.IDENTIFIER()):
                        identifier = option_ctx.IDENTIFIER().getText()
                        if(identifier in self.variables and isinstance(self.variables[identifier], Tile)):
                            tile = self.variables[identifier]
                        else:
                            tile = Tile([identifier])
                    else:
                        raise RuntimeError("❌ Błąd: Nieznany typ opcji blendu!")
                    
                    percentage = int(option_ctx.INT().getText())
                    if percentage < 0:
                        raise RuntimeError(f"❌ Błąd: Ujemny procent ({percentage}) nie jest dozwolony!")
                    blend_options.append((tile, percentage))
                except AttributeError as e:
                    print(f"AttributeError in blendOption loop: {e}")
                    continue
                except ValueError as e:
                    print(f"ValueError in blendOption loop: {e}")
                    continue
                except RuntimeError as e:
                    print(f"RuntimeError in blendOption loop: {e}")
                    raise  
                except Exception as e:
                    print(f"Unexpected error in blendOption loop: {e}")
                    continue

            self.variables[blend_name] = Blend(figure, blend_options)  
        except AttributeError as e:
            print(f"AttributeError in visitBlendAssign: {e}")
        except ValueError as e:
            print(f"ValueError in visitBlendAssign: {e}")
        except TypeError as e:
            print(f"TypeError in visitBlendAssign: {e}")
        except RuntimeError as e:
            print(f"RuntimeError: {e}")
            raise  
        except Exception as e:
            print(f"Unexpected error in visitBlendAssign: {e}")
    
    def visitVarAssign(self, ctx:MapperParser.VarAssignContext):
        print("handling var assignment")
        
        if not ctx.IDENTIFIER():
            raise RuntimeError("❌ Błąd: Brak nazwy zmiennej w przypisaniu")
        
        name = ctx.IDENTIFIER().getText()
        
        if name not in self.variables:
            raise RuntimeError(f"❌ Błąd: Zmienna '{name}' nie została zadeklarowana!")
        
        op = ctx.getChild(1).getText()
        if op != '=':
            self.report_error(f"Nieoczekiwany operator '{op}' w przypisaniu zmiennej '{name}' – oczekiwano '='")
        
        expr = ctx.expr()
        if not expr:
            raise RuntimeError(f"❌ Błąd: Brak wyrażenia w przypisaniu zmiennej '{name}'")
        
        print(f"{name} {op} {expr}")
        
        try:
            expr_value = self.visit(expr)
        except Exception as e:
            raise RuntimeError(f"❌ Błąd: Nie udało się obliczyć wyrażenia dla zmiennej '{name}': {str(e)}")
        
        print(f"expr v{expr_value}")
        
        if expr_value is not None and name in self.variables:
            current_type = type(self.variables[name])
            new_type = type(expr_value)
            if current_type != new_type:
                self.report_error(f"Przypisanie wartości typu '{new_type.__name__}' do zmiennej '{name}' typu '{current_type.__name__}'")
        
        if expr_value is None:
            self.report_error(f"Wartość wyrażenia dla zmiennej '{name}' jest None")
        
        self.variables[name] = expr_value


    def visitNumberAssign(self, ctx):
        print(f"handling: {ctx.getText()}")
        
        if not ctx.IDENTIFIER():
            raise RuntimeError("❌ Błąd: Brak nazwy zmiennej w przypisaniu typu 'number'")
        
        name = ctx.IDENTIFIER().getText()
        
        if name in self.variables and not isinstance(self.variables[name], (int, float)):
            self.report_error(f"Nazwa '{name}' jest już używana dla zmiennej innego typu niż 'number'")
        
        expr = ctx.expr()
        if not expr:
            raise RuntimeError(f"❌ Błąd: Brak wyrażenia w przypisaniu zmiennej '{name}' typu 'number'")
        
       
        try:
            value = self.visit(expr)
        except Exception as e:
            raise RuntimeError(f"❌ Błąd: Nie udało się obliczyć wyrażenia dla zmiennej '{name}': {str(e)}")
        
        if value is not None and not isinstance(value, (int, float)):
            self.report_error(f"Wartość dla zmiennej '{name}' typu 'number' powinna być liczbą, a jest typu '{type(value).__name__}'")
        
        if value is None:
            self.report_error(f"Wartość wyrażenia dla zmiennej '{name}' jest None")
        
        print(f"Evaluated value: {value}")
        self.variables[name] = value
        print(f"Number assigned: {name} = {value}")

    def visitBoolAssign(self, ctx):
    
        if not ctx.IDENTIFIER():
            raise RuntimeError("❌ Błąd: Brak nazwy zmiennej w przypisaniu typu 'bool'")
        
        name = ctx.IDENTIFIER().getText()
        
        if name in self.variables and not isinstance(self.variables[name], bool):
            self.report_error(f"Nazwa '{name}' jest już używana dla zmiennej innego typu niż 'bool'")
        
        if not ctx.expr():
            raise RuntimeError(f"❌ Błąd: Brak wyrażenia w przypisaniu zmiennej '{name}' typu 'bool'")
        
        try:
            value = self.visit(ctx.expr())
        except Exception as e:
            raise RuntimeError(f"❌ Błąd: Nie udało się obliczyć wyrażenia dla zmiennej '{name}': {str(e)}")
        
        if value is not None and not isinstance(value, bool):
            self.report_error(f"Wartość dla zmiennej '{name}' typu 'bool' powinna być typu bool, a jest typu '{type(value).__name__}'")
        
        if value is None:
            self.report_error(f"Wartość wyrażenia dla zmiennej '{name}' jest None")
        
        self.variables[name] = value
        print(f"Boolean assigned: {name} = {value}")
        return value

    def visitIncrement(self, ctx):
      
        if not ctx.IDENTIFIER():
            raise RuntimeError("❌ Błąd: Brak nazwy zmiennej w operacji inkrementacji")
        
        name = ctx.IDENTIFIER().getText()
        print(f"name {name}")
        
        if not ctx.expr():
            raise RuntimeError(f"❌ Błąd: Brak wyrażenia w operacji inkrementacji dla zmiennej '{name}'")
        
        try:
            value = self.resolve_if_variable_number(ctx.expr())
        except Exception as e:
            raise RuntimeError(f"❌ Błąd: Nie udało się obliczyć wartości dla inkrementacji zmiennej '{name}': {str(e)}")
        
        if name not in self.variables:
            raise RuntimeError(f"❌ Błąd: Nieznana zmienna '{name}'!")
        
        if value is None:
            self.report_error(f"Wartość wyrażenia dla inkrementacji zmiennej '{name}' jest None")
        
        if isinstance(self.variables[name], int):
            if not isinstance(value, (int, float)):
                self.report_error(f"Wartość '{value}' dla inkrementacji zmiennej '{name}' typu int powinna być liczbą")
            else:
                print(f"🔄 Aktualizuję {name}: {int(self.variables[name])} += {int(value)}")
                self.variables[name] += int(value)  
        
        print(self.variables[name])
        
        if isinstance(self.variables[name], Tile):
            if value not in self.backgroundObjects and value not in self.foregroundObjects:
                self.report_error(f"Nieznany obiekt '{value}' w inkrementacji kafelka '{name}'")
            try:
                self.variables[name].add_obj(value)
            except Exception as e:
                self.report_error(f"Nie udało się dodać obiektu '{value}' do kafelka '{name}': {str(e)}")
        
        if not isinstance(self.variables[name], (int, Tile)):
            self.report_error(f"Zmienna '{name}' typu '{type(self.variables[name]).__name__}' nie obsługuje operacji += ")
        
        return self.variables[name]


    def visitAssignment(self, ctx):
        print("⚠️ Visiting assignment...") 
        
        if ctx is None:
            raise RuntimeError("❌ Błąd: Brak kontekstu dla operacji przypisania")
        
        if ctx.tileAssign():
            print("✅ Tile assignment detected!")
            try:
                result = self.visitTileAssign(ctx.tileAssign())
                if result is None:
                    self.report_error("Przypisanie typu 'tile' zwróciło None")
                return result
            except Exception as e:
                raise RuntimeError(f"❌ Błąd w przypisaniu typu 'tile': {str(e)}")
        
        elif ctx.numberAssign():
            print("✅ Number assignment detected!")
            try:
                result = self.visitNumberAssign(ctx.numberAssign())
                if result is None:
                    self.report_error("Przypisanie typu 'number' zwróciło None")
                return result
            except Exception as e:
                raise RuntimeError(f"❌ Błąd w przypisaniu typu 'number': {str(e)}")
        
        elif ctx.boolAssign():
            print("✅ Boolean assignment detected!")
            try:
                result = self.visitBoolAssign(ctx.boolAssign())
                if result is None:
                    self.report_error("Przypisanie typu 'bool' zwróciło None")
                return result
            except Exception as e:
                raise RuntimeError(f"❌ Błąd w przypisaniu typu 'bool': {str(e)}")
        
        elif ctx.increment():
            print("✅ Increament assignment detected!")
            try:
                result = self.visitIncrement(ctx.increment())
                if result is None:
                    self.report_error("Operacja inkrementacji zwróciła None")
                return result
            except Exception as e:
                raise RuntimeError(f"❌ Błąd w operacji inkrementacji: {str(e)}")
        
        elif ctx.blendAssign():
            print("✅ Blend assignment detected!")
            try:
                result = self.visitBlendAssign(ctx.blendAssign())
                if result is None:
                    self.report_error("Przypisanie typu 'blend' zwróciło None")
                return result
            except Exception as e:
                raise RuntimeError(f"❌ Błąd w przypisaniu typu 'blend': {str(e)}")
        
        elif ctx.varAssign():
            try:
                result = self.visitVarAssign(ctx.varAssign())
                if result is None:
                    self.report_error("Przypisanie zmiennej zwróciło None")
                return result
            except Exception as e:
                raise RuntimeError(f"❌ Błąd w przypisaniu zmiennej: {str(e)}")
        
        else:
            self.report_error(f"Nieznany typ przypisania: {ctx.getText()}")
            print("❌ Unknown assignment type!")
            return None 

    def visitMove(self, ctx):
       
        if ctx is None:
            raise RuntimeError("❌ Błąd: Brak kontekstu dla operacji przesunięcia")
        
        if ctx.getChildCount() < 2 or not ctx.getChild(1):
            raise RuntimeError("❌ Błąd: Brak kierunku w operacji przesunięcia")
        
        direction = ctx.getChild(1).getText()
        
        valid_directions = ['up', 'down', 'left', 'right']
        if direction not in valid_directions:
            raise RuntimeError(f"❌ Błąd: Nieznany kierunek '{direction}' – oczekiwano 'up', 'down', 'left' lub 'right'")
        
        if ctx.getChildCount() < 3 or not ctx.getChild(2):
            raise RuntimeError(f"❌ Błąd: Brak wartości przesunięcia dla kierunku '{direction}'")
        
        value_expr = ctx.getChild(2)
        
        try:
            value = self.visit(value_expr)
        except Exception as e:
            raise RuntimeError(f"❌ Błąd: Nie udało się obliczyć wartości przesunięcia dla kierunku '{direction}': {str(e)}")
        
        if value is None:
             raise RuntimeError(f"❌ Błąd: Wartość przesunięcia dla kierunku '{direction}' jest None")
        
        if not isinstance(value, (int, float)):
            self.report_error(f"Wartość przesunięcia '{value}' dla kierunku '{direction}' powinna być liczbą, a jest typu '{type(value).__name__}'")
            value = 0 
      
        try:
            if direction == 'up':
                self.renderer.move_pointer(0, -value)
            elif direction == 'down':
                self.renderer.move_pointer(0, value)
            elif direction == 'left':
                self.renderer.move_pointer(-value, 0)
            elif direction == 'right':
                self.renderer.move_pointer(value, 0)
        except Exception as e:
            self.report_error(f"Nie udało się przesunąć wskaźnika w kierunku '{direction}' o wartość '{value}': {str(e)}")
        
        print(f"Pointer moved {direction} by {value}. New position: ({self.renderer.pointer_x}, {self.renderer.pointer_y})")

    def visitDraw(self, ctx):
        print("drawing..")
       
        if ctx is None:
            raise RuntimeError("❌ Błąd: Brak kontekstu dla polecenia rysowania")
        
        if ctx.IDENTIFIER():
            print("ctx")
            args = []
            counter = 0
            while(ctx.IDENTIFIER(counter)):
                arg = ctx.IDENTIFIER(counter).getText()
                args.append(arg)
                counter += 1
            
            if not args:
                self.report_error("Brak argumentów w poleceniu rysowania z identyfikatorami")
            
            for arg in args:
                if arg in self.variables:
                    try:
                        self.renderer.draw_tile(self.variables[arg])
                        return
                    except Exception as e:
                        raise RuntimeError(f"❌ Błąd: Nie udało się narysować zmiennej '{arg}': {str(e)}")
           
            for arg in args:
                if arg not in self.backgroundObjects and arg not in self.foregroundObjects:
                    self.report_error(f"Nieznany obiekt '{arg}' w poleceniu rysowania")
            
            try:
                self.renderer.draw_tile(Tile(args=args))
            except Exception as e:
                raise RuntimeError(f"❌ Błąd: Nie udało się narysować kafelka z argumentami {args}: {str(e)}")

        elif ctx.INT():  
            if not ctx.INT():
                raise RuntimeError("❌ Błąd: Brak promienia w poleceniu rysowania")
            
            try:
                radius = int(ctx.INT().getText())
                if radius <= 0:
                    self.report_error(f"Promień w poleceniu rysowania musi być dodatni (podano: {radius})")
            except ValueError:
                raise RuntimeError(f"❌ Błąd: Nieprawidłowa wartość promienia: {ctx.INT().getText()}")
            
            percentages = []
            if not ctx.percentagePair():
                raise RuntimeError("❌ Błąd: Brak par procent-kafelek w poleceniu rysowania z promieniem")
            
            for pair in ctx.percentagePair():
                if not pair.INT():
                    raise RuntimeError("❌ Błąd: Brak wartości procentowej w parze dla promienia")
                if not pair.IDENTIFIER():
                    raise RuntimeError("❌ Błąd: Brak typu kafelka w parze dla promienia")
                
                try:
                    percent = int(pair.INT().getText())
                    if percent < 0:
                        self.report_error(f"Ujemna wartość procentowa ({percent}%) w poleceniu rysowania")
                except ValueError:
                    raise RuntimeError(f"❌ Błąd: Nieprawidłowa wartość procentowa: {pair.INT().getText()}")
                
                tile_type = pair.IDENTIFIER().getText()
              
                if tile_type not in self.variables and tile_type not in self.backgroundObjects and tile_type not in self.foregroundObjects:
                    self.report_error(f"Nieznany kafelek lub obiekt '{tile_type}' w poleceniu rysowania z promieniem")
                
                percentages.append((percent, tile_type))
            
            total_percent = sum(p for p, _ in percentages)
            if total_percent != 100:
                self.report_error(f"Suma procentów w poleceniu rysowania wynosi {total_percent}%, a powinna wynosić 100%")
            
            print(f"Drawing radius {radius} with: {percentages}")
            try:
                blend = Blend(radius, percentages)
                self.renderer.draw_tile(blend)
            except Exception as e:
                raise RuntimeError(f"❌ Błąd: Nie udało się narysować blendu z promieniem {radius} i procentami {percentages}: {str(e)}")
        
        else:
            self.report_error(f"Nieprawidłowe polecenie rysowania: {ctx.getText()}")
            print("ERROR: Invalid draw command!")

    def visitErrorHandling(self, ctx):
        message = ctx.STRING().getText()
        print(f"Error: {message}")
    
    def visitWhileLoop(self, ctx):
        print("Handling while loop")
     
        if ctx is None:
            raise RuntimeError("❌ Błąd: Brak kontekstu dla pętli 'while'")
     
        condition_expr = ctx.expr()
        if not condition_expr:
            raise RuntimeError("❌ Błąd: Brak warunku w pętli 'while'")
        
        print(f"Loop condition: {condition_expr.getText()}")
    
        while True:
            try:
                condition_value = self.visit(condition_expr)
            except Exception as e:
                raise RuntimeError(f"❌ Błąd: Nie udało się ocenić warunku pętli 'while': {str(e)}")
            
            if condition_value is None:
                self.report_error("Warunek pętli 'while' zwrócił None – traktowany jako False")
                break
            if not isinstance(condition_value, bool):
                self.report_error(f"Warunek pętli 'while' powinien być typu bool, a jest typu '{type(condition_value).__name__}'")
            
            if not condition_value:
                break
            
            print("Loop body execution...")
            
            for stmt in ctx.statement():
                if not stmt:
                    self.report_error("Pusta instrukcja w ciele pętli 'while'")
                    continue
                print(f"Executing statement: {stmt.getText()}")
                try:
                    self.visit(stmt) 
                except Exception as e:
                    self.report_error(f"Nie udało się wykonać instrukcji w pętli 'while': {str(e)}")
        
        print("Exiting loop")

    def visitForLoop(self, ctx):
        print("Handling for loop")
      
        if ctx is None:
            raise RuntimeError("❌ Błąd: Brak kontekstu dla pętli 'for'")
     
        number_assign = ctx.numberAssign()
        if not number_assign:
            raise RuntimeError("❌ Błąd: Brak inicjalizacji w pętli 'for'")
        try:
            self.visit(number_assign)  
        except Exception as e:
            raise RuntimeError(f"❌ Błąd: Nie udało się wykonać inicjalizacji pętli 'for': {str(e)}")
        print(f"Initialized: {number_assign.getText()}")

        condition_expr = ctx.expr()
        if not condition_expr:
            raise RuntimeError("❌ Błąd: Brak warunku w pętli 'for'")
        print(f"Loop condition: {condition_expr.getText()}")

        increment_expr = ctx.increment()
        if not increment_expr:
            raise RuntimeError("❌ Błąd: Brak wyrażenia inkrementacji w pętli 'for'")
        print(f"Increment expression: {increment_expr.getText()}")

        while True:
            try:
                condition_value = self.visit(condition_expr) 
            except Exception as e:
                raise RuntimeError(f"❌ Błąd: Nie udało się ocenić warunku pętli 'for': {str(e)}")
          
            if condition_value is None:
                self.report_error("Warunek pętli 'for' zwrócił None – traktowany jako False")
                break
            if not isinstance(condition_value, bool):
                self.report_error(f"Warunek pętli 'for' powinien być typu bool, a jest typu '{type(condition_value).__name__}'")
            
            if not condition_value:
                break
            
            print("Loop body execution...")
           
            for stmt in ctx.statement():
                if not stmt:
                    self.report_error("Pusta instrukcja w ciele pętli 'for'")
                    continue
                print(f"Executing statement: {stmt.getText()}")
                try:
                    self.visit(stmt) 
                except Exception as e:
                    self.report_error(f"Nie udało się wykonać instrukcji w pętli 'for': {str(e)}")
  
            try:
                self.visit(increment_expr)
            except Exception as e:
                self.report_error(f"Nie udało się wykonać inkrementacji w pętli 'for': {str(e)}")
            print(f"Increment executed: {increment_expr.getText()}")
            
        print("Exiting for loop")

    def visitLoop(self, ctx):
   
        if ctx is None:
            raise RuntimeError("❌ Błąd: Brak kontekstu dla pętli")
        
        if ctx.forLoop():
            try:
                result = self.visitForLoop(ctx.forLoop())
                if result is None:
                    self.report_error("Pętla 'for' zwróciła None")
                return result
            except Exception as e:
                raise RuntimeError(f"❌ Błąd w pętli 'for': {str(e)}")
        
        elif ctx.whileLoop():
            try:
                result = self.visitWhileLoop(ctx.whileLoop())
                if result is None:
                    self.report_error("Pętla 'while' zwróciła None")
                return result
            except Exception as e:
                raise RuntimeError(f"❌ Błąd w pętli 'while': {str(e)}")
        
        else:
            self.report_error(f"Nieznany typ pętli: {ctx.getText()}")
            return None

    def visitRoadPlacement(self, ctx):
        if(ctx.roadStart()):
            return self.visitRoadStart(ctx.roadStart())
        elif(ctx.roadEnd()):
            return self.visitRoadEnd(ctx.roadEnd())

    def visitConditional(self, ctx:MapperParser.ConditionalContext):
        print(f"Handling if statement: {ctx.getText()}")  

        condition_value = self.visit(ctx.expr())  
        print(f"Condition evaluated to: {condition_value}")

        if condition_value:
            print("Executing if branch...")
            statements = ctx.statement()  
            print(f"Statements inside if: {len(statements)}")

            for statement_ctx in statements:
                print(f"Visiting statement: {statement_ctx.getText()}")
                self.visit(statement_ctx)

        print("Exiting if statement")

    def visitFunctionDecl(self, ctx):
        try:
            print("fun decl")
            function_name = ctx.IDENTIFIER().getText()
            print(function_name)

            params = []

            statements = ctx.statement()  
            print(f"dir: {dir(ctx)}")

            for param in ctx.param():
                print(param.type_().getText())
                print(param.IDENTIFIER())
                param_type = param.type_() 
                param_identifier = param.IDENTIFIER().getText()
                params.append({'type': param_type, 'identifier': param_identifier})

            self.functions[function_name] = {
                'params': params,
                'statements': statements
            }

            print(f"Function '{function_name}' declared with parameters {params}")
        except AttributeError as e:
            print(f"AttributeError in visitFunctionDecl: {e}")
        except TypeError as e:
            print(f"TypeError in visitFunctionDecl: {e}")
        except Exception as e:
            print(f"Unexpected error in visitFunctionDecl: {e}")

    def visitFunctionCall(self, ctx):
        try:
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

            local_vars = {}
            for param, expr in zip(params, expr_list):
                print(f"expr: {expr}")
                param_identifier = param['identifier']
                param_type = param['type']

                local_vars[param_identifier] = expr

            original_vars = self.variables
            self.variables = original_vars.copy()
            self.variables.update(local_vars)

            result = None
            for stmt in statements:
                result = self.visit(stmt)

            self.variables = original_vars
            return result
        except RuntimeError as e:
            print(f"RuntimeError: {e}")
            raise  
        except AttributeError as e:
            print(f"AttributeError in visitFunctionCall: {e}")
            return None
        except TypeError as e:
            print(f"TypeError in visitFunctionCall: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error in visitFunctionCall: {e}")
            return None

    def visitExprComp(self, ctx):
        try:
            print("Processing comparison expression")
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.children[1].getText()
        except AttributeError as e:
            print(f"AttributeError in visitExprComp: {e}")
            return None
        except IndexError as e:
            print(f"IndexError in visitExprComp: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error in visitExprComp: {e}")
            return None

    def visitExprAddSub(self, ctx):
        try:
            print("Processing addition/subtraction expression")
            left = self.visit(ctx.expr(0))  
            right = self.visit(ctx.expr(1))  
            op = ctx.children[1].getText()  

            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            else:
                raise RuntimeError(f"Unknown operator: {op}")
        except AttributeError as e:
            print(f"AttributeError in visitExprAddSub: {e}")
            return None
        except TypeError as e:
            print(f"TypeError in visitExprAddSub: {e}")
            return None
        except IndexError as e:
            print(f"IndexError in visitExprAddSub: {e}")
            return None
        except RuntimeError as e:
            print(f"RuntimeError: {e}")
            raise  
        except Exception as e:
            print(f"Unexpected error in visitExprAddSub: {e}")
            return None

    def visitExprMulDiv(self, ctx):
        try:
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
        except AttributeError as e:
            print(f"AttributeError in visitExprMulDiv: {e}")
            return None
        except TypeError as e:
            print(f"TypeError in visitExprMulDiv: {e}")
            return None
        except IndexError as e:
            print(f"IndexError in visitExprMulDiv: {e}")
            return None
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError in visitExprMulDiv: {e}")
            return None
        except RuntimeError as e:
            print(f"RuntimeError: {e}")
            raise  
        except Exception as e:
            print(f"Unexpected error in visitExprMulDiv: {e}")
            return None

    def visitExprParens(self, ctx):
        try:
            print("Processing parenthesized expression")
            return self.visit(ctx.expr())
        except AttributeError as e:
            print(f"AttributeError in visitExprParens: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error in visitExprParens: {e}")
            return None

    def visitExprVar(self, ctx):
        try:
            var_name = ctx.IDENTIFIER().getText()
            print(f"Processing variable reference: {var_name}: value: {self.variables.get(var_name)}")
            return self.variables.get(var_name)
        except AttributeError as e:
            print(f"AttributeError in visitExprVar: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error in visitExprVar: {e}")
            return None

    def visitExprInt(self, ctx):
        try:
            value = int(ctx.INT().getText())
            print(f"Processing integer literal: {value}")
            return value
        except AttributeError as e:
            print(f"AttributeError in visitExprInt: {e}")
            return None
        except ValueError as e:
            print(f"ValueError in visitExprInt: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error in visitExprInt: {e}")
            return None

    def visitExprBool(self, ctx):
        try:
            value = ctx.BOOL().getText().lower() == 'true'
            print(f"Processing boolean literal: {value}")
            return value
        except AttributeError as e:
            print(f"AttributeError in visitExprBool: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error in visitExprBool: {e}")
            return None

    def visitRoadStart(self, ctx: MapperParser.RoadStartContext):
        try:
            name = ctx.IDENTIFIER().getText()
            if name in self.variables.keys():
                print("this must be a new road")
            else:
                print(f"Starting road: {name}")
                self.variables[name] = Road(Position(self.renderer.pointer_x , self.renderer.pointer_y))
        except AttributeError as e:
            print(f"AttributeError in visitRoadStart: {e}")
        except TypeError as e:
            print(f"TypeError in visitRoadStart: {e}")
        except Exception as e:
            print(f"Unexpected error in visitRoadStart: {e}")

    def visitRoadEnd(self, ctx: MapperParser.RoadEndContext):
        try:
            name = ctx.IDENTIFIER().getText()
            print(f"Ending road {name}")
            if name not in self.variables.keys():
                print("the road you are refering to doesnt exist")
            else:
                self.variables[name].end(Position(self.renderer.pointer_x, self.renderer.pointer_y), self.renderer)
        except AttributeError as e:
            print(f"AttributeError in visitRoadEnd: {e}")
        except TypeError as e:
            print(f"TypeError in visitRoadEnd: {e}")
        except Exception as e:
            print(f"Unexpected error in visitRoadEnd: {e}")

if __name__ == "__main__":
    try:
        input_stream = FileStream(sys.argv[1])
        lexer = MapperLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = MapperParser(token_stream)
        tree = parser.program()
        
        interpreter = MapperInterpreter()
        interpreter.visit(tree)

        print("Starting Pygame loop...")
        interpreter.renderer.run()
    except IndexError as e:
        print(f"IndexError: {e} - Prawdopodobnie nie podano argumentu z nazwą pliku wejściowego")
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e} - Nie znaleziono pliku wejściowego")
    except AttributeError as e:
        print(f"AttributeError: {e} - Problem z dostępem do atrybutów (np. parser, interpreter lub renderer)")
    except SyntaxError as e:
        print(f"SyntaxError: {e} - Błąd składni w pliku wejściowym")
    except TypeError as e:
        print(f"TypeError: {e} - Nieprawidłowy typ danych w procesie parsowania lub interpretacji")
    except ImportError as e:
        print(f"ImportError: {e} - Brak wymaganych modułów (np. ANTLR, Pygame)")
    except Exception as e:
        print(f"Unexpected error: {e} - Nieoczekiwany błąd podczas uruchamiania interpretera")
