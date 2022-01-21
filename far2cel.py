import re
from Conv import Conv


def main():
    data = input(
        'Enter the value to convert(e.g. 40f or 40c): ').lower()
    if '+' in data:
        data = data[1:]
    regex = re.search(r'(^\-?\d+[\.|,]?\d*)([c|f]{1}$)', data)
    if regex != None:
        degree, prefix = float(regex[1]), str(regex[2])
        t = Conv(degree)
        if 'f' in prefix:
            print(''.join(str(i) for i in t.fahrenheit()))
        else:
            print(''.join(str(i) for i in t.celcius()))
        return main()
    else:
        print('Something is wrong!')
        return main()


if __name__ == '__main__':
    main()
