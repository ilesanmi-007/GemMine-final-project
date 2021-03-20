#ATM CLASS
#default amount== 1k
#methods: withdraw, add money, check balance

class Person:
    def __init__(self,age = 0, weight = 0,height = 0): #, calculate_BMI):
        #weight is in kg, height in m
        print("weight in kg, height in metre")
        self.age = age
        self.weight = weight
        self.height = height

    def setage(self, age):
        self.age = age

    def setweight(self, weight):
        self.weight = weight

    def getweight(self):
        return self.weight

    def getheight(self):
        return self.height

    def age(self):
        return self.age

    def calculate_BMI(self):
        #to calculate BMI, i need weight and height
        #formular: weight(kg) / (height)^2(m^2)
        calculate_BMI = self.weight / ((self.height)**2)
        return calculate_BMI

    def calculate_calories(self):
        #to calculate calories::::
#formular: BMR * 1.375
# remember i should be able to state excessiveness or less
#where bmr == basal metabolic rate === (diff from male and female)
#saved on desktop ---- bmr.jpg
        gender = input("are you male or female? ")
        if gender.lower() == 'male' or gender.lower() == 'm':
            bmr = (13.75 * self.weight) + (5 * self.height) - (6.76 * self.age) + 66
            calories = bmr * 1.375
            return calories
        if gender.lower() == 'female' or gender.lower() == 'f':
            bmr = (9.56 *self.weight) + (1.85 * self.height) - (4.68 * self.age) + 655
            calories = bmr * 1.375
            return calories

    def calculate_ideal_weight(self):
        # for ideal weight::::
        # diff from male and female
        # https://pubs.asahq.org/anesthesiology/article/127/1/203/18747/Calculating-Ideal-Body-Weight-Keep-It-Simple
        # that site gave an optional method
        gender = input("are you male or female? ")
        if gender.lower() == 'male' or gender.lower() == 'm':
        #using lorentz formula
            ideal_weight = self.height - 100 - ((self.height - 150)/4) #note, height is in cm
            #heigh now in metres
            return ideal_weight
        if gender.lower() == 'female' or gender.lower() == 'f':
            ideal_weight = self.height - 100 - ((self.height - 150)/4)
            return ideal_weight

    def healthy_weigh(self):
        bmi = self.weight / (self.height)**2 #weight in kg, height in metre
        if 0 < bmi < 18.5:
            return ("you are underweight")
        elif 18.5 < bmi < 24.9:
            return ("normal weight")
        elif 24.9 < bmi < 29.9:
            return ('overweight')
        elif 29.9 < bmi < 34.9:
            return ('obesity class 1')
        elif 34.9 < bmi < 39.9:
            return ('obesity class 2')
        elif bmi > 40:
            return ('obesity class 3')