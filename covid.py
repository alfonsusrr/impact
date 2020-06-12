import csv

data_covid = []
provinsi_list = []
data_new = []

def load():
    filename = input("Masukkan nama file data statistik: ")
    try:
        file = open(filename, "r")
    except:
        print("File tidak ditemukan")
        return 1
    else:
        file_reader = csv.reader(file)
        for provinsi, tanggal, penderita, sembuh, kematian in file_reader:
            if provinsi.lower() != "provinsi":
                data = {"provinsi" : provinsi, "tanggal" : tanggal, "penderita" : int(penderita), "sembuh" : int(sembuh), "kematian" : int(kematian)}
                if provinsi not in provinsi_list:
                    provinsi_list.append(provinsi.lower())
                data_covid.append(data)
        file.close()
        print("File data statistik sudah terbaca")
        return 0

def save():
    filename = input("Masukkan nama file data statistik: ")
    try:
        file = open(filename, "w")
    except:
        print("File tidak ditemukan")
        return 1
    else:
        file_writer = csv.writer(file, lineterminator='\n')
        for x in range(len(data_new)):
            data_add = [data_new[x]['provinsi'], data_new[x]['tanggal'], data_new[x]['penderita'], data_new[x]['sembuh'], data_new[x]['kematian']]
            file_writer.writerow(data_add)
        file.close()
        print("File data statistik sudah tersimpan")
        for x in range(len(data_new)):
            data_covid.append(data_new[x].copy())
        return 0

def show_prov(prov):
    if prov.lower() not in provinsi_list:
        print(f"Data tidak ditemukan untuk provinsi {prov}")
    else:
        data = []
        data.clear()
        for x in range(len(data_covid)):
            if data_covid[x]["provinsi"].lower() == prov.lower():
                data.append(data_covid[x].copy())
                
        for y in range(len(data)):
            data[y]['tanggal'] = data[y]['tanggal'].split('/')
        
        data = sorted(data, key=lambda x: (x['tanggal'][2], x['tanggal'][1], x['tanggal'][0]))

        print(f"Data penyebaran COVID-19 di Provinsi {prov}")
        print("Tanggal    | Penderita | Sembuh | Kematian ")
        for x in range(len(data)):
            print(data[x]['tanggal'][0] + "/" + data[x]['tanggal'][1] + "/" + data[x]['tanggal'][2],"|",data[x]['penderita'], " "*(8 - len(str(data[x]['penderita']))),"|",data[x]['sembuh'], " "*(5 - len(str(data[x]['sembuh']))),"|",data[x]['kematian'])
        data.clear()

def show_date(date):
    data = []
    data.clear()
    for x in range(len(data_covid)):
        if data_covid[x]["tanggal"] == date:
            data.append(data_covid[x].copy())
    if len(data) == 0:
        print(f"Data tidak ditemukan pada tanggal {date}")
    else:
        data = sorted(data, key=lambda x: x['provinsi'])
        print(f"Berikut adalah data statistik COVID-19 pada tanggal {date}")
        print("Provinsi   | Penderita | Sembuh | Kematian ")
        for x in range(len(data)):
            print(data[x]['provinsi']," "*(9 - len(data[x]['provinsi'])),"|",data[x]['penderita'], " "*(8 - len(str(data[x]['penderita']))),"|",data[x]['sembuh'], " "*(5 - len(str(data[x]['sembuh']))),"|",data[x]['kematian'])
    data.clear()

def sort(by, date):
    data = []
    data.clear()
    for x in range(len(data_covid)):
        if data_covid[x]["tanggal"] == date:
            data.append(data_covid[x].copy())
    if len(data) == 0:
        print(f"Data tidak ditemukan pada tanggal {date}")
    else:
        data = sorted(data, key=lambda x: x[by])
        if by == "penderita":
            print(f"Berikut adalah data statistik COVID-19 pada tanggal {date} terurut menaik berdasarkan jumlah kumulatif penderita")
        elif by == "sembuh":
            print(f"Berikut adalah data statistik COVID-19 pada tanggal {date} terurut menaik berdasarkan jumlah kumulatif penderita yang sembuh")
        else:
            print(f"Berikut adalah data statistik COVID-19 pada tanggal {date} terurut menaik berdasarkan angka kematian")
        print("Provinsi   | Penderita | Sembuh | Kematian ")
        for x in range(len(data)):
            print(data[x]['provinsi']," "*(9 - len(data[x]['provinsi'])),"|",data[x]['penderita'], " "*(8 - len(str(data[x]['penderita']))),"|",data[x]['sembuh'], " "*(5 - len(str(data[x]['sembuh']))),"|",data[x]['kematian'])
    data.clear()

def average(date):
    penderita = 0
    sembuh = 0
    kematian = 0
    total = 0
    for x in range(len(data_covid)):
        if data_covid[x]["tanggal"] == date:
            penderita += data_covid[x]["penderita"]
            sembuh += data_covid[x]["sembuh"]
            kematian += data_covid[x]["kematian"]
            total += 1
    if total == 0:
        print(f"Data tidak ditemukan pada tanggal {date}")
    else:
        avg_penderita = int(round(penderita/total, 0))
        avg_sembuh = int(round(sembuh/total, 0))
        avg_kematian = int(round(kematian/total, 0))
        print(f"Berikut adalah rata-rata data statistik COVID-19 pada tanggal {date}")
        print(f"Jumlah rata-rata penderita = {avg_penderita}")
        print(f"Jumlah rata-rata penderita yang sembuh = {avg_sembuh}")
        print(f"Angka kematian rata-rata = {avg_kematian}")
    
def add():
    print("Masukkan informasi statistik COVID-19 yang ditambahkan:")
    prov = "falsedata"
    while prov.lower() not in provinsi_list:
        prov = input("Masukkan nama provinsi: ")
        if prov.lower() not in provinsi_list:
            print(f"Nama provinsi tidak ditemukan, masukkan nama provinsi yang sesuai")
    date = input("Masukkan tanggal pencatatan (DD/MM/YYYY): ")
    penderita = input("Masukkan jumlah penderita yang tercatat: ")
    sembuh = input("Masukkan jumlah penderita yang sudah sembuh: ")
    kematian = input("Masukkan angka kematian akibat COVID-19: ")
    data = {"provinsi" : prov, "tanggal" : date, "penderita" : penderita, "sembuh" : sembuh, "kematian" : kematian}
    data_new.append(data)

def top(date):
    total = 0
    penderita = []
    sembuh = []
    kematian = []
    
    for x in range(len(data_covid)):
        if data_covid[x]['tanggal'] == date:
            penderita.append(data_covid[x]['penderita'])
            sembuh.append(data_covid[x]['sembuh'])
            kematian.append(data_covid[x]['kematian'])
            total += 1
    if total == 0:
        print(f"Data tidak ditemukan pada tanggal {date}")

    else:     
        penderita_banyak = []
        sembuh_banyak = []
        kematian_banyak = []
        penderita_sedikit = []
        sembuh_sedikit = []
        kematian_sedikit = []

        lowest_penderita = min(penderita)
        highest_penderita = max(penderita)
        lowest_sembuh = min(sembuh)
        highest_sembuh = max(sembuh)
        lowest_kematian = min(kematian)
        highest_kematian = max(kematian)

        for x in range(len(data_covid)):
            if data_covid[x]['penderita'] == lowest_penderita:
                penderita_sedikit.append(data_covid[x])
            elif data_covid[x]['penderita'] == highest_penderita:
                penderita_banyak.append(data_covid[x])
            
            if data_covid[x]['sembuh'] == lowest_sembuh:
                sembuh_sedikit.append(data_covid[x])
            elif data_covid[x]['sembuh'] == highest_sembuh:
                sembuh_banyak.append(data_covid[x])

            if data_covid[x]['kematian'] == lowest_kematian:
                kematian_sedikit.append(data_covid[x])
            elif data_covid[x]['kematian'] == highest_kematian:
                kematian_banyak.append(data_covid[x])
        print(f"Berikut adalah data statistik COVID-19 pada tanggal {date}")
        print("Dengan :")
        print("1. Jumlah Kumulatif Penderita Terbanyak")
        for x in range(len(penderita_banyak)):
            print(penderita_banyak[x]['provinsi']," "*(9 - len(penderita_banyak[x]['provinsi'])),"|",penderita_banyak[x]['penderita'], " "*(8 - len(str(penderita_banyak[x]['penderita']))),"|",penderita_banyak[x]['sembuh'], " "*(5 - len(str(penderita_banyak[x]['sembuh']))),"|",penderita_banyak[x]['kematian'])
        print("2. Jumlah Kumulatif Penderita Tersedikit")
        for x in range(len(penderita_sedikit)):
            print(penderita_sedikit[x]['provinsi']," "*(9 - len(penderita_sedikit[x]['provinsi'])),"|",penderita_sedikit[x]['penderita'], " "*(8 - len(str(penderita_sedikit[x]['penderita']))),"|",penderita_sedikit[x]['sembuh'], " "*(5 - len(str(penderita_sedikit[x]['sembuh']))),"|",penderita_sedikit[x]['kematian'])
        print("3. Jumlah Kumulatif Penderita yang Sembuh Terbanyak")
        for x in range(len(sembuh_banyak)):
            print(sembuh_banyak[x]['provinsi']," "*(9 - len(sembuh_banyak[x]['provinsi'])),"|",sembuh_banyak[x]['penderita'], " "*(8 - len(str(sembuh_banyak[x]['penderita']))),"|",sembuh_banyak[x]['sembuh'], " "*(5 - len(str(sembuh_banyak[x]['sembuh']))),"|",sembuh_banyak[x]['kematian'])
        print("4. Jumlah Kumulatif Penderita yang Sembuh Tersedikit")
        for x in range(len(sembuh_sedikit)):
            print(sembuh_sedikit[x]['provinsi']," "*(9 - len(sembuh_sedikit[x]['provinsi'])),"|",sembuh_sedikit[x]['penderita'], " "*(8 - len(str(sembuh_sedikit[x]['penderita']))),"|",sembuh_sedikit[x]['sembuh'], " "*(5 - len(str(sembuh_sedikit[x]['sembuh']))),"|",sembuh_sedikit[x]['kematian'])
        print("5. Angka Kematian Terbanyak")
        for x in range(len(kematian_banyak)):
            print(kematian_banyak[x]['provinsi']," "*(9 - len(kematian_banyak[x]['provinsi'])),"|",kematian_banyak[x]['penderita'], " "*(8 - len(str(kematian_banyak[x]['penderita']))),"|",kematian_banyak[x]['sembuh'], " "*(5 - len(str(kematian_banyak[x]['sembuh']))),"|",kematian_banyak[x]['kematian'])
        print("6. Angka Kematian Tersedikit")
        for x in range(len(kematian_sedikit)):
            print(kematian_sedikit[x]['provinsi']," "*(9 - len(kematian_sedikit[x]['provinsi'])),"|",kematian_sedikit[x]['penderita'], " "*(8 - len(str(kematian_sedikit[x]['penderita']))),"|",kematian_sedikit[x]['sembuh'], " "*(5 - len(str(kematian_sedikit[x]['sembuh']))),"|",kematian_sedikit[x]['kematian'])
            
def laju(prov, date):
    if prov.lower() not in provinsi_list:
        print(f"Tidak ditemukan data untuk provinsi {prov}")
    else:
        date_print = date
        data = []
        data_laju = []
        penderita = 0
        sembuh = 0
        kematian = 0
        total_laju = 0
        date = date.split('/')
        for x in range(len(data_covid)):
            if data_covid[x]['provinsi'].lower() == prov.lower():
                data.append(data_covid[x].copy())
            
        for y in range(len(data)):
            data[y]['tanggal'] = data[y]['tanggal'].split('/')
            if int(data[y]['tanggal'][2]) < int(date[2]):
                data_laju.append(data[y])
                penderita += data[y]['penderita']
                sembuh += data[y]['sembuh']
                kematian += data[y]['kematian']
                total_laju += 1
            elif int(data[y]['tanggal'][2]) == int(date[2]):
                if int(data[y]['tanggal'][1]) < int(date[1]):
                    data_laju.append(data[y])
                    penderita += data[y]['penderita']
                    sembuh += data[y]['sembuh']
                    kematian += data[y]['kematian']
                    total_laju += 1
                elif int(data[y]['tanggal'][1]) == int(date[1]):
                    if int(data[y]['tanggal'][0]) <= int(date[0]):
                        data_laju.append(data[y])
                        penderita += data[y]['penderita']
                        sembuh += data[y]['sembuh']
                        kematian += data[y]['kematian']
                        total_laju += 1
        if total_laju <= 0:
            print(f"Data tidak ditemukan untuk laju hingga tanggal {date_print}")
        else:
            laju_penderita = int(round(penderita/total_laju, 0))
            laju_sembuh = int(round(sembuh/total_laju, 0))
            laju_kematian = int(round(kematian/total_laju, 0))
        
            print(f"Laju rata-rata penyebaran dan pencegahan COVID-19 di provinsi {prov} sampai dengan tanggal {date_print}")
            print(f"Penderita : {laju_penderita}")
            print(f"Sembuh    : {laju_sembuh}")
            print(f"Kematian  : {laju_kematian}")
        

def main():
    read = False
    while read == False:
        x = load()
        if x != 1:
            read = True
        else:
            read = False

    run = True
    while run == True:
        print("Key: ", end='')
        cmd = input()
        if cmd.lower() == 'exit':
            run = False
        elif cmd.lower() == 'help':
            print("add: menambah data statistik")
            print("average [-tanggal]: menampilkan rata rata penambahan pada tanggal tertentu")
            print("exit: keluar dari program")
            print("help: bantuan untuk menggunakan program")
            print("laju [-provinsi] [-tanggal]: menampilkan laju penambahan pada suatu provinsi hingga tanggal tertentu")
            print("save: menyimpan pembaharuan data")
            print("sort [-sort by (penderita/sembuh/kematian)] [-tanggal]: menampilkan urutan data pada tanggal tertentu sesuai urutan tertentu")
            print("show [-show by (tanggal)] [-specific tanggal]: menampilkan data berdasarkan tanggal tertentu")
            print("show [-show by (provinsi)] [-specific provinsi]: menampilkan data berdasarkan provinsi tertentu")
            print("top [-tanggal]: menampilkan data terbanyak dan tersedikit pada tanggal tertentu")
        elif cmd.lower() == 'show':
            arg1 = input("Tampilkan berdasarkan: ")
            if arg1.lower() == "provinsi":
                arg2 = input("Provinsi: ")
                print("----------")
                show_prov(arg2)
                print("----------")
            elif arg1.lower() == "tanggal":
                arg2 = input("Tanggal: ")
                print("----------")
                show_date(arg2)
                print("----------")
            else:
                print("Usage: show [provinsi/tanggal] [specific provinsi/tanggal]")
        elif cmd.lower() == 'sort':
            arg1 = input("Urutkan berdasarkan: ")
            if arg1.lower() == "penderita":
                arg2 = input("Tanggal: ")
                print("----------")
                sort(arg1.lower(), arg2)
                print("----------")
            elif arg1.lower() == "sembuh":
                arg2 = input("Tanggal: ")
                print("----------")
                sort(arg1.lower(), arg2)
                print("----------")
            elif arg1.lower() == "kematian":
                arg2 = input("Tanggal: ")
                print("----------")
                sort(arg1.lower(), arg2)
                print("----------")
            else:
                print("Usage: sort [sort by (penderita/sembuh/kematian)] [tanggal (dd/mm/yyyy)]")
        elif cmd.lower() == 'average':
            arg1 = input("Tanggal: ")
            if arg1.lower() != "":
                print("----------")
                average(arg1)
                print("----------")
            else:
                print("Usage: average [tanggal (dd/mm/yyyy)]")
        elif cmd.lower() == 'top':
            arg1 = input("Tanggal: ")
            if arg1.lower() != "":
                print("----------")
                top(arg1)
                print("----------")
            else:
                print("Usage: top [tanggal (dd/mm/yyyy)]")
        elif cmd.lower() == 'laju':
            arg1 = input("Provinsi: ")
            arg2 = input("Hingga tanggal: ")
            if arg1.lower() != "" and arg2.lower() != "":
                print("----------")
                laju(arg1, arg2)
                print("----------")
            else:
                print("Usage: laju [provinsi] [tanggal (dd/mm/yyyy)]")
        elif cmd.lower() == 'add':
            print("----------")
            add()
            print("----------")
        elif cmd.lower() == 'save':
            print("----------")
            save()
            data_new.clear()
            print("----------")
        else:
            print("Command tidak ditemukan")
            print("----------")
            print("Daftar command yang ada:")
            print("add: menambah data statistik")
            print("average [-tanggal]: menampilkan rata rata penambahan pada tanggal tertentu")
            print("exit: keluar dari program")
            print("help: bantuan untuk menggunakan program")
            print("laju [-provinsi] [-tanggal]: menampilkan laju penambahan pada suatu provinsi hingga tanggal tertentu")
            print("save: menyimpan pembaharuan data")
            print("sort [-sort by (penderita/sembuh/kematian)] [-tanggal]: menampilkan urutan data pada tanggal tertentu sesuai urutan tertentu")
            print("show [-show by (tanggal)] [-specific tanggal]: menampilkan data berdasarkan tanggal tertentu")
            print("show [-show by (provinsi)] [-specific provinsi]: menampilkan data berdasarkan provinsi tertentu")
            print("top [-tanggal]: menampilkan data terbanyak dan tersedikit pada tanggal tertentu")
            print("----------")
    if len(data_new) != 0:
        save()

if __name__ == '__main__':
    main()