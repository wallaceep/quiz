import pytest
from model import Question
from model import Choice

@pytest.fixture
def question_with_choices():
    question = Question(title="Qual é a capital da França?", points=5, max_selections=1)
   
    question.add_choice("Paris", is_correct=True)
    question.add_choice("Londres", is_correct=False)
    question.add_choice("Roma", is_correct=False)
    
    return question

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

    choice = question.choices[1]
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
        Choice(1)

def test_check_choice_without_id():
    with pytest.raises(Exception):
        Choice("March 25")

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
    
def test_add_two_choices_with_same_text():
    question = Question(title='q1')
    
    question.add_choice('b', False)
    question.add_choice('b', True)

    cho1 = question.choices[0]
    cho2 = question.choices[1]
    assert len(question.choices) == 2
    assert cho1.text == 'b'
    assert not cho1.is_correct
    assert cho2.text == 'b'
    assert cho2.is_correct
    
def test_select_choices():
    question = Question(title='q1')
    
    question.add_choice('b', False)
    question.add_choice('b', True)

    choices = question.select_choices([2])
    assert(choices[0] == 2)
    
def test_add_duplicate_choices():
    question = Question(title="Which of these are fruits?")
    
    question.add_choice('Apple', True)
    question.add_choice('Apple', False)
    
    assert len(question.choices) == 2
    assert question.choices[0].text == 'Apple'
    assert question.choices[0].is_correct is True
    assert question.choices[1].text == 'Apple'
    assert question.choices[1].is_correct is False
        
def test_invalid_text_length_for_choice():
    question = Question(title="What's the largest ocean?")
    
    with pytest.raises(Exception):
        question.add_choice("", True)  
    
    with pytest.raises(Exception):
        question.add_choice("a" * 101, False)
