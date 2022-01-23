class Conv:

    def __init__(self, degree):
        self.degree = degree

    def fahrenheit(self):
        result = (self.degree - 32) * 5 / 9
        if result < -273.15:
            return 'Temperature below absolute zero'
        else:
            return self.degree, ' degrees Fahrenheit equals ', round(result, 1), ' degrees Celsius'

    def celsius(self):
        result = (self.degree * 9 / 5) + 32
        if result < -459.67:
            return 'Temperature below absolute zero'
        else:
            return self.degree, ' degrees Celsius equals ', round(result, 1), ' degrees Fahrenheit'
