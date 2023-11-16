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
        send = Transition("U", "B", "A")
        fsm = self.buildFSM("singleSend.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there is one transition: send
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(send, q0.transitionsToStates)

        # make transition send
        fsm.makeTransition(send)
        fsm.updateStates()
        q1 = fsm.getStates()[0]
        # in q1 there is no transition
        self.assertEqual(0, len(q1.transitionsToStates))
    
    def test_singleChoice(self):
        # see singleChoice.png in tests/testcases/fsms for fsm
        choice_a = Transition("V", "A", "B")
        choice_b = Transition("W", "B", "A")
        fsm = self.buildFSM("singleChoice.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there are two transitions: choice_a and choice_b
        self.assertEqual(2, len(q0.transitionsToStates))
        self.assertIn(choice_a, q0.transitionsToStates)
        self.assertIn(choice_b, q0.transitionsToStates)

        # make transition choice_a
        fsm.makeTransition(choice_a)
        fsm.updateStates()
        q1_a = fsm.getStates()[0]
        # in q1_a there is no transition
        self.assertEqual(0, len(q1_a.transitionsToStates))

        # reset fsm
        fsm.states = {q0}

        # make transition choice_b
        fsm.makeTransition(choice_b)
        fsm.updateStates()
        q1_b = fsm.getStates()[0]
        # in q1_b there is no transition
        self.assertEqual(0, len(q1_b.transitionsToStates))

        # q1_a and q1_b are the same state
        self.assertEqual(q1_a, q1_b)

    def test_singleSequence(self):
        # see singleSequence.png in tests/testcases/fsms for fsm
        sequence_a = Transition("Q", "A", "B")
        sequence_b = Transition("R", "B", "A")
        fsm = self.buildFSM("singleSequence.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in start_state there is one transition: send_1
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(sequence_a, q0.transitionsToStates)

        # make transition sequence_a
        fsm.makeTransition(sequence_a)
        fsm.updateStates()
        q1 = fsm.getStates()[0]
        # in q1 there is one transition: sequence_b
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(sequence_b, q1.transitionsToStates)

        # make transition sequence_b
        fsm.makeTransition(sequence_b)
        fsm.updateStates()
        q2 = fsm.getStates()[0]
        # in q2 there is no transition
        self.assertEqual(0, len(q2.transitionsToStates))

    def test_singleShuffle(self):
        # see singleShuffle.png in tests/testcases/fsms for fsm
        shuffle_a = Transition("X", "A", "B")
        shuffle_b = Transition("Y", "B", "A")
        fsm = self.buildFSM("singleShuffle.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there are two transitions: shuffle_a and shuffle_b
        self.assertEqual(2, len(q0.transitionsToStates))
        self.assertIn(shuffle_a, q0.transitionsToStates)
        self.assertIn(shuffle_b, q0.transitionsToStates)

        # perform shuffle: first shuffle_a then shuffle_b
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        fsm.updateStates()
        q1 = fsm.getStates()[0]
        # in q1 there is one transition: shuffle_b
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(shuffle_b, q1.transitionsToStates)
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        fsm.updateStates()
        q3_a_b = fsm.getStates()[0]
        # in q3_a_b there is no transition
        self.assertEqual(0, len(q3_a_b.transitionsToStates))

        # reset fsm
        fsm.states = {q0}

        # perform shuffle: first shuffle_b then shuffle_a
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        fsm.updateStates()
        q2 = fsm.getStates()[0]
        # in q2 there is one transition: shuffle_a
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(shuffle_a, q2.transitionsToStates)
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        fsm.updateStates()
        q3_b_a = fsm.getStates()[0]
        # in q3_b_a there is no transition
        self.assertEqual(0, len(q3_b_a.transitionsToStates))
        
        # q3_a_b and q3_b_a are the same state
        self.assertEqual(q3_a_b, q3_b_a)

    def test_choiceInShuffle(self):
        # see choiceInShuffle.png in tests/testcases/fsms for fsm
        choice_a = Transition("V", "A", "B")
        choice_b = Transition("W", "B", "A")
        send = Transition("U", "B", "A")
        fsm = self.buildFSM("choiceInShuffle.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there are 3 transitions: choice_a, choice_b and send
        self.assertEqual(3, len(q0.transitionsToStates))
        self.assertIn(choice_a, q0.transitionsToStates)
        self.assertIn(choice_b, q0.transitionsToStates)
        self.assertIn(send, q0.transitionsToStates)

        # perform shuffle: first send then choice
        # make transition send
        fsm.makeTransition(send)
        fsm.updateStates()
        q1 = fsm.getStates()[0]
        # in q1 there are 2 transitions: 
        self.assertEqual(2, len(q1.transitionsToStates))
        self.assertIn(choice_a, q1.transitionsToStates)
        self.assertIn(choice_b, q1.transitionsToStates)
        # make transition choice_a
        fsm.makeTransition(choice_a)
        fsm.updateStates()
        q3_send_a = fsm.getStates()[0]
        # in q3_send_a there is no transition
        self.assertEqual(0, len(q3_send_a.transitionsToStates))
        # revert fsm to q1
        fsm.states = {q1}
        # make transition choice_b
        fsm.makeTransition(choice_b)
        fsm.updateStates()
        q3_send_b = fsm.getStates()[0]
        # in q3_send_b there is no transition
        self.assertEqual(0, len(q3_send_b.transitionsToStates))
        # q3_send_a and q3_send_b are the same state
        self.assertEqual(q3_send_a, q3_send_b)

        # revert fsm to q0
        fsm.states = {q0}

        # perform shuffle: first choice then send
        # make transition choice_a
        fsm.makeTransition(choice_a)
        fsm.updateStates()
        q2_a = fsm.getStates()[0]
        # in q2_a there is 1 transition: send
        self.assertEqual(1, len(q2_a.transitionsToStates))
        self.assertIn(send, q2_a.transitionsToStates)
        # revert fsm to q0
        fsm.states = {q0}
        # make transition choice_b
        fsm.makeTransition(choice_b)
        fsm.updateStates()
        q2_b = fsm.getStates()[0]
        # in q2_b there is 1 transition: send
        self.assertEqual(1, len(q2_b.transitionsToStates))
        self.assertIn(send, q2_b.transitionsToStates)
        # q2_a and q2_b are the same state
        self.assertEqual(q2_a, q2_b)
        # make transition send
        fsm.makeTransition(send)
        fsm.updateStates()
        q3_b_send = fsm.getStates()[0]
        # in q3_b_send there is no transition
        self.assertEqual(0, len(q3_b_send.transitionsToStates))

        # q3_b_send and q3_send_b are the same state
        self.assertEqual(q3_b_send, q3_send_b)

    def test_sequenceInShuffle(self):
        # see sequenceInShuffle.png in tests/testcases/fsms for fsm
        send = Transition("U", "B", "A")
        sequence_a = Transition("Q", "A", "B")
        sequence_b = Transition("R", "B", "A")
        fsm = self.buildFSM("sequenceInShuffle.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there are 2 transitions: sequence_a and send
        self.assertEqual(2, len(q0.transitionsToStates))
        self.assertIn(sequence_a, q0.transitionsToStates)
        self.assertIn(send, q0.transitionsToStates)

        # perform shuffle: first sequence then send
        # make transition sequence_a
        fsm.makeTransition(sequence_a)
        fsm.updateStates()
        q1 = fsm.getStates()[0]
        # in q1 there is one transition: sequence_b
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(sequence_b, q1.transitionsToStates)
        # make transition sequence_b
        fsm.makeTransition(sequence_b)
        fsm.updateStates()
        q3 = fsm.getStates()[0]
        # in q3 there is one transition: send
        self.assertEqual(1, len(q3.transitionsToStates))
        # make transition send
        fsm.makeTransition(send)
        fsm.updateStates()
        q5_sequence_send = fsm.getStates()[0]
        # in q5_sequence_send there is no transition
        self.assertEqual(0, len(q5_sequence_send.transitionsToStates))

        # reset fsm
        fsm.states = {q0}

        # perform shuffle: first send then sequence
        # make transition send
        fsm.makeTransition(send)
        fsm.updateStates()
        q2 = fsm.getStates()[0]
        # in q2 there is one transition: sequence_a
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(sequence_a, q2.transitionsToStates)        
        # make transition sequence_a
        fsm.makeTransition(sequence_a)
        fsm.updateStates()
        q4 = fsm.getStates()[0]
        # in q4 there is one transition: sequence_b
        self.assertEqual(1, len(q4.transitionsToStates))
        self.assertIn(sequence_b, q4.transitionsToStates)        
        # make transition sequence_b
        fsm.makeTransition(sequence_b)
        fsm.updateStates()
        q5_send_sequence = fsm.getStates()[0]
        # in q5_send_sequence there is no transition
        self.assertEqual(0, len(q5_send_sequence.transitionsToStates))

        # q5_sequence_send and q5_send_sequence are the same state
        self.assertEqual(q5_sequence_send, q5_send_sequence)

    def test_shuffleInShuffle(self):
        # see shuffleInShuffle.png in tests/testcases/fsms for fsm
        shuffle_a = Transition("X", "A", "B")
        shuffle_b = Transition("Y", "B", "A")
        send = Transition("U", "B", "A")
        fsm = self.buildFSM("shuffleInShuffle.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there are 3 transitions: shuffle_a, shuffle_b and send
        self.assertEqual(3, len(q0.transitionsToStates))
        self.assertIn(shuffle_a, q0.transitionsToStates)
        self.assertIn(shuffle_b, q0.transitionsToStates)
        self.assertIn(send, q0.transitionsToStates)

        # perform shuffle: first shuffle then send
        # perform shuffle: first shuffle_a then shuffle_b
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        fsm.updateStates()
        q2 = fsm.getStates()[0]
        # in q2 there is one transition: shuffle_b
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(shuffle_b, q2.transitionsToStates)
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        fsm.updateStates()
        q6_a_b = fsm.getStates()[0] 
        # in q6_a_b there is 1 transition: send
        self.assertEqual(1, len(q6_a_b.transitionsToStates))
        self.assertIn(send, q6_a_b.transitionsToStates)
        # reset fsm
        fsm.states = {q0}
        # perform shuffle: first shuffle_b then shuffle_a
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        fsm.updateStates()
        q3 = fsm.getStates()[0]
        # in q3 there is one transition: shuffle_a
        self.assertEqual(1, len(q3.transitionsToStates))
        self.assertIn(shuffle_a, q3.transitionsToStates)
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        fsm.updateStates()
        q6_b_a = fsm.getStates()[0]
        # in q6_b_a there is 1 transition: send
        self.assertEqual(1, len(q6_b_a.transitionsToStates))
        self.assertIn(send, q6_b_a.transitionsToStates)
        # q6_a_b and q6_b_a are the same state
        self.assertEqual(q6_a_b, q6_b_a)        
        # make transition send
        fsm.makeTransition(send)
        fsm.updateStates()
        q7_shuffle_b_a_send = fsm.getStates()[0]
        # in q7_shuffle_b_a_send there is no transition
        self.assertEqual(0, len(q7_shuffle_b_a_send.transitionsToStates))

        # reset fsm
        fsm.states = {q0}

        # perform shuffle: first send then shuffle
        # make transition send
        fsm.makeTransition(send)
        fsm.updateStates()
        q1 = fsm.getStates()[0]
        # in q1 there are two transitions: shuffle_a and shuffle_b
        self.assertEqual(2, len(q1.transitionsToStates))
        self.assertIn(shuffle_a, q1.transitionsToStates)
        self.assertIn(shuffle_b, q1.transitionsToStates)
        # perform inner shuffle: first shuffle_b then shuffle_a
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        fsm.updateStates()
        q5 = fsm.getStates()[0]
        # in q5 there is one transition: shuffle_a
        self.assertEqual(1, len(q5.transitionsToStates))
        self.assertIn(shuffle_a, q5.transitionsToStates)
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        fsm.updateStates()
        q7_send_shuffle_b_a = fsm.getStates()[0]
        # in q7_send_shuffle_b_a there is no transition
        self.assertEqual(0, len(q7_send_shuffle_b_a.transitionsToStates))
        # revert fsm to q1
        fsm.states = {q1}
        # perform inner shuffle: first shuffle_a then shuffle_b
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        fsm.updateStates()
        q4 = fsm.getStates()[0]
        # in q2 there is one transition: shuffle_b
        self.assertEqual(1, len(q4.transitionsToStates))
        self.assertIn(shuffle_b, q4.transitionsToStates)
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        fsm.updateStates()
        q7_send_shuffle_a_b = fsm.getStates()[0] 
        # in q7_send_shuffle_a_b there is no transition
        self.assertEqual(0, len(q7_send_shuffle_a_b.transitionsToStates))
        
        # q7_send_shuffle_b_a, q7_send_shuffle_a_b 
        # and q7_shuffle_b_a_send are the same state
        self.assertEqual(q7_send_shuffle_b_a, q7_send_shuffle_a_b)
        self.assertEqual(q7_shuffle_b_a_send, q7_send_shuffle_b_a)

    def test_choiceInSequence(self):
        # see choiceInSequence.png in tests/testcases/fsms for fsm
        choice_a = Transition("V", "A", "B")
        choice_b = Transition("W", "B", "A")
        send = Transition("U", "B", "A")
        fsm = self.buildFSM("choiceInSequence.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there are 2 transitions: choice_a, choice_b
        self.assertEqual(2, len(q0.transitionsToStates))
        self.assertIn(choice_a, q0.transitionsToStates)
        self.assertIn(choice_b, q0.transitionsToStates)

        # make transition choice_a
        fsm.makeTransition(choice_a)
        fsm.updateStates()
        q1_a = fsm.getStates()[0]
        # in q1_a there is one transition: send
        self.assertEqual(1, len(q1_a.transitionsToStates))
        self.assertIn(send, q1_a.transitionsToStates)

        # reset fsm
        fsm.states = {q0}

        # make transition choice_b
        fsm.makeTransition(choice_b)
        fsm.updateStates()
        q1_b = fsm.getStates()[0]
        # in q1_b there is one transition: send
        self.assertEqual(1, len(q1_b.transitionsToStates))
        self.assertIn(send, q1_b.transitionsToStates)

        # q1_a and q1_b are the same state
        self.assertEqual(q1_a, q1_b)       

        # make transition send
        fsm.makeTransition(send)
        fsm.updateStates()
        q2 = fsm.getStates()[0]
        # in q2 there is no transition
        self.assertEqual(0, len(q2.transitionsToStates))

    def test_sequenceInSequence(self):
        # see sequenceInSequence.png in tests/testcases/fsms for fsm
        sequence_a = Transition("Q", "A", "B")
        sequence_b = Transition("R", "B", "A")
        send = Transition("U", "B", "A")
        fsm = self.buildFSM("sequenceInSequence.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there is one transitions: sequence_a
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(sequence_a, q0.transitionsToStates)

        # make transition sequence_a
        fsm.makeTransition(sequence_a)
        fsm.updateStates()
        q1 = fsm.getStates()[0]
        # in q1 there is one transition: sequence_b
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(sequence_b, q1.transitionsToStates)

        # make transition sequence_b
        fsm.makeTransition(sequence_b)
        fsm.updateStates()
        q2 = fsm.getStates()[0]
        # in q2 there is one transition: send
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(send, q2.transitionsToStates)

        # make transition send
        fsm.makeTransition(send)
        fsm.updateStates()
        q3 = fsm.getStates()[0]
        # in q3 there is no transition
        self.assertEqual(0, len(q3.transitionsToStates))

    def test_shuffleInSequence(self):
        # see shuffleInSequence.png in tests/testcases/fsms for fsm
        shuffle_a = Transition("X", "A", "B")
        shuffle_b = Transition("Y", "B", "A")
        send = Transition("U", "B", "A")
        fsm = self.buildFSM("shuffleInSequence.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there are 2 transitions: shuffle_a, shuffle_b
        self.assertEqual(2, len(q0.transitionsToStates))
        self.assertIn(shuffle_a, q0.transitionsToStates)
        self.assertIn(shuffle_b, q0.transitionsToStates)

        # perform shuffle: first a then b
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        fsm.updateStates()
        q1 = fsm.getStates()[0]
        # in q1 there is one transition: shuffle_b
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(shuffle_b, q1.transitionsToStates)
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        fsm.updateStates()
        q3_shuffle_a_b = fsm.getStates()[0]
        # in q3_shuffle_a_b there is one transition: send
        self.assertEqual(1, len(q3_shuffle_a_b.transitionsToStates))
        self.assertIn(send, q3_shuffle_a_b.transitionsToStates)

        # reset fsm
        fsm.states = {q0}

        # perform shuffle: first b then a
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        fsm.updateStates()
        q2 = fsm.getStates()[0]
        # in q2 there is one transition: shuffle_a
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(shuffle_a, q2.transitionsToStates)
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        fsm.updateStates()
        q3_shuffle_b_a = fsm.getStates()[0]
        # in q3_shuffle_b_a there is one transition: send
        self.assertEqual(1, len(q3_shuffle_b_a.transitionsToStates))
        self.assertIn(send, q3_shuffle_b_a.transitionsToStates)

        # make transition send
        fsm.makeTransition(send)
        fsm.updateStates()
        q4 = fsm.getStates()[0]
        # in q4 there is no transition
        self.assertEqual(0, len(q4.transitionsToStates))

    def test_choiceInChoice(self):
        # see choiceInChoice.png in tests/testcases/fsms for fsm
        choice_a = Transition("V", "A", "B")
        choice_b = Transition("W", "B", "A")
        send = Transition("U", "B", "A")
        fsm = self.buildFSM("choiceInChoice.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there are 3 transitions: send, choice_a and choice_b
        self.assertEqual(3, len(q0.transitionsToStates))
        self.assertIn(choice_a, q0.transitionsToStates)
        self.assertIn(choice_b, q0.transitionsToStates)
        self.assertIn(send, q0.transitionsToStates)

        # make transition choice_a
        fsm.makeTransition(choice_a)
        fsm.updateStates()
        q1_a = fsm.getStates()[0]
        # in q1_a there is no transition
        self.assertEqual(0, len(q1_a.transitionsToStates))

        # reset fsm
        fsm.states = {q0}

        # make transition choice_b
        fsm.makeTransition(choice_b)
        fsm.updateStates()
        q1_b = fsm.getStates()[0]
        # in q1_b there is no transition
        self.assertEqual(0, len(q1_b.transitionsToStates))

        # reset fsm
        fsm.states = {q0}

        # make transition send
        fsm.makeTransition(send)
        fsm.updateStates()
        q1_send = fsm.getStates()[0]
        # in q1_send there is no transition
        self.assertEqual(0, len(q1_send.transitionsToStates))

        # q1_a, q1_b and q1_send are the same state
        self.assertEqual(q1_a, q1_b)
        self.assertEqual(q1_b, q1_send)

    def test_sequenceInChoice(self):
        # see sequenceInChoice.png in tests/testcases/fsms for fsm
        sequence_a = Transition("Q", "A", "B")
        sequence_b = Transition("R", "B", "A")
        send = Transition("U", "B", "A")
        fsm = self.buildFSM("sequenceInChoice.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there is are two transitions: sequence_a, send
        self.assertEqual(2, len(q0.transitionsToStates))
        self.assertIn(sequence_a, q0.transitionsToStates)
        self.assertIn(send, q0.transitionsToStates)

        # make transition sequence_a
        fsm.makeTransition(sequence_a)
        fsm.updateStates()
        q1 = fsm.getStates()[0]
        # in q1 there is one transition: sequence_b
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(sequence_b, q1.transitionsToStates)

        # make transition sequence_b
        fsm.makeTransition(sequence_b)
        fsm.updateStates()
        q2_sequence = fsm.getStates()[0]
        # in q2_sequence there is no transition
        self.assertEqual(0, len(q2_sequence.transitionsToStates))

        # reset fsm
        fsm.states = {q0}

        # make transition send
        fsm.makeTransition(send)
        fsm.updateStates()
        q2_send = fsm.getStates()[0]
        # in q2_send there is no transition
        self.assertEqual(0, len(q2_send.transitionsToStates))

        # q2_sequence and q2_send are the same state
        self.assertEqual(q2_sequence, q2_send)

    def test_shuffleInChoice(self):
        # see shuffleInChoice.png in tests/testcases/fsms for fsm
        shuffle_a = Transition("X", "A", "B")
        shuffle_b = Transition("Y", "B", "A")
        send = Transition("U", "B", "A")
        fsm = self.buildFSM("shuffleInChoice.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there are 3 transitions: shuffle_a, shuffle_b and send
        self.assertEqual(3, len(q0.transitionsToStates))
        self.assertIn(shuffle_a, q0.transitionsToStates)
        self.assertIn(shuffle_b, q0.transitionsToStates)
        self.assertIn(send, q0.transitionsToStates)

        # perform shuffle: first shuffle_a then shuffle_b
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        fsm.updateStates()
        q1 = fsm.getStates()[0]
        # in q1 there is one transition: shuffle_b
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(shuffle_b, q1.transitionsToStates)
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        fsm.updateStates()
        q3_shuffle_a_b = fsm.getStates()[0]
        # in q3_shuffle_a_b there is no transition
        self.assertEqual(0, len(q3_shuffle_a_b.transitionsToStates))

        # reset fsm
        fsm.states = {q0}

        # perform shuffle: first shuffle_b then shuffle_a
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        fsm.updateStates()
        q2 = fsm.getStates()[0]
        # in q2 there is one transition: shuffle_a
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(shuffle_a, q2.transitionsToStates)
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        fsm.updateStates()
        q3_shuffle_b_a = fsm.getStates()[0]
        # in q3_shuffle_b_a there is no transition
        self.assertEqual(0, len(q3_shuffle_b_a.transitionsToStates))

        # reset fsm
        fsm.states = {q0}

        # make transition send
        fsm.makeTransition(send)
        fsm.updateStates()
        q3_send = fsm.getStates()[0]
        # in q3_send there is no transition
        self.assertEqual(0, len(q3_send.transitionsToStates))

        # q3_shuffle_a_b, q3_shuffle_b_a and q3_send are the same state
        self.assertEqual(q3_shuffle_a_b, q3_shuffle_b_a)
        self.assertEqual(q3_shuffle_b_a, q3_send)

    def test_single_loop_deterministic(self):
        # see single_loop_deterministic.png in tests/testcases/fsms for fsm
        t1_A_B = Transition("t1", "A", "B")
        t2_B_A = Transition("t2", "B", "A")
        t3_B_A = Transition("t3", "B", "A")
        fsm = self.buildFSM("single_loop_deterministic.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there is one transition
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(t1_A_B, q0.transitionsToStates)

        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        # transition t1_A_B leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q1 = fsm.getStates()[0]
        # in q1 there are two transitions: t2_B_A, t3_B_A
        self.assertEqual(2, len(q1.transitionsToStates))
        self.assertIn(t2_B_A, q1.transitionsToStates)
        self.assertIn(t3_B_A, q1.transitionsToStates)
        
        # enter loop first time     
    
        # make transition t2_B_A
        fsm.makeTransition(t2_B_A)
        fsm.updateStates()
        # transition t2_B_A leads to one state: q0
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q0, fsm.getStates()[0])
        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()

        # enter loop second time

        # make transition t2_B_A
        fsm.makeTransition(t2_B_A)
        fsm.updateStates()
        # transition t2_B_A leads to one state: q0
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q0, fsm.getStates()[0])
        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()

        # exit loop

        # make transition t3_B_A
        fsm.makeTransition(t3_B_A)
        fsm.updateStates()
        # transition t3_B_A leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q2 = fsm.getStates()[0]
        # in q2 there is no transition
        self.assertEqual(0, len(q2.transitionsToStates))

    def test_single_loop_non_deterministic(self):
        # see single_loop_npn_deterministic.png in tests/testcases/fsms for fsm
        t1_A_B = Transition("t1", "A", "B")
        t2_B_A = Transition("t2", "B", "A")
        fsm = self.buildFSM("single_loop_non_deterministic.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there is one transition
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(t1_A_B, q0.transitionsToStates)

        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        # transition t1_A_B leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q1 = fsm.getStates()[0]
        # in q1 there is one transition
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(t2_B_A, q1.transitionsToStates)

        # make transition t2_B_A
        fsm.makeTransition(t2_B_A)
        fsm.updateStates()
        # transition t2_B_A leads to two states: q0 and q2
        self.assertEqual(2, len(fsm.getStates()))
        if fsm.getStates()[0].containsTransition(t1_A_B):
            self.assertEqual(q0, fsm.getStates()[0])
            q2 = fsm.getStates()[1]
        elif fsm.getStates()[1].containsTransition(t1_A_B):
            self.assertEqual(q0, fsm.getStates()[1])
            q2 = fsm.getStates()[0]
        else:
            self.fail("Builder fails to handle recursive non-determinism")
        # in q2 there is no transition
        self.assertEqual(0, len(q2.transitionsToStates))

        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        # transition t1_A_B leads to one state: q1
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q1, fsm.getStates()[0])        
        # make transition t2_B_A
        fsm.makeTransition(t2_B_A)
        fsm.updateStates()
        # transition t2_B_A leads to two states
        self.assertEqual(2, len(fsm.getStates()))
        if fsm.getStates()[0].containsTransition(t1_A_B):
            self.assertEqual(q0, fsm.getStates()[0])
            self.assertEqual(q2, fsm.getStates()[1])
        elif fsm.getStates()[1].containsTransition(t1_A_B):
            self.assertEqual(q0, fsm.getStates()[1])
            self.assertEqual(q2, fsm.getStates()[0])
        else:
            self.fail("Builder fails to handle recursive non-determinism")

    def test_nested_loop_deterministic(self):
        # see single_loop_deterministic.png in tests/testcases/fsms for fsm
        t0_A_B = Transition("t0", "A", "B")
        t1_A_B = Transition("t1", "A", "B")
        t2_A_B = Transition("t2", "A", "B")
        t3_B_A = Transition("t3", "B", "A")
        t4_B_A = Transition("t4", "B", "A")
        t5_B_A = Transition("t5", "B", "A")
        fsm = self.buildFSM("nested_loop_deterministic.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there is one transition: t0_A_B
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(t0_A_B, q0.transitionsToStates)

        # make transition t0_A_B
        fsm.makeTransition(t0_A_B)
        fsm.updateStates()
        # transition t0_A_B leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q1 = fsm.getStates()[0]
        # in q1 there is one transition: t1_A_B
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(t1_A_B, q1.transitionsToStates)

        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        # transition t1_A_B leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q2 = fsm.getStates()[0]
        # in q2 there is one transition: t2_A_B
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(t2_A_B, q2.transitionsToStates)

        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q3 = fsm.getStates()[0]
        # in q3 there are three transitions: t3_B_A, t4_B_A and t5_B_A
        self.assertEqual(3, len(q3.transitionsToStates))
        self.assertIn(t3_B_A, q3.transitionsToStates)
        self.assertIn(t4_B_A, q3.transitionsToStates)
        self.assertIn(t5_B_A, q3.transitionsToStates)

        # peform outer, inner, outer, inner loop

        # perform outer loop
        # make transition t4_B_A
        fsm.makeTransition(t4_B_A)
        fsm.updateStates()
        # transition t4_B_A leads to one state: q1
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q1, fsm.getStates()[0])
        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        # transition t1_A_B leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])

        # perform inner loop
        # make transition t3_B_A
        fsm.makeTransition(t3_B_A)
        fsm.updateStates()
        # transition t3_B_A leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])

        # perform outer loop again
        # make transition t4_B_A
        fsm.makeTransition(t4_B_A)
        fsm.updateStates()
        # transition t4_B_A leads to one state: q1
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q1, fsm.getStates()[0])
        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        # transition t1_A_B leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])
        
        # perform inner loop again
        # make transition t3_B_A
        fsm.makeTransition(t3_B_A)
        fsm.updateStates()
        # transition t3_B_A leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])

        # exit both loops

        # make transition t5_B_A
        fsm.makeTransition(t5_B_A)
        fsm.updateStates()
        # transition t5_B_A leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q4 = fsm.getStates()[0]
        # in q4 there is no transition
        self.assertEqual(0, len(q4.transitionsToStates))

    def test_nested_loop_non_deterministic(self):
        # see single_loop_non_deterministic.png in tests/testcases/fsms for fsm
        t0_A_B = Transition("t0", "A", "B")
        t1_A_B = Transition("t1", "A", "B")
        t2_A_B = Transition("t2", "A", "B")
        t3_B_A = Transition("t3", "B", "A")
        t4_B_A = Transition("t4", "B", "A")
        fsm = self.buildFSM("nested_loop_non_deterministic.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there is one transition: t0_A_B
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(t0_A_B, q0.transitionsToStates)

        # make transition t0_A_B
        fsm.makeTransition(t0_A_B)
        fsm.updateStates()
        # transition t0_A_B leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q1 = fsm.getStates()[0]
        # in q1 there is one transition: t1_A_B
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(t1_A_B, q1.transitionsToStates)

        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        # transition t1_A_B leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q2 = fsm.getStates()[0]
        # in q2 there is one transition: t2_A_B
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(t2_A_B, q2.transitionsToStates)

        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q3 = fsm.getStates()[0]
        # in q3 there are two transitions: t3_B_A and t4_B_A
        self.assertEqual(2, len(q3.transitionsToStates))
        self.assertIn(t3_B_A, q3.transitionsToStates)
        self.assertIn(t4_B_A, q3.transitionsToStates)

        # peform outer, inner, outer, inner loop

        # perform outer loop
        # make transition t3_B_A
        fsm.makeTransition(t3_B_A)
        fsm.updateStates()
        # transition t3_B_A leads to two states
        self.assertEqual(2, len(fsm.getStates()))
        if fsm.getStates()[0].containsTransition(t1_A_B):
            self.assertEqual(q1, fsm.getStates()[0])
            self.assertEqual(q2, fsm.getStates()[1])
        elif fsm.getStates()[1].containsTransition(t1_A_B):
            self.assertEqual(q1, fsm.getStates()[1])
            self.assertEqual(q2, fsm.getStates()[0])
        else:
            self.fail("Builder fails to handle recursive non-determinism")
        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        # transition t1_A_B leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])

        # perform inner loop
        # make transition t3_B_A
        fsm.makeTransition(t3_B_A)
        fsm.updateStates()
        # transition t3_B_A leads to two states: q1 and q2
        self.assertEqual(2, len(fsm.getStates()))
        if fsm.getStates()[0].containsTransition(t1_A_B):
            self.assertEqual(q1, fsm.getStates()[0])
            self.assertEqual(q2, fsm.getStates()[1])
        elif fsm.getStates()[1].containsTransition(t1_A_B):
            self.assertEqual(q1, fsm.getStates()[1])
            self.assertEqual(q2, fsm.getStates()[0])
        else:
            self.fail("Builder fails to handle recursive non-determinism")
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])

        # perform outer loop again
        # make transition t3_B_A
        fsm.makeTransition(t3_B_A)
        fsm.updateStates()
        # transition t3_B_A leads to two states: q1 and q2
        self.assertEqual(2, len(fsm.getStates()))
        if fsm.getStates()[0].containsTransition(t1_A_B):
            self.assertEqual(q1, fsm.getStates()[0])
            self.assertEqual(q2, fsm.getStates()[1])
        elif fsm.getStates()[1].containsTransition(t1_A_B):
            self.assertEqual(q1, fsm.getStates()[1])
            self.assertEqual(q2, fsm.getStates()[0])
        else:
            self.fail("Builder fails to handle recursive non-determinism")
        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        # transition t1_A_B leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])

        # perform inner loop
        # make transition t3_B_A
        fsm.makeTransition(t3_B_A)
        fsm.updateStates()
        # transition t3_B_A leads to two states: q1 and q2
        self.assertEqual(2, len(fsm.getStates()))
        if fsm.getStates()[0].containsTransition(t1_A_B):
            self.assertEqual(q1, fsm.getStates()[0])
            self.assertEqual(q2, fsm.getStates()[1])
        elif fsm.getStates()[1].containsTransition(t1_A_B):
            self.assertEqual(q1, fsm.getStates()[1])
            self.assertEqual(q2, fsm.getStates()[0])
        else:
            self.fail("Builder fails to handle recursive non-determinism")
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])

        # exit both loops

        # make transition t4_B_A
        fsm.makeTransition(t4_B_A)
        fsm.updateStates()
        # transition t4_B_A leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q4 = fsm.getStates()[0]
        # in q4 there is no transition
        self.assertEqual(0, len(q4.transitionsToStates))

    def test_intertwined_loops(self):
        # see intertwined_loops.png in tests/testcases/fsms for fsm
        t0_A_B = Transition("t0", "A", "B")
        t1_A_B = Transition("t1", "A", "B")
        t2_A_B = Transition("t2", "A", "B")
        t3_B_A = Transition("t3", "B", "A")
        t4_B_C = Transition("t4", "B", "C")
        t5_C_A = Transition("t5", "C", "A")
        t6_C_D = Transition("t6", "C", "D")
        fsm = self.buildFSM("intertwined_loops.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there is one transition: t0_A_B
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(t0_A_B, q0.transitionsToStates)

        # make transition t0_A_B
        fsm.makeTransition(t0_A_B)
        fsm.updateStates()
        # transition t0_A_B leads to one state: q1
        self.assertEqual(1, len(fsm.getStates()))
        q1 = fsm.getStates()[0]
        # in q1 there is one transition: t1_A_B
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(t1_A_B, q1.transitionsToStates)

        # perform first, second, first, second loops

        # loop from q1 to q1 via first loop
        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        # transition t1_A_B leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        q2 = fsm.getStates()[0]
        # in q2 there is one transition: t2_A_B
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(t2_A_B, q2.transitionsToStates)
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        q3 = fsm.getStates()[0]
        # in q3 there are two transitions: t3_B_A and t5_B_C
        self.assertEqual(2, len(q3.transitionsToStates))
        self.assertIn(t3_B_A, q3.transitionsToStates)
        self.assertIn(t4_B_C, q3.transitionsToStates)
        # make transition t3_B_A
        fsm.makeTransition(t3_B_A)
        fsm.updateStates()
        # transition t3_B_A leads to one state: q1
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q1, fsm.getStates()[0])
        
        # move to q2
        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        # transition t1_A_B leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])
        
        # loop from q2 to q2 via second loop
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])
        # make transition t5_B_C
        fsm.makeTransition(t4_B_C)
        fsm.updateStates()
        # transition t5_B_C leads to one state: q4
        self.assertEqual(1, len(fsm.getStates()))
        q4 = fsm.getStates()[0]
        # in q4 there are two transitions: t5_C_A and t6_C_D
        self.assertEqual(2, len(q3.transitionsToStates))
        self.assertIn(t5_C_A, q4.transitionsToStates)
        self.assertIn(t6_C_D, q4.transitionsToStates)
        # make transition t5_C_A
        fsm.makeTransition(t5_C_A)
        fsm.updateStates()
        # transition t5_C_A leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])

        # move to q3
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])

        # move from q3 to q3 via first loop
        # make transition t3_B_A
        fsm.makeTransition(t3_B_A)
        fsm.updateStates()
        # transition t3_B_A leads to one state: q1
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q1, fsm.getStates()[0])
        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        # transition t1_A_B leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])

        # move to q4
        # make transition t4_B_C
        fsm.makeTransition(t4_B_C)
        fsm.updateStates()
        # transition t4_B_C leads to one state: q4
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q4, fsm.getStates()[0])
                
        # loop from q4 to q4 via second loop
        # make transition t5_C_A
        fsm.makeTransition(t5_C_A)
        fsm.updateStates()
        # transition t5_C_A leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])
        # make transition t4_B_C
        fsm.makeTransition(t4_B_C)
        fsm.updateStates()
        # transition t5_B_C leads to one state: q4
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q4, fsm.getStates()[0])

        # move to state q5
        # make transition t6_C_D
        fsm.makeTransition(t6_C_D)
        fsm.updateStates()
        # transition t6_C_D leads to one state: q5
        self.assertEqual(1, len(fsm.getStates()))
        q5 = fsm.getStates()[0]
        # in q5 there is no transition
        self.assertEqual(0, len(q5.transitionsToStates))    

    def test_non_intertwined_loops(self):
        # see intertwined_loops.png in tests/testcases/fsms for fsm
        t0_A_B = Transition("t0", "A", "B")
        t1_A_B = Transition("t1", "A", "B")
        t2_B_A = Transition("t2", "B", "A")
        t3_B_C = Transition("t3", "B", "C")
        t4_B_C = Transition("t4", "B", "C")
        t5_C_D = Transition("t5", "C", "D")
        t6_D_B = Transition("t6", "D", "B")
        t7_D_E = Transition("t7", "D", "E")
        fsm = self.buildFSM("non_intertwined_loops.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there is one transition: t0_A_B
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(t0_A_B, q0.transitionsToStates)

        # make transition t0_A_B
        fsm.makeTransition(t0_A_B)
        fsm.updateStates()
        # transition t0_A_B leads to one state: q1
        self.assertEqual(1, len(fsm.getStates()))
        q1 = fsm.getStates()[0]
        # in q1 there is one transition: t1_A_B
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(t1_A_B, q1.transitionsToStates)

        # loop from q1 to q1
        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        # transition t1_A_B leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        q2 = fsm.getStates()[0]
        # in q2 there are two transitions: t2_B_A and t3_B_C
        self.assertEqual(2, len(q2.transitionsToStates))
        self.assertIn(t2_B_A, q2.transitionsToStates)
        self.assertIn(t3_B_C, q2.transitionsToStates)
        # make transition t2_B_A
        fsm.makeTransition(t2_B_A)
        fsm.updateStates()
        # transition t2_B_A leads to one state: q1
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q1, fsm.getStates()[0])

        # move to q3
        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        # transition t1_A_B leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])
        # make transition t3_B_C
        fsm.makeTransition(t3_B_C)
        fsm.updateStates()
        # transition t3_B_C leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        q3 = fsm.getStates()[0]
        # in q3 there is one transition: t4_B_C
        self.assertEqual(1, len(q3.transitionsToStates))
        self.assertIn(t4_B_C, q3.transitionsToStates)

        # loop from q3 to q3
        # make transition t4_B_C
        fsm.makeTransition(t4_B_C)
        fsm.updateStates()
        # transition t4_B_C leads to one state: q4
        self.assertEqual(1, len(fsm.getStates()))
        q4 = fsm.getStates()[0]
        # in q4 there is one transition: t5_C_D
        self.assertEqual(1, len(q4.transitionsToStates))
        self.assertIn(t5_C_D, q4.transitionsToStates)
        # make transition t5_C_D
        fsm.makeTransition(t5_C_D)
        fsm.updateStates()
        # transition t5_C_D leads to one state: q5
        self.assertEqual(1, len(fsm.getStates()))
        q5 = fsm.getStates()[0]
        # in q5 there are two transitions: t6_D_B and t7_D_E
        self.assertEqual(2, len(q5.transitionsToStates))
        self.assertIn(t6_D_B, q5.transitionsToStates)
        self.assertIn(t7_D_E, q5.transitionsToStates)
        # make transition t6_D_B
        fsm.makeTransition(t6_D_B)
        fsm.updateStates()
        # transition t6_D_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])

        # continue to state q6
        # make transition t4_B_C
        fsm.makeTransition(t4_B_C)
        fsm.updateStates()
        # transition t4_B_C leads to one state: q4
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q4, fsm.getStates()[0])
        # make transition t5_C_D
        fsm.makeTransition(t5_C_D)
        fsm.updateStates()
        # transition t5_C_D leads to one state: q5
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q5, fsm.getStates()[0])
        # make transition t7_D_E
        fsm.makeTransition(t7_D_E)
        fsm.updateStates()
        # transition t7_D_E leads to one state: q6
        self.assertEqual(1, len(fsm.getStates()))
        q6 = fsm.getStates()[0]
        # in q6 there is no transition
        self.assertEqual(0, len(q6.transitionsToStates))    

    def test_connected_loops_perpetual(self):
        # see connected_loops_perpetual.png in tests/testcases/fsms for fsm
        t0_A_B = Transition("t0", "A", "B")
        t1_B_C = Transition("t1", "B", "C")
        t2_C_B = Transition("t2", "C", "B")
        t2_B_A = Transition("t2", "B", "A")
        fsm = self.buildFSM("connected_loops_perpetual.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there is one transition: t0_A_B
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(t0_A_B, q0.transitionsToStates)

        # loop from q0 to q0 via l1        
        # make transition t0_A_B
        fsm.makeTransition(t0_A_B)
        fsm.updateStates()
        # transition t0_A_B leads to one state: q1
        self.assertEqual(1, len(fsm.getStates()))
        q1 = fsm.getStates()[0]
        # in q1 there are two transitions: t1_B_C and t2_B_A
        self.assertEqual(2, len(q1.transitionsToStates))
        self.assertIn(t1_B_C, q1.transitionsToStates)
        self.assertIn(t2_B_A, q1.transitionsToStates)
        # make transition t2_B_A
        fsm.makeTransition(t2_B_A)
        fsm.updateStates()
        # transition t2_B_A leads to one state: q0
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q0, fsm.getStates()[0])

        # move to q1
        # make transition t0_A_B
        fsm.makeTransition(t0_A_B)
        fsm.updateStates()
        # transition t0_A_B leads to one state: q1
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q1, fsm.getStates()[0])

        # loop from q1 to q1 via l2        
        # make transition t1_B_C
        fsm.makeTransition(t1_B_C)
        fsm.updateStates()
        # transition t1_A_B leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        q2 = fsm.getStates()[0]
        # in q2 there is one transition: t2_C_B
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(t2_C_B, q2.transitionsToStates)
        # make transition t2_C_B
        fsm.makeTransition(t2_C_B)
        fsm.updateStates()
        # transition t2_C_B leads to one state: q1
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q1, fsm.getStates()[0])

        # loop from q1 to q1 via l2        
        # make transition t1_B_C
        fsm.makeTransition(t1_B_C)
        fsm.updateStates()
        # transition t1_A_B leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])
        # make transition t2_C_B
        fsm.makeTransition(t2_C_B)
        fsm.updateStates()
        # transition t2_C_B leads to one state: q1
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q1, fsm.getStates()[0])

        # return to q0 via l1
        # make transition t2_B_A
        fsm.makeTransition(t2_B_A)
        fsm.updateStates()
        # transition t2_B_A leads to one state: q0
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q0, fsm.getStates()[0])

    def test_nested_loops(self):
        # see nested_loops.png in tests/testcases/fsms for fsm
        t0_A_B = Transition("t0", "A", "B")
        t1_A_B = Transition("t1", "A", "B")
        t2_A_B = Transition("t2", "A", "B")
        t3_B_A = Transition("t3", "B", "A")
        t4_B_C = Transition("t4", "B", "C")
        t5_C_A = Transition("t5", "C", "A")
        t6_C_D = Transition("t6", "C", "D")
        fsm = self.buildFSM("nested_loops.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there is one transition: t0_A_B
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(t0_A_B, q0.transitionsToStates)

        # make transition t0_A_B
        fsm.makeTransition(t0_A_B)
        fsm.updateStates()
        # transition t0_A_B leads to one state: q1
        self.assertEqual(1, len(fsm.getStates()))
        q1 = fsm.getStates()[0]
        # in q1 there is one transition: t1_A_B
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(t1_A_B, q1.transitionsToStates)

        # first time: inner then outer loop

        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        # transition t1_A_B leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        q2 = fsm.getStates()[0]
        # in q2 there is one transition: t2_A_B
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(t2_A_B, q2.transitionsToStates)

        # loop from q2 to q2 via l2
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        q3 = fsm.getStates()[0]
        # in q3 there are two transitions:
        self.assertEqual(2, len(q3.transitionsToStates))
        self.assertIn(t3_B_A, q3.transitionsToStates)
        self.assertIn(t4_B_C, q3.transitionsToStates)
        # make transition t3_B_A
        fsm.makeTransition(t3_B_A)
        fsm.updateStates()
        # transition t3_B_A leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])
        
        # loop back to q1 via q4
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])
        # make transition t4_B_C
        fsm.makeTransition(t4_B_C)
        fsm.updateStates()
        # transition t4_B_C leads to one state: q4
        self.assertEqual(1, len(fsm.getStates()))
        q4 = fsm.getStates()[0]
        # in q4 there are two transitions:
        self.assertEqual(2, len(q4.transitionsToStates))
        self.assertIn(t5_C_A, q4.transitionsToStates)
        self.assertIn(t6_C_D, q4.transitionsToStates)
        # make transition t5_C_A
        fsm.makeTransition(t5_C_A)
        fsm.updateStates()
        # transition t5_C_A leads to one state: q1
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q1, fsm.getStates()[0])

        # second time: inner then outer loop

        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        # transition t1_A_B leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])
        # loop from q2 to q2 via l2
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])
        # make transition t3_B_A
        fsm.makeTransition(t3_B_A)
        fsm.updateStates()
        # transition t3_B_A leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])        
        # loop back to q1 via q4
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])
        # make transition t4_B_C
        fsm.makeTransition(t4_B_C)
        fsm.updateStates()
        # transition t4_B_C leads to one state: q4
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q4, fsm.getStates()[0])
        # make transition t5_C_A
        fsm.makeTransition(t5_C_A)
        fsm.updateStates()
        # transition t5_C_A leads to one state: q1
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q1, fsm.getStates()[0])

        # move to q5
        # make transition t1_A_B
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        # transition t1_A_B leads to one state: q2
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])
        # make transition t2_A_B
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        # transition t2_A_B leads to one state: q3
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])
        # make transition t4_B_C
        fsm.makeTransition(t4_B_C)
        fsm.updateStates()
        # transition t4_B_C leads to one state: q4
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q4, fsm.getStates()[0])
        # make transition t6_C_D
        fsm.makeTransition(t6_C_D)
        fsm.updateStates()
        # transition t6_C_D leads to one state: q5
        self.assertEqual(1, len(fsm.getStates()))
        q5 = fsm.getStates()[0]
        # in q5 there is no transition
        self.assertEqual(0, len(q5.transitionsToStates))       

    def one_loop_multiple_repeats(self):
        # see one_loop_multiple_repeats.png in tests/testcases/fsms for fsm
        t0_A_B = Transition("t0", "A", "B")
        t1_A_B = Transition("t1", "A", "B")
        t2_B_C = Transition("t2", "B", "C")
        t3_B_A = Transition("t3", "B", "A")
        t3_C_A = Transition("t3", "C", "A")
        t4_C_D = Transition("t5", "C", "D")
        fsm = self.buildFSM("one_loop_multiple_repeats.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there is one transition: t0_A_B
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(t0_A_B, q0.transitionsToStates)
        
        # transition t0_A_B leads to q1
        fsm.makeTransition(t0_A_B)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        q1 = fsm.getStates()[0]
        # in q1 there is one transition: t1_A_B
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(t1_A_B, q1.transitionsToStates)

        # transition t1_A_B leads to q2
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        q2 = fsm.getStates()[0]
        # in q2 there are two transitions: t2_B_C and t3_B_A
        self.assertEqual(2, len(q2.transitionsToStates))
        self.assertIn(t2_B_C, q2.transitionsToStates)
        self.assertIn(t2_B_C, q2.transitionsToStates)

        # transition t3_B_A leads to q1
        fsm.makeTransition(t3_B_A)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q1, fsm.getStates()[0])

        # transition t1_A_B leads to q2
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])

        # transition t1_A_B leads to q3
        fsm.makeTransition(t2_B_C)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        q3 = fsm.getStates()[0]
        # in q3 there are two transitions: t3_C_A and t4_C_D
        self.assertEqual(2, len(q3.transitionsToStates))
        self.assertIn(t3_C_A, q3.transitionsToStates)
        self.assertIn(t4_C_D, q3.transitionsToStates)

        # transition t3_C_A leads to q1
        fsm.makeTransition(t3_C_A)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q1, fsm.getStates()[0])
        
        # transition t1_A_B leads to q2
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q2, fsm.getStates()[0])
       
        # transition t1_A_B leads to q3
        fsm.makeTransition(t2_B_C)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])

        # transition t4_C_D leads to q4
        fsm.makeTransition(t4_C_D)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        q4 = fsm.getStates()[0]
        # in q4 there are no transitions
        self.assertEqual(0, len(q4.transitionsToStates))

    def test_choice_loop_sequence(self):
        # see choice_loop_sequence.png in tests/testcases/fsms for fsm
        t1_A_B = Transition("t1", "A", "B")
        t1_A_C = Transition("t1", "A", "C")
        t2_A_C = Transition("t2", "A", "C")
        t4_C_B = Transition("t4", "C", "B")
        t3_B_D = Transition("t3", "B", "D")
        t4_C_D = Transition("t4", "C", "D")
        fsm = self.buildFSM("choice_loop_sequence.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there is one transition: t1_A_B
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(t1_A_B, q0.transitionsToStates)

        # transition t1_A_B leads to q1 and q2
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        self.assertEqual(2, len(fsm.getStates()))
        if fsm.getStates()[0].containsTransition(t1_A_C):
            q1 = fsm.getStates()[0]
            q2 = fsm.getStates()[1]
        elif fsm.getStates()[1].containsTransition(t1_A_C):
            q1 = fsm.getStates()[1]
            q2 = fsm.getStates()[0]
        else:
            self.fail("Non-determinism failure")
        # in q1 there is one transition: t1_A_C
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(t1_A_C, q1.transitionsToStates)
        # in q2 there is one transition: t2_A_C
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(t2_A_C, q2.transitionsToStates)

        # transition t1_A_C leads to q3
        fsm.makeTransition(t1_A_C)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        q3 = fsm.getStates()[0]
        # in q3 there are two transitions: t4_C_B and t3_B_D
        self.assertEqual(2, len(q3.transitionsToStates))
        self.assertIn(t4_C_B, q3.transitionsToStates)
        self.assertIn(t3_B_D, q3.transitionsToStates)

        # transition t4_C_B leads to q0
        fsm.makeTransition(t4_C_B)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q0, fsm.getStates()[0])

        # transition t1_A_B leads to q1 and q2
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        self.assertEqual(2, len(fsm.getStates()))
        if fsm.getStates()[0].containsTransition(t1_A_C):
            self.assertEqual(q1, fsm.getStates()[0])
            self.assertEqual(q2, fsm.getStates()[1])
        elif fsm.getStates()[1].containsTransition(t1_A_C):
            self.assertEqual(q1, fsm.getStates()[1])
            self.assertEqual(q2, fsm.getStates()[0])
        else:
            self.fail("Non-determinism failure")

        # transition t2_A_C leads to q3
        fsm.makeTransition(t2_A_C)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])

        # transition t3_B_D leads to q4
        fsm.makeTransition(t3_B_D)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        q4 = fsm.getStates()[0]
        # in q4 there is one transition: t4_C_D
        self.assertEqual(1, len(q4.transitionsToStates))
        self.assertIn(t4_C_D, q4.transitionsToStates)
        
        # transition t4_C_D leads to q5
        fsm.makeTransition(t4_C_D)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        q5 = fsm.getStates()[0]
        # in q5 there is no transition
        self.assertEqual(0, len(q5.transitionsToStates))

    def test_shuffle_loop_sequence(self):
        # see shuffle_loop_sequence.png in tests/testcases/fsms for fsm
        t1_A_B = Transition("t1", "A", "B")
        t2_B_A = Transition("t2", "B", "A")
        t3_B_D = Transition("t3", "B", "D")
        t4_C_D = Transition("t4", "C", "D")
        fsm = self.buildFSM("shuffle_loop_sequence.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there are two transitions: t3_B_D and t4_C_D
        self.assertEqual(2, len(q0.transitionsToStates))
        self.assertIn(t3_B_D, q0.transitionsToStates)
        self.assertIn(t4_C_D, q0.transitionsToStates)

        # transition t3_B_D leads to q1
        fsm.makeTransition(t3_B_D)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        q1 = fsm.getStates()[0]
        # in q1 there is one transition: t4_C_D
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(t4_C_D, q1.transitionsToStates)

        # transition t4_C_D leads to q3
        fsm.makeTransition(t4_C_D)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        q3 = fsm.getStates()[0]
        # in q3 there is one transition: t1_A_B
        self.assertEqual(1, len(q3.transitionsToStates))

        # transition t1_A_B leads to q0 and q4
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        self.assertEqual(2, len(fsm.getStates()))
        if fsm.getStates()[0].containsTransition(t2_B_A):
            q4 = fsm.getStates()[0]
            self.assertEqual(q0, fsm.getStates()[1])
        elif fsm.getStates()[1].containsTransition(t2_B_A):
            q4 = fsm.getStates()[1]
            self.assertEqual(q0, fsm.getStates()[0])
        else:
            self.fail("Non-determinism failure")
        # in q4 there is one transition: t2_B_A
        self.assertEqual(1, len(q4.transitionsToStates))
        self.assertIn(t2_B_A, q4.transitionsToStates)

        # transition t4_C_D leads to q2
        fsm.makeTransition(t4_C_D)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        q2 = fsm.getStates()[0]
        # in q2 there is one transition: t3_B_D
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(t3_B_D, q2.transitionsToStates)

        # transition t3_B_D leads to q3
        fsm.makeTransition(t3_B_D)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q3, fsm.getStates()[0])
        
        # transition t1_A_B leads to q0 and q4
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        self.assertEqual(2, len(fsm.getStates()))
        if fsm.getStates()[0].containsTransition(t2_B_A):
            self.assertEqual(q4, fsm.getStates()[0])
            self.assertEqual(q0, fsm.getStates()[1])
        elif fsm.getStates()[1].containsTransition(t2_B_A):
            self.assertEqual(q4, fsm.getStates()[1])
            self.assertEqual(q0, fsm.getStates()[0])
        else:
            self.fail("Non-determinism failure")

        # transition t2_B_A leads to q5
        fsm.makeTransition(t2_B_A)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        q5 = fsm.getStates()[0]
        # in q5 there is no transition
        self.assertEqual(0, len(q5.transitionsToStates))

    def test_loop_choice(self):
        # see loop_choice.png in tests/testcases/fsms for fsm
        t1_A_B = Transition("t1", "A", "B")
        t2_A_B = Transition("t2", "A", "B")
        fsm = self.buildFSM("loop_choice.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there are two transitions: t1_A_B and t2_A_B
        self.assertEqual(2, len(q0.transitionsToStates))
        self.assertIn(t1_A_B, q0.transitionsToStates)
        self.assertIn(t2_A_B, q0.transitionsToStates)

        # transition t1_A_B leads to q0
        fsm.makeTransition(t1_A_B)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q0, fsm.getStates()[0])

        # transition t2_A_B leads to q1
        fsm.makeTransition(t2_A_B)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))
        q1 = fsm.getStates()[0]
        # in q1 there is no transition
        self.assertEqual(0, len(q1.transitionsToStates))

    def test_twoBuyer(self):
        # see twoBuyer.png in tests/testcases/fsms for fsm
        str_b1_s = Transition("str", "buyer1", "seller")
        int_s_b1 = Transition("int", "seller", "buyer1")
        int_s_b2 = Transition("int", "seller", "buyer2")
        int_b1_b2 = Transition("int", "buyer1", "buyer2")
        bool_b2_b1 = Transition("bool", "buyer2", "buyer1")
        bool_b2_s = Transition("bool", "buyer2", "seller")
        int_b2_s = Transition("int", "buyer2", "seller")
        fsm = self.buildFSM("twoBuyer.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there is one transition: str_b1_s
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(str_b1_s, q0.transitionsToStates)

        # make transition str_b1_s
        fsm.makeTransition(str_b1_s)
        fsm.updateStates()
        # transition str_b1_s leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q1 = fsm.getStates()[0]
        # in q1 there are two transitions: int_s_b1 and int_s_b2
        self.assertEqual(2, len(q1.transitionsToStates))
        self.assertIn(int_s_b1, q1.transitionsToStates)
        self.assertIn(int_s_b2, q1.transitionsToStates)

        # perform shuffle: first int_s_b1 then int_s_b2
        # make transition int_s_b1
        fsm.makeTransition(int_s_b1)
        fsm.updateStates()
        # transition int_s_b1 leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q2 = fsm.getStates()[0]
        # in q2 there is one transition: int_s_b2
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(int_s_b2, q2.transitionsToStates)
        # make transition int_s_b2
        fsm.makeTransition(int_s_b2)
        fsm.updateStates()
        # transition int_s_b2 leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q4_b1_b2 = fsm.getStates()[0]
        # in q4_b1_b2 there is one transition: int_b1_b2
        self.assertEqual(1, len(q4_b1_b2.transitionsToStates))
        self.assertIn(int_b1_b2, q4_b1_b2.transitionsToStates)

        # revert fsm to state q1
        fsm.states = {q1}

        # perform shuffle: first int_s_b2 then int_s_b1
        # make transition int_s_b2
        fsm.makeTransition(int_s_b2)
        fsm.updateStates()
        # transition int_s_b2 leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q3 = fsm.getStates()[0]
        # in q3 there is one transition: int_s_b1
        self.assertEqual(1, len(q3.transitionsToStates))
        self.assertIn(int_s_b1, q3.transitionsToStates)
        # make transition int_s_b1
        fsm.makeTransition(int_s_b1)
        fsm.updateStates()
        # transition int_s_b1 leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q4_b2_b1 = fsm.getStates()[0]

        # q4_b1_b2 and q4_b2_b1 are the same state
        self.assertEqual(q4_b1_b2, q4_b2_b1)

        # make transition int_b1_b2
        fsm.makeTransition(int_b1_b2)
        fsm.updateStates()
        # transition int_b1_b2 leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q5 = fsm.getStates()[0]
        # in q5 there are two transitions: bool_b2_b1 and bool_b2_s
        self.assertEqual(2, len(q5.transitionsToStates))
        self.assertIn(bool_b2_s, q5.transitionsToStates)
        self.assertIn(bool_b2_b1, q5.transitionsToStates)

        # perform shuffle: first bool_b2_s then bool_b2_b1
        # make transition bool_b2_s
        fsm.makeTransition(bool_b2_s)
        fsm.updateStates()
        # transition bool_b2_s leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q6 = fsm.getStates()[0]
        # in q6 there is one transition: bool_b2_b1
        self.assertEqual(1, len(q6.transitionsToStates))
        self.assertIn(bool_b2_b1, q6.transitionsToStates)
        # make transition bool_b2_b1
        fsm.makeTransition(bool_b2_b1)
        fsm.updateStates()
        # transition bool_b2_b1 leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q10_s_b1 = fsm.getStates()[0]
        # in q10_s_b1 there is no transition
        self.assertEqual(0, len(q10_s_b1.transitionsToStates))

        # revert fsm to state q5
        fsm.states = {q5}

        # perform shuffle: first bool_b2_b1 then bool_b2_s
        # make transition bool_b2_b1
        fsm.makeTransition(bool_b2_b1)
        fsm.updateStates()
        # transition bool_b2_b1 leads to two states
        self.assertEqual(2, len(fsm.getStates()))
        if fsm.getStates()[0].containsTransition(bool_b2_s):
            q9 = fsm.getStates()[0]
            q7 = fsm.getStates()[1]
        elif fsm.getStates()[1].containsTransition(bool_b2_s):
            q9 = fsm.getStates()[1]
            q7 = fsm.getStates()[0]
        else:
            self.fail("Builder fails to handle non-determinism")
        # in q9 there is one transition: bool_b2_s
        self.assertEqual(1, len(q9.transitionsToStates))
        self.assertIn(bool_b2_s, q9.transitionsToStates)
        # in q7 there is one transition: int_b1_b2
        self.assertEqual(1, len(q7.transitionsToStates))
        self.assertIn(int_b1_b2, q7.transitionsToStates)
        # make transition bool_b2_s
        fsm.makeTransition(bool_b2_s)
        fsm.updateStates()
        # transition bool_b2_s leads to one state
        self.assertEqual(1, len(fsm.getStates()))        
        q10_b1_s = fsm.getStates()[0]
        # in q10_b1_s there is no transition
        self.assertEqual(0, len(q10_b1_s.transitionsToStates))

        # revert fsm to state q5
        fsm.states = {q5}

        # make transition bool_b2_b1
        fsm.makeTransition(bool_b2_b1)
        fsm.updateStates()
        # make transition int_b1_b2
        fsm.makeTransition(int_b1_b2)
        fsm.updateStates()
        # transition int_b1_b2 leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q8 = fsm.getStates()[0]
        # in q8 there is one transition: int_b2_s
        self.assertEqual(1, len(q8.transitionsToStates))
        self.assertIn(int_b2_s, q8.transitionsToStates)

        # make transition int_b2_s
        fsm.makeTransition(int_b2_s)
        fsm.updateStates()
        # transition int_b1_b2 leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q10_sequence = fsm.getStates()[0]
        # in q10_sequence there is no transition
        self.assertEqual(0, len(q10_sequence.transitionsToStates))

        # q10_s_b1, q10_b1_s and q10_sequence are the same state
        self.assertEqual(q10_s_b1, q10_b1_s)
        self.assertEqual(q10_b1_s, q10_sequence)

    def test_travelAgency(self):
        # see travelAgency.png in tests/testcases/fsms for fsm
        str_C_A = Transition("str", "customer", "agency")
        int_A_C = Transition("int", "agency", "customer")
        str_A_S = Transition("str", "agency", "service")
        bool_C_A = Transition("bool", "customer", "agency")
        bool_A_S = Transition("bool", "agency", "service")
        str_C_S = Transition("str", "customer", "service")
        str_S_C = Transition("str", "service", "customer")
        fsm = self.buildFSM("travelAgency.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there is one transition: str_C_A
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(str_C_A, q0.transitionsToStates)

        # make transition str_C_A
        fsm.makeTransition(str_C_A)
        fsm.updateStates()
        # transition str_C_A leads to a single state
        self.assertEqual(1, len(fsm.getStates()))
        q1 = fsm.getStates()[0]
        # in q1 there is one transition: int_A_C
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(int_A_C, q1.transitionsToStates)

        # make transition int_A_C
        fsm.makeTransition(int_A_C)
        fsm.updateStates()
        # transition int_A_C leads to a single state
        self.assertEqual(1, len(fsm.getStates()))
        q2 = fsm.getStates()[0]
        # in q2 there is one transition: str_A_S
        self.assertEqual(1, len(q2.transitionsToStates))
        self.assertIn(str_A_S, q2.transitionsToStates)

        # make transition str_A_S
        fsm.makeTransition(str_A_S)
        fsm.updateStates()
        # transition str_A_S leads to two states
        self.assertEqual(2, len(fsm.getStates()))
        if fsm.getStates()[0].containsTransition(str_C_A):
            self.assertEqual(q0, fsm.getStates()[0])
            q3 = fsm.getStates()[1]
        elif fsm.getStates()[1].containsTransition(str_C_A):
            self.assertEqual(q0, fsm.getStates()[1])
            q3 = fsm.getStates()[0]
        else:
            self.fail("Builder fails to handle recursion")
        # in q3 there is one transition: bool_C_A
        self.assertEqual(1, len(q3.transitionsToStates))
        self.assertIn(bool_C_A, q3.transitionsToStates)

        # loop once

        # make transition str_C_A
        fsm.makeTransition(str_C_A)
        fsm.updateStates()
        # transition str_C_A leads to state q1
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(fsm.getStates()[0], q1)
        # make transition int_A_C
        fsm.makeTransition(int_A_C)
        fsm.updateStates()
        # transition int_A_C leads to q2
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(fsm.getStates()[0], q2)
        # make transition str_A_S
        fsm.makeTransition(str_A_S)
        fsm.updateStates()
        # transition str_A_S leads to two states
        self.assertEqual(2, len(fsm.getStates()))
        if fsm.getStates()[0].containsTransition(str_C_A):
            self.assertEqual(q0, fsm.getStates()[0])
            self.assertEqual(q3, fsm.getStates()[1])
        elif fsm.getStates()[1].containsTransition(str_C_A):
            self.assertEqual(q0, fsm.getStates()[1])
            self.assertEqual(q3, fsm.getStates()[0])
        else:
            self.fail("Loop fails to return to correct state")

        # break out of the loop

        # make transition bool_C_A
        fsm.makeTransition(bool_C_A)
        fsm.updateStates()
        # transition bool_C_A leads to two states
        self.assertEqual(2, len(fsm.getStates()))
        if fsm.getStates()[0].containsTransition(str_C_S):
            q5 = fsm.getStates()[0]
            q4 = fsm.getStates()[1]
        elif fsm.getStates()[1].containsTransition(str_C_S):
            q5 = fsm.getStates()[1]
            q4 = fsm.getStates()[0]
        else:
            self.fail("Builder fails to handle non-determinism")
        # in q4 there is one transition: bool_A_S
        self.assertEqual(1, len(q4.transitionsToStates))
        self.assertIn(bool_A_S, q4.transitionsToStates)
        # in q5 there are two transitions: bool_A_S and str_C_S
        self.assertEqual(2, len(q5.transitionsToStates))
        self.assertIn(bool_A_S, q5.transitionsToStates)
        self.assertIn(str_C_S, q5.transitionsToStates)

        # make transition bool_A_S
        fsm.makeTransition(bool_A_S)
        fsm.updateStates()
        # transition bool_A_S leads to two states
        self.assertEqual(2, len(fsm.getStates()))
        if fsm.getStates()[0].containsTransition(str_C_S):
            q6 = fsm.getStates()[0]
            q9 = fsm.getStates()[1]
        elif fsm.getStates()[1].containsTransition(str_C_S):
            q6 = fsm.getStates()[1]
            q9 = fsm.getStates()[0]
        else:
            self.fail("Builder fails to handle non-determinism")
        # in q6 there is one transition: str_C_S
        self.assertEqual(1, len(q6.transitionsToStates))
        self.assertIn(str_C_S, q6.transitionsToStates)

        # make transition str_C_S
        fsm.makeTransition(str_C_S)
        fsm.updateStates()
        # transition str_C_S leads to one state
        self.assertEqual(1, len(fsm.getStates()))
        q8 = fsm.getStates()[0]
        # in q8 there is one transition: str_S_C
        self.assertEqual(1, len(q8.transitionsToStates))
        self.assertIn(str_S_C, q8.transitionsToStates)

        # reset fsm
        fsm.states = {q0}
        # make transition str_C_A
        fsm.makeTransition(str_C_A)
        fsm.updateStates()
        # make transition int_A_C
        fsm.makeTransition(int_A_C)
        fsm.updateStates()
        # make transition str_A_S
        fsm.makeTransition(str_A_S)
        fsm.updateStates()
        # make transition bool_C_A
        fsm.makeTransition(bool_C_A)
        fsm.updateStates()

        # make transition str_C_S
        fsm.makeTransition(str_C_S)
        fsm.updateStates()
        # transition str_C_S leads to a single state
        self.assertEqual(1, len(fsm.getStates()))
        q7 = fsm.getStates()[0]
        # in q7 there is one transition: bool_A_S
        self.assertEqual(1, len(q7.transitionsToStates))
        self.assertIn(bool_A_S, q7.transitionsToStates)

        # make transition bool_A_S
        fsm.makeTransition(bool_A_S)
        fsm.updateStates()
        # transition bool_A_S leads to a single state
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q8, fsm.getStates()[0])

        # make transition str_S_C
        fsm.makeTransition(str_S_C)
        fsm.updateStates()
        # transition str_S_C leads to one state: q9
        self.assertEqual(1, len(fsm.getStates()))
        self.assertEqual(q9, fsm.getStates()[0])
        # in q9 there is no transition
        self.assertEqual(0, len(q9.transitionsToStates))
    
    def test_non_deterministic_equivalent_choices(self):
        # see non_deterministic_equivalent_choices.png in tests/testcases/fsms for fsm
        t1_A_B = Transition("t1", "A", "B")
        t2_A_C = Transition("t2", "A", "C")   
        fsm = self.buildFSM("non_deterministic_equivalent_choices.txt")
        self.assertEqual(1, len(fsm.getStates()))
        q0 = fsm.getStates()[0]
        # in q0 there is one transition: t1_A_B
        self.assertEqual(1, len(q0.transitionsToStates))
        self.assertIn(t1_A_B, q0.transitionsToStates)

        # fsm contains two states after t1_A_B
        fsm.makeTransition(t1_A_B)        
        fsm.updateStates()
        self.assertEqual(2, len(fsm.getStates()))
        # fsm contains one state after t2_A_C
        fsm.makeTransition(t2_A_C)
        fsm.updateStates()
        self.assertEqual(1, len(fsm.getStates()))

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
    