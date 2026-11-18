import pandas as pd

harga = [
    ["Plastik", 3000],
    ["Kertas", 2000],
    ["Kardus", 2500],
    ["Kaleng/Logam", 5000],
    ["Botol Kaca", 1000]
]

try:
    data = pd.read_csv("bank_sampah.csv")
except:
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

while True:
    print("===== BANK SAMPAH =====")
    print("1. Tampilkan semua setoran")
    print("2. Tambah setoran")
    print("3. Ubah setoran")
    print("4. Hapus setoran")
    print("5. Cari setoran")
    print("6. Urutkan setoran")
    print("7. Laporan saldo nasabah")
    print("8. Keluar")
    pilih = input("Pilih menu (1-8): ")

    if pilih == "1":
        print("=== DATA SETORAN ===")
        if len(data) == 0:
            print("Belum ada data setoran.")
        else:
            for i in range(len(data)):
                baris = data.iloc[i]
                print(f"{i + 1}. {baris['Nama']} - {baris['Jenis']} - {baris['Berat']} kg - {baris['Poin']} poin - Rp{baris['Rupiah']}")

    elif pilih == "2":
        print("=== TAMBAH SETORAN ===")
        nama = input("Nama nasabah : ")
        if nama == "":
            print("Nama tidak boleh kosong.")
            continue
        print("Jenis sampah:")
        for i in range(len(harga)):
            print(f"{i + 1}. {harga[i][0]} - Rp{harga[i][1]}/kg")
        pilih_jenis = input("Pilih jenis (1-5): ")
        if pilih_jenis not in ["1", "2", "3", "4", "5"]:
            print("Pilihan jenis tidak valid.")
            continue
        jenis = harga[int(pilih_jenis) - 1][0]
        harga_kg = harga[int(pilih_jenis) - 1][1]
        while True:
            berat_teks = input("Berat (kg) : ")
            try:
                berat = float(berat_teks)
            except:
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
        print("=== RINGKASAN SETORAN ===")
        print("Nama   :", nama)
        print("Jenis  :", jenis)
        print("Berat  :", berat, "kg")
        print("Poin   :", poin)
        print("Rupiah : Rp", rupiah)
        print("Data berhasil disimpan.")

    elif pilih == "3":
        print("=== UBAH SETORAN ===")
        if len(data) == 0:
            print("Belum ada data setoran.")
        else:
            for i in range(len(data)):
                baris = data.iloc[i]
                print(f"{i + 1}. {baris['Nama']} - {baris['Jenis']} - {baris['Berat']} kg - {baris['Poin']} poin - Rp{baris['Rupiah']}")
            nomor_teks = input("Nomor setoran yang diubah: ")
            try:
                nomor = int(nomor_teks)
            except:
                nomor = 0
            if nomor < 1 or nomor > len(data):
                print("Nomor tidak ditemukan.")
            else:
                lama = data.iloc[nomor - 1]
                print("Data lama:", lama["Nama"], "-", lama["Jenis"], "-", lama["Berat"], "kg -", lama["Poin"], "poin - Rp", lama["Rupiah"])
                nama_baru = input("Nama baru (kosongkan kalau tidak diubah): ")
                print("Jenis sampah:")
                for i in range(len(harga)):
                    print(f"{i + 1}. {harga[i][0]} - Rp{harga[i][1]}/kg")
                jenis_baru = input("Jenis baru (0 kalau tidak diubah): ")
                berat_baru_teks = input("Berat baru (kosongkan kalau tidak diubah): ")
                if nama_baru != "":
                    data.loc[nomor - 1, "Nama"] = nama_baru
                if jenis_baru == "" or jenis_baru == "0":
                    pass
                elif jenis_baru in ["1", "2", "3", "4", "5"]:
                    data.loc[nomor - 1, "Jenis"] = harga[int(jenis_baru) - 1][0]
                else:
                    print("Pilihan jenis tidak valid, jenis tidak diubah.")
                if berat_baru_teks != "":
                    try:
                        berat_baru = float(berat_baru_teks)
                    except:
                        berat_baru = -1
                    if berat_baru <= 0 or berat_baru > 50:
                        print("Berat baru tidak valid, berat tidak diubah.")
                    else:
                        data.loc[nomor - 1, "Berat"] = berat_baru
                harga_kg = 0
                for i in range(len(harga)):
                    if harga[i][0] == data.loc[nomor - 1, "Jenis"]:
                        harga_kg = harga[i][1]
                data.loc[nomor - 1, "Poin"] = int(data.loc[nomor - 1, "Berat"] * 10)
                data.loc[nomor - 1, "Rupiah"] = int(data.loc[nomor - 1, "Berat"] * harga_kg)
                data.to_csv("bank_sampah.csv", index=False)
                print("Data berhasil diubah.")

    elif pilih == "4":
        print("=== HAPUS SETORAN ===")
        if len(data) == 0:
            print("Belum ada data setoran.")
        else:
            for i in range(len(data)):
                baris = data.iloc[i]
                print(f"{i + 1}. {baris['Nama']} - {baris['Jenis']} - {baris['Berat']} kg - {baris['Poin']} poin - Rp{baris['Rupiah']}")
            nomor_teks = input("Nomor setoran yang dihapus: ")
            try:
                nomor = int(nomor_teks)
            except:
                nomor = 0
            if nomor < 1 or nomor > len(data):
                print("Nomor tidak ditemukan.")
            else:
                hapus = data.iloc[nomor - 1]
                print("Data yang dihapus:", hapus["Nama"], "-", hapus["Jenis"], "-", hapus["Berat"], "kg -", hapus["Poin"], "poin - Rp", hapus["Rupiah"])
                yakin = input("Yakin hapus? (y/n): ")
                if yakin == "y":
                    data = data.drop(nomor - 1).reset_index(drop=True)
                    data.to_csv("bank_sampah.csv", index=False)
                    print("Data berhasil dihapus.")
                else:
                    print("Penghapusan dibatalkan.")

    elif pilih == "5":
        print("=== CARI SETORAN ===")
        kata = input("Masukkan nama nasabah atau jenis sampah: ")
        ketemu = False
        for i in range(len(data)):
            if kata.lower() in str(data.iloc[i, 0]).lower() or kata.lower() in str(data.iloc[i, 1]).lower():
                baris = data.iloc[i]
                print(f"{i + 1}. {baris['Nama']} - {baris['Jenis']} - {baris['Berat']} kg - {baris['Poin']} poin - Rp{baris['Rupiah']}")
                ketemu = True
        if ketemu == False:
            print("Data tidak ditemukan.")

    elif pilih == "6":
        print("=== URUTKAN SETORAN ===")
        print("1. Berat (terbesar ke terkecil)")
        print("2. Rupiah (terbesar ke terkecil)")
        urut = input("Pilih urutan (1-2): ")
        if urut == "1":
            kolom = 2
        elif urut == "2":
            kolom = 4
        else:
            kolom = -1
            print("Pilihan tidak valid.")
        if kolom != -1:
            for i in range(len(data)):
                for j in range(len(data) - 1 - i):
                    if data.iloc[j, kolom] < data.iloc[j + 1, kolom]:
                        temp = data.iloc[j].tolist()
                        data.iloc[j] = data.iloc[j + 1].tolist()
                        data.iloc[j + 1] = temp
            print("Data berhasil diurutkan.")
            for i in range(len(data)):
                baris = data.iloc[i]
                print(f"{i + 1}. {baris['Nama']} - {baris['Jenis']} - {baris['Berat']} kg - {baris['Poin']} poin - Rp{baris['Rupiah']}")

    elif pilih == "7":
        print("=== LAPORAN SALDO NASABAH ===")
        nama = input("Nama nasabah : ")
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
            print("Nama nasabah :", nama)
            print("Jumlah setoran:", total_setoran)
            print("Total berat   :", total_berat, "kg")
            print("Total poin    :", total_poin)
            print("Total rupiah  : Rp", total_rupiah)

    elif pilih == "8":
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
