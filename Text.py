from tkinter import *
import tkinter.messagebox as tm
ChatWindow = Tk()
ChatWindow.geometry("500x300")
frame = Frame(ChatWindow)
frame.pack()
Counter = 0
def CreateChatWindow(Name):
	global Counter
	Counter = 1  
	window = Tk()
	window.title(Name)
	messages = Text(window, width = 30, height = 15)
	messages.pack()

	input_user = StringVar()
	input_field = Entry(window, text = input_user)
	input_field.pack(side=BOTTOM, fill=X)
	def Enter_pressed(event):
	    input_get = input_field.get()
	    print(input_get)
	    messages.insert(INSERT, '%s\n' % input_get)
	    input_field.delete(0, 'end')
	    return "break"
	frame = Frame(window) 
	input_field.bind("<Return>", Enter_pressed)
	frame.pack()
	window.mainloop()
def BuddyListBtnClicked():
	# top = Tk()
	global Counter
	def CurSelect(evt):
		# global Counter
		# if Counter ==1 :
			# WindowClose() 
		w = evt.widget
		index = int(w.curselection()[0])
		value = w.get(index)
	# if Counter == 1:
		CreateChatWindow(value)


	UserList = ['Deepika', 'Shirisha', 'Sandeep', 'Harsha', 'Santhosh', 'Murali']
	LengthOfUserList = len(UserList)

	Lb1 = Listbox(ChatWindow, width = 20, height = LengthOfUserList)
	for counter in range(LengthOfUserList):
		Lb1.insert(counter, UserList[counter])
	Lb1.bind('<<ListboxSelect>>', CurSelect)
	Lb1.pack(padx = 20)


BuddyListBtn = Button(ChatWindow, text = "Buddy List",command = BuddyListBtnClicked)
BuddyListBtn.pack(side = TOP)
ChatWindow.mainloop()