from flask import Flask, jsonify,request
from flask_sqlalchemy import SQLAlchemy
# import request
app = Flask(__name__)

# Replace with your database credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://saurabh5160:test12345@saurabh5160.mysql.pythonanywhere-services.com:3306/saurabh5160$test'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    item_query = db.Column(db.String(255))

# Route to insert data
@app.route('/insert_item', methods=['POST'])
def insert_item():
    request_data = request.get_json()    
    id = request_data['id']
    name = request_data['name']
    new_item = Item(id=id, name=name)
    db.session.add(new_item)    
    db.session.commit()
    return jsonify({'message': 'Item inserted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
