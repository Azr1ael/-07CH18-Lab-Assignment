
# Program: Circular Buffer
# Description: Implements a circular buffer using a Python list.
# Name: Kapil Basnet
# Date: 11/01/2026


class CircularBuffer:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__size = 0
        self.__buffer = [None] * capacity
        self.__head = 0
        self.__tail = 0

    # Getters
    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        if capacity > 0:
            items = []
            while not self.is_empty():
                items.append(self.delete())

            self.__capacity = capacity
            self.__buffer = [None] * capacity
            self.__head = 0
            self.__tail = 0
            self.__size = 0

            for item in items[:capacity]:
                self.add(item)

    def get_size(self):
        return self.__size

    def get_buffer(self):
        return self.__buffer

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    # Add an item to the buffer
    def add(self, item):
        self.__buffer[self.__tail] = item

        if self.__size == self.__capacity:
            self.__head = (self.__head + 1) % self.__capacity
        else:
            self.__size += 1

        self.__tail = (self.__tail + 1) % self.__capacity

    # Delete the first item
    def delete(self):
        if self.is_empty():
            return None

        item = self.__buffer[self.__head]
        self.__buffer[self.__head] = None

        self.__head = (self.__head + 1) % self.__capacity
        self.__size -= 1

        if self.__size == 0:
            self.__head = 0
            self.__tail = 0

        return item

    # Clear the buffer
    def clear(self):
        self.__buffer = [None] * self.__capacity
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    # Check whether the buffer is empty
    def is_empty(self):
        return self.__size == 0

    # Return the first item
    def peek_first(self):
        if self.is_empty():
            return None
        return self.__buffer[self.__head]

    # Return the last item
    def peek_last(self):
        if self.is_empty():
            return None
        last_index = (self.__tail - 1) % self.__capacity
        return self.__buffer[last_index]

    # Search for an item
    def find(self, item):
        for i in range(self.__size):
            index = (self.__head + i) % self.__capacity
            if self.__buffer[index] == item:
                return True
        return False

    # Display buffer contents from head to tail
    def __str__(self):
        if self.is_empty():
            return "Buffer is empty"

        items = []
        for i in range(self.__size):
            index = (self.__head + i) % self.__capacity
            items.append(str(self.__buffer[index]))

        return " --> ".join(items)
