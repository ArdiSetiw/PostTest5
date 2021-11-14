import secrets as gaca
from typing import Counter


data = {
    "Food":{"Ayam Geprek":20000,"Nasi":6969},
    "Drink":{"Tea":3000,"Kopi":5000,"Air":3000}
}
food_cart = []
food_price = []
drink_cart = []
drink_price = []
def show_menu () :
    makanan = data["Food"]
    print("> Menu Makanan")
    for nama, harga in makanan.items() :
        print(" -",nama,"=",harga)
    print("-"*57)
    minuman = data["Drink"]
    print("> Menu Minuman")
    for nama, harga in minuman.items() :
        print(" -",nama,"=",harga)
def add_menu () :
    show_menu()
    add = True
    while add :
        print("-"*57)
        print("Pilihan Menambah Menu\n[1]. Makanan\n[2]. Minuman")
        choice = str(input("Masukkan Pilihan = "))
        print("="*57)
        if choice == "1" :
            try :
                makanan = str(input("Tambah Makanan = "))
                harga_makanan = int(input("Harga Makanan = "))
                print("="*57)
                data["Food"][makanan] = harga_makanan
                print("MENU TELAH DITAMBAH")
            except ValueError :
                print("="*57)
                print("Harga Harus Berbentuk Angka Desimal !")
        elif choice == "2" :
            try :
                minuman = str(input("Tambah Minuman = "))
                harga_minuman = int(input("Harga Minuman = "))
                print("="*57)
                data["Drink"][minuman] = harga_minuman
                print("MENU TELAH DITAMBAH")
            except ValueError :
                print("="*57)
                print("Harga Harus Berbentuk Angka Desimal !")
        else : 
            print("Mohon Pilih Dengan Angka Yang Tertera")
        print("="*57)
        show_menu()
        print("="*57)
        print("Lanjut Menambah\n[1]. Ya\n[2]. Tidak")
        pilih = str(input("Masukkan Pilih = "))
        print("="*57)
        if pilih == "1" :
            continue
        elif pilih == "2":
            add = False
        else :
            print("Mohon Pilih Dengan Angka Yang Tertera")
        print("="*57)
def edit_menu() :
    show_menu()
    print("="*57)
    edit = True
    while edit :
        print("Pilihan Edit Menu\n[1]. Makanan\n[2]. Minuman")
        choice = str(input("Pilihan = "))
        print("="*57)
        if choice == "1" :
            makanan = data["Food"]
            akses = str(input("Menu Makanan Yang Diupdate = "))
            print("-"*57)
            try :
                if akses in makanan.keys() :
                    ganti = str(input("Update Nama Makanan = "))
                    harga = int(input("Update Harga Makanan = "))
                    makanan.pop(akses)
                    makanan.update({ganti:harga})
                    print("="*57)
                    print("MENU TELAH DIUPDATE")
                    print("="*57)
                else :
                    print("="*57)
                    print("Makanan Tidak Ada Dalam Menu !")
                    print("="*57)
            except ValueError :
                print("="*57)
                print("Harga Harus Berbentuk Angka Desimal !")
                print("="*57)
        elif choice == "2" :
            minuman = data["Drink"]
            akses = str(input("Menu Minuman Yang Diupdate = "))
            print("-"*57)
            try :
                if akses in minuman.keys() :
                    ganti = str(input("Update Nama Minuman = "))
                    harga = int(input("Update Harga Minuman = "))
                    minuman.pop(akses)
                    minuman.update({ganti:harga})
                    print("="*57)
                    print("MENU TELAH DIUPDATE")
                    data["Drink"] = minuman
                else :
                    print("="*57)
                    print("Minuman Tidak Ada Dalam Menu !")
                    print("="*57)
            except ValueError :
                print("="*57)
                print("Harga Harus Berbentuk Angka Desimal !")
                print("="*57)
        else :
            print("Mohon Pilih Dengan Angka Yang Tertera")
        print("="*57)
        show_menu()
        print("="*57)
        print("Lanjut Mengupdate\n[1]. Ya\n[2]. Tidak")
        pilih = str(input("Masukkan Pilih = "))
        print("="*57)
        if pilih == "1" :
            continue
        elif pilih == "2":
            edit = False
        else :
            print("Mohon Pilih Dengan Angka Yang Tertera")
        print("="*57)
def delete_menu ():
    show_menu()
    print("="*57)
    edit = True
    while edit :
        print("Pilihan Hapus Menu\n[1]. Makanan\n[2]. Minuman")
        choice = str(input("Pilihan = "))
        print("="*57)
        if choice == "1" :
            makanan = data["Food"]
            hapus = str(input("Hapus Menu Makanan = "))
            print("="*57)
            if hapus in makanan.keys() :
                del makanan[hapus]
                print("MENU TELAH DIHAPUS")
            else :
                print("Makanan Tidak Ada Dalam Menu !")
        elif choice == "2" :
            minuman = data["Drink"]
            hapus = str(input("Hapus Menu Minuman = "))
            print("="*57)
            if hapus in minuman.keys() :
                del minuman[hapus]
                print("MENU TELAH DIHAPUS")
            else :
                print("Minuman Tidak Ada Dalam Menu !")
        else :
            print("Mohon Pilih Dengan Angka Yang Tertera")
        print("="*57)
        show_menu()
        print("="*57)
        print("Lanjut Menghapus\n[1]. Ya\n[2]. Tidak")
        pilih = str(input("Masukkan Pilih = "))
        print("="*57)
        if pilih == "1" :
            continue
        elif pilih == "2":
            edit = False
        else :
            print("Mohon Pilih Dengan Angka Yang Tertera")
        print("="*57)
def payment ():
    show_menu()
    # Order Makanan
    print("="*57)
    print("                   > Memesan Makanan <")
    print("> Ketik pesanan sesuai yang tertera di menu")
    print("> Ketik 'end' untuk berhenti memesan")
    order_food = True 
    while order_food :
        makanan = data["Food"]
        pesan = str(input("Pesan Makanan = "))
        if pesan in makanan.keys() :
            food_cart.append(pesan)
        elif pesan == "end" or pesan == "End":
            order_food = False
        else :
            print("-"*57)
            print("Pesanan Tidak Ada Dalam Menu !")
            print("-"*57)
    for items in food_cart :
        hitung = Counter(makanan)
        food_price.append(hitung[items])
        bayar_food = sum(food_price)
    # Order Minuman
    print("="*57)
    print("                   > Memesan Minuman <")
    print("> Ketik pesanan sesuai yang tertera di menu")
    print("> Ketik 'end' untuk berhenti memesan")
    order_drink = True
    while order_drink :
        minuman = data["Drink"]
        pesan2 = str(input("Pesan Minuman = "))
        if pesan2 in minuman.keys() :
            drink_cart.append(pesan2)
        elif pesan2 == "end" or pesan2 == "End" :
            print("="*57)
            order_drink = False
        else :
            print("-"*57)
            print("Pesanan Tidak Ada Dalam Menu !")
            print("-"*57)
    for items in drink_cart :
        hitung2 = Counter(minuman)
        drink_price.append(hitung2[items])
        bayar_drink = sum(drink_price)
    # Diskon Makanan
    if len(food_cart) > 0 :
        if len(food_cart) >= 2 :
            print("="*57)
            print("-> Pesanan Makanan Anda")
            for p,q in zip (food_cart,food_price) :
                print("-",p,"   = Rp",q,)
            print("Total Harga Makanan = Rp",bayar_food)
            print("| Anda dapat 5% Diskon karena membeli setidaknya 2 Makanan")
            bayar_food = bayar_food - (bayar_food*5/100)
            print("Total Harga Makanan = Rp",bayar_food)
        else :
            print("="*57)
            print("-> Ini Pesanan Makanan Anda")
            for x,y in zip (food_cart,food_price):
                print("-",x,"= Rp",y)
            print("Total Harga Makanan = Rp",bayar_food)
    else :
        bayar_food = 0
        print("-"*57)
        print("Anda Tidak Memesan Makanan")
        print("-"*57)
    # Diskon Minuman
    if len(drink_cart) > 0 :
        if len(drink_cart) >= 3 :
            print("="*57)
            print("-> Pesanan Minuman Anda")
            for r,s in zip (drink_cart,drink_price) :
                print("-",r,"   = Rp",s,)
            print("Total Harga Minuman = Rp",bayar_drink)
            print("| Anda dapat 10% Diskon karena membeli setidaknya 3 Minuman")
            bayar_drink = bayar_drink - (bayar_drink*10/100)
            print("Total Harga Minuman = Rp",bayar_drink)
        else :
            print("="*57)
            print("-> Ini Pesanan Minuman Anda")
            for x,y in zip (drink_cart,drink_price):
                print("-",x,"= Rp",y)
            print("Total Harga Minuman = Rp",bayar_drink)
    else :
        bayar_drink = 0
        print("-"*57)
        print("Anda Tidak Memesan Minuman")
        print("-"*57)
    total_bayar = bayar_food + bayar_drink
    if total_bayar == 0 :
        print("="*57)
        print("Anda Tidak Memesan Apapun :)")
        print("="*57)
    else :
        print("="*57)
        print("Harga Makanan dan Minuman = Rp",total_bayar)
        print("="*57)
        # Diskon Hari
        # Hari beli 
        day = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
        hari = gaca.choice(day)
        print("\033[32m          Anda Memesan Pesanan Ini Pada",hari,"\033[39m")
        print("="*57)
        if hari == "Sabtu" or hari == "Minggu" :
                print("Karena Anda memesan ini di hari",hari,"Anda mendapatkan 5% Diskon")
                total_bayar = total_bayar - (total_bayar * 5/100)
                print("Harga Setelah Diskon = Rp",total_bayar)
        else :
                print("Karena Anda memesan ini di hari",hari,"Anda mendapatkan 10% Diskon")
                total_bayar = total_bayar - (total_bayar * 10/100)
                print("Harga Setelah Diskon = Rp",total_bayar)
        # Pembayaran and The End of the program
        print("="*57)
        print("""Pilih Pembayaran
            1. Cash
            2. CC Card
            3. eMoney""")
        print("="*57)
        bayar = str(input("Pembayaran = "))
        if bayar == "3" :
                print("Pembayaran eMoney, Anda mendapatkan 5% Diskon")
                total_bayar = total_bayar - (total_bayar * 5/100)
                print("Total Harga = Rp",total_bayar)
                print("="*57)
        else : 
                print("Total Harga = Rp",total_bayar)
                print("="*57)
def process ():
    proses = True
    while proses :
        print("""---------------------Pilihan Program---------------------
        [1]. Tambah Menu
        [2]. Lihat Menu
        [3]. Update Menu
        [4]. Hapus Menu
        [5]. Pesan Makanan dan Minuman 
        [0]. Keluar
        """)   
        choice = str(input("Pilih = "))
        print("="*57)
        if choice == "1" :
            add_menu()
        elif choice == "2":
            show_menu()
        elif choice == "3":
            edit_menu()
        elif choice == "4":
            delete_menu()
        elif choice == "5":
            payment()
        elif choice == "0":
            print("Program Berhenti")
            proses = False
        else :
            print("Pilih Dengan Angka Yang Tertera")
process()
