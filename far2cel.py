import re
from Conv import Conv


def main():
    data = input(
        'Enter the value to convert(e.g. 40f or 40c): ').lower()
    regex = re.search(r'(^-?\d+\.?\d*)(\s?)([c|f]{1}$)', data)
    if regex is not None:
        degree, prefix = float(regex[1]), str(regex[3])
        if 'f' in prefix:
            print(''.join(str(i) for i in Conv(degree).fahrenheit()))
        else:
            print(''.join(str(i) for i in Conv(degree).celsius()))
    else:
        print('Something is wrong!')


if __name__ == '__main__':
    main()
