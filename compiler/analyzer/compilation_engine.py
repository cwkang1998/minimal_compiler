class CompilationEngine:
    def __init__(self, input: str, output: str):
        self.input = input
        self.output = output
        self.tokens = []
        self.front_token_index = 0
        self.back_token_index = 0
        self.ast = None

    def compile_class(self):
        pass

    def compile_class_var_dec(self):
        pass

    def compile_subroutine(self):
        pass

    def compile_parameter_list(self):
        pass

    def compile_var_dec(self):
        pass

    def compile_statements(self):
        pass

    def compile_do(self):
        pass

    def compile_let(self):
        pass

    def compile_while(self):
        pass

    def compile_return(self):
        pass

    def compile_if(self):
        pass

    def compile_expression(self):
        pass

    def compile_term(self):
        pass

    def compiler_expression_list(self):
        pass
