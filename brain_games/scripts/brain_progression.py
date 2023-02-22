from brain_games.progression_game import get_question_answer_pair
from brain_games.progression_game import get_game_description
from brain_games.engine import run_game


def main():
    run_game(get_game_description, get_question_answer_pair)


if __name__ == '__main__':
    main()
