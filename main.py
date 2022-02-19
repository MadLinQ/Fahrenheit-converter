import re


def main():
    while True:
        data = input(
            'Enter the value to convert(e.g. 40f or 40c): ').lower()
        regex = re.search(r'(^-?\d+\.?\d*)(\s?)([c|f]$)', data)
        if regex is not None:
            degree, key = float(regex[1]), str(regex[3])
            if 'f' in key:
                print(''.join(str(i) for i in (degree, ' degrees Fahrenheit equals ',
                    round((lambda x: (x - 32) * 5 / 9)(degree), 1), ' degrees Celsius')))
            else:
                print(''.join(str(i) for i in (degree, ' degrees Celsius equals ',
                    round((lambda x: (x * 9 / 5) + 32)(degree), 1), ' degrees Fahrenheit')))
        else:
            print('Something is wrong!')
            break


if __name__ == '__main__':
    main()
