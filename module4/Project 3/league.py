# ADD CASES COVERED
# ALL TESTS PASSING
from identified_object import IdentifiedObject

class League(IdentifiedObject):

    @property
    def name(self): # name is read-write property, needs a setter
        return self._name

    @name.setter
    def name(self, name): # setter for name
        self._name = name

    @property
    def teams(self): # list of teams participating in this league, read only property
        return self._teams

    @property
    def competitions(self): # list of competitions (games), read only property
        return self._competitions


    # initialization method that sets the oid and name properties as
    # specified in the arguments (note: should call superclass constructor)
    def __init__(self, oid, name):
        super().__init__(oid) # calling super() from ancestor
        self._name = name
        self._teams = [] # use brackets to notate as list
        self._competitions = [] # use brackets to notate as list

    # add team to the teams collection unless
    # they are already in it (in which case do nothing)
    # Python Crash Course 2nd ed. "cheat sheet"
    def add_team(self, team):
        if team not in self._teams:
            self._teams.append(team) # build the teams list using .append()

    # remove the team if they are in the teams list, otherwise do nothing
    def remove_team(self, team):
        if team in self._teams:
            self._teams.remove(team) # remove the teams from the teams list using .remove()

    # return the team in this league whose name equals team_name
    # (case sensitive) or None if no such team exists
    def team_named(self, team_name):
        for team in self._teams: # for team in team list
            if team.name == team_name: # "whose name equals team_name"
                return team # return the team
        return None # or none if not such team exists

    # add competition to the competitions collection
    def add_competition(self, competition):
        self._competitions.append(competition) # append comp to comp list

    # return a list of all teams for which member plays
    def teams_for_member(self, member):
        teams_for_member_list = [] # list to hold teams of members
        for team in self._teams: # for loop to iterate over teams in the list of teams
            if member in team.members: # check if members are on team
                teams_for_member_list.append(team) # if on team, append team to new team list
        return teams_for_member_list


    # return a list of all competitions in which team is participating
    def competitions_for_team(self, team):
        competitions_for_team_list = [] # list to hold all comp of teams participating
        for competition in self._competitions: # for loop to iterate over comps in list of comps
            if team in competition.teams_competing: # check if team is competing
                competitions_for_team_list.append(competition) # if competing, append comp to comp team list
        return competitions_for_team_list

    # return a list of all competitions for which
    # member played on one of the competing teams
    def competitions_for_member(self, member):
        competitions_for_member_list = [] # list to hold all comp where member played on competing team
        for competition in self._competitions: # for loop to iterate over comps in list of comps
            for team in competition.teams_competing: # nested loop used to iterate over competing teams of all teams
                if member in team.members: # checks if members are on team
                    competitions_for_member_list.append(competition) # if on competing team, append comp to new comp member list
                    break # break out of inner loop after finding competing team
        return competitions_for_member_list

    # return a string resembling the following:
    # League Name: N teams, M competitions" where N and M
    # are replaced by the obvious values
    def __str__(self):
        return f"League Name: {self.teams} teams, {self.competitions} competitions"

