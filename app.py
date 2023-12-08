from flask import Flask, abort, jsonify,render_template,request,redirect, url_for
from flask_pymongo import PyMongo
from dotenv import load_dotenv, dotenv_values
import os



app=Flask(__name__)

load_dotenv()

mongo_hash =({
  "URI": os.getenv("MONGO_URI"),
  
})


app.config['MONGO_URI']=mongo_hash["URI"]
mongo=PyMongo(app)

@app.route('/')
def frontend():
    todos_collection=mongo.db.todos
    todos=todos_collection.find()
    return render_template('index.html',todos=todos)

#for testing via postman
# @app.route("/todos/")
# def get_all_todos():
#     return jsonify(todos)


@app.route("/add",methods=['GET','POST'])
def add_todo():
    todos_collection=mongo.db.todos
    new_title=request.form.get('title')
    new_desc=request.form.get('description')
    new_id=request.form.get('id')
    
    try:
        todos_collection.insert_one({'id':new_id,'title':new_title,"description":new_desc})
        
        return redirect(url_for('frontend'))
    except Exception as e:
        print("Error adding todo{e}")
        abort(400,"Bad Request: Unable to add todo.")

        
@app.route('/delete/<id>/',methods=['POST'])
def delete_todo(id):
    todos_collection=mongo.db.todos
    todo_item=todos_collection.delete_many({'id':id})
    return redirect(url_for('frontend'))
            


# app.run(debug=True)