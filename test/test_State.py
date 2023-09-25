from src.core.state import State
from src.core.transition import Transition

import unittest


class TestState(unittest.TestCase):


    def setUp(self):
        # create two states, one transition that links from state1 to state2 and a fake transition
        global state1, state2, transition, faketransition
        state1 = State()
        state2 = State()
        transition = Transition("Boolean", "Jacob", "Teun")
        faketransition = Transition("Integer", "Teun", "Jacob")
        state1.addTransitionToState(transition, state2)
    
    
    def testGetNextState(self):
        # check if an illegal transition returns None
        self.assertIsNone(state1.getNextState(faketransition), "An impossible transition did not return None")
        # check if possible transition returns the next state
        self.assertEqual(state2, state1.getNextState(transition), "A transition from state1 did not return state2")

    
    def testContainsTransition(self):
        # check if available transition returns True
        self.assertTrue(state1.containsTransition(transition), "A possible transition was not reported in containsTransition")
        # check if unavailable transition returns False, both in State with and without possible transitions
        self.assertFalse(state1.containsTransition(faketransition), "A non-existent transition was reported as available")
        self.assertFalse(state2.containsTransition(transition), "An empty transition dictionary returned true on containsTransition")

    
    def testAddTransitionToState(self):
        self.assertFalse(state2.containsTransition(transition), "Transition was already available before adding")
        # add transition and check if transition is correctly added
        state2.addTransitionToState(transition, state2)
        self.assertTrue(state2.containsTransition(transition), "Transition wasn't added in addTransitionToState function")

if __name__ == '__main__':
    unittest.main()