l = [1, 2, 3]
l.append(4)
print(l)

l = ["a", "b", "c", "a"]
l.remove("a")
print(l)

l = [9, 1, -4, 3, 7, 11, 3]
print(l.count(3))

l = [3, 12, 7, 9, 5, 3, 3, 3, 2, 4]  # 這是一個有十個元素的list
l.append(8)  # 把8加到L的最後面
print(l)  # 印出L

c = l.count(3)  # 計算L中有幾個3
for i in range(c):  # 把L中的所有3都移除
    l.remove(3)

print(l)  # 印出L

l.pop(0)  # 把l中的第0個元素移除
print(l)  # 印出L
# pop 與 remove 的差別, pop 是用index, remove 是用元素來刪除

l.sort()  # 把l中的元素由小到大排序
print(l)  # 印出L
l.sort(reverse=True)  # 把l中的元素由大到小排序
print(l)  # 印出L

l = [3, 1, 2, 4, 5]
print(l.index(5))  # 取出L中的5的index
