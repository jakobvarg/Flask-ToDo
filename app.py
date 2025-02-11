from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

todos = [
    {'id': 1, 'task': 'Buy groceries', 'checked': False},
    {'id': 4, 'task': 'Read a book', 'checked': True},
    {'id': 5, 'task': 'Exercise for 30 minutes', 'checked': False},
    {'id': 6, 'task': 'Fix a bug in the project', 'checked': True},
]

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
  if(request.method == "POST"):
    new_id = max([todo['id'] for todo in todos], default=0) + 1
    new_task = request.form['todo-name']
    todos.append({'id': new_id, 'task': new_task, 'checked': False})
  return render_template('index.html', items=todos)

@app.route("/checked/<int:todo_id>", methods=["POST"])
def checked_todo(todo_id):
  for todo in todos:
    if todo['id'] == todo_id:
      todo['checked'] = not todo['checked']
      break
  return redirect(url_for('home'))

@app.route("/home/delete/<int:todo_id>", methods=["POST"])
def delete_todo(todo_id):
  global todos
  for todo in todos:
    if todo['id'] == todo_id:
      todos.remove(todo)
  return redirect(url_for('home'))

@app.route("/api/<int:todo_id>")
def show_task(todo_id):
  global todos
  for todo in todos:
    if todo['id'] == todo_id:
      return jsonify(todo)
      break
  return ""
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
