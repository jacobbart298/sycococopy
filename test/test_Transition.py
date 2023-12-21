from src.core.transition import Transition, PredicateTransition
import unittest

# Method "satisfies" is always called with a Transition object as the first parameter.
# This test set is limited to this scenario.
class TestTransition(unittest.TestCase):


    def testEqualsRegularAndRegularTransition(self):

        transition_1 = Transition(bool, "A", "B")
        transition_2 = Transition(bool, "A", "B")
        self.assertEqual(transition_1, transition_2)


    def testEqualsRegularAndRegularTransitionUnequalType(self):

        transition_1 = Transition(bool, "A", "B")
        transition_2 = Transition(int, "A", "B")
        self.assertNotEqual(transition_1, transition_2)


    def testEqualsRegularAndRegularTransitionUnequalSender(self):

        transition_1 = Transition(bool, "A", "B")
        transition_2 = Transition(bool, "C", "B")
        self.assertNotEqual(transition_1, transition_2)


    def testEqualsRegularAndRegularTransitionUnequalReceiver(self):

        transition_1 = Transition(bool, "A", "B")
        transition_2 = Transition(bool, "A", "C")
        self.assertNotEqual(transition_1, transition_2)


    def testEqualsRegularAndPredicateTransition(self):

        transition_1 = Transition(int, "A", "B")
        transition_2 = PredicateTransition(int, "A", "B", ">=", 0)
        self.assertNotEqual(transition_1, transition_2)        
        self.assertNotEqual(transition_2, transition_1)


    def testEqualsPredicateAndPredicateTransition(self):

        transition_1 = PredicateTransition(int, "A", "B", ">", 5)
        transition_2 = PredicateTransition(int, "A", "B", ">", 5)
        self.assertEqual(transition_1, transition_2)


    def testEqualsPredicateAndPredicateTransitionUnequalType(self):
        
        transition_1 = PredicateTransition(float, "A", "B", ">=", 0)
        transition_2 = PredicateTransition(int, "A", "B", ">=", 0)
        self.assertNotEqual(transition_1, transition_2)


    def testEqualsPredicateAndPredicateTransitionUnequalSender(self):

        transition_1 = PredicateTransition(bool, "A", "B", "==", True)
        transition_2 = PredicateTransition(bool, "C", "B", "==", True)
        self.assertNotEqual(transition_1, transition_2)


    def testEqualsPredicateAndPredicateTransitionUnequalReceiver(self):

        transition_1 = PredicateTransition(int, "A", "B", "<", 0)
        transition_2 = PredicateTransition(int, "A", "C", "<", 0)
        self.assertNotEqual(transition_1, transition_2)


    def testEqualsPredicateAndPredicateTransitionUnequalComparator(self):

        transition_1 = PredicateTransition(str, "A", "B", "!=", "hello world")
        transition_2 = PredicateTransition(str, "A", "B", "==", "hello world")
        self.assertNotEqual(transition_1, transition_2)


    def testEqualsPredicateAndPredicateTransitionUnequalValue(self):
        
        transition_1 = PredicateTransition(float, "A", "B", "<=", 3.6)
        transition_2 = PredicateTransition(float, "A", "B", "<=", 3.4)
        self.assertNotEqual(transition_1, transition_2)


    def testSatisfiesRegularAndRegularTransition(self):
        
        transition_1 = Transition(int, "A", "B")
        transition_2 = Transition(int, "A", "B")
        value = 3        
        self.assertTrue(transition_1.satisfies(transition_2, value))


    def testSatisfiesRegularAndRegularTransitionUnequalType(self):
        
        transition_1 = Transition(int, "A", "B")
        transition_2 = Transition(float, "A", "B")
        value = 3.0
        self.assertFalse(transition_1.satisfies(transition_2, value))


    def testSatisfiesRegularAndRegularTransitionUnequalSender(self):
        
        transition_1 = Transition(bool, "C", "B")
        transition_2 = Transition(bool, "A", "B")
        value = True
        self.assertFalse(transition_1.satisfies(transition_2, value))


    def testSatisfiesRegularAndRegularTransitionUnequalReceiver(self):
        
        transition_1 = Transition(float, "A", "B")
        transition_2 = Transition(float, "A", "C")
        value = 42.0
        self.assertFalse(transition_1.satisfies(transition_2, value))


    def testSatisfiesRegularAndPredicateTransitionBoolMatch(self):
        
        transition_1 = Transition(bool, "A", "B")
        transition_2 = PredicateTransition(bool, "A", "B", "!=", False)
        value = True        
        self.assertTrue(transition_2.satisfies(transition_1, value))


    def testSatisfiesRegularAndPredicateTransitionStrMatch(self):
        
        transition_1 = Transition(str, "A", "B")
        transition_2 = PredicateTransition(str, "A", "B", "==", "hello world")
        value = "hello world"        
        self.assertTrue(transition_2.satisfies(transition_1, value))


    def testSatisfiesRegularAndPredicateTransitionFloatMatch(self):
        
        transition_1 = Transition(float, "A", "B")
        transition_2 = PredicateTransition(float, "A", "B", "<", 420.69)
        value = 420.0        
        self.assertTrue(transition_2.satisfies(transition_1, value))


    def testSatisfiesRegularAndPredicateTransitionIntMatch(self):
        
        transition_1 = Transition(int, "A", "B")
        transition_2 = PredicateTransition(int, "A", "B", ">=", 1337)
        value = 1338        
        self.assertTrue(transition_2.satisfies(transition_1, value))


    def testSatisfiesRegularAndPredicateTransitionBoolMismatch(self):
        
        transition_1 = Transition(bool, "A", "B")
        transition_2 = PredicateTransition(bool, "A", "B", "!=", False)
        value = False        
        self.assertFalse(transition_2.satisfies(transition_1, value))


    def testSatisfiesRegularAndPredicateTransitionStrMismatch(self):
        
        transition_1 = Transition(str, "A", "B")
        transition_2 = PredicateTransition(str, "A", "B", "==", "hello world")
        value = "world hello"        
        self.assertFalse(transition_2.satisfies(transition_1, value))


    def testSatisfiesRegularAndPredicateTransitionFloatMismatch(self):
        
        transition_1 = Transition(float, "A", "B")
        transition_2 = PredicateTransition(float, "A", "B", "<=", 420.69)
        value = 421.0        
        self.assertFalse(transition_2.satisfies(transition_1, value))


    def testSatisfiesRegularAndPredicateTransitionIntMismatch(self):
        
        transition_1 = Transition(float, "A", "B")
        transition_2 = PredicateTransition(float, "A", "B", ">", 1337)
        value = 1336        
        self.assertFalse(transition_2.satisfies(transition_1, value))
    

    def testSatisfiesRegularAndPredicateTransitionUnequalType(self):

        transition_1 = Transition(int, "A", "B")
        transition_2 = PredicateTransition(str, "A", "B", "==", "hello world")
        value = 3        
        self.assertFalse(transition_2.satisfies(transition_1, value))


    def testSatisfiesRegularAndPredicateTransitionUnequalSender(self):
        
        transition_1 = Transition(int, "A", "B")
        transition_2 = PredicateTransition(int, "C", "B", "!=", 2)
        value = 1337        
        self.assertFalse(transition_2.satisfies(transition_1, value))


    def testSatisfiesRegularAndPredicateTransitionUnequalReceiver(self):
        
        transition_1 = Transition(str, "A", "B")
        transition_2 = PredicateTransition(str, "A", "C", "==", "hello world")
        value = "hello world"        
        self.assertFalse(transition_2.satisfies(transition_1, value))
    
if __name__ == '__main__':
    unittest.main()
