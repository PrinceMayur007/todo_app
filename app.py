from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False) # wont be blank
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    # we have to import datetime
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/", methods = ['GET', 'POST'])
def hello_world():
    #getting from html form, import request from flask
    # now when you use post or get method you have to mention them in route , methods = ['GET', 'POST']
    # reload the page and click button to check, you will see post method in terminal after you click.
    if request.method == 'POST':
        # print(request.form['title'])   # when you add from form it will print title in terminal, for testing
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title = title, desc = desc)
        #adding a value, making object of todo class
        db.session.add(todo)
        db.session.commit()
    
    #todo = Todo(title = 'First Todo', desc = 'Start investing in Stock Market')
    #adding a value, making object of todo class
    #db.session.add(todo)
    #db.session.commit()  we added same line above but we do it there for form inputs.
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo = allTodo)
    #put here query.all printed it and return allTodo as allTodo, now how to print this in html?
    # this will be done by Jinja2 (the extension we downloaded Jinja2 snippet kit)
    # Jinja2 is templating engine which will used as mediator between flask and html. If you send the python variable in html so this is used.
    # Now we will display all todos in index.html
    # return "<p>Hello, World!</p>"

#@app.route("/show")
#def show():
 #   allTodo = Todo.query.all()
  #  print(allTodo)
  #  return "<p>this is my product page</p>"
# when you do /show in url it will show all the entries in terminal, it will print in __repr__(dunder repr) function return format
# if we not given __repr__ it will have given objects at address.
#ref IntroReadme

@app.route("/update/<int:sno>", methods = ['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

@app.route("/delete/<int:sno>")   #delete/todo.sno ayega na form se
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()  #i need query which represent this sno.
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)      # debug = True when you are in developement only.
