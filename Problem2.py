import math


def get_input():
    value_one = int(input("Enter the first value: \n"))
    value_two = int(input("Enter the second value: \n"))
    value_three = int(input("Enter the third value: \n"))
    value_four = int(input("Enter the fourth value: \n"))
    return value_one, value_two, value_three, value_four


def get_sum(value_one, value_two, value_three, value_four):
    return math.fsum([value_one, value_two, value_three, value_four])


def get_average(value_one, value_two, value_three, value_four):
    total = value_one + value_two + value_three + value_four
    average = total / 4
    return average


def get_difference(value_one, average):
    difference = abs(average - value_one)
    return difference


def display_menu(value_one, value_two, value_three, value_four):
    print("\n---------VALUES ENTERED---------")
    print("Input 1: " + str(value_one))
    print("Input 2: " + str(value_two))
    print("Input 3: " + str(value_three))
    print("Input 4: " + str(value_four) +"\n")

    print("-------------RESULTS-------------")
    average = int(get_average(value_one, value_two, value_three, value_four))
    print("Value 1: " + str(value_one) + " Difference: " + str(get_difference(value_one, average)))
    print("Value 2: " + str(value_two) + " Difference: " + str(get_difference(value_two, average)))
    print("Value 3: " + str(value_three) + " Difference: " + str(get_difference(value_three, average)))
    print("Value 4: " + str(value_four) + " Difference: " + str(get_difference(value_four, average)))
    print("The sum of the values: " + str(get_sum(value_one, value_two, value_three, value_four)))
    print("The average of the values: " + str(average))


def main():
    value_one, value_two, value_three, value_four = get_input()
    display_menu(value_one, value_two, value_three, value_four)


if __name__ == "__main__":
    main()