import tkinter as tk
#import the tkinter library
#tkinter is used to create GUI(graphical user interface)applications

#Main Window 

quiz=tk.Tk()
#tk.Tk make the main window application window
#we store this  window inside the variable 'quiz'

quiz.title('python quiz')
#title() set the title at the top of the window

quiz.geometry('500x500')
#geometry() sets the size of the window
#500=width
#500=height

#Quiz Questions

questions=[
    'What color is a Flamingo?',
    'Who was the first US president?',
    'What is the largest planet in our solar system?',
    'What gas makes up most of Earths air?',
]
#this is a list containing all the quiz questions
#each question is stored as a string

#question[0]=first question
#question[1]=second question
#question[2]=third question
#question[3]=fourth question

#Quiz Options

options=[
    ['blue','pink','purple','red'],
    ['George Washington','Donald Trump','Obama','Indira Gandhi'],
    ['Mars','Saturn','Uranus','Jupiter'],
    ['Oxygen','Carbon dioxide','Nitrogen','Carbon Monoxide'],
]
#this is a list containing options for each question

#the first inner list contains the options for question 1
#the second inner list contains options for qusetion 2
#and so on.

#for example option[0][0]='blue'
#and option[0][1]='pink'

#Correct Answers

answers=[
    'pink',
    'George Washington',
    'Jupiter',
    'Nitrogen',
]
#this list contains the correct answers for each question

#answer[0]=ans for question 1
#answer[1]=ans for question 2 ect.


#Variables to keep track of quiz

current=0
#this variable keeps track of which question we are showing

#python list numbering starts from 0

#0=question 1
#1=question 2
#2=question 3
#3=question 4

score=0
#this variable stores the score
#right now it is 0

#variable for selected radio button

selected=tk.StringVar()
#StringVar() is a special tk variable
#it will store the option selected

#for example if user chooses 'blue':

#selected.get()

#function to display questions

def show_question():
    #this function displays the current question and its options

    selected.set('')
    #this clears the previous answers
    #and no radio button will be selected
    #when new question appears

    question.config(
        text=questions[current]
    )
    #config() changes the properties of an existing widget

    #here we change the text of question

    #questions[current]
    #gets the current question from the questions list

    #for example:if current=0:
    
    #question[0]

    #gives the first question etc.

    option1.config(
        text=options[current][0],
        value=options[current][0]
    )

    option2.config(
        text=options[current][1],
        value=options[current][1]
    )

    option3.config(
        text=options[current][2],
        value=options[current][2]
    )

    option4.config(
        text=options[current][3],
        value=options[current][3]
    )

def check_answer():
    global current
    global score

    user_answer=selected.get()
    if user_answer==answers[current]:
        score += 1

    current += 1

    if current<len(questions):
        show_question()
    else:
        question.config(
            text='Quiz Finished'
        )

        option1.pack_forget()
        option2.pack_forget()
        option3.pack_forget()
        option4.pack_forget()
        button.pack_forget()
               
    result.config(
        text=f'Your Score:{score}/{len(questions)}'
    )

question=tk.Label(
    quiz,
    text='',
    font=('Arial',16),
    wraplength=450
)

question.pack(pady=30)

option1=tk.Radiobutton(
    quiz,
    variable=selected,
    )

option1.pack(anchor='w',padx=100)

option2=tk.Radiobutton(
    quiz,
    variable=selected,
    )

option2.pack(anchor='w',padx=100)

option3=tk.Radiobutton(
    quiz,
    variable=selected,
    )

option3.pack(anchor='w',padx=100)

option4=tk.Radiobutton(
    quiz,
    variable=selected,
    )

option4.pack(anchor='w',padx=100)

button=tk.Button(
    quiz,
    text='Sumbmit',
    command=check_answer
)

button.pack(pady=25)

result=tk.Label(
    quiz,
    text='',
    font=('Arial',16),
)

result.pack()

show_question()

quiz.mainloop()