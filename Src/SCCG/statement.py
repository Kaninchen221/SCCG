from enum import Enum


class StatementType(Enum):
    File = 0,
    Line = 1,
    VarDeclaration = 2,
    Expression = 3,
    Identifier = 4,
    StringConstant = 5,
    NumberConstant = 6,
    Comment = 7,
    Invalid = 8


class Statement:

    def __init__(self):
        self.type = StatementType.Invalid
        self.token = ""
        self.parent = None
        self.children = []

    def __str__(self):
        return Statement._to_string_internal(self)

    @staticmethod
    def _to_string_internal(statement, spacing=""):
        result = f"{spacing}{statement.type.name}"
        if statement.token:
            result += f" : {statement.token}"
        result += '\n'

        for child in statement.children:
            result += Statement._to_string_internal(child, spacing + "\t")
        return result
