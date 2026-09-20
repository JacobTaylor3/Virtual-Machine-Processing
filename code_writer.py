from parser import Parser

from pathlib import Path


class CodeWriter:

    def __init__(self, path):

        self.parser_in = Parser(path=path)

        path_obj = Path(path)

        filename = path_obj.stem + ".asm"

        self.asm_out = open(filename, "w")

    def write_arithmetic(self):
        pass

    def write_push_pop(self):
        pass
