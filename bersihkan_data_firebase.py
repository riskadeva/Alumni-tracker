"""
Script Bersihkan Data Ngasal Alumni dari Firebase
==================================================
Script ini akan MENGOSONGKAN field-field yang berisi data random/ngasal:
  - Email, No HP
  - LinkedIn, Instagram, Facebook, TikTok
  - Tempat Bekerja, Alamat Bekerja
  - Posisi / Jabatan
  - Status (PNS/Swasta/Wirausaha)
  - Sosmed Instansi

Yang DIPERTAHANKAN:
  - Nama, NIM, Tahun Masuk, Tanggal Lulus, Fakultas, Program Studi

Cara pakai:
  pip install requests
  python bersihkan_data_firebase.py
"""

import requests, time, json

FIREBASE_URL = "https://alumni-tracker-84ee8-default-rtdb.firebaseio.com"
BATCH_SIZE   = 200

FIELDS_TO_CLEAR = [
    "email", "hp", "linkedin", "instagram", "facebook", "tiktok",
    "tempat_kerja", "alamat_kerja", "posisi", "status", "sosmed_instansi",
]

def get_all_keys():
    url = f"{FIREBASE_URL}/alumni.json?shallow=true"
    print("Mengambil daftar key alumni dari Firebase...")
    r = requests.get(url, timeout=30)
    if r.status_code != 200:
        print(f"ERROR: HTTP {r.status_code} — {r.text[:200]}")
        exit(1)
    data = r.json()
    if not data:
        print("Tidak ada data.")
        exit(0)
    keys = list(data.keys())
    print(f"Total alumni: {len(keys):,}")
    return keys

def clear_batch(keys_batch):
    payload = {}
    for key in keys_batch:
        for field in FIELDS_TO_CLEAR:
            payload[f"{key}/{field}"] = ""
    r = requests.patch(f"{FIREBASE_URL}/alumni.json", json=payload, timeout=60)
    return r.status_code

def main():
    print("=" * 55)
    print("  BERSIHKAN DATA NGASAL ALUMNI — FIREBASE")
    print("=" * 55)
    print()
    print("Field yang akan DIKOSONGKAN:")
    for f in FIELDS_TO_CLEAR:
        print(f"  x  {f}")
    print()
    print("Field yang DIPERTAHANKAN:")
    for f in ["nama", "nim", "tahun_masuk", "tgl_lulus", "fakultas", "prodi"]:
        print(f"  v  {f}")
    print()

    ok = input("Lanjutkan? Ketik YA untuk memulai: ").strip()
    if ok.upper() != "YA":
        print("Dibatalkan.")
        return

    keys  = get_all_keys()
    total = len(keys)
    print(f"\nMulai membersihkan {total:,} data (batch {BATCH_SIZE})...\n")

    berhasil = 0
    gagal    = 0

    for i in range(0, total, BATCH_SIZE):
        batch  = keys[i : i + BATCH_SIZE]
        status = clear_batch(batch)
        if status == 200:
            berhasil += len(batch)
            pct    = berhasil / total * 100
            filled = int(30 * berhasil / total)
            bar    = "#" * filled + "-" * (30 - filled)
            print(f"  [{bar}] {berhasil:,}/{total:,} ({pct:.1f}%)", end="\r")
        else:
            gagal += len(batch)
            print(f"\n  ERROR HTTP {status} pada batch {i // BATCH_SIZE + 1}")
        time.sleep(0.15)

    print()
    print()
    print("=" * 55)
    print(f"  Selesai!")
    print(f"  Berhasil : {berhasil:,} alumni dibersihkan")
    if gagal:
        print(f"  Gagal    : {gagal:,} alumni")
    print("=" * 55)
    print()
    print("Data ngasal sudah dihapus semua.")
    print("Alumni bisa login dan isi data mereka sendiri.")

if __name__ == "__main__":
    main()
