class Sweet:

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Sweet()
e.name = "Diwakar Kamboj"
print(f"{e.fname} {e.lname}")
