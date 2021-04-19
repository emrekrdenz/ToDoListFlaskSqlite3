from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_sqlalchemy import SQLAlchemy     ##sqlite3 için


# Kullanıcı Kayıt Formu
class RegisterForm(Form):
    name=StringField("İsim Soyisim:",validators=[validators.Length(min=4,max=25)])
    username=StringField("Kullanıcı Adı:",validators=[validators.Length(min=5,max=25,message="En az 5 karakter girmeniz gerekiyor")])
    email=StringField("Email Adresi:",validators=[validators.Email(message="Lütfen geçerli bir email adresi girin..")])
    password=PasswordField("Parola:",validators=[
        validators.DataRequired(message="Lütfen bir parola giriniz"),
        validators.EqualTo(fieldname="confirm",message="Parolanız Uyuşmuyor....")
    ])
    confirm=PasswordField("Parola Doğrula")
#########################################################


# Login Formu 
class LoginForm(Form):
    username=StringField("Kullanıcı Adı")
    password=PasswordField("Parola")

#VERİTABANLARI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Emre/Desktop/todo/todo.db'   ##Kendi pcnizde todo.db nin yolunu değiştirin
db = SQLAlchemy(app)

app.secret_key="emreblog"
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="123456789"
app.config["MYSQL_DB"]="emreblog"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)
#########################################################

#Decarotarı İZİNSİZ GİRİŞTE LOGİN SAYFASINA ATIYOR
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Bu sayfayı görüntülemek için giriş yapın","danger")
            return redirect(url_for("login"))

    return decorated_function


@app.route("/dashboard")  
@login_required
def dashboard():
    return render_template("dashboard.html")


#Kayıt Olma
@app.route("/register",methods=["GET","POST"])
def register():
    form=RegisterForm(request.form)

    if request.method=="POST" and form.validate():     ## bir hata yoksa
        name=form.name.data
        username=form.username.data
        email=form.email.data
        password=sha256_crypt.encrypt(form.password.data)

        cursor=mysql.connection.cursor()

        sorgu="Insert into users(name,email,username,password) VALUES(%s,%s,%s,%s)"
        
        cursor.execute(sorgu,(name,email,username,password))
        mysql.connection.commit()
        cursor.close()
        
        flash("Başarıyla kayıt oldunuz...","success")

        return redirect(url_for("login"))  ##yönlendirme
    else:
        return render_template("register.html",form=form)


#Login İşlemi
@app.route("/login",methods=["GET","POST"])
def login():
    form=LoginForm(request.form)
    if request.method=="POST":
        username=form.username.data
        password_entered=form.password.data

        cursor=mysql.connection.cursor()

        sorgu="Select * from users where username=%s"

        result=cursor.execute(sorgu,(username,))

        if result>0:
            data=cursor.fetchone()
            real_password=data["password"]
            if sha256_crypt.verify(password_entered,real_password):
                flash("Başarıyla giriş yaptınız","success")

                session["logged_in"]=True
                session["username"]=username
                return redirect(url_for("index"))
            else:
                flash("Parola Yanlış","danger")
                return redirect(url_for("login"))
        else:
            flash("Böyle bir kullanıcı bulunmuyor..","danger")
            return redirect(url_for("login"))


    return render_template("login.html",form=form)

#LOGOUT İŞLEMİ
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/")
def index():
    return render_template("index.html")


##################TO DO SQLİTE3

class Todo(db.Model):    ##Veritabanı oluşturduk
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(80))
    complete=db.Column(db.Boolean)


@app.route("/add",methods=["POST"])                  ##post ile yeni todo ekleme
def addTodo():
    title=request.form.get("title")
    newTodo=Todo(title=title,complete=False)
    db.session.add(newTodo)
    db.session.commit()

    return redirect(url_for("todo"))

@app.route("/complete/<string:id>")            ###Güncelleme
def completeTodo(id):
    todo=Todo.query.filter_by(id=id).first()
    todo.complete=not todo.complete
    
    db.session.commit()
    return redirect(url_for("todo"))

@app.route("/delete/<string:id>")        ##Silme
def deleteTodo(id):
    todo=Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todo"))

    
@app.route("/todo")
def todo():
    todos=Todo.query.all()
    return render_template("todo.html",todos=todos)


#############


if __name__=="__main__":
    db.create_all()
    app.run(debug=True)


