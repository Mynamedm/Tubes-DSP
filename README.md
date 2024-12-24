# Sistem Pengukuran Sinyal Respirasi dan rPPG

## 👥 Anggota Kelompok
| NAMA | NIM | ID Github |
|:----:|:---:|:---------:|
| Dias Morello Sembiring | 120140167 | Mynamedm |
| Moratua Putra Pardede | 121140079 | kazuhikoakiraa |
| Joanne Polama Putri Sembiring | 121140128 | joanneps |

## 📝 Deskripsi
Sistem ini menggunakan computer vision dan pemrosesan sinyal untuk mengukur dua parameter vital signs:

1. **Sinyal Respirasi**: Data yang diperoleh dari proses pernapasan seseorang. Sinyal ini mencerminkan pola, ritme, dan karakteristik pernapasan, yang digunakan untuk memantau fungsi respirasi atau mendeteksi gangguan pada sistem pernapasan.

2. **Sinyal rPPG** (remote PhotoPlethysmoGraphy): Metode non-invasif untuk mengukur detak jantung menggunakan perubahan warna kulit yang disebabkan oleh aliran darah, diambil melalui kamera biasa.

## 🔧 Persyaratan Sistem

### Perangkat Keras
- Webcam dengan resolusi minimal 720p
- Processor minimal dual-core
- RAM minimal 4GB
- Ruangan dengan pencahayaan yang cukup

### Perangkat Lunak
- Windows 10/11, macOS, atau Linux
- Python 3.6 atau lebih tinggi
- Pip (Python package installer)

## 🚀 Instalasi

1. Clone repositori ini:
```bash
git clone [URL_REPOSITORY]
cd [NAMA_FOLDER]
```

2. Buat dan aktifkan virtual environment (opsional tapi direkomendasikan):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install semua dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Cara Penggunaan

1. Pastikan Anda berada di direktori proyek
2. Jalankan program:
```bash
python app.py
```

3. Setelah program berjalan:
   - Posisikan wajah Anda di depan kamera
   - Pastikan wajah terdeteksi (ditandai dengan kotak hijau)
   - Jaga posisi wajah tetap stabil
   - Monitor akan menampilkan:
     - Heart Rate (BPM)
     - Respiratory Rate (breaths/min)
     - Grafik real-time dari kedua sinyal

4. Untuk keluar dari program, tekan 'q' pada keyboard

## 📊 Fitur
- Deteksi wajah otomatis
- Pengukuran heart rate real-time
- Pengukuran respiratory rate real-time
- Visualisasi grafik sinyal vital
- ROI (Region of Interest) tracking
- Filter sinyal adaptif

## 📅 Logbook
| MINGGU KE- | KEGIATAN |
|:----------:|:--------:|
| Minggu ke-1 (24-30 November 2024) | Mencari berbagai referensi |
| Minggu ke-2 (1-7 Desember 2024) | Diskusi terkait ide project yang akan dibuat |
| Minggu ke-3 (8-14 Desember 2024) | Mengerjakan code program |
| Minggu ke-4 (15-21 Desember 2024) | Mengerjakan code program + mencicil laporan |
| Minggu ke-5 (22-24 Desember 2024) | Melakukan cross check program dan laporan + submit final project |

## ⚠️ Troubleshooting
1. Jika webcam tidak terdeteksi:
   - Pastikan webcam terhubung dengan benar
   - Coba ganti index webcam di `main()` dari `1` ke `0`
   - Periksa izin akses kamera

2. Jika program crash:
   - Pastikan semua dependencies terinstall dengan benar
   - Periksa versi Python dan library
   - Pastikan pencahayaan ruangan cukup


