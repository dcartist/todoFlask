from flask import Flask, request, render_template, redirect
app = Flask(__name__)


todoList = ["Code", "Eat Food", "breathe", "Code some more"]

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', todo=todoList)


################TODO ADD Function
@app.route("/add/", methods=['POST'])
def postTodo():
    # print(request.form['name'])
    todoList.append(request.form['name'])
    return redirect("/")
    # return render_template('index.html', todo=todoList)


################TODO Show individual item Function
@app.route("/id/<id>", methods=['GET', 'POST'])
def editInfo(id=None):
    if request.method =='GET':
        number = int(id)
        return render_template("edit.html", item=todoList[number], id=id )
    number = int(id)
    return render_template("edit.html", item=todoList[number], id=id )

################TODO EDIT Function
@app.route("/edit", methods=['GET', 'POST'])
def updateInfo():
    number = int(request.form['id'])
    todoList[number] = request.form['name']
    path = f"/id/{request.form['id']}"
    return redirect(path)


################TODO DELETE Function
@app.route("/delete/<id>", methods=["GET"])
def deleteItem(id=None):
    number = int(id)
    todoList.pop(number)
    return redirect("/")

################* Run App
app.run(port=3000, debug=True)