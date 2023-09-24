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
        self.assertEqual(self.fsm.getState(), state0)
        self.fsm.makeTransition(transition1)
        self.assertEqual(self.fsm.getState(), state1)
        # test if a newly made transition is also accepted (instead of using the global object)
        newTransition2 = Transition("Int", "Teun", "Tobias")
        self.fsm.makeTransition(newTransition2)
        self.assertEqual(self.fsm.getState(), state2)


    def testMakeIncorrectTransition(self):
        faketransition = Transition("Integer", "Teun", "Jacob")
        #check initial correct transition
        self.fsm.makeTransition(transition1)
        self.assertEqual(self.fsm.getState(), state1)
        #check incorrect transition (returns both transitions in a list)
        transitions = self.fsm.makeTransition(faketransition)
        self.assertEqual(transitions[0], transition1)
        self.assertEqual(transitions[1], faketransition)
    

    def testRemoveFromUncheckedReceives(self):
        self.fsm.makeTransition(transition1)
        self.fsm.makeTransition(transition2)
        self.assertEqual(3, len(self.fsm.uncheckedReceives.keys())) #three keys present
        self.assertIn(transition1, self.fsm.uncheckedReceives.get('Teun')) #transition1 linked to Teun
        self.assertIn(transition2, self.fsm.uncheckedReceives.get('Tobias')) #transition2 linked to Tobias
        self.fsm.removeFromUncheckedReceives(transition1)
        self.assertEqual(3, len(self.fsm.uncheckedReceives.keys())) #three keys still present
        self.assertNotIn(transition1, self.fsm.uncheckedReceives.get('Teun')) #transition1 no longer present for Teun
        self.assertIn(transition2, self.fsm.uncheckedReceives.get('Tobias')) #transition2 still linked to Tobias


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
        pass


    def testInitialiseUncheckedReceives(self):
        pass


    def testGetState(self):
        pass




if __name__ == '__main__':
    unittest.main()