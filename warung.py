import matplotlib.pyplot as plt

# File untuk menyimpan data transaksi
DATA_FILE = "data_transaksi.txt"
DATA_BARANG = "data_barang.txt"

# Inisialisasi data transaksi
def load_data():
    transaksi = []
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                if line.strip():
                    nama_barang, jumlah, harga, total = line.strip().split(",")
                    transaksi.append({
                        "nama_barang": nama_barang,
                        "jumlah": int(jumlah),
                        "harga": int(harga),
                        "total": int(total)
                    })
    except FileNotFoundError:
        pass
    return transaksi

# inisiasi data barang
def load_data_barang():
    barang = []
    try:
        with open(DATA_BARANG, "r") as file:
            for line in file:
                if line.strip():
                    nama_barang, stok , harga = line.strip().split(",")
                    barang.append({
                        "nama_barang": nama_barang,
                        "stok": stok,
                        "harga": int(harga)
                    })
    except FileNotFoundError:
        pass
    return barang

# Simpan data barang
def simpan_data_barang(barang):
    try:
        with open(DATA_BARANG, "w") as file:
            for b in barang:
                file.write(f"{b['nama_barang']},{b['stok']},{b['harga']}\n")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data barang: {e}")
            
# Fungsi untuk menambahkan barang
def tambah_barang(barang):
    try:
        nama_barang = input("Masukkan nama barang: ")
        stok = int(input("Masukkan jumlah stok: "))
        harga = int(input("Masukkan harga: Rp.  "))
        
        barang_baru = {
            "nama_barang": nama_barang,
            "stok": stok,
            "harga": harga
        }
        barang.append(barang_baru)
        simpan_data_barang(barang)
        print("Barang berhasil ditambahkan!")
    except ValueError:
        print("Input salah! Pastikan stok dan harga berupa angka.")
        
# Fungsi untuk menampilkan semua barang
def tampilkan_barang(barang):
    if not barang:
        print("Tidak ada barang.")
        return
    
    print("\n--- Daftar Barang ---")
    for i, b in enumerate(barang, start=1):
        harga_formatted = f"Rp. {b['harga']:,}".replace(',', '.')
        print(f"{i}. {b['nama_barang']} - Stok: {b['stok']}, Harga: {harga_formatted}")
        
# fungsi untuk mengubah data barang
def edit_barang(barang):
    tampilkan_barang(barang)
    if not barang:
        print("Tidak ada barang untuk diubah.")
        return
    
    nama_barang = input("\nMasukan nama barang yang ingin di ubah: ")
    found = False
    
    for b in barang:
        if b["nama_barang"].lower() ==nama_barang.lower():
            found = True
            print(f"\nBarang ditemukan: {b['nama_barang']}. - stok: {b['stok']}, harga: Rp. {b['harga']}")
        
        try:
            new_stok = int(input("Masukkan stok baru (atau tekan Enter untuk tidak mengubah): ") or b['stok'])
            new_harga = int(input("Masukkan harga baru (atau tekan Enter untuk tidak mengubah): Rp. ") or b['harga'])
            
            print("\nPerubahan:")    
            print(f"Stok: {b['stok']} -> {new_stok}")
            print(f"Harga: Rp. {b['harga']:,} -> Rp. {new_harga:,}".replace(',', '.'))
            konfirmasi = input("Apakah Anda yakin ingin menyimpan perubahan ini? (Y/N): ").lower()
            
            if konfirmasi == "y":
                b["stok"] = new_stok
                b["harga"] = new_harga
                simpan_data_barang(barang)
                print("Perubahan berhasil disimpan!")
            else:
                print("Perubahan dibatalkan")
        except ValueError:
            print("Input tidak valid. Pastikan stok dan harga berupa angka")
            
    if not found:
        print("Barang dengan nama tersebut tidak ditemukan.")
                    
        
# fungsi untuk menghapus barang
def hapus_barang(barang):
    tampilkan_barang(barang)
    if not barang:
        print("Tidak ada barang untuk dihapus.")
        return
    
    nama_barang = input("\nMasukkan nama barang yang ingin dihapus: ")
    found = False
    
    for b in barang: 
        if b["nama_barang"].lower() == nama_barang.lower():
            found = True
            print(f"Apakah Anda yakin ingin menghapus barang berikut?")
            print(f"{b['nama_barang']} - Stok: {b['stok']}, Harga: {b['harga']}")
            konfirmasi = input("Ketik 'Y' untuk menghapus atau apa saja untuk membatalkan: ")
            
            if konfirmasi.lower() == 'y':
                barang.remove(b)
                simpan_data_barang(barang)
                print("Barang berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
            break
        
    if not found:
        print("Data dengan nama barang tersebut tidak ditemukan.")
        
# Fungsi untuk menyimpan data transaksi ke file
def simpan_data(transaksi):
    with open(DATA_FILE, "w") as file:
        for t in transaksi:
            file.write(f"{t['nama_barang']},{t['jumlah']},{t['harga']},{t['total']}\n\n")
            
# Fungsi untuk menambahkan transaksi
def tambah_transaksi(transaksi, barang):
    try:
        tampilkan_barang(barang)
        nama_barang = input("\nMasukkan nama barang (pilih dari daftar): ").strip()
        
        barang_terpilih = next((b for b in barang if b['nama_barang'] == nama_barang), None)
        
        if not barang_terpilih:
            print("Barang tidak ditemukan dalam daftar. Transaksi gagal.")
            return
        
        stok_tersedia = int(barang_terpilih['stok'])
        harga = barang_terpilih['harga']
        
        jumlah = int(input("Masukkan jumlah pembelian: "))
        
        if jumlah > stok_tersedia:
            print(f"Stok tidak mencukupi. Stok tersedia: {stok_tersedia}. Transaksi gagal.")
            return
        
        total = jumlah * harga
        
        transaksi_baru = {
            "nama_barang": nama_barang,
            "jumlah": jumlah,
            "harga": harga,
            "total": total
        }
        transaksi.append(transaksi_baru)
        
        # Kurangi stok barang
        barang_terpilih['stok'] = str(stok_tersedia - jumlah)
        
        simpan_data(transaksi)
        simpan_data_barang(barang)
        
        total_formatted = f"Rp. {total:,}".replace(',', '.')
        print(f"Transaksi berhasil ditambahkan! Total: {total_formatted}")
    
    except ValueError:
        print("Input salah! Pastikan jumlah berupa angka.")

# Fungsi untuk menampilkan semua transaksi
def tampilkan_transaksi(transaksi):
    if not transaksi:
        print("Tidak ada transaksi.")
        return

    print("\n--- Daftar Transaksi ---")
    for i, t in enumerate(transaksi, start=1):
        harga_formatted = f"Rp. {t['harga']:,}".replace(',', '.')
        total_formatted = f"Rp. {t['total']:,}".replace(',', '.')
        print(f"{i}. {t['nama_barang']} - {t['jumlah']} x {harga_formatted} = {total_formatted}")

# fungsi untuk menghapus transaksi    
def hapus_data(transaksi):
    tambah_transaksi(transaksi)
    
    if not transaksi:
        print("Tidak ada transaksi untuk dihapus.")
        return

    nama_barang = input("Masukkan transaksi barang yang ingin dihapus: ")
    found = False

    for t in transaksi:
        if t["nama_barang"].lower() == nama_barang.lower():
            found = True
            harga_formatted = f"Rp. {t['harga']:,}".replace(',', '.')
            total_formatted = f"Rp. {t['total']:,}".replace(',', '.')
            print(f"Apakah Anda yakin ingin menghapus transaksi berikut?")
            print(f"{t['nama_barang']} - {t['jumlah']} x {harga_formatted} = {total_formatted}")
            konfirmasi = input("Ketik 'Y' untuk menghapus atau apa saja untuk membatalkan: ")

            if konfirmasi.lower() == 'y':
                transaksi.remove(t)
                simpan_data(transaksi)
                print("Transaksi berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
            break

    if not found:
        print("Data dengan nama barang tersebut tidak ditemukan.")

# Fungsi untuk membuat visualisasi data penjualan
def visualisasi_data(transaksi):
    if not transaksi:
        print("Tidak ada data untuk divisualisasikan.")
        return

    nama_barang = [t["nama_barang"] for t in transaksi]
    total_penjualan = [t["total"] for t in transaksi]

    plt.bar(nama_barang, total_penjualan, color='skyblue')

    plt.xlabel('Nama Barang')
    plt.ylabel('Total Penjualan (Rp)')
    plt.title('Visualisasi Penjualan')

    for i, total in enumerate(total_penjualan):
        plt.text(i, total, f"Rp. {total:,}".replace(',', '.'), ha='center', va='bottom', fontsize=9)

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n--- Selamat Datang di Warung Mamah Kaka ---")
    print("1. Tambahkan barang")
    print("2. Tampilkan barang")
    print("3. Ubah data barang")
    print("4. Hapus barang")
    print("5. Buat transaksi")
    print("6. Tampilkan transaksi")
    print("7. Hapus transaksi")
    print("8. Visualisasi data penjualan")
    print("9. Keluar")

# Program utama
def main():
    barang = load_data_barang()
    transaksi = load_data()
    while True:
        tampilkan_menu()
        pilihan = input("\nPilih opsi di atas : ")

        if pilihan == "1":
            tambah_barang(barang)
        elif pilihan == "2":
            tampilkan_barang(barang)
        elif pilihan == "3":
            edit_barang(barang)
        elif pilihan == "4":
            hapus_barang(barang)
        elif pilihan == "5":
            tambah_transaksi(transaksi, barang)
        elif pilihan == "6":
            tampilkan_transaksi(transaksi)
        elif pilihan == "7":
            hapus_data(transaksi)
        elif pilihan == "8":
            visualisasi_data(transaksi)
        elif pilihan == "9":
            print("Terima kasih telah menggunakan program warung.")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
