# Gunakan Python 3.9 Full
FROM python:3.9

# Set folder kerja
WORKDIR /app

# Copy requirements dan install semua   dependensi
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ------------------------------
RUN pip uninstall -y opencv-python opencv-python-headless || true

# 2. Install opencv-python-headless versi tertentu
RUN pip install --no-cache-dir opencv-python-headless
# ------------------------------

# Copy semua file ke dalam container
COPY . .

# Buka Port
EXPOSE 9000

# Jalankan
CMD ["python", "app.py"]