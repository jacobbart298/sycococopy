from src.core.fsm import FSM
from src.core.fsmBuilder import FsmBuilder
from src.core.exceptions.rolemismatchexception import RoleMismatchException

# The BenchmarkFsmBuilder inherits from the standard FsmBuilder and is used to benchmark the building
# of an FSM and monitoring, but without the overhead of parsing

class BenchmarkFsmBuilder(FsmBuilder):

    def buildFsm(self, tree) -> tuple[FSM, set[str]]:
        self.visitSpecification(tree)
        if not self.used_roles == self.defined_roles:
            raise RoleMismatchException(self.used_roles, self.defined_roles)
        return self.fsm