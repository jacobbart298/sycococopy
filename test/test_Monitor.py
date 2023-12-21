import unittest
from src.core.monitor import Monitor
from src.core.transition import Transition
from src.core.exceptions.illegaltransitionexception import IllegalTransitionException
from src.core.exceptions.rolemismatchexception import RoleMismatchException
from src.core.exceptions.haltedexception import HaltedException
from src.core.exceptions.pendingmessagesexception import PendingMessagesException

class TestMonitor(unittest.TestCase):


    def testCorrectRoles(self):        
        specification = r".\test\Test specifications\test_monitor.txt"
        try:
            Monitor(specification)
        except RoleMismatchException:
            self.fail
  

    def testRoleNotUsed(self):        
        specification = r".\test\Test specifications\test_role_not_used.txt"
        with self.assertRaises(RoleMismatchException):
            Monitor(specification)
        

    def testRoleNotDefined(self):
        specification = r".\test\Test specifications\test_role_not_defined.txt"
        with self.assertRaises(RoleMismatchException):
            Monitor(specification)


    def testRoleNotDefinedNotUsed(self):
        specification = r".\test\Test specifications\test_role_not_defined_not_used.txt"
        with self.assertRaises(RoleMismatchException):
            Monitor(specification)


    def testInitializationTransitionHistory(self):
        specification = r".\test\Test specifications\test_monitor.txt"
        monitor = Monitor(specification)
        # initally, transition history is empty
        self.assertEqual(0, len(monitor.transitionHistory))


    def testTransitionHistoryOnlyContainsSends(self):
        specification = r".\test\Test specifications\test_monitor.txt"
        monitor = Monitor(specification)

        str_A_B = Transition(str, "A", "B")
        int_B_A = Transition(int, "B", "A")
        message_str = "hello world"
        message_int = 42

        # initally, transition history is empty
        self.assertEqual(0, len(monitor.transitionHistory))

        monitor.verifySend(str_A_B, message_str)
        # send is added to the transition history
        self.assertEqual(1, len(monitor.transitionHistory))
        self.assertIn((str_A_B, message_str), monitor.transitionHistory)
       
        monitor.verifyReceive(str_A_B)
        # receive is not added to the transition history
        self.assertEqual(1, len(monitor.transitionHistory))
        self.assertIn((str_A_B, message_str), monitor.transitionHistory)
        
        monitor.verifySend(int_B_A, message_int)
        # send is added to the transition history
        self.assertEqual(2, len(monitor.transitionHistory))
        self.assertIn((str_A_B, message_str), monitor.transitionHistory)
        self.assertIn((int_B_A, message_int), monitor.transitionHistory)

        monitor.verifyReceive(int_B_A)
        # receive is not added to the transition history
        self.assertEqual(2, len(monitor.transitionHistory))
        self.assertIn((str_A_B, message_str), monitor.transitionHistory)
        self.assertIn((int_B_A, message_int), monitor.transitionHistory)
    

    def testTransitionHistoryIncludesIllegalSend(self):
        specification = r".\test\Test specifications\test_monitor.txt"
        monitor = Monitor(specification)

        str_A_B = Transition(str, "A", "B")
        bool_B_A = Transition(bool, "B", "A")
        message_str = "hello world"
        message_bool = True

        # initally, transition history is empty
        self.assertEqual(0, len(monitor.transitionHistory))

        monitor.verifySend(str_A_B, message_str)
        # send is added to the transition history
        self.assertEqual(1, len(monitor.transitionHistory))
        self.assertIn((str_A_B, message_str), monitor.transitionHistory)

        monitor.verifyReceive(str_A_B)

        with self.assertRaises(IllegalTransitionException):
            monitor.verifySend(bool_B_A, message_bool)     
        # illegal send is added to the transition history 
        self.assertEqual(2, len(monitor.transitionHistory))
        self.assertIn((str_A_B, message_str), monitor.transitionHistory)
        self.assertIn((bool_B_A, message_bool), monitor.transitionHistory)


    def testTransitionHistoryDoesNotIncludeIllegalReceive(self):
        specification = r".\test\Test specifications\test_monitor.txt"
        monitor = Monitor(specification)

        str_A_B = Transition(str, "A", "B")
        bool_B_A = Transition(bool, "B", "A")
        message_str = "hello world"

        # initally, transition history is empty
        self.assertEqual(0, len(monitor.transitionHistory))

        monitor.verifySend(str_A_B, message_str)
        # send is added to the transition history
        self.assertEqual(1, len(monitor.transitionHistory))
        self.assertIn((str_A_B, message_str), monitor.transitionHistory)

        with self.assertRaises(IllegalTransitionException):
            monitor.verifyReceive(bool_B_A)
        # transition history does not contain the illegal receive
        self.assertEqual(1, len(monitor.transitionHistory))
        self.assertIn((str_A_B, message_str), monitor.transitionHistory)


    def testInitializationUncheckedReceives(self):
        specification = r".\test\Test specifications\test_monitor.txt"
        monitor = Monitor(specification)

        # Upon initialization uncheckedReceives has keys for A and B
        self.assertEqual(2, len(monitor.uncheckedReceives))    
        self.assertIn("A", monitor.uncheckedReceives)  
        self.assertIn("B", monitor.uncheckedReceives)  

        # Upon initialization A and B have no unchecked receives
        self.assertEqual(0, len(monitor.uncheckedReceives["A"]))
        self.assertEqual(0, len(monitor.uncheckedReceives["B"]))


    def testInitializationHalted(self):
        specification = r".\test\Test specifications\test_monitor.txt"
        monitor = Monitor(specification)

        # Upon initialization halted is false
        self.assertFalse(monitor.halted)


    def testHaltedRemainsFalseAfterLegalSend(self):
        specification = r".\test\Test specifications\test_monitor.txt"
        monitor = Monitor(specification)
        
        str_A_B = Transition(str, "A", "B")
        message_str = "hello world"

        # A is allowed to send a str to B
        self.assertFalse(monitor.halted)
        monitor.verifySend(str_A_B, message_str)   
        self.assertFalse(monitor.halted)


    def testHaltedRemainsFalseAfterLegalReceive(self):
        specification = r".\test\Test specifications\test_monitor.txt"
        monitor = Monitor(specification)
        
        str_A_B = Transition(str, "A", "B")
        message_str = "hello world"

        monitor.verifySend(str_A_B, message_str)       
        # B is allowed to receive a str from A
        self.assertFalse(monitor.halted)
        monitor.verifyReceive(str_A_B)   
        self.assertFalse(monitor.halted)


    def testHaltedBecomesTrueAfterIllegalSend(self):
        specification = r".\test\Test specifications\test_monitor.txt"
        monitor = Monitor(specification)
        
        int_B_A = Transition(int, "B", "A")
        message_bool = 42

        # B is not allowed to send a int to A
        self.assertFalse(monitor.halted)
        with self.assertRaises(IllegalTransitionException):
            monitor.verifySend(int_B_A, message_bool)    
        self.assertTrue(monitor.halted)


    def testHaltedBecomesTrueAfterIllegalReceive(self):
        specification = r".\test\Test specifications\test_monitor.txt"
        monitor = Monitor(specification)
        
        str_A_B = Transition(str, "A", "B")

        # A is not allowed to receive any messages that have not been sent
        self.assertFalse(monitor.halted)
        with self.assertRaises(IllegalTransitionException):
            monitor.verifyReceive(str_A_B)   
        self.assertTrue(monitor.halted)


    def testNoTransitionsLegalOnceHalted(self):
        specification = r".\test\Test specifications\test_monitor.txt"
        monitor = Monitor(specification)
        
        str_A_B = Transition(str, "A", "B")
        message_str = "hello world"

        # A is not allowed to receive any messages that have not been sent
        self.assertFalse(monitor.halted)
        with self.assertRaises(IllegalTransitionException):
            monitor.verifyReceive(str_A_B)   
        self.assertTrue(monitor.halted)

        # once halted, further transitions are illegal      
        with self.assertRaises(HaltedException):
            monitor.verifySend(str_A_B, message_str)


    def testNoSendsAddedToTransitionHistoryOnceHalted(self):
        specification = r".\test\Test specifications\test_monitor.txt"
        monitor = Monitor(specification)
        
        str_A_B = Transition(str, "A", "B")
        bool_B_A = Transition(bool, "A", "B")
        int_B_A = Transition(int, "A", "B")
        message_str = "hello world"
        message_bool = True
        message_int = 42

        monitor.verifySend(str_A_B, message_str)
        monitor.verifyReceive(str_A_B)    

        self.assertFalse(monitor.halted)
        with self.assertRaises(IllegalTransitionException):
            monitor.verifySend(bool_B_A, message_bool)   
        self.assertTrue(monitor.halted)

        # transition history once halted
        self.assertEqual(2, len(monitor.transitionHistory))
        self.assertIn((str_A_B, message_str), monitor.transitionHistory)
        self.assertIn((bool_B_A, message_bool), monitor.transitionHistory)
        
        with self.assertRaises(HaltedException):
            monitor.verifySend(int_B_A, message_int)   
        
        # transition history remains the same
        self.assertEqual(2, len(monitor.transitionHistory))
        self.assertIn((str_A_B, message_str), monitor.transitionHistory)
        self.assertIn((bool_B_A, message_bool), monitor.transitionHistory)
        

    def testAlternateSendAndReceive(self):
        specification = r".\test\Test specifications\test_monitor.txt"
        monitor = Monitor(specification)

        str_A_B = Transition(str, "A", "B")
        int_B_A = Transition(int, "B", "A")
        message_str = "hello world"
        message_int = 42

        try:
            monitor.verifySend(str_A_B, message_str)
            monitor.verifyReceive(str_A_B)
            monitor.verifySend(int_B_A, message_int)
            monitor.verifyReceive(int_B_A)
        except IllegalTransitionException:
            self.fail


    def testConsecutiveSendsAndReveices(self):
        specification = r".\test\Test specifications\test_monitor_two.txt"
        monitor = Monitor(specification)

        bool_A_C = Transition(bool, "A", "B")
        bool_B_C = Transition(bool, "B", "A")
        message_bool = False

        try:
            monitor.verifySend(bool_A_C, message_bool)
            monitor.verifySend(bool_B_C, message_bool)
            monitor.verifyReceive(bool_A_C)
            monitor.verifyReceive(bool_B_C)
        except IllegalTransitionException:
            self.fail


    def testIllegalSendUncheckedReceivesEmpty(self):
        specification = r".\test\Test specifications\test_monitor_two.txt"
        monitor = Monitor(specification)

        bool_A_C = Transition(bool, "A", "C")
        bool_C_D = Transition(bool, "C", "D")
        message_bool = False

        monitor.verifySend(bool_A_C, message_bool)
        monitor.verifyReceive(bool_A_C)

        # C is not waiting for any messages, but sending a
        # bool from C to D is not allowed at this point
        self.assertEqual(0, len(monitor.uncheckedReceives["C"]))
        with self.assertRaises(IllegalTransitionException):
            monitor.verifySend(bool_C_D, message_bool)


    def testLegalSendUncheckedReceivesEmpty(self):    
        specification = r".\test\Test specifications\test_monitor_two.txt"
        monitor = Monitor(specification)

        bool_A_C = Transition(bool, "A", "C")
        bool_B_C = Transition(bool, "B", "C")
        message_bool = False

        monitor.verifySend(bool_A_C, message_bool)
        monitor.verifyReceive(bool_A_C)

        # B is not waiting for any messages, and sending a
        # bool from B to C is allowed at this point
        self.assertEqual(0, len(monitor.uncheckedReceives["B"]))
        try:
            monitor.verifySend(bool_B_C, message_bool)
        except IllegalTransitionException:
            self.fail


    def testSendUncheckedReceivesNotEmpty(self):    
        specification = r".\test\Test specifications\test_monitor.txt"
        monitor = Monitor(specification)

        str_A_B = Transition(str, "A", "B")
        int_B_A = Transition(int, "B", "A")
        message_str = "hello world"
        message_int = 42
        
        monitor.verifySend(str_A_B, message_str)

        # Even though int_B_A is the next send in the fsm, it is 
        # not allowed because B is waiting for a str from A.
        self.assertEqual(1, len(monitor.uncheckedReceives["B"]))
        with self.assertRaises(PendingMessagesException):
            monitor.verifySend(int_B_A, message_int)


    def testLegalReceiveUncheckedReceivesNotEmpty(self):
        specification = r".\test\Test specifications\test_monitor.txt"
        monitor = Monitor(specification)

        str_A_B = Transition(str, "A", "B")
        int_B_A = Transition(int, "B", "A")
        message_str = "hello world"
        message_int = 42

        monitor.verifySend(str_A_B, message_str)
        monitor.verifyReceive(str_A_B)
        monitor.verifySend(int_B_A, message_int)

        # A is waiting for an int from B
        self.assertEqual(1, len(monitor.uncheckedReceives["A"]))
        try:
            monitor.verifyReceive(int_B_A)
        except IllegalTransitionException:
            self.fail


    def testIllegalReceiveUncheckedReceivesNotEmpty(self):
        specification = r".\test\Test specifications\test_monitor.txt"
        monitor = Monitor(specification)

        str_A_B = Transition(str, "A", "B")
        bool_A_B = Transition(bool, "A", "B")
        message_str = "hello world"

        monitor.verifySend(str_A_B, message_str)
        self.assertEqual(1, len(monitor.uncheckedReceives["B"]))
        # B is waiting for a str from A, not a bool
        with self.assertRaises(IllegalTransitionException):
            monitor.verifyReceive(bool_A_B)    


    def testIllegalReceiveUncheckedReceivesEmpty(self):
        specification = r".\test\Test specifications\test_monitor.txt"
        monitor = Monitor(specification)

        str_A_B = Transition(str, "A", "B")
        message_str = "hello world"

        monitor.verifySend(str_A_B, message_str)
        monitor.verifyReceive(str_A_B)

        # B is not waiting for any messages
        self.assertEqual(0, len(monitor.uncheckedReceives["B"]))
        with self.assertRaises(IllegalTransitionException):
            monitor.verifyReceive(str_A_B)


    def testSendNonDeterminism(self):
        specification = r".\test\Test specifications\test_monitor_non_determinism.txt"
        monitor = Monitor(specification)

        t1_A_B = Transition(str, "A", "B")
        t2_B_A = Transition(bool, "B", "A")
        message_str = "hello world"

        monitor.verifySend(t1_A_B, message_str)
        monitor.verifyReceive(t1_A_B)

        # Note that sending True from B to A satisfies two edges in the FSM.
        # However, only one unchecked receive should be added to the monitor.        
        self.assertEqual(0, len(monitor.uncheckedReceives["A"]))
        monitor.verifySend(t2_B_A, True)
        self.assertEqual(1, len(monitor.uncheckedReceives["A"]))

        monitor.verifyReceive(t2_B_A)
        monitor.verifySend(t1_A_B, message_str)
        monitor.verifyReceive(t1_A_B)
        
        # Note that sending False from B to A satisfies one edge in the FSM.
        # Thus, only one unchecked receive should be added to the monitor.
        self.assertEqual(0, len(monitor.uncheckedReceives["A"]))
        monitor.verifySend(t2_B_A, False)
        self.assertEqual(1, len(monitor.uncheckedReceives["A"]))

        monitor.verifyReceive(t2_B_A)


    def testDoubleTest(self):
        specification = r".\test\Test specifications\test_double_send.txt"
        monitor = Monitor(specification)

        int_A_B = Transition(int, "A", "B")
        bool_B_A = Transition(bool, "B", "A")
        
        monitor.verifySend(int_A_B, 42)
        monitor.verifySend(int_A_B, 42)            
        monitor.verifyReceive(int_A_B)
        with self.assertRaises(PendingMessagesException):
            monitor.verifySend(bool_B_A, True)    