import MySQLdb
from tkinter import *

from tkinter import messagebox
from PIL import ImageTk, Image
import tablet

def destroy_t(root):
	root.destroy()

def retrieve_input(textBox):
	inputValue=textBox.get("1.0",END)
	return inputValue

def show_cl_name(n):
	db = MySQLdb.connect(host='',    # your host, usually localhost
						 user='',         # your usernames
						 passwd='',  # your password
						 db="db")
	cur = db.cursor()
	cur.execute('SHOW COLUMNS FROM {}'.format(n))
	data = cur.fetchall()
	cur.close()
	db.close()
	return data

# 127,'bro','bob','2018-06-09'
def gen_table(n,textBox):
	inputValue=textBox.get("1.0",END)
	n = "INSERT INTO {} VALUES({});".format(n.upper(),inputValue.rstrip())
	db = MySQLdb.connect(host='',    # your host, usually localhost
						 user='',         # your username
						 passwd='',  # your password
						 db="db")
	cur= db.cursor()
	cur.execute(n)
	db.commit()
	cur.close()
	db.close()


	#SQL_Exec('SELECT * FROM {};'.format(n))

def add_to_table(n):
	window = Toplevel()
	window.wm_title('Add to table')
	
	'''
	for a in range(len(l)):

		var = StringVar()
		label = Label(window, anchor = 'n',height=15, width=30, textvariable=var, relief=RAISED,justify='left')
		var.set(a)
		label.pack(side = 'left')
		textBox=Text(window, height=10, width=50,bg='black',fg='white').pack(side='right')
		inpt.append(textBox.get("1.0","end-1c"))
	print(inpt)
	buttonCommit=Button(window, height=1, width=10, text="Done", 
						command=lambda: donee(l)).pack()
	'''
	var = StringVar()
	p = show_cl_name(n)
	fin = []
	dat = ''
	for a in p:
		dat+=str(a[0])+' '*15
		fin.append(a[0])
	var = StringVar()
	label = Label(window, anchor = 'n',height=5, textvariable=var, relief=RAISED)
	var.set('\nEnter the values of the Columns separated by commas.\n Columns are: {}'.format(dat))
	label.pack()
	textBox=Text(window, height=5, width=80,bg='black',fg='white')
	textBox.pack()
	but = Button(window, height=1,width=15,text="Done",bg = 'white', 
						command=lambda:gen_table(n,textBox),padx = 10,pady = 10).pack()

def ftest(colname,data):
	root = Toplevel()
	root.wm_title('Table Info')
	l =[]
	for a in colname:
		l.append(a[0])
	#table.insert_row([25,26,27])
	table = tablet.Table(root, l)
	table.pack(padx=10,pady=10)
	dat = []
	for a in data:

		dat.append(a)
	table.set_data(dat)

	
	root.update()
	root.mainloop()
def format_table(n):
	t1 = []
	tab = []
	lines = n.split('\n')
	for a in range(len(lines)):
		if len(lines[a])>0:
			t1.append(lines[a])
	#print(t1)
	for a in range(len(t1)):
		ne = t1[a].rstrip().split('-')
		l = []
		for b in range(len(ne)):
			if len(ne[b])>0:
				l.append(ne[b])
		tab.append(l)
	return tab

def exec_remo(n,textBox):
	txt=textBox.get("1.0",END)
	p = txt.split(',')
	l = "DELETE FROM {} WHERE {} = {};".format(n.upper(),str(p[0]),str(p[1]))
	db = MySQLdb.connect(host='',    # your host, usually localhost
						 user='',         # your username
						 passwd='',  # your password
						 db="db")
	cur= db.cursor()
	cur.execute(l)
	db.commit()
	cur.close()
	db.close()



def rem_page(n):
	window = Toplevel()
	window.wm_title('Remove page')
	var = StringVar()
	p = show_cl_name(n)
	fin = []
	dat = ''
	for a in p:
		dat+=str(a[0])+' '*10
		fin.append(a[0])
	var = StringVar()
	label = Label(window, anchor = 'n',height=5, textvariable=var, relief=RAISED)
	var.set('\nEnter id name,id of the entry to remove(eg mgid,199): {}'.format(dat))
	label.pack()
	textBox=Text(window, height=5, width=60,bg='black',fg='white')
	textBox.pack()
	but = Button(window, height=1,width=15,text="Done",bg = 'white', 
						command=lambda:exec_remo(n,textBox),padx = 10,pady = 10).pack()


def return_SQL(n):
	db = MySQLdb.connect(host='',    # your host, usually localhost
						 user='',         # your username
						 passwd='',  # your password
						 db="db")
	cur = db.cursor()
	cur.execute(n)
	data = cur.fetchall()
	dat = ''

	for a in data:
		for b in a:
			dat+=str(b)+'-'
		dat+='\n'
	db.commit()
	cur.close()
	db.close()

	return dat

def run_qu(textBox):
	inputVal = textBox.get("1.0",END)
	SQL_Exec(inputVal)


def sq_query():
	window = Toplevel()
	window.wm_title('run query')
	window.geometry("500x500")
	var = StringVar()
	label = Label(window, anchor = 'n',height=15, width=30, textvariable=var, relief=RAISED,justify='center')

	var.set('''
	List of all databases

	participants: p
	events: e
	manager: m
	judge: j
	judging: jg
	accommodation: a
	venue: v
	college: c
	event_participation: ep
	Enter query here:''')
	label.pack()
	textBox=Text(window, height=10, width=50,bg='black',fg='white')
	textBox.pack()
	buttonCommit=Button(window, height=1, width=10, text="Fetch", 
						command=lambda: run_qu(textBox))
	buttonCommit.pack()
	window.mainloop()



def del_from_table():
	window = Toplevel()
	window.wm_title('Remove entry option')
	var = StringVar()
	label = Label(window, anchor = 'n', textvariable=var,justify='center')
	var.set("Choose from the tables given: ")
	label.pack()
	buttonCommit=Button(window, height=1,width=15, text="Participants",bg = 'white', 
						command=lambda:rem_page("Participants"),padx = 10,pady = 10)
	buttonCommit.pack()
	buttonCommit1=Button(window, height=1,width=15, text="Events", bg = 'white',
						command=lambda:rem_page("Events"),padx = 10,pady = 10)
	buttonCommit1.pack()
	buttonCommit2=Button(window, height=1,width=15, text="Manager",bg = 'white', 
						command=lambda:rem_page("Manager"),padx = 10,pady = 10)
	buttonCommit2.pack()
	buttonCommit3=Button(window, height=1,width=15,text="Judge",bg = 'white', 
						command=lambda:rem_page("Judge"),padx = 10,pady = 10)
	buttonCommit3.pack()
	buttonCommit4=Button(window, height=1,width=15,text="Judging",bg = 'white', 
						command=lambda:rem_page("Judging"),padx = 10,pady = 10)
	buttonCommit4.pack()
	buttonCommit5=Button(window, height=1,width=15,text="Accommodation", bg = 'white',
						command=lambda:rem_page("Accommodation"),padx = 10,pady = 10)
	buttonCommit5.pack()
	buttonCommit6=Button(window, height=1,width=15,text="Venue",bg = 'white', 
						command=lambda:rem_page("Venue"),padx = 10,pady = 10)
	buttonCommit6.pack()
	buttonCommit7=Button(window, height=1,width=15,text="College",bg = 'white', 
						command=lambda:rem_page("College"),padx = 10,pady = 10)
	buttonCommit7.pack()
	buttonCommit8=Button(window, height=1,width=15,text="Event Participation",bg = 'white', 
						command=lambda:rem_page("event_participation"),padx = 10,pady = 10)
	buttonCommit8.pack()
	



def SQL_Exec(n):
	root =Toplevel()
	var = StringVar()
	root.wm_title('Sql query')
	label = Label(root, anchor = 'n', textvariable=var,justify='center')
	try:
		var.set(format_table(return_SQL(n)))
	except:
		var.set('Try again. There is something wrong.')
	label.pack(fill="both", expand=True)
	root.mainloop()



def table_info_view():
	window = Toplevel()
	window.wm_title('Individual info view')
	scrollbar = Scrollbar(window,bg='black')
	scrollbar.pack( side = RIGHT, fill = Y )
	scrollbar2 = Scrollbar(window,bg='black',orient = HORIZONTAL)
	scrollbar.pack( side = RIGHT, fill = Y )
	
	var = StringVar()
	label = Label(window, anchor = 'n', textvariable=var,justify='center')
	var.set("Choose from the tables given: ")
	label.pack()
	buttonCommit=Button(window, height=1,width=15, text="Participants",bg = 'white', 
						command=lambda:ind_info_view("Participants"),padx = 10,pady = 10)
	buttonCommit.pack()
	buttonCommit1=Button(window, height=1,width=15, text="Events", bg = 'white',
						command=lambda:ind_info_view("Events"),padx = 10,pady = 10)
	buttonCommit1.pack()
	buttonCommit2=Button(window, height=1,width=15, text="Manager",bg = 'white', 
						command=lambda:ind_info_view("Manager"),padx = 10,pady = 10)
	buttonCommit2.pack()
	buttonCommit3=Button(window, height=1,width=15,text="Judge",bg = 'white', 
						command=lambda:ind_info_view("Judge"),padx = 10,pady = 10)
	buttonCommit3.pack()
	buttonCommit4=Button(window, height=1,width=15,text="Judging",bg = 'white', 
						command=lambda:ind_info_view("Judging"),padx = 10,pady = 10)
	buttonCommit4.pack()
	buttonCommit5=Button(window, height=1,width=15,text="Accommodation", bg = 'white',
						command=lambda:ind_info_view("Accommodation"),padx = 10,pady = 10)
	buttonCommit5.pack()
	buttonCommit6=Button(window, height=1,width=15,text="Venue",bg = 'white', 
						command=lambda:ind_info_view("Venue"),padx = 10,pady = 10)
	buttonCommit6.pack()
	buttonCommit7=Button(window, height=1,width=15,text="College",bg = 'white', 
						command=lambda:ind_info_view("College"),padx = 10,pady = 10)
	buttonCommit7.pack()
	buttonCommit8=Button(window, height=1,width=15,text="Event Participation",bg = 'white', 
						command=lambda:ind_info_view("event_participation"),padx = 10,pady = 10)
	buttonCommit8.pack()
	buttonCommit9=Button(window, height=1, text="DONE",bg = 'white', 
						command=lambda: destroy_t(window),padx = 10,pady = 10).pack()
	#window.mainloop()



def ind_info_view(n):
	p = show_cl_name(n)
	l = []
	for a in p:
		if a[0]=='dob' or a[0]=='edate':
			l.append('Year')
			l.append('Month')
			l.append('Date')
		else:
			l.append(a)
	ftest(l,format_table(return_SQL("SELECT * FROM {}".format(n))))

def csv_format(n):
	db = MySQLdb.connect(host='',    # your host, usually localhost
						 user='',         # your username
						 passwd='',  # your password
						 db="db")
	cur = db.cursor()
	cur.execute("SELECT * FROM {}".format(n.upper()))
	data = cur.fetchall()
	finstr = ''
	for a in data:
		for b in a:
			finstr+=str(b)+','
		finstr+='\n'
	f = open(n+'.csv','w+')
	f.write(finstr)
	f.close()
	messagebox.showinfo("Info", "Done Exporting")

def run_imp(n):
	db = MySQLdb.connect(host='',    # your host, usually localhost
						 user='',         # your username
						 passwd='',  # your password
						 db="db")
	cur = db.cursor()
	inputVal = textBox.get("1.0",END)
	f = open('{}','r').read()
	clm = show_cl_name(n)
	for a in clm:
		cur.execute("desc {}".format(n.upper()))

'''
def csv_import(n):

	db = MySQLdb.connect(host='',    # your host, usually localhost
						 user='',         # your username
						 passwd='',  # your password
						 db="db")
	cur = db.cursor()
	cur.execute("desc {}".format(n.upper()))
	data = cur.fetchall()
	st = ''
	for a in data:
		for b in range(2):
			st+=str(a[b])+','
		st+='\n'
	messagebox.showinfo("Check if your csv matches these parameters",st)

	window = Toplevel()
	window.wm_title('Import from csv')
	window.geometry("500x500")
	var = StringVar()
	label = Label(window, anchor = 'n',height=15, width=30, textvariable=var, relief=RAISED,justify='center')

	var.set('Enter name of file eg:(ev.csv)')
	label.pack()
	textBox=Text(window, height=10, width=50,bg='black',fg='white')
	textBox.pack()
	buttonCommit=Button(window, height=1, width=10, text="Fetch", 
						command=lambda: run_imp(textBox))
	buttonCommit.pack()
	window.mainloop()


def import_from_csv_main():
	window = Toplevel()
	window.wm_title('Send to csv main')
	var = StringVar()
	label = Label(window,height=15, textvariable=var,justify='left')
	var.set('Choose a table')
	label.pack()

	buttonCommit=Button(window, height=1,width=15, text="Participants",bg = 'white', 
						command=lambda:csv_import("Participants"),padx = 10,pady = 10)
	buttonCommit.pack()
	buttonCommit1=Button(window, height=1,width=15, text="Events", bg = 'white',
						command=lambda:csv_import("Events"),padx = 10,pady = 10)
	buttonCommit1.pack()
	buttonCommit2=Button(window, height=1,width=15, text="Manager",bg = 'white', 
						command=lambda:csv_import("Manager"),padx = 10,pady = 10)
	buttonCommit2.pack()
	buttonCommit3=Button(window, height=1,width=15,text="Judge",bg = 'white', 
						command=lambda:csv_import("Judge"),padx = 10,pady = 10)
	buttonCommit3.pack()
	buttonCommit4=Button(window, height=1,width=15,text="Judging",bg = 'white', 
						command=lambda:csv_import("Judging"),padx = 10,pady = 10)
	buttonCommit4.pack()
	buttonCommit5=Button(window, height=1,width=15,text="Accommodation", bg = 'white',
						command=lambda:csv_import("Accommodation"),padx = 10,pady = 10)
	buttonCommit5.pack()
	buttonCommit6=Button(window, height=1,width=15,text="Venue",bg = 'white', 
						command=lambda:csv_import("Venue"),padx = 10,pady = 10)
	buttonCommit6.pack()
	buttonCommit7=Button(window, height=1,width=15,text="College",bg = 'white', 
						command=lambda:csv_import("College"),padx = 10,pady = 10)
	buttonCommit7.pack()
	buttonCommit8=Button(window, height=1,width=15,text="Event Participation",bg = 'white', 
						command=lambda:csv_import("event_participation"),padx = 10,pady = 10)
	buttonCommit8.pack()
	window.mainloop()
'''

def send_to_csv_main():
	window = Toplevel()
	window.wm_title('Send to csv main')
	var = StringVar()
	label = Label(window,height=15, textvariable=var,justify='left')
	var.set('Choose a table')
	label.pack()

	buttonCommit=Button(window, height=1,width=15, text="Participants",bg = 'white', 
						command=lambda:csv_format("Participants"),padx = 10,pady = 10)
	buttonCommit.pack()
	buttonCommit1=Button(window, height=1,width=15, text="Events", bg = 'white',
						command=lambda:csv_format("Events"),padx = 10,pady = 10)
	buttonCommit1.pack()
	buttonCommit2=Button(window, height=1,width=15, text="Manager",bg = 'white', 
						command=lambda:csv_format("Manager"),padx = 10,pady = 10)
	buttonCommit2.pack()
	buttonCommit3=Button(window, height=1,width=15,text="Judge",bg = 'white', 
						command=lambda:csv_format("Judge"),padx = 10,pady = 10)
	buttonCommit3.pack()
	buttonCommit4=Button(window, height=1,width=15,text="Judging",bg = 'white', 
						command=lambda:csv_format("Judging"),padx = 10,pady = 10)
	buttonCommit4.pack()
	buttonCommit5=Button(window, height=1,width=15,text="Accommodation", bg = 'white',
						command=lambda:csv_format("Accommodation"),padx = 10,pady = 10)
	buttonCommit5.pack()
	buttonCommit6=Button(window, height=1,width=15,text="Venue",bg = 'white', 
						command=lambda:csv_format("Venue"),padx = 10,pady = 10)
	buttonCommit6.pack()
	buttonCommit7=Button(window, height=1,width=15,text="College",bg = 'white', 
						command=lambda:csv_format("College"),padx = 10,pady = 10)
	buttonCommit7.pack()
	buttonCommit8=Button(window, height=1,width=15,text="Event Participation",bg = 'white', 
						command=lambda:csv_format("event_participation"),padx = 10,pady = 10)
	buttonCommit8.pack()
	buttonCommit10=Button(window, height=1, text="DONE",bg = 'white', 
						command=lambda: destroy_t(window),padx = 10,pady = 10).pack()
	window.mainloop()

def command_exec():
	window = Toplevel()
	window.wm_title('Add to table')
	var = StringVar()
	label = Label(window,height=15, textvariable=var,justify='left')
	var.set('Choose a table')
	label.pack()

	buttonCommit=Button(window, height=1,width=15, text="Participants",bg = 'white', 
						command=lambda:add_to_table("Participants"),padx = 10,pady = 10)
	buttonCommit.pack()
	buttonCommit1=Button(window, height=1,width=15, text="Events", bg = 'white',
						command=lambda:add_to_table("Events"),padx = 10,pady = 10)
	buttonCommit1.pack()
	buttonCommit2=Button(window, height=1,width=15, text="Manager",bg = 'white', 
						command=lambda:add_to_table("Manager"),padx = 10,pady = 10)
	buttonCommit2.pack()
	buttonCommit3=Button(window, height=1,width=15,text="Judge",bg = 'white', 
						command=lambda:add_to_table("Judge"),padx = 10,pady = 10)
	buttonCommit3.pack()
	buttonCommit4=Button(window, height=1,width=15,text="Judging",bg = 'white', 
						command=lambda:add_to_table("Judging"),padx = 10,pady = 10)
	buttonCommit4.pack()
	buttonCommit5=Button(window, height=1,width=15,text="Accommodation", bg = 'white',
						command=lambda:add_to_table("Accommodation"),padx = 10,pady = 10)
	buttonCommit5.pack()
	buttonCommit6=Button(window, height=1,width=15,text="Venue",bg = 'white', 
						command=lambda:add_to_table("Venue"),padx = 10,pady = 10)
	buttonCommit6.pack()
	buttonCommit7=Button(window, height=1,width=15,text="College",bg = 'white', 
						command=lambda:add_to_table("College"),padx = 10,pady = 10)
	buttonCommit7.pack()
	buttonCommit8=Button(window, height=1,width=15,text="Event Participation",bg = 'white', 
						command=lambda:add_to_table("event_participation"),padx = 10,pady = 10)
	buttonCommit8.pack()

	window.mainloop()

	
def helloCallBack():
	window = Toplevel()
	window.geometry("1000x1000")
	window.wm_title('Options')
	var = StringVar()
	label = Label(window,height=15, textvariable=var,justify='left')
	var.set('')
	label.pack()
	#label = Label(window, anchor = 'n',height=15, width=30, textvariable=var, relief=RAISED,justify='center')
	#label.pack()
	#textBox=Text(window, height=10, width=50,bg='black',fg='white')
	#textBox.pack()
	buttonCommit=Button(window, height=1, text="View Table info",bg = 'white', 
						command=lambda: table_info_view(),padx = 10,pady = 10).pack()
	buttonCommit2=Button(window, height=1, text="Add to a table",bg = 'white', 
						command=lambda: command_exec(),padx = 10,pady = 10).pack()
	buttonCommit3=Button(window, height=1, text="Delete an entry",bg = 'white', 
						command=lambda: del_from_table(),padx = 10,pady = 10).pack()
	buttonCommit4=Button(window, height=1, text="Export to CSV",bg = 'white', 
						command=lambda: send_to_csv_main(),padx = 10,pady = 10).pack()
	#buttonCommit5=Button(window, height=1, text="Import from CSV",bg = 'white',
						#command=lambda: import_from_csv_main(),padx = 10,pady = 10).pack()
	buttonCommit6=Button(window, height=1, text="Run an SQL query",bg = 'white', 
						command=lambda: sq_query(),padx = 10,pady = 10).pack()
	buttonCommit7=Button(window, height=1, text="DONE",bg = 'white', 
						command=lambda: exit(0),padx = 10,pady = 10).pack()

	window.mainloop()
def GUI_disp():
	top = Tk()
	top.wm_title('Welcome')

	top.geometry('1500x1500')
	var = StringVar()
	label = Label(top,height=15, textvariable=var,justify='left')
	var.set(' ')
	label.pack()
	img = PhotoImage(file = r'/Users/lordvile/Documents/STUDY/DBMS/Dbms_project/enter.gif')
	B = Button(top,text = 'Enter R.D.B',bg='systemTransparent',image = img, command = helloCallBack,padx = 0,pady=0,bd = 0)
	#B = Button(top,top.geometry("500x500"), text ="Enter DB", command = helloCallBack)
	B.pack()

	top.mainloop()

#cur.execute("desc participants")

GUI_disp()
