"""
https://leetcode.com/problems/online-stock-span/
"""


class StockSpanner:

    def __init__(self):
        self.stack = []
        self.counter = 0

    def next(self, price: int) -> int:
        self.counter += 1

        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()

        if self.stack and price < self.stack[-1][0]:
            pr = self.counter - self.stack[-1][1]
        else:
            pr = self.counter

        self.stack.append((price, self.counter))
        return pr


def main():
    data = [100, 80, 60, 70, 60, 75, 85]
    # data = [1, 1, 1, 1, 1]
    rez = []
    sp = StockSpanner()
    for price in data:
        rez.append(sp.next(price))

    print(rez)


if __name__ == '__main__':
    main()
