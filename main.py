#7-m
class Ota:
    def __init__(self, ism):
        self.ism = ism
        
    def gapir(self):
        print("Gapirdi")
        
class Ogil(Ota):
    def gapir(self):
        super().gapir()
        print(f"O'g'il gapirdi")
        
    
u1 = Ota("Shokir")
u1.gapir()
