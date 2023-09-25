import unittest
from src.core.fsm import FSM
from src.core.state import State
from src.core.transition import Transition

class TestFSM(unittest.TestCase):


    def setUp(self):
        global state0, state1, state2, transition1, transition2 
        state1 = State()
        state2 = State()
        self.fsm = FSM()
        state0 = self.fsm.getState()
        transition1 = Transition("Boolean", "Jacob", "Teun")
        state0.addTransitionToState(transition1, state1)
        transition2 = Transition("Int", "Teun", "Tobias")
        state1.addTransitionToState(transition2, state2)
        

    def testMakeCorrectTransition(self):
        # test correct transition
        self.assertEqual(state0, self.fsm.getState(), "initial state of FSM is incorrect")
        self.fsm.makeTransition(transition1)
        self.assertEqual(state1, self.fsm.getState(), "state after transition is incorrect")
        # test if a newly made transition is also accepted (instead of using the global object)
        newTransition2 = Transition("Int", "Teun", "Tobias")
        self.fsm.makeTransition(newTransition2)
        self.assertEqual(state2, self.fsm.getState(), "state after manually made transition is incorrect")


    def testMakeIncorrectTransition(self):
        # check if making an incorrect transition raises a generic exception
        self.assertRaises(Exception, self.fsm.makeTransition(transition2))
    
    
    def testCheckTransition(self):
        # possible transition returns True
        self.assertTrue(self.fsm.checkTransition(transition1), "checkTransition returns False for possible transition")
        # impossible transition returns False
        self.assertFalse(self.fsm.checkTransition(transition2), "checkTransition returns True for impossible transition")


if __name__ == '__main__':
    unittest.main()