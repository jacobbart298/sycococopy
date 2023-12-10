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
    specification += writeProtocol(1, 2, level, True)
    specification += writeProtocol(1, 2, level, False)

    with open(r'.\tree_monitor_protocol.txt', 'w') as spec:
        spec.write(specification)

def writeProtocol(depth: int, indentLevel: int, maxDepth: int, value: bool) -> str:
    indent = "    "
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
        protocol += writeProtocol(depth + 1, indentLevel + 1, maxDepth, value)
        protocol += writeProtocol(depth + 1, indentLevel + 1, maxDepth, not value)
        return protocol

writeSpecification(3)