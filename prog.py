import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk as ttk
from datetime import date

 


def find_dates(first, second, all_val):

	for j in range(11, len(all_val)):
		#print("comparacao ", first[2], pd.Period(all_val[j]).year)
		if first[2] > pd.Period(all_val[j]).year:
			one = all_val[j]
			#print(all_val[j])
			continue
		elif first[2] == pd.Period(all_val[j]).year:
			#print("comparacao ",first[1], int(all_val[j][3:5]))
			if first[1] > int(all_val[j][3:5]):
				one = all_val[j]
				#print(all_val[j])
				continue
			elif first[1] == int(all_val[j][3:5]):
				#print("comparacao ",first[0], int(all_val[j][0:2]))
				if first[0] >= int(all_val[j][0:2] ):
					one = all_val[j]
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
			print(all_val[i])
			continue
		elif second[2] == pd.Period(all_val[i]).year:
			#print("comparacao ",second[1], int(all_val[i][3:5]))
			if second[1] > int(all_val[i][3:5]):
				print(all_val[i])
				continue
			elif second[1] == int(all_val[i][3:5]):
				#print("comparacao ",second[0], int(all_val[i][0:2]))
				if second[0] >= int(all_val[i][0:2] ):
					print(all_val[i])
				else:
					break
			else:
				break
		else:
			break

	return (j, i)


def fill_tree(val):


	for i,v in enumerate(val):
		i1 = i%2
		if (i1==0):
			tree.insert('', 'end', values = v,tag = 'gray')
		else:
			tree.insert('', 'end', values = v)
				


def search_code():

	values_gl = values
	entry = T.get()

	children = tree.get_children()
	
	print(children)
	
	for element in children:
		tree.delete(element)


	val = []

	for i in range(11, len(values_gl)):
		if values_gl[i][6] == entry:
			val.append([values_gl[i][1], values_gl[i][3], values_gl[i][4], values_gl[i][6], values_gl[i][7], values_gl[i][8], values_gl[i][9], values_gl[i][10]])

	fill_tree(val)



def show_all():

	values_gl = values
	

	values_gl = np.delete(values_gl, 2, 1)
	values_gl = np.delete(values_gl, 4, 1)


	children = tree.get_children()
	
	print(children)
	
	for element in children:
		tree.delete(element)


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


def fill_tree_interval(start, end):

	for i,val in enumerate(values):
		if (i >= start and i <= end):
			i1 = i%2
			if (i1==0):
				tree.insert('', 'end', values = (val[1],val[3],val[4],val[6],val[7],val[8],val[9],val[10]),tag = 'gray')
			else:
				tree.insert('', 'end', values = (val[1],val[3],val[4],val[6],val[7],val[8],val[9],val[10]))


root = tk.Tk()

root.attributes("-zoomed", True)
#root.geometry("1920x200")

file = ('InfoCEI.csv')

csv_data = pd.read_csv(file)

k = csv_data.shape

global values
global columns
global T

values = csv_data.values


columns = csv_data.columns


for i in range(10, len(values)-5):
	values[i][1] = str(np.char.strip(values[i][1]))
	values[i][3] = str(np.char.strip(values[i][3]))
	values[i][4] = str(values[i][4].replace(' ', ''))
	values[i][7] = str(values[i][7].replace(' ', '.'))


#Text type
label_search = tk.Label(text="Procurar: ")
label_search.place(relx = 0.32, rely = 0.05)


T = tk.Entry(root, width = 52) 
T.place(relx = 0.38, rely = 0.05)



#Frame

frame = tk.Frame(root, relief= 'ridge', bg='white')
frame.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.5)

tree = ttk.Treeview(frame, columns = (sorted(col for col in range(0,8))), height = 2, show = "headings")

#print(tree['columns'])

tree.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

scroll1 = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)	
scroll1.pack(side = 'right', fill = 'y')

tree.configure(yscrollcommand=scroll1.set)

scroll2 = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
scroll2.pack(side = 'bottom', fill = 'x')

tree.configure(xscrollcommand=scroll2.set)

datetosearch = [] 


datetosearch.append(17)
datetosearch.append(12)
datetosearch.append(2020)

print(datetosearch)

start_search = []

start_search.append(0)
start_search.append(12)
start_search.append(2020)

first, second = find_dates(start_search, datetosearch, values.transpose()[1])
#Button

fill_tree_interval(first, second-1)

searchbtt = tk.Button(root, text = "Buscar", width = 5, command = search_code).place(relx = 0.63, rely = 0.047)
searchbtt = tk.Button(root, text = "Mostrar Tudo", width = 9, command = show_all).place(relx = 0.68, rely = 0.047)



tree.tag_configure('gray', background='#cccccc')        


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

for i in range(0,8):
	tree.heading(i, text=header[i])
	#tree.column(i, width = 80)

#print(values_gl)



root.mainloop()
