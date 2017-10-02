"""
    ユーザー定義クラスを比較可能にする

    参考：
        https://docs.python.jp/3/reference/datamodel.html#object.__lt__
        https://docs.python.org/ja/3/library/constants.html#NotImplemented
"""

class Item(object):

    def __init__(self, price):
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.price == other.price    

    def __lt__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.price < other.price

    # 実装しなくても良い.
    # 実装しない場合には、__eq__の結果を反転してものが返される.
    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

item1 = Item(100)
item2 = Item(101)
print(item1 == item2)  # False
print(item1 == 101)    # False
print(item1 < item2)   # True
print(item1 != item2)  # True
print(item1 <= item2)  # True
print(item1 > item2)   # False
print(item1 >= item2)  # False


print("--------")

"""
    便利デコレーターを使う場合（ただし実行速度が落ちる）
    https://docs.python.jp/3/library/functools.html#functools.total_ordering
"""
from functools import total_ordering

@total_ordering
class Student(object):

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return (self.firstname, self.lastname) == (other.firstname, other.lastname)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return (self.firstname, self.lastname) < (other.firstname, other.lastname)


student1 = Student("Hen", "Lee")
student2 = Student("Ken", "Koba")
student3 = Student("Ken", "Koba")
print(student1 == student2)  # False
print(student2 == student3)  # True
print(student1 != student2)  # True
print(student1 < student2)   # True
print(student1 <= student2)  # True
print(student1 > student2)   # False
print(student1 >= student2)  # False