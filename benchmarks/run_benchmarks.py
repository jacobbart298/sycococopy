import subprocess
import json
from benchmarkmethods import writeSpecifications

benchmarkCounts = {"ringCount": 10, "shuffleCount": 2, "nddepth": 2, "loopCount": 2} 


# for i in range(3):
#     print(f"start run {i}")
#     subprocess.run(["python3.11", "voorbeeld_programma.py"])
#     print(f"finished run {i}")

if __name__ == '__main__':
    writeSpecifications(benchmarkCounts["shuffleCount"], benchmarkCounts["nddepth"], benchmarkCounts["ringCount"])
    with open("config.json", "w") as outfile:
        json.dump(benchmarkCounts, outfile)