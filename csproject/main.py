from asyncio.windows_events import NULL
from dataclasses import replace
from pynput import keyboard
from flask import Flask, render_template, request
from database import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'
global m
m=""
@app.route('/')
def index():
    return render_template('home.html')
    


@app.route('/focused')
def startlisten():
    global m
    m=""
    print("2222222******************hi I was here****************2222222222")
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
    

@app.route('/login',methods=['GET','POST'])
def login():
    if request.metohd=='GET':
        return render_template('login.html')
    else:
        username=request.form['username']
        password=request.form['password']
        user=user_by_username(username)
        if user:
            if user.password==password:
                return render_template('home.html')
        else:
            return render_template('login.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method=="GET":
        return render_template('signup.html')
    else:
        username=request.form['username']
        password=request.form['password'] 
        password2=request.form['password2'] 
        if password2 != password:
            return render_template('signup.html')
        allusers=query_all()
        for user in allusers:
            if user.username==username:
                return render_template('signup.html')
        createU(username,password)
        return render_template('home.html')


def on_press(key):
    print("******************hi I was here****************")
    global m
    if key==keyboard.Key.esc:
        print(m)
        return False
    try:
        k=key.char
        if(k!="space" and k!="backspace"):
            m+=k
    except:
        k=key.name
        if(k!="space" and k!="backspace"):
            m+=k
    if(k=="space"):
        k=" "
        m+=k
    if(k=="backspace"):
        m = m[:len(m)-1] + "" + m[len(m):]



        

        

            


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)