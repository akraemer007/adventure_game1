from random import randint

die_qualities = {
    'ability': [['none'], ['success'], ['success'], ['success', 'success'], ['advantage'], ['advantage'], ['success', 'advantage'], ['advantage', 'advantage']],
    'proficiency': [['none'], ['success'], ['success'], ['success', 'success'], ['success', 'success'], ['advantage'], ['success', 'advantage'], ['success', 'advantage'], ['success', 'advantage'], ['advantage', 'advantage'], ['advantage', 'advantage'], ['triumph', 'success']],
    'boost': [['none'], ['none'], ['success'], ['success', 'advantage'], ['advantage', 'advantage'], ['advantage']],
    'difficulty': [['none'], ['failure'], ['failure', 'failure'], ['threat'], ['threat'], ['threat'], ['threat', 'threat'], ['failure', 'threat']],
    'challenge': [['none'], ['failure'], ['failure'], ['failure', 'failure'], ['failure', 'failure'], ['threat'], ['threat'], ['failure', 'threat'], ['failure', 'threat'], ['threat', 'threat'], ['threat', 'threat'], ['dispair', 'failure']],
    'setback': [['none'], ['none'], ['failure'], ['failure'], ['threat'], ['threat']],
}

def build_die_pool(ability_count=0,
                   proficency_count=0,
                   boost_count=0,
                   difficulty_count=0,
                   challenge_count=0,
                   setback_count=0,
                   die_qualities=die_qualities):

    return {'ability': ability_count,
                         'proficiency': proficency_count,
                         'boost': boost_count,
                         'difficulty': difficulty_count,
                         'challenge': challenge_count,
                         'setback': setback_count,
    }

def roll_die(die_quality):
    """Takes single die, chooses side randomly, and returns contents"""
    sides = len(die_qualities['boost'])
    die_index = randint(0, sides - 1)
    return die_qualities['boost'][die_index]

def calculate_result(rolls):
    """Takes result of rolls and calculates the net of Successes & Failues as well as net of Advantage and threat """

    results = {
        'check_result': 0,
        'side_effect_result': 0,
        'triumph': 0,
        'dispair': 0,
    }

    for roll in rolls:
        if roll == 'none':
            continue
        elif roll == 'success':
            results['check_result'] += 1
        elif roll == 'failure':
            results['check_result'] -= 1
        elif roll == 'advantage':
            results['side_effect_result'] += 1
        elif roll == 'threat':
            results['side_effect_result'] -= 1
        elif roll == 'triumph':
            results['triumph'] += 1
        elif roll == 'dispair':
            results['dispair'] += 1

    return results

def roll_die_pool(die_pool):
    rolls = []
    for die, count in die_pool.items():
        for iteration in range(count):
            roll_result = roll_die(die_qualities.get(die))
            print(roll_result)
            if 'none' not in roll_result:
                rolls = rolls + roll_result
    return calculate_result(rolls)

# print(roll_die_pool(build_die_pool(ability_count=2, difficulty_count=2)))
