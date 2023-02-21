from math import gcd
from random import randint


def get_game_description():
    return 'Find the greatest common divisor of given numbers.'


def get_random_numbers(begin_number=0, end_number=100):
    number1 = randint(begin_number, end_number)
    number2 = randint(begin_number, end_number)
    return (number1, number2)


def get_question_answer_pair():
    number1, number2 = get_random_numbers()
    question = f'{number1} {number2}'
    answer = str(gcd(number1, number2))
    return (question, answer)
