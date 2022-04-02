from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rez = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                rez[stackInd] = i - stackInd
            stack.append((t, i))

        return rez


def main():
    temperatures = [73, 74, 75, 71, 73, 72, 76, 73]
    solution = Solution()
    print(solution.dailyTemperatures(temperatures))


if __name__ == '__main__':
    main()
