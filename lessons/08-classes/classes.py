class Car:
    brand: str
    model: str
    is_driving: bool

    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model
        self.is_driving = False

    def drive(self):
        print('Printed from instance: ', self)
        # print(f'{self.brand}, model {self.model} is DRIVING!')

    def stop_driving(self):
        self.is_driving = False
        print(f'{self.brand}, model {self.model} is STOPPED!')

    @classmethod
    def new_ford(cls, model: str) -> "Car":
        print('Printed from classmethod: ', cls)
        return Car('Ford', model)
