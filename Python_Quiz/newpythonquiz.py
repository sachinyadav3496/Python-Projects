import os, sys, json, time, random

def load_Data(cls_name) :
    
    """load_Data(cls_name) --> will take a class as an argument and will read a question data set file from current directory
     named as question_bank.db which should be json file having questions, options and answeres in object from such as dictionary. 
    sample entry for question_bank.db --> 
    question_bank = {} #the data set of questions, options and answers as { 'ques1':( ['op1','op2','op3','op4'],'answer' ), 'ques2':(['op1','op2','op3','op4'],'answer' ), ... }
    """
    
    try : 

        data_file = open('question_bank.db') #opening question_bank.db file for retriving questions-answere data
        question_bank = json.load(data_file) #using json to load data as dictionary from file pointer question_bank
        data_file.close() #closing file to prevent it from corruption
        cls_name.question_bank = question_bank #loading dataset into Quiz Class for further Processing
    
    except Exception as error : 
        
        print("\n\nThere is an error reading dataset file make sure question_bank.db file is in same directory (cwd) from which you are running this script")
        print("\n\nSomething Wrong With Data File Here is the Error : ",error)

class Quiz :
    
    """Welcome to Python Quiz. Here you can test how much you know about python."""
    
    question_bank = {} #the data set of questions, options and answers as { 'ques1':( ['op1','op2','op3','op4'],'answer' ), 'ques2':(['op1','op2','op3','op4'],'answer' ), ... }
    
    def __init__(self,name):
        
        self.name  = name #Student name 
        self.wrong_ques = 0 #number of wrong questions
        self.correct_ques = 0 #number of correct question
        self.wrong_answers = {} #list to store all questions which have answered wrongly with wrong option
        self.skip_ques = [] #Questions which are skipped by the user
        self.question_number = 0 #Question Number
        self.total_ques = 0  #Total Questions Attempted
        self.prev_ques = 0 #last question 
        self.next_ques = 1 #next question 
        self.current_ques = 0 #current question 
        self.question_set = None #total Questions in Data set
        self.ques_length = None #total number of question in data set
        self.answers = { }
    
    def show_Result(self):
        try : 
            self.clr_scr()
            print(f"{self.name} Here is your result ")
            total = len(self.question_set)
            correct_question = len(self.answers)
            skip_ques  = len(self.skip_ques)
            print(f"\nTotal Questions : {total} ")
            print(f"\nSkip Questions : {skip_ques}")
            print(f"\nCorrect Questios : {correct_question}")
            incorrect_question = len(self.wrong_answers)
            print(f"\nIncorrect Questions : {incorrect_question}")
            total_attempted = len(self.answers) + len(self.wrong_answers)
            print(f"\nTotal Questions Attempted : {total_attempted}")
            per = (correct_question / total_attempted) * 100
            print(f"\nPercentage Result  : {per:.2f}")
            per = (correct_question / total)*100
            print(f"\nOverall percentage : {per:.2f} ")
            print("\n\n\n")
            input("Press any key to exit")
        except ZeroDivisionError as error : 
            self.clr_scr()
            print("\n\n\nThanks For The taking Python Quiz")
            input("\n\nPress any key to exit")




    def ask_Question(self):
        "ask_Question(self,question) --> function to ask question and take response"
        q_no = self.current_ques + 1
        if self.current_ques >= len(self.question_set) : 
            print("\n\n...............Completed Quiz Sucessfully...................")
            return None
        question = self.question_set[self.current_ques]
        ques = self.question_bank.get(question)
        ops = ques[0]
        real_ans = ques[1]
        self.clr_scr()
        print("\t\t\t\tPYTHON QUIZ\t")
        print(f"\n\t\tQ{q_no}. {question}\n")
        print(f"\n\t\t1. {ops[0]}\n")
        print(f"\n\t\t2. {ops[1]}\n")
        print(f"\n\t\t3. {ops[2]}\n")
        print(f"\n\t\t4. {ops[3]}\n")
        try : 
            ch  = input("\n\nYour Answer (p,n,1,2,3,4) : ").strip().lower()
            if ch : 
                if ch == 'p' : 
                    if self.current_ques == 0 :
                        print('\n\nCan not go back... no question attempted till now ')
                        self.ask_Question()
                    else :
                        self.prev_ques -= 1
                        self.next_ques -= 1 
                        self.current_ques -= 1
                        if self.answers.get(self.current_ques):
                            self.answers.pop(self.current_ques)
                        self.ask_Question()
                elif ch == 'n' : 
                        self.next_ques += 1
                        self.current_ques += 1
                        self.prev_ques += 1
                        self.skip_ques.append(self.current_ques) 
                        self.ask_Question()
                else : 
                    ch = int(ch) 
                    if ch == 1 and ( ops[0].strip().lower() == real_ans.strip().lower() ) : 
                        self.answers[self.current_ques] = True
                    elif ch == 2 and ( ops[1].strip().lower() == real_ans.strip().lower() ) : 
                        self.answers[self.current_ques] = True
                    elif ch == 3 and ( ops[2].strip().lower() == real_ans.strip().lower() ) : 
                        self.answers[self.current_ques] = True
                    elif ch == 4 and ( ops[3].strip().lower() == real_ans.strip().lower() ) : 
                        self.answers[self.current_ques] = True
                    elif ch > 4 or ch < 1  :
                        print("\n\n\nInvalid Input Try Again\n\n\n")
                        return self.ask_Question()
                    else : 
                        self.wrong_answers[self.current_ques] = False 
                    self.current_ques += 1
                    self.prev_ques += 1
                    self.next_ques += 1
                self.ask_Question()

            else : 
                print('\n\nPlease Give an input')
                print("p for previous question")
                print("n for next question ")
                print("1-4 for your answer")
                self.ask_Question()

        except Exception as error : 
            
            print("\n\nInvalid Input or Something Went Wrong Try Again")
            print(f"\n\nError : {error} ")
            self.ask_Question()


    def quiz(self):
        """quiz(self) --> function to conduct quiz """
        self.clr_scr()
        print("Python Quiz Program")
        print("\nInstructions :- ")
        print("\n\t\tPress ctrl+c to complete your quiz ")
        print("\nPress p for previous question")
        print("\npress n for next question ( if you want to skip current question )")
        print("\nPress 1-4 key if you want answer a question \n\n")
        input("\nPress any key to continue : ")

        self.ask_Question()

        self.clr_scr()
        print("\n\n\n\t\tRESULT TIME\n\n\n")
        print("\n\tProcessing your Result Please Wait\n\t\t")
        time.sleep(1)
        self.show_Result()
    
    def shuffle_Ques(self):

        """shuffle_Ques(self) --> Function to load questions in question set and shuffling all the questions for better quiz formation"""

        self.question_set = list(self.question_bank.keys()) #retriving total number of questions from Data Dictionary
        for var in range(5):
            random.shuffle(self.question_set) #shuffling questions five time
            #self.question_set[:10]
        self.ques_length = len(self.question_set)

    
    
    
    def clr_scr(self):
        
        """clr_scr(self) --> function to clear screen output and print some blank lines on the top."""
        time.sleep(.5) #introducing delay before clearing screen
        
        if sys.platform == 'win32' or sys.platform == 'win64' : #checking if os type is windows or linux
            os.system('cls') #clear screen on windows systems
        else :
            os.system('clear') #clear screen on linux systems
        
        print("\n\n\n\n") #four Blank Lines on the top of blank screen 

    def question_Answers(self):

        """question_Answers(self) --> It will print each question, it's options and the correct answers in case you want to discover all the answers."""
        
        question_num= 1      #var to count question numbers 
        self.clr_scr() #clearing Screen 
        print("\t\tHere is the Python Question and Answers ") 

        try : 

                        
            for ques,value in Quiz.question_bank.items(): #retreving each question, it's options and answers from quiz data set store in class variable question_bank

                self.clr_scr() #clearing screen at each question
                print(f"Question[{question_num}]: {ques}") #printing question
                option_list = value[0] #here are the options from data set
                options = [ '\n\n\t\tA. ','\n\n\t\tB. ','\n\n\t\tC.','\n\n\t\tD. '] #prepraing options to print
                options = list(zip(options,option_list))
                options = list(map(lambda var:''.join(var[0]+var[1]),options))
                print("\n\n\t\tOptions : \n",*options) #printing options
                input("\n\n\tGuess your answers and press any key to disclose the answer ") #giving a chance to guess answer
                print(f"\n\tAnswer : \t{value[1]}") #printing correct answere
                ch = input("\n\nPress any key to Continue with next Question (EOF to finish here): ") #Next Question
                if ch.strip().lower() == 'eof' : 
                    break #stop quiz function  on user demand
                print("\n\n") #printing two blank lines
                question_num += 1 #incrementing question numbers
            
            else : 
                
                print("\n\nCongrats You have Seen all The Question and Answers\n\n") #congratulations message on completing the quiz
        
        except Exception as error : 
            
            print("There is an error in Quiz Show Function ",error) #printing error message in case of some error
            

def choice():
    try : 
        return int(input("\n\nEnter Your Choice : "))
    except KeyboardInterrupt as error : 
        print("\n\nPlease Choose one options among above")
        return choice()
    except ValueError as error : 
        print("\n\nIt is not a valid choice please input only number ")
        return choice()

if __name__ == '__main__' : 
    
    try : 

        Quiz.clr_scr('self')
        load_Data(Quiz)
        st = Quiz(input("Enter your name : "))
        print("\n\nSelect Quiz Type : ")
        print("\n1. Question Answeres ")
        print("\n2. Full Quiz")
        print("\n3. Quick Quiz")
        ch =  choice()
        st.shuffle_Ques()
        if ch == 1 : 
            st.question_Answers()
            st.clr_scr()
            print("\n\nThanks for taking Python Quiz")
        elif ch == 2 : 
            st.quiz()
        elif ch == 3 : 
            st.shuffle_Ques()
            while True :
                try :  
                    n = int(input("\n\nHow many Question You Want to Answer (10,150) : "))
                    if n >= 10 and n <= 150 : 
                        break
                    else :
                        print("\n\nQuestion Limit is in Between 10 to 150 so please choose between This range")
                except ValueError as e : 
                    print("\n\nEnter only number of question like 15, 20, 100 ")
                except KeyboardInterrupt as e :
                    print("\n\nEnter only number of question like 15, 20, 100 ")
            st.question_set = st.question_set[:n]
            st.clr_scr()
            st.quiz()
        else : 
            print("Select Correct Choice ")


    except KeyboardInterrupt as keyerror: 

        st.clr_scr()
        print("\n\n\t\t\tRedirecting you to Result Page ")
        time.sleep(2)
        st.show_Result()

    except Exception as error : 

        print("Something Went Wrong ",error)

    print("\n\n\n\n")