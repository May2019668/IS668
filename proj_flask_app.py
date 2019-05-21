from flask import Flask, render_template, url_for, flash, redirect
from proj_forms import StudentForm, AssignmentForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

students = [
    {
        'firstname': 'Corey',
        'lastname': 'Blunder',
        'email': 'cblunder@umbc.edu',
        'major': 'Economics'
    },
    {
        'firstname': 'Jane',
        'lastname': 'Doe',
        'email': 'jdoe@umbc.edu',
        'major': 'Anatomy'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', students=students)


@app.route("/description")
def description():
    return render_template('describe.html', title='Our Project')


@app.route("/student", methods=['GET', 'POST'])
def student():
    form = StudentForm()
    if form.validate_on_submit():
        flash('Student {form.firstname.data} Added' , 'success')
        return redirect(url_for('home'))
    return render_template('student.html', title='Add Student', form=form)

@app.route("/assignment", methods=['GET', 'POST'])
def assignment():
    form = AssignmentForm()
    if form.validate_on_submit():
        flash('Assignment Number {form.assignment_number.data}, {form.assignment_title.data} Added!', 'success')
        return redirect(url_for('home'))
    return render_template('assignment.html', title='Add Assignment', form=form)    


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)