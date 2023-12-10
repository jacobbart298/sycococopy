import pyperf
from benchmarks.config import level
from antlr4 import *
from antlrFiles.PythonicLexer import PythonicLexer
from antlrFiles.PythonicParser import PythonicParser
from src.core.fsmBuilder import FSMbuilder

specification_path = r".\tree_monitor_protocol.txt"

def writeSpecification(level: int) -> None:
    indent = "    "
    # write role header
    specification = "roles:\n"
    # write roles
    specification += indent + "A\n"
    specification += indent + "B\n"
    # write protocol header
    specification += "\nprotocol:\n"
    # write sequence expression
    specification += indent + "choice:\n"
    specification += writeProtocol(1, 2, level)
    specification += writeProtocol(1, 2, level)

    with open(specification_path, 'w') as spec:
        spec.write(specification)

def writeProtocol(depth: int, indentLevel: int, maxDepth: int) -> str:
    indent = "    "
    if depth == maxDepth and depth % 2 == 1:
        return indentLevel*indent + "send bool from A to B\n"
    elif depth == maxDepth and depth % 2 == 0:
        return indentLevel*indent + "send bool from B to A\n"
    else:
        protocol = indentLevel*indent + "sequence:\n"
        indentLevel += 1
        if depth % 2 == 1:
            protocol += indentLevel*indent + "send bool from A to B\n"
        else:
            protocol += indentLevel*indent + "send bool from B to A\n"
        protocol += indentLevel*indent + "choice:\n"
        protocol += writeProtocol(depth + 1, indentLevel + 1, maxDepth)
        protocol += writeProtocol(depth + 1, indentLevel + 1, maxDepth)
        return protocol

def buildParseTree():
    input = FileStream(specification_path)
    lexer = PythonicLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PythonicParser(stream)
    return parser.specification() 

writeSpecification(level)
parseTree = buildParseTree()

def runBenchmark():
    FSMbuilder().visitSpecification(parseTree)  

runner = pyperf.Runner()
runner.bench_func(f"Benchmark {level}", runBenchmark)