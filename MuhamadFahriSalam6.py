class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        print(f"Menambahkan buku: \"{item}\"")

    def pop(self):
        if not self.is_empty():
            item = self.items.pop()
            print(f"Mengambil buku: \"{item}\"")
            return item
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            item = self.items[-1]
            print(f"Melihat buku teratas: \"{item}\"")
            return item
        else:
            return "Stack is empty"

    def size(self):
        size = len(self.items)
        print(f"Jumlah buku dalam tumpukan: {size}")
        return size

    def display(self):
        return self.items

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
        print(f"Menambahkan pengunjung: \"{item}\"")

    def dequeue(self):
        if not self.is_empty():
            item = self.items.pop()
            print(f"Mengeluarkan pengunjung: \"{item}\"")
            return item
        else:
            return "Queue is empty"

    def size(self):
        size = len(self.items)
        print(f"Jumlah pengunjung dalam antrean: {size}")
        return size

    def display(self):
        return self.items

# Mengelola tumpukan buku dengan stack
book_stack = Stack()
book_stack.push("Struktur Data")
book_stack.push("Algoritma")
book_stack.push("Pemrograman Java")
book_stack.peek()
book_stack.pop()
book_stack.peek()
book_stack.size()
print("Daftar buku di stack:", book_stack.display())

# Mengelola antrean pengunjung dengan queue
visitor_queue = Queue()
visitor_queue.enqueue("Alice")
visitor_queue.enqueue("Bob")
visitor_queue.enqueue("Charlie")
print("\nPengunjung depan dalam antrean:", visitor_queue.display()[-1])
visitor_queue.dequeue()
print("Pengunjung depan dalam antrean:", visitor_queue.display()[-1])
visitor_queue.size()
print("Daftar antrean pengunjung di queue:", visitor_queue.display())
