from Tkinter import *
class Calc:
    def __init__(self,button):
        self.button=button
    def donothing(self):
        if self.button==calc['bt1']:
            for i in range(0,len(calc['bt1'])):
                if(i==len(calc['bt1'])-1):
                    calc['temp']+=calc['bt1']
            var.set(calc['temp'])
        elif self.button==calc['bt2']:
            for i in range(0,len(calc['bt2'])):
                if(i==len(calc['bt2'])-1):
                    calc['temp']+=calc['bt2']
            var.set(calc['temp'])
        elif self.button==calc['bt3']:
            for i in range(0,len(calc['bt3'])):
                if(i==len(calc['bt2'])-1):
                    calc['temp']+=calc['bt3']
            var.set(calc['temp'])
        elif self.button==calc['bt6']:
            for i in range(0,len(calc['bt2'])):
                if(i==len(calc['bt2'])-1):
                    calc['temp']+=calc['bt6']
            var.set(calc['temp'])
        elif self.button==calc['bt7']:
            for i in range(0,len(calc['bt2'])):
                if(i==len(calc['bt2'])-1):
                    calc['temp']+=calc['bt7']
            var.set(calc['temp'])
        elif self.button==calc['bt8']:
            for i in range(0,len(calc['bt2'])):
                if(i==len(calc['bt2'])-1):
                    calc['temp']+=calc['bt8']
            var.set(calc['temp'])
        elif self.button==calc['bt11']:
            for i in range(0,len(calc['bt2'])):
                if(i==len(calc['bt2'])-1):
                    calc['temp']+=calc['bt11']
            var.set(calc['temp'])
        elif self.button==calc['bt12']:
            for i in range(0,len(calc['bt2'])):
                if(i==len(calc['bt2'])-1):
                    calc['temp']+=calc['bt12']
            var.set(calc['temp'])
        elif self.button==calc['bt13']:
            for i in range(0,len(calc['bt13'])):
                if(i==len(calc['bt2'])-1):
                    calc['temp']+=calc['bt13']
            var.set(calc['temp'])
        elif self.button==calc['bt15']:
            for i in range(0,len(calc['bt2'])):
                if(i==len(calc['bt2'])-1):
                    calc['temp']+=calc['bt15']
            var.set(calc['temp'])
        elif self.button==calc['bt17']:
            for i in range(0,len(calc['bt2'])):
                if(i==len(calc['bt2'])-1):
                    calc['temp']+=calc['bt17']
            var.set(calc['temp'])
        elif self.button==calc['bt18']:
            add=[]
            ans=0
            temp=''
            op=''
            str1=calc['temp']
            for i in range(0,len(str1)):
                if(str1[i]=='.'):
                    temp='float'
                    break
                else:
                    temp="int"
            for i in range(0,len(str1)):
                if(str1[i]=='+'):
                    op='+'
                    break
                elif(str1[i]=='-'):
                    op='-'
                elif(str1[i]=='/'):
                    op='/'
                    break
                elif(str1[i]=='*'):
                    op='*'
                    break
                elif(str1[i]=='%'):
                    op='%'
                    break
            if(op=='/'):
                add=calc['temp'].split('/')
                add[0]=int(add[0])
                ans=add[0]
                for i in range(1,len(add)):
                    add[i]=float(add[i])
                    ans/=add[i]
            elif(op=='%'):
                add=calc['temp'].split('%')
                add[0]=int(add[0])
                ans=add[0]
                for i in range(1,len(add)):
                    add[i]=float(add[i])
                    ans*=add[i]
                ans=ans/100
            elif(op=='+'):
                add=calc['temp'].split('+')
                if(temp=='float'):
                    for i in range(0,len(add)):
                        add[i]=float(add[i])
                        ans+=add[i]
                elif(temp=="int"):
                    for i in range(0,len(add)):
                        add[i]=int(add[i])
                        ans+=add[i]
            elif(op=='*'):
                add=calc['temp'].split('*')  #for multiply#
                ans=1
                if(temp=='int'):
                    for i in range(0,len(add)):
                        add[i]=int(add[i])
                        ans*=add[i]
                elif(temp=='float'):
                    for i in range(0,len(add)):
                        add[i]=float(add[i])
                        ans*=add[i]
 
            elif(op=='-'):#neg errroooooorrrrr#
                add=calc['temp'].split('-')
                add[0]=int(add[0])
                ans=add[0]
                for i in range(1,len(add)):
                    add[i]=int(add[i])
                    ans-=add[i]

            calc['temp']=str(ans)
            var.set(ans)
            
            
        elif self.button==calc['bt9']:
            for i in range(0,len(calc['bt2'])):
                if(i==len(calc['bt2'])-1):
                    calc['temp']+=calc['bt9']
            var.set(calc['temp'])
        elif self.button==calc['bt4']:
            for i in range(0,len(calc['bt2'])):
                if(i==len(calc['bt2'])-1):
                    calc['temp']+=calc['bt4']
            var.set(calc['temp'])
        elif self.button==calc['bt5']:
            for i in range(0,len(calc['bt2'])):
                if(i==len(calc['bt2'])-1):
                    calc['temp']+=calc['bt5']
            var.set(calc['temp'])
        elif self.button==calc['bt16']:
            for i in range(0,len(calc['bt2'])):
                if(i==len(calc['bt2'])-1):
                    calc['temp']+=calc['bt16']
            var.set(calc['temp'])
        elif self.button==calc['bt14']:
            calc['temp']+=calc['bt14']
            var.set(calc['temp'])
        elif self.button=="clean":
            calc['temp']="0"
            var.set(calc['temp'])

def donothing():
        filewin=Toplevel(mainframe)
        buttonx=Button(filewin,text="do nothing button").pack()
root=Tk()
root.title("Calculator")
calc={'bt1':'7','bt2':'8','bt3':'9','bt4':'/','bt5':'%',
      'bt6':'4','bt7':'5','bt8':'6','bt9':'*','bt10':'1/x',
      'bt11':'1','bt12':'2','bt13':'3','bt14':'-',
      'bt15':'0','bt16':'.','bt17':'+','bt18':'=','temp':""}
var=StringVar()
var.set("0")
objclean=Calc("clean")
objeql=Calc(calc['bt18'])
objper=Calc(calc['bt5'])
objdiv=Calc(calc['bt4'])
objmul=Calc(calc['bt9'])
objsub=Calc(calc['bt14'])
objadd=Calc(calc['bt17'])
objdot=Calc(calc['bt16'])
obj9=Calc(calc['bt3'])
obj8=Calc(calc['bt2'])
obj7=Calc(calc['bt1'])
obj6=Calc(calc['bt8'])
obj5=Calc(calc['bt7'])
obj4=Calc(calc['bt6'])
obj3=Calc(calc['bt13'])
obj2=Calc(calc['bt12'])
obj1=Calc(calc['bt11'])
obj0=Calc(calc['bt15'])
root.minsize(width=210,height=265)
root.maxsize(width=210,height=265)
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=1)
filemenu.add_command(label="New",command=donothing)
filemenu.add_command(label="Open",command=donothing)
filemenu.add_command(label="save",command=donothing)
filemenu.add_command(label="save as..",command=donothing)
filemenu.add_command(label="Close",command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)
editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="Undo",command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut",command=donothing)
editmenu.add_command(label="Copy",command=donothing)
editmenu.add_command(label="Paste",command=donothing)
editmenu.add_command(label="Delete",command=donothing)
editmenu.add_command(label="Select All",command=donothing)
menubar.add_cascade(label="Edit",menu=editmenu)
root.config(menu=menubar)
label=Label(root,textvariable=var,relief=RAISED,height="2",width="22",anchor=E,font="Times").pack()
mainframe=Frame(root,pady=2)
frame=Frame(mainframe,pady=2)
button1=Button(frame,text="7",fg="red",height="2",width="3",font="18",
                 activebackground="grey",background="#87D2F2",command=obj7.donothing).pack(side=LEFT,padx=2)
button2=Button(frame,text="8",fg="red",height="2",width="3",font="18",
                 activebackground="grey",background="#87D2F2",command=obj8.donothing).pack(side=LEFT,padx=2)
button3=Button(frame,text="9",fg="red",height="2",width="3",font="18",
                 activebackground="grey",background="#87D2F2",command=obj9.donothing).pack(side=LEFT,padx=2)
button4=Button(frame,text="/",fg="red",height="2",width="3",font="18",
                 activebackground="grey",background="#87D2F2",command=objdiv.donothing).pack(side=LEFT,padx=2)
button5=Button(frame,text="%",fg="red",height="2",width="3",font="18",
                 activebackground="grey",background="#87D2F2",command=objper.donothing).pack(side=LEFT,padx=2)
frame.pack()
frame=Frame(mainframe,pady=2)
button6=Button(frame,text="4",fg="red",height="2",width="3",font="18",
                   activebackground="grey",background="#87D2F2",command=obj4.donothing).pack(side=LEFT,padx=2)
button7=Button(frame,text="5",fg="red",height="2",width="3",font="18",
                   activebackground="grey",background="#87D2F2",command=obj5.donothing).pack(side=LEFT,padx=2)
button8=Button(frame,text="6",fg="red",height="2",width="3",font="18",
                   activebackground="grey",background="#87D2F2",command=obj6.donothing).pack(side=LEFT,padx=2)
button9=Button(frame,text="*",fg="red",height="2",width="3",font="18",
                   activebackground="grey",background="#87D2F2",command=objmul.donothing).pack(side=LEFT,padx=2)
button10=Button(frame,text="1/x",fg="red",height="2",width="3",font="18",
                   activebackground="grey",background="#87D2F2").pack(side=LEFT,padx=2)
frame.pack()
frame=Frame(mainframe,pady=2)
button11=Button(frame,text="1",fg="red",height="2",width="3",font="18",
                   activebackground="grey",background="#87D2F2",command=obj1.donothing).pack(side=LEFT,padx=2)
button12=Button(frame,text="2",fg="red",height="2",width="3",font="18",
                   activebackground="grey",background="#87D2F2",command=obj2.donothing).pack(side=LEFT,padx=2)
button13=Button(frame,text="3",fg="red",height="2",width="3",font="18",
                   activebackground="grey",background="#87D2F2",command=obj3.donothing).pack(side=LEFT,padx=2)
button14=Button(frame,text="-",fg="red",height="2",width="3",font="18",
                   activebackground="grey",background="#87D2F2",command=objsub.donothing).pack(side=LEFT,padx=2)
button19=Button(frame,text="Clear",fg="red",height="2",width="3",font="12",
                   activebackground="grey",background="#87D2F2",command=objclean.donothing).pack(side=LEFT,padx=2)

frame.pack()
frame=Frame(mainframe,pady=2)
button15=Button(frame,text="0",fg="red",height="2",width="8",font="18",command=obj0.donothing).pack(side=LEFT,padx=2)
button16=Button(frame,text=".",fg="red",height="2",width="3",font="18",command=objdot.donothing).pack(side=LEFT,padx=2)
button17=Button(frame,text="+",fg="red",height="2",width="3",font="18",command=objadd.donothing).pack(side=LEFT,padx=2)
button18=Button(frame,text="=",fg="red",height="2",width="3",font="18",
                   activebackground="grey",background="#87D2F2",command=objeql.donothing).pack(side=BOTTOM,padx=2)
frame.pack(side=LEFT)
mainframe.pack()
root.mainloop()

