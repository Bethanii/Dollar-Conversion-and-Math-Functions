
from num2words import num2words


def get_input():
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    return quarters, dimes, nickels, pennies


def convert_to_dollars(quarters, dimes, nickels, pennies):
    total_cents = (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies
    dollar_value = total_cents / 100.0
    return dollar_value


def dollars_to_words(dollar_value):
    word_value = str(dollar_value).split(".")
    return (num2words(word_value[0]) + " dollars and " + num2words(word_value[1]) + " cents")


def display_menu(quarters, dimes, nickels, pennies, dollar_value):
    print("\n---------VALUES ENTERED---------")
    print("Quarters: " + str(quarters))
    print("Dimes: " + str(dimes))
    print("Nickels: " + str(nickels))
    print("Pennies: " + str(pennies))

    print("\n-------------RESULTS-------------")
    print("This is equal to: ${:.2f}".format(dollar_value) + " or " + dollars_to_words(dollar_value))


def main():
    quarters, dimes, nickels, pennies = get_input()
    dollar_value = convert_to_dollars(quarters, dimes, nickels, pennies)
    display_menu(quarters, dimes, nickels, pennies, dollar_value)


if __name__ == "__main__":
    main()