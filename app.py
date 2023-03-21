from flask import Flask, render_template, request
from pymongo import MongoClient
from gridfs import GridFS

app = Flask(__name__)
client = MongoClient("mongodb+srv://gdas37467:46262587@cluster0.2a1dsjs.mongodb.net/test")
db = client.jec_chess
fs = GridFS(db)


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    lichessid= request.form['lichessid']
    rating= request.form['rating']
    institute= request.form['institute']
    category= request.form['category']
    dob= request.form['dob']



    payment = request.files['payment']
    data = {
        'name': name,
        'email': email,
        'phone': phone,
        'dob' : dob,
        'lichessid' : lichessid,
        'rating' : rating,
        'institute' : institute,
        'category' : category
    }
    # Insert user data into the 'users' collection
    result = db.users.insert_one(data)
    # Store the uploaded file in GridFS and associate it with the new user document
    file_id = fs.put(payment.read(), filename=payment.filename, user_id=name)
    return 'User data and file stored with user ID: ' + str(result.inserted_id) + ' and file ID: ' + str(file_id)

if __name__ == '__main__':
    app.run(debug=True)