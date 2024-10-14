admin = ({"username" : "shafa", "password": "123", "role" : "admin" })

from prettytable import PrettyTable

kamera = []
transaksi = []

def lihat_kamera():
    if not kamera:
        print("Tidak ada kamera yang tersedia")
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama Kamera", "Jumlah Kamera", "Harga Sewa per Hari"]
        for idx, k in enumerate(kamera, 1):
            table.add_row([idx, k['nama'], k['jumlah'], k['harga']])
        print(table)

def tambah_kamera(nama, jumlah, harga):
    kamera.append({'nama': nama, 'jumlah': jumlah, 'harga': harga})
    print(f"Kamera {nama} telah ditambahkan")

def hapus_kamera(nama):
    for k in kamera:
        if k['nama'] == nama:
            kamera.remove(k)
            print(f"Kamera {nama} telah dihapus")
            return
    print(f"Kamera {nama} tidak tersedia")

def pesan_kamera(nama, jumlah, jumlah_hari):
    for k in kamera:
        if k['nama'] == nama:
            if k['jumlah'] >= jumlah:
                total_harga = k['harga'] * jumlah * jumlah_hari
                k['jumlah'] -= jumlah
                transaksi.append({'nama': k['nama'], 'jumlah': jumlah, 'hari': jumlah_hari, 'total': total_harga})
                tambah_fotografer = (input("Apakah anda ingin menyewa fotografer juga? (ya/tidak):"))
                if tambah_fotografer == "ya":
                    harga_total_fotografer = total_harga + (jumlah_hari * 500000) 
                    print(f"Fotografer dan kamera {nama} berhasil dipesan sebanyak {jumlah} kamera selama {jumlah_hari} hari. Total harga yang harus dibayar: {harga_total_fotografer}")
                else:
                    print(f"Kamera {nama} berhasil dipesan sebanyak {jumlah} kamera selama {jumlah_hari} hari. Total harga yang harus dibayar: {total_harga}")
            else:
                print(f"Kamera yang tersedia hanya {k['jumlah']}, tidak cukup untuk pesanan Anda.")
            return 
    print(f"Kamera {nama} tidak tersedia")

def kembalikan_kamera(nama, jumlah):
    for trans in transaksi:
        if trans['nama'] == nama and trans['jumlah'] >= jumlah:
            trans['jumlah'] -= jumlah
            for k in kamera:
                if k['nama'] == nama:
                    k['jumlah'] += jumlah
                    print(f"Kamera {nama} berhasil dikembalikan sebanyak {jumlah}.")
                    return
    print(f"Kamera {nama} gagal dikembalikan. Pastikan ulang jumlah yang dikembalikan benar")

def register(pengguna, password, level):
    return {'username': pengguna, 'password': password, 'level': level}

def login(username, password, pengguna):
    for user in pengguna:
        if user['username'] == username and user['password'] == password:
            return user['level']
    return None

def main():

    pengguna = []
    
    while True:
        print("Selamat Datang di Jasa Penyewaan Kamera dan Fotografer \nSilahkan pilih menu di bawah ini")
        print("1. Register")
        print("2. Login")
        pilihan = input("Masukkan pilihan (1/2):")

        if pilihan == '1':
            print("\nSilahkan melakukan registrasi")
            username = input("Username: ")
            password = input("Password: ")
            level = input("Anda login sebagai apa? (admin/user): ")

            if level in ['admin', 'user']:
                pengguna.append(register(username, password, level))
                print("Registrasi berhasil")
            else:
                print("Role salah. Pilih 'admin' atau 'user'.")

        elif pilihan == '2':
            print("\nSilahkan melakukan login")
            username = input("Username:")
            password = input("Password:")

            if username == "shafa" and password == "123":
                level = 'admin'
            else:
                level = login(username, password, pengguna)

            if level == 'admin':
                while True:
                    print("\nSelamat Datang Admin!")
                    print("1. Tambah Kamera")
                    print("2. Hapus Kamera")
                    print("3. Lihat Kamera")
                    print("4. Logout")
                    admin_pilihan = input("Pilih aksi (1/2/3/4): ")
                    if admin_pilihan == '1':
                        nama = input("Masukkan nama kamera: ")
                        jumlah = int(input("Masukkan jumlah kamera: "))
                        harga = float(input("Masukkan harga sewa per hari: "))
                        tambah_kamera(nama, jumlah, harga)
                    elif admin_pilihan == '2':
                        nama = input("Nama kamera yang ingin anda hapus: ")
                        hapus_kamera(nama)
                    elif admin_pilihan == '3':
                        lihat_kamera()
                    elif admin_pilihan == '4':
                        break
                    else:
                        print("Pilihan tidak tersedia")

            elif level == 'user':
                while True:
                    print("\nSelamat datang pelanggan!")
                    print("1. Lihat Kamera")
                    print("2. Pesan Kamera")
                    print("3. Kembalikan Kamera")
                    print("4. Logout")
                    user_pilihan = input("Masukkan pilihan (1/2/3/4):")
                    if user_pilihan == '1':
                        lihat_kamera()
                    elif user_pilihan == '2':
                        nama = input("Masukkan nama kamera yang ingin dipesan:")
                        jumlah = int(input("Masukkan jumlah kamera: "))
                        jumlah_hari = int(input("Masukkan jumlah hari sewa:"))
                        pesan_kamera(nama, jumlah, jumlah_hari)
                    elif user_pilihan == '3':
                        nama = input("Masukkan nama kamera yang ingin dikembalikan: ")
                        jumlah = int(input("Masukkan jumlah kamera yang ingin dikembalikan: "))
                        kembalikan_kamera(nama, jumlah)
                    elif user_pilihan == '4':
                        print("Terimakasih telah mengunjungi Jasa Penyewaan Kamera dan Fotografer")
                        break
                    else:
                        print("Pilihan tidak tersedia")

        else:
            print("Pilihan salah, silahkan coba lagi")

if __name__ == "__main__":
    main()
