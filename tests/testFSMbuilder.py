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
        fsm = self.buildFSM("singleSend.txt")
        start_state = fsm.getState()
        send = Transition("X", "A", "B")
        # in start_state there is one transition: send
        self.assertEqual(1, len(start_state.transitionsToStates))
        self.assertIn(send, start_state.transitionsToStates)

        # make transition send
        fsm.makeTransition(send)
        end_state = fsm.getState()
        # in end_state there is no transition
        self.assertEqual(0, len(end_state.transitionsToStates))
    
    def test_singleChoice(self):
        fsm = self.buildFSM("singleChoice.txt")
        start_state = fsm.getState()
        send_a = Transition("X", "A", "B")
        send_b = Transition("Y", "A", "B")
        # in start_state there are two transitions: send_a and send_b
        self.assertEqual(2, len(start_state.transitionsToStates))
        self.assertIn(send_a, start_state.transitionsToStates)
        self.assertIn(send_b, start_state.transitionsToStates)

        # make transition send_a
        fsm.makeTransition(send_a)
        end_state_a = fsm.getState()
        # in end_state_a there is no transition
        self.assertEqual(0, len(end_state_a.transitionsToStates))

        # reset fsm
        fsm.state = start_state

        # make transition send_b
        fsm.makeTransition(send_b)
        end_state_b = fsm.getState()
        # in end_state_b there is no transition
        self.assertEqual(0, len(end_state_b.transitionsToStates))

        # end_state_a and end_state_b are the same state
        self.assertEqual(end_state_a, end_state_b)

    def test_singleSequence(self):
        fsm = self.buildFSM("singleSequence.txt")
        start_state = fsm.getState()
        send_1 = Transition("X", "A", "B")
        send_2 = Transition("Y", "B", "A")
        # in start_state there is one transition: send_1
        self.assertEqual(1, len(start_state.transitionsToStates))
        self.assertIn(send_1, start_state.transitionsToStates)

        # make transition send_1
        fsm.makeTransition(send_1)
        in_between_state = fsm.getState()
        # in in_between_state there is one transition: send_2
        self.assertEqual(1, len(in_between_state.transitionsToStates))
        self.assertIn(send_2, in_between_state.transitionsToStates)

        # make transition send_2
        fsm.makeTransition(send_2)
        end_state = fsm.getState()
        # in end_state there is no transition
        self.assertEqual(0, len(end_state.transitionsToStates))

    def test_singleShuffle(self):
        fsm = self.buildFSM("singleShuffle.txt")
        start_state = fsm.getState()
        send_a = Transition("X", "A", "B")
        send_b = Transition("Y", "A", "B")
        # in start_state there are two transitions: send_a and send_b
        self.assertEqual(2, len(start_state.transitionsToStates))
        self.assertIn(send_a, start_state.transitionsToStates)
        self.assertIn(send_b, start_state.transitionsToStates)

        # perform shuffle: first send_a then send_b
        # make transition send_a
        fsm.makeTransition(send_a)
        in_between_state_1 = fsm.getState()
        # in in_between_state_1 there is one transition: send_b
        self.assertEqual(1, len(in_between_state_1.transitionsToStates))
        self.assertIn(send_b, in_between_state_1.transitionsToStates)
        # make transition send_b
        fsm.makeTransition(send_b)
        end_state_1 = fsm.getState()
        # in end_state_1 there is no transition
        self.assertEqual(0, len(end_state_1.transitionsToStates))

        # reset fsm
        fsm.state = start_state

        # perform shuffle: first send_b then send_a
        # make transition send_b
        fsm.makeTransition(send_b)
        in_between_state_2 = fsm.getState()
        # in in_between_state_2 there is one transition: send_a
        self.assertEqual(1, len(in_between_state_2.transitionsToStates))
        self.assertIn(send_a, in_between_state_2.transitionsToStates)
        # make transition send_a
        fsm.makeTransition(send_a)
        end_state_2 = fsm.getState()
        # in end_state_2 there is no transition
        self.assertEqual(0, len(end_state_2.transitionsToStates))
        
        # end_state_1 and end_state_2 are the same state
        self.assertEqual(end_state_1, end_state_2)

    def test_allOperationsInChoice(self):
        # see allOperationsInChoice.png in tests/testcases/fsms for fsm
        fsm = self.buildFSM("allOperationsInChoice.txt")
        q0 = fsm.getState()
        shuffle_a = Transition("X", "A", "B")
        shuffle_b = Transition("Y", "B", "A")
        send = Transition("U", "B", "A")
        choice_a = Transition("V", "A", "B")
        choice_b = Transition("W", "B", "A")
        sequence_a = Transition("Q", "A", "B")
        sequence_b = Transition("R", "B", "A")
        # in q0 there are 6 transitions: shuffle_a, shuffle_b,
        # send, choice_a, choice_b and sequence_a
        self.assertEqual(6, len(q0.transitionsToStates))
        self.assertIn(shuffle_a, q0.transitionsToStates)
        self.assertIn(shuffle_b, q0.transitionsToStates)
        self.assertIn(send, q0.transitionsToStates)
        self.assertIn(choice_a, q0.transitionsToStates)
        self.assertIn(choice_b, q0.transitionsToStates)
        self.assertIn(sequence_a, q0.transitionsToStates)

        # perform shuffle: first a then b
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        q1 = fsm.getState()
        # in q1 there is one transition: shuffle_b
        self.assertEqual(1, len(q1.transitionsToStates))
        self.assertIn(shuffle_b, q1.transitionsToStates)
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        end_state_shuffle_a_b = fsm.getState()
        # in end_state_shuffle_a_b there is no transition
        self.assertEqual(0, len(end_state_shuffle_a_b.transitionsToStates))

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
        end_state_shuffle_b_a = fsm.getState()
        # in end_state_shuffle_b_a there is no transition
        self.assertEqual(0, len(end_state_shuffle_b_a.transitionsToStates))

        # reset fsm
        fsm.state = q0

        # make transition send
        fsm.makeTransition(send)
        end_state_send = fsm.getState()
        # in end_state there is no transition
        self.assertEqual(0, len(end_state_send.transitionsToStates))

        # reset fsm
        fsm.state = q0

        # make transition choice_a
        fsm.makeTransition(choice_a)
        end_state_choice_a = fsm.getState()
        # in end_state_choice_a there is no transition
        self.assertEqual(0, len(end_state_choice_a.transitionsToStates))

        # reset fsm
        fsm.state = q0

        # make transition choice_b
        fsm.makeTransition(choice_b)
        end_state_choice_b = fsm.getState()
        # in end_state_choice_b there is no transition
        self.assertEqual(0, len(end_state_choice_b.transitionsToStates))

        # reset fsm
        fsm.state = q0

        # make transition sequence_a
        fsm.makeTransition(sequence_a)
        q3 = fsm.getState()
        # in q3 there is one transition: sequence_b
        self.assertEqual(1, len(q3.transitionsToStates))
        self.assertIn(sequence_b, q3.transitionsToStates)

        # make transition sequence_b
        fsm.makeTransition(sequence_b)
        end_state_sequence = fsm.getState()
        # in end_state_sequence there is no transition
        self.assertEqual(0, len(end_state_sequence.transitionsToStates))

        # end_state_choice_a, end_state_choice_b, end_state_send,
        # end_state_sequence, end_state_shuffle_a_b and 
        # end_state_shuffle_b_a are all the same state
        self.assertEqual(end_state_choice_a, end_state_choice_b)
        self.assertEqual(end_state_choice_b, end_state_send)
        self.assertEqual(end_state_send, end_state_sequence)
        self.assertEqual(end_state_sequence, end_state_shuffle_a_b)
        self.assertEqual(end_state_shuffle_a_b, end_state_shuffle_b_a)

    def test_allOperationsInSequence(self):
        # see allOperationsInSequence.png in tests/testcases/fsms for fsm
        fsm = self.buildFSM("allOperationsInSequence.txt")
        q0 = fsm.getState()
        shuffle_a = Transition("X", "A", "B")
        shuffle_b = Transition("Y", "B", "A")
        send = Transition("U", "B", "A")
        choice_a = Transition("V", "A", "B")
        choice_b = Transition("W", "B", "A")
        sequence_a = Transition("Q", "A", "B")
        sequence_b = Transition("R", "B", "A")
        # in q0 there are 2 transitions: shuffle_a, shuffle_b,
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
        end_state_shuffle_a_b = fsm.getState() 
        # in end_state_shuffle_a_b there is 1 transition: send
        self.assertEqual(1, len(end_state_shuffle_a_b.transitionsToStates))
        self.assertIn(send, end_state_shuffle_a_b.transitionsToStates)

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
        end_state_shuffle_b_a = fsm.getState()
        # in end_state_shuffle_b_a there is 1 transition: send
        self.assertEqual(1, len(end_state_shuffle_b_a.transitionsToStates))
        self.assertIn(send, end_state_shuffle_b_a.transitionsToStates)

        # end_state_shuffle_a_b and end_state_shuffle_b_a are the same state
        self.assertEqual(end_state_shuffle_a_b, end_state_shuffle_b_a)
        
        # make transition send
        fsm.makeTransition(send)
        q4 = fsm.getState()
        # in q4 there are 2 transitions
        self.assertEqual(2, len(q4.transitionsToStates))
        self.assertIn(choice_a, q4.transitionsToStates)
        self.assertIn(choice_b, q4.transitionsToStates)

        # make transition choice_a
        fsm.makeTransition(choice_a)
        end_state_choice_a = fsm.getState()
        # in end_state_choice_a there is 1 transition: sequence_a
        self.assertEqual(1, len(end_state_choice_a.transitionsToStates))
        self.assertIn(sequence_a, end_state_choice_a.transitionsToStates)

        # revert fsm to q4
        fsm.state = q4

        # make transition choice_b
        fsm.makeTransition(choice_b)
        end_state_choice_b = fsm.getState()
        # in end_state_choice_b there is 1 transition: sequence_a
        self.assertEqual(1, len(end_state_choice_b.transitionsToStates))
        self.assertIn(sequence_a, end_state_choice_b.transitionsToStates)

        # end_state_choice_a and end_state_choice_b are the same state
        self.assertEqual(end_state_choice_a, end_state_choice_b)
    
        # make transition sequence_a
        fsm.makeTransition(sequence_a)
        q6 = fsm.getState()
        # in q6 there is one transition: sequence_b
        self.assertEqual(1, len(q6.transitionsToStates))
        self.assertIn(sequence_b, q6.transitionsToStates)

        # make transition sequence_b
        fsm.makeTransition(sequence_b)
        q7 = fsm.getState()
        # in q7 there is no transition
        self.assertEqual(0, len(q7.transitionsToStates))

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
        end_state_send_choice_a = fsm.getState()
        # in end_state_choice_a there is no transition
        self.assertEqual(0, len(end_state_send_choice_a.transitionsToStates))
        # revert fsm to q1
        fsm.state = q1
        # make transition choice_b
        fsm.makeTransition(choice_b)
        end_state_send_choice_b = fsm.getState()
        # in end_state_choice_b there is no transition
        self.assertEqual(0, len(end_state_send_choice_b.transitionsToStates))
        # end_state_choice_a and end_state_choice_b are the same state
        self.assertEqual(end_state_send_choice_a, end_state_send_choice_b)

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
        end_state_choice_send = fsm.getState()
        # in end_state_choice_send there is no transition
        self.assertEqual(0, len(end_state_choice_send.transitionsToStates))

        # end_state_send_choice_{a,b} and end_state_choice_send are the same state
        self.assertEqual(end_state_send_choice_a, end_state_choice_send)

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
        end_state_sequence_send = fsm.getState()
        # in end_state_sequence_send there is no transition
        self.assertEqual(0, len(end_state_sequence_send.transitionsToStates))

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
        self.assertIn(sequence_b, q2.transitionsToStates)        
        # make transition sequence_b
        fsm.makeTransition(sequence_b)
        end_state_send_sequence = fsm.getState()
        # in end_state_send_sequence there is no transition
        self.assertEqual(0, len(end_state_send_sequence.transitionsToStates))

        # end_state_sequence_send and end_state_send_sequence are the same state
        self.assertEqual(end_state_send_sequence, end_state_sequence_send)

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
        end_state_shuffle_a_b = fsm.getState() 
        # in end_state_shuffle_a_b there is 1 transition: send
        self.assertEqual(1, len(end_state_shuffle_a_b.transitionsToStates))
        self.assertIn(send, end_state_shuffle_a_b.transitionsToStates)
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
        end_state_shuffle_b_a = fsm.getState()
        # in end_state_shuffle_b_a there is 1 transition: send
        self.assertEqual(1, len(end_state_shuffle_b_a.transitionsToStates))
        self.assertIn(send, end_state_shuffle_b_a.transitionsToStates)
        # end_state_shuffle_a_b and end_state_shuffle_b_a are the same state
        self.assertEqual(end_state_shuffle_a_b, end_state_shuffle_b_a)        
        # make transition send
        fsm.makeTransition(send)
        end_state_shuffle_send = fsm.getState()
        # in end_state_shuffle_send there is no transition
        self.assertEqual(0, len(end_state_shuffle_send.transitionsToStates))

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
        # in q3 there is one transition: shuffle_a
        self.assertEqual(1, len(q5.transitionsToStates))
        self.assertIn(shuffle_a, q5.transitionsToStates)
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        end_state_send_shuffle_b_a = fsm.getState()
        # in end_state_send_shuffle_b_a there is no transition
        self.assertEqual(0, len(end_state_send_shuffle_b_a.transitionsToStates))
        # perform inner shuffle: first shuffle_a then shuffle_b
        # make transition shuffle_a
        fsm.makeTransition(shuffle_a)
        q4 = fsm.getState()
        # in q2 there is one transition: shuffle_b
        self.assertEqual(1, len(q4.transitionsToStates))
        self.assertIn(shuffle_b, q4.transitionsToStates)
        # make transition shuffle_b
        fsm.makeTransition(shuffle_b)
        end_state_send_shuffle_a_b = fsm.getState() 
        # in end_state_send_shuffle_a_b there is no transition
        self.assertEqual(0, len(end_state_send_shuffle_a_b.transitionsToStates))
        # end_state_send_shuffle_a_b and end_state_send_shuffle_b_a are the same state
        self.assertEqual(end_state_send_shuffle_a_b, end_state_send_shuffle_b_a)        

        # end_state_send_shuffle_b_a and end_state_shuffle_send are the same state
        self.assertEqual(end_state_send_shuffle_a_b, end_state_shuffle_send)

    # to do
    def test_choiceInSequence(self):
        pass

    # to do
    def test_sequenceInSequence(self):
        pass

    # to do
    def test_shuffleInSequence(self):
        pass

    # to do
    def test_choiceInChoice(self):
        pass

    # to do
    def test_sequenceInChoice(self):
        pass

    # to do
    def test_shuffleInChoice(self):
        pass

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
    