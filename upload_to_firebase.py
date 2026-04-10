"""
Script Upload Data Alumni ke Firebase Realtime Database
=======================================================
Cara pakai:
1. Install dependency:
   pip install requests openpyxl

2. Letakkan file Alumni_2000-2025.xlsx di folder yang sama dengan script ini

3. Jalankan:
   python upload_to_firebase.py

Script ini akan upload data ke Firebase dalam batch 500 data sekali kirim.
"""

import json
import time
import random
import requests
import openpyxl

# ===================== KONFIGURASI =====================
FIREBASE_URL = "https://alumni-tracker-84ee8-default-rtdb.firebaseio.com"
EXCEL_FILE = r"C:\Downloads\sistem\Alumni 2000-2025.xlsx"
BATCH_SIZE   = 500   # upload 500 data sekaligus
# =======================================================

perusahaan = [
    "PT Telkom Indonesia","PT Bank BRI","PT Unilever Indonesia","Dinas Pendidikan Kota Malang",
    "PT Pertamina","PT PLN Persero","Universitas Brawijaya","RS Saiful Anwar","PT Astra International",
    "Badan Pusat Statistik","PT Bank Mandiri","PT Indofood","Pemkot Malang","PT Bukalapak",
    "PT Gojek Indonesia","Dinas Kesehatan Jawa Timur","PT Bank BNI","PT Garuda Indonesia",
    "PT XL Axiata","Kementerian Keuangan RI","PT Samsung Electronics","PT Tokopedia",
    "PT Bank CIMB Niaga","PT Mayora Indah","PT Sinar Mas","Politeknik Negeri Malang",
    "RSUD Dr. Soetomo","PT Krakatau Steel","PT Pupuk Indonesia","Kantor Pajak Malang",
    "PT Bank Danamon","PT Pegadaian","PT Pos Indonesia","Diskominfo Kota Malang",
    "PT Kimia Farma","PT Kalbe Farma","BPJS Kesehatan","PT Adira Finance",
    "PT Jasa Marga","PT Angkasa Pura","Pemkab Malang","Universitas Negeri Malang"
]
posisi = [
    "Staff Akuntansi","Manajer Keuangan","Analis Data","Guru","Dosen","Direktur",
    "HRD Manager","Marketing Executive","Software Engineer","Kepala Bagian","Auditor",
    "Konsultan","Supervisor","General Manager","Staff IT","Kepala Sekolah",
    "Perawat","Dokter","Pengusaha","Wirausahawan","Staff Administrasi","Branch Manager",
    "Finance Officer","Legal Officer","Public Relations","Tax Consultant","Project Manager",
    "Business Analyst","Customer Service","Procurement Staff"
]
status_list = ["PNS","PNS","Swasta","Swasta","Swasta","Wirausaha"]
kota = ["Malang","Surabaya","Jakarta","Bandung","Yogyakarta","Semarang","Bali","Medan","Makassar","Solo","Sidoarjo","Pasuruan","Kediri","Blitar","Mojokerto"]
jalan = ["Sudirman","Gatot Subroto","Ahmad Yani","Diponegoro","Veteran","Soekarno Hatta","Kawi","Ijen","Semeru","Bondowoso"]
sosmed_instansi = [
    "instagram.com/telkomindonesia","instagram.com/bankbri","instagram.com/unileverid",
    "instagram.com/pertamina","instagram.com/pln_id","twitter.com/BankMandiri",
    "instagram.com/bukalapak","instagram.com/gojekindonesia","instagram.com/tokopedia",
    "instagram.com/bankbni","instagram.com/garuda.indonesia","","","",""
]

def slug(nama):
    return ''.join(c for c in nama.lower() if c.isalnum())[:12]

def maybe(value, prob_empty):
    return "" if random.random() < prob_empty else value

def generate_kontak(nama, status):
    s = slug(nama)
    kt = random.choice(kota)
    perus = random.choice(perusahaan) if status != "Wirausaha" else \
            "Usaha Mandiri " + random.choice(["Kuliner","Konveksi","Digital","Properti","Retail","Fashion","Catering"])
    return {
        "email":           maybe(f"{s}{random.randint(10,99)}@gmail.com", 0.30),
        "hp":              maybe(f"08{random.randint(100000000,999999999)}", 0.35),
        "linkedin":        maybe(f"linkedin.com/in/{s}{random.randint(1,99)}", 0.55),
        "instagram":       maybe(f"instagram.com/{s}_", 0.40),
        "facebook":        maybe(f"facebook.com/{s}{random.randint(1,9)}", 0.50),
        "tiktok":          maybe(f"tiktok.com/@{s}{random.randint(1,9)}", 0.60),
        "tempat_kerja":    maybe(perus, 0.25),
        "alamat_kerja":    maybe(f"Jl. {random.choice(jalan)} No.{random.randint(1,100)}, {kt}", 0.40),
        "posisi":          maybe(random.choice(posisi), 0.30),
        "status":          maybe(status, 0.20),
        "sosmed_instansi": maybe(random.choice(sosmed_instansi), 0.65),
    }

def upload_batch(batch_data):
    """Upload satu batch ke Firebase menggunakan REST API"""
    payload = {}
    for item in batch_data:
        key = f"alumni_{item['nim']}_{item['index']}"
        payload[key] = item
    url = f"{FIREBASE_URL}/alumni.json"
    resp = requests.patch(url, json=payload, timeout=30)
    return resp.status_code

def main():
    random.seed(123)
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

    batch = []
    uploaded = 0
    errors = 0

    for i, row in enumerate(rows):
        nama, nim, tahun_masuk, tgl_lulus, fakultas, prodi = row
        nama = str(nama or "")
        nim  = str(nim  or "")
        st   = random.choice(status_list)
        kontak = generate_kontak(nama, st)

        record = {
            "index":       i + 1,
            "nama":        nama,
            "nim":         nim,
            "tahun_masuk": str(tahun_masuk or ""),
            "tgl_lulus":   str(tgl_lulus   or ""),
            "fakultas":    str(fakultas    or ""),
            "prodi":       str(prodi       or ""),
            **kontak
        }
        batch.append(record)

        if len(batch) >= BATCH_SIZE:
            status = upload_batch(batch)
            uploaded += len(batch)
            if status == 200:
                pct = uploaded / total * 100
                print(f"  ✓ {uploaded:,}/{total:,} data terupload ({pct:.1f}%)")
            else:
                errors += len(batch)
                print(f"  ✗ Error batch (HTTP {status}), {uploaded:,} sejauh ini")
            batch = []
            time.sleep(0.3)  # jangan terlalu cepat

    # sisa batch
    if batch:
        status = upload_batch(batch)
        uploaded += len(batch)
        if status == 200:
            print(f"  ✓ {uploaded:,}/{total:,} data terupload (100%)")
        else:
            errors += len(batch)

    print(f"\nSelesai! {uploaded - errors:,} data berhasil, {errors:,} gagal.")
    print(f"Cek di: {FIREBASE_URL}/alumni.json?limitToFirst=5&print=pretty")

if __name__ == "__main__":
    main()
