import pytest
from unittest.mock import patch
import unittest
from shelf_document_tests_homework import \
    check_document_existance, get_doc_owner_name, get_doc_shelf, remove_doc_from_shelf, \
    delete_doc, add_new_shelf, append_doc_to_shelf


FIXTURE = [("11-2", True), ("11-3", False)]
# FIXTURE2= [("11-2","Геннадий Покемонов"),("10006","Аристарх Павлов"), ("5555545", None)]
FIXTURE3 = [("10006", True), ("11-2", True), ("10005", False)]

@pytest.mark.parametrize("document, result", FIXTURE)
def test_check_document_existance(document, result):
    assert check_document_existance(document) == result

@patch('builtins.input', lambda _: '11-2')
def test_get_doc_owner_name():
    assert get_doc_owner_name() == "Геннадий Покемонов"

@patch('builtins.input', lambda _: '11-1')
def test_get_doc_owner_name2():
    assert get_doc_owner_name() == None

@patch('builtins.input', lambda _: '11-2')
def test_get_doc_shelf():
    assert get_doc_shelf() == "1"

@patch('builtins.input', lambda _: '10006')
def test_get_doc_shelf2():
    assert get_doc_shelf() == "2"

@patch('builtins.input', lambda _: '11-1')
def test_get_doc_shelf3():
    assert get_doc_shelf() == None

@pytest.mark.parametrize("document, result", FIXTURE3)
def test_remove_doc_from_shelf(document, result):
    assert remove_doc_from_shelf(document) == result

@patch('builtins.input', lambda _: '10006')
def test_remove_doc_from_shelf():
    assert delete_doc()[1] == True

@patch('builtins.input', lambda _: '10005')
def test_remove_doc_from_shelf2():
    assert delete_doc() == None

@patch('builtins.input', lambda _: '4')
def test_add_new_shelf():
    assert add_new_shelf()[1] == True

@patch('builtins.input', lambda _: '3')
def test_add_new_shelf2():
    assert add_new_shelf()[1] == False

FIXTURE4 = [("111","1", ('1', False)), ("222","4", ('4', False)),
            ("11-2", "1", ('1', False)), ("11-2", "6", ('6', True)),
            ("11-2", "5", ('5', True))
            ]
@pytest.mark.parametrize("doc_number, shelf_number, result", FIXTURE4)
def test_append_doc_to_shelf(doc_number, shelf_number, result):
    assert append_doc_to_shelf(doc_number, shelf_number) == result















