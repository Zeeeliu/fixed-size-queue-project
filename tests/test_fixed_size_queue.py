import unittest
from src.fixed_size_queue import FixedSizeQueue


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
        test_values = [1, 2, 3, 4, 5]
        test_val_size = len(test_values)
        for value in test_values:
            self.queue.enqueue(value)

        # Check initial length
        self.assertEqual(len(self.queue), test_val_size, f"Queue should have {test_val_size} elements")

        # Dequeue all items and check each one
        for i, expected_value in enumerate(test_values):
            # Check length before dequeue
            self.assertEqual(len(self.queue), test_val_size - i,
                             f"Queue should have {test_val_size - i} items before dequeue")

            # Dequeue and check value
            dequeued_value = self.queue.dequeue()
            self.assertEqual(dequeued_value, expected_value, f"Dequeued value should be {expected_value}")

            # Check length after dequeue
            self.assertEqual(len(self.queue), test_val_size - 1 - i,
                             f"Queue should have {test_val_size - 1 - i} items after dequeue")

        # Check if the queue is empty after all dequeues
        self.assertTrue(self.queue.is_empty(), "Queue should be empty after all dequeues")

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
