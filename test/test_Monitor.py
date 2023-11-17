import unittest
from src.core.monitor import Monitor
from src.core.transition import Transition
from src.core.exceptions.illegaltransitionexception import IllegalTransitionException

class TestMonitor(unittest.TestCase):

    def testVerifyCorrectSend(self):

        specification = r".\test\Test specifications\test_monitor_grammar.txt"
        monitor = Monitor(specification)

        transition = Transition("str", "buyer1", "seller")
        message = "hello world"
        monitor.verifySend(transition, message)
        # ensure transition is added to transition hostory
        self.assertIn((transition, message), monitor.transitionHistory)
        # ensure transition is added to unchecked receives for seller
        self.assertIn(transition, monitor.uncheckedReceives['seller'])
        # ensure transition is not accidentally loaded to sender side of uncheckedreceives
        self.assertNotIn(transition, monitor.uncheckedReceives['buyer1'], "Transition was loaded to sender")


    def testVerifyIncorrectSend(self):

        specification = r".\test\Test specifications\test_monitor_grammar.txt"
        monitor = Monitor(specification)

        faketransition = Transition("Integer", "Teun", "Jacob")
        message = 42
        with self.assertRaises(IllegalTransitionException):
            monitor.verifySend(faketransition, message)
    

    def testVerifyCorrectReceive(self):

        specification = r".\test\Test specifications\test_monitor_grammar.txt"
        monitor = Monitor(specification)

        # send the first message
        transition = Transition("str", "buyer1", "seller")
        message = "hello world"
        monitor.verifySend(transition, message)
        # verify transition is in uncheckedReceives for seller
        self.assertIn(transition, monitor.uncheckedReceives['seller'])
        # receive message and verify tranistion is removed
        monitor.verifyReceive(transition)
        self.assertNotIn(transition, monitor.uncheckedReceives['seller'])


    def testVerifyIncorrectReceive(self):

        specification = r".\test\Test specifications\test_monitor_grammar.txt"
        monitor = Monitor(specification)

        # send the first message
        transition = Transition("str", "buyer1", "seller")
        message = "hello world"
        monitor.verifySend(transition, message)
        # verify transition is in uncheckedReceives for seller
        self.assertIn(transition, monitor.uncheckedReceives['seller'])
        faketransition = Transition("str", "seller", "buyer1")
        with self.assertRaises(IllegalTransitionException):
            monitor.verifyReceive(faketransition)

    
    def testSendImpossibleWithUnreceivedMessage(self):    

        specification = r".\test\Test specifications\test_monitor_grammar.txt"
        monitor = Monitor(specification)

        transition1 = Transition("bool", "buyer1", "seller")
        transition2 = Transition("bool", "seller", "buyer1")
        message = True
        monitor.verifySend(transition1, message)
        # seller needs to receive the message from buyer1 before sending, check Exception is raised otherwise
        with self.assertRaises(IllegalTransitionException):
            monitor.verifyReceive(transition2)


    def testInitialiseUncheckedReceives(self):

        specification = r".\test\Test specifications\test_monitor_grammar.txt"
        monitor = Monitor(specification)

        # check initialise in setup worked correctly
        self.assertEqual(3, len(monitor.uncheckedReceives.keys()), "size of uncheckedReceives is incorrect after initial set-up")
        # adding roles is possible for new names
        monitor.initialiseUncheckedReceives(['Teun'])
        self.assertEqual(4, len(monitor.uncheckedReceives.keys()), "size of uncheckedReceives is incorrect after addition of role")

    def testUncheckedReceivesNonDeterminism(self):

        specification = r".\test\Test specifications\single_loop_grammar.txt"
        monitor = Monitor(specification)

        t1_A_B = Transition("str", "A", "B")
        t2_B_A = Transition("bool", "B", "A")

        self.assertEqual(2, len(monitor.uncheckedReceives))                
        self.assertIn("A", monitor.uncheckedReceives)  
        self.assertIn("B", monitor.uncheckedReceives)  
        self.assertEqual(0, len(monitor.uncheckedReceives["A"]))
        self.assertEqual(0, len(monitor.uncheckedReceives["B"]))

        monitor.verifySend(t1_A_B, "hello world")
        self.assertEqual(0, len(monitor.uncheckedReceives["A"]))
        self.assertEqual(1, len(monitor.uncheckedReceives["B"]))

        monitor.verifyReceive(t1_A_B)
        self.assertEqual(0, len(monitor.uncheckedReceives["A"]))
        self.assertEqual(0, len(monitor.uncheckedReceives["B"]))

        # Note that sending True from B to A satisfies two edges in the FSM.
        # However, only one unchecked receive should be added to the monitor.
        monitor.verifySend(t2_B_A, True)
        self.assertEqual(1, len(monitor.uncheckedReceives["A"]))
        self.assertEqual(0, len(monitor.uncheckedReceives["B"]))

        monitor.verifyReceive(t2_B_A)
        self.assertEqual(0, len(monitor.uncheckedReceives["A"]))
        self.assertEqual(0, len(monitor.uncheckedReceives["B"]))

        monitor.verifySend(t1_A_B, "hello world")
        self.assertEqual(0, len(monitor.uncheckedReceives["A"]))
        self.assertEqual(1, len(monitor.uncheckedReceives["B"]))

        monitor.verifyReceive(t1_A_B)
        self.assertEqual(0, len(monitor.uncheckedReceives["A"]))
        self.assertEqual(0, len(monitor.uncheckedReceives["B"]))

        # Note that sending False from B to A satisfies one edge in the FSM.
        # Therefore, only one unchecked receive should be added to the monitor.
        monitor.verifySend(t2_B_A, False)
        self.assertEqual(1, len(monitor.uncheckedReceives["A"]))
        self.assertEqual(0, len(monitor.uncheckedReceives["B"]))

        monitor.verifyReceive(t2_B_A)
        self.assertEqual(0, len(monitor.uncheckedReceives["A"]))
        self.assertEqual(0, len(monitor.uncheckedReceives["B"]))

        # At this point the protocol has terminated: no further communication is allowed.
        with self.assertRaises(IllegalTransitionException):
            monitor.verifySend(t1_A_B, "hello world")
