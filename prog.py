import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk as ttk
from datetime import date

 
def options(frame):

	global chosen

	OPTIONS = ["Codigo","Data"]

	chosen = tk.StringVar(frame)
	chosen.set(OPTIONS[0]) # default

	w = tk.OptionMenu(frame, chosen, *OPTIONS)
	w.place(relx = 0.75, rely = 0.047)

	button = tk.Button(frame, text="OK", command=decide)
	button.place(relx = 0.80, rely = 0.047)



def find_dates(first, second, all_val):

	i = 0
	j = 0

	for j in range(10, len(all_val)):
		#print("comparacao ", first[2], pd.Period(all_val[j]).year)
		if first[2] > pd.Period(all_val[j]).year:
			#print(all_val[j])
			continue
		elif first[2] <= pd.Period(all_val[j]).year:
			#print("comparacao ",first[1], int(all_val[j][3:5]))
			if first[1] > int(all_val[j][3:5]):
				pass
				#print(all_val[j])
				continue
			elif first[1] <= int(all_val[j][3:5]):
				#print("comparacao ",first[0], int(all_val[j][0:2]))
				if first[0] > int(all_val[j][0:2] ):
					pass
					#print(all_val[j])
				else:
					break
			else:
				break
		else:
			break


	for i in range(j, len(all_val)):
		#print("comparacao ", second[2], pd.Period(all_val[i]).year)
		if second[2] > pd.Period(all_val[i]).year:
			pass
			continue
		elif second[2] == pd.Period(all_val[i]).year:
			#print("comparacao ",second[1], int(all_val[i][3:5]))
			if second[1] > int(all_val[i][3:5]):
				pass
				continue
			elif second[1] == int(all_val[i][3:5]):
				#print("comparacao ",second[0], int(all_val[i][0:2]))
				if second[0] >= int(all_val[i][0:2] ):
					pass
				else:
					break
			else:
				break
		else:
			break

	return (j, i-1)


def fill_tree(tree, val):

	children = tree.get_children()
	
	
	for element in children:
		tree.delete(element)

	for i,v in enumerate(val):
		i1 = i%2
		if (i1==0):
			tree.insert('', 'end', values = v,tag = 'gray')
		else:
			tree.insert('', 'end', values = v)
				


def search_code(T, tree):

	values_gl = values
	entry = T.get()


	val = []

	for i in range(10, len(values_gl)):
		if values_gl[i][6] == entry:
			val.append([values_gl[i][1], values_gl[i][3], values_gl[i][4], values_gl[i][6], values_gl[i][7], values_gl[i][8], values_gl[i][9], values_gl[i][10]])

	fill_tree(tree, val)



def show_all(tree):

	values_gl = values
	

	values_gl = np.delete(values_gl, 2, 1)
	values_gl = np.delete(values_gl, 4, 1)

	#print(values_gl)
	for i,val in enumerate(values_gl):
		#print(val)
		if (i >= 10 and i <= len(values_gl)-6):
			i1 = i%2
			if (i1==0):
				tree.insert('', 'end', values = (val[sorted(j for j in range(1,9))]),tag = 'gray')
				#tree.insert('', 'end', values = (val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7],val[8],val[9],val[10],val[11],val[12],val[13],val[14],val[15]),tag = 'gray')
			else:
				#tree.insert('', 'end', values = (val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7],val[8],val[9],val[10],val[11],val[12],val[13],val[14],val[15]))
				tree.insert('', 'end', values = (val[sorted(j for j in range(1, 9))]))


def fill_tree_interval(tree, start, end):

	children = tree.get_children()
	
	
	for element in children:
		tree.delete(element)


	for i,val in enumerate(values):
		if (i >= start and i <= end):
			i1 = i%2
			if (i1==0):
				tree.insert('', 'end', values = (val[1],val[3],val[4],val[6],val[7],val[8],val[9],val[10]),tag = 'gray')
			else:
				tree.insert('', 'end', values = (val[1],val[3],val[4],val[6],val[7],val[8],val[9],val[10]))


def create_tree(frame_name):


	header = []

	for i, val in enumerate(values):

		if (i >= 9):
			header[1:10] = val[sorted(j for j in range(1, k[1]-3))]
			break


	header.pop(1)
	#print(header)
	header.pop(3)
	#print(header)
	#print(len(header))

	#Frame
	frame = tk.Frame(frame_name, relief= 'ridge', bg='white')
	frame.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.5)

	tree = ttk.Treeview(frame, columns = (sorted(col for col in range(0,8))), height = 2, show = "headings")

	#print(tree['columns'])

	tree.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

	scroll1 = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)	
	scroll1.pack(side = 'right', fill = 'y')

	tree.configure(yscrollcommand=scroll1.set)

	scroll2 = ttk.Scrollbar(frame_name, orient="horizontal", command=tree.xview)
	scroll2.pack(side = 'bottom', fill = 'x')

	tree.configure(xscrollcommand=scroll2.set)

	tree.tag_configure('gray', background='#cccccc')

	for i in range(0,8):
		tree.heading(i, text=header[i])
		#tree.column(i, width = 80)

	#print(values_gl)
	return tree


def exe_page_one(page_one):
	
	options(page_one)

	#Text type
	label_search = tk.Label(page_one, text="Procurar: ")
	label_search.place(relx = 0.32, rely = 0.05)


	T = tk.Entry(page_one, width = 52) 
	T.place(relx = 0.38, rely = 0.05)

	tree = create_tree(page_one)


	searchbtt = tk.Button(page_one, text = "Buscar", width = 5, command = lambda: search_code(T, tree)).place(relx = 0.63, rely = 0.047)
	searchbtt = tk.Button(page_one, text = "Mostrar Tudo", width = 9, command = lambda: show_all(tree)).place(relx = 0.68, rely = 0.047)



def convert_month(month):

	if month == "Janeiro":
		number = 1
	elif month == "Fevereiro":
		number = 2
	elif month == "Marco":
		number = 3
	elif month == "Abril":
		number = 4
	elif month == "Maio":
		number = 5
	elif month == "Junho":
		number = 6
	elif month == "Julho":
		number = 7
	elif month == "Agosto":
		number = 8
	elif month == "Setembro":
		number = 9
	elif month == "Outubro":
		number = 10
	elif month == "Novembro":
		number = 11
	elif month == "Dezembro":
		number = 12

	return number


def exe_page_data(tree_dates, date_d_to, date_m_to, date_y_to, date_d_from, date_m_from, date_y_from):

	d_to = int(date_d_to.get())
	m_to = convert_month(date_m_to.get())
	y_to = int(date_y_to.get())

	datetosearch = [] 

	datetosearch.append(d_to)
	datetosearch.append(m_to)
	datetosearch.append(y_to)

	start_search = []

	d_from = int(date_d_from.get())
	m_from = convert_month(date_m_from.get())
	y_from = int(date_y_from.get())

	start_search.append(d_from-1)
	start_search.append(m_from)
	start_search.append(y_from)

	first, second = find_dates(start_search, datetosearch, values.transpose()[1])

	
	fill_tree_interval(tree_dates, first, second)


def get_entry_dates():

	MONTHS = ["Janeiro","Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

	page_data = tk.Frame(root, relief= 'ridge')
	page_data.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

	tree_dates = create_tree(page_data)

	chosen_from = tk.StringVar(page_data)
	chosen_from.set(MONTHS[0]) # default

	date_d_from = tk.Entry(page_data, width = 10) 
	date_d_from.place(relx = 0.38, rely = 0.05)

	date_m_from = tk.OptionMenu(page_data, chosen_from, *MONTHS)
	date_m_from.place(relx = 0.43, rely = 0.05)

	date_y_from = tk.Entry(page_data, width = 10) 
	date_y_from.place(relx = 0.50, rely = 0.05)

	chosen_to = tk.StringVar(page_data)
	chosen_to.set(MONTHS[0]) # default

	date_d_to = tk.Entry(page_data, width = 10) 
	date_d_to.place(relx = 0.38, rely = 0.1)

	date_m_to = tk.OptionMenu(page_data, chosen_to, *MONTHS)
	date_m_to.place(relx = 0.43, rely = 0.1)

	date_y_to = tk.Entry(page_data, width = 10) 
	date_y_to.place(relx = 0.50, rely = 0.1)


	datesbtt = tk.Button(page_data, text = "Buscar", width = 5, command = lambda: exe_page_data(tree_dates, date_d_to, chosen_to, date_y_to, date_d_from, chosen_from, date_y_from))
	datesbtt.place(relx = 0.75, rely = 0.047)
	


def decide():

	test = chosen.get()

	if test == 'Codigo':
		exe_page_one()
	elif test == 'Data':
		get_entry_dates()



global root

root = tk.Tk()

root.attributes("-zoomed", True)
#root.geometry("1920x200")

file = ('InfoCEI.csv')

csv_data = pd.read_csv(file)

k = csv_data.shape

global values
global columns


values = csv_data.values
columns = csv_data.columns


for i in range(10, len(values)-5):
	values[i][1] = str(np.char.strip(values[i][1]))
	values[i][3] = str(np.char.strip(values[i][3]))
	values[i][4] = str(values[i][4].replace(' ', ''))
	values[i][7] = str(values[i][7].replace(' ', '.'))



page_one = tk.Frame(root, relief= 'ridge')
page_one.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

exe_page_one(page_one)

page_one.mainloop()
