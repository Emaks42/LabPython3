class Node:
    def __init__(self, value: tuple[int, int] = (0, 0)):
        self.next = None
        self.value = value


class Stack:
    def __init__(self):
        self.memory = Node()
        self.quick_access_memory = self.memory
        self.size = 0

    def push(self, elem: int):
        """
            Функция, кладущая число на вершину стека
            :param elem: число, которое надо доабвать в стек
            :return: ничего не возвращает
        """
        if not isinstance(elem, int):
            raise ValueError("в стеке хранятся только целые числа")
        node_ = self.quick_access_memory
        self.size += 1
        qam_size = 1
        fifth_elem: Node = Node()
        while node_.next:
            node_ = node_.next
            qam_size += 1
            if qam_size == 5:
                fifth_elem = node_
        node_.next = Node((elem, min(elem, node_.value[1])))
        if qam_size > 10:
            node_main = self.memory
            while node_main.next:
                node_main = node_main.next
            self.quick_access_memory = fifth_elem.next

    def pop(self) -> int:
        """
            Функция, забирающая число с вершины стека
            :return: Возвращает число с вершины стека
        """
        if self.size == 0:
            raise IndexError("стек пустой, pop невозможно применить")
        prev_node = None
        node_ = self.quick_access_memory
        qam_size = 1
        self.size -= 1
        while node_.next:
            prev_node = node_
            node_ = node_.next
            qam_size += 1
        answer = node_.value[0]
        if prev_node:
            del prev_node.next
            prev_node.next = None
        else:
            del node_.next
            node_.next = None
        if qam_size < 3:
            node_main = self.memory
            dist_from_start = 1
            while node_main.next and dist_from_start < self.size - 5:
                node_main = node_main.next
                dist_from_start += 1
            self.quick_access_memory = node_main.next
        return answer

    def min(self):
        """
            Функция, находящая минимальный элемент стека
            :return: возвращает минимальное число в стеке
        """
        if self.size == 0:
            raise IndexError("стек пустой, min невозможно применить")
        node_ = self.quick_access_memory
        while node_.next:
            node_ = node_.next
        return node_.value[1]

    def peek(self):
        """
            Функция, возвращающая число с вершины стека
            :return: Возвращает число с вершины стека
        """
        if self.size == 0:
            raise IndexError("стек пустой, peek невозможно применить")
        node_ = self.quick_access_memory
        while node_.next:
            node_ = node_.next
        return node_.value[0]

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0


def interactive_stack():
    """
        Функция, реализующая интерактивное взаимодейтсвие со стеком через консоль
        :return: ничего не возвращает
    """
    print("Запущен эмулятор стека(введите exit для завершения)")
    stack = Stack()
    for i in range(100):
        stack.push(i)
    for i in range(100):
        print(stack.pop())
    command = ""
    while command != "exit":
        command = input()
        if command[:3] == "pop":
            try:
                print(stack.pop())
            except IndexError:
                print("Ошибка: стек пустой, pop невозможно применить")
        elif command[:4] == "push":
            try:
                stack.push(int(command[5:]))
            except ValueError:
                print("Ошибка: в стеке хранятся только целые числа")
        elif command[:3] == "min":
            try:
                print(stack.peek())
            except IndexError:
                print("Ошибка: стек пустой, min невозможно применить")
        elif command[:3] == "len":
            print(len(stack))
        elif command[:4] == "peek":
            try:
                print(stack.peek())
            except IndexError:
                print("Ошибка: стек пустой, peek невозможно применить")
        elif command == "exit":
            continue
        else:
            print("Неизвестная команда")
    print("Спасибо, что использовали наш эмулятор")
