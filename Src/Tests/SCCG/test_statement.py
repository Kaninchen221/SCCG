from SCCG.statement import StatementType
from SCCG.statement import Statement


def test_statement_type():
    statement_type = StatementType.File


def test_statement():
    statement = Statement()

    assert type(statement.type) is StatementType
    assert type(statement.tokens) is type([])
    assert type(statement.children) is type([])
    assert statement.parent is None
