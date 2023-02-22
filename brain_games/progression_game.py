import random


def get_game_description():
    return 'What number is missing in the progression?'


def get_progression(progression_length):
    progression_start_number = random.randint(0, 100)
    progression_difference = random.randint(1, 10)
    progression = []
    for i in range(0, progression_length):
        progression.append(
            progression_start_number + i * progression_difference
        )
    return progression


def get_random_hidden_index(progression_length):
    return random.randint(0, progression_length - 1)


def make_question(progression, hidden_index):
    progression_text_before_hidden_index = \
        ' '.join(str(x) for x in progression[:hidden_index])
    progression_text_after_hidden_index = \
        ' '.join(str(x) for x in progression[hidden_index + 1:])
    if hidden_index == 0:
        return '.. ' + progression_text_after_hidden_index
    if hidden_index == len(progression) - 1:
        return progression_text_before_hidden_index + ' ..'
    return progression_text_before_hidden_index + \
        ' .. ' + \
        progression_text_after_hidden_index


def get_question_answer_pair():
    progression_length = 10
    progression = get_progression(progression_length)
    hidden_index = get_random_hidden_index(progression_length)
    question = make_question(progression, hidden_index)
    answer = str(progression[hidden_index])
    return (question, answer)


if __name__ == '__main__':
    print(get_question_answer_pair())
