# Как то вечером три разработчика написали 
# три метода класса `SomeClass`, каждый под себя. 
# Методы по сути своей почти одинаковые.
#
# Напишите свой метод `sorted_func`, 
# учитывая особенности всех представленных методов

class Solution:
    def __init__(self):
        self.lst = [3, 2, 1, 4, 2, 1]

    def sort(self, reverse=False):
        return sorted(self.lst, reverse=reverse)


if __name__ == "__main__":
    solution = Solution()
    print(solution.sort())
    print(solution.sort(True))
