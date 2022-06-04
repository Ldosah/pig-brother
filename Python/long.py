class hanjian:
    def run(self, c, name):
        print("跑喽")
        c.house(name)


class guojia:
    huji = "中国"

    def __init__(self, dream):
        self.huji = dream

    def house(self, name):
        print("%s完美的国家！" % (name))


person = hanjian()
dream = input("请输入你梦想移民的国家\n")
U = guojia(dream)
person.run(U, U.huji)