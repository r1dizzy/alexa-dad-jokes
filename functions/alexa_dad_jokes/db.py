import random
from collections import namedtuple
import os

module_path = os.path.abspath(__file__)
joke_dir = os.path.dirname(module_path)
joke_filepath = os.path.join(os.sep, joke_dir, 'jokes.csv')

Joke = namedtuple('Joke', ['joke', 'punchline'])


def get_joke():
    """
    http://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file-in-python
    """
    with open(joke_filepath) as joke_file:
        line = next(joke_file)

        for line_num, cur_line in enumerate(joke_file):
            if random.randrange(line_num + 2):
                continue
            line = cur_line

    line_parts = line.split(',')
    return Joke(joke=line_parts[0], punchline=line_parts[1])
