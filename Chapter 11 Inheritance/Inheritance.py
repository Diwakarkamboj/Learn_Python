class EMP:

    def Parents(self,property, mrg):
        if(mrg.lower() == "arrange"):
            print(f"I'll give you all property on {mrg} marrige, {property}")
            print("Gold and Diamonds and Plane")
        else:
            print(f"No {property} for you if you do {mrg} marrige")


class CHILD(EMP):
    child_pro = "Money"
    def Child(self,mrg):
        print(f"Child Says: I've, {self.child_pro} only and I'll do {mrg} marrige")


# obj = EMP()
Child_obj = CHILD()
Child_obj.Child("arrange")
Child_obj.Parents("++++ Property", "arrange")