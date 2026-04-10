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

import json, time, requests, openpyxl, os, glob

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

def upload_batch(payload):
    url = f"{FIREBASE_URL}/alumni.json"
    resp = requests.patch(url, json=payload, timeout=30)
    return resp.status_code

def main():
    print("Membaca file Excel...")
    wb = openpyxl.load_workbook(EXCEL_FILE, read_only=True)
    ws = wb.active

    rows = []
    for i, row in enumerate(ws.iter_rows(values_only=True)):
        if i == 0:
            continue  # skip header
        rows.append(row)

    total = len(rows)
    print(f"Total data: {total:,}")
    print(f"Mulai upload ke Firebase dalam batch {BATCH_SIZE}...\n")

    batch   = {}
    uploaded = 0
    errors   = 0

    for i, row in enumerate(rows):
        nama       = str(row[0] or "")
        nim        = str(row[1] or "")
        tahun_masuk = str(row[2] or "")
        tgl_lulus  = str(row[3] or "")
        fakultas   = str(row[4] or "")
        prodi      = str(row[5] or "")

        key = f"alumni_{i+1}"
        batch[key] = {
            "index":        i + 1,
            "nama":         nama,
            "nim":          nim,
            "tahun_masuk":  tahun_masuk,
            "tgl_lulus":    tgl_lulus,
            "fakultas":     fakultas,
            "prodi":        prodi,
            # kolom kontak dikosongkan - diisi manual nanti
            "email":        "",
            "hp":           "",
            "linkedin":     "",
            "instagram":    "",
            "facebook":     "",
            "tiktok":       "",
            "tempat_kerja": "",
            "alamat_kerja": "",
            "posisi":       "",
            "status":       "",
            "sosmed_instansi": ""
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

    # sisa batch
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