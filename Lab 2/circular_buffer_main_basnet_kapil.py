
# Program: Circular Buffer Test Program
# Description: Tests the operations of the CircularBuffer class.
# Name: Kapil Basnet
# Date: 11/01/2026

from circular_buffer import CircularBuffer


# Calculate the sum of all items
def add_all(buffer):
    total = 0

    for i in range(buffer.get_size()):
        index = (buffer.get_head() + i) % buffer.get_capacity()
        total += buffer.get_buffer()[index]

    return total


# Find the index of the largest item
def get_max_index(buffer):
    if buffer.is_empty():
        return -1

    max_index = buffer.get_head()

    for i in range(buffer.get_size()):
        index = (buffer.get_head() + i) % buffer.get_capacity()

        if buffer.get_buffer()[index] > buffer.get_buffer()[max_index]:
            max_index = index

    return max_index


# Find the index of the smallest item
def get_min_index(buffer):
    if buffer.is_empty():
        return -1

    min_index = buffer.get_head()

    for i in range(buffer.get_size()):
        index = (buffer.get_head() + i) % buffer.get_capacity()

        if buffer.get_buffer()[index] < buffer.get_buffer()[min_index]:
            min_index = index

    return min_index


# Main test program
def main():

    capacity = int(input("Enter Buffer Capacity: "))

    if capacity <= 0:
        print("Buffer capacity must be greater than zero.")
        return

    buffer = CircularBuffer(capacity)

    # 1. Delete operation
    print("1. Delete operation:")
    deleted = buffer.delete()

    if deleted is None:
        print("Buffer is empty")
    else:
        print(f"{deleted} has been deleted")

    # 2. Add 15
    print("2. Add 15:")
    buffer.add(15)
    print("Buffer:", buffer)

    # 3. Add 5
    print("3. Add 5:")
    buffer.add(5)
    print("Buffer:", buffer)

    # 4. Delete operation
    print("4. Delete operation:")
    deleted = buffer.delete()
    print(f"{deleted} has been deleted")
    print("Buffer:", buffer)

    # 5. Add 3
    print("5. Add 3:")
    buffer.add(3)
    print("Buffer:", buffer)

    # 6. Add 26
    print("6. Add 26:")
    buffer.add(26)
    print("Buffer:", buffer)

    # 7. Delete operation
    print("7. Delete operation:")
    deleted = buffer.delete()
    print(f"{deleted} has been deleted")
    print("Buffer:", buffer)

    # 8. Add 76
    print("8. Add 76:")
    buffer.add(76)
    print("Buffer:", buffer)

    # 9. Add 105
    print("9. Add 105:")
    buffer.add(105)
    print("Buffer:", buffer)

    # 10. Search for 48
    print("10. Search 48:")
    if buffer.find(48):
        print("48 is in the buffer")
    else:
        print("48 is not in the buffer")

    # 11. Display first and last items
    print("11. Display items at first and last")
    print(f"{buffer.peek_first()} is the first item, "
          f"and {buffer.peek_last()} is the last item")

    # 12. Add all items
    print("12. Add all items:")
    print("Sum =", add_all(buffer))

    # 13. Find largest and smallest items
    print("13. Locate the largest/smallest item")

    max_index = get_max_index(buffer)
    min_index = get_min_index(buffer)

    if max_index != -1:
        largest = buffer.get_buffer()[max_index]
        smallest = buffer.get_buffer()[min_index]

        print(f"The largest item = {largest}")
        print(f"The smallest item = {smallest}")

    # 14. Clear the buffer
    print("14. Clear the buffer:")
    buffer.clear()
    print("Buffer:", buffer)


if __name__ == "__main__":
    main()
