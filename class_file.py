
class Car:
    car_dict = {}
    def __init__(self,model,company,year):
        self.model = model
        self.company = company
        self.year = year
        Car.car_dict[self.model] = {'company':self.company,'year':self.year}