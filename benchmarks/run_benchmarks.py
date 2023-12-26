import subprocess
import json
from benchmarkmethods import writeSpecifications

benchmarkCounts = {"ringCount": 10, "shuffleCount": 2, "nddepth": 2, "loopCount": 2} 
# benchmarks = {"./loop_benchmarks/FSM_build_full_parsing/loop_no_predicates.py": "./results/loop_FULL_no_predicates.json",
#               "./loop_benchmarks/FSM_build_full_parsing/loop_with_predicates.py": "./results/loop_FULL_with_predicates.json",
#               "./loop_benchmarks/FSM_build_without_parsing/loop_no_predicates_build_without_parse.py": "./results/loop_BUILD_no_predicates.json",
#               "./loop_benchmarks/FSM_build_without_parsing/loop_with_predicates_build_without_parse.py": "./results/loop_BUILD_with_predicates.json",
#               "./loop_benchmarks/without_parsing_or_building/loop_free.py": "./results/loop_FREE.json",
#               "./loop_benchmarks/without_parsing_or_building/loop_no_predicates_no_parsing.py": "./results/loop_FREE_no_predicates.json",
#               "./loop_benchmarks/without_parsing_or_building/loop_with_predicates_no_parsing.py": "./results/loop_FREE_with_predicates.json",
#               "./non_determinism_benchmarks/FSM_build_full_parsing/tree_no_predicates.py": "./results/tree_FULL_no_predicates.json",
#               "./non_determinism_benchmarks/FSM_build_full_parsing/tree_with_predicates.py": "./results/tree_FULL_with_predicates.json",
#               "non_determinism_benchmarks/FSM_build_without_parsing/tree_no_predicates_build_without_parsing.py": "./results/tree_BUILD_no_predicates.json",
#               "non_determinism_benchmarks/FSM_build_without_parsing/tree_with_predicates_build_without_parsing.py": "./results/tree_BUILD_with_predicates.json"}
benchmarks = {"non_determinism_benchmarks/without_parsing_or_building/tree_free.py": "./results/tree_FREE.json",
              "non_determinism_benchmarks/without_parsing_or_building/tree_no_predicates_no_parsing.py": "./results/tree_FREE_no_predicates.json",
              "non_determinism_benchmarks/without_parsing_or_building/tree_with_predicates_no_parsing.py": "./results/tree_FREE_with_predicates.json"}

def writeToJson():
    with open("config.json", "w") as outfile:
        json.dump(benchmarkCounts, outfile)

def runBenchmarks():
    for i in range(3):
        writeToJson()
        writeSpecifications(benchmarkCounts["shuffleCount"], benchmarkCounts["nddepth"], benchmarkCounts["ringCount"])
        for benchmark in benchmarks:
            subprocess.run(["python3.11", benchmark, "--append", benchmarks[benchmark], "-p", "2"])
        benchmarkCounts["loopCount"] = benchmarkCounts["loopCount"] * 10
        benchmarkCounts["nddepth"] = benchmarkCounts["nddepth"] + 1

if __name__ == '__main__':
    runBenchmarks()