import os
from flask import Flask, render_template, request, send_file
from ultralytics import YOLO
import cv2
import numpy as np
import io

app = Flask(__name__)

# =================================================
# BAGIAN PENTING: LOAD MODEL
#  'best.pt' (otak hasil training dengan dataset semangka)
# =================================================
print("Sedang memuat model AI Semangka...")
model = YOLO('best.pt') 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return "No image uploaded", 400

    file_gambar = request.files['image']
    
    # Baca file gambar ke format Array (OpenCV)
    in_memory_file = file_gambar.read()
    nparr = np.frombuffer(in_memory_file, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Lakukan Deteksi (Inference)
    # conf=0.25 artinya yakin minimal 25% baru digambar
    results = model(img, conf=0.25)

    # Gambar Kotak Hasil
    res_plotted = results[0].plot()

    # Encode kembali ke JPG
    retval, buffer = cv2.imencode('.jpg', res_plotted)
    
    return send_file(
        io.BytesIO(buffer),
        mimetype='image/jpeg'
    )

if __name__ == '__main__':
    # Jalankan Aplikasi di port 9000 atau sesuai environment variable PORT
    port = int(os.environ.get("PORT", 9000))
    app.run(host='0.0.0.0', port=port)