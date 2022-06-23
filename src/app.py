from flask import Flask, redirect, render_template, request, url_for, flash
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect
from config import config
from models.modelusers import ModelUser
from models.entities.user import User, Item
from datetime import datetime, date
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '.\\src\\static\\img\\profile'
csrf = CSRFProtect()
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(id)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['log'] == "Sign In":
            useri = User(0, request.form['user'], request.form['pwd'], None, None)
            logged_user = ModelUser.login(useri)
            print(logged_user)
            if logged_user != None:
                if logged_user.password:
                    login_user(logged_user)
                    return redirect(url_for('home'))
                else:
                    flash('contraseña incorrecta...')
                    return render_template('auth/login.html')
            else:
                flash('este usuario no existe...')
                return render_template('auth/login.html')
        else:
            usera = User(0,request.form['user'], request.form['pwd'], request.form['mail'], None)
            register_user = ModelUser.login(usera)
            if register_user == None:
                profile = request.files['rofilep']
                print(profile)
                fileame = request.form['user']
                extra = secure_filename(profile.filename).split('.')
                ext = extra[-1]
                filename = f'{fileame}.{ext}'
                profile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                user = User(0, request.form['user'], request.form['pwd'], request.form['mail'],foto=filename)
                ModelUser.register(user)
                flash('te has registrado con exito, ya puedes iniciar sesion')
                return render_template('auth/login.html')
            else:
                flash('este usuario ya existe...')
                return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect('login')


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    a = date.today()
    d = datetime.strptime(str(a), "%Y-%m-%d")
    info = ModelUser.get_list_7(ModelUser.get_list(current_user))
    if request.method == 'POST':
        lista = Item(request.form['name'], request.form['type'], request.form['cap'], request.form['status'], request.form['link'])
        ModelUser.add_one(lista, current_user)
        return render_template('home.html', date=d.strftime("%d/%m/%Y"), info=info)
    else:
        return render_template('home.html', date=d.strftime("%d/%m/%Y"), info=info)


@app.route('/all')
@login_required
def all():
    a = date.today()
    d = datetime.strptime(str(a), "%Y-%m-%d")
    info = ModelUser.get_list(current_user)
    return render_template('cat/all.html', date=d.strftime("%d/%m/%Y"), info=info)

@app.route('/anime')
@login_required
def anime():
    a = date.today()
    d = datetime.strptime(str(a), "%Y-%m-%d")
    info = ModelUser.by_type('Anime',current_user)
    return render_template('cat/anime.html', date=d.strftime("%d/%m/%Y"), info=info)

@app.route('/anime_chino')
@login_required
def anime_chino():
    a = date.today()
    d = datetime.strptime(str(a), "%Y-%m-%d")
    info = ModelUser.by_type('Anime(chino)',current_user)
    return render_template('cat/animec.html', date=d.strftime("%d/%m/%Y"), info=info)

@app.route('/manhwa')
@login_required
def manhwa():
    a = date.today()
    d = datetime.strptime(str(a), "%Y-%m-%d")
    info = ModelUser.by_type('Manhwa',current_user)
    return render_template('cat/manhwa.html', date=d.strftime("%d/%m/%Y"), info=info)

@app.route('/manhua')
@login_required
def manhua():
    a = date.today()
    d = datetime.strptime(str(a), "%Y-%m-%d")
    info = ModelUser.by_type('Manhua',current_user)
    return render_template('cat/manhua.html', date=d.strftime("%d/%m/%Y"), info=info)

@app.route('/members')
def owner():
    return render_template('own.html')

@app.route('/ccgen')
@login_required
def ccgen():
    return render_template('namso.html')

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
