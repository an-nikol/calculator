def main():
    while True:
        print('Menu:')
        print('1.Addition')
        print('2.Subtraction')
        print('3.Multiplication')
        print('4.Division')
        print('5.Quit the program')
        print()

        option = input('Please choose one of the following options(1/2/3/4/5): ')

        if option == '1':
            first_number = int(input('Please enter the first number: '))
            second_number = int(input('Please enter the second number: '))
            result = addition(first_number, second_number)
            print(f'The result is: {first_number} + {second_number} = {result}')
        elif option == '2':
            first_number = int(input('Please enter the first number: '))
            second_number = int(input('Please enter the second number: '))
            result = subtraction(first_number, second_number)
            print(f'The result is: {first_number} - {second_number} = {result}')
        elif option == '3':
            first_number = int(input('Please enter the first number: '))
            second_number = int(input('Please enter the second number: '))
            result = multiplication(first_number, second_number)
            print(f'The result is: {first_number} * {second_number} = {result}')
        elif option == '4':
            first_number = int(input('Please enter the first number: '))
            second_number = int(input('Please enter the second number: '))
            result = division(first_number, second_number)
            print(f'The result is: {first_number} / {second_number} = {result}')
        elif option == '5':
            print('Goodbye!')
            break

def addition(n1, n2):
    result = n1 + n2
    return result


def subtraction(n1, n2):
    result = n1 - n2
    return result


def multiplication(n1, n2):
    result = n1 * n2
    return result


def division(n1, n2):
    result = n1 / n2
    return  result

if __name__=="__main__":
    main()
