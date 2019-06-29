import tkinter as tk
# i dont like to import tkinter as * i don't know why
# but thats the reason
from tkinter import ttk

from threading import Thread

from multiprocessing import process
win = tk.Tk()
win.title('Clock Angle Calc')

win.geometry('800x450')
# lables for the app






#hour lable

hour_label = ttk.Label(win, text = 'Enter Value of the hour : ')
hour_label.grid(row = 0 , column = 0, sticky = 'W')

#minute label
minute_label = ttk.Label(win , text = 'Enter Value of the minutes : ')
minute_label.grid(row = 1 , column = 0, sticky = 'W')


# Entry Boxes
hour_var = tk.IntVar()
hour_entry = ttk.Entry(win, width = 15 , textvariable = hour_var)
hour_entry.grid(row = 0, column = 1)

minute_var = tk.IntVar()
minutes_entry = ttk.Entry(win, width = 15, textvariable = minute_var)
minutes_entry.grid(row = 1, column = 1)

userH  =int(hour_var.get())
userM = int(minute_var.get())

#button
def action():
    i =1 
    hour_var.get()
    minute_var.get()
    userH  =int(hour_var.get())
    userM = int(minute_var.get())
    sentence = f'{userH} hours {userM} minutes\n'
    while(i < 2):
        textbox.insert(0.0,sentence)
        i+=1
        print(userH)
        ang_hour = userH * 30
        ang_min = userM * 6
        full_ang_hour = ang_hour + ((userM/60) * 30)
        result = full_ang_hour - ang_min
        r1 = result
        r2 = 360 - result
        s1 = f'\n{r1} is acute , {r2} is obtuse\n'
        s2 = f'\n{r2} is acute , {r1} is obtuse\n'
        a = 1
        while (a < 2):
            if r2 > 180:
                textbox.insert(0.1,s1)
            elif result > 180:
                textbox.insert(0.2,s2)
            a += 1


#ang_hour = userH * 30
#ang_min = userM * 6
#
#full_ang_hour = ang_hour + ((userM/60) * 30)
#
#result = full_ang_hour - ang_min
#
#r1 = result
#r2 = 360 - result


textbox = tk.Text(win, bg='pink')
textbox.grid()
 

def action2():
    pass
        

def run():
    th =  Thread(target=action)
    th.start()
    th1 = Thread(target=action2)
    th1.start()


submit_button = ttk.Button(win, text = 'Submit', command= run)
submit_button.grid(row = 3 , column = 0)


win.mainloop()
