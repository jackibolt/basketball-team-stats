import copy
from constants import TEAMS, PLAYERS

players =  copy.deepcopy(PLAYERS)
teams = copy.deepcopy(TEAMS)

cleaned_players = []

def clean_data():
    
    for player in players:

        # create boolean for player experience
        if player['experience'] == 'YES':
            player['experience'] = True
        elif player['experience'] == 'NO':
            player['experience'] = False

        # collect/transform height into int
        player['height'] = player['height'].split(' ')[0]

        # clean up guardians
        player['guardians'] = player['guardians'].split(' and ')

        cleaned_player = {
            "name": player['name'],
            "guardians": player['guardians'],
            "experience": player['experience'],
            "height": int(player['height'])
        }

        cleaned_players.append(cleaned_player)
        # print(cleaned_players)


all_roster_details = []

def balance_teams(player_data):

    # divide experienced / non-experienced players
    experienced_players = []
    non_exp_players = []
    for player in player_data:
        if player['experience'] == True:
            experienced_players.append(player)
        else:
            non_exp_players.append(player)

    # calculate needed player numbers
    players_per_team = int(len(players) / len(teams))
    exp_players_per_team = int(len(experienced_players) / len(teams))
    non_exp_players_per_team = int(len(non_exp_players) / len(teams))


    for team in teams:

        roster_list = []

        # add players
        for i in range(0, exp_players_per_team):
            roster_list.append(experienced_players.pop(0))
        for i in range(0, non_exp_players_per_team):
            roster_list.append(non_exp_players.pop(0))

        # create team details
        team_details = {
            "team_name": team,
            "roster_list": roster_list,
            "roster_total": len(roster_list),
        }

        all_roster_details.append(team_details)


def run_app():

    # continue running the app until user quits
    while True:
        try: 
            start = input("\nWould you like to view team roster details? (y/n)  ")

            # handle if input is not y or n
            if start.lower() != 'y' and start.lower() != 'n':
                raise Exception(f'\nPlease select y/n.\n')

            # print list of team, ask user to select
            if start.lower() == 'y':
                print("\n\nHere is a list of our teams:")
                for index, team in enumerate(all_roster_details):
                    print(f"{index+1}. {team['team_name']}")
                selected_team = input('\nPlease select a team number:  ')

                # check the input is a number.
                if selected_team.isdigit() == False:
                    raise Exception(f'\nOops. This is not an integar. Please try again.')

                # check the input is within the range.
                if 1 > int(selected_team) or int(selected_team) > len(teams):
                    raise Exception(f'\nOops. Please select a number corresponding to a team on this list.\n')

                # print content for selected team
                for index, team in enumerate(all_roster_details):

                    # create/print team details
                    if selected_team == (index+1):

                        player_names = []
                        for player in team['roster_list']:
                            player_names.append(player['name'])
                        player_names = ', '.join(player_names)

                        print(f"""
    ___________________
                              
    Team Name: {team['team_name'].upper()}

    Roster Total: {team['roster_total']}

    Players: {player_names}
                               """)
                        
                        # ask if user wants more details
                        show_more = input(f"\n    ---> Would you like to see more roster details for the {team['team_name']}? (y/n)  ")
                        
                        # handle if input is not y or n
                        if show_more.lower() != 'y' and show_more.lower() != 'n':
                            raise Exception(f'Please select y/n.\n')
                        
                        #if no, quit.
                        elif show_more.lower() == "n":
                            print('_____________________\n')
                            break
                        
                        # generate/print additional details
                        else:
                            experienced_players = []
                            non_exp_players = []
                            heights = []
                            guardians = []
                            for player in team['roster_list']:
                                if player['experience'] == True:
                                    experienced_players.append(player['name'])
                                else:
                                    non_exp_players.append(player['name'])
                                heights.append(player['height'])
                                for guardian in player['guardians']:
                                    guardians.append(guardian)
                            average_height = int(sum(heights) / len(heights))


                            print(f"""
        Experienced players: ({len(experienced_players)}) - {', '.join(experienced_players)}
        Non-experienced players: ({len(non_exp_players)}) - {', '.join(non_exp_players)}
        Average height: {average_height} inches
        List of guardians: {', '.join(guardians)}
                                   """)

            else:
                print('\nYou have quit the program. See ya later.')
                break
            
        
        # print errors  
        except ValueError:
            print('That is not a integar. Please try again.')
        except Exception as e:
            print(e)

# run the program
if __name__ == "__main__":

    clean_data()
    balance_teams(cleaned_players)

    run_app()


