from src.core.monitor import Monitor
from src.core.transition import Transition
from src.core.fsmBuilder import FsmBuilder
from src.core.roleBuilder import Rolebuilder
from src.core.exceptions.rolemismatchexception import RoleMismatchException

class BenchmarkMonitor(Monitor):
    
    def __init__(self, tree):
        self.halted: bool = False
        self.setExceptionHook()
        self.transitionHistory: list[tuple[Transition, any]] = []
        self.uncheckedReceives: dict[str, Transition] = {}
        self.fsm, used_roles = FsmBuilder().visitSpecification(tree)
        defined_roles: set[str] = Rolebuilder().visitSpecification(tree)         
        if not used_roles == defined_roles:
            raise RoleMismatchException(used_roles, defined_roles)
        self.initialiseUncheckedReceives(defined_roles)