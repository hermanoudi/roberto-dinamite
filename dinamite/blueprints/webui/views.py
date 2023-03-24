from os import path
from flask import abort, request, redirect, render_template, session, flash, url_for, send_from_directory
from flask_bcrypt import check_password_hash
from dinamite.config import UPLOAD_PATH
from dinamite.models import Services, Users
from dinamite.helpers import FormUser, FormService, reload_file, remove_file
from dinamite.ext.database import db
import time

upload_path = UPLOAD_PATH

def index():
    serviceList = Services.query.order_by(Services.id)
    return render_template("list-service.html", title="Serviços", price="Preço", unit="Unidade", services=serviceList )


# USUARIO
def login():
    next_page = request.args.get("next")
    form = FormUser()    
    return render_template("login.html", next=next_page, form=form)


def auth():

    form = FormUser(request.form)

    user = Users.query.filter_by(nickname=form.nickname.data).first()
    password = check_password_hash(user.password, form.password.data)
    
    if user and password:
    
        session['user_logged'] = user.nickname
        flash(user.nickname + ' logado com sucesso!')
        next_page = request.form["next"]

        if next_page == 'None' or next_page == '':
            print("vai retornar para INDEX")
            return redirect(url_for("webui.index"))
        else:
            print("vai retornar para NEXT")
            return redirect(next_page)     
    else:
        flash('user not logged.')
        return redirect(url_for("webui.login"))
    


def logout():
    session['user_logged'] = None
    flash("Logout efetuado com sucesso!")
    return redirect(url_for("webui.index"))


def new_service():
    if 'user_logged' not in session or session ['user_logged'] == None:
        return redirect(url_for("webui.login", next=url_for("webui.new_service")))
    form = FormService ()

    return render_template("new-service.html", title="Novo Serviço", form=form)


def edit_service(id):
    if 'user_logged' not in session or session ['user_logged'] == None:
        return redirect(url_for("login", next=url_for("edit_service", id=id)))
 
    service = Services.query.filter_by(id=id).first()
    form = FormService()
    form.name.data = service.name
    form.price.data = service.price
    form.unit.data = service.unit

    img_service = reload_file(id)

    return render_template("edit-service.html", title="Editando Serviço", id=id, img_service=img_service, form=form)


def update_service():
    
    form = FormService(request.form)

    if form.validate_on_submit():

        service = Services.query.filter_by(id=request.form['id']).first()
        service.name = form.name.data
        service.price = form.price.data
        service.unit = form.unit.data
        
        db.session.add(service)
        db.session.commit()

        image = request.files['image']
        

        timestamp = time.time()

        remove_file(service.id)
        image.save(f'{upload_path}/services{service.id}-{timestamp}.png')

    return redirect( url_for("webui.index") )



def delete_service(id):
    if 'user_logged' not in session or session ['user_logged'] == None:
        return redirect(url_for("login"))
    
    service = Services.query.filter_by(id=id).delete()
    db.session.commit()
    flash("Serviço removido com sucesso")

    return redirect(url_for("webui.index"))




def create_service():
    form = FormService(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('new_service'))

    name = form.name.data
    price = form.price.data
    unit = form.unit.data

    service = Services.query.filter_by(name=name).first()
    if service:
        flash("Serviço já existe!")
        return redirect(url_for("webui.index"))

    new_service = Services(name=name, price=price, unit=unit)
    db.session.add(new_service)
    db.session.commit()

    image = request.files['image']
    
    image.save(f'{upload_path}/services{new_service.id}-{image.filename}')

    return redirect(url_for("webui.index"))


def image(file_name):
    return send_from_directory('uploads', file_name)


def init_app(app):
    upload_path = app.configuration.UPLOAD_PATH
