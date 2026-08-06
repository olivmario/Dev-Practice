_memory = {}
_address_counter = 1

class Node:
    def __init__(self, element):
        self.element = element
        self.both = 0

class XORLinkedList:
    def __init__(self):
        self.head_ptr = 0
        self.tail_ptr = 0

    def add(self, element):
        new_node = Node(element)
        new_ptr = get_pointer(new_node)

        if self.head_ptr == 0:
            self.head_ptr = new_ptr
            self.tail_ptr = new_ptr
        else:
            prev_node = dereference_pointer(self.tail_ptr)
            prev_node.both = prev_node.both ^ new_ptr
            new_node.both = self.tail_ptr
            self.tail_ptr = new_ptr

    def get(self, index):
        prev_ptr = 0
        current_ptr = self.head_ptr

        for _ in range(index):
            current_node = dereference_pointer(current_ptr)
            next_ptr = prev_ptr ^ current_node.both
            prev_ptr = current_ptr
            current_ptr = next_ptr
        
        return dereference_pointer(current_ptr).element

def get_pointer(node):
    global _address_counter
    if node is None:
        return 0
    addr = _address_counter
    _memory[addr] = node
    _address_counter += 1
    return addr

def dereference_pointer(addr):
    if addr == 0:
        return None
    return _memory[addr]


# Test
xor_list = XORLinkedList()
xor_list.add("A")
xor_list.add("XOR")
xor_list.add("C")

print(xor_list.get(0))
print(xor_list.get(1))
print(xor_list.get(2))