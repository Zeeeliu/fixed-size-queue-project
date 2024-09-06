# Fixed Size Queue API Specification

September 1, 2024


## Overview

This API provides operations for interacting with a Fixed Size Queue. The queue has a default maximum capacity 
of 5 items.

## Base URL

`http://localhost:5001`

## Authentication

This API does not require authentication.

## Endpoints

The API provides five main endpoints for interacting with the Fixed Size Queue:

1. **GET /queue**: Print the current state of the queue along with its size.
2. **POST /queue/enqueue**: Adds an item to the back of the queue.
3. **DELETE /queue/dequeue**: Removes and returns the front item from the queue.
4. **GET /queue/peek**: Views the front item of the queue without removing it.
5. **POST /queue/clear**: Clears all items from the queue.

Detailed information for each endpoint is provided below.

### 1. Get Queue State

#### GET /queue

Retrieves the current state of the queue.

##### Parameters

None

##### Response

```json
{
  "queue": "Queue(item1->item2->item3)",
  "size": 3
}
```

### 2. Enqueue Item

#### POST /queue/enqueue

Adds an item to the back of the queue.

##### Parameters

| Name | Type   | Description           |
|------|--------|-----------------------|
| item | string | Item to add to queue  |

##### Request Body

```json
{
  "item": "example_item"
}
```

##### Response

```json
{
  "message": "Enqueued example_item",
  "queue": "Queue(item1->item2->item3->example_item)"
}
```

### 3. Dequeue Item

#### DELETE /queue/dequeue

Removes and returns the front item from the queue.

##### Parameters

None

##### Response

```json
{
  "dequeued": "item1",
  "queue": "Queue(item2->item3->item4)"
}
```

### 4. Peek Queue

#### GET /queue/peek

Views the front item of the queue without removing it.

##### Parameters

None

##### Response

```json
{
  "front": "item1"
}
```

### Clear Queue

#### POST /queue/clear

Removes all items from the queue.

##### Parameters

None

##### Response

```json
{
  "message": "Queue cleared"
}
```

## Error Responses

In case of errors, the API will return an appropriate HTTP status code and a JSON object with an error message.

```json
{
  "error": "Error message describing the issue"
}
```

Error status codes:

- 400 Bad Request: Invalid input or operation (e.g., enqueueing to a full queue or dequeueing from an empty queue)

## Notes

- The queue has a default fixed size of 5 items.
- All operations are thread-safe.
- The API runs on `http://localhost:5001` by default.