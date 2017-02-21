import random
from collections import namedtuple

Joke = namedtuple('Joke', ['joke', 'punchline'])


def get_joke():
    """
    http://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file-in-python
    """
    with open('jokes.csv') as joke_file:
        line = next(joke_file)

        for line_num, cur_line in enumerate(joke_file):
            if random.randrange(line_num + 2):
                continue
            line = cur_line

    line_parts = line.split(',')
    return Joke(joke=line_parts[0], punchline=line_parts[1])
