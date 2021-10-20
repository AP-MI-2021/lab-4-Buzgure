from typing import List


def show_menu():
    print('1. Citire lista float-uri')
    print('2. Afisarea partii intregi a tuturor numerelor din lista')
    print('3. Afisarea tuturor numerelor ce apartin unui interval deschis citit de la tastatura')
    print('4. Afisarea tuturor numerelor a caror parte intreaga este divizor al partii fractionare')
    print('5. Afisarea listei obtinute din lista initiala in care numerele sunt '
          'inlocuite cu un string format din cuvinte')
    print('x. Exit')

def main():
    while True:
        show_menu()
        option = input("Introduceti o optiune: ")
        if option == '1':
            lst = read_list()
        elif option == '2':
            print(f'Lista ce contine partea intreaga din {lst} este {show_int(lst)}')
        elif option == '3':
            print(f'Numerele din {lst} care se afla in intervalul cerut sunt {numere_in_interval(lst)}')
        elif option == '4':
            print(f'Numerele din {lst} a caror parte intreaga este divizor al partii fractionare sunt {int_div_fract(lst)} ')
        elif option == '5':
            print(replace_numbers(lst))
        elif option == 'x':
            break
        else:
            print("Optiune invalida")


def read_list():
    list = []
    list_str = input("Introduceti numerele separate prin spatiu: ")
    list_str_split = list_str.split(' ')
    for numbers in list_str_split:
        list.append(float(numbers))
    return list


def show_int(lst: List[float]) -> List[int]:
    """
    Returneaza partea intreaga a fiecarui element dintr-o lista de float-uri
    :param lst: Lista de float-uri
    :return: result: Lista ce contine partea intreaga a fiecarui element
    """

    result = []
    for numbers in lst:
        result.append(int(numbers))
    return result

def test_show_int():
    assert show_int([1.5, -3.3, 8, 9.8, 3.2]) == [1, -3, 8, 9, 3]
    assert show_int([1, -3.3, 8, 9.8, 3.2]) == [1, -3, 8, 9, 3]
    assert show_int([1.5, -3.3, 8, 9.8, 3.2, 72.6]) == [1, -3, 8, 9, 3, 72]



def numere_in_interval(lst:List[float]) -> List[float]:
    """
    Returneaza o lista cu numerele care se afla intr-un interval citit de la tastatura
    :param lst: lista de float-uri
    :return: result: lista ce contine numerele cerute
    """

    result = []
    first = int(input("Dati primul capat al intervalului: "))
    second = int(input("Dati celalalt capat al intervalului: "))
    for numbers in lst:
        if numbers > first and numbers < second:
            result.append(numbers)
    return result

def test_numere_in_interval():
    assert numere_in_interval([1.5, -3.3, 8, 9.8, 3.2]) == [1.5, -3.3, 3.2] #daca numerele citite sunt -4,5
    assert numere_in_interval([1.5, -3.3, 8, 9.8, 3.2]) == [1.5, 3.2] #daca numerele citite sunt 0,4
    assert numere_in_interval([1.5, -3.3, 8, 9.8, 3.2]) == [-3.3] #daca numerele citite sunt -4,-2
    assert numere_in_interval([1.5, -3.3, 8, 9.8, 3.2]) == [] #daca numerele citite sunt 10,15
def is_div(first, second):
    """
    Verifica daca second este divizorul lui first
    :param first: primul numar
    :param second: al doilea numar
    :return: True daca second este divizorul lui first, False altfel
    """

    if first % second == 0:
        return True
    return False


def test_is_div():
    assert is_div(8,4) is True
    assert is_div(8,5) is False
    assert is_div(12,4) is True

def get_fract(number: float) -> int:
    """
    Returneaza partea fractionara a unui float, ca int
    :param number:numarul a carui parte fractionara trebuie citita
    :return: fract: partea fractionara
    """

    result_str = str(number)
    result_split = result_str.split('.')
    fract = int(result_split[1])
    return fract


def test_get_fract():
    assert get_fract(14.5) == 5
    assert get_fract(14.523) == 523
    assert get_fract(14.0) == 0
    assert get_fract(14.897) == 897
    assert get_fract(14.512) == 512
    assert get_fract(14.90) == 90


def int_div_fract(lst):
    """
    Returneaza lista rezultata din lst ce contine doar numerele a caror parte intreaga este divizor al partii fractionare
    :param lst: lista de float-uri
    :return: lista ceruta
    """

    result = []
    for numbers in lst:
        if int(numbers) != numbers and is_div(get_fract(numbers), int(numbers)):
            result.append(numbers)
    return result

def replace_numbers(lst):
    replace_with = ['zero', 'unu', 'doi', 'trei', 'patru', 'cinci', 'sase', 'sapte', 'opt', 'noua', 'zece']
    separator = ['virgula']
    result = []
    for numbers in lst:
        if numbers == int(numbers):
            int_number = int(numbers)
            while(int_number):
                number_str = replace_with[int_number % 10]
                int_number //= 10
                result.append(number_str)
            result.reverse()

        else:
            int_part = int(numbers)
            fract_part = get_fract(numbers)
    return result
if __name__ == '__main__':
    test_show_int()
    test_is_div()
    test_get_fract()
    test_numere_in_interval()
    main()