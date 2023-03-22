from app import app
from flask import render_template, request, redirect, session, flash, url_for
from models import Users
from helpers import FormUser
from flask_bcrypt import check_password_hash


@app.route('/login')
def login():
    next_page = request.args.get("next")
    form = FormUser()    
    return render_template("login.html", next=next_page, form=form)


@app.route('/auth', methods=['POST',])
def auth():
    
    form = FormUser(request.form)

    user = Users.query.filter_by(nickname=form.nickname.data).first()
    password = check_password_hash(user.password, form.password.data)

    if user and password:
        session['user_logged'] = user.nickname
        flash(user.nickname + ' logado com sucesso!')
        next_page = request.form["next"]

        if next_page == 'None' or next_page == '':
            return redirect(url_for("index"))
        else:
            return redirect(next_page)     
    else:
        flash('user not logged.')
        return redirect(url_for("login"))
    

@app.route("/logout")
def logout():
    session['user_logged'] = None
    flash("Logout efetuado com sucesso!")
    return redirect(url_for("index"))