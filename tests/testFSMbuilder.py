"""  
Testopzet voor het testen van FSMBuilder. TestFSMBuilder moet testen of
het opbouwen van de FSM goed verloopt; oftewel, dat de juiste transities 
en states worden aangemaakt en correct met elkaar worden verbonden. 
Merk op dat in deze klasse het bouwen van de FSM wordt getest, niet de
juist werking van de FSM. Voor dat laatste dient testFSM. 

Conform het algoritme geldt dat de eerste operation binnen een compound
operation begint vanuit de start state van de compound operation en de 
laatste operation binnen de compound operation eindigt in de end state
van de compound operation, ongeacht of de eerste, laatste en tussenliggende
operations atomic of zelf ook compound operations zijn. Verder geldt dat 
wanneer een compound operation haar deeloperations a en b uitvoert in de 
volgorde a en dan b, de end state van a de start state van b vormt.

"""

import unittest
import os
from antlr4 import CommonTokenStream, FileStream
from antlrFiles.PythonicLexer import PythonicLexer
from antlrFiles.PythonicParser import PythonicParser
from src.core.FSMbuilder import FSMbuilder
from src.core.transition import Transition

class TestFSMBuilder(unittest.TestCase):

    def test_singleSend(self):
        # see singleSend.png in tests/testcases/fsms for fsm
        fsm = self.buildFSM("singleSend.txt")
        q0 = fsm.getState()
        send = Transition("U", "B", "A")
        # in q0 there is one transition: send
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(send, q0.transitionsToStates)

        # make transition send
        fsm.makeTransition(send)
        q1 = fsm.getState()
        # in q1 there is no transition
        self.assertEqual(0, len(q1.transitionsToStates))
    
    def test_singleChoice(self):
        # see singleChoice.png in tests/testcases/fsms for fsm
        fsm = self.buildFSM("singleChoice.txt")
        q0 = fsm.getState()
        choice_a = Transition("V", "A", "B")
        choice_b = Transition("W", "B", "A")
        # in q0 there are two transitions: choice_a and choice_b
        self.assertEqual(2, len(q0.transitionsToStates))
        self.assertIn(choice_a, q0.transitionsToStates)
        self.assertIn(choice_b, q0.transitionsToStates)

        # make transition choice_a
        fsm.makeTransition(choice_a)
        q1_a = fsm.getState()
        # in q1_a there is no transition
        self.assertEqual(0, len(q1_a.transitionsToStates))

        # reset fsm
        fsm.state = q0

        # make transition choice_b
        fsm.makeTransition(choice_b)
        q1_b = fsm.getState()
        # in q1_b there is no transition
        self.assertEqual(0, len(q1_b.transitionsToStates))

        # q1_a and q1_b are the same state
        self.assertEqual(q1_a, q1_b)

    def test_singleSequence(self):
        # see singleSequence.png in tests/testcases/fsms for fsm
        fsm = self.buildFSM("singleSequence.txt")
        q0 = fsm.getState()
        sequence_a = Transition("Q", "A", "B")
        sequence_b = Transition("R", "B", "A")
        # in start_state there is one transition: send_1
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(sequence_a, q0.transitionsToStates)

        # make transition sequence_a
        fsm.makeTransition(sequence_a)
        q1 = fsm.getState()
        # in q1 there is one transition: sequence_b
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(sequence_b, q1.transitionsToStates)

        # make transition sequence_b
        fsm.makeTransition(sequence_b)
        q2 = fsm.getState()
        # in q2 there is no transition
        self.assertEqual(0, len(q2.transitionsToStates))

    def test_singleShuffle(self):
        # see singleShuffle.png in tests/testcases/fsms for fsm
        fsm = self.buildFSM("singleShuffle.txt")
        q0 = fsm.getState()
        shuffle_a = Transition("X", "A", "B")
        shuffle_b = Transition("Y", "B", "A")
        # in q0 there are two transitions: shuffle_a and shuffle_b
        self.assertEqual(2, len(q0.transitionsToStates))
        self.assertIn(shuffle_a, q0.transitionsToStates)
        self.assertIn(shuffle_b, q0.transitionsToStates)

        # perform shuffle: first shuffle_a then shuffle_b
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        q1 = fsm.getState()
        # in q1 there is one transition: shuffle_b
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(shuffle_b, q1.transitionsToStates)
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        q3_a_b = fsm.getState()
        # in q3_a_b there is no transition
        self.assertEqual(0, len(q3_a_b.transitionsToStates))

        # reset fsm
        fsm.state = q0

        # perform shuffle: first shuffle_b then shuffle_a
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        q2 = fsm.getState()
        # in q2 there is one transition: shuffle_a
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(shuffle_a, q2.transitionsToStates)
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        q3_b_a = fsm.getState()
        # in q3_b_a there is no transition
        self.assertEqual(0, len(q3_b_a.transitionsToStates))
        
        # q3_a_b and q3_b_a are the same state
        self.assertEqual(q3_a_b, q3_b_a)

    def test_choiceInShuffle(self):
        # see choiceInShuffle.png in tests/testcases/fsms for fsm
        fsm = self.buildFSM("choiceInShuffle.txt")
        q0 = fsm.getState()
        send = Transition("U", "B", "A")
        choice_a = Transition("V", "A", "B")
        choice_b = Transition("W", "B", "A")
        # in q0 there are 3 transitions: choice_a, choice_b and send
        self.assertEqual(3, len(q0.transitionsToStates))
        self.assertIn(choice_a, q0.transitionsToStates)
        self.assertIn(choice_b, q0.transitionsToStates)
        self.assertIn(send, q0.transitionsToStates)

        # perform shuffle: first send then choice
        # make transition send
        fsm.makeTransition(send)
        q1 = fsm.getState()
        # in q1 there are 2 transitions: 
        self.assertEqual(2, len(q1.transitionsToStates))
        self.assertIn(choice_a, q1.transitionsToStates)
        self.assertIn(choice_b, q1.transitionsToStates)
        # make transition choice_a
        fsm.makeTransition(choice_a)
        q3_send_a = fsm.getState()
        # in q3_send_a there is no transition
        self.assertEqual(0, len(q3_send_a.transitionsToStates))
        # revert fsm to q1
        fsm.state = q1
        # make transition choice_b
        fsm.makeTransition(choice_b)
        q3_send_b = fsm.getState()
        # in q3_send_b there is no transition
        self.assertEqual(0, len(q3_send_b.transitionsToStates))
        # q3_send_a and q3_send_b are the same state
        self.assertEqual(q3_send_a, q3_send_b)

        # revert fsm to q0
        fsm.state = q0

        # perform shuffle: first choice then send
        # make transition choice_a
        fsm.makeTransition(choice_a)
        q2_a = fsm.getState()
        # in q2_a there is 1 transition: send
        self.assertEqual(1, len(q2_a.transitionsToStates))
        self.assertIn(send, q2_a.transitionsToStates)
        # revert fsm to q0
        fsm.state = q0
        # make transition choice_b
        fsm.makeTransition(choice_b)
        q2_b = fsm.getState()
        # in q2_b there is 1 transition: send
        self.assertEqual(1, len(q2_b.transitionsToStates))
        self.assertIn(send, q2_b.transitionsToStates)
        # q2_a and q2_b are the same state
        self.assertEqual(q2_a, q2_b)
        # make transition send
        fsm.makeTransition(send)
        q3_b_send = fsm.getState()
        # in q3_b_send there is no transition
        self.assertEqual(0, len(q3_b_send.transitionsToStates))

        # q3_b_send and q3_send_b are the same state
        self.assertEqual(q3_b_send, q3_send_b)

    def test_sequenceInShuffle(self):
        # see sequenceInShuffle.png in tests/testcases/fsms for fsm
        fsm = self.buildFSM("sequenceInShuffle.txt")
        q0 = fsm.getState()
        send = Transition("U", "B", "A")
        sequence_a = Transition("Q", "A", "B")
        sequence_b = Transition("R", "B", "A")
        # in q0 there are 2 transitions: sequence_a and send
        self.assertEqual(2, len(q0.transitionsToStates))
        self.assertIn(sequence_a, q0.transitionsToStates)
        self.assertIn(send, q0.transitionsToStates)

        # perform shuffle: first sequence then send
        # make transition sequence_a
        fsm.makeTransition(sequence_a)
        q1 = fsm.getState()
        # in q1 there is one transition: sequence_b
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(sequence_b, q1.transitionsToStates)
        # make transition sequence_b
        fsm.makeTransition(sequence_b)
        q3 = fsm.getState()
        # in q3 there is one transition: send
        self.assertEqual(1, len(q3.transitionsToStates))
        # make transition send
        fsm.makeTransition(send)
        q5_sequence_send = fsm.getState()
        # in q5_sequence_send there is no transition
        self.assertEqual(0, len(q5_sequence_send.transitionsToStates))

        # reset fsm
        fsm.state = q0

        # perform shuffle: first send then sequence
        # make transition send
        fsm.makeTransition(send)
        q2 = fsm.getState()
        # in q2 there is one transition: sequence_a
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(sequence_a, q2.transitionsToStates)        
        # make transition sequence_a
        fsm.makeTransition(sequence_a)
        q4 = fsm.getState()
        # in q4 there is one transition: sequence_b
        self.assertEqual(1, len(q4.transitionsToStates))
        self.assertIn(sequence_b, q4.transitionsToStates)        
        # make transition sequence_b
        fsm.makeTransition(sequence_b)
        q5_send_sequence = fsm.getState()
        # in q5_send_sequence there is no transition
        self.assertEqual(0, len(q5_send_sequence.transitionsToStates))

        # q5_sequence_send and q5_send_sequence are the same state
        self.assertEqual(q5_sequence_send, q5_send_sequence)

    def test_shuffleInShuffle(self):
        # see shuffleInShuffle.png in tests/testcases/fsms for fsm
        fsm = self.buildFSM("shuffleInShuffle.txt")
        q0 = fsm.getState()
        shuffle_a = Transition("X", "A", "B")
        shuffle_b = Transition("Y", "B", "A")
        send = Transition("U", "B", "A")
        # in q0 there are 3 transitions: shuffle_a, shuffle_b and send
        self.assertEqual(3, len(q0.transitionsToStates))
        self.assertIn(shuffle_a, q0.transitionsToStates)
        self.assertIn(shuffle_b, q0.transitionsToStates)
        self.assertIn(send, q0.transitionsToStates)

        # perform shuffle: first shuffle then send
        # perform shuffle: first shuffle_a then shuffle_b
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        q2 = fsm.getState()
        # in q2 there is one transition: shuffle_b
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(shuffle_b, q2.transitionsToStates)
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        q6_a_b = fsm.getState() 
        # in q6_a_b there is 1 transition: send
        self.assertEqual(1, len(q6_a_b.transitionsToStates))
        self.assertIn(send, q6_a_b.transitionsToStates)
        # reset fsm
        fsm.state = q0
        # perform shuffle: first shuffle_b then shuffle_a
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        q3 = fsm.getState()
        # in q3 there is one transition: shuffle_a
        self.assertEqual(1, len(q3.transitionsToStates))
        self.assertIn(shuffle_a, q3.transitionsToStates)
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        q6_b_a = fsm.getState()
        # in q6_b_a there is 1 transition: send
        self.assertEqual(1, len(q6_b_a.transitionsToStates))
        self.assertIn(send, q6_b_a.transitionsToStates)
        # q6_a_b and q6_b_a are the same state
        self.assertEqual(q6_a_b, q6_b_a)        
        # make transition send
        fsm.makeTransition(send)
        q7_shuffle_b_a_send = fsm.getState()
        # in q7_shuffle_b_a_send there is no transition
        self.assertEqual(0, len(q7_shuffle_b_a_send.transitionsToStates))

        # reset fsm
        fsm.state = q0

        # perform shuffle: first send then shuffle
        # make transition send
        fsm.makeTransition(send)
        q1 = fsm.getState()
        # in q1 there are two transitions: shuffle_a and shuffle_b
        self.assertEqual(2, len(q1.transitionsToStates))
        self.assertIn(shuffle_a, q1.transitionsToStates)
        self.assertIn(shuffle_b, q1.transitionsToStates)
        # perform inner shuffle: first shuffle_b then shuffle_a
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        q5 = fsm.getState()
        # in q5 there is one transition: shuffle_a
        self.assertEqual(1, len(q5.transitionsToStates))
        self.assertIn(shuffle_a, q5.transitionsToStates)
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        q7_send_shuffle_b_a = fsm.getState()
        # in q7_send_shuffle_b_a there is no transition
        self.assertEqual(0, len(q7_send_shuffle_b_a.transitionsToStates))
        # revert fsm to q1
        fsm.state = q1
        # perform inner shuffle: first shuffle_a then shuffle_b
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        q4 = fsm.getState()
        # in q2 there is one transition: shuffle_b
        self.assertEqual(1, len(q4.transitionsToStates))
        self.assertIn(shuffle_b, q4.transitionsToStates)
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        q7_send_shuffle_a_b = fsm.getState() 
        # in q7_send_shuffle_a_b there is no transition
        self.assertEqual(0, len(q7_send_shuffle_a_b.transitionsToStates))
        
        # q7_send_shuffle_b_a, q7_send_shuffle_a_b 
        # and q7_shuffle_b_a_send are the same state
        self.assertEqual(q7_send_shuffle_b_a, q7_send_shuffle_a_b)
        self.assertEqual(q7_shuffle_b_a_send, q7_send_shuffle_b_a)

    def test_choiceInSequence(self):
        # see choiceInSequence.png in tests/testcases/fsms for fsm
        fsm = self.buildFSM("choiceInSequence.txt")
        q0 = fsm.getState()
        choice_a = Transition("V", "A", "B")
        choice_b = Transition("W", "B", "A")
        send = Transition("U", "B", "A")
        # in q0 there are 2 transitions: choice_a, choice_b
        self.assertEqual(2, len(q0.transitionsToStates))
        self.assertIn(choice_a, q0.transitionsToStates)
        self.assertIn(choice_b, q0.transitionsToStates)

        # make transition choice_a
        fsm.makeTransition(choice_a)
        q1_a = fsm.getState()
        # in q1_a there is one transition: send
        self.assertEqual(1, len(q1_a.transitionsToStates))
        self.assertIn(send, q1_a.transitionsToStates)

        # reset fsm
        fsm.state = q0

        # make transition choice_b
        fsm.makeTransition(choice_b)
        q1_b = fsm.getState()
        # in q1_b there is one transition: send
        self.assertEqual(1, len(q1_b.transitionsToStates))
        self.assertIn(send, q1_b.transitionsToStates)

        # q1_a and q1_b are the same state
        self.assertEqual(q1_a, q1_b)       

        # make transition send
        fsm.makeTransition(send)
        q2 = fsm.getState()
        # in q2 there is no transition
        self.assertEqual(0, len(q2.transitionsToStates))

    def test_sequenceInSequence(self):
        # see sequenceInSequence.png in tests/testcases/fsms for fsm
        fsm = self.buildFSM("sequenceInSequence.txt")
        q0 = fsm.getState()
        sequence_a = Transition("Q", "A", "B")
        sequence_b = Transition("R", "B", "A")
        send = Transition("U", "B", "A")
        # in q0 there is one transitions: sequence_a
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(sequence_a, q0.transitionsToStates)

        # make transition sequence_a
        fsm.makeTransition(sequence_a)
        q1 = fsm.getState()
        # in q1 there is one transition: sequence_b
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(sequence_b, q1.transitionsToStates)

        # make transition sequence_b
        fsm.makeTransition(sequence_b)
        q2 = fsm.getState()
        # in q2 there is one transition: send
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(send, q2.transitionsToStates)

        # make transition send
        fsm.makeTransition(send)
        q3 = fsm.getState()
        # in q3 there is no transition
        self.assertEqual(0, len(q3.transitionsToStates))

    # to do
    def test_shuffleInSequence(self):
        # see shuffleInSequence.png in tests/testcases/fsms for fsm
        fsm = self.buildFSM("shuffleInSequence.txt")
        q0 = fsm.getState()
        shuffle_a = Transition("X", "A", "B")
        shuffle_b = Transition("Y", "B", "A")
        send = Transition("U", "B", "A")
        # in q0 there are 2 transitions: shuffle_a, shuffle_b
        self.assertEqual(2, len(q0.transitionsToStates))
        self.assertIn(shuffle_a, q0.transitionsToStates)
        self.assertIn(shuffle_b, q0.transitionsToStates)

        # perform shuffle: first a then b
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        q1 = fsm.getState()
        # in q1 there is one transition: shuffle_b
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(shuffle_b, q1.transitionsToStates)
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        q3_shuffle_a_b = fsm.getState()
        # in q3_shuffle_a_b there is one transition: send
        self.assertEqual(1, len(q3_shuffle_a_b.transitionsToStates))
        self.assertIn(send, q3_shuffle_a_b.transitionsToStates)

        # reset fsm
        fsm.state = q0

        # perform shuffle: first b then a
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        q2 = fsm.getState()
        # in q2 there is one transition: shuffle_a
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(shuffle_a, q2.transitionsToStates)
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        q3_shuffle_b_a = fsm.getState()
        # in q3_shuffle_b_a there is one transition: send
        self.assertEqual(1, len(q3_shuffle_b_a.transitionsToStates))
        self.assertIn(send, q3_shuffle_b_a.transitionsToStates)

        # make transition send
        fsm.makeTransition(send)
        q4 = fsm.getState()
        # in q4 there is no transition
        self.assertEqual(0, len(q4.transitionsToStates))

    def test_choiceInChoice(self):
        # see choiceInChoice.png in tests/testcases/fsms for fsm
        fsm = self.buildFSM("choiceInChoice.txt")
        q0 = fsm.getState()
        choice_a = Transition("V", "A", "B")
        choice_b = Transition("W", "B", "A")
        send = Transition("U", "B", "A")
        # in q0 there are 3 transitions: send, choice_a and choice_b
        self.assertEqual(3, len(q0.transitionsToStates))
        self.assertIn(choice_a, q0.transitionsToStates)
        self.assertIn(choice_b, q0.transitionsToStates)
        self.assertIn(send, q0.transitionsToStates)

        # make transition choice_a
        fsm.makeTransition(choice_a)
        q1_a = fsm.getState()
        # in q1_a there is no transition
        self.assertEqual(0, len(q1_a.transitionsToStates))

        # reset fsm
        fsm.state = q0

        # make transition choice_b
        fsm.makeTransition(choice_b)
        q1_b = fsm.getState()
        # in q1_b there is no transition
        self.assertEqual(0, len(q1_b.transitionsToStates))

        # reset fsm
        fsm.state = q0

        # make transition send
        fsm.makeTransition(send)
        q1_send = fsm.getState()
        # in q1_send there is no transition
        self.assertEqual(0, len(q1_send.transitionsToStates))

        # q1_a, q1_b and q1_send are the same state
        self.assertEqual(q1_a, q1_b)
        self.assertEqual(q1_b, q1_send)

    def test_sequenceInChoice(self):
        # see sequenceInChoice.png in tests/testcases/fsms for fsm
        fsm = self.buildFSM("sequenceInChoice.txt")
        q0 = fsm.getState()
        sequence_a = Transition("Q", "A", "B")
        sequence_b = Transition("R", "B", "A")
        send = Transition("U", "B", "A")
        # in q0 there is are two transitions: sequence_a, send
        self.assertEqual(2, len(q0.transitionsToStates))
        self.assertIn(sequence_a, q0.transitionsToStates)
        self.assertIn(send, q0.transitionsToStates)

        # make transition sequence_a
        fsm.makeTransition(sequence_a)
        q1 = fsm.getState()
        # in q1 there is one transition: sequence_b
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(sequence_b, q1.transitionsToStates)

        # make transition sequence_b
        fsm.makeTransition(sequence_b)
        q2_sequence = fsm.getState()
        # in q2_sequence there is no transition
        self.assertEqual(0, len(q2_sequence.transitionsToStates))

        # reset fsm
        fsm.state = q0

        # make transition send
        fsm.makeTransition(send)
        q2_send = fsm.getState()
        # in q2_send there is no transition
        self.assertEqual(0, len(q2_send.transitionsToStates))

        # q2_sequence and q2_send are the same state
        self.assertEqual(q2_sequence, q2_send)

    def test_shuffleInChoice(self):
        # see shuffleInChoice.png in tests/testcases/fsms for fsm
        fsm = self.buildFSM("shuffleInChoice.txt")
        q0 = fsm.getState()
        shuffle_a = Transition("X", "A", "B")
        shuffle_b = Transition("Y", "B", "A")
        send = Transition("U", "B", "A")
        # in q0 there are 3 transitions: shuffle_a, shuffle_b and send
        self.assertEqual(3, len(q0.transitionsToStates))
        self.assertIn(shuffle_a, q0.transitionsToStates)
        self.assertIn(shuffle_b, q0.transitionsToStates)
        self.assertIn(send, q0.transitionsToStates)

        # perform shuffle: first shuffle_a then shuffle_b
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        q1 = fsm.getState()
        # in q1 there is one transition: shuffle_b
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(shuffle_b, q1.transitionsToStates)
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        q3_shuffle_a_b = fsm.getState()
        # in q3_shuffle_a_b there is no transition
        self.assertEqual(0, len(q3_shuffle_a_b.transitionsToStates))

        # reset fsm
        fsm.state = q0

        # perform shuffle: first shuffle_b then shuffle_a
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        q2 = fsm.getState()
        # in q2 there is one transition: shuffle_a
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(shuffle_a, q2.transitionsToStates)
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        q3_shuffle_b_a = fsm.getState()
        # in q3_shuffle_b_a there is no transition
        self.assertEqual(0, len(q3_shuffle_b_a.transitionsToStates))

        # reset fsm
        fsm.state = q0

        # make transition send
        fsm.makeTransition(send)
        q3_send = fsm.getState()
        # in q3_send there is no transition
        self.assertEqual(0, len(q3_send.transitionsToStates))

        # q3_shuffle_a_b, q3_shuffle_b_a and q3_send are the same state
        self.assertEqual(q3_shuffle_a_b, q3_shuffle_b_a)
        self.assertEqual(q3_shuffle_b_a, q3_send)

    def test_twobuyer(self):
        # see twobuyer.png in tests/testcases/fsms for fsm
        fsm = self.buildFSM("twobuyer.txt")
        q0 = fsm.getState()
        title_b1_s = Transition("str", "buyer1", "seller")
        quote_s_b1 = Transition("int", "seller", "buyer1")
        quote_s_b2 = Transition("int", "seller", "buyer2")
        contrib_b1_b2 = Transition("int", "buyer1", "buyer2")
        accept_b2_b1 = Transition("bool", "buyer2", "buyer1")
        reject_b2_s = Transition("bool", "buyer2", "seller")
        reject_b2_b1 = Transition("bool", "buyer2", "buyer1")
        quote_b2_s = Transition("int", "buyer2", "seller")
        # in q0 there is one transition: title_b1_s
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(title_b1_s, q0.transitionsToStates)

        # make transition title_b1_s
        fsm.makeTransition(title_b1_s)
        q1 = fsm.getState()
        # in q1 there are two transitions: quote_s_b1 and quote_s_b2
        self.assertEqual(2, len(q1.transitionsToStates))
        self.assertIn(quote_s_b1, q1.transitionsToStates)
        self.assertIn(quote_s_b2, q1.transitionsToStates)

        # perform shuffle: first quote_s_b1 then quote_s_b2
        # make transition quote_s_b1
        fsm.makeTransition(quote_s_b1)
        q2 = fsm.getState()
        # in q2 there is one transition: quote_s_b2
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(quote_s_b2, q2.transitionsToStates)
        # make transition quote_s_b2
        fsm.makeTransition(quote_s_b2)
        q4_b1_b2 = fsm.getState()
        # in q4_b1_b2 there is one transition: quote_s_b2
        self.assertEqual(1, len(q4_b1_b2.transitionsToStates))
        self.assertIn(contrib_b1_b2, q4_b1_b2.transitionsToStates)

        # revert fsm to state q1
        fsm.state = q1

        # perform shuffle: first quote_s_b1 then quote_s_b2
        # make transition quote_s_b2
        fsm.makeTransition(quote_s_b2)
        q3 = fsm.getState()
        # in q3 there is one transition: quote_s_b1
        self.assertEqual(1, len(q3.transitionsToStates))
        self.assertIn(quote_s_b1, q3.transitionsToStates)
        # make transition quote_s_b1
        fsm.makeTransition(quote_s_b1)
        q4_b2_b1 = fsm.getState()

        # q4_b1_b2 and q4_b2_b1 are the same state
        self.assertEqual(q4_b1_b2, q4_b2_b1)

        # make transition contrib_b1_b2
        fsm.makeTransition(contrib_b1_b2)
        q5 = fsm.getState()
        # in q5 there are three transition: reject_b2_s, reject_b2_b1, accept_b2_b1
        self.assertEqual(3, len(q5.transitionsToStates))
        self.assertIn(reject_b2_s, q5.transitionsToStates)
        self.assertIn(reject_b2_b1, q5.transitionsToStates)
        self.assertIn(accept_b2_b1, q5.transitionsToStates)

        # perform shuffle: first reject_b2_s then reject_b2_b1
        # make transition reject_b2_s
        fsm.makeTransition(reject_b2_s)
        q6 = fsm.getState()
        # in q6 there is one transition: quote_s_b1
        self.assertEqual(1, len(q6.transitionsToStates))
        self.assertIn(reject_b2_b1, q6.transitionsToStates)
        # make transition reject_b2_b1
        fsm.makeTransition(reject_b2_b1)
        q10_s_b1 = fsm.getState()
        # in q10_s_b1 there is no transition
        self.assertEqual(0, len(q10_s_b1.transitionsToStates))

        # revert fsm to state q5
        fsm.state = q5

        # perform shuffle: first reject_b2_b1 then reject_b2_s
        # make transition reject_b2_b1
        fsm.makeTransition(reject_b2_b1)
        q9 = fsm.getState()
        # in q9 there is one transition: quote_s_b1
        self.assertEqual(1, len(q9.transitionsToStates))
        self.assertIn(reject_b2_s, q9.transitionsToStates)
        # make transition reject_b2_s
        fsm.makeTransition(reject_b2_s)
        q10_b1_s = fsm.getState()
        # in q10_b1_s there is no transition
        self.assertEqual(0, len(q10_b1_s.transitionsToStates))

        # revert fsm to state q5
        fsm.state = q5

        # make transition accept_b2_b1
        fsm.makeTransition(reject_b2_b1)
        q7 = fsm.getState()
        # in q7 there is one transition: contrib_b1_b2
        self.assertEqual(1, len(q7.transitionsToStates))
        #self.assertIn(contrib_b1_b2, q7.transitionsToStates)
        
        # make transition contrib_b1_b2
        fsm.makeTransition(contrib_b1_b2)
        q8 = fsm.getState()
        # in q8 there is one transition: quote_b2_s
        self.assertEqual(1, len(q8.transitionsToStates))
        self.assertIn(quote_b2_s, q8.transitionsToStates)

        # make transition quote_b2_s
        fsm.makeTransition(quote_b2_s)
        q10_sequence = fsm.getState()
        # in q10_sequence there is no transition
        self.assertEqual(0, len(q10_sequence.transitionsToStates))

        # q10_s_b1, q10_b1_s and q10_sequence are the same state
        self.assertEqual(q10_s_b1, q10_b1_s)
        self.assertEqual(q10_b1_s, q10_sequence)
    
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
    