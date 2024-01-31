from wordle import load_dictionary
from wordle import is_valid_guess
from wordle import evaluate_guess

def is_valid_guess(x):
    return x + 1

def test_valid_guess():
    assert is_valid_guess(3) == 5