class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        cars = {
            1: 'self.big',
            2: 'self.medium',
            3: 'self.small'
        }
        if cars[carType] == 'self.big' and self.big > 0:
            self.big -= 1
            return True
        elif cars[carType] == 'self.medium' and self.medium > 0:
            self.medium -= 1
            return True
        elif cars[carType] == 'self.small' and self.small > 0:
            self.small -= 1
            return True
        return False



# Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(450, 892, 488)
param_1 = obj.addCar(1)
param_2 = obj.addCar(2)
param_3 = obj.addCar(3)

print(param_1,param_2, param_3)
