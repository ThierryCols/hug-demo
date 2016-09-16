from datetime import datetime, timedelta
from functools import reduce

from demo_data import *


def compute_scores():
    """ return dict with userId and its score """
    return {
        id: reduce(
            compute_user_score,
            [p for p in pronos if p['userId'] == id],
            0
        ) for id in [1, 2, 3]
    }


def compute_user_score(total, game_prono):
    """ Compute user pronos and return user score """
    game_result = results[game_prono['gameId']]
    if game_prono['winner'] != game_result['winner']:
        return total
    elif game_prono['teamId1'] == game_result['teamId1'] \
            and game_prono['teamId2'] == game_result['teamId2']:
        return total + 3
    return total + 1


def fetch_next_games():
    """ Fetch games for the next ten days """
    today = datetime(2017, 4, 6)
    in_five_days = today + timedelta(days=10)
    return [game for game in games
            if (game['gameDate'] > today and game['gameDate'] <= in_five_days)]


def add_prono(new_prono):
    """ Simply add a prono to the list """
    pronos.append(new_prono)


def fetch_user_pronos(user_id):
    """ Retrieve all pronos from a user """
    return [prono for prono in pronos if prono['userId'] == user_id]


if __name__ == '__main__':
    print(compute_scores())
    print('*******')
    print('*******')
    print(fetch_next_games())
    print('*******')
    print('*******')
    print('Adding a prono for Player 3')
    add_prono({'id': 6, 'gameId': 3, 'userId': 3, 'teamId1': 2,
                        'teamId2': 0, 'winner': 1})
    print(compute_scores())
    print('**~~**')
    print(fetch_user_pronos(1))
