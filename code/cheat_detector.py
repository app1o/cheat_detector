import psutil
import time
import os
import sys
import tkinter
import customtkinter as tk

tk.set_appearance_mode("system")
app = tk.CTk()
app.title("cheat_detector🧑‍💻")
app.geometry("300x200")
tittle = tk.CTkLabel(master=app,text= "Cheat Detector💻",font = tk.CTkFont(size=20 , weight="bold"))
tittle.pack(pady=(30,20))
log_bx = tk.CTkTextbox(master=app,width=200,height=70,corner_radius=10,bg_color="transparent",activate_scrollbars=True,state="disable")
log_bx.pack(padx=10,pady=10,side=tkinter.BOTTOM)
pid=[]
def log(message:str):
    log_bx.configure(state="normal")
    log_bx.insert("end",message+"\n")
    log_bx.yview_moveto(1.0)
    log_bx.configure(state="disable")
switch = False
def check_once():
    if not switch:
        log("Stoped")
        return
    apps=[]
    pid.clear()
    c=0
    log_bx.configure(state="normal")
    log_bx.delete("1.0","end")
    log_bx.configure(state="disable")
    for poc in psutil.process_iter(['pid','name']):
        try:
            if poc.info['name'] in black:
                #psutil.Process(poc.info['pid']).terminate()
                pid.append(poc.info['pid'])
                if poc.info['name'] not in apps:
                    c=1
                    apps.append(str(poc.info['name']))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    if c==0:
        log("No cheating app found.\n")
    else:
        log("Running apps are:")
        log("\n ".join(apps))
    app.after(1000,check_once)
def start():
    global switch
    if not switch: 
        switch = True
    if getattr(sys, 'frozen', False):
        cheat_path = os.path.join(os.path.dirname(sys.executable), "cheat.csv")
    else:
        cheat_path = os.path.join(os.path.dirname(__file__), "cheat.csv")

    #print("Looking for cheat.csv at:", cheat_path) 

    if not os.path.exists(cheat_path):
        log("ERROR: cheat.csv not found!")
        return
    global black
    black = open(cheat_path).read().splitlines()
    print("looking...")
    check_once()
        
def stop():
    global switch 
    switch = False
def ter():
    for i in pid:
        psutil.Process(i).terminate()
    log("Terminated")
start_btn = tk.CTkButton(master=app,text= "Start",width=120,command=start)
start_btn.pack(pady=5)
stop_btn = tk.CTkButton(master=app,text= "Stop",width=120,command=stop)
stop_btn.pack(pady=5)
ter_btn = tk.CTkButton(master=app,text= "Terminate",width=120,command=ter)
ter_btn.pack(pady=5)
app.mainloop()

