class Counter:

    def __init__(self):
        self.input = [i for i in input().split()]
        self.count = {}
        self.search()

    def search(self):
        for s in self.input:
            if s in self.count:
                self.count[s] += 1
            else:
                self.count[s] = 1
        self.max()

    def max(self):
        self.maxim = 0
        self.maxim2 = 0
        for key in self.count:
            if len(key) > self.maxim2:
                self.maxim2 = len(key)
            if self.count[key] > self.maxim:
                self.maxim = float(self.count[key])
        self.output()

    def output(self):
        list_key = list(self.count.items())
        list_key.sort(key=lambda elem: elem[1])
        for i in list_key:
            number = round(float(i[1]) / self.maxim, 1) * 10
            if i[1] >= 1:
                print('_' * (self.maxim2 - len(i[0])) + i[0], int(number) * '.')

Counter()



