import prompt
from brain_games.cli import welcome_user


def show_game_description(get_game_description):
    print(get_game_description())


def ask_question(question):
    print(f'Question: {question}')


def get_user_answer():
    return prompt.string('Your answer: ')


def run_game(get_game_description, get_question_answer_pair):
    username = welcome_user()
    show_game_description(get_game_description)

    required_correct_answers_count = 3
    user_correct_answers_count = 0

    while user_correct_answers_count < required_correct_answers_count:
        question, correct_answer = get_question_answer_pair()
        ask_question(question)
        user_answer = get_user_answer()

        if (user_answer == correct_answer):
            print('Correct!')
            user_correct_answers_count += 1
            continue
        else:
            false_answer_description = (
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {username}!"
            )
            print(false_answer_description)
            return
    print(f'Congratulations, {username}!')
