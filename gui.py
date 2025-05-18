import os
import sys
import threading
import tempfile
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from MapperLexer import MapperLexer
from MapperParser import MapperParser
from MapperListener import MapperListener
from MapperInterpreter import MapperInterpreter
from ErrorListener import MapperErrorListener
from MapperInterpreter import VariableDeclarationListener
import pygame

# GUI Application
class MapEditorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Map Editor")
        self.geometry("1680x804")

        # Paned layout
        paned = tk.PanedWindow(self, sashrelief=tk.RAISED, sashwidth=4)
        paned.pack(fill=tk.BOTH, expand=1)

        # Left frame: code editor + run button + logs
        left_frame = tk.Frame(paned)
        paned.add(left_frame, width=400)

        tk.Label(left_frame, text=".map Code").pack()
        self.code_editor = ScrolledText(left_frame, height=20)
        self.code_editor.pack(fill=tk.BOTH, expand=1)

        self.run_button = tk.Button(left_frame, text="Run", command=self.on_run)
        self.run_button.pack(fill=tk.X)

        tk.Label(left_frame, text="Logs").pack()
        self.log_console = ScrolledText(left_frame, height=10, state=tk.DISABLED)
        self.log_console.pack(fill=tk.BOTH, expand=1)

        # Right frame: pygame canvas
        right_frame = tk.Frame(paned)
        paned.add(right_frame, width=1280)

        self.map_frame = tk.Frame(right_frame, width=1280, height=804)
        self.map_frame.pack(fill=tk.BOTH, expand=1)
        self.map_frame.update()

        # Embed pygame display
        os.environ['SDL_WINDOWID'] = str(self.map_frame.winfo_id())
        if sys.platform.startswith('win'):
            os.environ['SDL_VIDEODRIVER'] = 'windib'
        pygame.init()
        from MapperRenderer import MapperRenderer
        # Initialize only once
        self.renderer = MapperRenderer()

        # Start the pygame event loop in a thread
    def update_pygame(self):
        self.renderer.process_events()
        self.after(10, self.update_pygame) 

    def log(self, message):
        self.log_console.configure(state=tk.NORMAL)
        self.log_console.insert(tk.END, message + "\n")
        self.log_console.configure(state=tk.DISABLED)
        self.log_console.see(tk.END)

    def on_run(self):
        # Write current code to temp file
        self.log_console.configure(state=tk.NORMAL)
        self.log_console.delete('1.0', tk.END)
        self.log_console.configure(state=tk.DISABLED)


        code = self.code_editor.get('1.0', tk.END)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.map')
        tmp.write(code.encode('utf-8'))
        tmp.flush()
        tmp.close()

        # parse and interpret
        def task():
            try:
                # Reset renderer map to initial state
                input_stream = FileStream(tmp.name)

                lexer = MapperLexer(input_stream)
                token_stream = CommonTokenStream(lexer)
                
                parser = MapperParser(token_stream)
                parser.removeErrorListeners()
                parser.addErrorListener(MapperErrorListener())
                tree = parser.program()

                var_listener = VariableDeclarationListener()
                walker = ParseTreeWalker()
                walker.walk(var_listener, tree)
                var_listener.exitScope()
                if var_listener.errors:
                    for error in var_listener.errors:
                        # print to console
                        self.log(f"Error: {error}")
                    return

                interpreter = MapperInterpreter(var_listener.root, renderer=self.renderer, logger=self)
                self.renderer.reset_map()  # Reset map before interpreting
                interpreter.visit(tree)
            except Exception as e:
                self.log(f"Error: {e}")

        threading.Thread(target=task, daemon=True).start()

if __name__ == '__main__':
    app = MapEditorApp()
    app.mainloop()
