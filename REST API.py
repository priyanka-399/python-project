from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    user_id = request.json.get('id')
    name = request.json.get('name')
    if user_id in users:
        return jsonify({"error": "User  already exists"}), 400
    users[user_id] = {'name': name}
    return jsonify(users[user_id]), 201

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# Get a specific user by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user is None:
        return jsonify({"error": "User  not found"}), 404
    return jsonify(user), 200

# Update a user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if user is None:
        return jsonify({"error": "User  not found"}), 404
    name = request.json.get('name')
    users[user_id]['name'] = name
    return jsonify(users[user_id]), 200

# Delete a user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User  not found"}), 404
    del users[user_id]
    return jsonify({"message": "User  deleted"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
