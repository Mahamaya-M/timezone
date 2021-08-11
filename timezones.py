from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz 
import time


root=Tk()
root.title("Timezone Converter")
root.geometry("700x900")

i1=Image.open("ind.png")
i1=i1.resize((200,200), Image.ANTIALIAS)
india_image=ImageTk.PhotoImage(i1)

i2=Image.open("usa.png")
i2=i2.resize((200,200), Image.ANTIALIAS)
usa_image=ImageTk.PhotoImage(i2)

i3=Image.open("phil.png")
i3=i3.resize((200,200), Image.ANTIALIAS)
philippines_image=ImageTk.PhotoImage(i3)

i4=Image.open("jap.png")
i4=i4.resize((200,200), Image.ANTIALIAS)
japan_image=ImageTk.PhotoImage(i4)

l1=Label(root, text="India: GMT 5:30+")
l1.place(relx=0.25, rely=0.02, anchor=CENTER)
l1_map=Label(root)
l1_map["image"]=india_image
l1_map.place(relx=0.25, rely=0.21, anchor=CENTER)
l1_time=Label(root)
l1_time.place(relx=0.25, rely=0.4, anchor=CENTER)

l2=Label(root, text="USA: Hawaii-Aleutian time, Alaska time, Pacific time, Mountain time, Central time and Eastern time")
l2.place(relx=0.25, rely=0.5, anchor=CENTER)
l2_map=Label(root)
l2_map["image"]=usa_image
l2_map.place(relx=0.25, rely=0.69, anchor=CENTER)
l2_time=Label(root)
l2_time.place(relx=0.25, rely=0.88, anchor=CENTER)

l3=Label(root, text="Philippines: GMT 8:00+")
l3.place(relx=0.75, rely=0.02, anchor=CENTER)
l3_map=Label(root)
l3_map["image"]=philippines_image
l3_map.place(relx=0.75, rely=0.21, anchor=CENTER)
l3_time=Label(root)
l3_time.place(relx=0.75, rely=0.4, anchor=CENTER)

l4=Label(root, text="Japan: GMT 5:30+")
l4.place(relx=0.75, rely=0.5, anchor=CENTER)
l4_map=Label(root)
l4_map["image"]=japan_image
l4_map.place(relx=0.75, rely=0.69, anchor=CENTER)
l4_time=Label(root)
l4_time.place(relx=0.75, rely=0.88, anchor=CENTER)

class India():
    def times(self):
        home=pytz.timezone('Asia/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        l1_time["text"]=current_time
        l1_time.after(200,self.times)
        
        
class USA():
    def times(self):
        home=pytz.timezone('US/Central')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        l2_time["text"]=current_time
        l2_time.after(200,self.times)
        
        
class Philippines():
    def times(self):
        home=pytz.timezone('Asia/Manila')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        l3_time["text"]=current_time
        l3_time.after(200,self.times)
        
        
class Japan():
    def times(self):
        home=pytz.timezone('Japan')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        l4_time["text"]=current_time
        l4_time.after(200,self.times)
        
        
object_l1=India()
object_l2=USA()
object_l3=Philippines()
object_l4=Japan()

l1_btn=Button(root,text="Show Time",command=object_l1.times)
l1_btn.place(relx=0.25, rely=0.44, anchor=CENTER)
                
        
l2_btn=Button(root,text="Show Time",command=object_l2.times)
l2_btn.place(relx=0.25, rely=0.92, anchor=CENTER)
                

l3_btn=Button(root,text="Show Time",command=object_l3.times)
l3_btn.place(relx=0.75, rely=0.44, anchor=CENTER)
                

l4_btn=Button(root,text="Show Time",command=object_l4.times)
l4_btn.place(relx=0.75, rely=0.92, anchor=CENTER)
        

root.mainloop()



