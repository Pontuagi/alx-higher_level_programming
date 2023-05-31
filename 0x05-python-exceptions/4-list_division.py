#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    try:
        for i in range(list_length):
            try:
                div_1 = my_list_1[i]
                div_2 = my_list_2[i]
                if isinstance(div_1, (float, int)) and isinstance(div_2, (float, int)):
                    try:
                        division = div_1 / div_2
                        div_list.append(division)
                    except ZeroDivisionError:
                        print("division by 0")
                        div_list.append(0)
                else:
                    print("wrong type")
                    div_list.append(0)
            except IndexError:
                print("out of range")
                div_list.append(0)
    finally:
        return div_list
