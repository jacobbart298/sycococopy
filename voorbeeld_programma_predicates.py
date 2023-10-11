import src.core.instrumentation as asyncio
from src.core.monitor import Monitor

A = 'A'
B = 'B'
C = 'C'

specification_path = r".\protocol_voorbeeld_programma_predicates.txt"
monitor = Monitor(specification_path)

async def A:

async def B:

async def C:

async def main():
    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(A())
        task_group.create_task(B())
        task_group.create_task(C())

asyncio.run(main())