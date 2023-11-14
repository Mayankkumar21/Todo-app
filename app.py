from flask import Flask, abort, jsonify,render_template,request,redirect, url_for

todos = []

app=Flask(__name__)

@app.route('/')
def frontend():
    return render_template('index.html',todos=todos)

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

@app.route("/add",methods=['GET','POST'])
def add_todo():
    new_title=request.form.get('title')
    new_desc=request.form.get('description')
    new_id=request.form.get('id')
    # new_todo=[]
    
    try:
        todos.append({
            'id':new_id,
            'title':new_title,
            'description':new_desc,
            })
        print(new_desc,new_id,new_title)
        print(todos)
        return redirect(url_for('frontend'))
    except Exception as e:
        print("Error adding todo{e}")
        abort(400,"Bad Request: Unable to add todo.")

        
@app.route('/delete/<int:id>/',methods=['DELETE'])
def delete_todo(id):
    global todos
    initial_len=len(todos)
    todos=[item for item in todos if item['id']!=id]
    
    if len(todos)<initial_len:
        return jsonify({"message":"Todo deleted Successfully"}),201
    abort(400, "No todo was found with the given id")
            


app.run(debug=True)