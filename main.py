import csv

def find_matching_kode_akun():
    jurnal_filename = 'jurnal.csv'
    coa_filename = 'coa.csv'
    
    jurnal_kode_akun = set()
    coa_kode_akun = set()
    jurnal_nama_akun = set()
    coa_nama_akun = set()
    
    matching_kode_akun = set()
    unmatched_kode_akun = set()
    matching_nama_akun = set()
    unmatched_nama_akun = set()
    
    with open(jurnal_filename, 'r') as jurnal_file:
        jurnal_reader = csv.reader(jurnal_file)
        next(jurnal_reader)  # Skip header row
        for row in jurnal_reader:
            kode_akun = row[3]
            nama_akun = row[2]
            jurnal_kode_akun.add(kode_akun)
            jurnal_nama_akun.add(nama_akun)
    
    with open(coa_filename, 'r') as coa_file:
        coa_reader = csv.reader(coa_file)
        next(coa_reader)  # Skip header row
        for row in coa_reader:
            kode_akun = row[1]
            nama_akun = row[0]
            coa_kode_akun.add(kode_akun)
            coa_nama_akun.add(nama_akun)
    
    matching_kode_akun = jurnal_kode_akun.intersection(coa_kode_akun)
    unmatched_kode_akun = jurnal_kode_akun.symmetric_difference(coa_kode_akun)
    matching_nama_akun = jurnal_nama_akun.intersection(coa_nama_akun)
    unmatched_nama_akun = jurnal_nama_akun.symmetric_difference(coa_nama_akun)
    
    print("Daftar Kode Akun yang ada di Jurnal dan ada di COA:")
    for kode_akun in matching_kode_akun:
        print(kode_akun)
    
    print("\nDaftar Kode Akun yang ada di Jurnal tetapi tidak ada di COA:")
    if len(unmatched_kode_akun) == 0:
        print("Tidak ada data")
    else:
        for kode_akun in unmatched_kode_akun:
            print(kode_akun)
    
    print("\nDaftar Nama Akun yang ada di Jurnal dan ada di COA:")
    for nama_akun in matching_nama_akun:
        print(nama_akun)
    
    print("\nDaftar Nama Akun yang ada di Jurnal tetapi tidak ada di COA:")
    if len(unmatched_nama_akun) == 0:
        print("Tidak ada data")
    else:
        for nama_akun in unmatched_nama_akun:
            print(nama_akun)

# Call the function
find_matching_kode_akun()