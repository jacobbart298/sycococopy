# SyCoCoCoPy 
### Synchronisation and Communication between Coroutines in Concurrent Python

Welcome to the codebase of our Bachelor thesis project at the Open University in the Netherlands. 
With this project we provide a run-time framework based on the theory of multiparty session types that can be used to verify message passing between coroutines.

## Description
The SyCoCoCoPy framework can be used as a debugging tool to verify whether the communication between coroutines in a concurrent Python program adheres to a given specification. The specification can be written in a Python-like syntax, which is described below. 

If a communication operation occurs outside of the specification, the framework will end the asyncio event loop with an IllegalTransitionException and the communication history plus the violating message will be printed to the console for further evaluation.

At this stage, the error should be corrected by revising either the implementation or the provided specification.

## Installation
Before running the program, please install the framework with the following command from the sycococopy folder:

```
py -m pip install -e .
```

This ensures that the packages are correctly recognised.

## Usage as drop-in library for asyncio
The framework requires a specification that defines the roles and the communication protocol between those roles. Create a specification (as described below) and save it as a .txt file.

The library can be used as a drop-in replacement for the asyncio library within existing Python programs. 
Instead of importing asyncio, simply import the instrumentation as asyncio. The required imports are then:
```
import src.core.instrumentation as asyncio
from src.core.monitor import Monitor
```
To ensure that the instrumentation sends all relevant communication to the run-time verification monitor proceed as follows in the Python program that needs to be checked:
* Create a monitor with a link to the specification path: `monitor = Monitor(specification_path)`
* Create queues for inter-coroutine communication: `sender_to_receiver = asyncio.Queue()`
* Link the queues that are used for inter-coroutine communication to the monitor: `asyncio.link(sender_to_receiver, sender, receiver, monitor)`
Use the queues in the program for all inter-coroutine communication and run the program. The library checks if the communication adheres to the specification and provides a warning if a communication occurs that is in violation of the protocol.

## Usage with Channels for inter-coroutine communication
The library provides an alternative and possibly more intuitive way of communication via the Channel class. 
To use the Channel class proceed as follows:
* Import the Monitor and Channel classes as well as the native asyncio library:
```
import asyncio
from src.core.instrumentation import Channel
from src.core.monitor import Monitor
```
* Create a specification (as described below) and save it as a .txt file
* Create a monitor with a link to the specification path: `monitor = Monitor(specification_path)`
* Create channels for inter-coroutine communication: `sender_to_receiver = Channel(sender, receiver, monitor)`
* Use the `send` and `receive` functions of the Channel to send and receive messages between coroutines

## Architecture
The SyCoCoCoPy library contains the following modules:
* fsm.py provides the FSM class, which represents a finite state machine. Non-determinism is handled by allowing the fsm to contain more than one state at a time
* state.py provides the State class, which links transitions from its own state to one or more next states
* transition.py provides the Transition and PredicateTransition classes, which represent a message with a given type (and value constraint for a PredicateTransition) from a sender to a receiver
* fsmBuilder.py constructs an FSM from a given specification
* instrumentation.py can be used as a drop-in replacement for the asyncio library, or as a supplier of the Channel class for communication between coroutines. The instrumentation ensures that messages between coroutines in a given program are forwarded to the monitor
* monitor.py provides the Monitor class that is used to verify that send and receive operations adhere to the protocol

## Exceptions
The following exceptions can be raised by the framework:
* An IllegalTransitionException is raised when a transition occurs in the implementation that is not allowed by the specification
* A HaltedException is raised when a transition occurs, while the operation was already halted by an IllegalTransitionException. This is required because the asyncio event loop can continue its operation briefly when a coroutine raises an IllegalTransitionException
* A RoleMismatchException is raised when there were roles defined, but never used in the specification or when a role is used in a protocol, but never defined in a specification
* A PendingMessagesException is raised when a coroutine wants to send a message, but there are still incoming messages to that coroutine. Note that this check can be disabled by specifying the checkCausality attribute for the monitor as False
* A ComparatorNotImplementedException is raised when a comparator is used with a type that does not implement it.
* An IllegalTypeException is raised when the given type cannot be found in the customs module
* An IllegalValueException is raised when the provided value cannot be parsed to the given type.
* A SubtypingException is raised when the provided object is not an instance of the specified type.

When one of the SyCoCoCoPy exceptions is raised, a dedicated message is printed to the terminal providing clues about the cause of the error. The standard Python stack trace with the exception callers is not printed for clarity.

## Specification keywords
The following keywords are used in a specification:
```
# define roles with keyword roles
roles:
    name1
    name2

# define communication protocol with keyword protocol
protocol:
    #define the protocol

#send
send type[(constraint)] from p to q # refer to section value constraints

#sequentiality
sequence:
    protocol1
    protocol2

#shuffling
shuffle:
    protocol1
    protocol2

#alternativeness
choice:
    protocol1
    protocol2

#recursion/looping
loop <identifier>:
    protocol
        sequence:
            send type[(constraint)] from sender to receiver
            repeat <identifier> # the repeat keyword MUST be the last item in a sequence
``` 

## Value constraints
A specification may provide constraints on a message value, which are checked at run-time. The constraint should be provided between brackets with a comparator and value. The framework supports the comparators !=, <, >, <=, and >=, when no comparator is provided it defaults to ==.

An example constraint for a bool: `send bool(False) from p to q`

Or for an int: `send int(>=9) from p to q`

## Use of custom types
The framework supports the use of custom types in addition to Python's primitive types. Custom types must be imported in the customs.py module which is located in the customs folder. Subtyping is fully supported: when the object provided at runtime is an instance of the required type, it is accepted.

When a constraint on a custom type is given in a specification, the associated comparison method must be implemented. Specify the:
* \_\_eq\_\_ method for == comparison
* \_\_ne\_\_ method for != comparison
* \_\_lt\_\_ method for $\lt$ comparison
* \_\_le\_\_ method for $\leq$ comparison
* \_\_gt\_\_ method for $\lt$ comparison
* \_\_ge\_\_ method for $\geq$ comparison

## Roadmap
The current product is a demonstrator to showcase the possibilities of monitoring communications between coroutines at runtime in Python. To ensure that the codebase is easily readable and concepts can be extracted without undue difficulty, we have chosen not to harden the code against wrong usage. For instance, a given specification is not checked for correct syntax (other than the regular checks provided by antlr4) or semantics like checking for more than one provided option in a sequence, shuffle or choice. 

To enable the use of this library in a production environment, the codebase will need to be hardened to provide correct error messages when the provided specification is incorrect. The following is a non-exhaustive list with known issues of the specification language that need further development:
* The `repeat` statement should only be added at the end of a compound `sequence` operator. Adding a `repeat` in a `choice` or `shuffle` operator or at an intermediate position in a `sequence` does not provide a warning, but will not work.
* The compound operators `sequence`, `choice`, and `shuffle` should have at least two children, but no warning is produced if the protocol has zero or one child for a compound operator.
* If a specification does not adhere to the syntax the parser does not stop, but tries to parse as good as possible. We recommend that an incorrect syntax should halt the parsing and provide a warning to show any errors in the specification.

### Additional branches

Initially, the framework did not support the loop and repeat operations. When we decided to add them, we felt it made sense to require that the repeat operation must be the final operation in a sequence and must be preceded by another operation, the rationale being that the preceding operation brings us back to the loop state. During the validation of the framework, we came to realise that this requirement may lead to unpleasantly verbose specifications. Dropping the requirement and allowing the repeat operation to be placed within a choice turned out to be the solution. The most intuitive way of making the required changes in the builder was to employ epsilon transitions, which actually resulted in less complex builder methods with better defined responsibilities. Branch 'refactor-loop-and-repeat' offers the refactored code.  

The framework maintains the full history of transitions and prints this history to the console as part of some of the error messages. However, the full history might become too long for effective troubleshooting and we suspect that the performance may benefit if the size of the history is limited. Branch '144-limit-number-of-messages-in-transition-history' offers a fix that limits the history to 10 messages.

## Authors and acknowledgment
This project was created by Teun Schoutens and Jacob Bart as part of their Bachelor thesis project at the Open University in The Netherlands.

## License
Copyright 2024 Open University Netherlands

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Project status
Work on the project has ceased in January 2024.