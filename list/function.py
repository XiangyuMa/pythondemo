def square_sum_of_evens(lst):
    """
    计算给定列表中所有偶数的平方和。

    参数:
    lst (list): 包含整数的列表。

    返回值:
    int: 所有偶数的平方和。
    """
    # 检查列表是否为空
    if not lst:
        print("警告：输入列表为空！")
        return 0

    # 初始化平方和
    square_sum = 0

    # 遍历列表中的每个元素
    for num in lst:
        # 检查元素是否为整数
        if not isinstance(num, int):
            print(f"警告：元素 {num} 不是整数，已被忽略！")
            continue

        # 检查元素是否为偶数
        if num % 2 == 0:
            square_sum += num ** 2

    return square_sum

# 测试函数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = square_sum_of_evens(numbers)
print("所有偶数的平方和:", result)
