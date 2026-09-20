# input is a . vm file


class Parser:

    def __init__(self, path):

        self.stream = open(path, "r", encoding="utf-8")  # initalizes the file stream
        self.current_command = None
        self.next_command = None

    def has_more_commands(self) -> bool:
        # parse through the file and store next_command here, if present return true and populate next_command, otherwise None and return false
        # if this is false we exit out of the loop,advance is onl called when has_more_commands if true
        for line in self.stream:

            res = line.split("//")[0].strip()
            if res == "":
                continue

            self.next_command = res
            return True

        self.next_command = None
        return False

    def advance(self):
        self.current_command = self.next_command
        self.next_command = None

    def command_type(self) -> str:

        command = self.current_command.split()

        if command[0] == "push":
            return "C_PUSH"

        elif command[0] == "pop":
            return "C_POP"

        else:
            # arithmetic command,

            return "C_ARITHMETIC"

    def get_arg1(self) -> str:  # not called when the current command is C_RETURN

        if self.command_type() == "C_PUSH" or self.command_type() == "C_POP":
            return self.current_command.split()[1]

        else:  # arithmetic command
            return self.current_command

    def get_arg2(self) -> int:  # only called on C_push, C_pop, C_function, C_call

        # note this will not work in chapter 8, need to change
        return int(self.current_command.split()[2])

    def close (self):
        self.stream.close()
