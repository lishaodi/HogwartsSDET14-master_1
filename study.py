


#组合举例
class Turtle:
    def __init__(self, x):
        self.num = x
class Fish:
    def __init__(self, x):
        self.num = x
class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def number(self):
        print("水池里总共%s只乌龟，共%s条鱼" % (self.turtle.num, self.fish.num))

c=Pool(5,10)
c.number()

#python设计模式一 单例模式
# 通过改写__new__函数来实现单例模式
class A():
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = object.__new__(cls)
            return cls._instance
        else:
            return cls._instance
    def a(self):
        pass
a=A()
print(id(a))
b=A()
print(id(b))

#python设计模式二
#依赖倒置原则  ------抽象基类  "https://blog.csdn.net/ruguowoshiyu/article/details/81177852"

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
a,b,c,d = data
print(a,b,c,d)
print(type(d))
