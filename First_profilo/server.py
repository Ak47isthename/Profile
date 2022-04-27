
from unicodedata import name
from flask import Flask, redirect, render_template, request
# import the class from friend.py
from users import User
app = Flask(__name__)
@app.route('/')
def index():
    return redirect('/awet/pro')

@app.route('/awet/pro')
def awet_massages():
    return render_template('index.html', users=User.get_all())


@app.route('/user/create', methods=['POST'])
def create():
    
    print(request.form)
    User.save(request.form)
    

    return redirect('/awet/pro')



if __name__=="__main__":
    app.run(debug=True)