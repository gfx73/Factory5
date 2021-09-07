from random import randint


# Задание 1
# Предположим, что сложность randint(n) равна O(const)
# Тогда ожидаемая сложность алгоритма оценивается как O(k)
# Сложность худшего случая O(k)
# Потребление памяти составляет O(n)
def choose_k_rand_nums(input_list, k):
    n = len(input_list)
    result = []
    for i in range(k):
        index_to_swap = n - i - 1
        index_chosen = randint(0, index_to_swap)
        result.append(input_list[index_chosen])
        input_list[index_chosen], input_list[index_to_swap] = input_list[index_to_swap], input_list[index_chosen]

    return result


# Удаляет из списка элементы, вероятность выпадения которых равна нулю
# Сложность алгоритма в худшем и среднем случае O(n)
def del_el_with_0_probabilities(input_list, prob):
    n = len(input_list)
    zeroes_num = 0
    i = 0
    while i < n - zeroes_num:
        if prob[i] == 0:
            index_to_swap = n - zeroes_num - 1
            prob[i], prob[index_to_swap] = prob[index_to_swap], prob[i]
            input_list[i], input_list[index_to_swap] = input_list[index_to_swap], input_list[i]
            zeroes_num += 1
        else:
            i += 1
    return input_list, prob


# Задание 2
# Полсе выбора случайного индекса алгоритм решает выбрать ли это число.
# Предположим, что в среднем вероятность выбора числа равна p.
# Тода ожидаемое количество итераций после, которых будет выбрано число, оценивается как 1 / p.
# Так как вероятности кратны 0.1, а нулевые вероятности будут заранее удалены из списка,
# то количество необходимых итераций не превышает 10.
# Тогда ожидаемая сложность алгоритма оценивается как O(k).

# Тем не менее сложность худшего случая равна O(inf)

# Потребление памяти составляет O(n)
def choose_k_rand_nums_with_probabilities(input_list, prob, k):
    input_list, prob = del_el_with_0_probabilities(input_list, prob)
    n = len(input_list)
    result = []

    for i in range(k):
        number_found = False
        while not number_found:
            index_to_swap = n - i - 1
            index_chosen = randint(0, index_to_swap)
            p = randint(0, 9)
            if p < prob[index_chosen] * 10:
                result.append(input_list[index_chosen])
                input_list[index_chosen], input_list[index_to_swap] = input_list[index_to_swap], input_list[index_chosen]
                prob[index_chosen], prob[index_to_swap] = prob[index_to_swap], prob[index_chosen]
                number_found = True

    return result


my_list = [1, 3, 4, 3, 3, 9]
prob = [.7, .4, .5, .9, .1, .5]
k = 3
print(choose_k_rand_nums(my_list, k))
print(choose_k_rand_nums_with_probabilities(my_list, prob, k))
