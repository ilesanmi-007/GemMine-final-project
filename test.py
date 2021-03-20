from Person import Person
from ATM import ATM

bola = Person()
bola.height = 2.45
bola.weight = 25
bola.age = 19

#print(bola.calculate_BMI())
#print(bola.calculate_calories()) #khvmv,v
print(bola.healthy_weigh())
#print(bola.calculate_ideal_weight()) #ljkgljlk

me = ATM()
me.check_balance()
me.add_money(300)
me.check_balance()
me.withraw(400)
me.check_balance()
