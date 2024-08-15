# used similar tests from professor
# tests that implement the send_email and __str__ methods in competition class
from datetime import datetime
import unittest
from fake_emailer import FakeEmailer

from competition import Competition
from team import Team
from team_member import TeamMember

class CompetitionTestsB(unittest.TestCase):
    def test_send_email(self):
        tm1 = TeamMember(1, "name", "email")
        tm2 = TeamMember(2, "other name", "other email")

        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")

        t1.add_member(tm1)
        t2.add_member(tm2)

        competition = Competition(1, [t1, t2], "location", None)

        fe = FakeEmailer()

        competition.send_email(fe, "subject", "message")

        self.assertIn("email", fe.recipients)
        self.assertEqual("subject", fe.subject)
        self.assertEqual("message", fe.message)


    def test_str(self):
        date_time_format = datetime.now().strftime("%m/%d/%Y %H:%M")
        cmp1 = Competition(1, [], "location", date_time_format)
        cmp2 = Competition(2, [], "other location", None)

        # Test string representation with datetime
        self.assertEqual(f"Competition at location on {date_time_format} with [] teams", str(cmp1))

        # Test string representation without datetime
        self.assertEqual(f"Competition at other location with [] teams", str(cmp2))


if __name__ == '__main__':
    unittest.main()



