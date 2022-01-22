import re
from Conv import Conv


def main():
    data = input(
        'Enter the value to convert(e.g. 40f or 40c)\
        \nor type exit to close programm: ').lower()
    regex = re.search(r'(^\-?\d+\.?\d*)(\s?)([c|f]{1}$)', data)
    if regex != None:
        degree, prefix = float(regex[1]), str(regex[3])
        if 'f' in prefix:
            print(''.join(str(i) for i in Conv(degree).fahrenheit()))
        else:
            print(''.join(str(i) for i in Conv(degree).celcius()))
        return main()
    else:
        print('Something is wrong!')
        return main()


if __name__ == '__main__':
    main()
