class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def keliling (self):
        return 2* (self.panjang + self.lebar)
    
    def luas (self):
        return (self.panjang * self.lebar)
    
    def __str__ (self):
        return f"persegi panjang, panjang {self.panjang}cm , dan lebar {self.lebar} cm"

def main():
    try:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        
        if panjang <= 0 or lebar <= 0:
            print("Nilai harus diatas 0")
            return

        pp = PersegiPanjang(panjang, lebar)
        print(pp)
        print("Kelilingnya: ", pp.keliling(), "cm")
        print("Luasnya: ", pp.luas(), "cm2")
    
    except ValueError:
        print("Nilai harus sesuai")

main()