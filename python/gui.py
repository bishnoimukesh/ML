from Tkinter import *
root= Tk()
root.title('deep.tech')
root.configure(background='black')
root.geometry('360x480')
name = Label(root, text='entervalue:', width=20, bg = "green")
name.grid(row=0,column=0)

num1=Entry(root, width=20, bg='pink')
num1.grid(row=1,column=0)

num2=Entry(root, width=20, bg='pink')
num2.grid(row=2,column=0)

def changename():
    value_a=num1.get()
    value_b=num2.get()
    sum=int(value_a)+int(value_b)
    
    name.configure(text='your sum is:' + str(sum) )
    

btn=Button(root, width=10,bg='red', fg='red', command=changename)
btn.grid(row=2,column=1)



root.mainloop()


