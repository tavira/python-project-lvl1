import random


def get_game_description():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_random_number(begin_number=0, end_number=100):
    return random.randint(begin_number, end_number)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True


def get_question_answer_pair():
    random_number = get_random_number()
    question = str(random_number)
    answer = 'yes' if is_prime(random_number) else 'no'
    return (question, answer)
