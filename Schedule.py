import Patient


class ListEmptyException(Exception):
    pass


class ListFullException(Exception):
    pass


class QueueEmptyException(Exception):
    pass


class QueueFullException(Exception):
    pass


class ScheduleNode:
    def __init__(self, time_slot: int, data: Patient):
        self.time_slot = time_slot
        self.data = data
        self.next = None

    def get_node_info(self):
        return self.time_slot

    def __str__(self):
        return f"{self.data}, {self.time_slot}"


class ScheduleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = 0
        self.size_of_list = 0
        self.max_size = 10  # Sets the queue to a specific size.
        self.schedule = ["" for x in range(self.max_size)]

    def is_empty(self):
        return self.size_of_list == 0

    def is_full(self):
        return self.max_size == self.size_of_list

    def add_item(self, time_slot: int, new_data: Patient):
        new_node = ScheduleNode(time_slot, new_data)
        self.schedule[self.tail] = new_node
        self.tail += 1
        self.size_of_list += 1
        new_node.next = self.head
        self.head = new_node

    def get(self, time_slot: int):
        if self.is_empty():
            raise ListEmptyException
        node = self.head
        for i in range(self.size_of_list):
            if node.time_slot == time_slot:
                return f"{node.data.last_name}, {node.data.first_name}"
            node = node.next
        return "None found"

    def remove(self):
        if self.is_empty():
            raise ListEmptyException
        item_str = self.schedule[self.head]
        self.head += 1
        self.size_of_list -= 1
        return item_str

    def size(self):
        return self.size_of_list

    def print(self):
        if self.is_empty():
            return "List is Empty"
        else:
            list_string = ""
            i = 0
            n = 0
            while n < self.size_of_list:
                list_string += str(self.schedule[i]) + "\n"
                i = (i + 1) % self.max_size
                n += 1
            return list_string


class WaitListQueue:
    def __init__(self):
        self.head = 0
        self.max_size = 10  # Sets the queue to a specific size.
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return self.max_size == len(self.items)

    def enqueue(self, item: Patient):
        if self.is_full():
            raise QueueFullException
        else:
            self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyException
        item_str = self.items[self.head]
        self.items.pop(self.head)
        return item_str

    def peek(self):
        if self.is_empty():
            raise QueueEmptyException
        else:
            return self.items[self.head]

    def size(self):
        return len(self.items)

    def print_queue(self):
        if self.is_empty():
            return "Queue is Empty"
        else:
            queue_str = ""
            for i in range(len(self.items)):
                queue_str += self.items[i] + "\n"
                i+= 1
            return queue_str

