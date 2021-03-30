

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
        #https://isolatorfitness.com/blogs/iso/basal-metabolic-rate-calculator-what-does-it-mean
    #where bmr == basal metabolic rate === (diff from male and female)
    #saved on desktop ---- bmr.jpg

        #using mifflin st. jeor equation
        gender = input("are you male or female? ")
        if gender.lower() == 'male' or gender.lower() == 'm':
            bmr = (10 * self.weight) + (0.625 * self.height) - (5 * self.age) + 5
            calories = bmr * 1.375
            return calories
        if gender.lower() == 'female' or gender.lower() == 'f':
            bmr = (10 * self.weight) + (0.625 * self.height) - (5 * self.age) - 161
            calories = bmr * 1.375
            return calories

    def calculate_ideal_weight(self):
        #https://www.gigacalculator.com/calculators/ideal-weight-calculator.php
        #https://www.semanticscholar.org/paper/Universal-equation-for-estimating-ideal-body-weight-Peterson-Thomas/8613f2d265d9f314b7be312f27792961daa263a8/figure/3

        #using peterson formula. No need for gender
        BMI = self.weight / ((self.height)**2)
        ideal_weight = 2.2 * BMI + 3.5 * BMI * (self.height - 1.5 )
        #agrees with this site:
        # https://www.gigacalculator.com/calculators/ideal-weight-calculator.php
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