from state import State
from transition import Transition

import unittest


class TestState(unittest.TestCase):
    def testGetNextState(self):
        state1 = State()
        state2 = State()
        transition = Transition("Boolean", "Jacob", "Teun")
        faketransition = Transition("Integer", "Teun", "Jacob")
        print(transition)
        state1.addTransitionToState(transition, state2)
        self.assertIsNone(state1.getNextState(faketransition))
        self.assertEqual(state1.getNextState(transition), state2)


if __name__ == '__main__':
    unittest.main()