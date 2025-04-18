from enum import Enum
from typing import List

class SyntaxType(Enum):
    # Structure
    CLASS = "CLASS"
    CLASS_VAR_DEC = "CLASS_VAR_DEC"
    TYPE = "TYPE"
    SUBROUTINE_DEC = "SUBROUTINE_DEC"
    PARAMETER_LIST = "PARAMETER_LIST"
    SUBROUTINE_BODY = "SUBROUTINE_BODY"
    VAR_DEC = "VAR_DEC"
    CLASS_NAME = "CLASS_NAME"
    SUBROUTINE_NAME = "SUBROUTINE_NAME"
    VAR_NAME = "VAR_NAME"
    # Statements
    LET_STATEMENT = "LET_STATEMENT"
    IF_STATEMENT = "IF_STATEMENT"
    WHILE_STATEMENT = "WHILE_STATEMENT"
    DO_STATEMENT = "DO_STATEMENT"
    RETURN_STATEMENT = "RETURN_STATEMENT"
    # Expressions
    TERM = "TERM"
    SUBROUTINE_CALL = "SUBROUTINE_CALL"
    EXPRESSION_LIST = "EXPRESSION_LIST"
    OPERATOR = "OPERATOR"
    KEYWORD_CONSTANT = "KEYWORD_CONSTANT"


class SyntaxNode:
    def __init__(self, type: SyntaxType, body: List['SyntaxNode']):
        self.type = type
        self.body = body

    def __str__(self):
        return f"{self.type}: {self.body}"
    
    def syntax_analysis(self):
        pass

    def analyze_structure(self):
        pass
    
    def analyze_statements(self):
        pass
    
    def analyze_expressions(self):
        pass
    
