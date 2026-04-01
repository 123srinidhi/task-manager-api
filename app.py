from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return "Task Manager API is running!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    return jsonify([dict(t) for t in tasks])

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    conn = get_db()
    conn.execute('INSERT INTO tasks (title, status) VALUES (?, ?)',
                 (data['title'], 'pending'))
    conn.commit()
    return jsonify({"message": "Task added"})

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.json
    conn = get_db()
    conn.execute('UPDATE tasks SET status=? WHERE id=?',
                 (data['status'], id))
    conn.commit()
    return jsonify({"message": "Task updated"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = get_db()
    conn.execute('DELETE FROM tasks WHERE id=?', (id,))
    conn.commit()
    return jsonify({"message": "Task deleted"})

# ✅ ALWAYS KEEP THIS AT LAST
if __name__ == '__main__':
    app.run(debug=True)