from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('hw_04.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    phone_num_receive = request.form['phone_num_give']
    print(name_receive)
    print(quantity_receive)
    print(address_receive)
    print(phone_num_receive)

    doc = {
        'name': name_receive,
        'quantity': quantity_receive,
        'address': address_receive,
        'phone_num': phone_num_receive
    }

    db.orders.insert_one(doc)
    return jsonify({'result': 'success', 'msg':'주문완료!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.orders.find({},{'_id':False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)