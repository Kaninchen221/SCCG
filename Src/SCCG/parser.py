from SCCG.statement import Statement, StatementType
from Utils.helpers import find_next_occurrence


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
        is_in_string_literal = False

        for char in text:
            match char:
                
                # Found a separator
                case ' ':
                    if is_in_string_literal:
                        token += char
                    else:
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
                    is_in_string_literal = not is_in_string_literal

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
        root_statement = Statement()
        root_statement.type = StatementType.File

        first_line_statement = Statement()
        first_line_statement.parent = root_statement
        first_line_statement.type = StatementType.Line
        root_statement.children.append(first_line_statement)

        current_statement = first_line_statement

        index = 0
        while index < len(tokens):
            token = tokens[index]
            match token:

                # Is a variable declaration
                case "var":
                    statement = Statement()
                    statement.parent = current_statement
                    statement.type = StatementType.VarDeclaration
                    statement.token = token
                    current_statement.children.append(statement)

                # Is an assign expression
                case "=":
                    statement = Statement()
                    statement.parent = current_statement
                    statement.type = StatementType.Expression
                    statement.token = token

                    current_statement.children.append(statement)

                # Is a comment
                case ";":
                    statement = Statement()
                    statement.parent = current_statement
                    statement.type = StatementType.Comment

                    end_line_position = find_next_occurrence(tokens, '\n', index + 1, len(tokens))
                    statement.token = " ".join(tokens[index:end_line_position])

                    index = end_line_position - 1

                    current_statement.children.append(statement)

                # New Line
                case "\n":
                    current_statement = current_statement.parent
                    new_line_statement = Statement()
                    new_line_statement.parent = current_statement
                    new_line_statement.type = StatementType.Line
                    current_statement.children.append(new_line_statement)
                    current_statement = new_line_statement

                # String constant
                case "\"":
                    string_statement = Statement()
                    string_statement.parent = current_statement
                    string_statement.type = StatementType.StringConstant
                    end_of_string_expression = find_next_occurrence(tokens, "\"", index + 1, None)
                    if end_of_string_expression:
                        string_statement.token = tokens[index+1]
                        index = end_of_string_expression
                        current_statement.children.append(string_statement)
                    else:
                        raise Exception("Close the string expression")

                # Identifier
                case _:
                    if token == ' ' or token == '':
                        index += 1
                        continue

                    statement = Statement()
                    statement.parent = current_statement
                    statement.token = token
                    if token.isdigit():
                        statement.type = StatementType.NumberConstant
                    else:
                        statement.type = StatementType.Identifier
                    current_statement.children.append(statement)

            index += 1

        return root_statement
