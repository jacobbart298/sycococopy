# SyCoCoCoPy 
### Synchronisation and Communication between Coroutines in Concurrent Python

Welcome to the codebase of our Bachelor thesis project at the Open University in the Netherlands. 
With this project we provide a Python framework that can be used to monitor the communication between coroutines at runtime.

## Description
The SyCoCoCoPy framework can be used as a debugging tool to verify if the communication betweeen coroutines in a concurrent Python program runs as described in a given specification. The specification can be written in a Python-like syntax, which is described below. 

If a communication occurs outside of the specification, the library will end the asyncio Event loop with an IllegalTransitionException and the executed communication messages plus the violating message will be printed for further evaluation.

At this stage, the error should be corrected by revising either the implementation, or the provided specification.

## Installation
Before running the program, please install the library with the following command:

```
py -m pip install -e .
```

This will ensure that the packages are correctly recognized.

## Usage as drop-in library for asyncio
The library requires a specification that defines the roles and describes the allowed order of communication between those roles. Create a specification (as described below) and save it as a .txt file.

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
Use the queues in the program for all inter-coroutine communication and run the program. The library will check if the communication adheres to the specification and provide an alert if a communication occurs that is not according to the protocol.

## Usage with Channels for inter-coroutine communication
The library provides an alternative and possibly more intuitive way of communication via the Channel class. 
To use the Channel class proceed as follows:
* Import the Monitor and Channel classes as well as the asyncio library:
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
* fsm.py provides the FSM class, which represents a non-deterministic finite state machine. The non-determinism is handled by allowing the fsm to contain more than one state at a given time
* state.py provides the State class, which links transitions from its own state to one or more next state(s)
* transition.py provides the Transition and PredicateTransition classes, that represent a message with a given type (and value constraint for a PredicateTransition) from a sender to a receiver
* FSMbuilder.py parses a given specification to an FSM (item 1) with a start state and creates all the possible states and transitions
* instrumentation.py can be used as a drop-in replacement for the asyncio library, or as a supplier of the Channel class for communication between coroutines. The instrumentation ensures that messages between coroutines in a given program are forwarded to the monitor so they can be checked against the protocol
* monitor.py is used to verify send and receive operations adhere to the protocol

## Exceptions
The following exceptions can be raised by the framework:
* An IllegalTransitionException is raised when a transition occurs in the implementation that is not allowed by the specification
* A HaltedException is raised when a transition occurs, while the operation was already halted by an IllegalTransitionException. This is required because the asyncio event loop can continue its operation briefly when a coroutine raises an IllegalTransitionException
* A RoleMismatchException is raised when there were roles defined, but never used in the specification or when a role is used in a protocol, but never defined in a specification
* A PendingMessagesException is raised when a coroutine wants to send a message, but there are still incoming messages to that coroutine. Note that this check can be disabled by specifying the enforceCausality attribute for the monitor as False
* A ComparatorNotImplementedException is raised when a constraint is placed on a value, but the given comparator (greater than, less than, etc.) is not implemented for the value type
* An IllegalTypeException is raised when a type in the specification is not found in either the Python builtin types or the customs module
* An IllegalValueException is raised when the constructor as given for a value constraint in the specification cannot be used to create an instance of the associated type in the specification 

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

#choice
choice:
    protocol1
    protocol2

#recursion/looping
loop <identifier>:
    protocol
        send type from sender to receiver
        repeat <identifier> # the repeat keyword MUST follow a send action
``` 

## Value constraints
A specification may provide constraints on a message value, which are checked at run-time. The constraint should be provided between brackets with a comparator and value. The framework supports the comparators !=, <, >, <=, and >=, when no comparator is provided it defaults to ==.

An example constraint for a bool: `send bool(False) from p to q`

Or for an int: `send int(>=9) from p to q`

## Use of custom types
The framework supports the use of custom types in addition to the primitive types from Python. The custom types must be imported in the customs.py module which is located in the customs folder. Inheritance is fully supported, when a subtype is provided at runtime and the specification requires the superclass, it is accepted.

When a constraint on a custom type is given in a specification, the associated comparison method must be implemented. Specify the:
* \_\_eq\_\_ method for == and != comparison
* \_\_lt\_\_ method for $\lt$ comparison
* \_\_le\_\_ method for $\leq$ comparison
* \_\_gt\_\_ method for $\lt$ comparison
* \_\_ge\_\_ method for $\geq$ comparison


## Roadmap
The current product is a demonstrator to showcase the possibilities of monitoring of communications between coroutines at runtime in Python. To ensure that the codebase is easily readable and concepts can be extracted without undue difficulty, we have chosen not to harden the code against wrong usage. E.g. a given specification is not checked for correct syntax (other than the regular checks provided by antlr4) or semantics like checking for more than one provided option in a sequence, shuffle or choice. 

To enable the use of this library in a production environment, the codebase will need to be hardened to provide correct error messages when the provided specification is incorrect. The following is a non-exhaustive list with known issues of the specification language that need further development:
* The `repeat` statement should only be added at the end of a compound `sequence` operator and must follow a `send`. Adding a `repeat` in a `choice` or `shuffle` operator or at an intermediate position in a `sequence` does not provide a warning, but will not work.
* The compound operators `sequence`, `choice`, and `shuffle` should have at least two children, but no warning is produced if the protocol has zero or one child for a compound operator.
* If a specification does not adhere to the syntax the parser does not stop, but tries to parse as good as possible. We recommend that an incorrect syntax should halt the parsing and provide a warning to show where the specification is wrong.


## Authors and acknowledgment
This project was created by Teun Schoutens and Jacob Bart as part of their Bachelor thesis project at the Open University in The Netherlands.

## License
Copyright 2024 Open University Netherlands

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Project status
The project is still being worked, expected delivery is January 2024.