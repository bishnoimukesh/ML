from Tkinter import *
root= Tk()
root.title('deep.tech')
root.configure(background='black')
root.geometry('360x480')

details = Label(root, text='enter roll no:', width=30, bg = "green")
details.grid(row=0,column=0)


num1=Entry(root, width=10, bg='pink')
num1.grid(row=1,column=0)




def changename():
    roll_number=int(num1.get() )
    f=open('student.py')
    i=1
    for student in f:
        if i ==roll_number:
            all_details=student
        i=i+1
    li_details=all_details.split(',')
    details_of_user='name:'+ li_details[0] + 'marks' + li_details[1]+ 'attendance:' + li_details[2]
    
    details.configure(text=details_of_user)
    

btn=Button(root, width=10,bg='red', fg='red', command=changename)
btn.grid(row=2,column=1)

root.mainloop()
