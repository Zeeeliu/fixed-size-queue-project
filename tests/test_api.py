import unittest
import requests


class TestFixedSizeQueueAPI(unittest.TestCase):
    BASE_URL = 'http://localhost:5001'

    def setUp(self):
        # runs before each test and clear the queue before each test
        requests.post(f"{self.BASE_URL}/queue/clear")

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

        # test enqueue when the queue is full, expect to receive an error message
        for i in range(3):
            requests.post(f"{self.BASE_URL}/queue/enqueue", json={"item": "test"})  # add 3 "tests" to fill the queue

        response = requests.post(f"{self.BASE_URL}/queue/enqueue", json={"item":"overflow"})
        self.assertEqual(response.status_code, 400)     # should be bad request, can not enqueue when it's full
        data = response.json()
        self.assertIn("error", data)                    # should contain error

    def test_dequeue(self):
        # test dequeue from an empty queue
        response = requests.delete(f"{self.BASE_URL}/queue/dequeue")
        self.assertEqual(response.status_code, 400)     # should be bad request - can not dequeue from empty queue
        data = response.json()
        self.assertIn("error", data)

        # test successful dequeue
        requests.post(f"{self.BASE_URL}/queue/enqueue", json={"item": "test"})
        response = requests.delete(f"{self.BASE_URL}/queue/dequeue")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['dequeued'], "test")
        self.assertEqual(data['queue'], "Queue is empty")

    def test_peek(self):
        # Test peek on empty queue
        response = requests.get(f"{self.BASE_URL}/queue/peek")
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn("error", data)

        # Test successful peek
        requests.post(f"{self.BASE_URL}/queue/enqueue", json={"item": "test_item"})
        response = requests.get(f"{self.BASE_URL}/queue/peek")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['front'], "test_item")

    def test_clear_queue(self):
        # Populate the queue
        for i in range(3):
            response = requests.post(f"{self.BASE_URL}/queue/enqueue", json={"item": f"item{i}"})
            self.assertEqual(response.status_code, 201)

        # Verify queue is not empty
        response = requests.get(f"{self.BASE_URL}/queue")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertNotEqual(data['queue'], "Queue is empty")
        self.assertGreater(data['size'], 0)

        # Clear the queue
        response = requests.post(f"{self.BASE_URL}/queue/clear")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['message'], "Queue cleared")

        # Verify queue is now empty
        response = requests.get(f"{self.BASE_URL}/queue")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['queue'], "Queue is empty")
        self.assertEqual(data['size'], 0)