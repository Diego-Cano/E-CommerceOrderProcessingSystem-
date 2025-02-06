import unittest

class Order:
    def __init__(self, order_id, customer_name, order_details):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_details = order_details
        self.next = None  # Pointer to the next order
    
    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer_name}, Details: {self.order_details}"

class OrderLinkedList:
    def __init__(self):
        self.head = None  # First order in the list
    
    def append(self, order):
        if not self.head:
            self.head = order
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = order
    
    def display(self):
        current = self.head
        while current:
            print(current)
            current = current.next
        print("-" * 30)
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_order = current.next  # Save next order
            current.next = prev  # Reverse the pointer
            prev = current  # Move prev to current
            current = next_order  # Move current to next
        self.head = prev  # Update head to the new first order

class TestOrderLinkedList(unittest.TestCase):
    def setUp(self):
        self.order_list = OrderLinkedList()
        self.order1 = Order(1, "Alice", "Laptop")
        self.order2 = Order(2, "Bob", "Smartphone")
        self.order3 = Order(3, "Charlie", "Headphones")
        
    def test_append(self):
        self.order_list.append(self.order1)
        self.assertEqual(self.order_list.head, self.order1)
        
        self.order_list.append(self.order2)
        self.assertEqual(self.order_list.head.next, self.order2)
        
        self.order_list.append(self.order3)
        self.assertEqual(self.order_list.head.next.next, self.order3)
    
    def test_reverse(self):
        self.order_list.append(self.order1)
        self.order_list.append(self.order2)
        self.order_list.append(self.order3)
        
        self.order_list.reverse()
        self.assertEqual(self.order_list.head, self.order3)
        self.assertEqual(self.order_list.head.next, self.order2)
        self.assertEqual(self.order_list.head.next.next, self.order1)
        self.assertIsNone(self.order_list.head.next.next.next)

if __name__ == "__main__":
    unittest.main()
