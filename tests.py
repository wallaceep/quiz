import pytest
from model import Question
from model import Choice


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_remove_choice_by_id():
    question = Question(title='q1')
    question.add_choice('a', True)
    question.add_choice('b', True)
    choice = question._choice_by_id(1)
    assert choice.id == 1
    question.remove_choice_by_id(1)
    assert len(question.choices) == 1   

def test_set_correct_choices():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)
    question.add_choice('d', False)

    question.set_correct_choices([1,3])
    ch1 = question._choice_by_id(1)    
    ch2 = question._choice_by_id(2)
    ch3 = question._choice_by_id(3)

    assert ch1.is_correct == True and ch2.is_correct == False and ch3.is_correct == True

def test_remove_choice_in_questions_without_choices():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.remove_choice_by_id(1)
    with pytest.raises(Exception):
        question.remove_choice_by_id(1)

def test_add_choice_and_remove_and_add_again():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.remove_choice_by_id(1)
    question.add_choice('c', False)

    choice = question.choices[0]
    assert len(question.choices) == 2
    assert choice.text == 'c'
    assert not choice.is_correct

def test_check_if_choice_was_really_removed():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.remove_choice_by_id(2)
    question.add_choice('c', False)

    choice = question.choices[1]
    assert len(question.choices) == 2
    assert not choice.text == 'b'

def test_check_choice_without_text():
    with pytest.raises(Exception):
        choice = Choice(1)

def test_check_choice_without_id():
    with pytest.raises(Exception):
        choice = Choice("March 25")

def test_create_multiple_choices():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', True)

    c1 = question.choices[0]
    c2 = question.choices[1]
    assert len(question.choices) == 2
    assert c1.text == 'a'
    assert not c1.is_correct
    assert c2.text == 'b'
    assert c2.is_correct