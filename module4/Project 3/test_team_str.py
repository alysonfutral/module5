# used similar tests from professor
# test that implements the __str__ methods in team class

from team import Team
import unittest


class TeamStringTest(unittest.TestCase):
    def test_str(self):
        t_1 = Team(1, "name")
        t_2 = Team(1, "other name")
        self.assertEqual("name [] members", str(t_1))
        self.assertEqual("other name [] members", str(t_2))

if __name__ == '__main__':
    unittest.main()
