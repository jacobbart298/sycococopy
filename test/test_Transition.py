import unittest
from src.core.transition import Transition, PredicateTransition
from src.core.exceptions.comparatornotimplementedexception import ComparatorNotImplementedException
from customs.customs import *


# Method "satisfies" is always called with a Transition object as the first parameter.
# This test set is limited to this scenario.
class TestTransition(unittest.TestCase):


    def testEqualsRegularAndRegularTransition(self):

        transition1 = Transition(bool, "A", "B")
        transition2 = Transition(bool, "A", "B")
        self.assertEqual(transition1, transition2)


    def testEqualsRegularAndRegularTransitionUnequalType(self):

        transition1 = Transition(bool, "A", "B")
        transition2 = Transition(int, "A", "B")
        self.assertNotEqual(transition1, transition2)


    def testEqualsRegularAndRegularTransitionUnequalSender(self):

        transition1 = Transition(bool, "A", "B")
        transition2 = Transition(bool, "C", "B")
        self.assertNotEqual(transition1, transition2)


    def testEqualsRegularAndRegularTransitionUnequalReceiver(self):

        transition1 = Transition(bool, "A", "B")
        transition2 = Transition(bool, "A", "C")
        self.assertNotEqual(transition1, transition2)


    def testEqualsRegularAndPredicateTransition(self):

        transition1 = Transition(int, "A", "B")
        transition2 = PredicateTransition(int, "A", "B", ">=", 0)
        self.assertNotEqual(transition1, transition2)        
        self.assertNotEqual(transition2, transition1)


    def testEqualsPredicateAndPredicateTransition(self):

        transition1 = PredicateTransition(int, "A", "B", ">", 5)
        transition2 = PredicateTransition(int, "A", "B", ">", 5)
        self.assertEqual(transition1, transition2)


    def testEqualsPredicateAndPredicateTransitionUnequalType(self):
        
        transition1 = PredicateTransition(float, "A", "B", ">=", 0)
        transition2 = PredicateTransition(Dog, "A", "B", ">=", Dog('Lily', 4, 34.5))
        self.assertNotEqual(transition1, transition2)


    def testEqualsPredicateAndPredicateTransitionUnequalSender(self):

        transition1 = PredicateTransition(bool, "A", "B", "==", True)
        transition2 = PredicateTransition(bool, "C", "B", "==", True)
        self.assertNotEqual(transition1, transition2)


    def testEqualsPredicateAndPredicateTransitionUnequalReceiver(self):

        transition1 = PredicateTransition(int, "A", "B", "<", 0)
        transition2 = PredicateTransition(int, "A", "C", "<", 0)
        self.assertNotEqual(transition1, transition2)


    def testEqualsPredicateAndPredicateTransitionUnequalComparator(self):

        transition1 = PredicateTransition(str, "A", "B", "!=", "hello world")
        transition2 = PredicateTransition(str, "A", "B", "==", "hello world")
        self.assertNotEqual(transition1, transition2)


    def testEqualsPredicateAndPredicateTransitionUnequalValue(self):
        
        transition1 = PredicateTransition(float, "A", "B", "<=", 3.6)
        transition2 = PredicateTransition(float, "A", "B", "<=", 3.4)
        self.assertNotEqual(transition1, transition2)


    def testSatisfiesRegularAndRegularTransition(self):
        
        transition1 = Transition(int, "A", "B")
        transition2 = Transition(int, "A", "B")
        item = 3        
        self.assertTrue(transition1.satisfies(transition2, item))


    def testSatisfiesRegularAndRegularTransitionUnequalType(self):
        
        transition1 = Transition(int, "A", "B")
        transition2 = Transition(float, "A", "B")
        item = 3.0
        self.assertFalse(transition1.satisfies(transition2, item))


    def testSatisfiesRegularAndRegularTransitionUnequalSender(self):
        
        transition1 = Transition(bool, "C", "B")
        transition2 = Transition(bool, "A", "B")
        item = True
        self.assertFalse(transition1.satisfies(transition2, item))


    def testSatisfiesRegularAndRegularTransitionUnequalReceiver(self):
        
        transition1 = Transition(float, "A", "B")
        transition2 = Transition(float, "A", "C")
        item = 42.0
        self.assertFalse(transition1.satisfies(transition2, item))


    def testSatisfiesRegularAndPredicateTransitionBoolMatch(self):
        
        transition1 = Transition(bool, "A", "B")
        transition2 = PredicateTransition(bool, "A", "B", "!=", False)
        item = True        
        self.assertTrue(transition2.satisfies(transition1, item))


    def testSatisfiesRegularAndPredicateTransitionStrMatch(self):
        
        transition1 = Transition(str, "A", "B")
        transition2 = PredicateTransition(str, "A", "B", "==", "hello world")
        item = "hello world"        
        self.assertTrue(transition2.satisfies(transition1, item))


    def testSatisfiesRegularAndPredicateTransitionFloatMatch(self):
        
        transition1 = Transition(float, "A", "B")
        transition2 = PredicateTransition(float, "A", "B", "<", 420.69)
        item = 420.0        
        self.assertTrue(transition2.satisfies(transition1, item))


    def testSatisfiesRegularAndPredicateTransitionIntMatch(self):
        
        transition1 = Transition(int, "A", "B")
        transition2 = PredicateTransition(int, "A", "B", ">=", 1337)
        item = 1338        
        self.assertTrue(transition2.satisfies(transition1, item))


    def testSatisfiesRegularAndPredicateTransitionBoolMismatch(self):
        
        transition1 = Transition(bool, "A", "B")
        transition2 = PredicateTransition(bool, "A", "B", "!=", False)
        item = False        
        self.assertFalse(transition2.satisfies(transition1, item))


    def testSatisfiesRegularAndPredicateTransitionStrMismatch(self):
        
        transition1 = Transition(str, "A", "B")
        transition2 = PredicateTransition(str, "A", "B", "==", "hello world")
        item = "world hello"        
        self.assertFalse(transition2.satisfies(transition1, item))


    def testSatisfiesRegularAndPredicateTransitionFloatMismatch(self):
        
        transition1 = Transition(float, "A", "B")
        transition2 = PredicateTransition(float, "A", "B", "<=", 420.69)
        item = 421.0        
        self.assertFalse(transition2.satisfies(transition1, item))


    def testSatisfiesRegularAndPredicateTransitionIntMismatch(self):
        
        transition1 = Transition(float, "A", "B")
        transition2 = PredicateTransition(float, "A", "B", ">", 1337)
        item = 1336        
        self.assertFalse(transition2.satisfies(transition1, item))
    

    def testSatisfiesRegularAndPredicateTransitionUnequalType(self):

        transition1 = Transition(int, "A", "B")
        transition2 = PredicateTransition(str, "A", "B", "==", "hello world")
        item = 3        
        self.assertFalse(transition2.satisfies(transition1, item))


    def testSatisfiesRegularAndPredicateTransitionUnequalSender(self):
        
        transition1 = Transition(int, "A", "B")
        transition2 = PredicateTransition(int, "C", "B", "!=", 2)
        item = 1337        
        self.assertFalse(transition2.satisfies(transition1, item))


    def testSatisfiesRegularAndPredicateTransitionUnequalReceiver(self):
        
        transition1 = Transition(str, "A", "B")
        transition2 = PredicateTransition(str, "A", "C", "==", "hello world")
        item = "hello world"        
        self.assertFalse(transition2.satisfies(transition1, item))
    

    def testSatisfiesRegularAndRegularTransitionCustomType(self):
        transition1 = Transition(Dog, "A", "B")
        transition2 = Transition(Dog, "A", "B")
        item = Dog('Lily', 5, 28.5)        
        self.assertTrue(transition2.satisfies(transition1, item))


    def testSatisfiesRegularAndPredicateTransitionCustomTypeLt(self):
        transition1 = Transition(Dog, "A", "B")
        transition2 = PredicateTransition(Dog, "A", "B", "<", Dog('Lady', 2, 60.0))
        item = Dog('Lily', 5, 28.5)
        self.assertTrue(transition2.satisfies(transition1, item))


    def testSatisfiesRegularAndPredicateTransitionCustomTypeLe(self):
        transition1 = Transition(Dog, "A", "B")
        transition2 = PredicateTransition(Dog, "A", "B", "<=", Dog('Lady', 2, 60.0))
        item = Dog('Lily', 5, 28.5)
        self.assertTrue(transition2.satisfies(transition1, item))


    def testSatisfiesRegularAndPredicateTransitionCustomTypeGt(self):
        transition1 = Transition(Dog, "A", "B")
        transition2 = PredicateTransition(Dog, "A", "B", ">", Dog('Lily', 5, 28.5))
        item = Dog('Lady', 2, 60.0)
        self.assertTrue(transition2.satisfies(transition1, item))


    def testSatisfiesRegularAndPredicateTransitionCustomTypeGe(self):
        transition1 = Transition(Dog, "A", "B")
        transition2 = PredicateTransition(Dog, "A", "B", ">=", Dog('Lily', 5, 28.5))
        item = Dog('Lady', 2, 28.5)
        self.assertTrue(transition2.satisfies(transition1, item))


    def testSatisfiesRegularAndPredicateTransitionCustomTypeEq(self):
        transition1 = Transition(Dog, "A", "B")
        transition2 = PredicateTransition(Dog, "A", "B", "==", Dog('Lily', 5, 28.5))
        item = Dog('Lily', 5, 28.5)
        self.assertTrue(transition2.satisfies(transition1, item))


    def testSatisfiesRegularAndPredicateTransitionCustomTypeNe(self):
        transition1 = Transition(Dog, "A", "B")
        transition2 = PredicateTransition(Dog, "A", "B", "!=", Dog('Lily', 5, 28.5))
        item = Dog('Lily', 4, 28.5)
        self.assertTrue(transition2.satisfies(transition1, item))


    def testInheritanceWithTypeSuperClassItemSubClass(self):
        transition1 = Transition(Dog, "A", "B")
        transition2 = Transition(Pet, "A", "B")
        item = Dog('Lily', 5, 28.5)        
        self.assertTrue(transition2.satisfies(transition1, item))


    def testInheritanceWithTypeSubClassItemSuperClass(self):
        transition1 = Transition(Pet, "A", "B")
        transition2 = Transition(Dog, "A", "B")
        item = Pet('Lily', 5)        
        self.assertFalse(transition2.satisfies(transition1, item))


    def testInheritanceWithTypeClassEqualsItemClass(self):
        transition1 = Transition(Dog, "A", "B")
        transition2 = Transition(Dog, "A", "B")
        item = Dog('Hector', 2, 32.5)        
        self.assertTrue(transition2.satisfies(transition1, item))


    def testComparatorNotImplementedLt(self):
        transition1 = Transition(Plant, "A", "B")
        transition2 = PredicateTransition(Plant, "A", "B", "<", Plant('Sansevieria', 40))
        item = Plant('Areca', 32)
        with self.assertRaises(ComparatorNotImplementedException):
            transition2.satisfies(transition1, item)


    def testComparatorNotImplementedGt(self):
        transition1 = Transition(Plant, "A", "B")
        transition2 = PredicateTransition(Plant, "A", "B", ">", Plant('Sansevieria', 40))
        item = Plant('Areca', 32)
        with self.assertRaises(ComparatorNotImplementedException):
            transition2.satisfies(transition1, item)
    

    def testComparatorNotImplementedLe(self):
        transition1 = Transition(Plant, "A", "B")
        transition2 = PredicateTransition(Plant, "A", "B", "<=", Plant('Sansevieria', 40))
        item = Plant('Areca', 32)
        with self.assertRaises(ComparatorNotImplementedException):
            transition2.satisfies(transition1, item) 
    

    def testComparatorNotImplementedGe(self):
        transition1 = Transition(Plant, "A", "B")
        transition2 = PredicateTransition(Plant, "A", "B", ">=", Plant('Sansevieria', 40))
        item = Plant('Areca', 32)
        with self.assertRaises(ComparatorNotImplementedException):
            transition2.satisfies(transition1, item)


    def testComparatorNotImplementedEq(self):
        transition1 = Transition(Plant, "A", "B")
        transition2 = PredicateTransition(Plant, "A", "B", "==", Plant('Sansevieria', 40))
        item = Plant('Areca', 32)
        with self.assertRaises(ComparatorNotImplementedException):
            transition2.satisfies(transition1, item)


    def testComparatorNotImplementedNe(self):
        transition1 = Transition(Plant, "A", "B")
        transition2 = PredicateTransition(Plant, "A", "B", "!=", Plant('Sansevieria', 40))
        item = Plant('Areca', 32)
        with self.assertRaises(ComparatorNotImplementedException):
            transition2.satisfies(transition1, item)
