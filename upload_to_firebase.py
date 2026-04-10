"""
Script Upload Data Alumni ke Firebase Realtime Database
=======================================================
Cara pakai:
1. Install dependency:
   pip install requests openpyxl

2. Letakkan file Excel alumni di folder yang sama dengan script ini

3. Jalankan:
   python upload_to_firebase.py
"""

import json, time, random, requests, openpyxl, os, glob

# ===================== KONFIGURASI =====================
FIREBASE_URL = "https://alumni-tracker-84ee8-default-rtdb.firebaseio.com"
BATCH_SIZE   = 500
# =======================================================

# Auto-detect file Excel
xlsx_files = glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "*.xlsx"))
if not xlsx_files:
    print("ERROR: Tidak ada file .xlsx di folder ini!")
    exit(1)
elif len(xlsx_files) == 1:
    EXCEL_FILE = xlsx_files[0]
    print(f"File Excel ditemukan: {os.path.basename(EXCEL_FILE)}")
else:
    print("File Excel yang ditemukan:")
    for i, f in enumerate(xlsx_files):
        print(f"  [{i+1}] {os.path.basename(f)}")
    pilihan = input("Pilih nomor file: ").strip()
    EXCEL_FILE = xlsx_files[int(pilihan) - 1]

# ===== DATA DUMMY KONTAK =====
perusahaan = [
    "PT Telkom Indonesia","PT Bank BRI","PT Unilever Indonesia","Dinas Pendidikan Kota Malang",
    "PT Pertamina","PT PLN Persero","Universitas Brawijaya","RS Saiful Anwar","PT Astra International",
    "Badan Pusat Statistik","PT Bank Mandiri","PT Indofood","Pemkot Malang","PT Bukalapak",
    "PT Gojek Indonesia","Dinas Kesehatan Jawa Timur","PT Bank BNI","PT Garuda Indonesia",
    "PT XL Axiata","Kementerian Keuangan RI","PT Tokopedia","PT Bank CIMB Niaga",
    "PT Mayora Indah","PT Sinar Mas","Politeknik Negeri Malang","RSUD Dr. Soetomo",
    "PT Krakatau Steel","PT Pupuk Indonesia","Kantor Pajak Malang","PT Bank Danamon",
    "PT Pegadaian","PT Pos Indonesia","Diskominfo Kota Malang","PT Kimia Farma",
    "BPJS Kesehatan","PT Jasa Marga","Pemkab Malang","Universitas Negeri Malang"
]
posisi = [
    "Staff Akuntansi","Manajer Keuangan","Analis Data","Guru","Dosen","Direktur",
    "HRD Manager","Marketing Executive","Software Engineer","Kepala Bagian","Auditor",
    "Konsultan","Supervisor","General Manager","Staff IT","Kepala Sekolah",
    "Perawat","Dokter","Pengusaha","Wirausahawan","Staff Administrasi","Branch Manager",
    "Finance Officer","Legal Officer","Tax Consultant","Project Manager","Business Analyst"
]
status_list = ["PNS","PNS","Swasta","Swasta","Swasta","Wirausaha"]
kota = ["Malang","Surabaya","Jakarta","Bandung","Yogyakarta","Semarang","Bali",
        "Medan","Makassar","Solo","Sidoarjo","Pasuruan","Kediri","Blitar","Mojokerto"]
jalan = ["Sudirman","Gatot Subroto","Ahmad Yani","Diponegoro","Veteran",
         "Soekarno Hatta","Kawi","Ijen","Semeru","Bondowoso"]
sosmed_instansi = [
    "instagram.com/telkomindonesia","instagram.com/bankbri","instagram.com/pertamina",
    "instagram.com/pln_id","twitter.com/BankMandiri","instagram.com/gojekindonesia",
    "instagram.com/tokopedia","instagram.com/bankbni","","","",""
]

def slug(nama):
    return ''.join(c for c in nama.lower() if c.isalnum())[:12]

def maybe(value, prob_empty):
    return "" if random.random() < prob_empty else value

def generate_kontak(nama):
    s = slug(nama)
    st = random.choice(status_list)
    kt = random.choice(kota)
    perus = random.choice(perusahaan) if st != "Wirausaha" else \
            "Usaha Mandiri " + random.choice(["Kuliner","Konveksi","Digital","Properti","Retail"])
    return {
        "email":           maybe(f"{s}{random.randint(10,99)}@gmail.com", 0.05),
        "hp":              maybe(f"08{random.randint(100000000,999999999)}", 0.05),
        "linkedin":        maybe(f"linkedin.com/in/{s}{random.randint(1,99)}", 0.10),
        "instagram":       maybe(f"instagram.com/{s}_", 0.10),
        "facebook":        maybe(f"facebook.com/{s}{random.randint(1,9)}", 0.10),
        "tiktok":          maybe(f"tiktok.com/@{s}{random.randint(1,9)}", 0.15),
        "tempat_kerja":    maybe(perus, 0.05),
        "alamat_kerja":    maybe(f"Jl. {random.choice(jalan)} No.{random.randint(1,100)}, {kt}", 0.10),
        "posisi":          maybe(random.choice(posisi), 0.05),
        "status":          maybe(st, 0.05),
        "sosmed_instansi": maybe(random.choice(sosmed_instansi), 0.20),
    }

def upload_batch(payload):
    url = f"{FIREBASE_URL}/alumni.json"
    resp = requests.patch(url, json=payload, timeout=30)
    return resp.status_code

def main():
    random.seed(42)
    print("Membaca file Excel...")
    wb = openpyxl.load_workbook(EXCEL_FILE, read_only=True)
    ws = wb.active

    rows = []
    for i, row in enumerate(ws.iter_rows(values_only=True)):
        if i == 0:
            continue
        rows.append(row)

    total = len(rows)
    print(f"Total data: {total:,}")
    print(f"Mulai upload ke Firebase dalam batch {BATCH_SIZE}...\n")

    batch    = {}
    uploaded = 0
    errors   = 0

    for i, row in enumerate(rows):
        nama        = str(row[0] or "")
        nim         = str(row[1] or "")
        tahun_masuk = str(row[2] or "")
        tgl_lulus   = str(row[3] or "")
        fakultas    = str(row[4] or "")
        prodi       = str(row[5] or "")

        kontak = generate_kontak(nama)

        key = f"alumni_{i+1}"
        batch[key] = {
            "index":       i + 1,
            "nama":        nama,
            "nim":         nim,
            "tahun_masuk": tahun_masuk,
            "tgl_lulus":   tgl_lulus,
            "fakultas":    fakultas,
            "prodi":       prodi,
            **kontak
        }

        if len(batch) >= BATCH_SIZE:
            status = upload_batch(batch)
            uploaded += len(batch)
            if status == 200:
                pct = uploaded / total * 100
                print(f"  ✓ {uploaded:,}/{total:,} ({pct:.1f}%)")
            else:
                errors += len(batch)
                print(f"  ✗ Error HTTP {status}")
            batch = {}
            time.sleep(0.2)

    if batch:
        status = upload_batch(batch)
        uploaded += len(batch)
        if status == 200:
            print(f"  ✓ {uploaded:,}/{total:,} (100%)")
        else:
            errors += len(batch)

    print(f"\nSelesai! {uploaded - errors:,} data berhasil, {errors:,} gagal.")
    print(f"Cek: {FIREBASE_URL}/alumni.json?limitToFirst=3&print=pretty")

if __name__ == "__main__":
    main()
