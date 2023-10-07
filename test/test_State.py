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
        self.assertEqual([], state1.getNextStates(faketransition), "An impossible transition did not return an empty list")
        # check if possible transition returns the next state
        self.assertEqual(state2, state1.getNextStates(transition)[0], "A transition from state1 did not return state2")

    
    def testContainsTransition(self):
        # check if available transition returns True
        self.assertTrue(state1.containsTransition(transition), "A possible transition was not reported in containsTransition")
        # check if unavailable transition returns False, both in State with and without possible transitions
        self.assertFalse(state1.containsTransition(faketransition), "A non-existent transition was reported as available")
        self.assertFalse(state2.containsTransition(transition), "An empty transition dictionary returned true on containsTransition")
        # check transition is reported as possible if in a list of two possible transitions
        state1.addTransitionToState(faketransition, state2)
        self.assertTrue(state1.containsTransition(transition), "A possible transition was not reported in containsTransition")
        self.assertTrue(state1.containsTransition(faketransition), "A possible transition was not reported in containsTransition")

    
    def testAddTransitionToState(self):
        self.assertFalse(state2.containsTransition(transition), "Transition was already available before adding")
        # add transition and check if transition is correctly added
        state2.addTransitionToState(transition, state2)
        self.assertTrue(state2.containsTransition(transition), "Transition wasn't added in addTransitionToState function")
        # add same transition to another state and check correctly added
        self.assertEqual(1, len(state2.getNextStates(transition)), "Incorrect state count returned for deterministic transition")
        state2.addTransitionToState(transition, state1)
        self.assertEqual(2, len(state2.getNextStates(transition)), "Incorrect state count returned for non-deterministic transition")
        
    def testGetNextStates(self):
        # add non deterministc transition to state1 and check if two states are returned to transition
        state3 = State()
        state1.addTransitionToState(transition, state3)
        self.assertEqual(2, len(state1.getNextStates(transition)), "Incorrect state count returned for non-deterministic transition")

    def test_add_same_transition_twice_to_one_state(self):
        q0 = State()
        q1 = State()
        transition1 = Transition("t1", "A", "B")
        self.assertFalse(q0.containsTransition(transition1))
        # add transition (transition1, q1) to state q0
        q0.addTransitionToState(transition1, q1)
        self.assertTrue(q0.containsTransition(transition1))
        self.assertEqual(1, len(q0.getNextStates(transition1)))
        # add transition (transition1, state1) to state q0 once more: should not make a difference
        q0.addTransitionToState(transition1, q1)
        self.assertTrue(q0.containsTransition(transition1))
        self.assertEqual(1, len(q0.getNextStates(transition1)), "It does make a difference...")     

if __name__ == '__main__':
    unittest.main()