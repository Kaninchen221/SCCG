
class Parser:

    def __init__(self):
        pass

    @staticmethod
    def parse(text):
        pass

    @staticmethod
    def tokenization(text):
        result = []
        token = ""
        for char in text:
            match char:
                # Found a separator
                case ' ':
                    if Parser.is_token_valid(token):
                        result.append(token)
                    token = ""
                # Found a new line
                case '\n':
                    if Parser.is_token_valid(token):
                        result.append(token)
                    if token != '\n':
                        result.append('\n')
                    token = ""
                # Found a comment
                case ';':
                    if Parser.is_token_valid(token):
                        result.append(token)
                    token = ";"
                    result.append(token)
                    token = ""
                # Start/End of a string
                case '"':
                    if Parser.is_token_valid(token):
                        result.append(token)
                    token = ""
                    result.append('"')
                # Default
                case _:
                    token += char

        if Parser.is_token_valid(token):
            result.append(token)

        return result

    @staticmethod
    def is_token_valid(token):
        match token:
            case ' ':
                return False
            case '':
                return False
        return True

    @staticmethod
    def print_tokens(tokens):
        print('\n')
        index = 0
        for token in tokens:
            if token == '\n':
                print(f"[{index}]: ", r'\n')
            else:
                print(f"[{index}]: {token}")
            index += 1

    @staticmethod
    def get_abstract_syntax_tree(tokens):
        result = []
        for index in range(0, len(tokens)):
            token = tokens[index]
            match token:
                # Is a variable declaration
                case "var":
                    result.append(["Variable declaration", [token, tokens[index + 1]]])
                    index += 1
                # Is an assign
                case "=":
                    result.append(["Assign", [token, tokens[index + 1]]])
                    index += 1
                # Is a comment
                case ";":
                    try:
                        end_line_position = tokens.index('\n', index + 1)
                        comment_value = " ".join(tokens[index + 1:end_line_position])
                        index = end_line_position
                    # Couldn't find new line
                    except ValueError:
                        comment_value = " ".join(tokens[index + 1:])
                        index = len(tokens)

                    result.append(["Comment", [token, comment_value]])
                # New Line
                case "\n":
                    pass

        return result

    @staticmethod
    def print_abstract_syntax_tree(tokens, spacing=""):
        if type(tokens) is list:
            for token in tokens:
                Parser.print_abstract_syntax_tree(token, spacing + "\t")
        else:
            if tokens == "\n":
                print(spacing, r"\n")
            else:
                print(spacing, tokens)
