from flask import Flask, request, jsonify
from src.fixed_size_queue import FixedSizeQueue

# Initialize Flask application
app = Flask(__name__)

# Crate a global instance of FixedSizeQueue， initiate its max_size as 5
queue = FixedSizeQueue(max_size=5)


@app.route('/queue', methods=['GET'])
def get_queue():
    """
    Endpoint to get the current state of the queue.
    :return: JSON response with the queue's string representation and its current size
    """
    return jsonify({
        'queue': str(queue),  # convert queue to string representation
        'size': len(queue)  # get current number of items in the queue
    })


@app.route('/queue/enqueue', methods=['POST'])
def enqueue():
    """
    Endpoint to add an item to the queue.
    :return: JSON response with a success message or error, and the state of the updated queue
    """
    data = request.json  # get JSON data from the request body

    # check if the required 'item' field is in the request data
    if 'item' not in data:
        return jsonify({'error': 'No item provided for enqueue'}), 400  # bad request

    try:
        queue.enqueue(data['item'])  # try to add the item to the queue
        return jsonify({
            'message': f"Enqueued {data['item']}",
            'queue': str(queue)
        }), 201  # created status code
    except OverflowError as e:
        # if the queue is full, catch the OverFlowError and return the error response
        return jsonify({'error': str(e)}), 400  # bad request


@app.route('/queue/dequeue', methods=['DELETE'])
def dequeue():
    """
    Endpoint to remove and return the front item from the queue.
    :return: JSON response with the dequeued item and updated queue state, or an error
    """
    try:
        deleted_item = queue.dequeue()  # try to remove an item from the queue
        return jsonify({
            'dequeued': deleted_item,
            'queue': str(queue)
        })
    except IndexError as e:
        # if the queue is empty, catch the IndexError and return an error message
        return jsonify({'error': str(e)}), 400  # bad request


@app.route('/queue/peek', methods=['GET'])
def peek():
    """
    Endpoint to view the front item of the queue without removing it.
    :return: JSON response with the front item, or an error if the queue is empty
    """
    peek_item = queue.peek()  # try to peek at the front item
    if peek_item is None:
        return jsonify({'error': 'Queue is empty'}), 400  # bad request
    return jsonify({'front': peek_item})


@app.route('/queue/clear', methods=['POST'])
def clear_queue():
    global queue
    queue = FixedSizeQueue(max_size=5)  # reinitialize the queue
    return jsonify({'message': 'Queue cleared'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
