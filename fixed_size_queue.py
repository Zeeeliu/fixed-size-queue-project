"""
Fixed Size Queue Implementation

An implementation of a fixed-size queue using circular array with two pointers.

Author: Ziye Liu

Features:
- Fixed size, pre-allocated memory
- FIFO behaviors
- Thread-safe
"""

import threading

class FixedSizeQueue:
    def __init__(self, max_size: int):
        """
        Initialize a fixed size queue with a given fixed size.
        :param max_size: Maximum number of elements the queue can hold (must be positive).
        """
        if max_size <= 0:               # validate max_size is positive
            raise ValueError("Queue size must be positive")

        self.max_size = max_size
        self.queue = [None] * max_size  # pre-allocate to avoid dynamically expanding array size during run time
        self.head = 0                   # pointer to the front of the queue
        self.tail = 0                   # pointer to the tail of the queue: next available position in the queue to add
        self.size = 0                   # current number of elements in the queue

        self.lock = threading.Lock()

    def is_empty(self) -> bool:
        """
        Check if the queue is empty
        :return: True if the queue is empty, false otherwise
        """

        return self.size == 0

    def is_full(self) -> bool:
        """
        Check if the queue is at its capacity
        :return: true if the queue is at its max size, false otherwise
        """

        return self.size == self.max_size

    def enqueue(self, item):
        """
        Add an item to the back of the queue.
        :param item: The item to be added to the back of the queue
        :raises OverflowError: If the queue is already full.
        """

        with self.lock:

            # check if the queue is already at its capacity.
            if self.is_full():
                raise OverflowError("Enqueue failed: Queue is full")

            else:
                self.queue[self.tail] = item    # place the new item at the end of the queue
                self.tail = (self.tail + 1) % self.max_size  # update tail to the next position, wrap around if needed
                self.size += 1                  # increment the size counter to reflect the addition of the new item

            print(f"Enqueued {item} at the queue")

    def peek(self):
        """
        peek at the front item without removing it
        :return: The front element in the queue. returns None if the queue is empty
        """

        if self.is_empty():
            return None

        else:
            return self.queue[self.head]    # return the item that is at the front of the queue

    def dequeue(self):
        """
        remove and return the front item from the back of the queue.
        :return: The item removed from the front the of the queue
        :raises IndexError: if the queue is empty
        """
        with self.lock:
            if self.is_empty():
                raise IndexError("Failed to deque: Queue is empty")

            else:
                dequeued_item = self.queue[self.head]           # use peek to find the element at the head of the queue
                self.queue[self.head] = None                    # clear the element at the head of the queue
                self.head = (self.head + 1) % self.max_size     # move the head pointer to the next position
                self.size -= 1                                  # decrease the size of the queue by 1
                print(f"Dequeued successfully")
                return dequeued_item

    def __len__(self) -> int:
        """
        Provide the current number of elements in the queue.
        :return: the current size of the queue
        """

        return self.size


    def __str__(self) -> str:
        """
        Print a string representation of the queue in a format of "Queue(item1) -> (item2) -> ...
        :return: a string representing the queue's contents.
        """

        if self.is_empty():
            return "Queue is empty"

        else:
            items = []                  # create an empty list to store the string representation
            current = self.head         # start from the head of the queue
            for _ in range(self.size):  # iterate through all items in the queue
                items.append(str(self.queue[current]))   # convert the current item to a str and add it to the list
                current = (current + 1) % self.max_size  # move to the next item, considering the circular array
            return f"Queue({'->'.join(items)})"          # Format the result



