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
        state0 = self.fsm.getStates()[0]
        transition1 = Transition("Boolean", "Jacob", "Teun")
        state0.addTransitionToState(transition1, state1)
        transition2 = Transition("Int", "Teun", "Tobias")
        state1.addTransitionToState(transition2, state2)
        

    def testMakeCorrectTransition(self):
        # test correct transition
        self.assertEqual(state0, self.fsm.getStates()[0], "initial state of FSM is incorrect")
        self.fsm.makeTransition(transition1)
        self.assertEqual(state1, self.fsm.getStates()[0], "state after transition is incorrect")
        # test if a newly made transition is also accepted (instead of using the global object)
        newTransition2 = Transition("Int", "Teun", "Tobias")
        self.fsm.makeTransition(newTransition2)
        self.assertEqual(state2, self.fsm.getStates()[0], "state after manually made transition is incorrect")


    def testMakeIncorrectTransition(self):
        # check if making an incorrect transition raises a generic exception
        self.assertRaises(Exception, self.fsm.makeTransition(transition2))
    
    
    def testCheckTransition(self):
        # possible transition returns True
        self.assertTrue(self.fsm.checkTransition(transition1), "checkTransition returns False for possible transition")
        # impossible transition returns False
        self.assertFalse(self.fsm.checkTransition(transition2), "checkTransition returns True for impossible transition")

    
    def testDualStateFSM(self):
        # create a non deterministic transition in state 1: to state2 or state3
        state3 = State()
        state1.addTransitionToState(transition2, state3)
        # check currently only 1 state in FSM and transition1 is and transition2 is not allowed
        self.assertEqual(1, len(self.fsm.getStates()), "Start FSM does not have a single state")
        self.assertFalse(self.fsm.checkTransition(transition2), "Transition2 already allowed start state")
        self.assertTrue(self.fsm.checkTransition(transition1), "Transition1 not allowed from start state")
        # make first transition and check FSM still only tracks one state
        self.fsm.makeTransition(transition1)
        self.assertEqual(1, len(self.fsm.getStates()), "After transition to single state, FSM does not have a single state")
        # check transition2 is and transition1 is not allowed
        self.assertTrue(self.fsm.checkTransition(transition2), "Transition2 not allowed from state1")
        self.assertFalse(self.fsm.checkTransition(transition1), "Transition1 allowed from state1")
        # make second transition and check that FSM now has two states
        self.fsm.makeTransition(transition2)
        self.assertEqual(2, len(self.fsm.getStates()), "Non deterministic transition did not lead to two states")

    
    def testMultipleStateFSM(self):
        state3 = State()
        state4 = State()
        state5 = State()
        # add non deterministic transition in state0, so there are two possible states
        state0.addTransitionToState(transition1, state3)
        # add transition2 from state3 to state4 and from state2 to state4, to check if fsm still tracks two states three transitions
        state3.addTransitionToState(transition2, state4)
        state2.addTransitionToState(transition2, state4)
        # add transition3 from state4 to state5 so transition leads to only one state in FSM
        state4.addTransitionToState(transition1, state5)
        # test start FSM has one state only
        self.assertEqual(1, len(self.fsm.getStates()), "FSM starts with incorrect state count")
        # make transition1, FSM should now have two states
        self.fsm.makeTransition(transition1)
        self.assertEqual(2, len(self.fsm.getStates()), "FM has incorrect state count after non-deterministic transition")
        # make transition2 and check that there are now 2 possible states (state4 twice, should become one element)
        self.fsm.makeTransition(transition2)
        self.assertEqual(2, len(self.fsm.getStates()), "FM has incorrect state count after non-deterministic transition")
        # make transition1 and check if only one state remains
        self.fsm.makeTransition(transition1)
        self.assertEqual(1, len(self.fsm.getStates()), "FSM has incorrect state count after deterministic transition")
        self.assertEqual(state5, self.fsm.getStates()[0], "FSM did not end up in state5")
        # add 3 identical transitions from state5 to states 0, 1, 2, 3 and 4 and check that they can all be made
        state5.addTransitionToState(transition1, state0)
        state5.addTransitionToState(transition1, state1)
        state5.addTransitionToState(transition1, state2)
        state5.addTransitionToState(transition1, state3)
        state5.addTransitionToState(transition1, state4)
        self.fsm.makeTransition(transition1)
        self.assertEqual(5, len(self.fsm.getStates()), "FSM has incorrect state count after non-deterministic transition")
                         

    def testReflexiveTransition(self):
        # create an FSM with a state that transitions to itself
        newFSM = FSM()
        startState = newFSM.getStates()[0]
        startState.addTransitionToState(transition1, startState)
        # check transition works
        newFSM.makeTransition(transition1)
        self.assertEqual(1, len(newFSM.getStates()), "incorrect stte count after reflexive transition")
        self.assertEqual(startState, newFSM.getStates()[0], "Reflexive transition did not work")

    def test_non_deterministic_equivalent_choices(self):
        fsm = FSM()        
        q0 = fsm.getStates()[0]
        q1 = State()
        q2 = State()
        q3 = State()
        transition1 = Transition("t1", "A", "B")
        transition2 = Transition("t2", "A", "B")
        q0.addTransitionToState(transition1, q1)
        q0.addTransitionToState(transition1, q2)
        q1.addTransitionToState(transition2, q3)
        q2.addTransitionToState(transition2, q3)

        fsm.makeTransition(transition1)
        # fsm should contain two states: q1 and q2
        self.assertEqual(2, len(fsm.getStates()))
        self.assertIn(q1, fsm.getStates())
        self.assertIn(q2, fsm.getStates())
        fsm.makeTransition(transition2)
        # ----- start bug illustration -----
        # fsm should contain only one instance of q3 but contains two!
        self.assertEqual(2, len(fsm.getStates()))
        q3_a = fsm.getStates()[0]
        q3_b = fsm.getStates()[1]
        self.assertEqual(q3_a, q3_b)
        # ----- end bug illustration -----
        # fsm should contain one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertIn(q3, fsm.getStates())

if __name__ == '__main__':
    unittest.main()