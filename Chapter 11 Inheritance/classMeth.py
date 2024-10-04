class Me:
    a = 1

    @classmethod
    def chk(cls):
        return cls.a
        # print(f"Class attribute is {cls.a}") 

b = Me()
b.a = 44
print(b.chk())