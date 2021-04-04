# simple FIFO queue implementation with array and two pointers
import sys


class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []
        self.front = 0
        self.rear = 0

    # method to check if queue is full
    def is_full(self):
        if self.rear == self.max_size:
            return True
        else:
            return False

    # method to check if queue is empty
    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    # method to add element at the rear of the
    def add_to_queue(self, element):
        # Check if queue is full
        if self.is_full():
            print('Queue is full. Maxsize is reached')
        else:
            self.queue.append(element)
            self.rear += 1

    # method to delete an element from the front of the queue
    def get_from_queue(self):
        # Check if queue is empty
        if self.is_empty():
            print('Queue is empty.')
        else:
            self.rear -= 1
            return self.queue.pop(0)

    # method to check len of the queue
    def queue_len(self):
        return len(self.queue)

    # method to check size of the queue
    def queue_size(self):
        size = 0
        for element in self.queue:
            size += sys.getsizeof(element)

        return size

    # method to display all elements of the queue
    def display_all_elements(self):
        # check if queue is not empty
        if self.is_empty():
            print('Queue is empty')
        else:
            for count, value in enumerate(self.queue):
                print(count, value)

    # method to display front element of the queue
    def display_front_element(self):
        # check if queue is not empty
        if self.is_empty():
            print('Queue is empty')
        else:
            print('Front element is: ', self.queue[self.front])