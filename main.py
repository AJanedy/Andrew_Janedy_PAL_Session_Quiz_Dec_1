def count_down_by_3():

    highest_number = 200
    lowest_number = 0
    number_list = []

    for number in range(lowest_number, highest_number):
        if number % 3 == 0 and number / 3 != 0:
            number_list.append(number)
    number_list.reverse()

    for number in number_list:
        print(number)

def main():
    count_down_by_3()

main()