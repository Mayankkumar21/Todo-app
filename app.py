from flask import Flask, abort, jsonify,render_template,request

todos = [
    {
        'id': 1,
        'title': 'wipe windows',
        'description': 'wipe windows properly'
    },
    {
        'id': 2,
        'title': 'write article',
        'description': 'write beautiful article'
    },
]

app=Flask(__name__)

@app.route('/')
def frontend():
    return render_template('index.html')

@app.route("/todos/")
def get_all_todos():
    return jsonify(todos)

@app.route("/todo/<int:id>/")
def get_todoById(id):
    try:
        required_todo=[item for item in todos if item["id"]==id]
        newtodo={"id":3,"title":"gym","desc":"go to gym"}
        todos.append(newtodo)
        return jsonify(required_todo[0])
        
    except IndexError:
        abort(404)

@app.route("/add",methods=['POST'])
def addTodo():
    data=request.json
    if 'title' in data and 'description' in data and 'id' in data:
        todos.append({
            'id':data['id'],
            'title':data['title'],
            'description':data['description'],
        })
        return jsonify({"message": "Todo added successfully"}), 201
    else:
        abort(400, "Bad Request: 'title', 'description', and 'id' are required fields")
        
@app.route('/delete/<int:id>/',methods=['POST'])
def delete_todo(id):
    global todos
    initial_len=len(todos)
    todos=[item for item in todos if item['id']!=id]
    
    if len(todos)<initial_len:
        return jsonify({"message":"Todo deleted Successfully"}),201
    abort(400, "No todo was found with the given id")
            


app.run()