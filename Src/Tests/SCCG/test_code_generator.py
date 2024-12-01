import pytest

from SCCG.code_generator import CodeGenerator
from SCCG.parser import Parser


def get_code():
    return ("var integer = 50    ;comment\n"
            "var floating = 3.14    ;comment2\n"
            ";line with only comment\n"
            "var string = \"String Constant\" ;comment 3")


def test_code_generator():
    tokens = Parser.tokenization(get_code())
    ast = Parser.get_abstract_syntax_tree(tokens)

    #print()
    #Parser.print_abstract_syntax_tree(ast)

    nasm = CodeGenerator.transform_ast_to_nasm(ast)

    expected = \
        ("integer db 50\n"
         "floating dd 3.14\n"
         "string db \"String Constant\", 0\n")

    print("\nGenerated nasm:")
    print(nasm)

    assert nasm == expected


def test_not_supported_expression():
    code = "var integer -= 50"
    tokens = Parser.tokenization(code)
    # print(tokens)
    ast = Parser.get_abstract_syntax_tree(tokens)
    # print(ast)

    with pytest.raises(Exception):
        nasm = CodeGenerator.transform_ast_to_nasm(ast)
        print(nasm)
