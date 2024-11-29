from SCCG.parser import Parser


def get_one_line():
    return "var integer = 50    ;comment means the end of the line"


def get_multi_line():
    return ("var integer = 50    ;comment\n"
            "var floating = 3.14    ;comment2\n"
            ";only comment\n"
            "var string = \"String variable\" ;comment 3")


def test_tokenization_one_line():
    tokens = Parser.tokenization(get_one_line())
    #Parser.print_tokens(tokens)

    expected = ["var", "integer", "=", "50", ";", "comment", "means", "the", "end", "of", "the", "line"]

    assert tokens == expected


def test_tokenization_multi_line():
    tokens = Parser.tokenization(get_multi_line())
    Parser.print_tokens(tokens)

    expected = ["var", "integer", "=", "50", ";", "comment", "\n",
                "var", "floating", "=", "3.14", ";", "comment2", "\n",
                ";", "only", "comment", "\n",
                "var", "string", "=", "\"", "String", "variable", "\"", ";", "comment", "3"]

    assert tokens == expected


def test_get_abstract_syntax_tree_one_line():
    tokens = Parser.tokenization(get_multi_line())
    ast = Parser.get_abstract_syntax_tree(tokens)

    #print()
    #Parser.print_abstract_syntax_tree(ast)


def test_get_abstract_syntax_tree_multi_line():
    tokens = Parser.tokenization(get_multi_line())
    ast = Parser.get_abstract_syntax_tree(tokens)

    print()
    Parser.print_abstract_syntax_tree(ast)
