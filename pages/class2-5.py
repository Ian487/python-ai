print([])  # 這是一個空的元素
print([1, 2, 3])  # 這是一個有三個元素的list
print([1, 2, 3, "a", "b", "c"])  # 這是一個有六個元素的list
print([1, 2, 3, ["a", "b", "c"]])  # 這是一個有四個元素的list
# 這是cow語言的程式碼
L = ["moO", "MOo", "moo", "mOO", "MoO", "moO"]
print(L[0])  # 取出L中的第一個元素, 元素編號index是從0開始
print(L[1])  # 取出L中的第二個元素
print(L[2])  # 取出L中的第三個元素
for index in range(len(L)):
    print(L[index])  # 取出L中的所有元素
for cow in L:
    print(cow)  # 取出L中的所有元素
L
