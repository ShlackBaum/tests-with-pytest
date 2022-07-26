import pytest
from unittest.mock import patch
import unittest
from shelf_document_tests_homework import \
    check_document_existance, get_doc_owner_name, \
    get_doc_shelf, remove_doc_from_shelf, \
    delete_doc, add_new_shelf, append_doc_to_shelf, \
    get_all_doc_owners_names, move_doc_to_shelf, show_document_info, \
    show_all_docs_info


FIXTURE = [("11-2", True), ("11-3", False)]
# FIXTURE2= [("11-2","Геннадий Покемонов"),("10006","Аристарх Павлов"), ("5555545", None)]
FIXTURE3 = [("10006", True), ("11-2", True), ("10005", False)]
FIXTURE4 = [("111","1", ('1', False)), ("222","4", ('4', True)),
            ("11-2", "1", ('1', False)), ("11-2", "6", ('6', True)),
            ("11-2", "5", ('5', True))
            ]
FIXTURE5 = [({"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}, ('passport', '2207 876234', 'Василий Гупкин')),
            ({"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}, ('invoice', '11-2', 'Геннадий Покемонов')),
            ({"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}, ('insurance', '10006', 'Аристарх Павлов'))]


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


@pytest.mark.parametrize("doc_number, shelf_number, result", FIXTURE4)
#По непонятной причине третья проверка в фикстуре выдает ошибку
def test_append_doc_to_shelf(doc_number, shelf_number, result):
    assert append_doc_to_shelf(doc_number, shelf_number) == result

def test_get_all_doc_owners_names(): #По непонятной причине Аристарх лишний
    assert get_all_doc_owners_names() == ['Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов']


@pytest.mark.parametrize("document, result", FIXTURE5)
def test_show_document_info(document, result):
    assert show_document_info(document) == result

def test_show_all_docs_info(): #По непонятной причине Аристарх лишний и здесь
    assert show_all_docs_info() == [('passport', '2207 876234', 'Василий Гупкин'), ('invoice', '11-2', 'Геннадий Покемонов'), ('insurance', '10006', 'Аристарх Павлов')]

# @patch('builtins.input', side_effect=['11-2', '3']) Multiple Inputs How?
# def test_move_doc_to_shelf():
#     assert move_doc_to_shelf() == "Document moved"

# def test_add_new_doc():
#     assert add_new_doc() == ??? Multiple inputs again


















