from datetime import datetime
from prettytable import PrettyTable

print(f"{'='*50} DATA PEMINJAMAN BUKU PERPUSTAKAAN{'='*50}")

# Existing Data
data_peminjaman = [
    {"id": "0001", "nama_peminjam": "Anna", "judul_buku": "Diary of a Wimpy Kid", "tanggal_pinjam": "01-09-2024", "tanggal_kembali": "08-09-2024"},
    {"id": "0002", "nama_peminjam": "Budi", "judul_buku": "Yellowface", "tanggal_pinjam": "02-09-2024", "tanggal_kembali": "09-09-2024"},
    {"id": "0003", "nama_peminjam": "Charlie", "judul_buku": "Moby Dick", "tanggal_pinjam": "03-09-2024", "tanggal_kembali": "10-09-2024"}
]

# Fungsi untuk validasi tanggal
def validasi_tanggal(tanggal_str):
    try:
        tanggal = datetime.strptime(tanggal_str, "%d-%m-%Y")
        return tanggal
    except ValueError:
        return None

# Fungsi untuk menampilkan tabel data
def tampilkan_data(data):
    if not data:
        print("\nTidak ada data yang tersedia.")
        return

    table = PrettyTable()
    table.field_names = ["ID", "Nama Peminjam", "Judul Buku", "Tanggal Pinjam", "Tanggal Kembali"]

    for item in data:
        table.add_row([item['id'], item['nama_peminjam'], item['judul_buku'], item['tanggal_pinjam'], item['tanggal_kembali']])

    print(table)

# Fungsi untuk generate ID otomatis
def generate_id():
    if data_peminjaman:
        # Ambil ID terakhir, konversi ke integer dan tambahkan 1
        last_id = int(data_peminjaman[-1]['id'])
        new_id = last_id + 1
    else:
        # Jika belum ada data, ID pertama adalah 0001
        new_id = 1

    # Kembalikan ID dalam format 4 digit
    return str(new_id).zfill(4)

# Fungsi untuk menambahkan data
def tambah_data():
    print("\nTambah Data Peminjaman Buku")
    
    # Generate ID secara otomatis
    id_peminjam = generate_id()
    print(f"ID Peminjam yang di-generate: {id_peminjam}")

    nama_peminjam = input("Masukkan Nama Peminjam: ").title()  # Mengubah input menjadi format title case
    judul_buku = input("Masukkan Judul Buku: ").title()  # Mengubah input menjadi format title case

    # Validasi tanggal pinjam
    while True:
        tanggal_pinjam = input("Masukkan Tanggal Pinjam (DD-MM-YYYY): ")
        if validasi_tanggal(tanggal_pinjam):
            break
        else:
            print("Format atau tanggal tidak valid. Harap masukkan dalam format DD-MM-YYYY.")

    # Validasi tanggal kembali
    while True:
        tanggal_kembali = input("Masukkan Tanggal Kembali (DD-MM-YYYY): ")
        if validasi_tanggal(tanggal_kembali):
            break
        else:
            print("Format atau tanggal tidak valid. Harap masukkan dalam format DD-MM-YYYY.")

    # Tampilkan kembali data yang ingin ditambahkan untuk konfirmasi
    print("\nData yang akan ditambahkan:")
    print(f"ID: {id_peminjam}\nNama: {nama_peminjam}\nJudul Buku: {judul_buku}\nTanggal Pinjam: {tanggal_pinjam}\nTanggal Kembali: {tanggal_kembali}")
    
    konfirmasi = input("Apakah data ini benar? (ya/tidak): ").lower()
    
    if konfirmasi == "ya":
        # Tambah ke list
        data_peminjaman.append({
            "id": id_peminjam,
            "nama_peminjam": nama_peminjam,
            "judul_buku": judul_buku,
            "tanggal_pinjam": tanggal_pinjam,
            "tanggal_kembali": tanggal_kembali
        })
        print("Data berhasil ditambahkan!\n")
    else:
        print("Penambahan data dibatalkan.\n")

# Fungsi untuk mengubah data
def ubah_data():
    print("\nUbah Data Peminjaman Buku")
    id_peminjam = input("Masukkan ID Peminjam yang akan diubah: ")

    # Cari data berdasarkan ID
    for item in data_peminjaman:
        if item['id'] == id_peminjam:
            print("Data ditemukan. Pilih kolom yang akan diubah:")
            print("1. Nama Peminjam")
            print("2. Judul Buku")
            print("3. Tanggal Pinjam")
            print("4. Tanggal Kembali")

            pilihan = input("Pilih kolom (1-4): ")
            data_sebelum = item.copy()  # Salin data sebelum perubahan untuk ditampilkan

            if pilihan == "1":
                item['nama_peminjam'] = input("Masukkan Nama Peminjam baru: ").title()  # title case
            elif pilihan == "2":
                item['judul_buku'] = input("Masukkan Judul Buku baru: ").title()  # title case
            elif pilihan == "3":
                while True:
                    tanggal_pinjam_baru = input("Masukkan Tanggal Pinjam baru (DD-MM-YYYY): ")
                    if validasi_tanggal(tanggal_pinjam_baru):
                        item['tanggal_pinjam'] = tanggal_pinjam_baru
                        break
                    else:
                        print("Format atau tanggal tidak valid.")
            elif pilihan == "4":
                while True:
                    tanggal_kembali_baru = input("Masukkan Tanggal Kembali baru (DD-MM-YYYY): ")
                    if validasi_tanggal(tanggal_kembali_baru):
                        item['tanggal_kembali'] = tanggal_kembali_baru
                        break
                    else:
                        print("Format atau tanggal tidak valid.")
            else:
                print("Pilihan tidak valid.")
                return
            
            # Tampilkan data sebelum dan sesudah perubahan untuk konfirmasi
            print("\nData Sebelum:")
            tampilkan_data([data_sebelum])
            print("Data Sesudah:")
            tampilkan_data([item])

            konfirmasi = input("Apakah perubahan ini benar? (ya/tidak): ").lower()
            if konfirmasi == "ya":
                print("Data berhasil diubah!\n")
            else:
                item.update(data_sebelum)  # Batalkan perubahan
                print("Perubahan data dibatalkan.\n")
            return

    print("Data tidak ditemukan.\n")

# Fungsi untuk menghapus data
def hapus_data():
    print("\nHapus Data Peminjaman Buku")
    id_peminjam = input("Masukkan ID Peminjam yang akan dihapus: ")

    for item in data_peminjaman:
        if item['id'] == id_peminjam:
            print("\nData yang akan dihapus:")
            tampilkan_data([item])
            
            konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (ya/tidak): ").lower()
            if konfirmasi == "ya":
                data_peminjaman.remove(item)
                print("Data berhasil dihapus!\n")
            else:
                print("Penghapusan data dibatalkan.\n")
            return

    print("Data tidak ditemukan.\n")

# Menu utama
def main_menu():
    while True:
        print("\nMenu Peminjaman Buku:")
        print("1. Tambah Data Peminjaman")
        print("2. Tampilkan Data Peminjaman")
        print("3. Ubah Data Peminjaman")
        print("4. Hapus Data Peminjaman")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            print("\nTampilkan Data:")
            print("1. Tampilkan Semua Data")
            print("2. Tampilkan Data Tertentu")

            submenu_pilihan = input("Pilih submenu (1-2): ")

            if submenu_pilihan == "1":
                tampilkan_data(data_peminjaman)
            elif submenu_pilihan == "2":
                id_peminjam = input("Masukkan ID Peminjam: ")
                data_tertentu = [item for item in data_peminjaman if item['id'] == id_peminjam]
                tampilkan_data(data_tertentu)
            else:
                print("Pilihan submenu tidak valid.")
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("Terima kasih! Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Menjalankan program
main_menu()