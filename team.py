from tabulate import tabulate
from update import update_team
import getters as get


class Team:

    def __init__(self, pokemon, box, team):
        self.pokemon = pokemon
        self.box = box

        self.team_list = team

    def add_mon(self, name):
        for x in range(len(self.box)):
            if name == self.box[x][0]:
                self.team_list.append(self.box[x])
                print(tabulate(self.team_list))

    def remove_mon(self, name):
        for x,foo in enumerate(self.team_list):
            if name == self.team_list[x][0]:
                self.team_list.pop(x)
                print(tabulate(self.team_list))

    def get_team_types(self):
        player_types = {}

        for index, player in enumerate(get.players()):
            player_types[player] = []
            for mon in self.team_list[1:]:
                player_types[player].append(get.pokemon_type(mon[index + 1]))

            # squashes the lists
            player_types[player] = sum(player_types[player], [])

        return player_types

    def eligible_mons(self):
        player_types = self.get_team_types()
        print(tabulate(player_types, headers = get.players()))

        # get a list of pokemon that aren't those types for each player

        # get a list of all of the pokemon the players have in common

    def menu(self):
        response = 'NULL'
        while response:
            print('CURRENT TEAM\n' + tabulate(self.team_list))
            print('1. add\n'
                  '2. remove\n')

            response = input()

            if response == '1' or response == 'add' or response == 'a':
                name = 'NULL'
                while name:
                    name = input()
                    self.add_mon(name)
                    update_team(self.team_list)
            elif response == '2' or response == 'remove' or response == 'rm':
                name = 'NULL'
                while name:
                    name = input()
                    self.remove_mon(name)
                    update_team(self.team_list)
