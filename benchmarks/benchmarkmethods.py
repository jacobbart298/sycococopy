from antlr4 import FileStream, CommonTokenStream
from antlrFiles.PythonicLexer import PythonicLexer
from antlrFiles.PythonicParser import PythonicParser
from os import path

# Paths to specifications
specification_folder = path.abspath("benchmark_specifications")
specLoopNoPredicates = "protocol_loop_no_predicates.txt"
specLoopWithPredicates = "protocol_loop_with_predicates.txt"


# Parses the given specification in the filePath to a parse tree.
def buildParseTree(filePath: str):
    input = FileStream(filePath)
    lexer = PythonicLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PythonicParser(stream)
    return parser.specification()


def writeSpecifications(shuffleCount: int, nddepth: int, ringCount: int):
    writeLoopSpecificationNoPredicates()
    writeLoopSpecificationWithPredicates()


def writeLoopSpecificationNoPredicates() -> None:
    indent = '\t'
    specification : str = ""
    # write role header and roles
    specification += f"roles:\n{indent}A\n{indent}B\n"
    # write protocol header
    specification += "\nprotocol:\n"
    # start loop
    specification += indent + "loop start:\n"
    # sequence with choice to loop or send and end
    specification += 2 * indent + "choice:\n"
    specification += 3 * indent + "sequence:\n"
    specification += 4 * indent + "send int from A to B\n"
    specification += 4 * indent + "send int from B to A\n"
    specification += 4 * indent + "repeat start\n"
    specification += 3 * indent + "send int from A to B\n"

    specification_path = path.normpath(path.join(specification_folder, specLoopNoPredicates))
    with open(specification_path, 'w') as spec:
        spec.write(specification)


def writeLoopSpecificationWithPredicates():
    indent = '\t'
    specification : str = ""
    # write role header and roles
    specification += f"roles:\n{indent}A\n{indent}B\n"
    # write protocol header
    specification += "\nprotocol:\n"
    # start loop
    specification += indent + "loop start:\n"
    # sequence with choice to loop or send and end
    specification += 2 * indent + "choice:\n"
    specification += 3 * indent + "sequence:\n"
    specification += 4 * indent + "send int(1) from A to B\n"
    specification += 4 * indent + "send int(0) from B to A\n"
    specification += 4 * indent + "repeat start\n"
    specification += 3 * indent + "send int(>-1) from A to B\n"

    specification_path = path.normpath(path.join(specification_folder, specLoopWithPredicates))
    with open(specification_path, 'w') as spec:
        spec.write(specification)