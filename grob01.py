#!/usr/bin/python3

'''
The utility converts dimmensional corrections from rotated coordinate system to non-rotated, basic oriented machine coordinate system.
'''

import tkinter
from tkinter import ttk
import sys

class MainWindow(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title('GROB utility')
        self.parent.rowconfigure(0, weight=91)
        self.parent.rowconfigure(1, weight=91)
        self.parent.rowconfigure(2, weight=91)
        self.parent.rowconfigure(3, weight=91)
        self.parent.rowconfigure(4, weight=91)
        self.parent.rowconfigure(5, weight=91)
        self.parent.rowconfigure(6, weight=91)
        self.parent.rowconfigure(7, weight=91)
        self.parent.rowconfigure(8, weight=91)
        self.parent.rowconfigure(9, weight=91)
        self.parent.rowconfigure(10, weight=91)
        self.parent.columnconfigure(0, weight=250)
        self.parent.columnconfigure(1, weight=250)
        self.parent.columnconfigure(2, weight=250)
        self.parent.columnconfigure(3, weight=250)
        self.parent.resizable(True, True)
        self.parent.minsize(350, 400)
        self.create_variables()
        self.create_styles()
        self.create_widgets()

    def create_variables(self):
        # tkinter interactive variables definitions
        self.csys = tkinter.StringVar() # radiobutton variable, choosen operation
        self.csys.set('op10') # set initial value

        self.x = tkinter.DoubleVar() # x axis input variable
        self.x.set(0.0) # initial value set to 0
        self.y = tkinter.DoubleVar() # y axis input variable
        self.y.set(0.0)
        self.z = tkinter.DoubleVar() # z axis input variable
        self.z.set(0.0)
        self.x_res = tkinter.DoubleVar() # output x axis variable
        self.x_res.set(0.0)
        self.y_res = tkinter.DoubleVar() # output y axis variable
        self.y_res.set(0.0)
        self.z_res = tkinter.DoubleVar() # output z axis variable
        self.z_res.set(0.0)


    def x_plus(self):
        # to increase X dimm in 0.01mm
        a = float(self.x.get())
        a += 0.01
        self.x.set(round(a, 2))

    def x_minus(self):
        # to decrease X dimm in 0.01mm
        a = float(self.x.get())
        a -= 0.01
        self.x.set(round(a, 2))

    def y_plus(self):
        # to increase Y dimm in 0.01mm
        a = float(self.y.get())
        a += 0.01
        self.y.set(round(a, 2))

    def y_minus(self):
        # to decrease Y dimm in 0.01mm
        a = float(self.y.get())
        a -= 0.01
        self.y.set(round(a, 2))

    def z_plus(self):
        # to increase Z dimm in 0.01mm
        a = float(self.z.get())
        a += 0.01
        self.z.set(round(a, 2))

    def z_minus(self):
        # to decrease Z dimm in 0.01mm
        a = float(self.z.get())
        a -= 0.01
        self.z.set(round(a, 2))

    def convert(self):
        #converts dimms from one coordinate system to other
        # get values from input variables
        a = float(self.x.get())
        b = float(self.y.get())
        c = float(self.z.get())

        # if operation 10 is choosen
        if self.csys.get() == 'op10':
            X = -0.707*c +0.707*b
            Y = 0.707*c +0.707*b
            Z = a
        else: # or if operation 20 is choosen
            X = 0.707*c -0.707*b
            Y = 0.707*c +0.707*b
            Z = -1*a

        # set result values into variables
        self.x_res.set(round(X, 3)) 
        self.y_res.set(round(Y, 3))
        self.z_res.set(round(Z, 3))


    def nulling(self):
        # sets input variables to zero
        self.x.set(0.0)
        self.y.set(0.0)
        self.z.set(0.0)

    def create_styles(self):
        # ttk styles definitions
        self.style=ttk.Style()
        self.style.configure('EXE.TButton', foreground='green')
        self.style.configure('EXIT.TButton', foreground='red')
        self.style.configure('RES.TLabel', background='white', font=('bold'))

    def create_widgets(self):
        # widget definitions

        # rdiobuttons to choose from two operations
        self.radio10 = ttk.Radiobutton(root, variable=self.csys, value='op10', text='Operace 10: G54, G56')
        self.radio20 = ttk.Radiobutton(root, variable=self.csys, value='op20', text='Operace 20: G55, G57')

        # empty label to add row space
        self.empty_label = ttk.Label(root, text='     ')

        self.x_lab = ttk.Label(text=' X: ') # label axis description
        self.x_label = ttk.Label(root, textvariable=self.x) # label shows input variable value x
        self.x_Pbutton = ttk.Button(root, text='+0.01', command=self.x_plus) # button to increase value
        self.x_Mbutton = ttk.Button(root, text='-0.01', command=self.x_minus) # button to decrease value

        self.y_lab = ttk.Label(text=' Y: ')
        self.y_label = ttk.Label(root, textvariable=self.y) # label shows input variable value y
        self.y_Pbutton = ttk.Button(root, text='+0.01', command=self.y_plus)
        self.y_Mbutton = ttk.Button(root, text='-0.01', command=self.y_minus)

        self.z_lab = ttk.Label(text=' Z: ')
        self.z_label = ttk.Label(root, textvariable=self.z) # label shows input variable value z
        self.z_Pbutton = ttk.Button(root, text='+0.01', command=self.z_plus)
        self.z_Mbutton = ttk.Button(root, text='-0.01', command=self.z_minus)

        self.x_res_lbl = ttk.Label(root, text='Result X:') # label output value description
        self.x_res_label = ttk.Label(root, textvariable=self.x_res, style='RES.TLabel') # label output value x axis
        self.y_res_lbl = ttk.Label(root, text='Result Y:')
        self.y_res_label = ttk.Label(root, textvariable=self.y_res, style='RES.TLabel') # label output value y axis
        self.z_res_lbl = ttk.Label(root, text='Result Z:')
        self.z_res_label = ttk.Label(root, textvariable=self.z_res, style='RES.TLabel') # label output value z axis


        self.exec_button = ttk.Button(text='EXECUTE', style='EXE.TButton', command=self.convert) # convert function button 
        self.null_button = ttk.Button(text='NULL', command=self.nulling) # nulling function button
        self.exit_button=ttk.Button(text='EXIT', style='EXIT.TButton', command=lambda: sys.exit(0)) # exit app button

        # geometry definition, grid packing manager

        # radiobuttons in the first two rows
        self.radio10.grid(column=1, row=0, columnspan=2, sticky=tkinter.NSEW, pady=7)
        self.radio20.grid(column=1, row=1, columnspan=2, sticky=tkinter.NSEW, pady=7)

        self.empty_label.grid(column=0, row=2) # empty label to add empty space in row 3

        # x axis input widgwts in row 4
        self.x_lab.grid(column=0, row=3)
        self.x_label.grid(column=1, row=3)
        self.x_Pbutton.grid(column=2, row=3, pady=2, padx=2)
        self.x_Mbutton.grid(column=3, row=3, pady=2, padx=2)

        # y axis input widgwts in row 5
        self.y_lab.grid(column=0, row=4)
        self.y_label.grid(column=1, row=4)
        self.y_Pbutton.grid(column=2, row=4, pady=2, padx=2)
        self.y_Mbutton.grid(column=3, row=4, pady=2, padx=2)

        # z axis input widgwts in row 6
        self.z_lab.grid(column=0, row=5)
        self.z_label.grid(column=1, row=5)
        self.z_Pbutton.grid(column=2, row=5, pady=2, padx=2)
        self.z_Mbutton.grid(column=3, row=5, pady=2, padx=2)

        # exec and nulling functions buttons in row 7
        self.exec_button.grid(column=2, row=6, pady=20, padx=2)
        self.null_button.grid(column=1, row=6, pady=20, padx=2)
        # exit app button, row 11
        self.exit_button.grid(column=2, row=10, pady=20, padx=2)

        # output variables descriptions and values widgets in rows 8 to 10
        self.x_res_lbl.grid(column=1, row=7)
        self.x_res_label.grid(column=2, row=7, sticky=tkinter.NSEW)
        self.y_res_lbl.grid(column=1, row=8)
        self.y_res_label.grid(column=2, row=8, sticky=tkinter.NSEW)
        self.z_res_lbl.grid(column=1, row=9)
        self.z_res_label.grid(column=2, row=9, sticky=tkinter.NSEW)

# main container 
root = tkinter.Tk()
app = MainWindow(root)
app.mainloop()





