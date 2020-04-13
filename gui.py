from tkinter import *
from Process import process
from Fcfs import fcfs
from copy import deepcopy
from Element import element
List_of_elemnts=[]
List_of_process=[]
root=Tk()
root.title("os cpu scheduler")

def draw():
    gantt=Frame()
    gantt.pack(side =RIGHT)
    x=0
    for i in List_of_elemnts:
        e=Label(gantt,text=i.p.name ,borderwidth=2, relief="solid",width=1+(i.end-i.start),height=5)
        e.grid(row=0,column=x)
        x=x+(i.end-i.start)

def get_info_fcfs(i,p) :
    def get_info(event):
        P=process()
        P.name="p"+str(i+1)
        P.burst_time=int(bt_entry.get())
        P.arrival_time=int(at_entry.get())
        at_entry.delete(0,END)
        bt_entry.delete(0,END)
        p.append(P)

    down_frame=Frame(root)
    down_frame.pack(side=BOTTOM)
    s="process "+str(i+1)
    l=Label(down_frame,text=s)
    l.grid(row=0 )
    at_label = Label(down_frame, text="arrival time")
    at_label.grid(row=1)
    bt_Label = Label(down_frame, text="brust time ")
    bt_Label.grid(row=2)
    at_entry = Entry(down_frame)
    bt_entry = Entry(down_frame)
    at_entry.grid(row=1, column=1)
    bt_entry.grid(row=2, column=1)
    b1 = Button(down_frame, text="OK")
    b1.bind("<Button-1>",get_info )
    b1.grid(row=3,column=1)



def FCFS(n) :
    def cont(event):
        global List_of_elemnts
        f1 = fcfs()
        f1.list_process = List_of_process
        f1.calc()
        draw()
        f1.out()
        List_of_elemnts = deepcopy(f1.list_element)
    for i in range(n):
        get_info_fcfs(i,List_of_process)

    left_frame = Frame(root)
    left_frame.pack(side=LEFT)
    b=Button(left_frame, text="result")
    b.bind("<Button-1>", cont)
    b.pack()


def sjf(n): pass

def priority(n): pass

def rr(n) : pass

def stage1(event):
    s=type_entry.get()
    n=int(n_entry.get())
    type_entry.delete(0,END)
    n_entry.delete(0,END)
    if s=="fcfs": FCFS(n)
    elif s=="sjf" : sjf(n)
    elif s=="priority" : priority(n)
    elif s=="rr" : rr(n)

top_frame=Frame(root)
top_frame.pack()
n_label=Label(top_frame,text="no of process")
n_label.grid(row=0)
type_Label=Label(top_frame,text="type of scheduler ")
type_Label.grid(row=1)
n_entry=Entry(top_frame)
type_entry=Entry(top_frame)
n_entry.grid(row=0,column=1)
type_entry.grid(row=1,column=1)
b1=Button(top_frame,text="OK")
b1.bind("<Button-1>",stage1)
b1.grid(column=2)
root.mainloop()