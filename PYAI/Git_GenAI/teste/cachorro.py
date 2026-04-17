class Cachorro:
    def __init__(self, raca = "vira-latas"):
        self.raca = raca


cao = Cachorro()
print(cao.raca)
cao2 = Cachorro("labrador")
print(cao2.raca)