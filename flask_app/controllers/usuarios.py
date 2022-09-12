
from flask import  render_template, session, redirect,request
from flask_app import app
from flask_app.models.users import User

@app.route('/users')
def users():
    usuario = User.get_all()
    print("user: ", usuario)
    return render_template("index.html", list_users = usuario)

@app.route('/user/new')
def new():
    return render_template("adduser.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route("/users/detalle/<id>")
def users_detalle(id):

    return render_template("detalles.html", user=User.get_by_id(id))

@app.route('/user/updated/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("updated_user.html",user=User.get_one(data))

@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')


@app.route('/user/eliminar/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')
