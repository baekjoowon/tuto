from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.iwdcyza.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('main.html')

@app.route("/mini", methods=["POST"])
def mini_post():
    text_receive = request.form['text_give']

    doc = {
        'text': text_receive,

    }
    db.mini.insert_one(doc)

    return jsonify({'msg': '일촌평등록!'})


@app.route("/mini", methods=["GET"])
def mini_get():
    mini_list = list(db.mini.find({}, {'_id': False}))
    return jsonify({'texts': mini_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

