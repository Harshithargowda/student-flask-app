from flask import Flask,request,redirect,url_for,render_template
from student import Student # from student.py import Student class
import IPython

app=Flask(__name__)

students =[]

@app.route('/') #means wen u call localhost:3000/ u will be redirected to below root function
def root():
    return redirect(url_for('index')) #redirect to the url function index(ie view function)

@app.route('/students', methods=["GET","POST"]) #rest api for students
def index(): #here we are making function for index
    if request.method == 'POST':
        from IPython import embed;embed()
    return render_template('index.html',students=students) # student variable in index.html=students list in app.py

@app.route('/students/new',methods=["GET"])
def new():
    return render_template('new.html')

if __name__=='__main__':
    app.run(debug=True,port=3003)