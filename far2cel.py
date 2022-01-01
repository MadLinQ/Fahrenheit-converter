import re


def main():
    data = input(r'Enter the value to convert(e.g. 40f or 40c): ')
    try:
        regex = re.search(r'([-+]?\d+)([c,C]$|[f,F]$)', data)
        result, degree, prefix = str(regex[0]), int(regex[1]), str(regex[2].lower())
    except (TypeError, AttributeError):
        regex = ''
        print('Something is wrong!')
        return main()

    while re.match(result, data):
        if 'f' in prefix:
            fahrenheit(degree)
        else:
            celcius(degree)
    else:
        print('Error')
        return main()


def fahrenheit(degree):
    far = (degree - 32) * 5 / 9
    print(degree, 'degrees Fahrenheit equals ', far, 'degrees Celcius')
    return main()


def celcius(degree):
    cel = (degree * 9 / 5) + 32
    print(degree, 'degrees Celcius equals ', cel, 'degrees Fahrenheit')
    return main()


if __name__ == '__main__':
    main()
