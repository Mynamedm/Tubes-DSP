import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Fungsi untuk memproses sinyal respirasi dan rPPG
def process_signal(frame):
    """
    Memproses sinyal dari frame input dengan mengambil rata-rata nilai pada kanal hijau.

    Parameter:
        frame (numpy.ndarray): Frame gambar yang diambil dari webcam.

    Return:
        float: Rata-rata nilai dari kanal hijau pada frame.
    """
    green_channel = frame[:, :, 1]  # Mengambil kanal hijau dari frame (channel 1 pada format BGR OpenCV).
    avg_green = np.mean(green_channel)  # Menghitung rata-rata nilai kanal hijau.
    return avg_green

# Inisialisasi webcam
cap = cv2.VideoCapture(2)  # Menggunakan webcam indeks 2 (sesuaikan dengan perangkat Anda).

if not cap.isOpened():
    print("Error: Tidak dapat mengakses webcam.")
    exit()

# List untuk menyimpan sinyal
respiration_signal = []  # Menyimpan data sinyal respirasi.
rppg_signal = []         # Menyimpan data sinyal rPPG.
time_points = []         # Menyimpan titik waktu.

# Menyiapkan visualisasi interaktif menggunakan matplotlib
plt.ion()
fig, ax = plt.subplots(2, 1, figsize=(10, 6))  # Membuat dua subplot untuk visualisasi sinyal.

frame_count = 0  # Menghitung jumlah frame yang telah diproses.
fps = cap.get(cv2.CAP_PROP_FPS)  # Mendapatkan frame rate dari webcam.

try:
    while True:
        # Membaca frame dari webcam
        ret, frame = cap.read()
        if not ret:
            print("Error: Tidak dapat membaca frame dari webcam.")
            break

        # Ubah ukuran frame untuk konsistensi
        frame = cv2.resize(frame, (640, 480))

        # Tampilkan umpan langsung dari webcam
        cv2.imshow('Webcam Feed', frame)

        # Proses sinyal dari frame
        signal_value = process_signal(frame)  # Ekstraksi sinyal dari frame.
        respiration_signal.append(signal_value)  # Tambahkan nilai sinyal ke daftar respirasi.
        rppg_signal.append(signal_value)  # Tambahkan nilai sinyal ke daftar rPPG (contoh sederhana).
        time_points.append(frame_count / fps)  # Hitung waktu berdasarkan frame count dan FPS.

        # Update visualisasi sinyal
        ax[0].cla()  # Bersihkan plot sebelumnya untuk subplot 1 (respiration).
        ax[0].plot(time_points, respiration_signal, label='Respiration Signal', color='blue')
        ax[0].set_title('Respiration Signal')
        ax[0].set_xlabel('Time (s)')
        ax[0].set_ylabel('Amplitude')
        ax[0].legend()

        ax[1].cla()  # Bersihkan plot sebelumnya untuk subplot 2 (rPPG).
        ax[1].plot(time_points, rppg_signal, label='rPPG Signal', color='green')
        ax[1].set_title('rPPG Signal')
        ax[1].set_xlabel('Time (s)')
        ax[1].set_ylabel('Amplitude')
        ax[1].legend()

        # Render visualisasi
        plt.pause(0.001)

        frame_count += 1  # Tambahkan jumlah frame yang telah diproses.

        # Tekan 'q' untuk keluar dari aplikasi
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Program dihentikan oleh pengguna.")

finally:
    # Pastikan resource dilepas dengan benar
    cap.release()  # Lepaskan webcam.
    cv2.destroyAllWindows()  # Tutup semua jendela OpenCV.
    plt.ioff()  # Matikan mode interaktif matplotlib.
    plt.show()  # Tampilkan grafik terakhir sebelum program selesai.
