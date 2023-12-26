from antlr4 import FileStream, CommonTokenStream
from antlrFiles.PythonicLexer import PythonicLexer
from antlrFiles.PythonicParser import PythonicParser
from os import path

# Paths to specifications
specification_folder = path.abspath("benchmark_specifications")
specLoopNoPredicates = "protocol_loop_no_predicates.txt"
specLoopWithPredicates = "protocol_loop_with_predicates.txt"
specTreeNoPredicates = "protocol_tree_no_predicates.txt"
specTreeWithPredicates= "protocol_tree_with_predicates.txt"


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
    writeTreeSpecificationNoPredicates(nddepth)
    writeTreeSpecificationWithPredicates(nddepth)


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


def writeTreeSpecificationNoPredicates(level: int) -> None:
    indent = "\t"
    # write role header
    specification = "roles:\n"
    # write roles
    specification += indent + "A\n"
    specification += indent + "B\n"
    # write protocol header
    specification += "\nprotocol:\n"
    # write sequence expression
    specification += indent + "choice:\n"
    specification += writeProtocolNoPredicates(1, 2, level)
    specification += writeProtocolNoPredicates(1, 2, level)

    specification_path = path.normpath(path.join(specification_folder, specTreeNoPredicates))
    with open(specification_path, 'w') as spec:
        spec.write(specification)

def writeProtocolNoPredicates(depth: int, indentLevel: int, maxDepth: int) -> str:
    indent = "\t"
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
        protocol += writeProtocolNoPredicates(depth + 1, indentLevel + 1, maxDepth)
        protocol += writeProtocolNoPredicates(depth + 1, indentLevel + 1, maxDepth)
        return protocol
    

def writeTreeSpecificationWithPredicates(level: int) -> None:
    indent = "\t"
    # write role header
    specification = "roles:\n"
    # write roles
    specification += indent + "A\n"
    specification += indent + "B\n"
    # write protocol header
    specification += "\nprotocol:\n"
    # write sequence expression
    specification += indent + "choice:\n"
    specification += writeProtocolWithPredicates(1, 2, level, True)
    specification += writeProtocolWithPredicates(1, 2, level, False)

    specification_path = path.normpath(path.join(specification_folder, specTreeWithPredicates))
    with open(specification_path, 'w') as spec:
        spec.write(specification)

def writeProtocolWithPredicates(depth: int, indentLevel: int, maxDepth: int, value: bool) -> str:
    indent = "\t"
    if depth == maxDepth and depth % 2 == 1:
        return indentLevel*indent + f"send bool({value}) from A to B\n"
    elif depth == maxDepth and depth % 2 == 0:
        return indentLevel*indent + f"send bool({value}) from B to A\n"
    else:
        protocol = indentLevel*indent + "sequence:\n"
        indentLevel += 1
        if depth % 2 == 1:
            protocol += indentLevel*indent + f"send bool({value}) from A to B\n"
        else:
            protocol += indentLevel*indent + f"send bool({value}) from B to A\n"
        protocol += indentLevel*indent + "choice:\n"
        protocol += writeProtocolWithPredicates(depth + 1, indentLevel + 1, maxDepth, value)
        protocol += writeProtocolWithPredicates(depth + 1, indentLevel + 1, maxDepth, not value)
        return protocol