from src.core.state import State
from src.core.transition import Transition

import unittest


class TestState(unittest.TestCase):
    

    def testInitialization(self):

        q0 = State()
        # upon initialization q0 does not feature any transitions
        self.assertEqual(0, len(q0.getTransitions()))


    def testGetTransitions(self):

        q0 = State()
        q1 = State()
        q2 = State()
        bool_A_A = Transition("bool", "A", "A")
        bool_A_B = Transition("bool", "A", "B")
        bool_A_C = Transition("bool", "A", "C")

        self.assertEqual(0, len(q0.getTransitions()))
        
        # add a reflexive transition to q0
        q0.addTransitionToState(bool_A_A, q0)
        # add the same transition to the same state twice
        q0.addTransitionToState(bool_A_B, q1)
        q0.addTransitionToState(bool_A_B, q1)
        # add the same transition but to a different state
        q0.addTransitionToState(bool_A_B, q2)
        # add a different transition to the same state
        q0.addTransitionToState(bool_A_C, q2)

        self.assertEqual(3, len(q0.getTransitions()))
        self.assertIn(bool_A_A, q0.getTransitions())
        self.assertIn(bool_A_B, q0.getTransitions())
        self.assertIn(bool_A_C, q0.getTransitions())


    def testContainsTransition(self):

        q0 = State()
        q1 = State()
        q2 = State()
        bool_A_A = Transition("bool", "A", "A")
        bool_A_B = Transition("bool", "A", "B")
        bool_A_C = Transition("bool", "A", "C")

        self.assertFalse(q0.containsTransition(bool_A_A))
        self.assertFalse(q0.containsTransition(bool_A_B))
        self.assertFalse(q0.containsTransition(bool_A_C))

        # add a reflexive transition to q0
        q0.addTransitionToState(bool_A_A, q0)
        # add the same transition to the same state twice
        q0.addTransitionToState(bool_A_B, q1)
        q0.addTransitionToState(bool_A_B, q1)
        # add the same transition but to a different state
        q0.addTransitionToState(bool_A_B, q2)
        # add a different transition to the same state
        q0.addTransitionToState(bool_A_C, q2)

        self.assertTrue(q0.containsTransition(bool_A_A))
        self.assertTrue(q0.containsTransition(bool_A_B))
        self.assertTrue(q0.containsTransition(bool_A_C))


    def testAddTransitionToState(self):

        q0 = State()
        q1 = State()
        q2 = State()
        bool_A_A = Transition("bool", "A", "A")
        bool_A_B = Transition("bool", "A", "B")
        bool_A_C = Transition("bool", "A", "C")

        self.assertEqual(0, len(q0.getTransitions()))

        # add a reflexive transition to q0
        q0.addTransitionToState(bool_A_A, q0)
        # add the same transition to the same state twice
        q0.addTransitionToState(bool_A_B, q1)
        q0.addTransitionToState(bool_A_B, q1)
        # add the same transition but to a different state
        q0.addTransitionToState(bool_A_B, q2)
        # add a different transition to the same state
        q0.addTransitionToState(bool_A_C, q2)

        self.assertEqual(3, len(q0.getTransitions()))
        self.assertTrue(q0.containsTransition(bool_A_A))
        self.assertTrue(q0.containsTransition(bool_A_B))
        self.assertTrue(q0.containsTransition(bool_A_C))

        self.assertTrue(1, len(q0.getNextStates(bool_A_A)))
        self.assertIn(q0, q0.getNextStates(bool_A_A))

        self.assertTrue(2, len(q0.getNextStates(bool_A_B)))
        self.assertIn(q1, q0.getNextStates(bool_A_B))
        self.assertIn(q2, q0.getNextStates(bool_A_B))

        self.assertTrue(1, len(q0.getNextStates(bool_A_C)))
        self.assertIn(q2, q0.getNextStates(bool_A_C))


    def testGetNextStates(self):

        q0 = State()
        q1 = State()
        q2 = State()
        bool_A_A = Transition("bool", "A", "A")
        bool_A_B = Transition("bool", "A", "B")
        bool_A_C = Transition("bool", "A", "C")

        self.assertEqual(0, len(q0.getNextStates(bool_A_A)))
        self.assertEqual(0, len(q0.getNextStates(bool_A_B)))
        self.assertEqual(0, len(q0.getNextStates(bool_A_C)))

        # add a reflexive transition to q0
        q0.addTransitionToState(bool_A_A, q0)
        # add the same transition to the same state twice
        q0.addTransitionToState(bool_A_B, q1)
        q0.addTransitionToState(bool_A_B, q1)
        # add the same transition but to a different state
        q0.addTransitionToState(bool_A_B, q2)
        # add a different transition to the same state
        q0.addTransitionToState(bool_A_C, q2)

        self.assertTrue(1, len(q0.getNextStates(bool_A_A)))
        self.assertIn(q0, q0.getNextStates(bool_A_A))

        self.assertTrue(2, len(q0.getNextStates(bool_A_B)))
        self.assertIn(q1, q0.getNextStates(bool_A_B))
        self.assertIn(q2, q0.getNextStates(bool_A_B))

        self.assertTrue(1, len(q0.getNextStates(bool_A_C)))
        self.assertIn(q2, q0.getNextStates(bool_A_C))


if __name__ == '__main__':
    unittest.main()
