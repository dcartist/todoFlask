from flask import Flask, jsonify, request, render_template, redirect
app = Flask(__name__)


todoList = ["Clean Kitchen", "Eat Food", "Code"]

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', todo=todoList)
@app.route("/add/", methods=['POST'])
def postTodo():
    # print(request.form['name'])
    todoList.append(request.form['name'])
    return redirect("/")
    # return render_template('index.html', todo=todoList)
@app.route("/id/<id>", methods=['GET', 'POST'])
def editInfo(id=None):
    if request.method =='GET':
        number = int(id)
        return render_template("edit.html", item=todoList[number], id=id )
    number = int(id)
    return render_template("edit.html", item=todoList[number], id=id )


@app.route("/edit", methods=['GET', 'POST'])
def updateInfo():
    print(request.form)
    number = int(request.form['id'])
    print (todoList[number])
    todoList[number] = request.form['name']
    path = f"/id/{request.form['id']}"
    return redirect(path)

################* Run App
app.run(port=3000, debug=True)