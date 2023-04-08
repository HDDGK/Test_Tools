#practise[1]汽车类
class Car:
    rank="原形"
    color="原色"
    brand="杂牌"
    mileage=0
    def __init__(self):
        print("工厂刚产生一辆新车,车型是："+self.rank+"，车色是："+self.color+"，品牌是："+self.brand+"，汽车行驶里程是"+str(self.mileage)+"公里")

    def Getmileage(self):
        return  self.mileage
