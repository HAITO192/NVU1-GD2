from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/phan-tich', methods=['POST'])
def phan_tich_text():
    if 'file_van_ban' in request.files:
        tu_dai_nhat = ""
        tu_ngan_nhat = "a" * 100
        so_dong = 0
        tong_so_tu = 0
        for line in request.files['file_van_ban']:
            so_dong += 1
            for word in line.decode('utf-8').strip().split():
                tong_so_tu += 1
                if len(word) > len(tu_dai_nhat): tu_dai_nhat = word
                if len(word) < len(tu_ngan_nhat): tu_ngan_nhat = word
        return jsonify({
            'So_dong': so_dong,
            'Tong_so_tu': tong_so_tu,
            'Tu_dai_nhat': tu_dai_nhat,
            'Tu_ngan_nhat': tu_ngan_nhat
        })
    return jsonify({
        'Loi': 'Khong tim thay file'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)