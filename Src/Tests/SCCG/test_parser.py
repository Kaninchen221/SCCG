from SCCG.parser import Parser


def get_one_line():
    return "var integer = 50    ;comment means the end of the line"


def get_multi_line():
    return ("var integer = 50    ;comment\n"
            "var floating = 3.14    ;comment2\n"
            ";line with only comment\n"
            "var string = \"String Constant\" ;comment 3")


def test_tokenization_one_line():
    tokens = Parser.tokenization(get_one_line())
    # Parser.print_tokens(tokens)

    expected = ["var", "integer", "=", "50", ";", "comment", "means", "the", "end", "of", "the", "line"]

    assert tokens == expected


def test_tokenization_multi_line():
    tokens = Parser.tokenization(get_multi_line())
    # Parser.print_tokens(tokens)

    expected = ["var", "integer", "=", "50", ";", "comment", "\n",
                "var", "floating", "=", "3.14", ";", "comment2", "\n",
                ";", "line", "with", "only", "comment", "\n",
                "var", "string", "=", "\"", "String Constant", "\"", ";", "comment", "3"]

    assert tokens == expected


def test_get_abstract_syntax_tree_one_line():
    tokens = Parser.tokenization(get_one_line())
    ast = Parser.get_abstract_syntax_tree(tokens)

    # print()
    # print(tokens)
    # Parser.print_abstract_syntax_tree(ast)

    line_statement = ast.children[0]
    assert len(line_statement.children) == 5
    assert line_statement.children[0].token == "var"
    assert line_statement.children[1].token == "integer"
    assert line_statement.children[2].token == "="
    assert line_statement.children[3].token == "50"
    assert line_statement.children[4].token == "; comment means the end of the line"


def test_get_abstract_syntax_tree_multi_line():
    tokens = Parser.tokenization(get_multi_line())
    ast = Parser.get_abstract_syntax_tree(tokens)

    # print()
    # print(tokens)
    # Parser.print_abstract_syntax_tree(ast)

    # Test count of lines statements
    assert len(ast.children) == 4

    # Test count of statements in second line
    assert len(ast.children[1].children) == 5

    # Test string expression
    assert ast.children[3].children[3].token == "String Constant"
