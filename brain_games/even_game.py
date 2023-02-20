import random
import prompt


def show_game_description():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number):
    return number % 2 == 0


def run(username):
    right_answers_count = 0
    required_right_answers_count = 3

    while right_answers_count < required_right_answers_count:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')

        user_answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if is_even(random_number) else 'no'

        if (user_answer == correct_answer):
            right_answers_count += 1
            print('Correct!')
        else:
            false_answer_description = (
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {username}!"
            )
            print(false_answer_description)
            return
    print(f'Congratulations, {username}!')


def even_game(username):
    show_game_description()
    run(username)
