"""
    自作クラスをSetで使えるようにするための方法

    参考：
        https://docs.python.jp/3/reference/datamodel.html#object.__hash__
"""

class User(object):
    
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __eq__(self, other):
        if type(other) != User:
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
        # return hash((self.id, self.name))
        # return hash(repr(user1))


user1 = User(1, "Yohei")
user2 = User(2, "Satoshi")
user3 = User(3, "Kento")
user4 = User(1, "Shunji")  # idが一緒


d = dict([(user1, 30), (user2, 25)])



s = set([user1, user2, user3, user4])
print(len(s)) # => 3
for user in s:
    print(user.id, user.name)
    # 1 Yohei
    # 2 Satoshi
    # 3 Kento

print(repr(user1))          # <__main__.User object at 0x1022a4c50>
# print(hash(repr(user1)))


# $ python3 hashable.py 
# Traceback (most recent call last):
#   File "hashable.py", line 30, in <module>
#     d = dict([(user1, 30), (user2, 25)])
# TypeError: unhashable type: 'User'


# $ python3 hashable.py 
# Traceback (most recent call last):
#   File "hashable.py", line 30, in <module>
#     s = set([user1, user2, user3, user4])
# TypeError: unhashable type: 'User'