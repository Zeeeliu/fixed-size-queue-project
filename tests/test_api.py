import unittest
import requests


class TestFixedSizeQueueAPI(unittest.TestCase):
    BASE_URL = 'http://localhost:5001'

    def setUp(self):
        # runs before each test and clear the queue before each test
        requests.delete(f"{self.BASE_URL}/queue/clear")

    def test_get_queue(self):
        # test on empty queue, expect to see "Queue is empty" and size = 0
        response = requests.get(f"{self.BASE_URL}/queue")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['queue'], "Queue is empty")
        self.assertEqual(data['size'], 0)

        # add an item and test again, expect to see "Queue(test_item)" and size = 1
        requests.post(f"{self.BASE_URL}/queue/enqueue", json={"item": "test_item"})  # add test item

        response = requests.get(f"{self.BASE_URL}/queue")  # get_queue state
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['queue'], "Queue(test_item)")
        self.assertEqual(data['size'], 1)

    def test_enqueue(self):
        # test enqueue of test item "A"
        response = requests.post(f"{self.BASE_URL}/queue/enqueue", json={"item": "A"}) # add "A" to the queue
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data['queue'], "Queue(A)")

        # test enqueue of test item "B"
        response = requests.post(f"{self.BASE_URL}/queue/enqueue", json={"item": "B"})  # add "B" to the queue
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data['queue'], "Queue(A->B)")




