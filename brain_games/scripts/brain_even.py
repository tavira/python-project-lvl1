from brain_games.cli import welcome_user
from brain_games.even_game import even_game


def main():
    username = welcome_user()
    even_game(username)


if __name__ == '__main__':
    main()