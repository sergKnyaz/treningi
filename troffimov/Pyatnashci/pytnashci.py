from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import randint
from winsound import Beep

def startNewRound():
    '''вызывается при нажатий кнопки СТАРТ,
    делает кнопки неактивными,находит координаты пустого спрайта,
    вызывает методы перемешивания изображений,обновления текстовых меток в окне'''
    pass

def sufflePictures(x,y):
    '''Перемешивает спрайты,
    x и y координаты пустого спрайта'''

def exchangeImage(x1,y1,x2,y2):
    '''Меняет спрайты местами по координатам'''

def resetPictuhts():
    '''сбрасывает порядок изображений в стандартный,
    при котором игровое поле "собрано" правильным образом.
    Метод вызываетсяпри нажатии кнопки СБРОС'''

def updatePictures():
    '''Обновляет все изображения на основе матиматической
    модели из двумерного списка'''

def saveRecords():
    '''Сохраняет в фал рекорды пользователя для 
    каждого уровня сложности.
    Если файл отсутствует, то метод создает его'''

def getRecordStep():
    '''Загружает из файла рекорды пользователя
    для каждого уровня сложности.
    Если файл отсутствует, то метод создает его'''

def refreshText():
    '''обновляет поля Label:
    рекорд и текущее кол-во сделанных ходов'''

def go(x,y):
    '''Внешний методю Определяет,что делать,
    когдапользователь нажимает на спрайт по
    координатам X,Y. Проверяет: если справа, 
    слева, сверху или снизу находится пустая 
    клетка,то меняет текущий спрайт с пустым
    местами. Увеличивает кол-во сделанных ходов.
    Проверяет собран ли пазл целиком'''

def seeStart(event):
    '''Вызывается, когда нажата кнопка "Посмотреть,как 
    должно быть". Запоминает текущее расположение игрового
    поля,показывает, как должен выглядеть пазл в финале
    '''

def seeEnd(event):
    '''Вызывается, когда кнопка"Посмотреть,как должно
    быть", отпущена. Возвращает расположение элементов
    на игровом поле в то состояние, при котором была
    нажата кнопка "Посмотреть,как должно быть"'''

def isCheckImage():
    '''Выбор скина. делает активным набор
    спрайтов "Космос" или "Природа"
    '''

def music():
    '''Вызывается при выигрыше мелодия победы'''

root=Tk()
root.resizable(False,False)
root.title('Пятнашки')
root.iconbitmap('C:/Users/MR_GREEN_PC/Desktop/trenning/treningi/troffimov/Pyatnashci/icon/icon.ico')

back='#373737'
fore='#AFAFAF'
WIDGH=422
HEIGHT=730
POS_X=root.winfo_screenwidth()//2-WIDGH//2
POS_Y=root.winfo_screenheight()//2-HEIGHT//2
root.geometry(f'{WIDGH}x{HEIGHT}+{POS_X}+{POS_Y}')

root['bg']=back

# Кнопка "Посмотреть собранное"
seeButton=Button(root,text='Посмотреть как должно быть',width=56)
seeButton.place(x=10,y=620)
seeButton.bind('<Button-1>',seeStart)
seeButton.bind('<ButtonRelease>',seeEnd)

# Кнопка "Старт"
startButton=Button(root,text='START',width=56)
startButton.place(x=10,y=650)
startButton['command']=startNewRound

# Сброс
resetButton=Button(root,text='Сброс',width=56)
resetButton.place(x=10,y=680)
resetButton['command']=resetPictuhts

# Метка кол-во сделаных ходов и рекордом текущего уровня
textSteps=Label(root,bg=back,fg=fore)
textSteps.place(x=10,y=550)
textRecord=Label(root,bg=back,fg=fore)
textRecord.place(x=10,y=570)

# Метка сложности
Label(root,bg=back,fg=fore,text='Сложность: ').place(x=267,y=550)

itemDiff=['Новичек','В теме','Бывалый','Профи','Асс','Супер асс']
diffCombobox=ttk.Combobox(root,width=18,values=itemDiff,state='readonly')
diffCombobox.place(x=270,y=570)
diffCombobox.bind('<<ComboboxSelected>>',lambda e: refreshText())
diffCombobox.current(0)

# Радио переключатели
image=BooleanVar()
image.set(True)
radio1=Radiobutton(root,text='Космос',variable=image,value=True,activebackground=back,bg=back,fg=fore)
radio2=Radiobutton(root,text='Природа',variable=image,value=False,activebackground=back,bg=back,fg=fore)
radio1['command']=isCheckImage
radio2['command']=isCheckImage
radio1.place(x=150,y=548)
radio2.place(x=150,y=568)

# ИЗОБРАЖЕНИЯ===============================
n=4
m=4
pictureWidth=500
pictureHeight=500
fileName=['img01.png','img02.png','img03.png','img04.png','img05.png','img06.png','img07.png','img08.png',
'img09.png','img10.png','img11.png','img12.png','img13.png','img14.png','img15.png','img16.png','black.png']
imageBackground=[]
imageBackground1=[]
imageBackground2=[]

for name in fileName:
    imageBackground1.append(PhotoImage(file='image01/'+name))
    imageBackground2.append(PhotoImage(file='image02/'+name))
# пустой спраит
blackImg=16
imageBackground=imageBackground1

# метки Label
labelImage=[]
# математическая модель игрового поля
dataImage=[]
copyData=[]

root.mainloop()