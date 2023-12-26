import subprocess
import json
from benchmarkmethods import writeLoopSpecifications, writeTreeSpecifications, writeRingSpecifications, writeStarSpecifications

benchmarkCounts = {"ringCount": 10, "shuffleCount": 2, "nddepth": 2, "loopCount": 1} 
loops =     { "loop_benchmarks/FSM_build_full_parsing/loop_no_predicates.py": "./results/loop_FULL_no_predicates.json",
              "loop_benchmarks/FSM_build_full_parsing/loop_with_predicates.py": "./results/loop_FULL_with_predicates.json",
              "loop_benchmarks/FSM_build_without_parsing/loop_no_predicates_build_without_parse.py": "./results/loop_BUILD_no_predicates.json",
              "loop_benchmarks/FSM_build_without_parsing/loop_with_predicates_build_without_parse.py": "./results/loop_BUILD_with_predicates.json",
              "loop_benchmarks/without_parsing_or_building/loop_free.py": "./results/loop_FREE.json",
              "loop_benchmarks/without_parsing_or_building/loop_no_predicates_no_parsing.py": "./results/loop_FREE_no_predicates.json",
              "loop_benchmarks/without_parsing_or_building/loop_with_predicates_no_parsing.py": "./results/loop_FREE_with_predicates.json"}

trees =     { "non_determinism_benchmarks/FSM_build_full_parsing/tree_no_predicates.py": "./results/tree_FULL_no_predicates.json",
              "non_determinism_benchmarks/FSM_build_full_parsing/tree_with_predicates.py": "./results/tree_FULL_with_predicates.json",
              "non_determinism_benchmarks/FSM_build_without_parsing/tree_no_predicates_build_without_parsing.py": "./results/tree_BUILD_no_predicates.json",
              "non_determinism_benchmarks/FSM_build_without_parsing/tree_with_predicates_build_without_parsing.py": "./results/tree_BUILD_with_predicates.json",
              "non_determinism_benchmarks/without_parsing_or_building/tree_free.py": "./results/tree_FREE.json",
              "non_determinism_benchmarks/without_parsing_or_building/tree_no_predicates_no_parsing.py": "./results/tree_FREE_no_predicates.json",
              "non_determinism_benchmarks/without_parsing_or_building/tree_with_predicates_no_parsing.py": "./results/tree_FREE_with_predicates.json"}

rings =     { "ring_benchmarks/FSM_build_full_parsing/ring_no_predicates.py": "./results/ring_FULL_no_predicates.json",
              "ring_benchmarks/FSM_build_full_parsing/ring_with_predicates.py": "./results/ring_FULL_with_predicates.json",
              "ring_benchmarks/FSM_build_without_parsing/channel_ring_no_predicates_build_without_parse.py": "./results/ring_BUILD_CHANNEL_no_predicates.json",
              "ring_benchmarks/FSM_build_without_parsing/channel_ring_with_predicates_build_without_parse.py": "./results/ring_BUILD_CHANNEL_with_predicates.json",
              "ring_benchmarks/FSM_build_without_parsing/ring_no_predicates_build_without_parse.py": "./results/ring_BUILD_no_predicates.json",
              "ring_benchmarks/FSM_build_without_parsing/ring_with_predicates_build_without_parse.py": "./results/ring_BUILD_with_predicates.json",
              "ring_benchmarks/without_parsing_or_building/channel_ring_no_predicates_no_parsing.py": "./results/ring_FREE_CHANNEL_no_predicates.json",
              "ring_benchmarks/without_parsing_or_building/channel_ring_with_predicates_no_parsing.py": "./results/ring_FREE_CHANNEL_with_predicates.json",
              "ring_benchmarks/without_parsing_or_building/ring_free.py": "./results/ring_FREE.json",
              "ring_benchmarks/without_parsing_or_building/ring_no_predicates_no_parsing.py": "./results/ring_FREE_no_predicates.json",
              "ring_benchmarks/without_parsing_or_building/ring_with_predicates_no_parsing.py": "./results/ring_FREE_with_predicates.json"}

stars =     { "shuffle_benchmarks/FSM_build_full_parsing/shuffle_no_predicates.py": "./results/shuffle_FULL_no_predicates.json",
              "shuffle_benchmarks/FSM_build_full_parsing/shuffle_with_predicates.py": "./results/shuffle_FULL_with_predicates.json",
              "shuffle_benchmarks/FSM_build_without_parsing/shuffle_no_predicates_build_without_parse.py": "./results/shuffle_BUILD_no_predicates.json",
              "shuffle_benchmarks/FSM_build_without_parsing/shuffle_with_predicates_build_without_parse.py": "./results/shuffle_BUILD_with_predicates.json",
              "shuffle_benchmarks/without_parsing_or_building/shuffle_free.py": "./results/shuffle_FREE.json",
              "shuffle_benchmarks/without_parsing_or_building/shuffle_no_predicates_no_parsing.py": "./results/shuffle_FREE_no_predicates.json",
              "shuffle_benchmarks/without_parsing_or_building/shuffle_with_predicates_no_parsing.py": "./results/shuffle_FREE_with_predicates.json"}

def writeToJson():
    with open("config.json", "w") as outfile:
        json.dump(benchmarkCounts, outfile)

def runBenchmarks():
    runLoops()
    runTrees()
    runRings()
    runStars()

def runLoops():
    writeLoopSpecifications()
    for i in range(6): # up to 1000000 loops
        writeToJson()
        for benchmark in loops:
            print(f"Starting {benchmark} with loopCount {benchmarkCounts['loopCount']}")
            subprocess.run(["python3.11", benchmark, "--append", loops[benchmark]])
        benchmarkCounts["loopCount"] = benchmarkCounts["loopCount"] * 10

def runTrees():
    for i in range(13): # up to 15 levels deep
        writeToJson()
        writeTreeSpecifications(benchmarkCounts["nddepth"])
        for benchmark in trees:
            print(f"Starting {benchmark} with depth {benchmarkCounts['nddepth']}")
            subprocess.run(["python3.11", benchmark, "--append", trees[benchmark]])
        benchmarkCounts["nddepth"] = benchmarkCounts["nddepth"] + 1

def runRings():
    for i in range(4): # up to 100000 coroutines
        writeToJson()
        writeRingSpecifications(benchmarkCounts["ringCount"])
        for benchmark in rings:
            print(f"Starting {benchmark} with ringCount {benchmarkCounts['ringCount']}")
            subprocess.run(["python3.11", benchmark, "--append", rings[benchmark]])
        benchmarkCounts["ringCount"] = benchmarkCounts["ringCount"] * 10

def runStars():
    for i in range(8): # up to 10 parallel send options 
        writeToJson()
        writeStarSpecifications(benchmarkCounts["shuffleCount"])
        for benchmark in stars:
            print(f"Starting {benchmark} with starCount {benchmarkCounts['shuffleCount']}")
            subprocess.run(["python3.11", benchmark, "--append", stars[benchmark]])
        benchmarkCounts["shuffleCount"] = benchmarkCounts["shuffleCount"] + 1

if __name__ == '__main__':
    runBenchmarks()