# NetAutomate Green 🌿

NetAutomate Green adalah platform berbasis web (Web GUI) interaktif yang dirancang untuk mempermudah pemantauan dan otomasi perangkat jaringan **MikroTik RouterOS**. Menggunakan framework **Flask (Python)** di backend dan **Tailwind CSS** di frontend, project ini memberikan alternatif pengelolaan router yang lebih visual, modern, dan efisien dibandingkan harus mengetik perintah manual di CLI secara terus-menerus.

---

## 📌 Latar Belakang

Dalam pengelolaan jaringan, khususnya saat melakukan simulasi atau konfigurasi skala lab di **GNS3 / VMware**, administrator jaringan sering kali harus membuka terminal SSH satu per satu untuk mengecek status perangkat. Proses ini memakan waktu dan kurang efisien secara visual. 

**NetAutomate Green** hadir sebagai solusi *eco-automation* yang menjembatani jalur remote SSH aman (via Netmiko) ke dalam sebuah dashboard web yang bersih. Hanya dengan sekali klik, data internal router langsung ditarik, diproses, dan disajikan dalam bentuk tabel grid yang rapi layaknya tampilan WinBox, tanpa perlu login ke aplikasi eksternal.

---

## 🚀 Fitur Utama & Kegunaan

<img width="1920" height="977" alt="Screenshot 2026-07-03 144209" src="https://github.com/user-attachments/assets/4d70c42a-b37d-4c80-bc74-0849261e642d" />
<br><br>
<img width="1907" height="977" alt="Screenshot 2026-07-03 144258" src="https://github.com/user-attachments/assets/8b20e514-29d0-4f15-93f3-5c27c298ada8" />


* **Real-time Interface Monitoring:** Membaca dan menampilkan seluruh daftar interface aktif, tipe interface, nilai MTU, hingga MAC Address langsung ke halaman web.
* **WinBox-Style Grid:** Mengubah output teks mentah (*raw text*) dari CLI MikroTik menjadi tabel data yang rapi dan mudah dianalisis.
* **Double Password Verification:** Proteksi keamanan tambahan sebelum mengeksekusi perintah *remote SSH* ke router.
* **GNS3 & Environment Ready:** Dilengkapi dengan penanganan delay parameter yang dioptimalkan untuk mesin virtual jaringan.

---

## 🛠️ Teknologi yang Digunakan

* **Backend:** Python 3.x, Flask Framework
* **Network Automation:** Netmiko (SSH Library)
* **Frontend:** HTML5, Tailwind CSS (Green Tech Theme)

---

## 💻 Cara Penggunaan (How to Run)

Ikuti langkah-langkah berikut untuk menjalankan NetAutomate Green di lingkungan lokal Anda:

### 1. Kloning Repository
```bash
git clone [https://github.com/KeyOfNajwa/netautomate-mikrotik.git](https://github.com/KeyOfNajwa/netautomate-mikrotik.git)
cd netautomate-mikrotik
```
### 2. Install Dependensi (Library)
Pastikan Python sudah terinstall di komputer Anda, lalu install Flask dan Netmiko melalui Terminal/CMD:

```Bash
pip install Flask netmiko
3. Jalankan Aplikasi
Jalankan server Flask dengan mengetik perintah berikut:

Bash
python app.py
Jika berhasil, server akan aktif di jalur lokal.
```
4. Akses Dashboard Web
Buka browser kesayangan Anda, lalu masuk ke alamat URL berikut:

Plaintext
```
[http://127.0.0.1:8080](http://127.0.0.1:8080)
```
5. Hubungkan ke Router GNS3
Pastikan router MikroTik CHR di GNS3 Anda sudah bisa di-ping dari komputer asli.

Masukkan IP Address, Port SSH (Default: 22), serta Username & Password router Anda pada panel Akses Router.

Klik tombol 🔍 Cek Interface List, dan data tabel interface Anda akan langsung muncul di sisi kanan layar!
