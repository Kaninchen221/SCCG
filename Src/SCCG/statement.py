from enum import Enum


class StatementType(Enum):
    File = 0,
    Line = 1,
    VarDeclaration = 2,
    Expression = 3,
    Comment = 5,
    Invalid = 6


class Statement:

    def __init__(self):
        self.type = StatementType.Invalid
        self.tokens = []
        self.parent = None
        self.children = []

    def __str__(self):
        if self.tokens:
            return f"{self.type.name} : {self.tokens}"
        else:
            return f"{self.type.name}"
