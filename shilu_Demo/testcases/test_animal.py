# -- coding: utf-8 --
# shilutest

class animal:
    name_1 = 'tiger'
    name_2 = 'panda'
    color_1 = "yellow"
    color_2 = "while and black"
    sex_1 = 'male'
    sex_2 = 'female'

    def __init__(self):
        print(self.name_2)

    def willCall(self):
        print("叫的非常凶")

    def willRun(self):
        print('根本跑不动')
        '''父类私有属性'''
    def _willeat(self):
        print('能吃好多东西')


# if __name__ == '__main__':
    # xiongmao = animal()
    # print(f'性别是{xiongmao.sex_2},颜色是{xiongmao.color_2}')
    # xiongmao.willRun()

class Cat(animal):
    hair = 'red'

    def __init__(self):
        self.name_1 = '猫猫'
        print(self.name_1)


    def canCatchMouse(self):
        print("捉老鼠可是一把好手")


    def willCall(self):
        print("喵～喵～的叫")

if __name__ == '__main__':
    bosimao = Cat()
    print(f'毛发是:{bosimao.hair}')
    bosimao.willCall()
