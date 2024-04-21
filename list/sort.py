my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# 对列表进行排序并打印结果
sorted_list = sorted(my_list)
print("使用 sorted() 函数排序后的列表:", sorted_list)

# 原始列表并未改变
print("原始列表:", my_list)

my_list2 = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# 对列表进行排序（会修改原始列表）并打印结果 降序
my_list2.sort(reverse=True)

print("使用 sort() 方法排序后的列表:", my_list2)

# 原始列表已经被排序
print("原始列表:", my_list2)
