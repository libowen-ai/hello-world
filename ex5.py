def greet(name):
    print("你好，", name)

greet("libowen-ai")
greet("Python")


def is_even(n):
    if n % 2 == 0:
        return True
    return False


for i in range(1, 11):
    if is_even(i):
        print(i, "是偶数")