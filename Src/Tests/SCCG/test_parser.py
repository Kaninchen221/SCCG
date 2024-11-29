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
    #Parser.print_tokens(tokens)

    expected = ["var", "integer", "=", "50", ";", "comment", "means", "the", "end", "of", "the", "line"]

    assert tokens == expected


def test_tokenization_multi_line():
    tokens = Parser.tokenization(get_multi_line())
    #Parser.print_tokens(tokens)

    expected = ["var", "integer", "=", "50", ";", "comment", "\n",
                "var", "floating", "=", "3.14", ";", "comment2", "\n",
                ";", "line", "with", "only", "comment", "\n",
                "var", "string", "=", "\"", "String", "Constant", "\"", ";", "comment", "3"]

    assert tokens == expected


def test_get_abstract_syntax_tree_one_line():
    tokens = Parser.tokenization(get_one_line())
    ast = Parser.get_abstract_syntax_tree(tokens)

    line_statement = ast.children[0]
    assert len(line_statement.children) == 3
    assert " ".join(line_statement.children[0].tokens) == "var integer"
    assert " ".join(line_statement.children[1].tokens) == "= 50"
    assert " ".join(line_statement.children[2].tokens) == "; comment means the end of the line"

    #print()
    #Parser.print_abstract_syntax_tree(ast)


def test_get_abstract_syntax_tree_multi_line():
    tokens = Parser.tokenization(get_multi_line())
    ast = Parser.get_abstract_syntax_tree(tokens)

    # Test count of lines statements
    assert len(ast.children) == 4

    # Test count of statements in second line
    assert len(ast.children[1].children) == 3

    # Test string expression
    assert ''.join(ast.children[3].children[1].tokens) == "=\"StringConstant\""

    #print()
    #Parser.print_abstract_syntax_tree(ast)
