import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Fungsi untuk memproses sinyal respirasi dan rPPG
def process_signal(frame):
    # Contoh sederhana: Ekstraksi sinyal menggunakan rata-rata warna hijau dari frame
    green_channel = frame[:, :, 1]  # Kanal hijau
    avg_green = np.mean(green_channel)
    return avg_green

# Inisialisasi webcam
cap = cv2.VideoCapture(2)

if not cap.isOpened():
    print("Error: Tidak dapat mengakses webcam.")
    exit()

# List untuk menyimpan sinyal
respiration_signal = []
rppg_signal = []
time_points = []

plt.ion()
fig, ax = plt.subplots(2, 1, figsize=(10, 6))

frame_count = 0
fps = cap.get(cv2.CAP_PROP_FPS)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Tidak dapat membaca frame dari webcam.")
            break

        frame = cv2.resize(frame, (640, 480))
        cv2.imshow('Webcam Feed', frame)

        # Proses sinyal dari frame
        signal_value = process_signal(frame)
        respiration_signal.append(signal_value)
        rppg_signal.append(signal_value)  # Misal, gunakan sinyal yang sama untuk rPPG (contoh sederhana)
        time_points.append(frame_count / fps)

        # Update visualisasi
        ax[0].cla()
        ax[0].plot(time_points, respiration_signal, label='Respiration Signal', color='blue')
        ax[0].set_title('Respiration Signal')
        ax[0].set_xlabel('Time (s)')
        ax[0].set_ylabel('Amplitude')
        ax[0].legend()

        ax[1].cla()
        ax[1].plot(time_points, rppg_signal, label='rPPG Signal', color='green')
        ax[1].set_title('rPPG Signal')
        ax[1].set_xlabel('Time (s)')
        ax[1].set_ylabel('Amplitude')
        ax[1].legend()

        plt.pause(0.001)

        frame_count += 1

        # Tekan 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Program dihentikan oleh pengguna.")

finally:
    cap.release()
    cv2.destroyAllWindows()
    plt.ioff()
    plt.show()