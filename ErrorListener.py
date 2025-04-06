import re
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

class MapperErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Domyślna wiadomość błędu
        error_msg = f"SyntaxError: line {line}: column {column} - {msg}"
        current_token = offendingSymbol.text if offendingSymbol else ""

        # 1. Nieprawidłowa składnia (np. brak argumentu przed operatorem lub ujemne procenty)
        if "no viable alternative at input" in msg:
            match = re.search(r"['](.*?)[']", msg)
            token = match.group(1) if match else current_token
            # Specjalna obsługa ujemnych procentów w blendzie
            if "blend" in str(recognizer.getRuleInvocationStack()) and '-' in token:
                error_msg = f"SyntaxError: line {line}: column {column} - negative percentages are not allowed in the blend definition"
            else:
                error_msg = f"SyntaxError: line {line}: column {column} - incorrect syntax at '{token}'"

        # 2. Błąd rozpoznania tokenu (np. nieoczekiwany znak)
        elif "token recognition error at" in msg:
            match = re.search(r"token recognition error at: ['\"](.*?)['\"]", msg)
            token = match.group(1) if match else current_token
            if token == '\n':
                error_msg = f"SyntaxError: line {line}: column {column} - no closing quotation mark (\")"
            else:
                error_msg = f"SyntaxError: line {line}: column {column} - unexpected sign '{token}'"

        # 3. Niedopasowane wejś
        elif "mismatched input" in msg:
            match = re.search(r"mismatched input '(.*?)' expecting (.*?)$", msg)
            if match:
                found = match.group(1)
                expected = match.group(2)
                # Specjalna obsługa ujemnych procentów w blendzie
                if "blend" in str(recognizer.getRuleInvocationStack()) and found == '-':
                    error_msg = f"SyntaxError: line {line}: column {column} - negative percentages are not allowed in the blend definition"
                elif "blend" in str(recognizer.getRuleInvocationStack()) and found not in ["circle", "rectangle"]:
                    error_msg = f"SyntaxError: line {line}: column {column} - unknown figure type '{found}' at blendu definition"
                elif "pointer" in str(recognizer.getRuleInvocationStack()) and found not in ["up", "down", "left", "right"]:
                    error_msg = f"SyntaxError: line {line}: column {column} - unknown direction'{found}' in pointer instruction"
                else:
                    error_msg = f"SyntaxError: line {line}: column {column} - found '{found}', expected {expected}"
            else:
                error_msg = f"SyntaxError: line {line}: column {column} - incomplete or incorrect instructions"

        # 4. Brakujące elementy (np. ';', '%', ')')
        elif "missing" in msg:
            match = re.search(r"missing (.*?) at '(.*?)'", msg)
            if match:
                missing = match.group(1)
                at_token = match.group(2)
                if missing == "'%'" and "blend" in str(recognizer.getRuleInvocationStack()):
                    error_msg = f"SyntaxError: line {line}: column {column} - missing '%' in blend definition at '{at_token}'"
                elif missing == "';'" and "for" in str(recognizer.getRuleInvocationStack()):
                    error_msg = f"SyntaxError: line {line}: column {column} - issing ';' in 'for' loop at '{at_token}'"
                elif missing == "')'" and "if" in str(recognizer.getRuleInvocationStack()):
                    error_msg = f"SyntaxError: line {line}: column {column} - missing ')' in 'if' statment at '{at_token}'"
                else:
                    error_msg = f"SyntaxError: line {line}: column {column} - missin {missing} at token '{at_token}'"
            else:
                error_msg = f"SyntaxError: line {line}: column {column} - missing required syntax element"

        # 5. Niepotrzebne tokeny (np. podwójny przecinek w liście argumentów)
        elif "extraneous input" in msg:
            match = re.search(r"extraneous input '(.*?)' expecting", msg)
            token = match.group(1) if match else current_token
            if "function" in str(recognizer.getRuleInvocationStack()):
                error_msg = f"SyntaxError: line {line}: column {column} - invalid argument list, unnecessary token '{token}'"
            elif "for" in str(recognizer.getRuleInvocationStack()):
                error_msg = f"SyntaxError: line {line}: column {column} - not-needed token '{token}' in 'for' loop"
            else:
                error_msg = f"SyntaxError: line {line}: column {column} - not-needed token '{token}'"

        # 6. Niekompletna instrukcja road
        elif "road" in str(recognizer.getRuleInvocationStack()) and "mismatched" in msg:
            match = re.search(r"mismatched input '(.*?)' expecting", msg)
            token = match.group(1) if match else current_token
            if token not in ["start", "end"]:
                error_msg = f"SyntaxError: line {line}: column {column} - incomplete road manual, expected 'start' or 'end'"

        # 7. Nieprawidłowy operator w wyrażeniu porównania
        elif "exprComp" in str(recognizer.getRuleInvocationStack()) and "mismatched" in msg:
            match = re.search(r"mismatched input '(.*?)' expecting", msg)
            token = match.group(1) if match else current_token
            if token == '=':
                error_msg = f"SyntaxError: line {line}: column {column} - incorrect operator '=', expecting '==' in comparison"

        # Rzucenie wyjątku z komunikatem błędu
        raise Exception(error_msg)
