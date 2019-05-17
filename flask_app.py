from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import current_user, login_user, logout_user, login_required, LoginManager, UserMixin
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="cnzume1",
    password="6E95msGrTWjcWpH",
    hostname="cnzume1.mysql.pythonanywhere-services.com",
    databasename="cnzume1$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.secret_key = "updatedpasswordagain"
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username=user_id).first()

class Student(db.Model):

    __tablename__ = "students"

    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(4096))
    last_name = db.column(db.String(4096))
    email_address = db.column(db.String(4096))
    student_major = db.column(db.String(4096))
    posted = db.Column(db.DateTime, default=datetime.now)

    commenter_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    commenter = db.relationship('User', foreign_keys=commenter_id)
   
class Assignment(db.Model)

    __tablename__ = "assignments"
    
    assignment_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(4096))
    assigner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    assigner = db.relationship('User', foreign_keys=assigner_id)
    
class Grade(db.Model)

    __tablename__ = "grades"
    
    grade_id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    student_id = db.Column(db.Integer, db.ForeignKey('student_id')
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignment_id')                       
                           
                          
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=Comment.query.all())

    if not current_user.is_authenticated:
        return redirect(url_for('index'))

    student = Student(first=request.form["contents"], assigner=current_user)
    db.session.add(student)
    db.session.commit()
    return redirect(url_for('index'))
                              
    student = Student(first=request.form["contents"], assigner=current_user)
    db.session.add(student)
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login_page.html", error=False)

    user = load_user(request.form["username"])
    if user is None:
        return render_template("login_page.html", error=True)

    if not user.check_password(request.form["password"]):
        return render_template("login_page.html", error=True)

    login_user(user)
    return redirect(url_for('index'))

@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
