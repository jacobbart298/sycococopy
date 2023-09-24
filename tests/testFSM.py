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
        self.fsm.initialiseUncheckedReceives(["Teun", "Tobias", "Jacob"])
        

    def testMakeCorrectTransition(self):
        # test correct transition
        global state0, state1, state2, transition1
        self.assertEqual(state0, self.fsm.getState(), "initial state of FSM is incorrect")
        self.fsm.makeTransition(transition1)
        self.assertEqual(state1, self.fsm.getState(), "state after transition is incorrect")
        # test if a newly made transition is also accepted (instead of using the global object)
        newTransition2 = Transition("Int", "Teun", "Tobias")
        self.fsm.makeTransition(newTransition2)
        self.assertEqual(state2, self.fsm.getState(), "state after manually made transition is incorrect")


    def testMakeIncorrectTransition(self):
        faketransition = Transition("Integer", "Teun", "Jacob")
        #check initial correct transition
        self.fsm.makeTransition(transition1)
        self.assertEqual(state1, self.fsm.getState(), "state after transition is incorrect")
        #check incorrect transition (returns both transitions in a list)
        transitions = self.fsm.makeTransition(faketransition)
        self.assertEqual(transition1, transitions[0], "first transition on error message is incorrect")
        self.assertEqual(faketransition, transitions[1], "incorrect transition is incorrectly displayed in error message")
    

    def testRemoveFromUncheckedReceives(self):
        self.fsm.makeTransition(transition1)
        self.fsm.makeTransition(transition2)
        #three keys present
        self.assertEqual(3, len(self.fsm.uncheckedReceives.keys()), "incorrect amount of keys in uncheckedReceives") 
        #transition1 linked to Teun
        self.assertIn(transition1, self.fsm.uncheckedReceives.get('Teun'), "transition1 is not shown in unCheckedReceives for Teun") 
        #transition2 linked to Tobias
        self.assertIn(transition2, self.fsm.uncheckedReceives.get('Tobias'), "transition2 is not shown in uncheckedReceives for Tobias") 
        self.fsm.removeFromUncheckedReceives(transition1)
        #three keys still present
        self.assertEqual(3, len(self.fsm.uncheckedReceives.keys()), "incorrect amount of keys in uncheckedReceives after removal of transition") 
        #transition1 no longer present for Teun
        self.assertNotIn(transition1, self.fsm.uncheckedReceives.get('Teun'), "transition was not removed by removeFromUncheckedReceives function") 
        #transition2 still linked to Tobias
        self.assertIn(transition2, self.fsm.uncheckedReceives.get('Tobias'), "transition2 was removed while not requested") 


    def testCheckTransition(self):
        # possible transition with empty uncheckedReceives returns True
        self.assertTrue(self.fsm.checkTransition(transition1), "checkTransition returns False for possible transition")
        # impossible transition with empty uncheckReceives returns False
        self.assertFalse(self.fsm.checkTransition(transition2), "checkTransition returns True for impossible transition")
        # possible transition with non-empty uncheckReceives for other sender returns True
        self.fsm.uncheckedReceives['Teun'] = [transition1]
        self.assertTrue(self.fsm.checkTransition(transition1), "checkTransition returns False if other party has non-empty uncheckedReceive")
        # possible transition with non-empty uncheckReceives returns False
        self.fsm.uncheckedReceives['Jacob'] = [transition2]
        self.assertFalse(self.fsm.checkTransition(transition1), "checkTransition returns True but uncheckReceive wasn't empty")
        

    def testCheckReceive(self):
        # after transition, receive is added to unCheckedReceives
        self.fsm.makeTransition(transition1)
        self.assertTrue(self.fsm.checkReceive(transition1), "transition not added to uncheckedReceives when transition is made")
        # if transition wasn't made yet, checkReceive returns false
        self.assertFalse(self.fsm.checkReceive(transition2), "checkReceive failed to return false on impossible receive")


    def testInitialiseUncheckedReceives(self):
        # check initialise in setup worked correctly
        self.assertEqual(3, len(self.fsm.uncheckedReceives.keys()), "size of uncheckedReceives is incorrect after initial set-up")
        # adding roles is possible for new names
        self.fsm.initialiseUncheckedReceives(['Sung'])
        self.assertEqual(4, len(self.fsm.uncheckedReceives.keys()), "size of uncheckedReceives is incorrect after addition of role")


if __name__ == '__main__':
    unittest.main()