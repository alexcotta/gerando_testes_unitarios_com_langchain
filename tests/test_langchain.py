import pytest
from app.langchain_utils import python_repl, chatgpt

def test_python_repl_addition():
    output = python_repl.run("print(2 + 3)")
    assert output.strip() == "5"

def test_python_repl_variable():
    code = """
x = 10
y = 7
print(x * y)
"""
    output = python_repl.run(code)
    assert output.strip() == "70"

def test_chatgpt_response():
    response = chatgpt.predict("Qual é a capital da França?")
    assert "Paris" in response
