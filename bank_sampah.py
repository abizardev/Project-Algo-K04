import pandas as pd


# Tugas: Abizar (Tampilan banner awal)
def banner_selamat_datang():
    print("╔══════════════════════════════════════════════════════╗")
    print("║             SISTEM MANAJEMEN BANK SAMPAH             ║")
    print("║          FASILKOM - UNIVERSITAS JEMBER 2026          ║")
    print("╠══════════════════════════════════════════════════════╣")
    print("║  Ubah Sampah Jadi Berkah, Kumpulkan Poin & Sembako   ║")
    print("╚══════════════════════════════════════════════════════╝")


# Tugas: Abizar (Menu utama dinamis admin dan petugas)
def tampil_menu(peran):
    if peran == "admin":
        print("\nRole Aktif: ADMINISTRATOR")
    else:
        print("\nRole Aktif: PETUGAS LOKET")
    print("---------------------------------------------")
    print("1.  Tampilkan semua setoran")
    print("2.  Tambah setoran")
    if peran == "admin":
        print("3.  Ubah setoran")
        print("4.  Hapus setoran")
        print("5.  Cari setoran")
        print("6.  Urutkan setoran")
        print("7.  Laporan saldo nasabah")
        print("8.  Pembayaran nasabah")
        print("9.  Tukar poin sembako")
        print("10. Riwayat transaksi nasabah")
        print("11. Statistik bank sampah")
        print("12. Cek & restok sembako")
        print("13. Keluar")
    else:
        print("3.  Cari setoran")
        print("4.  Urutkan setoran")
        print("5.  Laporan saldo nasabah")
        print("6.  Tukar poin sembako")
        print("7.  Riwayat transaksi nasabah")
        print("8.  Statistik bank sampah")
        print("9.  Cek stok sembako")
        print("10. Keluar")
    print("---------------------------------------------")

# Tugas: Habibi (Autentikasi login multi-role admin dan petugas)
def login():
    kesempatan = 3
    while kesempatan > 0:
        print("\n--- Silakan Login (Sisa Kesempatan:", kesempatan, ") ---")
        username = input("Username : ")
        password = input("Password : ")

        if password.isdigit() == False:
            print("Password harus angka.")
            kesempatan = kesempatan - 1
            print("Sisa kesempatan:", kesempatan)
        elif username == "admin" and password == "123456":
            print("\nLogin berhasil. Selamat datang, admin.")
            return "admin"
        elif username == "petugas" and password == "111111":
            print("\nLogin berhasil. Selamat datang, petugas.")
            return "petugas"
        else:
            kesempatan = kesempatan - 1
            print("Username atau password salah. Sisa kesempatan:", kesempatan)

    print("\nLogin gagal 3 kali. Program berhenti.")
    exit()


# Tugas: Habibi (Basis data CSV: muat harga sampah)
def muat_harga():
    try:
        df = pd.read_csv("harga_sampah.csv")
        if len(df) == 0:
            raise FileNotFoundError
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame([
            ["Plastik", 3000],
            ["Kertas", 2000],
            ["Kardus", 2500],
            ["Kaleng/Logam", 5000],
            ["Botol Kaca", 1000]
        ], columns=["Jenis", "Harga"])
        df.to_csv("harga_sampah.csv", index=False)
    harga = []
    for i in range(len(df)):
        harga.append([df.iloc[i, 0], int(df.iloc[i, 1])])
    return harga


# Tugas: Habibi (Basis data CSV: muat sembako gudang)
def muat_sembako():
    try:
        df = pd.read_csv("sembako.csv")
        if len(df) == 0:
            raise FileNotFoundError
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame([
            ["Beras 1 kg", 100, 20],
            ["Minyak Goreng 1 Liter", 200, 15],
            ["Gula Pasir 1 kg", 120, 15],
            ["Mie Instan 1 bungkus", 25, 50],
            ["Telur Ayam 1 kg", 150, 10],
            ["Tepung Terigu 1 kg", 80, 20],
            ["Garam 500 gram", 30, 25]
        ], columns=["Nama", "Poin", "Stok"])
        df.to_csv("sembako.csv", index=False)
    sembako = []
    for i in range(len(df)):
        sembako.append([df.iloc[i, 0], int(df.iloc[i, 1]), int(df.iloc[i, 2])])
    return sembako


# Tugas: Habibi (Basis data CSV: simpan stok sembako)
def simpan_sembako(sembako):
    df = pd.DataFrame(sembako, columns=["Nama", "Poin", "Stok"])
    df.to_csv("sembako.csv", index=False)


# Tugas: Habibi (Basis data CSV: muat data setoran)
def muat_data():
    try:
        data = pd.read_csv("bank_sampah.csv")
        if len(data) == 0:
            raise FileNotFoundError
    except (FileNotFoundError, pd.errors.EmptyDataError):
        data = pd.DataFrame([
            ["Budi", "Plastik", 5, 50, 15000],
            ["Siti", "Kertas", 8, 80, 16000],
            ["Andi", "Kardus", 4, 40, 10000],
            ["Dewi", "Kaleng/Logam", 3, 30, 15000],
            ["Rizky", "Botol Kaca", 10, 100, 10000],
            ["Budi", "Kertas", 6, 60, 12000],
            ["Siti", "Plastik", 7, 70, 21000],
            ["Andi", "Kaleng/Logam", 2, 20, 10000],
            ["Dewi", "Kardus", 9, 90, 22500],
            ["Rizky", "Plastik", 12, 120, 36000]
        ], columns=["Nama", "Jenis", "Berat", "Poin", "Rupiah"])
        data.to_csv("bank_sampah.csv", index=False)
    return data


# Tugas: Habibi (Basis data CSV: muat riwayat pembayaran nasabah)
def muat_bayar():
    try:
        data_bayar = pd.read_csv("pembayaran.csv")
        if len(data_bayar) == 0:
            raise FileNotFoundError
    except (FileNotFoundError, pd.errors.EmptyDataError):
        data_bayar = pd.DataFrame([
            ["Budi", 10000, "Tunai"],
            ["Siti", 15000, "Transfer"],
            ["Rizky", 20000, "Tunai"]
        ], columns=["Nama", "Jumlah", "Metode"])
        data_bayar.to_csv("pembayaran.csv", index=False)
    return data_bayar


# Tugas: Habibi (Basis data CSV: muat riwayat penukaran poin)
def muat_tukar():
    try:
        data_tukar = pd.read_csv("penukaran.csv")
        if len(data_tukar) == 0:
            raise FileNotFoundError
    except (FileNotFoundError, pd.errors.EmptyDataError):
        data_tukar = pd.DataFrame([
            ["Budi", "Beras 1 kg", 100],
            ["Dewi", "Minyak Goreng 1 Liter", 200],
            ["Siti", "Gula Pasir 1 kg", 120]
        ], columns=["Nama", "Sembako", "Poin"])
        data_tukar.to_csv("penukaran.csv", index=False)
    return data_tukar

# Tugas: Abizar (Format tampilan cetak tabel setoran)
def tampilkan_tabel(kolom, baris_data):
    lebar_kolom = []
    for i in range(len(kolom)):
        lebar = len(str(kolom[i]))
        for baris in baris_data:
            if len(str(baris[i])) > lebar:
                lebar = len(str(baris[i]))
        lebar_kolom.append(lebar)

    garis = "+"
    for lebar in lebar_kolom:
        garis = garis + "-" * (lebar + 2) + "+"

    print(garis)
    teks_kolom = []
    for i in range(len(kolom)):
        teks_kolom.append(str(kolom[i]).ljust(lebar_kolom[i]))
    print("| " + " | ".join(teks_kolom) + " |")
    print(garis)

    for baris in baris_data:
        teks_baris = []
        for i in range(len(kolom)):
            teks_baris.append(str(baris[i]).ljust(lebar_kolom[i]))
        print("| " + " | ".join(teks_baris) + " |")
    print(garis)


# Tugas: Abizar (Format tampilan cetak tabel setoran)
def tampilkan_data(data):
    baris_tabel = []
    for i in range(len(data)):
        baris = data.iloc[i]
        baris_tabel.append([
            i + 1, baris["Nama"], baris["Jenis"], str(baris["Berat"]) + " kg",
            str(baris["Poin"]) + " poin", "Rp" + str(baris["Rupiah"])
        ])
    tampilkan_tabel(["No", "Nama", "Jenis Sampah", "Berat", "Poin", "Rupiah"], baris_tabel)


# Tugas: Abizar (Modul tampilkan data setoran)
def tampilkan(data):
    print("\n-- Data Setoran --")
    if len(data) == 0:
        print("Belum ada data setoran.")
    else:
        tampilkan_data(data)


# Tugas: Gala (Tambah data setoran baru & validasi berat)
def tambah(data, harga):
    print("\nTambah Setoran:")
    nama = input("Nama nasabah : ").strip()
    if nama == "":
        print("Nama tidak boleh kosong.")
        return
    if nama.replace(" ", "").isalpha() == False:
        print("Nama hanya boleh huruf.")
        return

    print("Jenis sampah:")
    baris_harga = []
    for i in range(len(harga)):
        baris_harga.append([i + 1, harga[i][0], "Rp" + str(harga[i][1]) + "/kg"])
    tampilkan_tabel(["No", "Jenis Sampah", "Harga per kg"], baris_harga)

    pilih_jenis = input("Pilih jenis (1-" + str(len(harga)) + "): ")
    cek_valid = False
    for i in range(len(harga)):
        if pilih_jenis == str(i + 1):
            cek_valid = True
    if cek_valid == False:
        print("Pilihan jenis tidak valid.")
        return

    idx = int(pilih_jenis) - 1
    jenis = harga[idx][0]
    harga_kg = harga[idx][1]

    while True:
        berat_teks = input("Berat (kg) : ")
        try:
            berat = float(berat_teks)
        except ValueError:
            print("Berat harus angka.")
            continue
        if berat <= 0:
            print("Berat harus lebih dari 0.")
        elif berat > 50:
            print("Berat maksimal 50 kg per setoran, pecah jadi beberapa setoran.")
        else:
            break

    poin = int(berat * 10)
    rupiah = int(berat * harga_kg)

    data.loc[len(data)] = [nama, jenis, berat, poin, rupiah]
    data.to_csv("bank_sampah.csv", index=False)

    print("\nRingkasan Setoran:")
    tampilkan_tabel(
        ["Keterangan", "Nilai"],
        [
            ["Nama", nama],
            ["Jenis", jenis],
            ["Berat", str(berat) + " kg"],
            ["Poin", poin],
            ["Rupiah", "Rp" + str(rupiah)]
        ]
    )
    print("Data berhasil disimpan.")


# Tugas: Gala (Ubah data setoran & rekalkulasi tarif)
def ubah(data, harga, peran):
    print("\nUbah Setoran:")
    if peran != "admin":
        print("Hanya admin yang bisa mengubah data.")
        return
    if len(data) == 0:
        print("Belum ada data setoran.")
        return

    tampilkan_data(data)
    nomor_teks = input("Nomor setoran yang diubah: ")
    try:
        nomor = int(nomor_teks)
    except ValueError:
        nomor = 0

    if nomor < 1 or nomor > len(data):
        print("Nomor tidak ditemukan.")
        return

    idx = nomor - 1
    lama = data.iloc[idx]
    print("Data lama:")
    tampilkan_tabel(
        ["Nama", "Jenis Sampah", "Berat", "Poin", "Rupiah"],
        [[lama["Nama"], lama["Jenis"], str(lama["Berat"]) + " kg",
          str(lama["Poin"]) + " poin", "Rp" + str(lama["Rupiah"])]]
    )

    nama_baru = input("Nama baru (kosongkan kalau tidak diubah): ").strip()
    print("Jenis sampah:")
    baris_harga = []
    for i in range(len(harga)):
        baris_harga.append([i + 1, harga[i][0], "Rp" + str(harga[i][1]) + "/kg"])
    tampilkan_tabel(["No", "Jenis Sampah", "Harga per kg"], baris_harga)
    jenis_baru = input("Jenis baru (0 kalau tidak diubah): ")
    berat_baru_teks = input("Berat baru (kosongkan kalau tidak diubah): ")

    if nama_baru != "":
        if nama_baru.replace(" ", "").isalpha() == False:
            print("Nama baru hanya boleh huruf, nama tidak diubah.")
        else:
            data.loc[idx, "Nama"] = nama_baru

    cek_jenis = False
    for i in range(len(harga)):
        if jenis_baru == str(i + 1):
            cek_jenis = True
    if cek_jenis == True:
        data.loc[idx, "Jenis"] = harga[int(jenis_baru) - 1][0]
    elif jenis_baru != "" and jenis_baru != "0":
        print("Pilihan jenis tidak valid, jenis tidak diubah.")

    if berat_baru_teks != "":
        try:
            berat_baru = float(berat_baru_teks)
            if berat_baru <= 0 or berat_baru > 50:
                print("Berat baru tidak valid, berat tidak diubah.")
            else:
                data.loc[idx, "Berat"] = berat_baru
        except ValueError:
            print("Berat baru tidak valid, berat tidak diubah.")

    # cari harga per kg berdasarkan jenis yang sekarang tersimpan
    harga_kg = 0
    for i in range(len(harga)):
        if str(harga[i][0]).lower() == str(data.loc[idx, "Jenis"]).lower():
            harga_kg = harga[i][1]

    if harga_kg == 0:
        print("Peringatan: jenis sampah tidak dikenali, poin dan rupiah tidak dihitung ulang.")
    else:
        data.loc[idx, "Poin"] = int(data.loc[idx, "Berat"] * 10)
        data.loc[idx, "Rupiah"] = int(data.loc[idx, "Berat"] * harga_kg)

    data.to_csv("bank_sampah.csv", index=False)
    print("Data berhasil diubah.")


# Tugas: Gala (Hapus data setoran & reset indeks DataFrame)
def hapus(data, peran):
    print("\nHapus Setoran:")
    if peran != "admin":
        print("Hanya admin yang bisa menghapus data.")
        return data
    if len(data) == 0:
        print("Belum ada data setoran.")
        return data

    tampilkan_data(data)
    nomor_teks = input("Nomor setoran yang dihapus: ")
    try:
        nomor = int(nomor_teks)
    except ValueError:
        nomor = 0

    if nomor < 1 or nomor > len(data):
        print("Nomor tidak ditemukan.")
        return data

    idx = nomor - 1
    hapus_data = data.iloc[idx]
    print("Data yang dihapus:")
    tampilkan_tabel(
        ["Nama", "Jenis Sampah", "Berat", "Poin", "Rupiah"],
        [[hapus_data["Nama"], hapus_data["Jenis"], str(hapus_data["Berat"]) + " kg",
          str(hapus_data["Poin"]) + " poin", "Rp" + str(hapus_data["Rupiah"])]]
    )
    yakin = input("Yakin hapus? (y/n): ")

    if yakin == "y":
        data = data.drop(idx).reset_index(drop=True)
        data.to_csv("bank_sampah.csv", index=False)
        print("Data berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")
    return data


# Tugas: Nafisa (Algoritma Linear Search untuk mencari setoran) >
def cari(data):
    print("\nCari Setoran:")
    kata = input("Masukkan nama nasabah atau jenis sampah: ").strip()

    if kata == "":
        print("Kata kunci tidak boleh kosong.")
        return

    kata_cari = kata.lower()
    baris_ditemukan = []

    for i in range(len(data)):
        nama = str(data.iloc[i, 0]).lower()
        jenis = str(data.iloc[i, 1]).lower()

        if kata_cari in nama or kata_cari in jenis:
            baris = data.iloc[i]
            baris_ditemukan.append([
                len(baris_ditemukan) + 1, baris["Nama"], baris["Jenis"],
                str(baris["Berat"]) + " kg", str(baris["Poin"]) + " poin",
                "Rp" + str(baris["Rupiah"])
            ])

    if len(baris_ditemukan) == 0:
        print("Data tidak ditemukan.")
    else:
        tampilkan_tabel(
            ["No", "Nama", "Jenis Sampah", "Berat", "Poin", "Rupiah"],
            baris_ditemukan
        )


# Tugas: Nafisa (Algoritma Bubble Sort untuk mengurutkan setoran)
def urutkan(data):
    print("\nUrutkan Setoran:")
    print("1. Berat (terbesar ke terkecil)")
    print("2. Rupiah (terbesar ke terkecil)")
    print("3. Nama (A - Z)")
    urut = input("Pilih urutan (1-3): ")

    if urut == "1":
        kolom = 2  
    elif urut == "2":
        kolom = 4  
    elif urut == "3":
        kolom = 0  
    else:
        print("Pilihan tidak valid.")
        return

    for i in range(len(data)):
        for j in range(len(data) - 1 - i):
            if urut == "3":
                perlu_tukar = str(data.iloc[j, kolom]).lower() > str(data.iloc[j + 1, kolom]).lower()
            else:
                perlu_tukar = data.iloc[j, kolom] < data.iloc[j + 1, kolom]

            if perlu_tukar:
                data.iloc[[j, j + 1]] = data.iloc[[j + 1, j]].values

    print("Data berhasil diurutkan.")
    print("Catatan: urutan ini tidak disimpan ke file dan akan kembali seperti semula saat program dibuka ulang.")
    tampilkan_data(data)


# Tugas: Gala (Rekapitulasi saldo setoran per nasabah)
def laporan(data):
    print("\nLaporan Saldo Nasabah:")
    nama = input("Nama nasabah : ").strip()
    total_setoran = 0
    total_berat = 0
    total_poin = 0
    total_rupiah = 0

    for i in range(len(data)):
        if str(data.iloc[i, 0]).lower() == nama.lower():
            total_setoran = total_setoran + 1
            total_berat = total_berat + data.iloc[i, 2]
            total_poin = total_poin + data.iloc[i, 3]
            total_rupiah = total_rupiah + data.iloc[i, 4]

    if total_setoran == 0:
        print("Nasabah tidak ditemukan.")
    else:
        tampilkan_tabel(
            ["Keterangan", "Nilai"],
            [
                ["Nama nasabah", nama],
                ["Jumlah setoran", total_setoran],
                ["Total berat", str(total_berat) + " kg"],
                ["Total poin", total_poin],
                ["Total rupiah", "Rp" + str(total_rupiah)]
            ]
        )


# Tugas: Nafisa (Pencairan dana kasir dan validasi saldo)
def bayar(data, data_bayar, peran):
    print("\nPembayaran Nasabah:")
    if peran != "admin":
        print("Hanya admin yang bisa memproses pembayaran.")
        return

    nama = input("Nama nasabah : ").strip()
    if nama == "":
        print("Nama nasabah tidak boleh kosong.")
        return

    nama_cari = nama.lower()
    ditemukan = False
    total_rupiah = 0

    for i in range(len(data)):
        if str(data.iloc[i, 0]).lower() == nama_cari:
            ditemukan = True
            total_rupiah += data.iloc[i, 4]

    if not ditemukan:
        print("Nasabah tidak ditemukan.")
        return

    # Hitung total yang sudah pernah dibayar nasabah
    total_bayar = 0
    for i in range(len(data_bayar)):
        if str(data_bayar.iloc[i, 0]).lower() == nama_cari:
            total_bayar += data_bayar.iloc[i, 1]

    sisa = total_rupiah - total_bayar
    if sisa <= 0:
        print("Saldo nasabah sudah lunas.")
        return

    tampilkan_tabel(
        ["Keterangan", "Nilai"],
        [
            ["Nama nasabah", nama],
            ["Total saldo", "Rp" + str(total_rupiah)],
            ["Sudah dibayar", "Rp" + str(total_bayar)],
            ["Sisa saldo", "Rp" + str(sisa)]
        ]
    )

    while True:
        jumlah_teks = input("Jumlah dibayar (Rp): ").strip()
        if not jumlah_teks.isdigit():
            print("Jumlah harus angka bulat tanpa titik atau koma.")
            continue

        jumlah = int(jumlah_teks)
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0.")
            continue
        if jumlah > sisa:
            print("Jumlah melebihi sisa saldo.")
            continue
        break

    print("Metode pembayaran:")
    print("1. Tunai")
    print("2. Transfer")
    while True:
        metode_pilih = input("Pilih metode (1-2): ").strip()
        if metode_pilih == "1":
            metode = "Tunai"
            break
        elif metode_pilih == "2":
            metode = "Transfer"
            break
        else:
            print("Metode tidak valid, pilih 1 atau 2.")

    data_bayar.loc[len(data_bayar)] = [nama, jumlah, metode]
    data_bayar.to_csv("pembayaran.csv", index=False)

    print("\nBukti Pembayaran:")
    tampilkan_tabel(
        ["Keterangan", "Nilai"],
        [
            ["Nama nasabah", nama],
            ["Jumlah bayar", "Rp" + str(jumlah)],
            ["Metode", metode],
            ["Sisa saldo", "Rp" + str(sisa - jumlah)]
        ]
    )
    print("Pembayaran berhasil disimpan.")


# Tugas: Nafisa (Penukaran poin reward dengan sembako)
def tukar_poin(data, data_tukar, sembako):
    print("\nTukar Poin:")
    nama = input("Nama nasabah : ").strip()
    if nama == "":
        print("Nama nasabah tidak boleh kosong.")
        return

    if not sembako:
        print("Daftar sembako sedang kosong.")
        return

    nama_cari = nama.lower()
    ditemukan = False
    nama_baku = nama
    total_poin = 0

    for i in range(len(data)):
        if str(data.iloc[i, 0]).strip().lower() == nama_cari:
            if not ditemukan:
                nama_baku = str(data.iloc[i, 0]).strip()
                ditemukan = True
            total_poin += data.iloc[i, 3]

    if not ditemukan:
        print("Nasabah tidak ditemukan.")
        return

    total_tukar = 0
    for i in range(len(data_tukar)):
        if str(data_tukar.iloc[i, 0]).strip().lower() == nama_cari:
            total_tukar += data_tukar.iloc[i, 2]

    sisa = total_poin - total_tukar
    if sisa <= 0:
        print("Poin nasabah sudah habis.")
        return

    tampilkan_tabel(
        ["Keterangan", "Nilai"],
        [
            ["Nama nasabah", nama_baku],
            ["Total poin", total_poin],
            ["Sudah ditukar", str(total_tukar) + " poin"],
            ["Sisa poin", str(sisa) + " poin"]
        ]
    )

    print("\nDaftar sembako:")
    tampilkan_sembako(sembako)

    pilih_teks = input(f"Pilih sembako (1-{len(sembako)}): ").strip()
    if not pilih_teks.isdigit():
        print("Pilihan tidak valid.")
        return

    nomor_pilih = int(pilih_teks)
    if nomor_pilih < 1 or nomor_pilih > len(sembako):
        print("Pilihan tidak valid.")
        return

    posisi = nomor_pilih - 1
    barang = sembako[posisi][0]
    harga_poin = sembako[posisi][1]
    stok_barang = sembako[posisi][2]

    if harga_poin > sisa:
        print("Poin tidak cukup.")
        return
    if stok_barang <= 0:
        print("Stok sembako tersebut sedang kosong di gudang.")
        return

    sembako[posisi][2] -= 1
    simpan_sembako(sembako)

    data_tukar.loc[len(data_tukar)] = [nama_baku, barang, harga_poin]
    data_tukar.to_csv("penukaran.csv", index=False)

    print("\nBukti Penukaran:")
    tampilkan_tabel(
        ["Keterangan", "Nilai"],
        [
            ["Nama nasabah", nama_baku],
            ["Sembako", barang],
            ["Poin dipakai", str(harga_poin) + " poin"],
            ["Sisa poin", str(sisa - harga_poin) + " poin"]
        ]
    )
    print("Penukaran berhasil disimpan.")


# Tugas: Abizar (Pencarian riwayat pencairan uang dan penukaran sembako)
def riwayat_transaksi(data, data_bayar, data_tukar):
    print("\nRiwayat Transaksi Nasabah:")
    nama = input("Nama nasabah : ").strip()

    # cek apakah nasabah terdaftar di data setoran
    ada_nasabah = False
    for i in range(len(data)):
        if str(data.iloc[i, 0]).lower() == nama.lower():
            ada_nasabah = True
            break

    if ada_nasabah == False:
        print("Nasabah tidak ditemukan.")
        return

    bayar_list = []
    for i in range(len(data_bayar)):
        if str(data_bayar.iloc[i, 0]).lower() == nama.lower():
            bayar_list.append(data_bayar.iloc[i])

    tukar_list = []
    for i in range(len(data_tukar)):
        if str(data_tukar.iloc[i, 0]).lower() == nama.lower():
            tukar_list.append(data_tukar.iloc[i])

    print(f"\n1. Riwayat Pembayaran Rupiah ({len(bayar_list)} kali):")
    if len(bayar_list) == 0:
        print("   (Belum pernah mencairkan saldo)")
    else:
        baris_bayar = []
        for i in range(len(bayar_list)):
            row = bayar_list[i]
            baris_bayar.append([i + 1, "Rp" + f"{int(row['Jumlah']):,}", row["Metode"]])
        tampilkan_tabel(["No", "Jumlah dibayar", "Metode"], baris_bayar)

    print(f"\n2. Riwayat Penukaran Sembako ({len(tukar_list)} kali):")
    if len(tukar_list) == 0:
        print("   (Belum pernah menukarkan poin)")
    else:
        baris_tukar = []
        for i in range(len(tukar_list)):
            row = tukar_list[i]
            baris_tukar.append([i + 1, row["Sembako"], str(int(row["Poin"])) + " poin"])
        tampilkan_tabel(["No", "Sembako", "Poin"], baris_tukar)


# Tugas: Habibi (Dashboard statistik global bank sampah)
def statistik_bank_sampah(data, data_bayar, data_tukar):
    print("\nStatistik Bank Sampah:")
    total_setoran = len(data)
    total_berat = 0
    total_rupiah = 0
    total_poin = 0

    for i in range(len(data)):
        total_berat = total_berat + float(data.iloc[i, 2])
        total_rupiah = total_rupiah + int(data.iloc[i, 4])
        total_poin = total_poin + int(data.iloc[i, 3])

    total_cair = 0
    for i in range(len(data_bayar)):
        total_cair = total_cair + int(data_bayar.iloc[i, 1])

    total_poin_tukar = 0
    for i in range(len(data_tukar)):
        total_poin_tukar = total_poin_tukar + int(data_tukar.iloc[i, 2])

    # hitung nasabah unik pakai set supaya nama yang sama tidak dihitung dua kali
    nasabah_unik = set()
    for i in range(len(data)):
        nasabah_unik.add(str(data.iloc[i, 0]).lower())

    tampilkan_tabel(
        ["Statistik", "Nilai"],
        [
            ["Total berat sampah terkumpul", f"{total_berat:.1f} kg"],
            ["Total transaksi setoran", str(total_setoran) + " kali"],
            ["Jumlah nasabah terdaftar", str(len(nasabah_unik)) + " orang"],
            ["Total nilai rupiah sampah", "Rp" + f"{total_rupiah:,}"],
            ["Total saldo sudah dibayar", "Rp" + f"{total_cair:,}"],
            ["Sisa saldo belum dibayar", "Rp" + f"{total_rupiah - total_cair:,}"],
            ["Sisa poin reward beredar", str(total_poin - total_poin_tukar) + " poin"]
        ]
    )


# Tugas: Habibi (Manajemen stok gudang dan restok sembako oleh admin)
def tampilkan_sembako(sembako):
    baris_tabel = []
    for i in range(len(sembako)):
        baris_tabel.append([
            i + 1, sembako[i][0], str(sembako[i][1]) + " poin",
            str(sembako[i][2]) + " unit"
        ])
    tampilkan_tabel(["No", "Nama Sembako", "Harga Poin", "Stok"], baris_tabel)
    

# Tugas: Habibi (Manajemen stok gudang dan restok sembako oleh admin)
def kelola_sembako(sembako, peran):
    print("\nStok Sembako Gudang:")
    tampilkan_sembako(sembako)

    if peran == "admin":
        tambah_stok = input("\nTambah stok sembako? (y/n): ").lower()
        if tambah_stok == "y":
            pilih_item = input("Pilih nomor sembako (1-" + str(len(sembako)) + "): ")
            cek_valid = False
            for i in range(len(sembako)):
                if pilih_item == str(i + 1):
                    cek_valid = True
            if cek_valid == True:
                idx = int(pilih_item) - 1
                jumlah_masuk = input("Jumlah stok tambahan untuk " + sembako[idx][0] + ": ")
                if jumlah_masuk.isdigit() and int(jumlah_masuk) > 0:
                    sembako[idx][2] = sembako[idx][2] + int(jumlah_masuk)
                    simpan_sembako(sembako)
                    print("Stok", sembako[idx][0], "berhasil ditambah. Stok sekarang:", sembako[idx][2], "unit.")
                else:
                    print("Jumlah harus angka lebih dari 0.")
            else:
                print("Nomor sembako tidak valid.")


# Tugas: Abizar (Alur program utama dan navigasi menu)
if __name__ == "__main__":
    banner_selamat_datang()
    peran = login()
    data = muat_data()
    data_bayar = muat_bayar()
    data_tukar = muat_tukar()
    harga = muat_harga()
    sembako = muat_sembako()

    while True:
        tampil_menu(peran)
        pilih = input("Pilih menu: ").strip()

        if peran == "admin":
            if pilih == "1":
                tampilkan(data)
            elif pilih == "2":
                tambah(data, harga)
            elif pilih == "3":
                ubah(data, harga, peran)
            elif pilih == "4":
                data = hapus(data, peran)
            elif pilih == "5":
                cari(data)
            elif pilih == "6":
                urutkan(data)
            elif pilih == "7":
                laporan(data)
            elif pilih == "8":
                bayar(data, data_bayar, peran)
            elif pilih == "9":
                tukar_poin(data, data_tukar, sembako)
            elif pilih == "10":
                riwayat_transaksi(data, data_bayar, data_tukar)
            elif pilih == "11":
                statistik_bank_sampah(data, data_bayar, data_tukar)
            elif pilih == "12":
                kelola_sembako(sembako, peran)
            elif pilih == "13":
                yakin = input("Yakin keluar? (y/n): ")
                if yakin == "y":
                    print("\nTerima kasih, program selesai.")
                    break
            else:
                print("Pilihan tidak valid, coba lagi.")
        else:
            if pilih == "1":
                tampilkan(data)
            elif pilih == "2":
                tambah(data, harga)
            elif pilih == "3":
                cari(data)
            elif pilih == "4":
                urutkan(data)
            elif pilih == "5":
                laporan(data)
            elif pilih == "6":
                tukar_poin(data, data_tukar, sembako)
            elif pilih == "7":
                riwayat_transaksi(data, data_bayar, data_tukar)
            elif pilih == "8":
                statistik_bank_sampah(data, data_bayar, data_tukar)
            elif pilih == "9":
                kelola_sembako(sembako, peran)
            elif pilih == "10":
                yakin = input("Yakin keluar? (y/n): ")
                if yakin == "y":
                    print("\nTerima kasih, program selesai.")
                    break
            else:
                print("Pilihan tidak valid, coba lagi.")
