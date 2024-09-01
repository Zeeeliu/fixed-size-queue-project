from src.fixed_size_queue import FixedSizeQueue


def print_menu():
    print("\nFixed Size Queue Operations:")
    print("1. Initialize/Reset Queue")
    print("2. Enqueue")
    print("3. Dequeue")
    print("4. Peek")
    print("5. Display Queue")
    print("6. Exit")


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def run_cli():
    """
    Run the command-line interface for the Fixed Size Queue Program.
    This function provides a menu-based interface for interacting with a FixedSizeQueue instance
    """
    queue = None

    print("Welcome to the Fixed Size Queue Program!")
    print("This program demonstrates the implementation of a fixed size queue.")

    while True:
        print_menu()
        choice = get_int_input("Enter your choice (1-6): ")

        if choice == 1:
            size = get_int_input("Enter the maximum size of the queue: ")
            try:
                queue = FixedSizeQueue(size)
                print(f"Queue initialized with max size {size}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice in [2, 3, 4, 5]:
            if queue is None:
                print("Please initialize the queue first (Option 1).")
            else:
                if choice == 2:  # Enqueue
                    item = input("Enter the item to enqueue: ")
                    try:
                        queue.enqueue(item)
                        print(f"Enqueued: {item}")
                    except OverflowError as e:
                        print(f"Error: {e}")

                elif choice == 3:  # Dequeue
                    try:
                        item = queue.dequeue()
                        print(f"Dequeued: {item}")
                    except IndexError as e:
                        print(f"Error: {e}")

                elif choice == 4:  # Peek
                    item = queue.peek()
                    if item is None:
                        print("Queue is empty.")
                    else:
                        print(f"Front item (peek): {item}")

                elif choice == 5:  # Display Queue
                    print(f"Current queue: {queue}")
                    print(f"Queue size: {len(queue)}")

        elif choice == 6:
            print("Thank you for using the Fixed Size Queue Simulator. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    run_cli()
