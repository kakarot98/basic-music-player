from tkinter import*
from pygame.mixer import*
from tkinter import filedialog
from tkinter import messagebox

root=Tk()
root.geometry("400x100+400+200")
root.title("Music player")
root.configure(background='black')
fn=""
pos=0

def play():
	if fn is not"":
		init()
		music.load(fn)
		music.play(1,start=pos/1000)
	else:
		messagebox.showerror("error",'select file to open')

def stop():
	music.stop()
	global pos
	pos=0
	
def pause():
	global pos
	pos=pos+music.get_pos()
	music.pause()

def open():
	global fn
	fn=filedialog.askopenfilename(title='select music file',filetypes=(('music files','*.mp3'),('all files','*.*')))

btnPlay=Button(root,text="play",command=play)
btnStop=Button(root,text="stop",command=stop)
btnPause=Button(root,text="pause",command=pause)
btnOpen=Button(root,text="open",command=open)

btnPlay.pack(side=LEFT,padx=20)

btnStop.pack(side=LEFT,padx=20)

btnPause.pack(side=LEFT,padx=20)

btnOpen.pack(side=LEFT,padx=20)
root.mainloop()