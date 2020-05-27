from threadsafe_tkinter import *

root = Tk()
#Label(tk,text = 'Hello World').pack()
root.title('Event test')
root.geometry('100x100+640+480')

def callback():
    print('Event 발생!')

button = Button(root, text='Click',width= 10, command = callback)
button.pack(padx=10, pady = 10)
root.mainloop()