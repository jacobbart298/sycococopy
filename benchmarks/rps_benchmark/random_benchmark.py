from examples.rps_item import Item
import pyperf

def findRandomItem():
    return Item.random()

if __name__ == '__main__':
    runner = pyperf.Runner()
    runner.bench_func(f"Random", findRandomItem)