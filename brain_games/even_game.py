import random


def get_game_description():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_random_number(begin_number=0, end_number=100):
    return random.randint(begin_number, end_number)


def get_question_answer_pair():
    random_number = get_random_number()
    correct_answer = 'yes' if is_even(random_number) else 'no'
    return (random_number, correct_answer)
