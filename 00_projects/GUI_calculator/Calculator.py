#!/usr/bin/env python
# coding: utf-8

# # Calculator
# - Title
# - max, min & close button
# - #menu bar
# - #history
# - display
# - clear button
# - #sq root advance signs
# - 0-9 numbers (same light shade, black)
# - basic arithmetic operator (diff dark color, black)
# - equal to button (light blue)
# - decimal point

# # Front-end

# In[1]:


import tkinter as tk


# In[10]:


app = tk.Tk()

# to decide the dimensions of calc
app.geometry('237x293')
# title of app
app.title('Calculator')

# display the result
display = tk.Text(app,height=2,width=13,fg='white',bg='#303030',font=('Arial',24,'bold'))
display.grid(row=1,columnspan=4)

#buttons 0-9
btn_1 = tk.Button(app,text='1',width=4,fg='white',bg='#505050',font=('Arial',14),command= lambda:click(1))
btn_1.grid(row=5,column=0,padx=0,pady=2)

btn_2 = tk.Button(app,text='2',width=4,fg='white',bg='#505050',font=('Arial',14),command= lambda:click(2))
btn_2.grid(row=5,column=1,padx=0,pady=2)

btn_3 = tk.Button(app,text='3',width=4,fg='white',bg='#505050',font=('Arial',14),command= lambda:click(3))
btn_3.grid(row=5,column=2,padx=0,pady=2)

btn_4 = tk.Button(app,text='4',width=4,fg='white',bg='#505050',font=('Arial',14),command= lambda:click(4))
btn_4.grid(row=4,column=0,padx=0,pady=2)

btn_5 = tk.Button(app,text='5',width=4,fg='white',bg='#505050',font=('Arial',14),command= lambda:click(5))
btn_5.grid(row=4,column=1,padx=0,pady=2)

btn_6 = tk.Button(app,text='6',width=4,fg='white',bg='#505050',font=('Arial',14),command= lambda:click(6))
btn_6.grid(row=4,column=2,padx=0,pady=2)

btn_7 = tk.Button(app,text='7',width=4,fg='white',bg='#505050',font=('Arial',14),command= lambda:click(7))
btn_7.grid(row=3,column=0,padx=0,pady=2)

btn_8 = tk.Button(app,text='8',width=4,fg='white',bg='#505050',font=('Arial',14),command= lambda:click(8))
btn_8.grid(row=3,column=1,padx=0,pady=2)

btn_9 = tk.Button(app,text='9',width=4,fg='white',bg='#505050',font=('Arial',14),command= lambda:click(9))
btn_9.grid(row=3,column=2,padx=0,pady=2)

btn_0 = tk.Button(app,text='0',width=4,fg='white',bg='#505050',font=('Arial',14),command= lambda:click(0))
btn_0.grid(row=6,column=1,padx=0,pady=2)

btn_dev = tk.Button(app,text='/',width=4,fg='white',bg='#505050',font=('Arial',14),command= lambda:click('/'))
btn_dev.grid(row=6,column=2,padx=0,pady=2)

btn_mul = tk.Button(app,text='x',width=4,fg='white',bg='#505050',font=('Arial',14),command= lambda:click('*'))
btn_mul.grid(row=3,column=3,padx=0,pady=2)

btn_sub = tk.Button(app,text='-',width=4,fg='white',bg='#505050',font=('Arial',14),command= lambda:click('-'))
btn_sub.grid(row=4,column=3,padx=0,pady=2)

btn_add = tk.Button(app,text='+',width=4,fg='white',bg='#505050',font=('Arial',14),command= lambda:click('+'))
btn_add.grid(row=5,column=3,padx=0,pady=2)

# Decimal point
btn_dec = tk.Button(app,text='.',width=4,fg='white',bg='#505050',font=('Arial',14),command= lambda:click('.'))
btn_dec.grid(row=6,column=0,padx=0,pady=2)

# CLear button
btn_cl = tk.Button(app,text='C',width=4,fg='white',bg='#505050',font=('Arial',14),command = clear)
btn_cl.grid(row=2,column=2,padx=0,pady=2)

btn_del = tk.Button(app,text='⌫',width=4,fg='white',bg='#505050',font=('Arial',14),command = dell)
btn_del.grid(row=2,column=3,padx=0,pady=2)

btn_ce = tk.Button(app,text='CE',width=4,fg='white',bg='#505050',font=('Arial',14),command = clear)
btn_ce.grid(row=2,column=1,padx=0,pady=2)

btn_mod = tk.Button(app,text='%',width=4,fg='white',bg='#505050',font=('Arial',14),command= lambda:click('%'))
btn_mod.grid(row=2,column=0,padx=0,pady=2)

# Equal to button
btn_eq = tk.Button(app,text='=',width=4,fg='black',bg='#00FFFF',font=('Arial',14),command= result )
btn_eq.grid(row=6,column=3,padx=0,pady=2)

app.mainloop()


# # Back-end
# - 

# In[2]:


# For clicking the button

calculation = ''
def click(symbol):
    global calculation
    calculation += str(symbol)
    display.delete(1.0,'end')
    display.insert(1.0,calculation)


# In[3]:


# Calculation of input

def result():
    try:
        global calculation
        calculation = str(eval(calculation))
        display.delete(1.0,'end')
        display.insert(1.0,calculation)
    except:
        #To hande the error part
        clear()
        display.insert(1.0,'Error')


# In[4]:


# Clear of display

def clear():
    global calculation
    calculation = ''
    display.delete(1.0,'end')


# In[9]:


def dell():
    global calculation
    calculation = calculation[:-1]
    display.delete(1.0,'end')
    display.insert(1.0,calculation)


# In[ ]:




