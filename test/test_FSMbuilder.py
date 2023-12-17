import unittest
import os
from antlr4 import CommonTokenStream, FileStream
from antlrFiles.PythonicLexer import PythonicLexer
from antlrFiles.PythonicParser import PythonicParser
from src.core.fsmBuilder import FSMbuilder
from src.core.transition import Transition, PredicateTransition

class TestFSMBuilder(unittest.TestCase):


    # see singleSend.png in tests/testcases/fsms for fsm
    def test_singlePredicateSend(self):
        
        send = PredicateTransition(int, "B", "A", ">", 4)

        fsm = self.buildFSM("singlePredicateSend.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there is one transition: send
        self.assertEqual(1, len(q0.getTransitions()))
        self.assertIn(send, q0.getTransitions())

        # transition send in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(send)))
        q1 = list(q0.getNextStates(send))[0]
        # in q1 there is no transition
        self.assertEqual(0, len(q1.getTransitions()))
    

    # see singleSend.png in tests/testcases/fsms for fsm
    def test_singleRegularSend(self):
        
        send = Transition(int, "B", "A")

        fsm = self.buildFSM("singleRegularSend.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there is one transition: send
        self.assertEqual(1, len(q0.getTransitions()))
        self.assertIn(send, q0.getTransitions())

        # transition send in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(send)))
        q1 = list(q0.getNextStates(send))[0]
        # in q1 there is no transition
        self.assertEqual(0, len(q1.getTransitions()))


    # see singleChoice.png in tests/testcases/fsms for fsm
    def test_singleChoice(self):

        choice_a = Transition(int, "A", "B")
        choice_b = PredicateTransition(bool, "B", "A", "==", True)

        fsm = self.buildFSM("singleChoice.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there are two transitions: choice_a and choice_b
        self.assertEqual(2, len(q0.getTransitions()))
        self.assertIn(choice_a, q0.getTransitions())
        self.assertIn(choice_b, q0.getTransitions())

        # transition choice_a in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(choice_a)))
        q1 = list(q0.getNextStates(choice_a))[0]

        # transition choice_b in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(choice_b)))
        self.assertIn(q1, q0.getNextStates(choice_b))

        # in q1 there is no transition
        self.assertEqual(0, len(q1.getTransitions()))


    # see singleSequence.png in tests/testcases/fsms for fsm
    def test_singleSequence(self):

        sequence_a = Transition(bool, "A", "B")
        sequence_b = PredicateTransition(int, "B", "A", "==", 42)

        fsm = self.buildFSM("singleSequence.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there is one transition: sequence_a
        self.assertEqual(1, len(q0.getTransitions()))
        self.assertIn(sequence_a, q0.getTransitions())

        # transition sequence_a in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(sequence_a)))
        q1 = list(q0.getNextStates(sequence_a))[0]

        # in q1 there is one transition: sequence_b
        self.assertEqual(1, len(q1.getTransitions()))
        self.assertIn(sequence_b, q1.getTransitions())

        # transition sequence_b in q1 leads to q2
        self.assertEqual(1, len(q1.getNextStates(sequence_b)))
        q2 = list(q1.getNextStates(sequence_b))[0]

        # in q2 there is no transition
        self.assertEqual(0, len(q2.getTransitions()))


    # see singleShuffle.png in tests/testcases/fsms for fsm 
    def test_singleShuffle(self):

        shuffle_a = PredicateTransition(float, "A", "B", "<=", -44.29)
        shuffle_b = Transition(int, "B", "A")

        fsm = self.buildFSM("singleShuffle.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there are two transitions: shuffle_a and shuffle_b
        self.assertEqual(2, len(q0.getTransitions()))
        self.assertIn(shuffle_a, q0.getTransitions())
        self.assertIn(shuffle_b, q0.getTransitions())

        # transition shuffle_a in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(shuffle_a)))
        q1 = list(q0.getNextStates(shuffle_a))[0]        
        # in q1 there is one transition: shuffle_b
        self.assertEqual(1, len(q1.getTransitions()))
        self.assertIn(shuffle_b, q1.getTransitions())
        # transition shuffle_b in q1 leads to q3
        self.assertEqual(1, len(q1.getNextStates(shuffle_b)))
        q3 = list(q1.getNextStates(shuffle_b))[0]

        # transition shuffle_b in q0 leads to q2
        self.assertEqual(1, len(q0.getNextStates(shuffle_b)))
        q2 = list(q0.getNextStates(shuffle_b))[0]        
        # in q2 there is one transition: shuffle_a
        self.assertEqual(1, len(q2.getTransitions()))
        self.assertIn(shuffle_a, q2.getTransitions())
        # transition shuffle_a in q2 leads to q3
        self.assertEqual(1, len(q2.getNextStates(shuffle_a)))
        self.assertIn(q3, q2.getNextStates(shuffle_a))

        # in q3 there is no transition
        self.assertEqual(0, len(q3.getTransitions()))


    # see choiceInShuffle.png in tests/testcases/fsms for fsm
    def test_choiceInShuffle(self):

        choice_a = Transition(int, "A", "B")
        choice_b = PredicateTransition(float, "B", "A", ">", 13333.7)

        send = Transition(str, "B", "A")        

        fsm = self.buildFSM("choiceInShuffle.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there are 3 transitions: choice_a, choice_b and send
        self.assertEqual(3, len(q0.getTransitions()))
        self.assertIn(choice_a, q0.getTransitions())
        self.assertIn(choice_b, q0.getTransitions())
        self.assertIn(send, q0.getTransitions())

        # transition send in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(send)))
        q1 = list(q0.getNextStates(send))[0]        
        # in q1 there are two transitions: choice_a and choice_b
        self.assertEqual(2, len(q1.getTransitions()))
        self.assertIn(choice_a, q1.getTransitions())
        self.assertIn(choice_b, q1.getTransitions())
        # transition choice_a in q1 leads to q3
        self.assertEqual(1, len(q1.getNextStates(choice_a)))
        q3 = list(q1.getNextStates(choice_a))[0]
        # transition choice_b in q1 leads to q3
        self.assertEqual(1, len(q1.getNextStates(choice_b)))
        self.assertIn(q3, q1.getNextStates(choice_b))

        # transition choice_a in q0 leads to q2
        self.assertEqual(1, len(q0.getNextStates(choice_a)))
        q2 = list(q0.getNextStates(choice_a))[0]       
        # transition choice_b in q0 leads to q2
        self.assertEqual(1, len(q0.getNextStates(choice_b)))
        self.assertIn(q2, q0.getNextStates(choice_b))     
        # in q2 there is one transition
        self.assertEqual(1, len(q2.getTransitions()))
        self.assertIn(send, q2.getTransitions())
        # transition send in q2 leads to q3
        self.assertEqual(1, len(q2.getNextStates(send)))
        self.assertIn(q3, q2.getNextStates(send))

        # in q3 there is no transition
        self.assertEqual(0, len(q3.getTransitions()))


    # see sequenceInShuffle.png in tests/testcases/fsms for fsm
    def test_sequenceInShuffle(self):

        send = Transition(str, "B", "A")
        sequence_a = PredicateTransition(int, "A", "B", "==", 5234904798238)
        sequence_b = PredicateTransition(bool, "B", "A", "==", True)

        fsm = self.buildFSM("sequenceInShuffle.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        
        # in q0 there are 2 transitions: sequence_a and send
        self.assertEqual(2, len(q0.getTransitions()))
        self.assertIn(sequence_a, q0.getTransitions())
        self.assertIn(send, q0.getTransitions())

        # transition sequence_a in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(sequence_a)))
        q1 = list(q0.getNextStates(sequence_a))[0]    
        # in q1 there is one transition: sequence_b
        self.assertEqual(1, len(q1.getTransitions()))
        self.assertIn(sequence_b, q1.getTransitions())
        # transition sequence_b in q1 leads to q3
        self.assertEqual(1, len(q1.getNextStates(sequence_b)))
        q3 = list(q1.getNextStates(sequence_b))[0]    
        # in q3 there is one transition: send
        self.assertEqual(1, len(q3.getTransitions()))
        self.assertIn(send, q3.getTransitions())
        # transition send in q3 leads to q5
        self.assertEqual(1, len(q3.getNextStates(send)))
        q5 = list(q3.getNextStates(send))[0]    

        # transition send in q0 leads to q2
        self.assertEqual(1, len(q0.getNextStates(send)))
        q2 = list(q0.getNextStates(send))[0]    
        # in q2 there is one transition: sequence_a
        self.assertEqual(1, len(q2.getTransitions()))
        self.assertIn(sequence_a, q2.getTransitions())
        # transition sequence_a in q2 leads to q4
        self.assertEqual(1, len(q2.getNextStates(sequence_a)))
        q4 = list(q2.getNextStates(sequence_a))[0]    
        # in q4 there is one transition: sequence_b
        self.assertEqual(1, len(q4.getTransitions()))
        self.assertIn(sequence_b, q4.getTransitions())
        # transition sequence_b in q4 leads to q5
        self.assertEqual(1, len(q4.getNextStates(sequence_b)))
        self.assertIn(q5, q4.getNextStates(sequence_b))    

        # in q5 there is no transition
        self.assertEqual(0, len(q5.getTransitions()))


    # see shuffleInShuffle.png in tests/testcases/fsms for fsm
    def test_shuffleInShuffle(self):

        shuffle_a = Transition(str, "A", "B")
        shuffle_b = PredicateTransition(bool, "B", "A", "==", True)
        send = Transition(int, "B", "A")

        fsm = self.buildFSM("shuffleInShuffle.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        
        # in q0 there are 3 transitions: shuffle_a, shuffle_b and send
        self.assertEqual(3, len(q0.getTransitions()))
        self.assertIn(shuffle_a, q0.getTransitions())
        self.assertIn(shuffle_b, q0.getTransitions())
        self.assertIn(send, q0.getTransitions())

        # transition shuffle_a in q0 leads to q2
        self.assertEqual(1, len(q0.getNextStates(shuffle_a)))
        q2 = list(q0.getNextStates(shuffle_a))[0]    
        # in q2 there is one transition: shuffle_b
        self.assertEqual(1, len(q2.getTransitions()))
        self.assertIn(shuffle_b, q2.getTransitions())
        # transition shuffle_b in q2 leads to q6
        self.assertEqual(1, len(q2.getNextStates(shuffle_b)))
        q6 = list(q2.getNextStates(shuffle_b))[0]    
        # transition shuffle_b in q0 leads to q3
        self.assertEqual(1, len(q0.getNextStates(shuffle_b)))
        q3 = list(q0.getNextStates(shuffle_b))[0]   
        # in q3 there is one transition: shuffle_a
        self.assertEqual(1, len(q3.getTransitions()))
        self.assertIn(shuffle_a, q3.getTransitions())
        # transition shuffle_a in q3 leads to q6
        self.assertEqual(1, len(q3.getNextStates(shuffle_a)))
        self.assertIn(q6, q3.getNextStates(shuffle_a))  
        # in q6 there is 1 transition: send
        self.assertEqual(1, len(q6.getTransitions()))
        self.assertIn(send, q6.getTransitions())
        # transition send in q6 leads to q7
        self.assertEqual(1, len(q6.getNextStates(send)))
        q7 = list(q6.getNextStates(send))[0]    

        # transition send in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(send)))
        q1 = list(q0.getNextStates(send))[0]    
        # transition shuffle_a in q1 leads to q4
        self.assertEqual(1, len(q1.getNextStates(shuffle_a)))
        q4 = list(q1.getNextStates(shuffle_a))[0]    
        # in q4 there is one transition: shuffle_b
        self.assertEqual(1, len(q4.getTransitions()))
        self.assertIn(shuffle_b, q4.getTransitions())
        # transition shuffle_b in q4 leads to q7
        self.assertEqual(1, len(q4.getNextStates(shuffle_b)))
        self.assertIn(q7, q4.getNextStates(shuffle_b))  
        # transition shuffle_b in q1 leads to q5
        self.assertEqual(1, len(q1.getNextStates(shuffle_b)))
        q5 = list(q1.getNextStates(shuffle_b))[0]   
        # in q5 there is one transition: shuffle_a
        self.assertEqual(1, len(q5.getTransitions()))
        self.assertIn(shuffle_a, q5.getTransitions())
        # transition shuffle_a in q5 leads to q7
        self.assertEqual(1, len(q5.getNextStates(shuffle_a)))
        self.assertIn(q7, q5.getNextStates(shuffle_a))  

        # in q7 there is no transition
        self.assertEqual(0, len(q7.getTransitions()))

    # see choiceInSequence.png in tests/testcases/fsms for fsm
    def test_choiceInSequence(self):

        choice_a = PredicateTransition(int, "A", "B", "<", 1024)
        choice_b = Transition(bool, "B", "A")
        send = Transition(int, "B", "A")

        fsm = self.buildFSM("choiceInSequence.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        
        # in q0 there are 2 transitions: choice_a, choice_b
        self.assertEqual(2, len(q0.getTransitions()))
        self.assertIn(choice_a, q0.getTransitions())
        self.assertIn(choice_b, q0.getTransitions())
        # transition choice_a in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(choice_a)))
        q1 = list(q0.getNextStates(choice_a))[0]            
        # transition choice_b in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(choice_a)))
        self.assertIn(q1, q0.getNextStates(choice_a))  
        # in q1 there is one transition: send
        self.assertEqual(1, len(q1.getTransitions()))
        self.assertIn(send, q1.getTransitions())
        # transition send in q1 leads to q2
        self.assertEqual(1, len(q1.getNextStates(send)))
        q2 = list(q1.getNextStates(send))[0]    
        # in q2 there is no transition
        self.assertEqual(0, len(q2.getTransitions()))


    # see sequenceInSequence.png in tests/testcases/fsms for fsm
    def test_sequenceInSequence(self):

        sequence_a = PredicateTransition(float, "A", "B", "<", -438923.34832488394834)
        sequence_b = PredicateTransition(bool, "B", "A", "==", True)
        send = Transition(str, "B", "A")

        fsm = self.buildFSM("sequenceInSequence.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there is one transitions: sequence_a
        self.assertEqual(1, len(q0.getTransitions()))
        self.assertIn(sequence_a, q0.getTransitions())
        # transition sequence_a in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(sequence_a)))
        q1 = list(q0.getNextStates(sequence_a))[0] 
        # in q1 there is one transition: sequence_b
        self.assertEqual(1, len(q1.getTransitions()))
        self.assertIn(sequence_b, q1.getTransitions())
        # transition sequence_b in q1 leads to q2
        self.assertEqual(1, len(q1.getNextStates(sequence_b)))
        q2 = list(q1.getNextStates(sequence_b))[0] 
        # in q2 there is one transition: send
        self.assertEqual(1, len(q2.getTransitions()))
        self.assertIn(send, q2.getTransitions())
        # transition send in q2 leads to q3
        self.assertEqual(1, len(q2.getNextStates(send)))
        q3 = list(q2.getNextStates(send))[0] 
        # in q3 there is no transition
        self.assertEqual(0, len(q3.getTransitions()))


    # see shuffleInSequence.png in tests/testcases/fsms for fsm
    def test_shuffleInSequence(self):

        shuffle_a = PredicateTransition(bool, "A", "B", "==", True)
        shuffle_b = Transition(bool, "B", "A")
        send = PredicateTransition(str, "B", "A", "==", "")

        fsm = self.buildFSM("shuffleInSequence.txt")
        
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there are 2 transitions: shuffle_a, shuffle_b
        self.assertEqual(2, len(q0.getTransitions()))
        self.assertIn(shuffle_a, q0.getTransitions())
        self.assertIn(shuffle_b, q0.getTransitions())

        # transition shuffle_a in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(shuffle_a)))
        q1 = list(q0.getNextStates(shuffle_a))[0]    
        # in q1 there is one transition: shuffle_b
        self.assertEqual(1, len(q1.getTransitions()))
        self.assertIn(shuffle_b, q1.getTransitions())
        # transition shuffle_b in q1 leads to q3
        self.assertEqual(1, len(q1.getNextStates(shuffle_b)))
        q3 = list(q1.getNextStates(shuffle_b))[0]    
        # transition shuffle_b in q0 leads to q2
        self.assertEqual(1, len(q0.getNextStates(shuffle_b)))
        q2 = list(q0.getNextStates(shuffle_b))[0]   
        # in q2 there is one transition: shuffle_a
        self.assertEqual(1, len(q2.getTransitions()))
        self.assertIn(shuffle_a, q2.getTransitions())
        # transition shuffle_a in q2 leads to q3
        self.assertEqual(1, len(q2.getNextStates(shuffle_a)))
        self.assertIn(q3, q2.getNextStates(shuffle_a))          
        # in q3 there is 1 transition: send
        self.assertEqual(1, len(q3.getTransitions()))
        self.assertIn(send, q3.getTransitions())
        # transition send in q3 leads to q4
        self.assertEqual(1, len(q3.getNextStates(send)))
        q4 = list(q3.getNextStates(send))[0]   
        # in q4 there is no transition
        self.assertEqual(0, len(q4.getTransitions()))


    # see choiceInChoice.png in tests/testcases/fsms for fsm
    def test_choiceInChoice(self):

        choice_a = PredicateTransition(float, "A", "B", "<=", -1.000000000)
        choice_b = PredicateTransition(float, "B", "A", ">=", 1.000000000)
        send = Transition(bool, "B", "A")

        fsm = self.buildFSM("choiceInChoice.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there are 3 transitions: send, choice_a and choice_b
        self.assertEqual(3, len(q0.getTransitions()))
        self.assertIn(choice_a, q0.getTransitions())
        self.assertIn(choice_b, q0.getTransitions())
        self.assertIn(send, q0.getTransitions())

        # transition choice_a in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(choice_a)))
        q1 = list(q0.getNextStates(choice_a))[0]   
        # transition choice_b in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(choice_b)))
        self.assertIn(q1, q0.getNextStates(choice_b))    
        # transition send in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(send)))
        self.assertIn(q1, q0.getNextStates(send))    
        # in q1 there is no transition
        self.assertEqual(0, len(q1.getTransitions()))


    # see sequenceInChoice.png in tests/testcases/fsms for fsm
    def test_sequenceInChoice(self):

        sequence_a = PredicateTransition(bool, "A", "B", "==", True)
        sequence_b = PredicateTransition(bool, "B", "A", "==", True)
        send = Transition(str, "B", "A")

        fsm = self.buildFSM("sequenceInChoice.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there is are two transitions: sequence_a, send
        self.assertEqual(2, len(q0.getTransitions()))
        self.assertIn(sequence_a, q0.getTransitions())
        self.assertIn(send, q0.getTransitions())

        # transition sequence_a in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(sequence_a)))
        q1 = list(q0.getNextStates(sequence_a))[0]   
        # in q1 there is one transition: sequence_b
        self.assertEqual(1, len(q1.getTransitions()))
        self.assertIn(sequence_b, q1.getTransitions())
        # transition sequence_b in q1 leads to q2
        self.assertEqual(1, len(q1.getNextStates(sequence_b)))
        q2 = list(q1.getNextStates(sequence_b))[0]   
        # transition send in q0 leads to q2
        self.assertEqual(1, len(q0.getNextStates(send)))
        self.assertIn(q2, q0.getNextStates(send)) 
        # in q2 there is no transition
        self.assertEqual(0, len(q2.getTransitions()))


    # see shuffleInChoice.png in tests/testcases/fsms for fsm
    def test_shuffleInChoice(self):

        shuffle_a = Transition(int, "A", "B")
        shuffle_b = Transition(bool, "B", "A")
        send = PredicateTransition(int, "B", "A", "<", -48790)

        fsm = self.buildFSM("shuffleInChoice.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        
        # in q0 there are 3 transitions: shuffle_a, shuffle_b and send
        self.assertEqual(3, len(q0.getTransitions()))
        self.assertIn(shuffle_a, q0.getTransitions())
        self.assertIn(shuffle_b, q0.getTransitions())
        self.assertIn(send, q0.getTransitions())

        # transition shuffle_a in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(shuffle_a)))
        q1 = list(q0.getNextStates(shuffle_a))[0]  
        # in q1 there is one transition: shuffle_b
        self.assertEqual(1, len(q1.getTransitions()))
        self.assertIn(shuffle_b, q1.getTransitions())
        # transition shuffle_b in q1 leads to q3
        self.assertEqual(1, len(q1.getNextStates(shuffle_b)))
        q3 = list(q1.getNextStates(shuffle_b))[0]  

        # transition shuffle_b in q0 leads to q2
        self.assertEqual(1, len(q0.getNextStates(shuffle_b)))
        q2 = list(q0.getNextStates(shuffle_b))[0]  
        # in q2 there is one transition: shuffle_a
        self.assertEqual(1, len(q2.getTransitions()))
        self.assertIn(shuffle_a, q2.getTransitions())
        # transition shuffle_a in q2 leads to q3
        self.assertEqual(1, len(q2.getNextStates(shuffle_a)))
        self.assertIn(q3, q2.getNextStates(shuffle_a))  

        # transition send in q0 leads to q3
        self.assertEqual(1, len(q0.getNextStates(send)))
        self.assertIn(q3, q0.getNextStates(send))  

        # in q3 there is no transition
        self.assertEqual(0, len(q3.getTransitions()))

    # see single_loop_deterministic.png in tests/testcases/fsms for fsm
    def test_single_loop_deterministic(self):
       
        t1_A_B = Transition(int, "A", "B")
        t2_B_A = Transition(bool, "B", "A")
        t3_B_A = Transition(str, "B", "A")

        fsm = self.buildFSM("single_loop_deterministic.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there is one transition
        self.assertEqual(1, len(q0.getTransitions()))
        self.assertIn(t1_A_B, q0.getTransitions())
        # transition t1_A_B in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(t1_A_B)))
        q1 = list(q0.getNextStates(t1_A_B))[0]  
        # in q1 there are two transitions: t2_B_A, t3_B_A
        self.assertEqual(2, len(q1.getTransitions()))
        self.assertIn(t2_B_A, q1.getTransitions())
        self.assertIn(t3_B_A, q1.getTransitions())
        # transition t2_B_A in q1 leads to q0
        self.assertEqual(1, len(q1.getNextStates(t2_B_A)))
        self.assertIn(q0, q1.getNextStates(t2_B_A))
        # transition t3_B_A in q1 leads to q2
        self.assertEqual(1, len(q1.getNextStates(t3_B_A)))
        q2 = list(q1.getNextStates(t3_B_A))[0]
        # in q2 there is no transition
        self.assertEqual(0, len(q2.getTransitions()))

    # see single_loop_non_deterministic.png in tests/testcases/fsms for fsm
    def test_single_loop_non_deterministic(self):
        
        t1_A_B = PredicateTransition(bool, "A", "B", "==", True)
        t2_B_A = PredicateTransition(int, "B", "A", ">=", -422390482308423)

        fsm = self.buildFSM("single_loop_non_deterministic.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there is one transition
        self.assertEqual(1, len(q0.getTransitions()))
        self.assertIn(t1_A_B, q0.getTransitions())
        # transition t1_A_B in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(t1_A_B)))
        q1 = list(q0.getNextStates(t1_A_B))[0]         
        # in q1 there is one transition
        self.assertEqual(1, len(q1.getTransitions()))
        self.assertIn(t2_B_A, q1.getTransitions())
        # transition t2_B_A in q1 leads to q0 and q2
        self.assertEqual(2, len(q1.getNextStates(t2_B_A)))
        self.assertIn(q0, q1.getNextStates(t2_B_A))
        if q0 is list(q1.getNextStates(t2_B_A))[0]:
            q2 = list(q1.getNextStates(t2_B_A))[1]
        else:
            q2 = list(q1.getNextStates(t2_B_A))[0]
        # in q2 there is no transition
        self.assertEqual(0, len(q2.getTransitions()))

    # see nested_loop_deterministic.png in tests/testcases/fsms for fsm
    def test_nested_loop_deterministic(self):
        
        t0_A_B = Transition(int, "A", "B")
        t1_A_B = Transition(str, "A", "B")
        t2_A_B = Transition(float, "A", "B")
        t3_B_A = PredicateTransition(bool, "B", "A", "==", True)
        t4_B_A = PredicateTransition(bool, "B", "A", "==", False)
        t5_B_A = PredicateTransition(str, "B", "A", "==", "hello world")

        fsm = self.buildFSM("nested_loop_deterministic.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there is one transition: t0_A_B
        self.assertEqual(1, len(q0.getTransitions()))
        self.assertIn(t0_A_B, q0.getTransitions())

        # transition t0_A_B in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(t0_A_B)))
        q1 = list(q0.getNextStates(t0_A_B))[0]   
        # in q1 there is one transition: t1_A_B
        self.assertEqual(1, len(q1.getTransitions()))
        self.assertIn(t1_A_B, q1.getTransitions())
        # transition t1_A_B in q1 leads to q2
        self.assertEqual(1, len(q1.getNextStates(t1_A_B)))
        q2 = list(q1.getNextStates(t1_A_B))[0]   
        # in q2 there is one transition: t2_A_B
        self.assertEqual(1, len(q2.getTransitions()))
        self.assertIn(t2_A_B, q2.getTransitions())
        # transition t2_A_B in q2 leads to q3
        self.assertEqual(1, len(q2.getNextStates(t2_A_B)))
        q3 = list(q2.getNextStates(t2_A_B))[0]   
        # in q3 there are three transitions: t3_B_A, t4_B_A and t5_B_A
        self.assertEqual(3, len(q3.getTransitions()))
        self.assertIn(t3_B_A, q3.getTransitions())
        self.assertIn(t4_B_A, q3.getTransitions())
        self.assertIn(t5_B_A, q3.getTransitions())

        # transition t4_B_A in q3 leads to q1
        self.assertEqual(1, len(q3.getNextStates(t4_B_A)))
        self.assertIn(q1, q3.getNextStates(t4_B_A))
        # transition t3_B_A in q3 leads to q2
        self.assertEqual(1, len(q3.getNextStates(t3_B_A)))
        self.assertIn(q2, q3.getNextStates(t3_B_A))
        # transition t5_B_A in q3 leads to q4
        self.assertEqual(1, len(q3.getNextStates(t5_B_A)))
        q4 = list(q3.getNextStates(t5_B_A))[0]   

        # in q4 there is no transition
        self.assertEqual(0, len(q4.getTransitions()))


    # see nested_loop_non_deterministic.png in tests/testcases/fsms for fsm
    def test_nested_loop_non_deterministic(self):
        
        t0_A_B = Transition(int, "A", "B")
        t1_A_B = PredicateTransition(str, "A", "B", "==", "s2348SJrfh2314")
        t2_A_B = Transition(bool, "A", "B")
        t3_B_A = PredicateTransition(bool, "B", "A", "==", True)
        t4_B_A = PredicateTransition(bool, "B", "A", "==", False)

        fsm = self.buildFSM("nested_loop_non_deterministic.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there is one transition: t0_A_B
        self.assertEqual(1, len(q0.getTransitions()))
        self.assertIn(t0_A_B, q0.getTransitions())

        # transition t0_A_B in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(t0_A_B)))
        q1 = list(q0.getNextStates(t0_A_B))[0]   
        # in q1 there is one transition: t1_A_B
        self.assertEqual(1, len(q1.getTransitions()))
        self.assertIn(t1_A_B, q1.getTransitions())
        # transition t1_A_B in q1 leads to q2
        self.assertEqual(1, len(q1.getNextStates(t1_A_B)))
        q2 = list(q1.getNextStates(t1_A_B))[0]   
        # in q2 there is one transition: t2_A_B
        self.assertEqual(1, len(q2.getTransitions()))
        self.assertIn(t2_A_B, q2.getTransitions())
        # transition t2_A_B in q2 leads to q3
        self.assertEqual(1, len(q2.getNextStates(t2_A_B)))
        q3 = list(q2.getNextStates(t2_A_B))[0]   
        # in q3 there are two transitions: t3_B_A and t4_B_A
        self.assertEqual(2, len(q3.getTransitions()))
        self.assertIn(t3_B_A, q3.getTransitions())
        self.assertIn(t4_B_A, q3.getTransitions())

        # transition t3_B_A in q3 leads to q1 and q2
        self.assertEqual(2, len(q3.getNextStates(t3_B_A)))
        self.assertIn(q1, q3.getNextStates(t3_B_A))
        self.assertIn(q2, q3.getNextStates(t3_B_A))
        # transition t4_B_A in q3 leads to q4
        self.assertEqual(1, len(q3.getNextStates(t4_B_A)))
        q4 = list(q3.getNextStates(t4_B_A))[0]   

        # in q4 there is no transition
        self.assertEqual(0, len(q4.getTransitions()))


    # see intertwined_loops.png in tests/testcases/fsms for fsm
    def test_intertwined_loops(self):

        t0_A_B = Transition(bool, "A", "B")
        t1_A_B = Transition(int, "A", "B")
        t2_A_B = Transition(bool, "A", "B")
        t3_B_A = PredicateTransition(int, "B", "A", "<=", -42342432)
        t4_B_C = Transition(int, "B", "C")
        t5_C_A = PredicateTransition(float, "C", "A", "<", 3.9)
        t6_C_D = Transition(str, "C", "D")

        fsm = self.buildFSM("intertwined_loops.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there is one transition: t0_A_B
        self.assertEqual(1, len(q0.getTransitions()))
        self.assertIn(t0_A_B, q0.getTransitions())
        # transition t0_A_B in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(t0_A_B)))
        q1 = list(q0.getNextStates(t0_A_B))[0]   
        # in q1 there is one transition: t1_A_B
        self.assertEqual(1, len(q1.getTransitions()))
        self.assertIn(t1_A_B, q1.getTransitions())
        # transition t1_A_B in q1 leads to q2
        self.assertEqual(1, len(q1.getNextStates(t1_A_B)))
        q2 = list(q1.getNextStates(t1_A_B))[0]   
        # in q2 there is one transition: t2_A_B
        self.assertEqual(1, len(q2.getTransitions()))
        self.assertIn(t2_A_B, q2.getTransitions())
        # transition t2_A_B in q2 leads to q3
        self.assertEqual(1, len(q2.getNextStates(t2_A_B)))
        q3 = list(q2.getNextStates(t2_A_B))[0]   
        # in q3 there are 2 transitions: t3_B_A and t4_B_C
        self.assertEqual(2, len(q3.getTransitions()))
        self.assertIn(t3_B_A, q3.getTransitions())
        self.assertIn(t4_B_C, q3.getTransitions())
        # transition t3_B_A in q3 leads to q1
        self.assertEqual(1, len(q3.getNextStates(t3_B_A)))
        self.assertIn(q1, q3.getNextStates(t3_B_A))
        # transition t4_B_C in q3 leads to q4
        self.assertEqual(1, len(q3.getNextStates(t4_B_C)))
        q4 = list(q3.getNextStates(t4_B_C))[0]         
        # in q4 there are 2 transitions: t5_C_A and t6_C_D
        self.assertEqual(2, len(q4.getTransitions()))
        self.assertIn(t5_C_A, q4.getTransitions())
        self.assertIn(t6_C_D, q4.getTransitions())
        # transition t5_C_A in q4 leads to q2
        self.assertEqual(1, len(q4.getNextStates(t5_C_A)))
        self.assertIn(q2, q4.getNextStates(t5_C_A))
        # transition t6_C_D in q4 leads to q5
        self.assertEqual(1, len(q4.getNextStates(t6_C_D)))
        q5 = list(q4.getNextStates(t6_C_D))[0]   
        
        # in q5 there is no transition
        self.assertEqual(0, len(q5.getTransitions()))


    # see non_intertwined_loops.png in tests/testcases/fsms for fsm
    def test_non_intertwined_loops(self):

        t0_A_B = Transition(bool, "A", "B")
        t1_A_B = PredicateTransition(str, "A", "B", "!=", "420691337")
        t2_B_A = PredicateTransition(bool, "B", "A", "==", False)
        t3_B_C = PredicateTransition(bool, "B", "C", "==", False)
        t4_B_C = Transition(int, "B", "C")
        t5_C_D = Transition(int, "C", "D")
        t6_D_B = PredicateTransition(bool, "D", "B", "==", False)
        t7_D_E = Transition(str, "D", "E")

        fsm = self.buildFSM("non_intertwined_loops.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there is one transition: t0_A_B
        self.assertEqual(1, len(q0.getTransitions()))
        self.assertIn(t0_A_B, q0.getTransitions())
        # transition t0_A_B in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(t0_A_B)))
        q1 = list(q0.getNextStates(t0_A_B))[0]   
        # in q1 there is one transition: t1_A_B
        self.assertEqual(1, len(q1.getTransitions()))
        self.assertIn(t1_A_B, q1.getTransitions())
        # transition t1_A_B in q1 leads to q2
        self.assertEqual(1, len(q1.getNextStates(t1_A_B)))
        q2 = list(q1.getNextStates(t1_A_B))[0]   
        # in q2 there is are 2 transitions: t2_B_A and t3_B_C
        self.assertEqual(2, len(q2.getTransitions()))
        self.assertIn(t2_B_A, q2.getTransitions())
        self.assertIn(t3_B_C, q2.getTransitions())
        # transition t2_B_A in q2 leads to q1
        self.assertEqual(1, len(q2.getNextStates(t2_B_A)))
        self.assertIn(q1, q2.getNextStates(t2_B_A))
        # transition t3_B_C in q2 leads to q3
        self.assertEqual(1, len(q2.getNextStates(t3_B_C)))
        q3 = list(q2.getNextStates(t3_B_C))[0]  
        # in q3 there is one transition: t4_B_C
        self.assertEqual(1, len(q3.getTransitions()))
        self.assertIn(t4_B_C, q3.getTransitions())
        # transition t4_B_C in q3 leads to q4
        self.assertEqual(1, len(q3.getNextStates(t4_B_C)))
        q4 = list(q3.getNextStates(t4_B_C))[0]   
        # in q4 there is one transition: t5_C_D
        self.assertEqual(1, len(q4.getTransitions()))
        self.assertIn(t5_C_D, q4.getTransitions())
        # transition t5_C_D in q4 leads to q5
        self.assertEqual(1, len(q4.getNextStates(t5_C_D)))
        q5 = list(q4.getNextStates(t5_C_D))[0]   
        # in q5 there is are 2 transitions: t6_D_B and t7_D_E
        self.assertEqual(2, len(q5.getTransitions()))
        self.assertIn(t6_D_B, q5.getTransitions())
        self.assertIn(t7_D_E, q5.getTransitions())
        # transition t6_D_B in q5 leads to q3
        self.assertEqual(1, len(q5.getNextStates(t6_D_B)))
        self.assertIn(q3, q5.getNextStates(t6_D_B))
        # transition t7_D_E in q5 leads to q6
        self.assertEqual(1, len(q5.getNextStates(t7_D_E)))
        q6 = list(q5.getNextStates(t7_D_E))[0]

        # in q6 there is no transition
        self.assertEqual(0, len(q6.getTransitions()))
        

    # see connected_loops_perpetual.png in tests/testcases/fsms for fsm
    def test_connected_loops_perpetual(self):
    
        t0_A_B = Transition(str, "A", "B")
        t1_B_C = Transition(str, "B", "C")
        t2_C_B = Transition(int, "C", "B")
        t2_B_A = Transition(float, "B", "A")

        fsm = self.buildFSM("connected_loops_perpetual.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there is one transition: t0_A_B
        self.assertEqual(1, len(q0.getTransitions()))
        self.assertIn(t0_A_B, q0.getTransitions())
        # transition t0_A_B in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(t0_A_B)))
        q1 = list(q0.getNextStates(t0_A_B))[0]   
        # in q1 there are two transitions: t2_B_A and t1_B_C
        self.assertEqual(2, len(q1.getTransitions()))
        self.assertIn(t2_B_A, q1.getTransitions())
        self.assertIn(t1_B_C, q1.getTransitions())
        # transition t2_B_A in q1 leads to q0
        self.assertEqual(1, len(q1.getNextStates(t2_B_A)))
        self.assertIn(q0, q1.getNextStates(t2_B_A))
        # transition t1_B_C in q1 leads to q2
        self.assertEqual(1, len(q1.getNextStates(t1_B_C)))
        q2 = list(q1.getNextStates(t1_B_C))[0]
        # in q2 there is one transition: t2_B_C
        self.assertEqual(1, len(q2.getTransitions()))
        self.assertIn(t2_C_B, q2.getTransitions())
        # transition t2_C_B in q2 leads to q1
        self.assertEqual(1, len(q2.getNextStates(t2_C_B)))
        self.assertIn(q1, q2.getNextStates(t2_C_B))

    # see nested_loops.png in tests/testcases/fsms for fsm
    def test_nested_loops(self):

        t0_A_B = Transition(int, "A", "B")
        t1_A_B = Transition(bool, "A", "B")
        t2_A_B = Transition(str, "A", "B")
        t3_B_A = PredicateTransition(bool, "B", "A", "==", False)
        t4_B_C = PredicateTransition(bool, "B", "C", "==", True)
        t5_C_A = Transition(str, "C", "A")
        t6_C_D = Transition(float, "C", "D")

        fsm = self.buildFSM("nested_loops.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there is one transition: t0_A_B
        self.assertEqual(1, len(q0.getTransitions()))
        self.assertIn(t0_A_B, q0.getTransitions())
        # transition t0_A_B in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(t0_A_B)))
        q1 = list(q0.getNextStates(t0_A_B))[0]   
        # in q1 there is one transition: t1_A_B
        self.assertEqual(1, len(q1.getTransitions()))
        self.assertIn(t1_A_B, q1.getTransitions())
        # transition t1_A_B in q1 leads to q2
        self.assertEqual(1, len(q1.getNextStates(t1_A_B)))
        q2 = list(q1.getNextStates(t1_A_B))[0]   
        # in q2 there is one transition: t2_A_B
        self.assertEqual(1, len(q2.getTransitions()))
        self.assertIn(t2_A_B, q2.getTransitions())
        # transition t2_A_B in q2 leads to q3
        self.assertEqual(1, len(q2.getNextStates(t2_A_B)))
        q3 = list(q2.getNextStates(t2_A_B))[0]   
        # in q3 there are 2 transitions: t3_B_A and t4_B_C
        self.assertEqual(2, len(q3.getTransitions()))
        self.assertIn(t3_B_A, q3.getTransitions())
        self.assertIn(t4_B_C, q3.getTransitions())
        # transition t3_B_A in q3 leads to q2
        self.assertEqual(1, len(q3.getNextStates(t3_B_A)))
        self.assertIn(q2, q3.getNextStates(t3_B_A))
        # transition t4_B_C in q3 leads to q4
        self.assertEqual(1, len(q3.getNextStates(t4_B_C)))
        q4 = list(q3.getNextStates(t4_B_C))[0]         
        # in q4 there are 2 transitions: t5_C_A and t6_C_D
        self.assertEqual(2, len(q4.getTransitions()))
        self.assertIn(t5_C_A, q4.getTransitions())
        self.assertIn(t6_C_D, q4.getTransitions())
        # transition t5_C_A in q4 leads to q1
        self.assertEqual(1, len(q4.getNextStates(t5_C_A)))
        self.assertIn(q1, q4.getNextStates(t5_C_A))
        # transition t6_C_D in q4 leads to q5
        self.assertEqual(1, len(q4.getNextStates(t6_C_D)))
        q5 = list(q4.getNextStates(t6_C_D))[0]           
        # in q5 there is no transition
        self.assertEqual(0, len(q5.getTransitions()))

    # see one_loop_multiple_repeats.png in tests/testcases/fsms for fsm
    def one_loop_multiple_repeats(self):
        
        t0_A_B = PredicateTransition(int, "A", "B", "!=", 0)
        t1_A_B = Transition(str, "A", "B")
        t2_B_C = Transition(str, "B", "C")
        t3_B_A = Transition(bool, "B", "A")
        t3_C_A = Transition(bool, "C", "A")
        t4_C_D = Transition(float, "C", "D")

        fsm = self.buildFSM("one_loop_multiple_repeats.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there is one transition: t0_A_B
        self.assertEqual(1, len(q0.getTransitions()))
        self.assertIn(t0_A_B, q0.getTransitions())
        # transition t0_A_B in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(t0_A_B)))
        q1 = list(q0.getNextStates(t0_A_B))[0]
        # in q1 there is one transition: t1_A_B
        self.assertEqual(1, len(q1.getTransitions()))
        self.assertIn(t1_A_B, q1.getTransitions())
        # transition t1_A_B in q1 leads to q2
        self.assertEqual(1, len(q1.getNextStates(t1_A_B)))
        q2 = list(q1.getNextStates(t1_A_B))[0]   
        # in q2 there is are two transitions: t2_B_C and t3_B_A
        self.assertEqual(2, len(q2.getTransitions()))
        self.assertIn(t2_B_C, q2.getTransitions())
        self.assertIn(t3_B_A, q2.getTransitions())
        # transition t3_B_A in q2 leads to q1
        self.assertEqual(1, len(q2.getNextStates(t3_B_A)))
        self.assertIn(q1, q2.getNextStates(t3_B_A))
        # transition t2_B_C in q2 leads to q3
        self.assertEqual(1, len(q2.getNextStates(t2_B_C)))
        q3 = list(q2.getNextStates(t2_B_C))[0]   
        # in q3 there is are two transitions: t3_C_A and t4_C_D
        self.assertEqual(2, len(q3.getTransitions()))
        self.assertIn(t3_C_A, q3.getTransitions())
        self.assertIn(t4_C_D, q3.getTransitions())
        # transition t3_C_A in q3 leads to q1
        self.assertEqual(1, len(q3.getNextStates(t3_C_A)))
        self.assertIn(q1, q3.getNextStates(t3_C_A))
        # transition t4_C_D in q3 leads to q4
        self.assertEqual(1, len(q3.getNextStates(t4_C_D)))
        q4 = list(q3.getNextStates(t4_C_D))[0]   
        # in q4 there are no transitions
        self.assertEqual(0, len(q4.getTransitions()))

    # see choice_loop_sequence.png in tests/testcases/fsms for fsm
    def test_choice_loop_sequence(self):
        
        t1_A_B = PredicateTransition(int, "A", "B", ">", 0)
        t1_A_C = PredicateTransition(int, "A", "C", ">", 0)
        t2_A_C = Transition(str, "A", "C")
        t4_C_B = PredicateTransition(bool, "C", "B", "==", False)
        t3_B_D = Transition(int, "B", "D")
        t4_C_D = PredicateTransition(bool, "C", "D", "==", False)

        fsm = self.buildFSM("choice_loop_sequence.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there is one transition: t1_A_B
        self.assertEqual(1, len(q0.getTransitions()))
        self.assertIn(t1_A_B, q0.getTransitions())
        # transition t1_A_B in q0 leads to q1 and q2
        self.assertEqual(2, len(q0.getNextStates(t1_A_B)))
        if t1_A_C in list(q0.getNextStates(t1_A_B))[0].getTransitions():
            q1 = list(q0.getNextStates(t1_A_B))[0]
            q2 = list(q0.getNextStates(t1_A_B))[1]
        elif t1_A_C in list(q0.getNextStates(t1_A_B))[1].getTransitions():
            q1 = list(q0.getNextStates(t1_A_B))[1]
            q2 = list(q0.getNextStates(t1_A_B))[0]
        else:
            # neither state features transition t1_A_C
            self.fail
        # in q1 there is one transition: t1_A_C
        self.assertEqual(1, len(q1.getTransitions()))
        self.assertIn(t1_A_C, q1.getTransitions())
        # transition t1_A_C in q1 leads to q3
        self.assertEqual(1, len(q1.getNextStates(t1_A_C)))
        q3 = list(q1.getNextStates(t1_A_C))[0]   
        # in q2 there is one transition: t2_A_C
        self.assertEqual(1, len(q2.getTransitions()))
        self.assertIn(t2_A_C, q2.getTransitions())
        # transition t2_A_C in q2 leads to q3
        self.assertEqual(1, len(q2.getNextStates(t2_A_C)))
        self.assertIn(q3, q2.getNextStates(t2_A_C))          
        # in q3 there are two transitions: t4_C_B and t3_B_D
        self.assertEqual(2, len(q3.getTransitions()))
        self.assertIn(t4_C_B, q3.getTransitions())
        self.assertIn(t3_B_D, q3.getTransitions())
        # transition t4_C_B in q3 leads to q0
        self.assertEqual(1, len(q3.getNextStates(t4_C_B)))
        self.assertIn(q0, q3.getNextStates(t4_C_B))
        # transition t3_B_D in q3 leads to q4
        self.assertEqual(1, len(q3.getNextStates(t3_B_D)))
        q4 = list(q3.getNextStates(t3_B_D))[0]
        # in q4 there is one transition: t4_C_D
        self.assertEqual(1, len(q4.getTransitions()))
        self.assertIn(t4_C_D, q4.getTransitions())
        # transition t4_C_D in q4 leads to q5
        self.assertEqual(1, len(q4.getNextStates(t4_C_D)))
        q5 = list(q4.getNextStates(t4_C_D))[0]        
        # in q5 there is no transition
        self.assertEqual(0, len(q5.getTransitions()))

    # see shuffle_loop_sequence.png in tests/testcases/fsms for fsm
    def test_shuffle_loop_sequence(self):
        
        t1_A_B = Transition(bool, "A", "B")
        t2_B_A = Transition(str, "B", "A")
        t3_B_D = Transition(float, "B", "D")
        t4_C_D = Transition(float, "C", "D")

        fsm = self.buildFSM("shuffle_loop_sequence.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there are two transitions: t3_B_D and t4_C_D
        self.assertEqual(2, len(q0.getTransitions()))
        self.assertIn(t3_B_D, q0.getTransitions())
        self.assertIn(t4_C_D, q0.getTransitions())

        # transition t3_B_D in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(t3_B_D)))
        q1 = list(q0.getNextStates(t3_B_D))[0]   
        # in q1 there is one transition: t4_C_D
        self.assertEqual(1, len(q1.getTransitions()))
        self.assertIn(t4_C_D, q1.getTransitions())
        # transition t4_C_D in q1 leads to q3
        self.assertEqual(1, len(q1.getNextStates(t4_C_D)))
        q3 = list(q1.getNextStates(t4_C_D))[0]   
        # transition t4_C_D in q0 leads to q2
        self.assertEqual(1, len(q0.getNextStates(t4_C_D)))
        q2 = list(q0.getNextStates(t4_C_D))[0]   
        # in q2 there is one transition: t3_B_D
        self.assertEqual(1, len(q2.getTransitions()))
        self.assertIn(t3_B_D, q2.getTransitions())
        # transition t3_B_D in q2 leads to q3
        self.assertEqual(1, len(q2.getNextStates(t3_B_D)))
        self.assertIn(q3, q2.getNextStates(t3_B_D)) 
        # in q3 there is one transition: t1_A_B
        self.assertEqual(1, len(q3.getTransitions()))
        self.assertIn(t1_A_B, q3.getTransitions())
        # transition t1_A_B in q3 leads to q0 and q4
        self.assertEqual(2, len(q3.getNextStates(t1_A_B)))
        self.assertIn(q0, q3.getNextStates(t1_A_B))
        if q0 is list(q3.getNextStates(t1_A_B))[0]:
            q4 = list(q3.getNextStates(t1_A_B))[1]
        else:
            q4 = list(q3.getNextStates(t1_A_B))[0]
        # in q4 there is one transition: t2_B_A
        self.assertEqual(1, len(q4.getTransitions()))
        self.assertIn(t2_B_A, q4.getTransitions())
        # transition t2_B_A in q4 leads to q5
        self.assertEqual(1, len(q4.getNextStates(t2_B_A)))
        q5 = list(q4.getNextStates(t2_B_A))[0]           
        # in q5 there is no transition
        self.assertEqual(0, len(q5.getTransitions()))

    # see loop_choice.png in tests/testcases/fsms for fsm
    def test_loop_choice(self):

        t1_A_B = PredicateTransition(bool, "A", "B", "==", False)
        t2_A_B = PredicateTransition(bool, "A", "B", "==", True)

        fsm = self.buildFSM("loop_choice.txt")

        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]

        # in q0 there are two transitions: t1_A_B and t2_A_B
        self.assertEqual(2, len(q0.getTransitions()))
        self.assertIn(t1_A_B, q0.getTransitions())
        self.assertIn(t2_A_B, q0.getTransitions())

        # transition t1_A_B in q0 leads to q0
        self.assertEqual(1, len(q0.getNextStates(t1_A_B)))
        self.assertIn(q0, q0.getNextStates(t1_A_B)) 
        # transition t2_A_B in q0 leads to q1
        self.assertEqual(1, len(q0.getNextStates(t2_A_B)))
        q1 = list(q0.getNextStates(t2_A_B))[0]
        # in q1 there is no transition
        self.assertEqual(0, len(q1.getTransitions()))


    def buildFSM(self, fileName):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        specification_path = os.path.join(current_directory, "testcases", fileName)
        input = FileStream(specification_path)           
        lexer = PythonicLexer(input)
        stream = CommonTokenStream(lexer)
        parser = PythonicParser(stream)
        tree = parser.specification() 
        fsm_builder = FSMbuilder()
        return fsm_builder.visitSpecification(tree)[0]


if __name__ == '__main__':
    unittest.main()
