def even_numbers(n):
    even_list = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_list.append(i)
    return even_list

