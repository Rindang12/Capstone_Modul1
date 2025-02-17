import os
import re
import pwinput
from dotenv import load_dotenv
from tabulate import tabulate
from colorama import init, Fore
from datetime import datetime

# Inisialisasi Clear-Screen
os.system('cls')

# Inisialisasi Colorama
init(autoreset=True)

# Data login admin
load_dotenv()
ADMIN_USERNAME = "adminTIM"
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "").strip()

# Tempat penyimpanan sementara buku yang dihapus
recycle_bin = [] 

# Dictionary untuk menyimpan wishlist pengguna
wishlist_buku = {
    "RINDANG": ["THE MIDNIGHT LIBRARY"],
    "KHADIJAH": ["PYTHON FOR DATA ANALYSIS"],
    "MAGHRIBA": ["THE RULE OF LAW"]
}

# Tempat penyimpanan sementara buku yang dipinjam
koleksi_buku = {
    "Fiksi": [],
    "Akademik & Referensi": [],
    "Hukum & Politik": [],
    "Ekonomi": [],
    "Sains": [],
    "Teknologi": [],
    "Sejarah": []
}

# Koleksi Buku Perpustakaan
koleksi_buku = {
    "Fiksi": [
        {"id": "FIK-0001", "judul": "THE OVERSTORY", "tahun": 2018, "pengarang": "Richard Powers", "penerbit": "W.W. Norton & Company", "stok": 5},
        {"id": "FIK-0002", "judul": "WHERE THE CRAWDADS SING", "tahun": 2018, "pengarang": "Delia Owens", "penerbit": "G.P. Putnam's Sons", "stok": 5},
        {"id": "FIK-0003", "judul": "THE TESTAMENTS", "tahun": 2019, "pengarang": "Margaret Atwood", "penerbit": "Nan A. Talese", "stok": 5},
        {"id": "FIK-0004", "judul": "THE SILENT PATIENT", "tahun": 2019, "pengarang": "Alex Michaelides", "penerbit": "Celadon Books", "stok": 4},
        {"id": "FIK-0005", "judul": "THE MIDNIGHT LIBRARY", "tahun": 2020, "pengarang": "Matt Haig", "penerbit": "Canongate Books", "stok": 0},
        {"id": "FIK-0006", "judul": "PROJECT HAIL MARY", "tahun": 2021, "pengarang": "Andy Weir", "penerbit": "Ballantine Books", "stok": 5},
        {"id": "FIK-0007", "judul": "KLARA AND THE SUN", "tahun": 2021, "pengarang": "Kazuo Ishiguro", "penerbit": "Faber & Faber", "stok": 5},
        {"id": "FIK-0008", "judul": "SEA OF TRANQUILITY", "tahun": 2022, "pengarang": "Emily St. John Mandel", "penerbit": "Knopf", "stok": 5},
        {"id": "FIK-0009", "judul": "DEMON COPPERHEAD", "tahun": 2022, "pengarang": "Barbara Kingsolver", "penerbit": "Harper", "stok": 5},
        {"id": "FIK-0010", "judul": "THE BEE STING", "tahun": 2023, "pengarang": "Paul Murray", "penerbit": "Farrar, Straus and Giroux", "stok": 5}
    ],
    "Akademik & Referensi": [
        {"id": "AKD-0001", "judul": "MATHEMATICAL FOUNDATIONS OF DATA SCIENCE", "tahun": 2019, "pengarang": "John Doe", "penerbit": "Cambridge University Press", "stok": 5},
        {"id": "AKD-0002", "judul": "INTRODUCTION TO QUANTUM MECHANICS", "tahun": 2019, "pengarang": "David J. Griffiths", "penerbit": "Pearson", "stok": 0},
        {"id": "AKD-0003", "judul": "DEEP LEARNING", "tahun": 2018, "pengarang": "Ian Goodfellow", "penerbit": "MIT Press", "stok": 0},
        {"id": "AKD-0004", "judul": "MACHINE LEARNING YEARNING", "tahun": 2020, "pengarang": "Andrew Ng", "penerbit": "Self-Published", "stok": 5},
        {"id": "AKD-0005", "judul": "PYTHON FOR DATA ANALYSIS", "tahun": 2022, "pengarang": "Wes McKinney", "penerbit": "O'Reilly Media", "stok": 0},
        {"id": "AKD-0006", "judul": "PRINCIPLES OF ECONOMICS", "tahun": 2021, "pengarang": "N. Gregory Mankiw", "penerbit": "Cengage", "stok": 5},
        {"id": "AKD-0007", "judul": "THE ELEMENTS OF STATISTICAL LEARNING", "tahun": 2020, "pengarang": "Trevor Hastie", "penerbit": "Springer", "stok": 5},
        {"id": "AKD-0008", "judul": "INTRODUCTION TO ALGORITHMS", "tahun": 2021, "pengarang": "Thomas H. Cormen", "penerbit": "MIT Press", "stok": 4},
        {"id": "AKD-0009", "judul": "ARTIFICIAL INTELLIGENCE: A GUIDE", "tahun": 2023, "pengarang": "Melanie Mitchell", "penerbit": "Macmillan", "stok": 5},
        {"id": "AKD-0010", "judul": "THE SCIENCE OF READING", "tahun": 2024, "pengarang": "Mark Seidenberg", "penerbit": "Penguin Books", "stok": 5}
    ],
    "Hukum & Politik": [
        {"id": "HUK-0001", "judul": "THE COLOR OF LAW", "tahun": 2018, "pengarang": "Richard Rothstein", "penerbit": "Liveright", "stok": 5},
        {"id": "HUK-0002", "judul": "JUST MERCY", "tahun": 2019, "pengarang": "Bryan Stevenson", "penerbit": "Spiegel & Grau", "stok": 5},
        {"id": "HUK-0003", "judul": "HOW DEMOCRACIES DIE", "tahun": 2018, "pengarang": "Steven Levitsky & Daniel Ziblatt", "penerbit": "Broadway Books", "stok": 4},
        {"id": "HUK-0004", "judul": "THE RULE OF LAW", "tahun": 2019, "pengarang": "Tom Bingham", "penerbit": "Penguin Books", "stok": 1},
        {"id": "HUK-0005", "judul": "WE THE PEOPLE", "tahun": 2020, "pengarang": "Erwin Chemerinsky", "penerbit": "Yale University Press", "stok": 5},
        {"id": "HUK-0006", "judul": "THE AGE OF SURVEILLANCE CAPITALISM", "tahun": 2021, "pengarang": "Shoshana Zuboff", "penerbit": "PublicAffairs", "stok": 5},
        {"id": "HUK-0007", "judul": "SUPREME INEQUALITY", "tahun": 2021, "pengarang": "Adam Cohen", "penerbit": "Penguin Press", "stok": 5},
        {"id": "HUK-0008", "judul": "THE CONSTITUTION OF KNOWLEDGE", "tahun": 2022, "pengarang": "Jonathan Rauch", "penerbit": "Brookings Institution Press", "stok": 5},
        {"id": "HUK-0009", "judul": "THE END OF THE WORLD IS JUST THE BEGINNING", "tahun": 2023, "pengarang": "Peter Zeihan", "penerbit": "Harper Business", "stok": 5},
        {"id": "HUK-0010", "judul": "TYRANNY OF THE MINORITY", "tahun": 2024, "pengarang": "Steven Levitsky & Daniel Ziblatt", "penerbit": "Crown Publishing Group", "stok": 5}
    ],
    "Ekonomi": [
        {"id": "E001", "judul": "THE PRICE OF TIME", "tahun": 2022, "pengarang": "Edward Chancellor", "penerbit": "Atlantic Monthly Press", "stok": 5},
        {"id": "E002", "judul": "THE FUTURE OF MONEY", "tahun": 2021, "pengarang": "Eswar S. Prasad", "penerbit": "Harvard University Press", "stok": 5},
        {"id": "E003", "judul": "TRADE WARS ARE CLASS WARS", "tahun": 2020, "pengarang": "Matthew C. Klein & Michael Pettis", "penerbit": "Yale University Press", "stok": 5},
        {"id": "E004", "judul": "HOW THE WORLD REALLY WORKS", "tahun": 2022, "pengarang": "Vaclav Smil", "penerbit": "Viking", "stok": 4},
        {"id": "E005", "judul": "THE KEY MAN", "tahun": 2021, "pengarang": "Simon Clark & Will Louch", "penerbit": "Harper Business", "stok": 5},
        {"id": "E006", "judul": "THE POWER LAW", "tahun": 2022, "pengarang": "Sebastian Mallaby", "penerbit": "Penguin Press", "stok": 5},
        {"id": "E007", "judul": "THE DEFICIT MYTH", "tahun": 2020, "pengarang": "Stephanie Kelton", "penerbit": "PublicAffairs", "stok": 5},
        {"id": "E008", "judul": "RADICAL MARKETS", "tahun": 2019, "pengarang": "Eric A. Posner & Glen Weyl", "penerbit": "Princeton University Press", "stok": 5},
        {"id": "E009", "judul": "DOUGHNUT ECONOMICS", "tahun": 2020, "pengarang": "Kate Raworth", "penerbit": "Chelsea Green Publishing", "stok": 5},
        {"id": "E010", "judul": "MISSION ECONOMY", "tahun": 2021, "pengarang": "Mariana Mazzucato", "penerbit": "Penguin Books", "stok": 5},
    ],
    "Sains": [
        {"id": "SAI-0001", "judul": "BRIEF ANSWERS TO THE BIG QUESTIONS", "tahun": 2018, "pengarang": "Stephen Hawking", "penerbit": "Bantam Books", "stok": 5},
        {"id": "SAI-0002", "judul": "THE ORDER OF TIME", "tahun": 2018, "pengarang": "Carlo Rovelli", "penerbit": "Riverhead Books", "stok": 4},
        {"id": "SAI-0003", "judul": "THE BODY: A GUIDE FOR OCCUPANTS", "tahun": 2019, "pengarang": "Bill Bryson", "penerbit": "Doubleday", "stok": 5},
        {"id": "SAI-0004", "judul": "ENTANGLED LIFE", "tahun": 2020, "pengarang": "Merlin Sheldrake", "penerbit": "Random House", "stok": 5},
        {"id": "SAI-0005", "judul": "A BRIEF HISTORY OF TIME", "tahun": 2021, "pengarang": "Stephen Hawking", "penerbit": "Bantam Books", "stok": 5},
        {"id": "SAI-0006", "judul": "LIFE ON THE EDGE", "tahun": 2021, "pengarang": "Jim Al-Khalili & Johnjoe McFadden", "penerbit": "Broadway Books", "stok": 5},
        {"id": "SAI-0007", "judul": "FUNDAMENTALS", "tahun": 2022, "pengarang": "Frank Wilczek", "penerbit": "Penguin Books", "stok": 5},
        {"id": "SAI-0008", "judul": "THE BIGGEST IDEAS IN THE UNIVERSE", "tahun": 2023, "pengarang": "Sean Carroll", "penerbit": "Dutton", "stok": 5},
        {"id": "SAI-0009", "judul": "THE GENETIC AGE", "tahun": 2023, "pengarang": "Matthew Cobb", "penerbit": "Profile Books", "stok": 5},
        {"id": "SAI-0010", "judul": "THE HIDDEN UNIVERSE", "tahun": 2024, "pengarang": "Alex White", "penerbit": "Orion Publishing", "stok": 5}
    ],
    "Teknologi": [
        {"id": "TEK-0001", "judul": "THE INNOVATORS", "tahun": 2014, "pengarang": "Walter Isaacson", "penerbit": "Simon & Schuster", "stok": 5},
        {"id": "TEK-0002", "judul": "HOW WE GOT TO NOW", "tahun": 2014, "pengarang": "Steven Johnson", "penerbit": "Riverhead Books", "stok": 5},
        {"id": "TEK-0003", "judul": "THE MASTER ALGORITHM", "tahun": 2015, "pengarang": "Pedro Domingos", "penerbit": "Basic Books", "stok": 5},
        {"id": "TEK-0004", "judul": "HOMO DEUS", "tahun": 2017, "pengarang": "Yuval Noah Harari", "penerbit": "Harper", "stok": 5},
        {"id": "TEK-0005", "judul": "ARTIFICIAL INTELLIGENCE", "tahun": 2019, "pengarang": "Melanie Mitchell", "penerbit": "Farrar, Straus and Giroux", "stok": 5},
        {"id": "TEK-0006", "judul": "HUMAN COMPATIBLE", "tahun": 2020, "pengarang": "Stuart Russell", "penerbit": "Viking", "stok": 5},
        {"id": "TEK-0007", "judul": "THE CODE BREAKER", "tahun": 2021, "pengarang": "Walter Isaacson", "penerbit": "Simon & Schuster", "stok": 5},
        {"id": "TEK-0008", "judul": "A THOUSAND BRAINS", "tahun": 2021, "pengarang": "Jeff Hawkins", "penerbit": "Basic Books", "stok": 5},
        {"id": "TEK-0009", "judul": "THE FUTURE IS FASTER THAN YOU THINK", "tahun": 2022, "pengarang": "Peter H. Diamandis & Steven Kotler", "penerbit": "Simon & Schuster", "stok": 5},
        {"id": "TEK-0010", "judul": "CHIP WAR", "tahun": 2023, "pengarang": "Chris Miller", "penerbit": "Scribner", "stok": 5}
    ],
    "Sejarah": [
        {"id": "SEJ-0001", "judul": "SAPIENS", "tahun": 2015, "pengarang": "Yuval Noah Harari", "penerbit": "Harper", "stok": 4},
        {"id": "SEJ-0002", "judul": "GUNS, GERMS, AND STEEL", "tahun": 1997, "pengarang": "Jared Diamond", "penerbit": "W.W. Norton & Company", "stok": 5},
        {"id": "SEJ-0003", "judul": "THE SILK ROADS", "tahun": 2015, "pengarang": "Peter Frankopan", "penerbit": "Bloomsbury Publishing", "stok": 5},
        {"id": "SEJ-0004", "judul": "A PEOPLE'S HISTORY OF THE UNITED STATES", "tahun": 1980, "pengarang": "Howard Zinn", "penerbit": "Harper Perennial", "stok": 5},
        {"id": "SEJ-0005", "judul": "THE RISE AND FALL OF THE THIRD REICH", "tahun": 1960, "pengarang": "William L. Shirer", "penerbit": "Simon & Schuster", "stok": 5},
        {"id": "SEJ-0006", "judul": "THE WRIGHT BROTHERS", "tahun": 2015, "pengarang": "David McCullough", "penerbit": "Simon & Schuster", "stok": 5},
        {"id": "SEJ-0007", "judul": "THE ROAD TO WIGAN PIER", "tahun": 1937, "pengarang": "George Orwell", "penerbit": "Victor Gollancz Ltd", "stok": 5},
        {"id": "SEJ-0008", "judul": "THE SPLENDID AND THE VILE", "tahun": 2020, "pengarang": "Erik Larson", "penerbit": "Crown Publishing Group", "stok": 5},
        {"id": "SEJ-0009", "judul": "CIVILIZATION: THE WEST AND THE REST", "tahun": 2011, "pengarang": "Niall Ferguson", "penerbit": "Penguin Books", "stok": 5},
        {"id": "SEJ-0010", "judul": "THE DAWN OF EVERYTHING", "tahun": 2021, "pengarang": "David Graeber & David Wengrow", "penerbit": "Farrar, Straus and Giroux", "stok": 5}
    ],
}


# Data peminjam dalam bentuk list of dictionaries
daftar_peminjam = [
        {"id_peminjam": "USR-0001", "nama": "AHMAD FAUZI", "judul_buku": "THE MIDNIGHT LIBRARY", "jumlah": 5, "tanggal_pinjam": "05-02-2025"},
        {"id_peminjam": "USR-0002", "nama": "SITI AISYAH", "judul_buku": "PYTHON FOR DATA ANALYSIS", "jumlah": 2, "tanggal_pinjam": "05-02-2025"},
        {"id_peminjam": "USR-0002", "nama": "NUR ARSANI", "judul_buku": "PYTHON FOR DATA ANALYSIS", "jumlah": 3, "tanggal_pinjam": "05-02-2025"},
        {"id_peminjam": "USR-0003", "nama": "BUDI SANTOSO", "judul_buku": "THE RULE OF LAW", "jumlah": 4, "tanggal_pinjam": "06-02-2025"},
        {"id_peminjam": "USR-0004", "nama": "DEWI KARTIKA", "judul_buku": "THE ORDER OF TIME", "jumlah": 1, "tanggal_pinjam": "06-02-2025"},
        {"id_peminjam": "USR-0005", "nama": "RIZKY MAULANA", "judul_buku": "SAPIENS", "jumlah": 1, "tanggal_pinjam": "07-02-2025"},
        {"id_peminjam": "USR-0006", "nama": "ARGA SANTOSO", "judul_buku": "HOW THE WORLD REALLY WORKS", "jumlah": 1, "tanggal_pinjam": "07-02-2025"},
        {"id_peminjam": "USR-0007", "nama": "INDAH PERMATA", "judul_buku": "HOW DEMOCRACIES DIE", "jumlah": 1, "tanggal_pinjam": "07-02-2025"},
        {"id_peminjam": "USR-0008", "nama": "JOKO WIDODO", "judul_buku": "THE SILENT PATIENT", "jumlah": 1, "tanggal_pinjam": "08-02-2025"},
        {"id_peminjam": "USR-0009", "nama": "MEGA CAHYANI", "judul_buku": "INTRODUCTION TO ALGORITHMS", "jumlah": 1, "tanggal_pinjam": "08-02-2025"},
        {"id_peminjam": "USR-0010", "nama": "FAJAR NUGROHO", "judul_buku": "INTRODUCTION TO QUANTUM MECHANICS", "jumlah": 5, "tanggal_pinjam": "09-02-2025"},
        {"id_peminjam": "USR-0011", "nama": "BUDI RAHAYOU", "judul_buku": "INTRODUCTION TO QUANTUM MECHANICS", "jumlah": 1, "tanggal_pinjam": "09-02-2025"},
        {"id_peminjam": "USR-0012", "nama": "RINA LESTARI", "judul_buku": "INTRODUCTION TO ALGORITHMS", "jumlah": 1, "tanggal_pinjam": "10-02-2025"},
        {"id_peminjam": "USR-0013", "nama": "DOSEN UI", "judul_buku": "DEEP LEARNING", "jumlah": 5, "tanggal_pinjam": "11-02-2025"}
]

# Fungsi untuk login ke sistem
def login():
    while True:  # Loop untuk memastikan hanya input valid yang diterima
        print("\n=====  SELAMAT DATANG DI PERPUSTAKAAN TAMAN ISMAIL MARZUKI  =====")
        print("1. " + Fore.GREEN + "Login sebagai Admin")
        print("2. " + Fore.GREEN + "Masuk sebagai Pengunjung")
        print("3. " + Fore.GREEN + "Keluar")

        pilihan = input("Pilih opsi (1-3): ")

        if pilihan == "1":
            while True:  
                username = input(Fore.WHITE + "Masukkan username admin: ")
                password = pwinput.pwinput(Fore.WHITE + "Masukkan password admin: ")

                if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                    print(Fore.GREEN + "\n✅ Berhasil Login sebagai ADMIN!")
                    menu_utama()
                    return  
                else:
                    print(Fore.RED + "\n Username atau password salah! Silakan coba lagi.\n")

        elif pilihan == "2":
            print(Fore.BLUE + "\n✅ Anda masuk sebagai PENGUNJUNG.")
            menu_pengunjung()
            return  

        elif pilihan == "3":
            print(Fore.RED + "\nTerima kasih telah menggunakan sistem perpustakaan!")
            exit()

        else:
            print(Fore.RED + "\nPilihan tidak valid! Silakan coba lagi.")




# -----------------------------------------------------------AKSES USER-----------------------------------------------------------
#Fungsi untuk akses pengunjung
def menu_pengunjung():
    while True:
        print("\n=====  MENU PENGUNJUNG  =====")
        print("1. Lihat Daftar Buku")
        print("2. Wishlist Buku")
        print("3. Keluar")

        pilihan = input("Pilih opsi (1-3): ")

        if pilihan == "1":
            lihat_daftar_buku()
        elif pilihan == "2":
            menu_wishlist()  
        elif pilihan == "3":
            print("\nKeluar dari sistem pengunjung...")
            login()  
        else:
            print("\nPilihan tidak valid! Silakan coba lagi.")


# Fungsi sub-menu wishlist
def menu_wishlist():
    while True:
        print("\n===== WISHLIST =====")
        print("1. Tambah Buku ke Wishlist")
        print("2. Lihat Wishlist")
        print("3. Hapus Buku dari Wishlist")
        print("4. Kembali ke Menu Pengunjung")

        pilihan = input("Pilih opsi (1-3): ")

        if pilihan in ["1", "2", "3"]:
            nama_peminjam = input("Masukkan nama peminjam: ")
        
        if pilihan == "1":
            tambah_ke_wishlist(nama_peminjam)
        elif pilihan == "2":
            lihat_wishlist(nama_peminjam)
        elif pilihan == "3":
            hapus_dari_wishlist(nama_peminjam)
        elif pilihan == "4":
            return  # Untuk kembali ke menu pengunjung
        else:
            print("\nPilihan tidak valid! Silakan coba lagi.")
      

# Fungsi untuk calon peminjam menambah buku ke wishlist
def tambah_ke_wishlist(nama_peminjam):
    """Menambahkan buku ke wishlist jika stoknya 0."""
    nama_peminjam = nama_peminjam.strip().upper()

    if nama_peminjam not in wishlist_buku:
        wishlist_buku[nama_peminjam] = []

    judul_buku = input("Masukkan judul buku yang ingin ditambahkan ke wishlist: ").strip().upper()

    # Mencari buku dalam koleksi
    buku_ditemukan = None
    for kategori in koleksi_buku.values():
        for buku in kategori:
            if buku["judul"].upper() == judul_buku:
                if buku["stok"] == 0:
                    buku_ditemukan = buku
                break  

    if buku_ditemukan:
        wishlist_buku[nama_peminjam].append(judul_buku)
        print(f"\nBuku '{judul_buku}' telah ditambahkan ke wishlist {nama_peminjam.upper()}.\n")
    else:
        print("\nBuku tidak ditemukan atau stoknya masih tersedia. Hanya buku dengan stok 0 yang bisa ditambahkan ke wishlist.")
        print("Kembali ke menu wishlist...\n")


# Fungsi untuk mengecek apakah buku ada di wishlist
def lihat_wishlist(nama_peminjam):
    nama_peminjam = nama_peminjam.upper()
    if nama_peminjam in wishlist_buku and wishlist_buku[nama_peminjam]:
        print(f"\nWishlist {nama_peminjam}:")
        for i, judul in enumerate(wishlist_buku[nama_peminjam], 1):
            print(f"{i}. {judul}")
    else:
        print("\nWishlist Anda kosong.")


# Fungsi untuk menghapus buku dari wishlist
def hapus_dari_wishlist(nama_peminjam):
    nama_peminjam = nama_peminjam.strip().upper()  

    if nama_peminjam not in wishlist_buku or not wishlist_buku[nama_peminjam]:
        print("\nWishlist kosong atau tidak ditemukan.")
        return

    while True:  # Loop agar pengguna bisa memasukkan ulang input jika salah
        print(f"\nWishlist {nama_peminjam.upper()}:")
        for i, buku in enumerate(wishlist_buku[nama_peminjam], start=1):
            print(f"{i}. {buku}")

        pilihan = input("Masukkan nomor buku yang ingin dihapus (pisahkan dengan koma jika lebih dari satu, atau ketik 'all' untuk menghapus semua): ").strip()

        if pilihan.lower() == "all":
            wishlist_buku.pop(nama_peminjam)  
            print(f"\nSemua buku telah dihapus dari wishlist {nama_peminjam}.")
            break  
        else:
            try:
                pilihan_index = sorted(set(int(x) - 1 for x in pilihan.split(",")), reverse=True)

                if any(i < 0 or i >= len(wishlist_buku[nama_peminjam]) for i in pilihan_index):
                    raise IndexError  #Memastikan indeks valid
                
                buku_dihapus = [wishlist_buku[nama_peminjam][i] for i in pilihan_index]

                for i in pilihan_index:
                    del wishlist_buku[nama_peminjam][i]

                for buku in buku_dihapus:
                    print(f"Buku '{buku}' telah dihapus dari wishlist {nama_peminjam}.")
                
                # Jika wishlist menjadi kosong, hapus entri peminjam dari dictionary
                if not wishlist_buku[nama_peminjam]:
                    del wishlist_buku[nama_peminjam]

                break  # Keluar dari loop setelah penghapusan sukses

            except (ValueError, IndexError):
                print("\nInput tidak valid. Pastikan memasukkan nomor yang benar.\nSilakan coba lagi.")





# -----------------------------------------------------AKSES USER DAN ADMIN-----------------------------------------------------
# Fungsi untuk mengurutkan buku berdasarkan judul (A-Z)
def bubble_sort_buku(daftar):
    n = len(daftar)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if daftar[j]["judul"].upper() > daftar[j + 1]["judul"].upper():
                daftar[j], daftar[j + 1] = daftar[j + 1], daftar[j]
    return daftar


# Fungsi untuk melihat daftar koleksi buku
def lihat_daftar_buku():
    while True:  
        print("\nLihat buku berdasarkan:")
        print("1. Judul")
        print("2. Kategori")
        print("3. Semua")

        pilihan = input("Pilih opsi (1-3): ")

        if pilihan == "1":
            judul_buku = input("\nMasukkan judul buku yang ingin dicari: ")
            data_buku = []
            for kategori, daftar in koleksi_buku.items():
                for buku in daftar:
                    if buku["judul"].upper() == judul_buku.upper():
                        data_buku.append([buku["id"], buku["judul"], buku["tahun"], buku["pengarang"], buku["penerbit"], buku["stok"]])

            if data_buku:
                print("\nHasil Pencarian Buku:")
                print(tabulate(data_buku, headers=["ID", "Judul", "Tahun", "Pengarang", "Penerbit", "Stok"], tablefmt="fancy_grid"))
            else:
                print("Buku tidak ditemukan.")

        elif pilihan == "2":
            kategori_list = ["Fiksi", "Akademik & Referensi", "Hukum & Politik", "Ekonomi", "Sains", "Teknologi", "Sejarah"]
            while True:
                print("\nPilih kategori buku:")
                for i, kategori in enumerate(kategori_list, 1):
                    print(f"{i}. {kategori}")
                kategori_input = input("\nMasukkan nomor kategori: ")

                if kategori_input.isdigit() and 1 <= int(kategori_input) <= len(kategori_list):
                    kategori_terpilih = kategori_list[int(kategori_input) - 1]
                    # Mengurutkan buku dalam kategori
                    daftar_terurut = bubble_sort_buku(koleksi_buku[kategori_terpilih])  
                    data_buku = [[buku["id"], buku["judul"], buku["tahun"], buku["pengarang"], buku["penerbit"], buku["stok"]] for buku in daftar_terurut]
                    print(f"\nDaftar buku dalam kategori '{kategori_terpilih}' (A-Z):")
                    print(tabulate(data_buku, headers=["ID", "Judul", "Tahun", "Pengarang", "Penerbit", "Stok"], tablefmt="fancy_grid"))
                    break  
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

        elif pilihan == "3":
            data_buku = []
            for kategori, daftar in koleksi_buku.items():
                daftar_terurut = bubble_sort_buku(daftar)  
                for buku in daftar_terurut:
                    data_buku.append([kategori, buku["id"], buku["judul"], buku["tahun"], buku["pengarang"], buku["penerbit"], buku["stok"]])

            if data_buku:
                print("\nDaftar semua buku di perpustakaan (A-Z per kategori):")
                print(tabulate(data_buku, headers=["Kategori", "ID", "Judul", "Tahun", "Pengarang", "Penerbit", "Stok"], tablefmt="pretty", maxcolwidths=[None, None, 40, None, None, None, None]))
            else:
                print("Tidak ada buku yang tersedia.")

        else:
            print("\nPilihan tidak valid, silakan coba lagi!")
            continue  # Kembali ke awal loop untuk memilih ulang

        # Konfirmasi sebelum kembali ke menu utama
        while True:
            lanjut = input("\nApakah ingin melihat daftar buku lagi? (ya/tidak): ").strip().lower()
            if lanjut == "ya":
                break  
            elif lanjut == "tidak":
                return  
            else:
                print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")





# ------------------------------------------------------AKSES ADMIN-----------------------------------------------------------
# Fungsi untuk menambah koleksi buku
def tambah_buku():
    while True:  # Loop agar tetap dalam fungsi sampai user memilih kembali
        buku = input("Masukkan nama buku: ")
        kategori = input("Buku ditambahkan pada kategori: ")
        pengarang = input("Masukkan nama pengarang: ")
        penerbit = input("Masukkan penerbit: ")
        jumlah = int(input("Masukkan jumlah stok: "))
        tahun = int(input("Masukkan tahun terbit buku: "))

        buku_tambahan = buku.upper()  
        pengarang_buku = pengarang.title()
        penerbit_buku = penerbit.title()
        kategori = kategori.title()

        if kategori in koleksi_buku:
            if buku_tambahan not in [book['judul'] for book in koleksi_buku[kategori]]:
                koleksi_buku[kategori].append({
                    "id": f"{kategori[:3].upper()}-{len(koleksi_buku[kategori]) + 1:04d}",
                    "judul": buku_tambahan,
                    "tahun": tahun,
                    "pengarang": pengarang_buku,
                    "penerbit": penerbit_buku,
                    "stok": jumlah
                })
                print(f"\n✅ Buku '{buku_tambahan}' berhasil ditambahkan ke kategori '{kategori}' dengan stok {jumlah}.")
            else:
                print("Buku sudah ada dalam koleksi.")
        else:
            print("Kategori tidak ditemukan. Silakan pilih kategori yang valid.")

        # Konfirmasi sebelum kembali ke menu
        while True:
            lanjut = input("\nApakah ingin menambah koleksi buku lagi? (ya/tidak): ").strip().lower()
            if lanjut == "ya":
                break  
            elif lanjut == "tidak":
                return  
            else:
                print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")


# Fungsi untuk menghapus buku dari koleksi
def hapus_buku():
    while True: 
        buku = input("Masukkan nama buku yang ingin dihapus: ")

        ditemukan = False
        for kategori in koleksi_buku.keys():
            for item in koleksi_buku[kategori]:
                if item["judul"] == buku.upper():
                    recycle_bin.append({"kategori": kategori, **item})
                    koleksi_buku[kategori].remove(item)
                    print(f"\n✅ Buku '{buku.upper()}' berhasil dihapus dari koleksi.")
                    ditemukan = True
                    break  
            if ditemukan:
                break  
        
        if not ditemukan:
            print("Buku tidak ditemukan.\nSilakan cari lagi.")

        # Konfirmasi sebelum kembali ke menu
        while True:
            lanjut = input("\nApakah ingin menghapus buku lagi? (ya/tidak): ").strip().lower()
            if lanjut == "ya":
                break  
            elif lanjut == "tidak":
                return  
            else:
                print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")


# Fungsi untuk peminjaman buku
def pinjam_buku():
    while True:
        print("\nPeminjaman Buku")
        nama_peminjam = input("Masukkan nama peminjam: ").strip()
        buku = input("Masukkan nama buku yang ingin dipinjam: ").strip()
        jumlah_pinjam = int(input("Masukkan jumlah buku yang ingin dipinjam: "))

        # Validasi format tanggal
        while True:
            tanggal_peminjaman = input("Masukkan tanggal peminjaman (DD-MM-YYYY): ").strip()
            if re.match(r"^\d{2}-\d{2}-\d{4}$", tanggal_peminjaman):
                try:
                    datetime.strptime(tanggal_peminjaman, "%d-%m-%Y")
                    break  
                except ValueError:
                    print("Format tanggal salah! Pastikan tanggal valid (DD-MM-YYYY).")
            else:
                print("Format tanggal harus DD-MM-YYYY.")

        # Format input agar seragam
        buku_formatted = buku.upper()
        peminjam_formatted = nama_peminjam.upper()

        ditemukan = False
        for kategori, daftar in koleksi_buku.items():
            for item in daftar:
                if item["judul"] == buku_formatted:
                    ditemukan = True
                    if item["stok"] >= jumlah_pinjam:
                        # Proses peminjaman jika stok cukup
                        item["stok"] -= jumlah_pinjam
                        id_peminjam = f"USR-{len(daftar_peminjam) + 1:04d}"

                        daftar_peminjam.append({
                            "id_peminjam": id_peminjam,
                            "nama": peminjam_formatted,
                            "judul_buku": item["judul"],
                            "jumlah": jumlah_pinjam,
                            "tanggal_pinjam": tanggal_peminjaman
                        })

                        print(f"\n✅ Buku '{item['judul']}' berhasil dipinjam oleh {peminjam_formatted}. Sisa stok: {item['stok']}")

                        # Hapus buku dari wishlist setelah dipinjam
                        if peminjam_formatted in wishlist_buku and buku_formatted in wishlist_buku[peminjam_formatted]:
                            wishlist_buku[peminjam_formatted].remove(buku_formatted)
                            print(f"Buku '{buku_formatted}' telah dihapus dari wishlist {peminjam_formatted}.")
                        break  
                    else:
                        print("\nStok tidak mencukupi!")
                    break  
            if ditemukan:
                break

        if not ditemukan:
            print("\nBuku tidak ditemukan dalam koleksi.")

        # Konfirmasi sebelum kembali ke menu utama
        while True:
            lanjut = input("\nApakah ingin meminjam buku lagi? (ya/tidak): ").strip().lower()
            if lanjut == "ya":
                break
            elif lanjut == "tidak":
                return
            else:
                print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")


# Fungsi untuk Admin Cek Wishlist Setelah Pengembalian
def cek_wishlist_setelah_pengembalian(judul_buku):
    judul_buku = judul_buku.upper()  
    
    ada_wishlist = False
    for peminjam, buku_list in wishlist_buku.items():
        if judul_buku in [b.upper() for b in buku_list]:  
            ada_wishlist = True
            print(f"Ada yang menunggu buku '{judul_buku}' dalam wishlist!")
            return  
    
    if not ada_wishlist:
        print(f"Tidak ada yang menunggu buku '{judul_buku}' dalam wishlist.")


# Fungsi untuk pengembalian buku
def kembalikan_buku():
    while True:
        print("\nPengembalian Buku")
        # Memastikan nama peminjam dan buku ada dalam daftar sebelum lanjut
        while True:
            nama_peminjam = input("Masukkan nama peminjam: ").strip().upper()
            buku = input("Masukkan nama buku yang dikembalikan: ").strip().upper()
            
            peminjam_ditemukan = None
            for peminjam in daftar_peminjam:
                if peminjam["nama"].upper() == nama_peminjam and peminjam["judul_buku"].upper() == buku:
                    peminjam_ditemukan = peminjam
                    break
            
            if peminjam_ditemukan:
                break
            else:
                print("\nData peminjaman tidak ditemukan! Harap masukkan data yang valid.\n")

        while True:
            try:
                jumlah_kembali = int(input("Masukkan jumlah buku yang dikembalikan: "))
                if jumlah_kembali <= 0 or jumlah_kembali > peminjam_ditemukan["jumlah"]:
                    print(f"\nJumlah buku tidak valid! Anda hanya dapat mengembalikan hingga {peminjam_ditemukan['jumlah']} buku.")
                    continue
                break
            except ValueError:
                print("\nInput tidak valid! Masukkan angka.")

        # Validasi input tanggal
        while True:
            tanggal_pengembalian = input("Masukkan tanggal pengembalian (DD-MM-YYYY): ").strip()
            try:
                tanggal_kembali = datetime.strptime(tanggal_pengembalian, "%d-%m-%Y")
                break  
            except ValueError:
                print("\nFormat tanggal salah! Harap masukkan dengan format DD-MM-YYYY.")

        # Cek keterlambatan
        tanggal_peminjaman = datetime.strptime(peminjam_ditemukan["tanggal_pinjam"], "%d-%m-%Y")
        
        terlambat = (tanggal_kembali - tanggal_peminjaman).days > 7
        if terlambat:
            denda = 20000
            print("\nBuku dikembalikan terlambat! Denda berlaku.")
            print(f"Denda yang harus dibayar: Rp {denda}")

            while True:
                try:
                    pembayaran = int(input("Masukkan jumlah yang dibayarkan: Rp "))
                    if pembayaran < denda:
                        print(f"\nJumlah yang dibayarkan kurang. Silakan masukkan Rp {denda}.")
                    else:
                        kembalian = pembayaran - denda
                        print(f"\n✅ Pembayaran berhasil! Anda telah membayar Rp {pembayaran}.")
                        if kembalian > 0:
                            print(f"Kembalian Anda: Rp {kembalian}")
                        break  
                except ValueError:
                    print("\nInput tidak valid! Masukkan angka.")

        # Update stok buku
        for kategori, daftar in koleksi_buku.items():
            for item in daftar:
                if item["judul"].upper() == buku:
                    item["stok"] += jumlah_kembali
                    print(f"\n✅ Buku '{buku}' berhasil dikembalikan oleh {nama_peminjam}. Stok sekarang: {item['stok']}")

                    # Cek wishlist setelah stok bertambah
                    cek_wishlist_setelah_pengembalian(buku)
                    break
        
        # Update jumlah buku yang dipinjam atau hapus data peminjam
        if jumlah_kembali < peminjam_ditemukan["jumlah"]:
            peminjam_ditemukan["jumlah"] -= jumlah_kembali  # Kurangi jumlah buku
        else:
            daftar_peminjam.remove(peminjam_ditemukan)  # Hapus jika semua dikembalikan

        while True:
            lanjut = input("\nApakah ingin mengembalikan buku lagi? (ya/tidak): ").strip().lower()
            if lanjut == "ya":
                break  
            elif lanjut == "tidak":
                return  
            else:
                print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")


# Fungsi untuk daftar data peminjam
def lihat_daftar_peminjam():
    while True:
        # Cek jika daftar peminjam kosong
        if not daftar_peminjam: 
            print("\nBelum ada peminjam saat ini.")
        else:
            data_peminjam = [[peminjam["nama"], peminjam["judul_buku"], peminjam["jumlah"]] for peminjam in daftar_peminjam]
            print("\nDaftar Peminjam")
            print(tabulate(data_peminjam, headers=["Nama", "Judul Buku", "Jumlah"], tablefmt="fancy_grid"))

        # Konfirmasi sebelum kembali ke menu utama
        kembali = input("\nTekan 1 untuk kembali ke menu utama: ").strip()
        if kembali == "1":
            break  
        else:
            print("Input tidak valid! Silakan tekan 1 untuk kembali.")


#Fugsi untuk mengembalikan buku dari recycle bin
def restore_buku():
    if not recycle_bin:
        print("\nRecycle Bin kosong. Tidak ada buku untuk dikembalikan.")
        return
    
    while True:
        # Tampilkan daftar buku di Recycle Bin
        print("\nBuku dalam Recycle Bin:")
        for i, buku in enumerate(recycle_bin):
            print(f"{i + 1}. {buku['judul']} ({buku['kategori']})")

        try:
            # Input beberapa angka dipisahkan koma atau spasi
            pilihan = input("\nMasukkan nomor buku yang ingin dikembalikan (pisahkan dengan koma/spasi): ")
            pilihan_list = pilihan.replace(",", " ").split() 
            
            # Konversi ke angka dan validasi
            pilihan_angka = [int(num) - 1 for num in pilihan_list if num.isdigit()]
            pilihan_angka = sorted(set(pilihan_angka), reverse=True)  

            if not pilihan_angka:
                print("Input tidak valid! Masukkan angka yang sesuai.")
                continue

            # Pastikan semua angka dalam rentang yang valid
            if any(i < 0 or i >= len(recycle_bin) for i in pilihan_angka):
                print("Ada nomor yang tidak valid. Coba lagi.")
                continue

            # Restore buku satu per satu
            for i in pilihan_angka:
                buku_dipulihkan = recycle_bin.pop(i)
                koleksi_buku[buku_dipulihkan["kategori"]].append(buku_dipulihkan)
                print(f"✅ Buku '{buku_dipulihkan['judul']}' dikembalikan ke koleksi.")

            # Konfirmasi apakah ingin me-restore lagi
            while True:
                lanjut = input("\nApakah ingin mengembalikan buku lain? (ya/tidak): ").strip().lower()
                if lanjut == "ya":
                    break  
                elif lanjut == "tidak":
                    return  # Keluar dari fungsi, kembali ke menu utama
                else:
                    print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")
        
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")


# Fungsi menu admin
def menu_utama():
    while True:
        daftar_menu = [
            ["1", "Tambah Buku"],
            ["2", "Hapus Buku"],
            ["3", "Lihat Daftar Buku"],
            ["4", "Pinjam Buku"],
            ["5", "Kembalikan Buku"],
            ["6", "Lihat Daftar Peminjam"],
            ["7", "Restore Buku dari Recycle Bin"],
            ["8", "Keluar"]
        ]

        print("\nMENU UTAMA")
        print(tabulate(daftar_menu, headers=["No", "Menu"], tablefmt="fancy_grid"))  
        
        pilihan = input("Pilih menu (1-7): ")

        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            hapus_buku()
        elif pilihan == "3":
            lihat_daftar_buku()
        elif pilihan == "4":
            pinjam_buku()
        elif pilihan == "5":
            kembalikan_buku()
        elif pilihan == "6":
            lihat_daftar_peminjam()
        elif pilihan == "7":
            restore_buku() 
        elif pilihan == "8":
            print("\nTerima kasih! Selamat Beristirahat.")
            login() 
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# Program utama
login()
menu_utama()
