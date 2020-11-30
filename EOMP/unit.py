import unittest

#test if your age is in range
class AgeTest(unittest.TestCase):
    def testentry(self):

        x= 19
        msg="False"
        self.assertIn(x, range(18, 100), msg)


