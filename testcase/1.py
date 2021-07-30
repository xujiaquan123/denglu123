class Animal():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(name+age+"你很年轻")

    def ren(self):
        print("不错哦")


if __name__ == '__main__':
    i = Animal("张三","18")
    i.ren()
    print(i)
