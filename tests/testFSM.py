import unittest
from src.core.fsm import FSM
from src.core.state import State
from src.core.transition import Transition

class TestFSM(unittest.TestCase):


    def setUp(self):
        global state1
        state1 = State()
        global state2
        state2 = State()
        self.fsm = FSM()
        global state0
        state0 = self.fsm.getState()
        transition1 = Transition("Boolean", "Jacob", "Teun")
        state0.addTransitionToState(transition1, state1)
        transition2 = Transition("Int", "Teun", "Tobias")
        state1.addTransitionToState(transition2, state2)
        self.fsm.initialiseUncheckedReceives(["Teun"])
        

    def testCorrectTransition(self):
        # test correct transition
        global state1, state0
        self.assertEqual(self.fsm.state, state0)
        transition1 = Transition("Boolean", "Jacob", "Teun")
        self.fsm.makeTransition(transition1)
        self.assertEqual(self.fsm.state, state1)

    def testIncorrectTransition(self):
        global state1
        faketransition = Transition("Integer", "Teun", "Jacob")
        transition1 = Transition("Boolean", "Jacob", "Teun")
        self.fsm.makeTransition(transition1)
        self.assertEqual(self.fsm.state, state1)
        self.fsm.makeTransition(faketransition)

if __name__ == '__main__':
    unittest.main()