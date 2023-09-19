import sys
import random
import asyncio
import logging

getattr(logging, "basicConfig")(
    format="%(asctime)-15s %(message)s", level=logging.INFO)

assert sys.version_info[:3] >= (3, 5, 0), \
"This gist requires Python 3.5.0 or higher."


class Fork:
    def __init__(self):
        self.in_use = False


class ForkInquiry:
    def __init__(self, table: "Table", left_fork: Fork, right_fork: Fork):
        self._table = table
        self._left_fork = left_fork
        self._right_fork = right_fork

    async def __aenter__(self) -> (Fork, Fork):
        while True:
            if self._left_fork.in_use or self._right_fork.in_use:
                fur = self._table._loop.create_future()
                self._table._futures.append(fur)
                await fur

            else:
                break

        self._left_fork.in_use, self._right_fork.in_use = True, True

        return self._left_fork, self._right_fork

    async def __aexit__(self, *args, **kwargs):
        self._left_fork.in_use, self._right_fork.in_use = False, False
        self._table._forks_released()


class Table:
    def __init__(self):
        self._loop = asyncio.get_event_loop()
        self._forks = []
        self._philosophers = []
        self._tasks = []

        self._futures = []

    def invite_philosopher(self) -> "Philosopher":
        new_philosopher = Philosopher(self, len(self._philosophers))
        self._philosophers.append(new_philosopher)
        self._forks.append(Fork())
        self._tasks.append(
            self._loop.create_task(new_philosopher.dining_or_thinking()))
        return new_philosopher

    def ask_for_forks(self, number: int) -> ForkInquiry:
        left_fork = self._forks[number]
        try:
            right_fork = self._forks[number + 1]
            right_fork_no = number + 1

        except IndexError:
            right_fork = self._forks[0]
            right_fork_no = 0

        logging.debug("Philosopher {} asks for fork {} and {}."
        .format(number, number, right_fork_no))

        return ForkInquiry(self, left_fork, right_fork)

    def _forks_released(self):
        self._futures, futures = [], self._futures

        for fur in futures:
            if not fur.cancelled():
                fur.set_result(None)

    def start(self):
        while True:
            self.invite_philosopher()
            if len(self._philosophers) >= 5:
                break

        try:
            self._loop.run_forever()

        except KeyboardInterrupt:
            async def cancel_tasks():
                for task in self._tasks:
                    task.cancel()

            self._loop.run_until_complete(cancel_tasks())

class Philosopher:
    def __init__(self, table: Table, number: int):
        self._number = number
        self._table = table

    def _ask_for_forks(self) -> ForkInquiry:
        return self._table.ask_for_forks(self._number)

    async def dining_or_thinking(self):
        while True:
            async with self._ask_for_forks() as (left_fork, right_fork):
                logging.info(
                    "Philosopher {} starts eating.".format(self._number))

                await asyncio.sleep(random.choice(range(0, 15)) / 10)
                # Eat for a while.

                logging.info(
                    "Philosopher {} finished eating.".format(self._number))

            await asyncio.sleep(random.choice(range(0, 15)) / 10)
            # Think for a while.

if __name__ == "__main__":
    table = Table()
    table.start()