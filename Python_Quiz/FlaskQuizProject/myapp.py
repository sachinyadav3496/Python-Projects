from flask import Flask,request,render_template,session,redirect,jsonify
import pymysql as sql
import json 
from datetime import timedelta
import random 

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

with open('question_bank.db') as f : 
        data = json.load(f)
        f.close() 
questions =[ 
        { 'question': d, 'options': data[d][0],'answer':data[d][1] } for d in data 
        ]
random.shuffle(questions)
questions = questions[:50]

total_ques = len(questions)


@app.route('/')
def index():
    if 'username' in session and 'ques' in session :
            return render_template('quiz.html',name=session['username'],course=session['course'])
    
    return render_template('index.html')
    
@app.route('/startquiz/',methods=['GET','POST'])
def startquiz():
    if request.method == 'POST' : 
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        course = request.form['course']
        session['username'] = fname.capitalize()+" "+lname.capitalize()
        session['course'] = course.upper()
        session['ques'] = 0
        return render_template('quiz.html',name=session['username'],course=session['course'])
    #return "Invalid Form Method We Only Accept POST Methods"
    elif 'username' in session :#and 'ques' in session :
            return render_template('quiz.html',name=session['username'],course=session['course'])
    else : 
        return redirect("/", code=302)


@app.route('/logout/')
def logout():
    session.pop('username',None)
    session.pop('course',None)
    #session.pop('ques',None)
    return redirect("/", code=302)


@app.route('/question/<int:ques>')
def question(ques=None):
    if ques < len(questions):
        session['ques'] = ques 
        new_ques = { 'question': questions[ques]['question'],'options':questions[ques]['options'],'total_questions':total_ques}
        return jsonify(new_ques)
    else : 
        return jsonify(None)


@app.route('/check_question/',methods=['POST','GET'])
def check():
    ques = request.form['ques']
    ans = request.form['answer']
    print(ques,ans)
    if str(questions[int(ques)]['answer']).strip().lower() == str(ans).strip().lower() : 

        return jsonify(True)
    else : 
        return jsonify(False)

if __name__ == "__main__" : 
    app.run(debug=True)
    #app.run('192.168.1.107',5000,debug=True)
