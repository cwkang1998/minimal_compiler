import re
from compiler.lang_tokens import KEYWORDS, SYMBOLS, INTEGER_CONST_MIN, INTEGER_CONST_MAX, KEYWORD_CONSTANTS, TYPES, TokenTypes

class Tokenizer:
    input_file = None
    file_contents = None
    word_lists = list()

    def __init__(self, input_file):
        self.input_file_name = input_file
        with open(input_file, "r") as f:
            self.file_contents = f.read()
        self.remove_comments()
        self.parse_and_tokenize()

    """
    Remove comments from the file contents
    """
    def remove_comments(self):
        # Remove block comments (/* ... */ and /** ... */)
        self.file_contents = re.sub(r'/\*\*?[\s\S]*?\*/', '', self.file_contents)
        
        # Remove line comments (// ...)
        self.file_contents = re.sub(r'//.*?$', '', self.file_contents, flags=re.MULTILINE)

    """
    Parse the input jack into separated words, handling symbols properly.
    """
    def parse_and_tokenize(self):
        # First, handle string literals to protect them from tokenization
        strings = []
        def save_string(match):
            strings.append(match.group(1))
            return f" STRING_{len(strings)-1} "
        
        # Replace string literals with placeholders
        content_with_placeholders = re.sub(r'"(.*?)"', save_string, self.file_contents)
        
        # Add spaces around symbols for easier splitting
        for symbol in sorted(SYMBOLS, key=len, reverse=True):  # Process longer symbols first
            content_with_placeholders = content_with_placeholders.replace(symbol, f" {symbol} ")
        
        # Split by whitespace and filter out empty strings
        tokens = [token for token in content_with_placeholders.split() if token]
        
        # Restore string literals
        for i, token in enumerate(tokens):
            if token.startswith("STRING_"):
                string_index = int(token.split("_")[1])
                tokens[i] = (f'"{strings[string_index]}"', self.get_token_type(token))
            else:
                tokens[i] = (token, self.get_token_type(token))
        
        self.word_lists = tokens
        # print(self.word_lists)
        
        # Find the maximum token length for proper alignment
        max_token_length = max(len(str(token)) for token, _ in self.word_lists)
        
        print(f"{'TOKEN':>{max_token_length}} | TYPE")
        print("-" * (max_token_length + 25))
        
        # Print each token with aligned formatting
        for token, token_type in self.word_lists:
            print(f"{str(token):>{max_token_length}} | {token_type}")

    def get_token_type(self, token):
        try:
            if token in KEYWORDS:
                return TokenTypes.KEYWORD
            
            if token in SYMBOLS:
                return TokenTypes.SYMBOL
            
            if isinstance(token, str) and token.isdigit():
                num = int(token)
                try: 
                    assert INTEGER_CONST_MIN <= num <= INTEGER_CONST_MAX
                    return TokenTypes.INTEGER_CONST
                except ValueError:
                    error_msg = f"Error: Integer constant '{token}' is out of bounds"
                    print(error_msg)
                    return error_msg

            if isinstance(token, tuple) and len(token) == 1:
                return TokenTypes.STRING_CONST
            
            if isinstance(token, str):
                return TokenTypes.IDENTIFIER
            
            error_msg = f"Error: Unknown token type for '{token}'"
            print(error_msg)
            return error_msg
        except Exception as e:
            error_msg = f"Error processing token '{token}': {e}"
            print(error_msg)
            return error_msg

Tokenizer("project/Main.jack")