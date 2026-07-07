import json
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_PATH = os.path.join(BASE_DIR, 'questions.json')
SCORES_PATH = os.path.join(BASE_DIR, 'scores.json')

root = Tk()
root.geometry('405x585')
root.config(bg='#99C377')
root.resizable(0, 0)

# Function
def load_questions():
    try:
        with open(QUESTIONS_PATH, 'r', encoding='utf-8') as file:
            questions = json.load(file)
        if len(questions) < 3:
            raise ValueError("Need at least 3 questions in questions.json")
        return questions
    except FileNotFoundError:
        messagebox.showerror('Error', 'questions.json not found!')
        root.destroy()
        exit()
    except (json.JSONDecodeError, ValueError) as e:
        messagebox.showerror('Error', f'Invalid questions.json: {e}')
        root.destroy()
        exit()


quiz_data = load_questions()


def save_score(name, score, total):
    try:
        with open(SCORES_PATH, 'r', encoding='utf-8') as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = []
    except json.JSONDecodeError:
        scores = []

    new_result = {
        "name": name,
        "score": score,
        "total": total,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    scores.append(new_result)

    try:
        with open(SCORES_PATH, 'w', encoding='utf-8') as file:
            json.dump(scores, file, ensure_ascii=False, indent=4)
    except OSError as e:
        messagebox.showerror('Error', f'Could not save score: {e}')


def clear():
    ent_name.delete(0, END)
    var_answer1.set('x')
    var_answer2.set('x')
    var_answer3.set('x')
    lbl_score.config(text='')
    btn_accept.config(state='normal')


def accept():
    name = ent_name.get().strip()
    if name == '':
        messagebox.showerror('Error', 'Please enter your name!')
        return

    score = 0
    answer_1 = var_answer1.get()
    answer_2 = var_answer2.get()
    answer_3 = var_answer3.get()

    if answer_1 == 'x' or answer_2 == 'x' or answer_3 == 'x':
        messagebox.showerror('Error', 'Please answer all the questions!')
        return

    if answer_1 == quiz_data[0]['answer']:
        score += 1
    if answer_2 == quiz_data[1]['answer']:
        score += 1
    if answer_3 == quiz_data[2]['answer']:
        score += 1

    save_score(name, score, len(quiz_data))
    lbl_score.config(text=f'Score : {score}')
    btn_accept.config(state='disabled')
    root.after(4000, clear)


def cancel():
    result = messagebox.askquestion('Exit', 'Are you sure to exit?')
    if result == 'yes':
        root.destroy()


# widget
btn_accept = Button(root, text='Accept', font='arial 16', width=14, command=accept)
btn_accept.place(x=15, y=520)

btn_cancel = Button(root, text='Cancel', font='arial 16', width=14, fg='red', command=cancel)
btn_cancel.place(x=205, y=520)

ent_name = Entry(root, font='arial 18', width=16)
ent_name.place(x=160, y=20)
ent_name.focus_set()

lbl_name = Label(root, text='Name:', font='arial 20 bold', fg='brown')
lbl_name.place(x=20, y=20)

lbl_score = Label(root, text='Score :', font='arial 22 bold', fg='blue')
lbl_score.place(x=140, y=465)

lbl_q1 = Label(root, text=quiz_data[0]['question'], font='arial 14 bold', fg='purple')
lbl_q1.place(x=10, y=80)

lbl_q2 = Label(root, text=quiz_data[1]['question'], font='arial 13 bold', fg='purple')
lbl_q2.place(x=14, y=220)

lbl_q3 = Label(root, text=quiz_data[2]['question'], font='arial 15 bold', fg='purple')
lbl_q3.place(x=10, y=360)

# radiobutton q1
var_answer1 = StringVar()
var_answer2 = StringVar()
var_answer3 = StringVar()

var_answer1.set('x')
var_answer2.set('x')
var_answer3.set('x')

rb_answer1_1 = Radiobutton(root, text=quiz_data[0]['options'][0], font='arial 12', variable=var_answer1, value=quiz_data[0]['options'][0])
rb_answer1_2 = Radiobutton(root, text=quiz_data[0]['options'][1], font='arial 12', variable=var_answer1, value=quiz_data[0]['options'][1])
rb_answer1_3 = Radiobutton(root, text=quiz_data[0]['options'][2], font='arial 12', variable=var_answer1, value=quiz_data[0]['options'][2])

rb_answer1_1.place(x=60, y=140)
rb_answer1_2.place(x=160, y=140)
rb_answer1_3.place(x=260, y=140)

# radiobutton q2
rb_answer2_1 = Radiobutton(root, text=quiz_data[1]['options'][0], font='arial 12', variable=var_answer2, value=quiz_data[1]['options'][0])
rb_answer2_2 = Radiobutton(root, text=quiz_data[1]['options'][1], font='arial 12', variable=var_answer2, value=quiz_data[1]['options'][1])
rb_answer2_3 = Radiobutton(root, text=quiz_data[1]['options'][2], font='arial 12', variable=var_answer2, value=quiz_data[1]['options'][2])

rb_answer2_1.place(x=60, y=280)
rb_answer2_2.place(x=160, y=280)
rb_answer2_3.place(x=260, y=280)

# radiobutton q3
rb_answer3_1 = Radiobutton(root, text=quiz_data[2]['options'][0], font='arial 12', variable=var_answer3, value=quiz_data[2]['options'][0])
rb_answer3_2 = Radiobutton(root, text=quiz_data[2]['options'][1], font='arial 12', variable=var_answer3, value=quiz_data[2]['options'][1])
rb_answer3_3 = Radiobutton(root, text=quiz_data[2]['options'][2], font='arial 12', variable=var_answer3, value=quiz_data[2]['options'][2])

rb_answer3_1.place(x=60, y=420)
rb_answer3_2.place(x=160, y=420)
rb_answer3_3.place(x=260, y=420)

root.mainloop()
