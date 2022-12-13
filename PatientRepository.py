import Patient


class Node:
    def __init__(self, data: Patient):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class ListEmptyException(Exception):
    pass


class ListFullException(Exception):
    pass


class PatientRepoLinkedList:
    def __init__(self):
        self.head = None
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def remove(self):
        if self.is_empty():
            raise ListEmptyException
        item_str = self.items[self.head]
        self.head += 1
        return item_str

    def size(self):
        return len(self.items)

    def add_item(self, new_data: Patient):
        new_node = Node(new_data)
        self.items.append(new_node)
        new_node.next = self.head
        self.head = new_node

    def search(self, linked_list, search_last_name: str, search_first_name: str):
        if not linked_list:
            return False
        elif linked_list.data.last_name == search_last_name.upper():
            if linked_list.data.first_name == search_first_name.upper():
                return linked_list.data
        return self.search(linked_list.next, search_last_name, search_first_name)

    def print(self):
        if self.is_empty():
            return "List is Empty"
        else:
            list_string = ""
            for n in self.items:
                list_string += f"{n.__str__()}\n"
            return list_string





