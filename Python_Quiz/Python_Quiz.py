import os
import json
import time
import random
def Quiz():
	os.system('cls')
	name = input("\n\n\n\n\tYour Name : ")
	time.sleep(2)
	pmark = 4
	nmark = -1
	os.system('cls')
	print(f"\n\nWelcome {name} to python Quiz Program")
	print("\nAll Questions are Theoritical MCQ's there is only one answer out of 4 options")
	print("\n\nNote :- Press 1-4 to select your  answer among given four options else press 0 to skip the Question In case you don't want to answere the Question at that moment.\nYou will get one another chance to reattempt those skipped questions.\n")
	print(f"\n\nAll Questions have Equal Marks where on a correct answere you will get {pmark} marks and on a incorrect answere you will get {nmark} mark.")
	print("\nDon't Press any other key except 0-4, if you do so your paper will be submitted and marking will be done on basis of the questions you have attempted")
	print("\n\nBest of luck :-) \tYour result will be saved in result.txt file")
	print("\n\nAdvice :-> Read Questions CareFully")
	input("\nPress Any key to Start Your Test ")
	try :
		total_ques = 0
		wrong_ques = []
		wrong_ans = []
		skip_ones = []
		skip_ones_again = []
		correct_ques = 0
		incorrect_ques = 0
		skip_ques = 0
		f = open('question_bank.db')
		data = json.load(f)
		f.close()
		c = 1
		for question in data :
			os.system('cls')
			print('\n\n\n',flush=True)
			print("\n\tQuestion {}. {}".format(c,question),flush=True)
			c = c + 1
			op = [ '1. ','2. ','3. ','4. ']
			print("\n\n",flush=True)
			print("Press 0 to skip this question\n\n")
			for var in range(4):
				print('\t',op[var],data[question][0][var],sep=' ',end='\n\n',flush=True)
			print('\n\n')
			ch = input("\nYour ANSWER : ")
			if ch :
				ch = int(ch)
			else :
				print("\n\nPlease Provide an Answere ( 0- 5 ) ")
				ch = int(input("Your Answers : "))
			if ch <= 0 or ch > 4 :
				skip_ques += 1
				skip_ones.append(question)
				print("\n\nYou Have Escaped This Question")
				continue 
			print("\n\n")
			if data[question][0][ch-1].strip().lower() == data[question][1].strip().lower() : 
				correct_ques += 1
				total_ques += 1
			else : 
				wrong_ques.append(question)
				wrong_ans.append(data[question][0][ch-1])
				incorrect_ques += 1
				total_ques += 1
				
		c = 1
		for question in skip_ones :
			os.system('cls')
			print("\n\nHere are the Questions You Have Skipped Previously\n\n")
			print('\n\n\n',flush=True)
			print("\n\tQuestion {}. {}".format(c,question),flush=True)
			c = c + 1
			op = [ '1. ','2. ','3. ','4. ']
			print("\n\n",flush=True)
			print("Press 0 to skip this question\n\n")
			for var in range(4):
				print('\t',op[var],data[question][0][var],sep=' ',end='\n\n',flush=True)
			print('\n\n')
			ch = input("\nYour ANSWER : ")
			if ch :
				ch = int(ch)
			else :
				print("\n\nPlease Provide an Answere ( 0- 5 ) ")
				ch = int(input("Your Answers : "))
			if ch <= 0 or ch > 4 :
				skip_ques += 1
				total_ques += 1
				skip_ones_again.append(question)
				print("\n\nYou Have Escaped This Question")
				continue 
			print("\n\n")
			if data[question][0][ch-1].strip().lower() == data[question][1].strip().lower() : 
				correct_ques += 1
				total_ques += 1
				skip_ques -= 1
			else : 
				wrong_ques.append(question)
				wrong_ans.append(data[question][0][ch-1])
				incorrect_ques += 1
				total_ques += 1
				skip_ques -= 1
	except KeyboardInterrupt as error :
		print("\n\nYou have interrupted the Test\n\n")
	except Exception as e :
		print("\n\nInterrupted Course \n\n")
	else :
		os.system('cls')
		print('\n\n\n\n')
		print("\n\n\t\tThanks For Completing The Quiz\n\n")
		time.sleep(5)
	finally :	
		os.system('cls')
		print('\n\n\n')
		print(f"\t\tStudent Name : {name}")
		print("\t\tTotal question = ",total_ques)
		print("\n\t\tCorrect Question = ",correct_ques)
		print("\n\t\tIncorrect Question = ",incorrect_ques)
		print("\n\tSkipped Questions = ",skip_ques)
		total_marks = total_ques * pmark 
		print("\t\tTotal Marks = ",total_marks)
		marks_obtained = (correct_ques * pmark ) + ( incorrect_ques * nmark )
		print("\t\tObtained Marks = ",marks_obtained)
		per = ( marks_obtained/total_marks)*100
		print("\n\t\tPercentage Marks = {:.2f}".format(per))
		f = open('result.txt','w')
		result = f"""
		
Student Name : 			    {name}
Total Questions Attempted : {total_ques}
Total Correct Questions : 	{correct_ques}
Total InCorrect Questions : {incorrect_ques}
Total Skipped Questions : 	{skip_ques}
Total Marks : 				{total_marks}
Obtained Marks : 			{marks_obtained}
Result Percentage : 		{per:.2f}


		"""
		f.write(result)
		f.close()
		print("\n\n")
		time.sleep(4)
		input("\nPress Any Key to See The Wrong Answers You Have Given ")
		os.system('cls')
		print("\n\n\t\tHere is the question you have done wrong \n\n")
		c = 0
		input("\n\n\tPress Any Key to continue : ")
		for ques in wrong_ques : 
			os.system('cls')
			print("\n\n\n\n")
			print(c+1,ques,end='\n\n')
			print("\t\tCorrect Answer : {}".format(data[ques][1]))
			print("\t\tYour Answer Was : {}".format(wrong_ans[c]))
			print("\n\n\n")
			c = c + 1
			input("\n\n\nPress Any Key For Next Wrong Question : ")
		os.system('cls')
		print("\n\n\n\nHere are The Questions You have skipped\n\n")
		c = 1
		time.sleep(3)
		for ques in skip_ones_again :
			os.system('cls')
			print(f"Question[{c}]. {ques}")
			print("\n 1. {}\n 2. {}\n 3. {}\n 4. {}\n".format(*data[ques][0]))
			print("\n ANSWER is --> {}".format(data[ques][1]))
			print("\n\n")
			c = c + 1
			input("Press Any Key To See Next Question you have Skipped")
		input("\n\nPress any key to exit")
		 
			
	

if __name__ == '__main__' : 
    Quiz()
