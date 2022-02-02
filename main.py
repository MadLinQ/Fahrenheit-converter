import re
from Conv import Conv


def main():
    data = input(
        'Enter the value to convert(e.g. 40f or 40c): ').lower()
    regex = re.search(r'(^-?\d+\.?\d*)(\s?)([c|f]$)', data)
    if regex is not None:
        degree, key = float(regex[1]), str(regex[3])
        if 'f' in key:
            print(''.join(str(i) for i in Conv(degree).fahrenheit()))
        else:
            print(''.join(str(i) for i in Conv(degree).celsius()))
    else:
        print('Something is wrong!')


if __name__ == '__main__':
    main()
