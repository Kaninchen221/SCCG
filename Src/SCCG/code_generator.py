from SCCG.statement import StatementType


class CodeGenerator:

    @staticmethod
    def transform_ast_to_nasm(file_statement):
        result = ""

        if file_statement.type != StatementType.File:
            raise Exception("file_statement isn't file statement")

        for line_statement in file_statement.children:
            children = line_statement.children

            # Filter the statement
            match children[0].type:
                case StatementType.VarDeclaration:
                    if children[2].token != '=':
                        raise Exception("Var declaration needs value assignment")

                    result += children[1].token
                    value = children[3].token
                    # String
                    if children[3].type == StatementType.StringConstant:
                        result += f" db \"{children[3].token}\", 0\n"
                    # Floating point
                    elif '.' in value:
                        result += f" dd {children[3].token}\n"
                    # Integer
                    else:
                        result += f" db {children[3].token}\n"

        return result
