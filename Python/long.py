class hanjian:
    def run(self, c, name):
        c.house(name)
        print("跑喽")


class guojia:
    huji = "中国"

    def __init__(self, dream):
        self.huji = dream

    def house(self, name):
        if name=="中国":
            print("傻逼是吧")
            quit()
        else:
            print("%s完美的国家！" % (name))


person = hanjian()
dream = input("请输入你梦想移民的国家\n")
U = guojia(dream)
person.run(U, U.huji)