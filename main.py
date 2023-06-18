from tkinter import *

color_win_bg='black'
color_btn_bg='#C0DBE8'
color_light_text='#476D80'
color_btn_active='#8A2BE2'

class Fr(Frame):
    def __init__(self,*arg, **kwarg):
        super().__init__(bg=color_win_bg,*arg, **kwarg)
class Sc(Scale):
    def __init__(self,*arg, **kwarg):
        super().__init__(orient=HORIZONTAL,width=10,length=250,bg=color_win_bg,fg=color_light_text,
                         highlightbackground=color_win_bg,font=('Courier New',13),*arg, **kwarg)
class Butt(Button):
    def __init__(self,*arg, **kwarg):
        super().__init__(bg=color_btn_bg,fg=color_light_text,activebackground=color_btn_active,
                         borderwidth=5,relief='ridge',font=('Courier New',12),*arg, **kwarg)
class Lbl (Label):
    def __init__(self, *arg, **kwarg):
        super().__init__(bg=color_win_bg,fg=color_light_text,font=('Courier New',13),pady=5,*arg, **kwarg)

root=Tk()
root.configure(bg=color_btn_bg)
root.resizable(False,False)
root.title('CITY PLUS')
root.iconphoto(True,PhotoImage(file='logo.png'))
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')

option=Fr(height=f'{root.winfo_screenheight()-20}')
option.grid(row=0,column=0)

btnlist=['главная страница','Загрязнение воздуха','Криминогенная обстановка','Стоимость земли',
         'Озеленение районов','Школы и сады','Больницы']
#commandlist=['startmap.png','map1.png','map2.png','map3.png','map4.png','map5.png','map6.png']
for i in range (7):
    def func(i):
        for widget in mainmap.winfo_children():
            widget.destroy()
        if i==0:
            img=PhotoImage(file="startmap.png")
        else:
            img=PhotoImage(file="map1.png")
        mapbtn=Butt(mainmap,width=f'{root.winfo_screenwidth()}',height=f'{root.winfo_screenheight()-20}',image=img)
        mapbtn.grid()
    btn=Butt(option,height=5,command=lambda: func(i),text=btnlist[i])
    #img = PhotoImage(file="logo.png")
    #btn.config(image=img)
    btn.grid(sticky='we')
    btnlist.append(btn)


img=PhotoImage(file="startmap.png")
mainmap=Fr()
mapbtn=Butt(mainmap,width=f'{root.winfo_screenwidth()}',height=f'{root.winfo_screenheight()-20}',image=img)
mapbtn.grid()
#self.Photo=pixil_none
#super().__init__(master=gamewindow,width=20, height=20,image=self.Photo)
mainmap.grid(row=0,column=1)


root.mainloop()