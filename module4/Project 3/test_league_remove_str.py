# used similar tests from professor
# tests that implement the remove_team and __str__ methods in league class

from competition import Competition
from league import League
from team import Team
from team_member import TeamMember
import unittest


class LeagueTestsB(unittest.TestCase):
    # opposite of add_team
    def test_remove_team(self):
        t = Team(1, "Ice Maniacs")
        league = League(1, "AL State Curling League")
        league.add_team(t)
        self.assertIn(t, league.teams)
        league.remove_team(t)
        self.assertNotIn(t, league.teams)

    def test_str(self):
        l_1 = League(1, "name")
        l_2 = League(1, "other name")
        self.assertEqual("League Name: [] teams, [] competitions", str(l_1))
        self.assertEqual("League Name: [] teams, [] competitions", str(l_2))


if __name__ == '__main__':
    unittest.main()

