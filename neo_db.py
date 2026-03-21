from unittest.mock import patch
from Validation import user_valid
from RecordManager import RecordManager
from storage import get_db
from user_interface import time_save,generate_id
from search import combined_search
def test_username_case():
    assert user_valid("NEO21")==False
def test_username_short_length():
    assert user_valid("ob")==False
def test_username_long_length():
    assert user_valid("the_user_of_the_north_states")==False
def test_username_space():
    assert user_valid("neo star")==False
def test_valid_username():
    assert user_valid("neo_aizen07")==True
def test_record_insertions():
    manager=RecordManager()
    manager.update_record("neo_user",generate_id(),time_save())
    with get_db() as conn:
        row=conn.execute("Select * from records where username=?",("neo_user",)).fetchone()
    assert row is not None
def test_delete_one_record():
    manager=RecordManager()
    manager.update_record("del_test","894032jhiu",time_save())
    manager.delete_1("del_test")
    with get_db() as conn:
        rec=conn.execute("select * from records where username=?",("del_test",)).fetchone()
    assert rec is None
def test_delete_all_record():
    manager=RecordManager()
    manager.update_record("user_one", generate_id(), time_save())
    manager.update_record("user_two", generate_id(), time_save())
    manager.delete_0()
    with get_db() as conn:
        rec=conn.execute("select * from records").fetchall()
    assert len(rec)==0
def test_search_username(capsys):
    with patch('builtins.input',return_value='test_1'):
        combined_search()
    captured=capsys.readouterr()
    assert "test_1" in captured.out
def test_search_par_username(capsys):
    with patch('builtins.input',side_effect=['test_1','test']):
        combined_search()
    captured=capsys.readouterr()
    assert "test_1"and 'test' in captured.out
def test_search_id(capsys):
    with patch('builtins.input',return_value='ji93hdcn34'):
        combined_search()
    captured=capsys.readouterr()
    assert 'ji93hdcn34' in captured.out