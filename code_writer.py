from parser import Parser

from pathlib import Path


class CodeWriter:

    def __init__(self, path):

        self.parser_in = Parser(path=path)

        path_obj = Path(path)

        filename = path_obj.stem + ".asm"

        self.asm_out = open(filename, "w")

    def write_arithmetic(self):  # called only when the Command instruction is arthmetic

        pass

    def write_push(self):  #

       arg1 = self.parser_in.get_arg1()
       arg2 = self.parser_in.get_arg2(), # this is an int 


        # below is the default push command, we just need to first load the desired value into the D register first, which changes based on what type it is, eg., local,constant,etc

        # @SP
        # A=M
        # M=D
        # @SP
        # M=M+

        

    def write_pop (self):
        pass

    def run(self):

        while self.parser_in.has_more_commands():

            self.parser_in.advance()

            if self.parser_in.command_type() == "C_POP":
                self.write_pop()

            elif self.parser_in.command_type() == "C_PUSH":
                self.write_push()

            elif self.parser_in.command_type() == "C_ARITHMETIC":
                self.write_arithmetic()

            #will add the function stuff in chapter 8


