class Raiser:
    @staticmethod
    def raiseError(ctx, msg):
        try:
            token = ctx.IDENTIFIER().getSymbol()
        except AttributeError:
            token = ctx.start
        line = token.line
        column = token.column
        raise RuntimeError(f"line: {line}, column: {column} – {msg}")