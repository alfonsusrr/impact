Jalankan program dengan: python [atau python3] covid.py

1. Load data statistik (masukkan file csv data statistik contoh: statistik.csv)
2. Key (adalah input untuk menjalankan fungsi), optionnya adalah:
    - add: menambah data statistik
    - average [-tanggal]: menampilkan rata rata penambahan pada tanggal tertentu
    - exit: keluar dari program
    - help: bantuan untuk menggunakan program
    - laju [-provinsi] [-tanggal]: menampilkan laju penambahan pada suatu provinsi hingga tanggal tertentu
    - save: menyimpan pembaharuan data
    - sort [-sort by (penderita/sembuh/kematian)] [-tanggal]: menampilkan urutan data pada tanggal tertentu
    - show [-show by (tanggal)] [-specific tanggal]: menampilkan urutan data pada tanggal tertentu
    - show [-show by (provinsi)] [-specific provinsi]: menampilkan urutan data pada tanggal tertentu
    - top [-tanggal]: menampilkan data terbanyak dan tersedikit pada tanggal tertentu
3. Format input tanggal yang benar: DD/MM/YYYY (bilangan 1 digit ditulis 2 digit), Contoh: 01/01/2001
4. Format input provinsi harus sesuai dengan list provinsi yang ada, yakni: STEI ITB, DE Impact, Salting, Kekaosan, Girintili, Par, Tibis, KTOM, Daspro, atau Rebeel (caps lock yang digunakan harus sesuai/ case-sensitive)
5. Ketika keluar dari program (dengan key: exit) maka program akan otomasis menyimpan data yang ditambah

Program ini dibuat sebagai tugas "PROBLEM SOLVING KOMPUTER - SEMIFINAL IMPACT 2020"
Dibuat oleh: Tim Altair - Impact 2020