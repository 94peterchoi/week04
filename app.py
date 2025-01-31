from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    quan_receive = request.form['quan_give']
    addr_receive = request.form['addr_give']
    phone_receive = request.form['phone_give']

    orderinfo = {
        'username': name_receive,
        'quantity': quan_receive,
        'address': addr_receive,
        'phonenumber': phone_receive
    }

    db.orderinfo.insert_one(orderinfo)
    return jsonify({'result': 'success', 'msg': '성공했을까요?'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orderinfos = list(db.orderinfo.find({}, {'_id' : False}))
    return jsonify({'result': 'success', 'orders': orderinfos})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
