from flask import Flask, render_template, request
from pymongo import MongoClient
from gridfs import GridFS
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb+srv://gdas37467:46262587@cluster0.2a1dsjs.mongodb.net/test")
db = client.jec_chess
fs = GridFS(db)


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    fideid= request.form['fideid']
    rating= request.form['rating']
    institute= request.form['institute']
    category= request.form['category']
    dob= request.form['dob']
    gender = request.form['gender']



    payment = request.files['payment']
    idproof = request.files['idproof']
    data = {
        'name': name,
        'email': email,
        'phone': phone,
        'dob' : dob,
        'fideid' : fideid,
        'rating' : rating,
        'institute' : institute,
        'category' : category,
        'gender' : gender

    }
    # Insert user data into the 'users' collection
    result = db.users.insert_one(data)
    # Store the uploaded file in GridFS and associate it with the new user document
    payment_id = fs.put(payment.read(), filename=payment.filename, user_id=name)
    idproof_id = fs.put(idproof.read(),filename = idproof.filename,user_id=name)
    return 'User data and file stored with user ID: ' + str(result.inserted_id) + ' and paymentfile ID: ' + str(payment_id) +  'and file ID: ' + str(idproof_id)

if __name__ == '__main__':
    app.run(debug=True)