import tkinter as tk
from tkinter import Canvas, Frame, Radiobutton
import pygame
from pygame import mixer

class Piano(Frame):
    '''This class will be used for the creation of the  keys in the program.'''
    def __init__(self):
        super().__init__()
        self.pianokeys()  #when class is created, the 'pianokeys' method is started.
             
    def pianokeys(self):
        self.master.title("Piano Application")
        self.pack(fill="both", expand=1)
        canvas = Canvas(self)
        
        def audioOFF(self = None):
            mixer.init
            pygame.mixer.music.stop()
        
        def eightyBPM(self = None):         #why does self = none work here????
            mixer.init()
            pygame.mixer.set_num_channels(20)
            mixer.music.load('NoteWavFile\80BPM.wav')
            mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            pygame.mixer.Channel(13).play(pygame.mixer.Sound('NoteWavFile\80BPM.wav'))
            
        def oneHundredBPM(self = None):
            mixer.init()
            pygame.mixer.set_num_channels(20)
            mixer.music.load('NoteWavFile\\100BPM.wav')
            mixer.music.set_volume(0.5)
            pygame.mixer.Channel(14).play(pygame.mixer.Sound('NoteWavFile\\100BPM.wav'))
            pygame.mixer.music.play(-1)
            
        def oneTwentyBPM(self = None):
            mixer.init()
            pygame.mixer.set_num_channels(20)
            mixer.music.load('NoteWavFile\\120BPM.wav')
            mixer.music.set_volume(0.5)
            pygame.mixer.Channel(15).play(pygame.mixer.Sound('NoteWavFile\\120BPM.wav'))
            pygame.mixer.music.play(-1)
            
        rad1 = Radiobutton(master=None,text= "OFF", value= '1', command= audioOFF).pack(ipady=0, 
                                ipadx= 0, anchor= "n", side= "left")
        rad2 = Radiobutton(master=None,text= "80 BPM", value= '2' ,command= eightyBPM).pack(ipady=0, 
                                ipadx= 0, anchor= "n", side= "left")
        rad3 = Radiobutton(master=None,text= "100 BPM", value= '3',command= oneHundredBPM).pack(ipady=0, 
                                ipadx= 0, anchor= "n", side= "left")
        rad4 = Radiobutton(master=None,text= "120 BPM", value= '4',command= oneTwentyBPM).pack(ipady=0, 
                                ipadx= 0, anchor= "n", side= "left")
        
        '''Sounds for the piano.'''
        def playsoundC1(self):
            mixer.init()
            pygame.mixer.set_num_channels(20)
            mixer.music.load('NoteWavFile\C.wav')
            mixer.music.set_volume(0.5)
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('NoteWavFile\C.wav'))
            
        def playsoundD(self):
            mixer.init()
            pygame.mixer.set_num_channels(20)
            mixer.music.load('NoteWavFile\D.wav')
            mixer.music.set_volume(0.5)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('NoteWavFile\D.wav'))
            
        def playsoundE(self):
            mixer.init()
            pygame.mixer.set_num_channels(20)
            mixer.music.load('NoteWavFile\E.wav')
            mixer.music.set_volume(0.5)
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('NoteWavFile\E.wav'))
            
        def playsoundF(self):
            mixer.init()
            pygame.mixer.set_num_channels(20)
            mixer.music.load('NoteWavFile\F.wav')
            mixer.music.set_volume(0.5)
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('NoteWavFile\F.wav'))
            
        def playsoundG(self):
            mixer.init()
            pygame.mixer.set_num_channels(20)
            mixer.music.load('NoteWavFile\G.wav')
            mixer.music.set_volume(0.5)
            pygame.mixer.Channel(4).play(pygame.mixer.Sound('NoteWavFile\G.wav'))
            
        def playsoundA(self):
            mixer.init()
            pygame.mixer.set_num_channels(20)
            mixer.music.load('NoteWavFile\A.wav')
            mixer.music.set_volume(0.5)
            pygame.mixer.Channel(5).play(pygame.mixer.Sound('NoteWavFile\A.wav'))
            
        def playsoundB(self):
            mixer.init()
            pygame.mixer.set_num_channels(20)
            mixer.music.load('NoteWavFile\B.wav')
            mixer.music.set_volume(0.5)
            pygame.mixer.Channel(6).play(pygame.mixer.Sound('NoteWavFile\B.wav'))
            
        def playsoundC2(self):
            mixer.init()
            pygame.mixer.set_num_channels(20)
            mixer.music.load('NoteWavFile\C2.wav')
            mixer.music.set_volume(0.5)
            pygame.mixer.Channel(7).play(pygame.mixer.Sound('NoteWavFile\C2.wav'))
        
        def playsoundCsharp(self):
            mixer.init()
            pygame.mixer.set_num_channels(20)
            mixer.music.load('NoteWavFile\C#.wav')
            mixer.music.set_volume(0.5)
            pygame.mixer.Channel(8).play(pygame.mixer.Sound('NoteWavFile\C#.wav'))
            
        def playsoundEflat(self):
            mixer.init()
            pygame.mixer.set_num_channels(20)
            mixer.music.load('NoteWavFile\Eb.wav')
            mixer.music.set_volume(0.5)
            pygame.mixer.Channel(9).play(pygame.mixer.Sound('NoteWavFile\Eb.wav'))
            
        def playsoundFsharp(self):
            mixer.init()
            pygame.mixer.set_num_channels(20)
            mixer.music.load('NoteWavFile\F#.wav')
            mixer.music.set_volume(0.5)
            pygame.mixer.Channel(10).play(pygame.mixer.Sound('NoteWavFile\F#.wav'))
            
        def playsoundAflat(self):
            mixer.init()
            pygame.mixer.set_num_channels(20)
            mixer.music.load('NoteWavFile\Ab.wav')
            mixer.music.set_volume(0.5)
            pygame.mixer.Channel(11).play(pygame.mixer.Sound('NoteWavFile\Ab.wav'))
            
        def playsoundBflat(self):
            mixer.init()
            pygame.mixer.set_num_channels(20)
            mixer.music.load('NoteWavFile\Bb.wav')
            mixer.music.set_volume(0.5)
            pygame.mixer.Channel(12).play(pygame.mixer.Sound('NoteWavFile\Bb.wav'))
  
        '''White Key Creation.'''
        c1 = canvas.create_rectangle(0, 200, 100, 500,
        outline="black", fill="#ede0df", tags="c1")
        canvas.tag_bind("c1","<Button-1>", playsoundC1)
        canvas.pack()
        
        d= canvas.create_rectangle(100, 200, 200, 500,
        outline="black", fill="#ede0df", tags="d")
        canvas.tag_bind("d","<Button-1>", playsoundD)
        canvas.pack()
   
        e = canvas.create_rectangle(200, 200, 300, 500,
        outline="black", fill="#ede0df", tags='e')
        canvas.tag_bind("e","<Button-1>", playsoundE)
        canvas.pack()

        f = canvas.create_rectangle(300, 200, 400, 500,
        outline="black", fill="#ede0df", tags='f')
        canvas.tag_bind("f","<Button-1>", playsoundF)
        canvas.pack()
        
        g = canvas.create_rectangle(400, 200, 500, 500,
        outline="black", fill="#ede0df", tags='g')
        canvas.tag_bind("g","<Button-1>", playsoundG)
        canvas.pack()
        
        a = canvas.create_rectangle(500, 200, 600, 500,
        outline="black", fill="#ede0df", tags='a')
        canvas.tag_bind("a","<Button-1>", playsoundA)
        canvas.pack()
        
        b = canvas.pack(fill="both", expand=1)
        canvas.create_rectangle(600, 200, 700, 500,
        outline="black", fill="#ede0df", tags='b')
        canvas.tag_bind("b","<Button-1>", playsoundB)
        canvas.pack()

        c2 = canvas.create_rectangle(700, 200, 800, 500,
        outline="black", fill="#ede0df", tags='c2')
        canvas.tag_bind("c2","<Button-1>", playsoundC2)
        canvas.pack()
        
        '''Black key creation.'''
        csharp = canvas.create_rectangle(75, 200, 125, 350,
        outline="black", fill="black", tags='csharp')
        canvas.tag_bind("csharp","<Button-1>", playsoundCsharp)
        canvas.pack()
        
        EFlat = canvas.create_rectangle(175, 200, 225, 350,
        outline="black", fill="black", tags='Eflat')
        canvas.tag_bind("Eflat","<Button-1>", playsoundEflat)
        canvas.pack()
         
        Fsharp = canvas.create_rectangle(375, 200, 425, 350,
        outline="black", fill="black", tags='Fsharp')
        canvas.tag_bind("Fsharp","<Button-1>", playsoundFsharp)
        canvas.pack()
        
        Aflat = canvas.create_rectangle(475, 200, 525, 350,
        outline="black", fill="black", tags='Aflat')
        canvas.tag_bind("Aflat","<Button-1>", playsoundAflat)
        canvas.pack()
        
        Bflat = canvas.create_rectangle(575, 200, 625, 350,
        outline="black", fill="black", tags='Bflat')
        canvas.tag_bind("Bflat","<Button-1>", playsoundBflat)
        canvas.pack()
        
def main():
    window = tk.Tk()
    window.geometry("810x550")
    window.attributes('-alpha',True,)
    window.resizable(False,False)
    pianoapplication = Piano()
    window.mainloop()
     
if __name__ == "__main__":
    main()