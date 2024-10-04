class Father:
    def p(self):
        print("Hey I'm a Father")

class Mother:
    def m(self):
        print("Hey I'm a Mother")

class Child(Father, Mother):
    def c(self):
        print("Hey I'm a child of Mother and Father")

c1 = Child()
c1.p()
c1.m()
c1.c()



