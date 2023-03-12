def get_delta_with_avg(lst):
    """Получаем массив разниц между каждым элементом списка и ср знач."""
    delta_lst = []
    avg = sum(lst)/len(lst)
    for i in lst:
        delta_lst.append(i - avg)
    return delta_lst

def get_multiplication_lst(lst1, lst2):
    """Получаем список перемноженных между собой элементов двух исходных массивов."""
    lst_multiply = []
    for i in range(len(lst1)):
        lst_multiply.append(lst1[i] * lst2[i])
    return lst_multiply

def get_squaring_lst(lst):
    """Получаем список элементов, возведенных в квадрат."""
    lst_squaring = []
    for i in range(len(lst)):
        lst_squaring.append(lst[i] ** 2)
    return lst_squaring   


def get_correlation_coefficient(prices_first, prices_second):
    """Рассчет коэффициента корреляции."""
    first_lst_delta_avg = get_delta_with_avg(prices_first)
    second_lst_delta_avg = get_delta_with_avg(prices_second)
    multiply_lst_divinded = get_multiplication_lst(first_lst_delta_avg, second_lst_delta_avg)
    divinded_pirson = sum(multiply_lst_divinded)

    first_lst_squering = get_squaring_lst(first_lst_delta_avg)
    second_lst_squering = get_squaring_lst(second_lst_delta_avg)
    divisor_pirson = (sum(first_lst_squering) * sum(second_lst_squering)) ** 0.5
    print(divinded_pirson/divisor_pirson)
    return divinded_pirson/divisor_pirson