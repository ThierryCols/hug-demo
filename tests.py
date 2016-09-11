from demo_data import *
from main import *


def test_compute_scores():
    expected_result = {1: 6, 2: 0, 3: 1}
    assert compute_scores(results) == expected_result


def test_fetch_next_games():
    assert len(fetch_next_games()) == 2


def test_add_prono():
    assert len(pronos) == 5
    add_prono({'id': 6, 'gameId': 3, 'userId': 3, 'teamId1': 2,
                        'teamId2': 0, 'winner': 1})
    assert len(pronos) == 6
    new_expected_result = {1: 6, 2: 0, 3: 2}
    assert compute_scores(results) == new_expected_result


def test_fetch_user_pronos():
    assert len(fetch_user_pronos(1)) == 2
