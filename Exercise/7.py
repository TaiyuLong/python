list1 = ['Google', 'Github', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

print("list1: ", list1)
print("list1[0]: ", list1[0])
print("list2: ", list2)
print("list2[1:5]: ", list2[1:5])
print("list3: ", list3)
print("list3[2:3]: ", list3[2:3])

print("\n")

list1[1] = 'CSDN'
print("更新后list1: ", list1)

del list2[2]
print("删除第三个元素后list2: ", list2)
