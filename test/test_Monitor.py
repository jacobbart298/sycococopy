import unittest
from src.core.monitor import Monitor
from src.core.transition import Transition
from src.core.exceptions.illegaltransitionexception import IllegalTransitionException

class TestMonitor(unittest.TestCase):

    
    def setUp(self):
        test_specification = r".\test\Test specifications\test_monitor_grammar.txt"
        self.test_monitor = Monitor(test_specification)


    def testVerifyCorrectSend(self):
        transition = Transition("str", "buyer1", "seller")
        self.test_monitor.verifySend(transition)
        # ensure transition is added to transition hostory
        self.assertIn(transition, self.test_monitor.transitionHistory, "Failed to add transition to transition history")
        # ensure transition is added to unchecked receives for seller
        self.assertIn(transition, self.test_monitor.uncheckedReceives['seller'], "Failed to add transition to unchecked receives")
        # ensure transition is not accidentally loaded to sender side of uncheckedreceives
        self.assertNotIn(transition, self.test_monitor.uncheckedReceives['buyer1'], "Transition was loaded to sender")


    def testVerifyIncorrectSend(self):
        faketransition = Transition("Integer", "Teun", "Jacob")
        with self.assertRaises(IllegalTransitionException) as error:
            self.test_monitor.verifySend(faketransition)
        message = str(error.exception)
        self.assertIn("TRANSITION FAILURE:", message, "Exception did not contain TRANSITION FAILURE header")
        self.assertIn(str(faketransition), message, "Offending transition not printed in exception message")
    

    def testVerifyCorrectReceive(self):
        # send the first message
        transition = Transition("str", "buyer1", "seller")
        self.test_monitor.verifySend(transition)
        # verify transition is in uncheckedReceives for seller
        self.assertIn(transition, self.test_monitor.uncheckedReceives['seller'], "Failed to add transition to unchecked receives")
        # receive message and verify tranistion is removed
        self.test_monitor.verifyReceive(transition)
        self.assertNotIn(transition, self.test_monitor.uncheckedReceives['seller'], "Transition was not removed after recieve")


    def testVerifyIncorrectReceive(self):
        # send the first message
        transition = Transition("str", "buyer1", "seller")
        self.test_monitor.verifySend(transition)
        # verify transition is in uncheckedReceives for seller
        self.assertIn(transition, self.test_monitor.uncheckedReceives['seller'], "Failed to add transition to unchecked receives")
        faketransition = Transition("str", "seller", "buyer1")
        with self.assertRaises(IllegalTransitionException) as error:
            self.test_monitor.verifyReceive(faketransition)

    
    def testSendImpossibleWithUnreceivedMessage(self):    
        transition1 = Transition("str", "buyer1", "seller")
        transition2 = Transition("str", "seller", "buyer1")
        self.test_monitor.verifySend(transition1)
        # seller needs to receive the message from buyer1 before sending, check Exception is raised otherwise
        with self.assertRaises(IllegalTransitionException) as error:
            self.test_monitor.verifyReceive(transition2)


    def testInitialiseUncheckedReceives(self):
        # check initialise in setup worked correctly
        self.assertEqual(3, len(self.test_monitor.uncheckedReceives.keys()), "size of uncheckedReceives is incorrect after initial set-up")
        # adding roles is possible for new names
        self.test_monitor.initialiseUncheckedReceives(['Teun'])
        self.assertEqual(4, len(self.test_monitor.uncheckedReceives.keys()), "size of uncheckedReceives is incorrect after addition of role")