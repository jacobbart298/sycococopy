import unittest
import os
from src.core.monitor import Monitor
from src.core.transition import Transition
from src.core.exceptions.illegaltransitionexception import IllegalTransitionException
from src.core.exceptions.haltedexception import HaltedException
from src.core.exceptions.pendingmessagesexception import PendingMessagesException

class TestMonitor(unittest.TestCase):


    def testInitializationTransitionHistory(self):
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        # initally, transition history is empty
        self.assertEqual(0, len(monitor.transitionHistory))


    def testTransitionHistoryOnlyContainsSends(self):
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

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
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

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

        # B is allowed to send an int to A, not a bool.
        with self.assertRaises(IllegalTransitionException):
            monitor.verifySend(bool_B_A, message_bool)     
        # illegal send is added to the transition history 
        self.assertEqual(2, len(monitor.transitionHistory))
        self.assertIn((str_A_B, message_str), monitor.transitionHistory)
        self.assertIn((bool_B_A, message_bool), monitor.transitionHistory)


    def testTransitionHistoryDoesNotIncludeIllegalReceive(self):
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

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


    def testHaltedRemainsFalseAfterLegalSend(self):
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)
        
        str_A_B = Transition(str, "A", "B")
        message_str = "hello world"

        # A is allowed to send a str to B
        self.assertFalse(monitor.halted)
        monitor.verifySend(str_A_B, message_str)   
        self.assertFalse(monitor.halted)


    def testHaltedRemainsFalseAfterLegalReceive(self):
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)
        
        str_A_B = Transition(str, "A", "B")
        message_str = "hello world"

        monitor.verifySend(str_A_B, message_str)       
        # B is allowed to receive a str from A
        self.assertFalse(monitor.halted)
        monitor.verifyReceive(str_A_B)   
        self.assertFalse(monitor.halted)


    def testHaltedBecomesTrueAfterIllegalSend(self):
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)
        
        int_B_A = Transition(int, "B", "A")
        message_bool = 42

        # B is not allowed to send a int to A
        self.assertFalse(monitor.halted)
        with self.assertRaises(IllegalTransitionException):
            monitor.verifySend(int_B_A, message_bool)    
        self.assertTrue(monitor.halted)


    def testHaltedBecomesTrueAfterIllegalReceive(self):
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)
        
        str_A_B = Transition(str, "A", "B")

        # A is not allowed to receive any messages that have not been sent
        self.assertFalse(monitor.halted)
        with self.assertRaises(IllegalTransitionException):
            monitor.verifyReceive(str_A_B)   
        self.assertTrue(monitor.halted)


    def testNoReceiveLegalOnceHaltedAfterIllegalSend(self):
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)
        
        bool_A_B = Transition(bool, "A", "B")
        str_A_B = Transition(str, "A", "B")
        message_str = "hello world"
        message_bool = True

        monitor.verifySend(str_A_B, message_str)
        self.assertFalse(monitor.halted)
        # A is not allowed to send a bool to B at this point
        with self.assertRaises(IllegalTransitionException):
            monitor.verifySend(bool_A_B, message_bool)
        self.assertTrue(monitor.halted)

        # once halted, further receives are illegal      
        with self.assertRaises(HaltedException):
            monitor.verifyReceive(str_A_B)


    def testNoReceiveLegalOnceHaltedAfterIllegalReceive(self):
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)
        
        str_A_B = Transition(str, "A", "B")
        int_B_A = Transition(int, "B", "A")
        message_str = "hello world"

        monitor.verifySend(str_A_B, message_str)
        self.assertFalse(monitor.halted)
        # A should not receive a message as none were sent to A
        with self.assertRaises(IllegalTransitionException):
            monitor.verifyReceive(int_B_A)
        self.assertTrue(monitor.halted)

        # once halted, further receives are illegal      
        with self.assertRaises(HaltedException):
            monitor.verifyReceive(str_A_B)


    def testNoSendLegalOnceHaltedAfterIllegalSend(self):
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)
       
        bool_A_B = Transition(bool, "A", "B")
        str_A_B = Transition(str, "A", "B")
        int_B_A = Transition(int, "B", "A")
        message_str = "hello world"
        message_bool = True
        message_int = -1

        monitor.verifySend(str_A_B, message_str)
        monitor.verifyReceive(str_A_B)
        self.assertFalse(monitor.halted)
        # A is not allowed to send a bool to B at this point
        with self.assertRaises(IllegalTransitionException):
            monitor.verifySend(bool_A_B, message_bool)
        self.assertTrue(monitor.halted)

        # once halted, further sends are illegal      
        with self.assertRaises(HaltedException):
            monitor.verifySend(int_B_A, message_int)


    def testNoSendLegalOnceHaltedAfterIllegalReceive(self):
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)
        
        str_A_B = Transition(str, "A", "B")
        int_B_A = Transition(int, "B", "A")
        message_str = "hello world"
        message_int = -1

        monitor.verifySend(str_A_B, message_str)
        monitor.verifyReceive(str_A_B)
        self.assertFalse(monitor.halted)
        # A should not receive a message from B as it was not sent yet
        with self.assertRaises(IllegalTransitionException):
            monitor.verifyReceive(int_B_A)
        self.assertTrue(monitor.halted)

        # once halted, further sends are illegal      
        with self.assertRaises(HaltedException):
            monitor.verifySend(int_B_A, message_int)


    def testNoSendsAddedToTransitionHistoryOnceHalted(self):
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)
        
        str_A_B = Transition(str, "A", "B")
        bool_B_A = Transition(bool, "B", "A")
        int_B_A = Transition(int, "B", "A")
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
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        str_A_B = Transition(str, "A", "B")
        int_B_A = Transition(int, "B", "A")
        message_str = "hello world"
        message_int = 42

        monitor.verifySend(str_A_B, message_str)
        monitor.verifyReceive(str_A_B)
        monitor.verifySend(int_B_A, message_int)
        monitor.verifyReceive(int_B_A)


    def testFirstSendsThenReveicesInOrder(self):
        specificationPath = getSpecificationPath("test_monitor_two")
        monitor = Monitor(specificationPath)

        bool_A_C = Transition(bool, "A", "C")
        bool_B_C = Transition(bool, "B", "C")
        message_bool = False

        monitor.verifySend(bool_A_C, message_bool)
        monitor.verifySend(bool_B_C, message_bool)
        monitor.verifyReceive(bool_A_C)
        monitor.verifyReceive(bool_B_C)


    def testFirstSendsThenReveicesNotInOrder(self):
        specificationPath = getSpecificationPath("test_monitor_two")
        monitor = Monitor(specificationPath)

        bool_A_C = Transition(bool, "A", "C")
        bool_B_C = Transition(bool, "B", "C")
        message_bool = False

        monitor.verifySend(bool_A_C, message_bool)
        monitor.verifySend(bool_B_C, message_bool)
        monitor.verifyReceive(bool_B_C)
        monitor.verifyReceive(bool_A_C)


    def testIllegalSendUncheckedReceivesEmpty(self):
        specificationPath = getSpecificationPath("test_monitor_two")
        monitor = Monitor(specificationPath)   

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
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)   

        str_A_B = Transition(str, "A", "B")
        int_B_A = Transition(int, "B", "A")
        message_str = "hello world"
        message_int = 42

        monitor.verifySend(str_A_B, message_str)
        monitor.verifyReceive(str_A_B)

        # B is not waiting for any messages, and sending an
        # int from B to A is allowed at this point
        self.assertEqual(0, len(monitor.uncheckedReceives["B"]))
        monitor.verifySend(int_B_A, message_int)
        monitor.verifyReceive(int_B_A)
    

    def testSendUncheckedReceivesNotEmptyWithCausalityCheck(self):    
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath, checkCausality = True)

        str_A_B = Transition(str, "A", "B")
        int_B_A = Transition(int, "B", "A")
        message_str = "hello world"
        message_int = 42
        
        monitor.verifySend(str_A_B, message_str)

        # B is waiting for a str from A. B is not allowed 
        # to send, for the monitor checks causality.
        self.assertEqual(1, len(monitor.uncheckedReceives["B"]))
        with self.assertRaises(PendingMessagesException):
            monitor.verifySend(int_B_A, message_int)


    def testSendUncheckedReceivesNotEmptyWithoutCausalityCheck(self):    
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath, checkCausality = False)

        str_A_B = Transition(str, "A", "B")
        int_B_A = Transition(int, "B", "A")
        message_str = "hello world"
        message_int = 42
        
        monitor.verifySend(str_A_B, message_str)

        # B is waiting for a str from A. B is allowed to 
        # send, for the monitor does not check causality.
        self.assertEqual(1, len(monitor.uncheckedReceives["B"]))
        monitor.verifySend(int_B_A, message_int)  
        monitor.verifyReceive(int_B_A)
        monitor.verifyReceive(str_A_B)


    def testLegalReceiveUncheckedReceivesNotEmpty(self):
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        str_A_B = Transition(str, "A", "B")
        int_B_A = Transition(int, "B", "A")
        message_str = "hello world"
        message_int = 42

        monitor.verifySend(str_A_B, message_str)
        monitor.verifyReceive(str_A_B)
        monitor.verifySend(int_B_A, message_int)

        # A is waiting for an int from B
        self.assertEqual(1, len(monitor.uncheckedReceives["A"]))
        monitor.verifyReceive(int_B_A)


    def testIllegalReceiveUncheckedReceivesNotEmpty(self):
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        str_A_B = Transition(str, "A", "B")
        bool_A_B = Transition(bool, "A", "B")
        message_str = "hello world"

        monitor.verifySend(str_A_B, message_str)
        self.assertEqual(1, len(monitor.uncheckedReceives["B"]))
        # B is waiting for a str from A, not a bool
        with self.assertRaises(IllegalTransitionException):
            monitor.verifyReceive(bool_A_B)


    def testIllegalReceiveUncheckedReceivesEmpty(self):
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        str_A_B = Transition(str, "A", "B")
        message_str = "hello world"

        monitor.verifySend(str_A_B, message_str)
        monitor.verifyReceive(str_A_B)

        # B is not waiting for any messages
        self.assertEqual(0, len(monitor.uncheckedReceives["B"]))
        with self.assertRaises(IllegalTransitionException):
            monitor.verifyReceive(str_A_B)


    def testSendNonDeterminism(self):
        specificationPath = getSpecificationPath("test_monitor_three")
        monitor = Monitor(specificationPath)
        
        str_A_B = Transition(str, "A", "B")
        bool_B_A = Transition(bool, "B", "A")
        message_str = "hello world"

        monitor.verifySend(str_A_B, message_str)
        monitor.verifyReceive(str_A_B)

        # Note that sending True from B to A satisfies two edges in the FSM.
        # However, only one unchecked receive should be added to the monitor.        
        monitor.verifySend(bool_B_A, True)
        self.assertEqual(1, len(monitor.uncheckedReceives["A"]))

        monitor.verifyReceive(bool_B_A)
        monitor.verifySend(str_A_B, message_str)
        monitor.verifyReceive(str_A_B)
        
        # Note that sending False from B to A satisfies one edge in the FSM.
        # Thus, only one unchecked receive should be added to the monitor.
        self.assertEqual(0, len(monitor.uncheckedReceives["A"]))
        monitor.verifySend(bool_B_A, False)
        self.assertEqual(1, len(monitor.uncheckedReceives["A"]))

        monitor.verifyReceive(bool_B_A)


    def testIllegalSendUncheckedReceivesNotEmpty(self):
        specificationPath = getSpecificationPath("test_double_send")
        monitor = Monitor(specificationPath, checkCausality = True)

        int_A_B = Transition(int, "A", "B")
        bool_B_A = Transition(bool, "B", "A")
        
        monitor.verifySend(int_A_B, 42)
        monitor.verifySend(int_A_B, 42)            
        monitor.verifyReceive(int_A_B)
        with self.assertRaises(PendingMessagesException):
            monitor.verifySend(bool_B_A, True)
        

    def testPrematureTerminationEndOfProtocolNotReached(self):
        specificationPath = getSpecificationPath("test_monitor_four")
        monitor = Monitor(specificationPath)

        str_A_B = Transition(str, "A", "B")
        bool_B_A = Transition(bool, "B", "A")
        message_str = "hello world"
        message_bool = True

        monitor.verifySend(str_A_B, message_str)
        monitor.verifyReceive(str_A_B)
        monitor.verifySend(bool_B_A, message_bool)
        monitor.verifyReceive(bool_B_A)

        # The program terminates before the end of the protocol was reached.
        monitor.__del__()
        # Check console for an error message stating that the program failed
        # to reach the end of the protocol. It should NOT state that there
        # are any lost messages.


    def testPrematureTerminationLostMessage(self):
        specificationPath = getSpecificationPath("test_monitor_four")
        monitor = Monitor(specificationPath)

        str_A_B = Transition(str, "A", "B")
        bool_B_A = Transition(bool, "B", "A")
        message_str = "hello world"
        message_bool = False

        monitor.verifySend(str_A_B, message_str)
        monitor.verifyReceive(str_A_B)
        monitor.verifySend(bool_B_A, message_bool)

        # The program terminates before all messages were received.
        monitor.__del__()
        # Check console for an error message stating there is a lost message,
        # namely, bool from B to A. It should NOT declare a failure to reach
        # the end of the protocol.


    def testPrematureTerminationEndOfProtocolNotReachedAndLostMessage(self):
        specificationPath = getSpecificationPath("test_monitor_four")
        monitor = Monitor(specificationPath)

        str_A_B = Transition(str, "A", "B")
        bool_B_A = Transition(bool, "B", "A")
        message_str = "hello world"
        message_bool = True

        monitor.verifySend(str_A_B, message_str)
        monitor.verifyReceive(str_A_B)
        monitor.verifySend(bool_B_A, message_bool)

        # The program terminates before the end of the protocol was reached;
        # also, there are still messages pending reception.
        monitor.__del__()
        # Check console for an error message stating that the program failed
        # to reach the end of the protocol AND that there is a lost message,
        # namely bool from B to A.


    def testPrematureTerminationAfterHalted(self):
        specificationPath = getSpecificationPath("test_monitor_four")
        monitor = Monitor(specificationPath)

        bool_B_A = Transition(bool, "B", "A")
        message_bool = True

        with self.assertRaises(IllegalTransitionException):
            # this is an illegal send which will halt the monitor
            monitor.verifySend(bool_B_A, message_bool)

        # The program terminates prematurely due to the illegal send.
        monitor.__del__()
        # Check console that NO error message is shown.


def getSpecificationPath(specificationName: str):
    return os.path.abspath(f"test/testcases/specifications/{specificationName}.txt")
