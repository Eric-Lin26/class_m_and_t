from abc import ABCMeta, abstractmethod # 抽象類別模組
import random

class Menberdata(metaclass=ABCMeta): # 括弧中使用抽象類別模組
    def __init__(self): # 初始化
        self.employee() #執行 class裡的employee函式
    
    @abstractmethod
    def showid():
        pass
    
    def employee(self, name="", age=0):
        print("歡迎進入，新進員工資料系統。")
        self.name = name = input("請輸入名字：")
        self.age = age = int(input("請輸入年齡："))
        self.mid = mid = random.randint(1, 3000)
        print("歡迎你/妳", name)
    
class Manager(Menberdata):
    def __init__(self):
        super().employee()
        self.showid()
        self.salary_Man()
    
    def showid(self):
        print("您的員工ID是：", self.mid)
    
    def salary_Man(self, mon=45000, bonus=3000):
        print("薪資查詢系統")
        print("您當月的薪水是：", mon, "當月的獎金：" , bonus)
        print("一共為：", mon + bonus)

class Teacher(Menberdata):
    def __init__(self):
        super().employee()
        self.showid()
        self.salary_Tec()
    
    def showid(self):
        print("您的員工ID是：", self.mid)

    def salary_Tec(self, mon=40000, bonus=2000):
        print("薪資查詢系統")
        print("您當月的薪水是：", mon, "當月的獎金：" , bonus)
        print("一共為：", mon + bonus)


eric = Manager()
iris = Teacher()
print(iris)
