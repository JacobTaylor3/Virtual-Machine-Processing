# input is a . vm file



class Parser:

    def __init__(self, path):

        self.stream = open(path, "r", encoding="utf-8")  # initalizes the file stream
        self.current_command = None


        pass

    def has_more_lines(self)->bool:
        pass

    def advance(self):
        pass

    def command_type(self)->str:
        pass

    def get_arg1(self)->str:
        pass

    def get_arg2(self)->int:
        pass
