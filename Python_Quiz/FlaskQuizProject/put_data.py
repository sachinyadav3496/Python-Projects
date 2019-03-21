import pymysql as sql 
import json 

data = json.load(open('question_bank.db'))

con = sql.connect('localhost','root','','python')
cursor = con.cursor()

cmd = """insert into quiz(ques,op1,op2,op3,op4,ans) values("{}","{}","{}","{}","{}","{}")"""
c = 1
for key,value in data.items() : 
	ques = key.strip().capitalize()
	opt = [ op.strip().lower() for op in value[0] ]
	ans = value[1].strip()
	new_cmd = cmd.format(ques,*opt,ans)
	cursor.execute(new_cmd)
con.commit()
print("Exported Data SucessFully")