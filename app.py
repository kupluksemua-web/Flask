from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data stok sementara (simulasi database)
inventory = [
    {"nama": "Deterjen Cair", "stok": 10},
    {"nama": "Parfum Laundry", "stok": 5},
    {"nama": "Plastik Packing", "stok": 20}
]

@app.route('/')
def index():
    return render_template('index.html', items=inventory)

@app.route('/tambah', methods=['POST'])
def tambah_barang():
    nama = request.form.get('nama')
    stok = request.form.get('stok')
    
    if nama and stok:
        inventory.append({"nama": nama, "stok": int(stok)})
    
    # Redirect kembali ke halaman utama setelah menambah
    return redirect(url_for('index'))

@app.route('/cetak')
def cetak():
    # Mengirim data ke halaman khusus cetak
    return render_template('struk_print.html', items=inventory)

if __name__ == '__main__':
    app.run(debug=True)