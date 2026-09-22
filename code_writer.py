from parser import Parser

from pathlib import Path


class CodeWriter:

    def __init__(self, path):

        self.parser_in = Parser(path=path)

        path_obj = Path(path)

        self.file_name = path_obj.stem

        filename = self.file_name + ".asm"

        self.asm_out = open(filename, "w")

    def write_arithmetic(self):  # called only when the Command instruction is arthmetic

        pass

    def write_push(self):  #

        arg1 = self.parser_in.get_arg1()
        index = self.parser_in.get_arg2()  # this is an int

        asm = []

        base_segments = {
            "argument": "ARG",
            "local": "LCL",
            "this": "THIS",
            "that": "THAT",
        }

        # @ARG // M=RAM[ARG]
        # D=M  // D=RAM[ARG], D stores base address
        # @arg2
        # A=A+D // base Address + index
        # D=M

        if arg1 in base_segments:
            asm.append(f"@{base_segments[arg1]}")
            asm.append("D=M")
            asm.append(f"@{index}")
            asm.append("A=A+D")
            asm.append("D=M")

        elif arg1 == "static":

            symbol = f"@{self.file_name}.{index}"

            asm.append(symbol)
            asm.append("D=M")

        elif arg1 == "constant":

            asm.append(f"@{index}")
            asm.append("D=A")

        elif arg1 == "pointer":

            if index == 0:

                asm.append("@THIS")
                asm.append("D=M")

            else:  # index ==1

                asm.append("@THAT")
                asm.append("D=M")

        elif arg1 == "temp":

            asm.append("@5")
            asm.append("D=A")
            asm.append(f"@{index}")
            asm.append("A=A+D")
            asm.append("D=M")

        base_str = "@SP\nA=M\nM=D\n@SP\nM=M+1"

        push_instructions = "\n".join(asm) + "\n" + base_str

        self.asm_out.write(f"// {self.parser_in.current_command}")

        self.asm_out.write(f"{push_instructions}")

    def write_pop(self):
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

            # will add the function stuff in chapter 8
