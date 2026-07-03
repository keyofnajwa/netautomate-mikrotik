import os
import re
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

def clean_and_parse_interfaces(raw_text):
    """
    Fungsi parse super aman untuk memecah text mentah '/interface print' 
    menjadi dictionary per kolom (ID, Flags, Name, Type, MTU, MAC).
    """
    parsed_list = []
    lines = raw_text.strip().splitlines()

    for line in lines:
        line = line.strip()
        # Lewati baris judul kolom bawaan mikrotik
        if not line or "FLAGS" in line or line.startswith("#") or line.startswith("columns:"):
            continue

        try:
            # Pola regex dinamis untuk membaca spasi renggang kolom MikroTik
            # Kolom: ID, Flags (opsional), Name, Type, Actual-MTU, MAC-Address
            tokens = re.split(r'\s{2,}', line)
            
            # Pengkondisian jika kolom pertama berisi ID dan Flag menyatu (Contoh: "0  R")
            first_token_split = tokens[0].split()
            
            if len(first_token_split) >= 2:
                item_id = first_token_split[0]
                flags = first_token_split[1]
                remaining_tokens = tokens[1:]
            else:
                item_id = tokens[0]
                flags = ""
                remaining_tokens = tokens[1:]

            # Normalisasi panjang token agar tidak crash jika salah satu field kosong
            if len(remaining_tokens) >= 4:
                name = remaining_tokens[0]
                iface_type = remaining_tokens[1]
                mtu = remaining_tokens[2]
                mac = remaining_tokens[3]
            elif len(remaining_tokens) == 3:
                name = remaining_tokens[0]
                iface_type = remaining_tokens[1]
                mtu = remaining_tokens[2]
                mac = "-"
            else:
                continue

            parsed_list.append({
                "id": item_id,
                "flags": flags,
                "name": name,
                "type": iface_type,
                "mtu": mtu,
                "mac": mac
            })
        except Exception:
            # Jika ada satu baris aneh, lewati baris tersebut agar server tidak crash 500
            continue

    return parsed_list

@app.route('/')
def index():
    return render_template('index.html', error=None, interfaces=None)

@app.route('/execute', methods=['POST'])
def execute():
    from netmiko import ConnectHandler

    ip = request.form.get('ip')
    port = request.form.get('port')
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    form_data = {'ip': ip, 'port': port, 'username': username}

    # Validasi input password
    if password != confirm_password:
        return render_template('index.html', error="Konfirmasi password tidak sesuai!", form_data=form_data)

    device_params = {
        'device_type': 'mikrotik_routeros',
        'host': ip,
        'port': int(port) if port else 22,
        'username': username,
        'password': password,
        'conn_timeout': 10,
    }

    try:
        # Hubungkan SSH ke MikroTik
        ssh = ConnectHandler(**device_params)
        # Menggunakan without-paging agar output teks tidak terpotong text '-- more --'
        raw_output = ssh.send_command("/interface print without-paging")
        ssh.disconnect()

        # Proses data mentah menjadi bentuk list berkolom
        interfaces_data = clean_and_parse_interfaces(raw_output)

        if not interfaces_data:
            return render_template('index.html', error="Berhasil terhubung, tetapi gagal mengekstrak baris interface.", form_data=form_data)

        # Kirim data sukses ke frontend
        return render_template('index.html', interfaces=interfaces_data, form_data=form_data)

    except Exception as e:
        # Penahan crash: Kembalikan pesan galat ke form asal jika RTO / salah password
        return render_template('index.html', error=f"Koneksi Router Gagal: {str(e)}", form_data=form_data)

if __name__ == '__main__':
    # Kita ubah port-nya dari 5000 ke 8080
    app.run(host='0.0.0.0', port=8080, debug=True)