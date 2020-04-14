from tkinter import *
from Process import process
from Fcfs import fcfs
from Round import roound
from SJF import Sjf
from Priority import  priority
import os
import sys
from Element import element
root=Tk()
root.title("cpu scheduler")
ii=0
def stage1(event):
    list_of_process=[]
    def reset(event):
        root.destroy()
        os.system('python "modified_gui.py"')


    def draw(List_of_elemnts,wt):
        gantt = Frame(main_frame,width=1300)
        gantt.pack()
        wait="avg waiting time is  :  " +str(wt)

        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=1300, height=200)

        canvas = Canvas(gantt)
        frame = Frame(canvas)
        myscrollbar = Scrollbar(gantt, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=myscrollbar.set)
        canvas.create_window((0, 0), window=frame, anchor='nw')
        frame.bind("<Configure>", myfunction)

        myscrollbar.pack(side="bottom", fill="x")
        canvas.pack(side="bottom")
        x = 0
        for i in List_of_elemnts:
            s = i.p.name+" ( "+str(i.start)+" : " +str(i.end)+" )"
            e = Label(frame, text=s, borderwidth=2, relief="solid", width=13 + int(i.end - i.start), height=5)
            e.grid(row=0, column=int(x))
            if x == int(x + (i.end - i.start)):
                x = x + 1
            else:
                x = x + (i.end - i.start)
        lb =Label(gantt,text=wait)
        lb.pack()
    def claculate(event):
        if s == "fcfs":
            f1 = fcfs()
            f1.list_process = list_of_process
            f1.real()
            f1.calc()
            wt=f1.waiting_time()
            f1.empty()
            draw(f1.list_element,wt)


        elif s == "sjf":
            pre=int(pree_entry.get())
            pree_entry.delete(0, END)
            f1 = Sjf()
            f1.preemptive=pre
            f1.list_process = list_of_process
            f1.real()
            f1.calc()
            wt=f1.waiting_time()
            f1.empty()
            draw(f1.list_element,wt)


        elif s == "priority":
            pre = int(pree_entry.get())
            pree_entry.delete(0, END)
            f1 = priority()
            f1.preemptive = pre
            f1.list_process = list_of_process
            f1.real()
            f1.calc()
            wt=f1.waiting_time()
            f1.empty()
            draw(f1.list_element,wt)

        elif s == "rr":
            q = int(q_entry.get())
            q_entry.delete(0, END)
            f1 = roound()
            f1.list_process = list_of_process
            f1.quantum=q
            f1.real()
            f1.calc()
            wt=f1.waiting_time()
            f1.empty()
            draw(f1.list_element,wt)

    def show(ii):
        def get_info(event):
            global ii
            P = process()
            P.name = "p" + str(ii + 1)
            P.burst_time = float(bt_entry.get())
            P.arrival_time = float(at_entry.get())
            at_entry.delete(0, END)
            bt_entry.delete(0, END)
            if s == "priority":
                P.pr=int(pr_entry.get())
                pr_entry.delete(0,END)
            list_of_process.append(P)
            down_frame.pack_forget()
            down_frame.destroy()
            ii=ii+1
            if ii<n :show(ii)
        st = "process " + str(ii + 1)
        down_frame = Frame(main_frame)
        down_frame.pack(side=BOTTOM)
        l = Label(down_frame, text=st)
        l.grid(row=0)
        at_label = Label(down_frame, text="arrival time")
        at_label.grid(row=1)
        bt_Label = Label(down_frame, text="brust time ")
        bt_Label.grid(row=2)
        at_entry = Entry(down_frame)
        at_entry.grid(row=1, column=1)
        bt_entry = Entry(down_frame)
        bt_entry.grid(row=2, column=1)
        if s == "priority":
            pr_Label = Label(down_frame, text="priority")
            pr_Label.grid(row=3)
            pr_entry = Entry(down_frame)
            pr_entry.grid(row=3, column=1)
        b1 = Button(down_frame, text="OK")
        b1.bind("<Button-1>",get_info )
        b1.grid(row=4, column=1)
    s=type_entry.get()
    n=int(n_entry.get())
    type_entry.delete(0,END)
    n_entry.delete(0,END)
    main_frame = Frame(root)
    main_frame.pack(side=BOTTOM)
    ii=0
    show(ii)
    if s == "sjf" or  s=="priority" :
        down_frame = Frame(main_frame)
        down_frame.pack(side=BOTTOM)
        pree__Label = Label(down_frame, text="preemptive")
        pree__Label.grid(row=0,column=0)
        pree_entry = Entry(down_frame)
        pree_entry.grid(row=0, column=1)
    if s == "rr":
        down_frame = Frame(main_frame)
        down_frame.pack(side=BOTTOM)
        q__Label = Label(down_frame, text="Quantum")
        q__Label.grid(row=0,column=0)
        q_entry = Entry(down_frame)
        q_entry.grid(row=0, column=1)
    result_button=Button(main_frame, text="result")
    result_button.pack()
    result_button.bind("<Button-1>", claculate)
    reset_button.bind("<Button-1>", reset)
top_frame=Frame(root)
top_frame.pack()
n_label=Label(top_frame,text="no of process")
n_label.grid(row=0)
type_Label=Label(top_frame,text="type of scheduler(fcfs,sjf,priority,rr) ")
type_Label.grid(row=2)
n_entry=Entry(top_frame)
type_entry=Entry(top_frame)
n_entry.grid(row=0,column=1)
type_entry.grid(row=2,column=1)
b1=Button(top_frame,text="OK")
b1.bind("<Button-1>",stage1)
b1.grid(column=2,row=1)
reset_button = Button(top_frame, text="reset")
reset_button.grid(row=1,column=3)
root.mainloop()