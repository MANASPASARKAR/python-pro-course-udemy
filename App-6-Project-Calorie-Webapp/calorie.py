from temperature import Temperature

class Calorie:

    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.age = age
        self.height = height
        self.weight = weight

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 * self.age - float(self.temperature) * 10
        return result

if __name__ == "__main__":
    temp = Temperature(city='Pune', country='India').get()
    calorie = Calorie(weight=75, height=172, age=17, temperature=temp)
    print(calorie.calculate())