from src.core.monitor import Monitor
from src.core.transition import Transition
from benchmarks.benchmark_fsm_builder import BenchmarkFsmBuilder
from src.core.fsm import FSM

class BenchmarkMonitor(Monitor):
    
    def __init__(self, tree):
        self.halted: bool = False
        self.setExceptionHook()
        self.transitionHistory: list[tuple[Transition, any]] = []
        self.uncheckedReceives: dict[str, Transition] = {}
        self.fsm: FSM = BenchmarkFsmBuilder().buildFsm(tree)