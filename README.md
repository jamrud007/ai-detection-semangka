#  AI Watermelon Detector

Aplikasi Object Detection berbasis Web untuk mendeteksi buah semangka. Menggunakan **YOLOv8** (Custom Trained) dan **Flask**, dikemas dalam **Docker**.

##  Fitur
- **Custom AI Model:** Dilatih menggunakan dataset spesifik semangka (bukan model standar).
- **Web Interface:** UI sederhana untuk upload dan preview gambar.
- **REST API:** Endpoint `/detect` untuk integrasi dengan sistem lain.
- **Dockerized:** Siap dijalankan di environment apapun tanpa instalasi library manual.

## 🛠 Teknologi
- Python 3.9
- Ultralytics YOLOv8
- Flask
- OpenCV
- Docker

## 📦 Cara Menjalankan (Docker)

Pastikan Docker sudah terinstall, lalu jalankan perintah berikut di terminal:

# 1. Build Image
docker build -t semangka-app .

# 2. Jalankan Container
docker run -p 9000:9000 semangka-app