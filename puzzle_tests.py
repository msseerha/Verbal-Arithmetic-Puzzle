import unittest
from a2q3.verbal_arithmetic import solve

class PuzzleTests (unittest.TestCase):

    def setUp (self):
        """Reset Z3 context between tests"""
        import z3
        z3._main_ctx = None
    def tearDown (self):
        """Reset Z3 context after test"""
        import z3
        z3._main_ctx = None
        
    def test_1 (self):
        """SEND + MORE = MONEY"""
        res = solve ('SEND', 'MORE', 'MONEY')
        self.assertEquals (res, (9567, 1085, 10652))

    def test_2 (self):
        """CORAL + ORANGE = COLORS"""
        res = solve ('CORAL', 'ORANGE', 'COLORS')
        self.assertEquals (res, (54872, 487609, 542481))
    

    def test_3 (self):
        """SATURN + URANUS = PLANETS"""
        res = solve ('SATURN', 'URANUS', 'PLANETS')
        self.assertEquals (res, (546790, 794075, 1340865))
        
    
    def test_4 (self):
        """EVERY + THREE = MONTHS"""
        res = solve ('EVERY', 'THREE', 'MONTHS')
        self.assertEquals (res, (65672, 43766, 109438))

    def test_5 (self):
        """I + DID = TOO"""
        res = solve ('I', 'DID', 'TOO')
        self.assertEquals (res, (9, 191, 200))

    def test_6 (self):
        """THREE + DAYS = GRACE""" #WITH NO SOLUTION
        res = solve ('THREE','DAYS','GRACE')
        self.assertEquals(res,None)

    def test_7 (self):
        """SOME + THING = WRONG""" #WITH NO SOLUTION
        res = solve ('SOME','THING','WRONG')
        self.assertEquals(res,None)
        
