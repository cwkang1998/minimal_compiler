from enum import Enum

KEYWORDS = {
    "class",
    "constructor",
    "function",
    "method",
    "field",
    "static",
    "var",
    "int",
    "char",
    "boolean",
    "void",
    "true",
    "false",
    "null",
    "this",
    "let",
    "do",
    "if",
    "else",
    "while",
    "return",
}

SYMBOLS = {
    '{',
    '}',
    '(',
    ')',
    '[',
    ']',
    '.',
    ',',
    ';',
    '+',
    '-',
    '*',
    '/',
    '&',
    '|',
    '<',
    '>',
    '=',
    '~',
}

# Integer constants are in the range 0..32767
INTEGER_CONST_MIN = 0
INTEGER_CONST_MAX = 32767

# Keyword constants
KEYWORD_CONSTANTS = {
    "true",
    "false",
    "null",
    "this"
}

# Types in the Jack language
TYPES = {
    "int",
    "char",
    "boolean",
    # class names are also types, but those are dynamic
}

# Operators in Jack language
OPERATORS = {
    "+": "add",
    "-": "sub",
    "*": "multiply",
    "/": "divide",
    "&": "and",
    "|": "or",
    "<": "lt",
    ">": "gt",
    "=": "eq"
}

# Unary operators
UNARY_OPERATORS = {
    "-": "neg",
    "~": "not"
}

# Statement types
STATEMENT_TYPES = {
    "let",
    "if",
    "while",
    "do",
    "return"
}

# Token types for the Jack language
class TokenTypes(Enum):
    KEYWORD = "keyword"
    SYMBOL = "symbol"
    INTEGER_CONST = "integerConstant"
    STRING_CONST = "stringConstant"
    IDENTIFIER = "identifier"