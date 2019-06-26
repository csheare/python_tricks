
from flask import Flask,json,jsonify,request,render_template
app = Flask(__name__)


stores = [
    {
        'name' : 'My Store 1',
        'items' : [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')
# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name:}
@app.route('/storef', methods=['POST'])
def create_storef():
    request_data =request.form.to_dict()
    new_store = {
       'name' : request_data['name'],
       'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data =request.get_json()
    new_store = {
       'name' : request_data['name'],
       'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    #Iterate over stores
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        else:
            return jsonify({'message' : "Store Not Found!"})

# GET /store
@app.route('/store/', methods=['GET'])
def get_stores():
    return jsonify({'stores':stores})

# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    print(stores)
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : request_data['name'],
                'price' : request_data['price']
            }
            store['items'].append(new_item)
            message = 'Item Created!'
        else:
            message = 'Store Not Found'
    return jsonify({'message': message})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(name):
    #find store
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
        else:
            return jsonify({'message' : 'store not found'})

app.run(port=5000)
