import unittest
from src.core.fsm import FSM
from src.core.state import State
from src.core.transition import Transition, PredicateTransition

# Method "makeTransition" is always called with a Transition object as the first parameter.
# This test set is limited to this scenario.
class TestFSM(unittest.TestCase):


    def testInitializationFSM(self):

        fsm = FSM()

        # Upon initialization the fsm manages one state
        self.assertEqual(1, len(fsm.getStates()))


    def testSingleStateWithNoTransitionsIllegalTransition(self):

        fsm = FSM()

        float_A_B = Transition(float, "A", "B")

        transitionMade = fsm.makeTransition(float_A_B, -42.1337)
        self.assertFalse(transitionMade)
        self.assertEqual(0, len(fsm.getStates()))


    def testSingleStateWithOneTransitionIllegalTransition(self):

        fsm = FSM()

        q0 = fsm.getStates()[0]
        q1 = State()

        bool_A_B = Transition(bool, "A", "B")
        p_bool_A_B_True = PredicateTransition(bool, "A", "B", "==", True)

        q0.addTransitionToState(p_bool_A_B_True, q1)

        transitionMade = fsm.makeTransition(bool_A_B, False)
        self.assertFalse(transitionMade)
        self.assertEqual(0, len(fsm.getStates()))


    def testSingleStateWithMultipleTransitionsIllegalTransition(self):

        fsm = FSM()

        q0 = fsm.getStates()[0]
        q1 = State()
        q2 = State()

        int_A_B = Transition(int, "A", "B")
        p_bool_A_B_True = PredicateTransition(bool, "A", "B", "==", True)
        p_bool_A_B_False = PredicateTransition(bool, "A", "B", "==", False)

        q0.addTransitionToState(p_bool_A_B_True, q1)
        q0.addTransitionToState(p_bool_A_B_False, q2)

        transitionMade = fsm.makeTransition(int_A_B, 0)
        self.assertFalse(transitionMade)
        self.assertEqual(0, len(fsm.getStates()))


    def testSingleStateWithOneReflexiveTransitionLegalTransition(self):

        fsm = FSM()

        q0 = fsm.getStates()[0]

        str_A_B = Transition(str, "A", "B")
        p_str_A_B = PredicateTransition(str, "A", "B", "==", "hello world")

        q0.addTransitionToState(p_str_A_B, q0)

        transitionMade = fsm.makeTransition(str_A_B, "hello world")
        self.assertTrue(transitionMade)
        self.assertEqual(1, len(fsm.getStates()))
        self.assertIn(q0, fsm.getStates())


    def testSingleStateWithOneTransitionOneLegalTransition(self):

        fsm = FSM()

        q0 = fsm.getStates()[0]
        q1 = State()

        bool_A_B = Transition(bool, "A", "B")
        p_bool_A_B = PredicateTransition(bool, "A", "B", "==", False)

        q0.addTransitionToState(p_bool_A_B, q1)

        transitionMade = fsm.makeTransition(bool_A_B, False)
        self.assertTrue(transitionMade)
        self.assertEqual(1, len(fsm.getStates()))
        self.assertIn(q1, fsm.getStates())


    def testSingleStateWithMultipleTransitionsOneLegalTransition(self):

        fsm = FSM()

        q0 = fsm.getStates()[0]
        q1 = State()
        q2 = State()

        int_A_B = Transition(int, "A", "B")
        p_int_A_B_1024 = PredicateTransition(int, "A", "B", ">=", 1024)
        p_int_A_B_2048 = PredicateTransition(int, "A", "B", ">=", 2048)

        q0.addTransitionToState(p_int_A_B_1024, q1)
        q0.addTransitionToState(p_int_A_B_2048, q2)

        transitionMade = fsm.makeTransition(int_A_B, 1536)
        self.assertTrue(transitionMade)
        self.assertEqual(1, len(fsm.getStates()))
        self.assertIn(q1, fsm.getStates())


    def testSingleStateWithMultipleTransitionsMultipleLegalTransitions(self):

        fsm = FSM()

        q0 = fsm.getStates()[0]
        q1 = State()
        q2 = State()

        int_A_B = Transition(int, "A", "B")
        p_int_A_B_1024 = PredicateTransition(int, "A", "B", ">", 1024)
        p_int_A_B_2048 = PredicateTransition(int, "A", "B", ">", 2048)

        q0.addTransitionToState(p_int_A_B_1024, q1)
        q0.addTransitionToState(p_int_A_B_2048, q2)

        transitionMade = fsm.makeTransition(int_A_B, 4096)
        self.assertTrue(transitionMade)
        self.assertEqual(2, len(fsm.getStates()))
        self.assertIn(q1, fsm.getStates())
        self.assertIn(q2, fsm.getStates())


    def testMultipleStatesWithNoTransitionsIllegalTransition(self):
         
        fsm = FSM()

        q0 = fsm.getStates()[0]
        q1 = State()
        q2 = State()

        bool_B_C = Transition(bool, "B", "C")
        int_A_B = Transition(int, "A", "B")
        p_int_A_B_169 = PredicateTransition(int, "A", "B", "<", 169)
        p_int_A_B_42 = PredicateTransition(int, "A", "B", ">", 42)

        q0.addTransitionToState(p_int_A_B_169, q1)
        q0.addTransitionToState(p_int_A_B_42, q2)

        transitionMade = fsm.makeTransition(int_A_B, 111)
        self.assertTrue(transitionMade)
        self.assertEqual(2, len(fsm.getStates()))
        self.assertIn(q1, fsm.getStates())
        self.assertIn(q2, fsm.getStates())

        transitionMade = fsm.makeTransition(bool_B_C, True)
        self.assertFalse(transitionMade)
        self.assertEqual(0, len(fsm.getStates()))


    def testMultipleStatesWithOneTransitionIllegalTransition(self):
         
        fsm = FSM()

        q0 = fsm.getStates()[0]
        q1 = State()
        q2 = State()
        q3 = State()
        q4 = State()

        str_C_D = Transition(str, "C", "D")
        int_A_B = Transition(int, "A", "B")
        p_int_A_B_169 = PredicateTransition(int, "A", "B", "<", 169)
        p_int_A_B_42 = PredicateTransition(int, "A", "B", ">", 42)
        p_bool_B_C_True = PredicateTransition(bool, "B", "C", "==", True)
        p_bool_B_C_False= PredicateTransition(bool, "B", "C", "==", True)

        q0.addTransitionToState(p_int_A_B_169, q1)
        q0.addTransitionToState(p_int_A_B_42, q2)
        q1.addTransitionToState(p_bool_B_C_True, q3)
        q2.addTransitionToState(p_bool_B_C_False, q4)

        transitionMade = fsm.makeTransition(int_A_B, 111)
        self.assertTrue(transitionMade)
        self.assertEqual(2, len(fsm.getStates()))
        self.assertIn(q1, fsm.getStates())
        self.assertIn(q2, fsm.getStates())

        transitionMade = fsm.makeTransition(str_C_D, "hello world")
        self.assertFalse(transitionMade)
        self.assertEqual(0, len(fsm.getStates()))
        

    def testMultipleStatesWithMultipleTransitionsIllegalTransition(self):
        
        fsm = FSM()

        q0 = fsm.getStates()[0]
        q1 = State()
        q2 = State()
        q3 = State()
        q4 = State()

        str_C_D = Transition(str, "C", "D")
        int_A_B = Transition(int, "A", "B")
        p_int_A_B_169 = PredicateTransition(int, "A", "B", "<", 169)
        p_int_A_B_42 = PredicateTransition(int, "A", "B", ">", 42)
        p_bool_B_C_True = PredicateTransition(bool, "B", "C", "==", True)
        p_bool_B_C_False= PredicateTransition(bool, "B", "C", "==", True)
        p_str_B_C_hello = PredicateTransition(str, "B", "C", "==", "hello")
        p_str_B_C_world = PredicateTransition(str, "B", "C", "==", "world")

        q0.addTransitionToState(p_int_A_B_169, q1)
        q0.addTransitionToState(p_int_A_B_42, q2)
        q1.addTransitionToState(p_bool_B_C_True, q3)
        q1.addTransitionToState(p_str_B_C_hello, q4)
        q2.addTransitionToState(p_bool_B_C_False, q3)
        q2.addTransitionToState(p_str_B_C_world, q4)

        transitionMade = fsm.makeTransition(int_A_B, 111)
        self.assertTrue(transitionMade)
        self.assertEqual(2, len(fsm.getStates()))
        self.assertIn(q1, fsm.getStates())
        self.assertIn(q2, fsm.getStates())

        transitionMade = fsm.makeTransition(str_C_D, "hello")
        self.assertFalse(transitionMade)
        self.assertEqual(0, len(fsm.getStates()))


    def testMultipleStatesWithOneTransitionOneLegalTransition(self):
       
        fsm = FSM()
        
        q0 = fsm.getStates()[0]
        q1 = State()
        q2 = State()
        q3 = State()
        q4 = State()
        q5 = State()

        int_A_B = Transition(int, "A", "B")
        p_int_A_B_10 = PredicateTransition(int, "A", "B", ">", 10)
        p_int_A_B_20 = PredicateTransition(int, "A", "B", ">", 20)
        p_int_A_B_30 = PredicateTransition(int, "A", "B", ">", 30)

        int_B_C = Transition(int, "B", "C")
        p_int_B_C = PredicateTransition(int, "B", "C", "==", 42)
        p_float_B_C = PredicateTransition(float, "B", "C", "<", 13.37)

        q0.addTransitionToState(p_int_A_B_10, q1)
        q0.addTransitionToState(p_int_A_B_20, q2)
        q0.addTransitionToState(p_int_A_B_30, q3)
        q1.addTransitionToState(p_int_B_C, q4)
        q2.addTransitionToState(p_float_B_C, q5)

        transitionMade = fsm.makeTransition(int_A_B, 40)
        self.assertTrue(transitionMade)
        self.assertEqual(3, len(fsm.getStates()))
        self.assertIn(q1, fsm.getStates())
        self.assertIn(q2, fsm.getStates())
        self.assertIn(q3, fsm.getStates())

        transitionMade = fsm.makeTransition(int_B_C, 42)
        self.assertTrue(transitionMade)
        self.assertEqual(1, len(fsm.getStates()))
        self.assertIn(q4, fsm.getStates())


    def testMultipleStatesWithSameTransitionOneLegalTransition(self):
       
        fsm = FSM()
        
        q0 = fsm.getStates()[0]
        q1 = State()
        q2 = State()
        q3 = State()
        q4 = State()

        int_A_B = Transition(int, "A", "B")
        p_int_A_B_10 = PredicateTransition(int, "A", "B", ">", 10)
        p_int_A_B_20 = PredicateTransition(int, "A", "B", ">", 20)
        p_int_A_B_30 = PredicateTransition(int, "A", "B", ">", 30)

        bool_B_C = Transition(bool, "B", "C")
        p_bool_B_C = PredicateTransition(bool, "B", "C", "==", True)

        q0.addTransitionToState(p_int_A_B_10, q1)
        q0.addTransitionToState(p_int_A_B_20, q2)
        q0.addTransitionToState(p_int_A_B_30, q3)
        q1.addTransitionToState(p_bool_B_C, q4)
        q2.addTransitionToState(p_bool_B_C, q4)

        transitionMade = fsm.makeTransition(int_A_B, 40)
        self.assertTrue(transitionMade)
        self.assertEqual(3, len(fsm.getStates()))
        self.assertIn(q1, fsm.getStates())
        self.assertIn(q2, fsm.getStates())
        self.assertIn(q3, fsm.getStates())

        transitionMade = fsm.makeTransition(bool_B_C, True)
        self.assertTrue(transitionMade)
        self.assertEqual(1, len(fsm.getStates()))
        self.assertIn(q4, fsm.getStates())


    def testMultipleStatesWithOneTransitionMultipleLegalTransitions(self):

        fsm = FSM()
        
        q0 = fsm.getStates()[0]
        q1 = State()
        q2 = State()
        q3 = State()
        q4 = State()

        bool_A_B = Transition(bool, "A", "B")
        p_bool_A_B_True = PredicateTransition(bool, "A", "B", "==", True)
        int_B_C = Transition(int, "B", "C")
        p_int_B_C_42 = PredicateTransition(int, "B", "C", "==", 42)

        q0.addTransitionToState(bool_A_B, q1)
        q0.addTransitionToState(p_bool_A_B_True, q2)
        q1.addTransitionToState(int_B_C, q3)
        q2.addTransitionToState(p_int_B_C_42, q4)

        transitionMade = fsm.makeTransition(bool_A_B, True)
        self.assertTrue(transitionMade)
        self.assertEqual(2, len(fsm.getStates()))
        self.assertIn(q1, fsm.getStates())
        self.assertIn(q2, fsm.getStates())

        transitionMade = fsm.makeTransition(int_B_C, 42)
        self.assertTrue(transitionMade)
        self.assertEqual(2, len(fsm.getStates()))
        self.assertIn(q3, fsm.getStates())
        self.assertIn(q4, fsm.getStates())
          

    def testMultipleStatesWithMultipleTransitionsOneLegalTransition(self):

        fsm = FSM()
        
        q0 = fsm.getStates()[0]
        q1 = State()
        q2 = State()
        q3 = State()
        q4 = State()
        q5 = State()
        q6 = State()
        q7 = State()

        int_B_C = Transition(int, "B", "C")
        bool_A_B = Transition(bool, "A", "B")
        bool_B_C = Transition(bool, "B", "C")
        p_int_B_C_42 = PredicateTransition(int, "B", "C", "==", 42)
        p_bool_A_B_True = PredicateTransition(bool, "A", "B", "==", True)
        p_bool_B_C_False = PredicateTransition(bool, "B", "C", "==", False)
        p_bool_B_C_True = PredicateTransition(bool, "B", "C", "==", True)

        q0.addTransitionToState(bool_A_B, q1)
        q0.addTransitionToState(p_bool_A_B_True, q2)
        q1.addTransitionToState(int_B_C, q3)
        q1.addTransitionToState(p_bool_B_C_False, q4)
        q2.addTransitionToState(p_int_B_C_42, q5)
        q2.addTransitionToState(int_B_C, q6)
        q2.addTransitionToState(p_bool_B_C_True, q7)

        transitionMade = fsm.makeTransition(bool_A_B, True)
        self.assertTrue(transitionMade)
        self.assertEqual(2, len(fsm.getStates()))
        self.assertIn(q1, fsm.getStates())
        self.assertIn(q2, fsm.getStates())

        transitionMade = fsm.makeTransition(bool_B_C, False)
        self.assertTrue(transitionMade)
        self.assertEqual(1, len(fsm.getStates()))
        self.assertIn(q4, fsm.getStates())


    def testMultipleStatesWithMultipleTransitionsMultipleLegalTransitions(self):
          
        fsm = FSM()
        
        q0 = fsm.getStates()[0]
        q1 = State()
        q2 = State()
        q3 = State()
        q4 = State()
        q5 = State()
        q6 = State()
        q7 = State()

        bool_A_B = Transition(bool, "A", "B")
        p_bool_A_B_True = PredicateTransition(bool, "A", "B", "==", True)
        int_B_C = Transition(int, "B", "C")
        p_int_B_C_42 = PredicateTransition(int, "B", "C", "==", 42)
        p_bool_B_C_False = PredicateTransition(bool, "B", "C", "==", False)
        p_bool_B_C_True = PredicateTransition(bool, "B", "C", "==", True)

        q0.addTransitionToState(bool_A_B, q1)
        q0.addTransitionToState(p_bool_A_B_True, q2)
        q1.addTransitionToState(int_B_C, q3)
        q1.addTransitionToState(p_bool_B_C_False, q4)
        q2.addTransitionToState(p_int_B_C_42, q5)
        q2.addTransitionToState(int_B_C, q6)
        q2.addTransitionToState(p_bool_B_C_True, q7)

        transitionMade = fsm.makeTransition(bool_A_B, True)
        self.assertTrue(transitionMade)
        self.assertEqual(2, len(fsm.getStates()))
        self.assertIn(q1, fsm.getStates())
        self.assertIn(q2, fsm.getStates())

        transitionMade = fsm.makeTransition(int_B_C, 42)
        self.assertTrue(transitionMade)
        self.assertEqual(3, len(fsm.getStates()))
        self.assertIn(q3, fsm.getStates())
        self.assertIn(q5, fsm.getStates())
        self.assertIn(q6, fsm.getStates())


    def testNoTransitionsAfterIllegalTransition(self):

        fsm = FSM()

        q0 = fsm.getStates()[0]
        q1 = State()

        bool_A_B = Transition(bool, "A", "B")
        p_bool_A_B = PredicateTransition(bool, "A", "B", "==", True)
        
        q0.addTransitionToState(p_bool_A_B, q1)

        transitionMade = fsm.makeTransition(bool_A_B, False)
        self.assertFalse(transitionMade)
        self.assertEqual(0, len(fsm.getStates()))

        transitionMade = fsm.makeTransition(bool_A_B, True)
        self.assertFalse(transitionMade)
        self.assertEqual(0, len(fsm.getStates()))


    def testIsInFinalStateOneStateFinalState(self):
        
        fsm = FSM()

        q0 = fsm.getStates()[0]     # not final state
        q1 = State()                # final state
        
        bool_A_B = Transition(bool, "A", "B")
        p_bool_A_B = PredicateTransition(bool, "A", "B", "==", True)

        q0.addTransitionToState(p_bool_A_B, q1)

        # fsm is not in a final state
        self.assertFalse(fsm.isInFinalState())

        transitionMade = fsm.makeTransition(bool_A_B, True)
        self.assertTrue(transitionMade)
        self.assertEqual(1, len(fsm.getStates()))
        self.assertIn(q1, fsm.getStates())

        # fsm is in a final state
        self.assertTrue(fsm.isInFinalState())


    def testIsInFinalStateMultipleStatesAllFinalStates(self):
        
        fsm = FSM()

        q0 = fsm.getStates()[0]     # not final state
        q1 = State()                # final state
        q2 = State()                # final state
        
        bool_A_B = Transition(bool, "A", "B")

        q0.addTransitionToState(bool_A_B, q1)
        q0.addTransitionToState(bool_A_B, q2)

        # fsm is not in a final state
        self.assertFalse(fsm.isInFinalState())

        transitionMade = fsm.makeTransition(bool_A_B, False)
        self.assertTrue(transitionMade)
        self.assertEqual(2, len(fsm.getStates()))
        self.assertIn(q1, fsm.getStates())
        self.assertIn(q2, fsm.getStates())

        # fsm is in a final state
        self.assertTrue(fsm.isInFinalState())


    def testIsInFinalStateMultipleStatesSomeFinalStates(self):

        fsm = FSM()

        q0 = fsm.getStates()[0]     # not final state
        q1 = State()                # final state
        
        str_B_C = Transition(str, "B", "C")
        p_str_B_C = PredicateTransition(str, "B", "C", "==", "hello world!")

        q0.addTransitionToState(p_str_B_C, q0)
        q0.addTransitionToState(p_str_B_C, q1)

        # fsm is not in a final state
        self.assertFalse(fsm.isInFinalState())

        transitionMade = fsm.makeTransition(str_B_C, "hello world!")
        self.assertTrue(transitionMade)
        self.assertEqual(2, len(fsm.getStates()))
        self.assertIn(q1, fsm.getStates())
        self.assertIn(q0, fsm.getStates())

        # fsm is in a final state
        self.assertTrue(fsm.isInFinalState())


if __name__ == '__main__':
    unittest.main()
