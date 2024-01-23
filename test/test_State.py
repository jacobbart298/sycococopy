import unittest
from src.core.state import State
from src.core.transition import Transition, PredicateTransition

class TestState(unittest.TestCase):
    

    def testInitialization(self):

        q0 = State()
        # upon initialization q0 does not feature any transitions
        self.assertEqual(0, len(q0.getTransitions()))


    def testGetTransitions(self):

        q0 = State()
        q1 = State()
        q2 = State()
        q3 = State()
        bool_A_A = Transition(bool, "A", "A")
        bool_A_B = Transition(bool, "A", "B")
        bool_A_C = Transition(bool, "A", "C")
        p_bool_A_B = PredicateTransition(bool, "A", "B", "==", True)
        p_float_A_D = PredicateTransition(float, "A", "D", "<", -4.809)

        self.assertEqual(0, len(q0.getTransitions()))
        
        # add a reflexive transition to q0
        q0.addTransitionToState(bool_A_A, q0)
        # add the same transition to the same state twice
        q0.addTransitionToState(bool_A_B, q1)
        q0.addTransitionToState(bool_A_B, q1)
        # add the same transition but to a different state
        q0.addTransitionToState(bool_A_B, q2)
        # add a predicate variant to the same state
        q0.addTransitionToState(p_bool_A_B, q2)
        # add a different transition to the same state
        q0.addTransitionToState(bool_A_C, q2)
        # add a predicate transition to another state
        q0.addTransitionToState(p_float_A_D, q3)

        self.assertEqual(5, len(q0.getTransitions()))
        self.assertIn(bool_A_A, q0.getTransitions())
        self.assertIn(bool_A_B, q0.getTransitions())
        self.assertIn(bool_A_C, q0.getTransitions())
        self.assertIn(p_bool_A_B, q0.getTransitions())
        self.assertIn(p_float_A_D, q0.getTransitions())


    def testAddTransitionToState(self):

        q0 = State()
        q1 = State()
        q2 = State()
        q3 = State()
        bool_A_A = Transition(bool, "A", "A")
        bool_A_B = Transition(bool, "A", "B")
        bool_A_C = Transition(bool, "A", "C")
        p_bool_A_B = PredicateTransition(bool, "A", "B", "==", True)
        p_str_A_D = PredicateTransition(str, "A", "D", "!=", "hello world")

        self.assertEqual(0, len(q0.getTransitions()))

        # add a reflexive transition to q0
        q0.addTransitionToState(bool_A_A, q0)
        # add the same transition to the same state twice
        q0.addTransitionToState(bool_A_B, q1)
        q0.addTransitionToState(bool_A_B, q1)
        # add the same transition but to a different state
        q0.addTransitionToState(bool_A_B, q2)
        # add a predicate variant to the same state
        q0.addTransitionToState(p_bool_A_B, q2)
        # add a different transition to the same state
        q0.addTransitionToState(bool_A_C, q2)
        # add a predicate transition to another state
        q0.addTransitionToState(p_str_A_D, q3)

        self.assertEqual(5, len(q0.getTransitions()))
        self.assertIn(bool_A_A, q0.getTransitions())
        self.assertIn(bool_A_B, q0.getTransitions())
        self.assertIn(bool_A_C, q0.getTransitions())
        self.assertIn(p_bool_A_B, q0.getTransitions())
        self.assertIn(p_str_A_D, q0.getTransitions())

        self.assertTrue(1, len(q0.getNextStates(bool_A_A)))
        self.assertIn(q0, q0.getNextStates(bool_A_A))

        self.assertTrue(2, len(q0.getNextStates(bool_A_B)))
        self.assertIn(q1, q0.getNextStates(bool_A_B))
        self.assertIn(q2, q0.getNextStates(bool_A_B))

        self.assertTrue(1, len(q0.getNextStates(p_bool_A_B)))
        self.assertIn(q2, q0.getNextStates(p_bool_A_B))

        self.assertTrue(1, len(q0.getNextStates(bool_A_C)))
        self.assertIn(q2, q0.getNextStates(bool_A_C))

        self.assertTrue(1, len(q0.getNextStates(p_str_A_D)))
        self.assertIn(q3, q0.getNextStates(p_str_A_D))


    def testGetNextStates(self):

        q0 = State()
        q1 = State()
        q2 = State()
        q3 = State()
        bool_A_A = Transition(bool, "A", "A")
        bool_A_B = Transition(bool, "A", "B")
        bool_A_C = Transition(bool, "A", "C")
        p_bool_A_B = PredicateTransition(bool, "A", "B", "==", False)
        p_int_A_D = PredicateTransition(int, "A", "D", ">", 42)

        self.assertEqual(0, len(q0.getNextStates(bool_A_A)))
        self.assertEqual(0, len(q0.getNextStates(bool_A_B)))
        self.assertEqual(0, len(q0.getNextStates(bool_A_C)))
        self.assertEqual(0, len(q0.getNextStates(p_bool_A_B)))
        self.assertEqual(0, len(q0.getNextStates(p_int_A_D)))

        # add a reflexive transition to q0
        q0.addTransitionToState(bool_A_A, q0)
        # add the same transition to the same state twice
        q0.addTransitionToState(bool_A_B, q1)
        q0.addTransitionToState(bool_A_B, q1)
        # add the same transition but to a different state
        q0.addTransitionToState(bool_A_B, q2)
        # add a predicate variant to the same state
        q0.addTransitionToState(p_bool_A_B, q2)
        # add a different transition to the same state
        q0.addTransitionToState(bool_A_C, q2)
        # add a predicate transition to another state
        q0.addTransitionToState(p_int_A_D, q3)

        self.assertTrue(1, len(q0.getNextStates(bool_A_A)))
        self.assertIn(q0, q0.getNextStates(bool_A_A))

        self.assertTrue(2, len(q0.getNextStates(bool_A_B)))
        self.assertIn(q1, q0.getNextStates(bool_A_B))
        self.assertIn(q2, q0.getNextStates(bool_A_B))

        self.assertTrue(1, len(q0.getNextStates(p_bool_A_B)))
        self.assertIn(q2, q0.getNextStates(p_bool_A_B))

        self.assertTrue(1, len(q0.getNextStates(bool_A_C)))
        self.assertIn(q2, q0.getNextStates(bool_A_C))

        self.assertTrue(1, len(q0.getNextStates(p_int_A_D)))
        self.assertIn(q3, q0.getNextStates(p_int_A_D))

    def testIsFinalState(self):

        q0 = State()
        q1 = State()
        q2 = State()

        p_int_A_D = PredicateTransition(int, "A", "D", ">", 42)
        p_bool_D_B_True = PredicateTransition(bool, "D", "B", "==", True)
        p_bool_D_A_False = PredicateTransition(bool, "D", "A", "==", False)

        # add one transition to q0
        q0.addTransitionToState(p_int_A_D, q1)
        # add two transitions to q1
        q1.addTransitionToState(p_bool_D_A_False, q0)
        q1.addTransitionToState(p_bool_D_B_True, q2)

        # state with one transition is not a final state
        self.assertFalse(q0.isFinalState())

        # state with multiple transitions is not a final state
        self.assertFalse(q1.isFinalState())

        # state with no transitions is a final state
        self.assertTrue(q2.isFinalState())
