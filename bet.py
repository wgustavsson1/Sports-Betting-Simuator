import random
import sys


INPUT_HELP = "To run this program please specify <matches> <insert> <name of team A> <name of team B <Number of times Team A have won over Team B> <Team a return> (Ex:1.5) <Team B return> (Ex:1.5) <number of games to simulate>"
INPUT_ERROR_FEEDBACK = "ERROR: Missing some command"


def get_match_params():
    try:
        sysvars = {}
        sysvars['matches'] = int(sys.argv[1])
        sysvars['insert'] = int(sys.argv[2])
        sysvars['team_a_name'] = sys.argv[3]
        sysvars['team_b_name'] = sys.argv[4]
        sysvars['team_a_wins'] = int(sys.argv[5])
        sysvars['team_a_return'] = float(sys.argv[6])
        sysvars['team_b_return'] = float(sys.argv[7])
        sysvars['games'] = int(sys.argv[8])
    except:
        print(INPUT_ERROR_FEEDBACK)
        print(INPUT_HELP)

    return sysvars

def play():

    params = get_match_params()

    matches = params.get('matches')
    insert = params.get('insert')
    team_a_name = params.get('team_a_name')
    team_b_name = params.get('team_b_name')
    team_a_wins = params.get('team_a_wins')
    team_a_return = params.get('team_a_return')
    team_b_return = params.get('team_b_return')
    games = params.get('games')

    team_a_money, team_b_money = 0,0


    a_winning = team_a_wins/matches
    for i in range(params.get('games')):
        res = random.random()

        if 0 < res < a_winning:
            team_a_money += insert * team_a_return
            team_b_money -= insert
        
        else:
            team_b_money += insert * team_b_return
            team_a_money -= insert
            
            
    team_a_res = (int(team_a_money)/(games*insert)) - 1
    team_b_res = (int(team_b_money)/(games*insert)) -1
    team_a_res = round(team_a_res*100,2)
    team_b_res = round(team_b_res * 100,2)
    print(team_a_name + " " + str(team_a_res) + "%")
    print(team_b_name + " " + str(team_b_res)  + "%")


play()

