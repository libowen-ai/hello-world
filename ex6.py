fruits = ["苹果","香蕉","橘子"]
print(fruits[0])    # 苹果
print(fruits[1])    # 香蕉
print(fruits[2])    # 橘子
print(fruits[-1])   # 橘子, -1 表示最后一个
print(fruits[-2])   # 香蕉
fruits.append("葡萄")
print(fruits)
print("一共",len(fruits),"个")

for f in fruits:
    print(f)