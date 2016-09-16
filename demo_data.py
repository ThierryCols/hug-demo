from datetime import datetime


users = [
    {
        'id': 1,
        'name': 'John',
    }, {
        'id': 2,
        'name': 'Paul',
    }, {
        'id': 3,
        'name': 'Marc',
    }]

pronos = [{
    'id': 1,
    'gameId': 1,
    'userId': 1,
    'teamId1': 2,
    'teamId2': 1,
    'winner': 1,
}, {
    'id': 2,
    'gameId': 1,
    'userId': 3,
    'teamId1': 3,
    'teamId2': 0,
    'winner': 1,
}, {
    'id': 3,
    'gameId': 1,
    'userId': 2,
    'teamId1': 2,
    'teamId2': 3,
    'winner': 2,
}, {
    'id': 4,
    'gameId': 3,
    'userId': 2,
    'teamId1': 1,
    'teamId2': 2,
    'winner': 2,
}, {
    'id': 5,
    'gameId': 3,
    'userId': 1,
    'teamId1': 2,
    'teamId2': 1,
    'winner': 1,
}]
games = [{
    'id': 1,
    'teamId1': 1,
    'teamId2': 2,
    'gameDate': datetime(2017, 4, 10),
}, {
    'id': 2,
    'teamId1': 2,
    'teamId2': 1,
    'gameDate': datetime(2017, 4, 15),
}, {
    'id': 3,
    'teamId1': 2,
    'teamId2': 3,
    'gameDate': datetime(2017, 4, 20),
}]
results = {
    1: {
        'teamId1': 2,
        'teamId2': 1,
        'winner': 1,
    },
    3: {
        'teamId1': 2,
        'teamId2': 1,
        'winner': 1,
    }
}
activeUser = 1
teams = {
    1: {
        'teamName': 'France',
        'crest': 'path/to/crest',
    },
    2: {
        'teamName': 'Italy',
        'crest': 'path/to/crest',
    },
    3: {
        'teamName': 'Germany',
        'crest': 'path/to/crest',
    }
}
