from flask import Flask
from flask import render_template
from flask import request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

lists = []
ToDo_lists = []

@app.route('/', methods=['GET', 'POST'])
def ToDo_feature():
    add_ToDo = request.form.get('add_ToDo')
    lists.append(add_ToDo)

    with open('ToDo.txt', 'a') as f:
        for list in lists:
            if list != None:
                f.write("%s\n" % list)
    with open('ToDo.txt', 'r') as f:
        ToDo_lists = f.read().split("\n")

    check_ToDo = request.form.getlist('check_ToDo')

    if check_ToDo != None:
        for i in check_ToDo:
            lists.remove(i)

    with open('ToDo.txt', 'w') as f:
        for list in lists:
            if list != None:
                f.write("%s\n" % list)
    with open('ToDo.txt', 'r') as f:
        ToDo_lists = f.read().split("\n")

    return render_template("ToDo.html", ToDo_lists=ToDo_lists)