import unittest
from fixed_size_queue import FixedSizeQueue


class TestFixedSizeQueue(unittest.TestCase):
    def setUp(self):
        # Create a new queue before each test
        self.queue = FixedSizeQueue(5)

    def test_initialization(self):
        # Test if the queue is correctly initialized
        self.assertEqual(len(self.queue), 0, "Queue should be empty upon initialization")
        self.assertTrue(self.queue.is_empty(), "Queue should be empty upon initialization")

    def test_enqueue(self):
        print("Starting enqueue test")
        for i in range(5):
            print(f"Enqueueing {i}")
            self.queue.enqueue(i)
            print(f"Queue after enqueue: {self.queue}")

        self.assertEqual(len(self.queue), 5, "Queue should have 5 items")
        self.assertTrue(self.queue.is_full(), "Queue should be full")

        with self.assertRaises(OverflowError):
            print("Attempting to enqueue to full queue")
            self.queue.enqueue(5)

    def test_enqueue_full(self):
        # Test enqueueing to a full queue
        for i in range(5):
            self.queue.enqueue(i)
        self.assertTrue(self.queue.is_full(), "Queue should be full after enqueueing 5 items")
        with self.assertRaises(OverflowError, msg="Enqueueing to a full queue should raise OverflowError"):
            self.queue.enqueue(5)

    def test_dequeue(self):
        # Test basic dequeue functionality
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1, "First dequeued item should be 1")
        self.assertEqual(len(self.queue), 1, "Queue length should be 1 after dequeueing")

    def test_dequeue_empty(self):
        # Test dequeueing from an empty queue
        with self.assertRaises(IndexError, msg="Dequeueing from an empty queue should raise IndexError"):
            self.queue.dequeue()

    def test_peek(self):
        # Test peek functionality
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.peek(), 1, "Peek should return the first item")
        self.assertEqual(len(self.queue), 2, "Peek shouldn't remove the item")

    def test_peek_empty(self):
        # Test peeking an empty queue
        self.assertIsNone(self.queue.peek(), "Peek should return None for an empty queue")

    def test_circular_behavior(self):
        # Test if the queue correctly wraps around when it reaches its capacity
        for i in range(5):
            self.queue.enqueue(i)
        for i in range(3):
            self.queue.dequeue()
        self.queue.enqueue(5)
        self.queue.enqueue(6)
        self.assertEqual(str(self.queue), "Queue(3->4->5->6)", "Queue should correctly wrap around")

    def test_str_representation(self):
        # Test string representation of a non-empty queue
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(str(self.queue), "Queue(1->2)", "String representation should be correct")

    def test_wrap_around_behavior(self):
        # Test wrap-around behavior
        for i in range(5):
            self.queue.enqueue(i)
        for i in range(5):
            self.assertEqual(self.queue.dequeue(), i, f"Dequeued item should be {i}")
        for i in range(5, 10):
            self.queue.enqueue(i)
        self.assertEqual(str(self.queue), "Queue(5->6->7->8->9)", "Queue should wrap around correctly")

