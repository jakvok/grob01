#!/usr/bin/python3

'''
The utility converts dimmensional corrections from rotated coordinate system to non-rotated, basic oriented machine coordinate system.
'''

import tkinter
from tkinter import ttk
import sys

# definitions of event functions

def x_plus():
    # to increase X dimm in 0.01mm
    a = float(x.get())
    a += 0.01
    x.set(round(a, 2))

def x_minus():
    # to decrease X dimm in 0.01mm
    a = float(x.get())
    a -= 0.01
    x.set(round(a, 2))

def y_plus():
    # to increase Y dimm in 0.01mm
    a = float(y.get())
    a += 0.01
    y.set(round(a, 2))

def y_minus():
    # to decrease Y dimm in 0.01mm
    a = float(y.get())
    a -= 0.01
    y.set(round(a, 2))

def z_plus():
    # to increase Z dimm in 0.01mm
    a = float(z.get())
    a += 0.01
    z.set(round(a, 2))

def z_minus():
    # to decrease Z dimm in 0.01mm
    a = float(z.get())
    a -= 0.01
    z.set(round(a, 2))

def convert():
    '''
    converts dimms from one coordinate system to other
    '''
    # get values from input variables
    a = float(x.get())
    b = float(y.get())
    c = float(z.get())

    # if operation 10 is choosen
    if csys.get() == 'op10':
        X = -0.707*c +0.707*b
        Y = 0.707*c +0.707*b
        Z = a
    else: # or if operation 20 is choosen
        X = 0.707*c -0.707*b
        Y = 0.707*c +0.707*b
        Z = -1*a

    # set result values into variables
    x_res.set(round(X, 3)) 
    y_res.set(round(Y, 3))
    z_res.set(round(Z, 3))


def nulling():
    # sets input variables to zero
    x.set(0.0)
    y.set(0.0)
    z.set(0.0)


# main container 
root = tkinter.Tk()

# ttk styles definitions
style=ttk.Style()
style.configure('EXE.TButton', foreground='green')
style.configure('EXIT.TButton', foreground='red')
style.configure('RES.TLabel', background='white', font=('bold'))

# tkinter interactive variables definitions
csys = tkinter.StringVar() # radiobutton variable, choosen operation
csys.set('op10') # set initial value

x = tkinter.DoubleVar() # x axis input variable
x.set(0.0) # initial value set to 0
y = tkinter.DoubleVar() # y axis input variable
y.set(0.0)
z = tkinter.DoubleVar() # z axis input variable
z.set(0.0)
x_res = tkinter.DoubleVar() # output x axis variable
x_res.set(0.0)
y_res = tkinter.DoubleVar() # output y axis variable
y_res.set(0.0)
z_res = tkinter.DoubleVar() # output z axis variable
z_res.set(0.0)

# widget definitions

# rdiobuttons to choose from two operations
radio10 = ttk.Radiobutton(root, variable=csys, value='op10', text='Operace 10: G54, G56')
radio20 = ttk.Radiobutton(root, variable=csys, value='op20', text='Operace 20: G55, G57')

# empty label to add row space
empty_label = ttk.Label(root, text='     ')

x_lab = ttk.Label(text=' X: ') # label axis description
x_label = ttk.Label(root, textvariable=x) # label shows input variable value x
x_Pbutton = ttk.Button(root, text='+0.01', command=x_plus) # button to increase value
x_Mbutton = ttk.Button(root, text='-0.01', command=x_minus) # button to decrease value

y_lab = ttk.Label(text=' Y: ')
y_label = ttk.Label(root, textvariable=y) # label shows input variable value y
y_Pbutton = ttk.Button(root, text='+0.01', command=y_plus)
y_Mbutton = ttk.Button(root, text='-0.01', command=y_minus)

z_lab = ttk.Label(text=' Z: ')
z_label = ttk.Label(root, textvariable=z) # label shows input variable value z
z_Pbutton = ttk.Button(root, text='+0.01', command=z_plus)
z_Mbutton = ttk.Button(root, text='-0.01', command=z_minus)

x_res_lbl = ttk.Label(root, text='Result X:') # label output value description
x_res_label = ttk.Label(root, textvariable=x_res, style='RES.TLabel') # label output value x axis
y_res_lbl = ttk.Label(root, text='Result Y:')
y_res_label = ttk.Label(root, textvariable=y_res, style='RES.TLabel') # label output value y axis
z_res_lbl = ttk.Label(root, text='Result Z:')
z_res_label = ttk.Label(root, textvariable=z_res, style='RES.TLabel') # label output value z axis


exec_button = ttk.Button(text='EXECUTE', style='EXE.TButton', command=convert) # convert function button 
null_button = ttk.Button(text='NULL', command=nulling) # nulling function button
exit_button=ttk.Button(text='EXIT', style='EXIT.TButton', command=lambda: sys.exit(0)) # exit app button


# geometry definition, grid packing manager

# radiobuttons in the first two rows
radio10.grid(column=1, row=1, columnspan=2, sticky=tkinter.NSEW, pady=7)
radio20.grid(column=1, row=2, columnspan=2, sticky=tkinter.NSEW, pady=7)

empty_label.grid(column=0, row=3) # empty label to add empty space in row 3

# x axis input widgwts in row 4
x_lab.grid(column=0, row=4)
x_label.grid(column=1, row=4)
x_Pbutton.grid(column=2, row=4, pady=2, padx=2)
x_Mbutton.grid(column=3, row=4, pady=2, padx=2)

# y axis input widgwts in row 5
y_lab.grid(column=0, row=5)
y_label.grid(column=1, row=5)
y_Pbutton.grid(column=2, row=5, pady=2, padx=2)
y_Mbutton.grid(column=3, row=5, pady=2, padx=2)

# z axis input widgwts in row 6
z_lab.grid(column=0, row=6)
z_label.grid(column=1, row=6)
z_Pbutton.grid(column=2, row=6, pady=2, padx=2)
z_Mbutton.grid(column=3, row=6, pady=2, padx=2)

# exec and nulling functions buttons in row 7
exec_button.grid(column=2, row=7, pady=20, padx=2)
null_button.grid(column=1, row=7, pady=20, padx=2)
# exit app button, row 11
exit_button.grid(column=2, row=11, pady=20, padx=2)

# output variables descriptions and values widgets in rows 8 to 10
x_res_lbl.grid(column=1, row=8)
x_res_label.grid(column=2, row=8, sticky=tkinter.NSEW)
y_res_lbl.grid(column=1, row=9)
y_res_label.grid(column=2, row=9, sticky=tkinter.NSEW)
z_res_lbl.grid(column=1, row=10)
z_res_label.grid(column=2, row=10, sticky=tkinter.NSEW)


# application main loop method
root.mainloop()
