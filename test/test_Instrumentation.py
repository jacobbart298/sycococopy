import unittest
import os
import src.core.instrumentation as asyncio
from src.core.monitor import Monitor
from src.core.exceptions.illegaltransitionexception import IllegalTransitionException

class TestInstrumentation(unittest.IsolatedAsyncioTestCase):

      
    async def asyncSetUp(self): 
        asyncio.linked_queues.clear()


    def testLink(self):

        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        # queue that will be linked
        queue1 = asyncio.Queue()
        # queue that will not be linked
        queue2 = asyncio.Queue()

        # linked_queues is empty
        self.assertEqual(0, len(asyncio.linked_queues))
        # link queue1
        asyncio.link(queue1, "A", "B", monitor)        
        # linked_queues contains queue1 but not queue2
        self.assertEqual(1, len(asyncio.linked_queues))
        self.assertIn(queue1, asyncio.linked_queues)
        self.assertNotIn(queue2, asyncio.linked_queues)
        
        # queue1 has attributes monitor, sender, receiver
        self.assertTrue(hasattr(queue1, 'monitor'))                
        self.assertTrue(hasattr(queue1, 'sender'))
        self.assertTrue(hasattr(queue1, 'receiver'))

        # queue2 does not have attributes monitor, sender, receiver
        self.assertFalse(hasattr(queue2, 'monitor'))                
        self.assertFalse(hasattr(queue2, 'sender'))
        self.assertFalse(hasattr(queue2, 'receiver'))


    async def testPutOnUnlinkedQueue(self):
        specificationPath = getSpecificationPath("test_monitor")
        Monitor(specificationPath)

        queue_A_to_B = asyncio.Queue()
        # A sending True to B would throw an IllegalTransitionException
        # if the queue were monitored. This is not the case.
        await queue_A_to_B.put(True)

    
    async def testGetOnUnlinkedQueue(self):
        specificationPath = getSpecificationPath("test_monitor")
        Monitor(specificationPath)

        queue_A_to_B = asyncio.Queue()
        # A sending True to B would throw an IllegalTransitionException
        # if the queue were monitored. This is not the case.
        await queue_A_to_B.put(True)
        # Because the monitor would now be halted, the get method would
        # return None instead of the first item. This is not the case.
        item = await queue_A_to_B.get()
        self.assertTrue(item)


    async def testLegalPutOnLinkedQueue(self):

        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        queue_A_to_B = asyncio.Queue()
        asyncio.link(queue_A_to_B, "A", "B", monitor)

        await queue_A_to_B.put("hello world")


    async def testIllegalPutOnLinkedQueue(self):
        
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        queue_A_to_B = asyncio.Queue()
        asyncio.link(queue_A_to_B, "A", "B", monitor)

        with self.assertRaises(IllegalTransitionException):
            await queue_A_to_B.put(True)


    async def testLegalGetOnLinkedQueue(self):

        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        queue_A_to_B = asyncio.Queue()
        asyncio.link(queue_A_to_B, "A", "B", monitor)

        message = "hello world"

        await queue_A_to_B.put(message)
        item = await queue_A_to_B.get()
        self.assertEqual(item, message)


    async def testIllegalGetOnLinkedQueue(self):

        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        queue_A_to_B = asyncio.Queue()
        # put an item on the queue before linking
        queue_A_to_B.put_nowait(True)
        asyncio.link(queue_A_to_B, "A", "B", monitor)

        with self.assertRaises(IllegalTransitionException):
            self.assertIsNone(await queue_A_to_B.get())


    async def testLegalSendOnChannel(self):
        
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        channel_A_to_B = asyncio.Channel("A", "B", monitor)

        await channel_A_to_B.send("hello world")


    async def testIllegalSendOnChannel(self):

        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        channel_A_to_B = asyncio.Channel("A", "B", monitor)

        with self.assertRaises(IllegalTransitionException):
            await channel_A_to_B.send(1.5)
    

    async def testLegalReceiveOnChannel(self):

        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        message = "hello world"

        channel_A_to_B = asyncio.Channel("A", "B", monitor)

        await channel_A_to_B.send(message)
        item = await channel_A_to_B.receive()
        self.assertEqual(item, message)


    async def testIllegalReceiveOnChannel(self):
        
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        channel_A_to_B = asyncio.Channel("A", "B", monitor)
        # put an item on the channel via its queue (no monitoring)
        channel_A_to_B.queue.put_nowait(True)

        with self.assertRaises(IllegalTransitionException):
            self.assertIsNone(await channel_A_to_B.receive())            


    def testRecognitionRandomAsyncioObject(self):
        asyncio.Lock()


    async def testPutOnLinkedQueueHalted(self):

        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        queue_A_to_B = asyncio.Queue()
        asyncio.link(queue_A_to_B, "A", "B", monitor)

        with self.assertRaises(IllegalTransitionException):
            await queue_A_to_B.put(True)
        await queue_A_to_B.put("hello world")


    async def testGetOnLinkedQueueHalted(self):
        
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        queue_A_to_B = asyncio.Queue()
        asyncio.link(queue_A_to_B, "A", "B", monitor)

        await queue_A_to_B.put("hello world")
        with self.assertRaises(IllegalTransitionException):
            await queue_A_to_B.put(True)
        self.assertIsNone(await queue_A_to_B.get())


    async def testSendOnChannelHalted(self):

        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        channel_A_to_B = asyncio.Channel("A", "B", monitor)

        with self.assertRaises(IllegalTransitionException):
            await channel_A_to_B.send(True)
        await channel_A_to_B.send("hello world")


    async def testReceiveOnChannelHalted(self):

        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)

        channel_A_to_B = asyncio.Channel("A", "B", monitor)

        await channel_A_to_B.send("hello world")
        with self.assertRaises(IllegalTransitionException):
            await channel_A_to_B.send(True)
        self.assertIsNone(await channel_A_to_B.receive())


    async def testChannelEmpty(self):

        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)
        
        channel_A_to_B = asyncio.Channel("A", "B", monitor)

        self.assertTrue(channel_A_to_B.empty())
        await channel_A_to_B.send("hello world")
        self.assertFalse(channel_A_to_B.empty())
        await channel_A_to_B.receive()
        self.assertTrue(channel_A_to_B.empty())


    async def testChannelFull(self):

        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)
        
        channel_A_to_B = asyncio.Channel("A", "B", monitor, 1)

        self.assertFalse(channel_A_to_B.full())
        await channel_A_to_B.send("hello world")
        self.assertTrue(channel_A_to_B.full())
        await channel_A_to_B.receive()
        self.assertFalse(channel_A_to_B.full())


    async def testChannelSize(self):
        
        specificationPath = getSpecificationPath("test_monitor")
        monitor = Monitor(specificationPath)
        
        channel_A_to_B = asyncio.Channel("A", "B", monitor)

        self.assertEqual(0, channel_A_to_B.size())
        await channel_A_to_B.send("hello world")
        self.assertEqual(1, channel_A_to_B.size())
        await channel_A_to_B.receive()
        self.assertEqual(0, channel_A_to_B.size())


def getSpecificationPath(specificationName: str):
    return os.path.abspath(f"test/testcases/specifications/{specificationName}.txt")   
