from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/xu-ly-van-ban')
def xu_ly():
    try:
        with open('text.txt', 'rb') as file:
            data = {
                'file_van_ban': file    
            }
            response = requests.post('http://worker:5001/phan-tich', files=data)
        if response.status_code==200:
            ket_qua = response.json()

            if 'Loi' in ket_qua:
                return jsonify({
                    'Loi': ket_qua['Loi']
                })

            return jsonify({
                'So_dong': ket_qua['So_dong'],
                'Tong_so_tu': ket_qua['Tong_so_tu'],
                'Tu_dai_nhat': ket_qua['Tu_dai_nhat'],
                'Tu _ngan_nhat': ket_qua['Tu_ngan_nhat']
            })
        else:
            return jsonify({
                'Thong_bao': "Co loi xay ra !"
            })
    except Exception as e:
        return jsonify({
            'Error': str(e)
        })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)