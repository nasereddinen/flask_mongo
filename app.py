from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from pymongo import MongoClient
from bson.objectid import ObjectId

# ...

app = Flask(__name__)
app.debug=True

#connect to the database
MongoClient = MongoClient('localhost', 27017)
db = MongoClient.tododb
todos = db.todos




@app.route("/",methods=['GET', 'POST'])
def index():
    '''
    get all todos from the database
    add a new todo to the database
    from the form data and redirect to the index page
    if the request method is POST
    insert the new todo into the todos collection
    
    '''
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))
    all_todos = todos.find()

    
    return render_template("index.html",todos=all_todos)

@app.post('/<id>/delete/')
def delete(id):
    '''
    Delete a todo item
    using the id
    by calling the delete_one method on the todos collection
    and redirecting to the index page
    
    '''
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()



