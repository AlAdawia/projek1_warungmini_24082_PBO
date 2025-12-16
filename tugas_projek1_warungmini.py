
class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga


class Pesanan:
    def __init__(self):
        self.daftar_pesanan = []  

    def tambah_pesanan(self, menu, jumlah):
        self.daftar_pesanan.append((menu, jumlah))

    def hitung_total(self):
        total = 0
        for menu, jumlah in self.daftar_pesanan:
            total += menu.harga * jumlah
        return total

    def tampilkan_pesanan(self):
        print("\n=== DAFTAR PESANAN ===")
        for menu, jumlah in self.daftar_pesanan:
            print(f"{menu.nama} x{jumlah} = Rp{menu.harga * jumlah}")


class Warung:
    def __init__(self):
        self.menu_list = [
            Menu("Nasi Goreng", 15000),
            Menu("Mie Goreng", 15000),
            Menu("Ayam Goreng", 18000),
            Menu("Pentol Kuah", 10000),
            Menu("Es Teh Jeruk", 7000),
            Menu("Pop Ice", 6000)
        ]
        self.pesanan = Pesanan()

    def tampilkan_menu(self):
        print("\n=== MENU WARUNG MINI ===")
        for i, menu in enumerate(self.menu_list, start=1):
            print(f"{i}. {menu.nama} - Rp{menu.harga}")
        print("0. Selesai Pesan")

    def jalankan(self):
        while True:
            self.tampilkan_menu()
            try:
                pilihan = int(input("Pilih menu (angka): "))
            except ValueError:
                print("Input harus angka!")
                continue

            if pilihan == 0:
                break

            if pilihan < 1 or pilihan > len(self.menu_list):
                print("Pilihan tidak valid!")
                continue

            try:
                jumlah = int(input("Jumlah: "))
            except ValueError:
                print("Jumlah harus angka!")
                continue

            menu_dipilih = self.menu_list[pilihan - 1]
            self.pesanan.tambah_pesanan(menu_dipilih, jumlah)
            print(f"{menu_dipilih.nama} x{jumlah} ditambahkan ke pesanan.")

        self.selesai()

    def selesai(self):
        self.pesanan.tampilkan_pesanan()
        total = self.pesanan.hitung_total()
        print(f"\nTotal Bayar: Rp{total}")
        print("Terima kasih sudah memesan di Warung Mini 😊")


if __name__ == "__main__":
    warung = Warung()
    warung.jalankan()




    
