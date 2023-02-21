import operator
import random


def get_game_description():
    return 'What is the result of the expression?'


def get_random_operator():
    available_operators = [
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul)
    ]
    random_operator = random.choice(available_operators)
    return random_operator


def get_random_operands(begin_number=0, end_number=100):
    operand1 = random.randint(begin_number, end_number)
    operand2 = random.randint(begin_number, end_number)
    return (operand1, operand2)


def get_question_answer_pair():
    operator_repr, operator_func = get_random_operator()
    operand1, operand2 = get_random_operands()
    question = f'{operand1} {operator_repr} {operand2}'
    answer = str(operator_func(operand1, operand2))
    return (question, answer)
