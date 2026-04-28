📊 Proyek Analisis Data E-Commerce
👤 Informasi
Nama: Fajar Istiqomah
Email: [	CDCC290D6X2058@student.devacademy.id]
ID Dicoding: [CDCC290D6X2058]
📌 Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data transaksi e-commerce guna memahami pola pembelian pelanggan, tren transaksi, serta hubungan antara nilai pembayaran dan kepuasan pelanggan.
Hasil analisis divisualisasikan dalam bentuk dashboard interaktif menggunakan Streamlit.

❓ Pertanyaan Bisnis
Bagaimana tren jumlah transaksi dan rata-rata nilai pembayaran per bulan selama tahun 2018?
Apakah terdapat hubungan antara nilai pembayaran dengan skor review pelanggan?

🛠️ Tools & Library
Python
Pandas
NumPy
Matplotlib
Seaborn
Streamlit

📂 Struktur Proyek
📁 proyek-ecommerce
│
├── dashboard/
│   └── dashboard.py
│
├── data/
│   └── dataset.csv
│
├── notebook.ipynb
├── requirements.txt
└── README.md

# 🔄 Alur Analisis
# 1. Data Wrangling
- Load dataset
- Assessing data (cek missing value, tipe data, duplikasi)
- Cleaning data (handling missing values, outliers, dll)

# 3. Exploratory Data Analysis (EDA)
Melakukan eksplorasi data untuk mendapatkan insight:
# Univariate Analysis
  - Distribusi nilai pembayaran
  - Distribusi skor review
# Bivariate Analysis
  - Hubungan payment vs review
  - Tren transaksi per bulan
# Multivariate Analysis
  - Analisis kategori produk vs jumlah transaksi
  - Payment vs kategori vs review
# Menggunakan:
  - Histogram
  - Boxplot
  - Scatter plot
  - Line chart

# 📊 Hasil Insight
  - Terjadi peningkatan transaksi pada bulan tertentu (contoh: akhir tahun)
  - Nilai pembayaran tidak selalu berbanding lurus dengan skor review
  - Beberapa kategori produk mendominasi transaksi
  - Terdapat outlier pada data pembayaran
  - 
# 📈 Dashboard
Dashboard dibuat menggunakan Streamlit dan menampilkan:
  - Tren transaksi bulanan
  - Rata-rata pembayaran
  - Hubungan payment vs review
  - Distribusi data
    
▶️ Cara Menjalankan Dashboard
# 1. Clone Repository
git clone https://github.com/username/proyek-ecommerce.git
cd proyek-ecommerce

# 2. Buat Virtual Environment (Opsional tapi disarankan)
python -m venv venv
# Aktifkan environment:
  - Windows:
      ( venv\Scripts\activate )
  - Mac/Linux:
      ( source venv/bin/activate )
    
# 3. Install Dependencies
pip install -r requirements.txt
# 4. Jalankan Dashboard
streamlit run dashboard/dashboard.py
# 5. Akses Dashboard
Buka browser dan akses:
http://localhost:8501
📌 Catatan Tambahan
Pastikan semua library sudah terinstall sesuai requirements.txt
Gunakan Python versi 3.8 atau lebih baru
Dataset harus tersedia di folder /data
🚀 Kesimpulan
Analisis data e-commerce menunjukkan bahwa:
  - Pola transaksi memiliki tren musiman
  - Tidak semua transaksi dengan nilai tinggi menghasilkan review tinggi
  - Insight ini dapat digunakan untuk strategi bisnis dan peningkatan layanan pelanggan
