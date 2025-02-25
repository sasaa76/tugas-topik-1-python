class Komputer:
    def __init__(self, merek, tipe):
        self.merek = merek
        self.tipe = tipe
    
    def nyalakan(self):
        print(f"{self.merek} {self.tipe} sekarang menyala")
    
    def matikan(self):
        print(f"{self.merek} {self.tipe} sekarang mati")

komputer1 = Komputer("Lenovo", "ThinkPad")
komputer2 = Komputer("Dell", "XPS")

komputer1.nyalakan()
komputer1.matikan()

komputer2.nyalakan()
komputer2.matikan()