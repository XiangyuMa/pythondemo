#print('hello world')
# 创建一个列表
my_list = [1, 2, 3, 4, 5]

# 访问列表元素
print("第一个元素:", my_list[0])  # 访问第一个元素
print("最后一个元素:", my_list[-2])


# 对列表进行切片
print("切片元素:", my_list[2:5])  # 对索引 2 到 4 的元素进行切片

# 修改列表元素
my_list[0] = 10  # 修改第一个元素
print("修改后的列表:", my_list)

# 向列表添加元素
my_list.append(6)
print("添加后的列表:", my_list)

# 从列表中删除元素
my_list.remove(3)
print("删除元素 3 后的列表:", my_list)

# 获取列表长度
print("列表长度:", len(my_list))

# 遍历列表
print("遍历列表:")
for item in my_list:
    print(item)
