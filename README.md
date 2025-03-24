# Kompilatory

# Uruchamianie gramatyki w ANTLR - wybór jednej z opcji:
# Jeśli masz alias 'antlr4':
antlr4 -Dlanguage=Python3 -visitor Mapper.g4

# Jeśli nie masz aliasu, użyj pełnej ścieżki:
java -jar C:\antlr\antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor Mapper.g4

# Uruchamianie skryptu Python - wybór jednej z opcji:
# Jeśli system wymaga użycia 'python3' (np. na systemach Linux/MacOS):
python3 MapperInterpreter.py example.map

# Jeśli masz Pythona 3 ustawionego domyślnie, użyj:
## python MapperInterpreter.py example.map
## py MapperInterpreter.py example.map


# Instalacja pygame:
# Użyj 'pip3' jeśli masz zainstalowanego Pythona 3:
pip3 install pygame

# Użyj 'pip' jeśli masz zainstalowanego Pythona 3 jako domyślną wersję:
pip install pygame

