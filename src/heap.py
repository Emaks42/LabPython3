class Heap:
    list_: list[int] = []

    def get_head(self):
        return len(self.list_)

    def add(self, elem):
        cur_ind = self.get_head()
        self.list_.append(elem)
        parent = (cur_ind - 1) // 2
        while self.list_[cur_ind] > self.list_[parent] and cur_ind != 0:
            self.list_[cur_ind], self.list_[parent] = self.list_[parent], self.list_[cur_ind]
            cur_ind = parent
            parent = (cur_ind - 1) // 2

    def heapify(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < self.get_head():
            if self.list_[largest] < self.list_[left]:
                largest = left
        if right < self.get_head():
            if self.list_[largest] < self.list_[right]:
                largest = right
        if largest != index:
            self.list_[largest], self.list_[index] = self.list_[index], self.list_[largest]
            self.heapify(largest)

    def get_max(self):
        result = self.list_[0]
        self.list_[0] = self.list_[-1]
        self.list_.pop()
        self.heapify(0)
        return result
