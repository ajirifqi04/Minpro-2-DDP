from prettytable import PrettyTable

akun = {
    "manager": {"username": "Aji", "password": "123", "role": "Admin"},
    "karyawan": {"username": "Rifqi", "password": "456", "role": "User"}
}

peralatan = [
    ["Tenda", 4],
    ["Sleeping Bag", 9],
    ["Kompor Portable", 7],
    ["Tas Besar", 5],
    ["Jaket Gunung", 10]
]

menu_manager = {
    1: "Menampilkan Daftar List Peralatan",
    2: "Menambah Peralatan",
    3: "Menghapus Peralatan",
    4: "Mengambil Peralatan",
    5: "Keluar"
}

menu_karyawan = {
    1: "Menampilkan Daftar List Peralatan",
    2: "Mengambil Peralatan",
    3: "Keluar"
}

def display_menu(menu):
    print("================================================")
    print("   Sistem Manajemen Peralatan Mendaki Gunung")
    print("================================================")
    for key, value in menu.items():
        print(f"{key}. {value}")

def view_equipment():
        table = PrettyTable()
        table.field_names = ["Nama Peralatan", "Jumlah"]

        for item in peralatan:
            table.add_row(item)

        print(table)

def add_equipment():
    while True:  
        try:
            tambah = input("Masukkan nama peralatan yang ingin ditambahkan: ")
            if tambah == "":  
                raise ValueError("Nama peralatan tidak boleh kosong!")

            while True:
                try:
                    jumlah = input("Masukkan jumlah peralatan: ")
                    if jumlah == "":  
                        raise ValueError("Jumlah tidak boleh kosong!")

                    if int(jumlah) <= 0:
                        raise ValueError("Jumlah harus lebih dari 0!")
                    break  

                except ValueError:
                    print("PERINGATAN: Jumlah harus berupa angka dan lebih dari 0!")

            peralatan.append([tambah, int(jumlah)])
            print("Peralatan berhasil ditambahkan") 
            view_equipment()
            break  

        except ValueError as e:
            print("PERINGATAN:", e)

def delete_equipment():
    while True:
        try:
            hapus = input("Masukkan nama peralatan yang ingin dihapus: ")
            if hapus == "":
                raise ValueError("Nama peralatan tidak boleh kosong!")
            
            for item in peralatan:
                if item[0] == hapus:   
                    peralatan.remove(item)
                    print(f"{hapus} berhasil dihapus")
                    view_equipment()
                    return
                
                else:
                    print("Peralatan tidak ditemukan")
                    view_equipment()
                    break
        
        except ValueError as e:
            print("PERINGATAN:", e)

def pick_equipment():
    while True:
        try:
            nama = input("Masukkan nama peralatan yang ingin diambil: ")
            if nama == "":
                raise ValueError("Nama peralatan tidak boleh kosong!")
            
            for item in peralatan:
                if item[0] == nama:
                    while True:  
                        try:
                            jumlah = int(input("Masukkan jumlah peralatan: "))
                            if jumlah <= item[1]:  
                                item[1] -= jumlah
                                print(f"Berhasil mengambil {jumlah} {nama}")
                                if item[1] == 0:
                                    peralatan.remove(item)
                                view_equipment()
                                return  
                            else:
                                print("Jumlah melebihi stok yang tersedia!")
                                
                        except ValueError:
                            print("Jumlah harus berupa angka!")  
                            continue
            print("Peralatan tidak ditemukan")
            return
        
        except ValueError as e:
            print("PERINGATAN:", e)

def menu_utama(role):
    if role == "Admin":
        while True:
            try:
                display_menu(menu_manager)
                pilihan = int(input("Masukkan pilihan (1-5): "))

                if pilihan == 1:
                    view_equipment()
                elif pilihan == 2:
                    add_equipment()
                elif pilihan == 3:
                    delete_equipment()
                elif pilihan == 4:
                    pick_equipment()
                elif pilihan == 5:
                    print("Keluar dari program...")
                    break
                else:
                    print("Pilihan tidak valid!")
            except ValueError:
                print("Input harus berupa angka!")

    elif role == "User":
        while True:
            try:
                display_menu(menu_karyawan)
                pilihan = int(input("Masukkan pilihan (1-3): "))

                if pilihan == 1:
                    view_equipment()
                elif pilihan == 2:
                    pick_equipment()
                elif pilihan == 3:
                    print("Keluar dari program...")
                    break
                else:
                    print("Pilihan tidak valid, coba lagi!")
            except ValueError:
                print("Input harus berupa angka!")

import pwinput  

def login():
    while True:
        try:
            username = input("Masukkan username: ")
            if username == "":
                raise ValueError("Username tidak boleh kosong!")

            while True:
                try:
                    password = pwinput.pwinput("Masukkan password: ")
                    if password == "":
                        raise ValueError("Password tidak boleh kosong!")
                    break  
                except ValueError as e:
                    print("PERINGATAN:", e)

            for data in akun.values():
                if username == data["username"] and password == data["password"]:
                    print(f"Login berhasil sebagai {data['role']}. Selamat datang, {username}")
                    menu_utama(data["role"])
                    return

            print("Login gagal! Username atau password salah.")

        except ValueError as e:
            print("PERINGATAN:", e)



login()
