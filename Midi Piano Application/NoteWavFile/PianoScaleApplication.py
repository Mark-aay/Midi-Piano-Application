''' I want to build a small scale application for users.
    I want the user to have access to a single scale on a piano, 
    and I want it to be wrapped in the tkniter module.
    When the user event clicks on a specific key within the program,
    the corresponding note will play on the event. 
    
    There may be a sustain button that makes all the sounds sustain with 
    reverb, and there may be a dry button that makes the sound play only
    once. '''
import tkinter as tk
from tkinter import Canvas, Frame
from pygame import mixer
    
class Piano(Frame):
    '''This class will be used for the creation of the  keys in the program.'''
    def __init__(self):
        super().__init__()
        self.pianokeys()
       
    def pianokeys(self):
        self.master.title("Piano Application")
        self.pack(fill="both", expand=1)
        canvas = Canvas(self)
        
        def playsoundC1(self):
            mixer.init()
            mixer.music.load('NoteWavFile\C.wav')
            mixer.music.set_volume(0.5)
            mixer.music.play()
            
        def playsoundD(self):
            mixer.init()
            mixer.music.load('NoteWavFile\D.wav')
            mixer.music.set_volume(0.5)
            mixer.music.play()
            
        def playsoundE(self):
            mixer.init()
            mixer.music.load('NoteWavFile\E.wav')
            mixer.music.set_volume(0.5)
            mixer.music.play()
            
        def playsoundF(self):
            mixer.init()
            mixer.music.load('NoteWavFile\F.wav')
            mixer.music.set_volume(0.5)
            mixer.music.play()
            
        def playsoundG(self):
            mixer.init()
            mixer.music.load('NoteWavFile\G.wav')
            mixer.music.set_volume(0.5)
            mixer.music.play()
            
        def playsoundA(self):
            mixer.init()
            mixer.music.load('NoteWavFile\A.wav')
            mixer.music.set_volume(0.5)
            mixer.music.play()
            
        def playsoundB(self):
            mixer.init()
            mixer.music.load('NoteWavFile\B.wav')
            mixer.music.set_volume(0.5)
            mixer.music.play()
            
        def playsoundC2(self):
            mixer.init()
            mixer.music.load('NoteWavFile\C2.wav')
            mixer.music.set_volume(0.5)
            mixer.music.play()
        
        def playsoundCsharp(self):
            mixer.init()
            mixer.music.load('NoteWavFile\C#.wav')
            mixer.music.set_volume(0.5)
            mixer.music.play()
            
        def playsoundEflat(self):
            mixer.init()
            mixer.music.load('NoteWavFile\Eb.wav')
            mixer.music.set_volume(0.5)
            mixer.music.play()
            
        def playsoundFsharp(self):
            mixer.init()
            mixer.music.load('NoteWavFile\F#.wav')
            mixer.music.set_volume(0.5)
            mixer.music.play()
            
        def playsoundAflat(self):
            mixer.init()
            mixer.music.load('NoteWavFile\Ab.wav')
            mixer.music.set_volume(0.5)
            mixer.music.play()
            
        def playsoundBflat(self):
            mixer.init()
            mixer.music.load('NoteWavFile\Bb.wav')
            mixer.music.set_volume(0.5)
            mixer.music.play()
  
        '''White Key Creation.'''
        c1 = canvas.create_rectangle(0, 100, 100, 400,
        outline="black", fill="#ede0df", tags="c1")
        canvas.tag_bind("c1","<Button-1>", playsoundC1)
        canvas.pack()
        
        d= canvas.create_rectangle(100, 100, 200, 400,
        outline="black", fill="#ede0df", tags="d")
        canvas.tag_bind("d","<Button-1>", playsoundD)
        canvas.pack()
   
        e = canvas.create_rectangle(200, 100, 300, 400,
        outline="black", fill="#ede0df", tags='e')
        canvas.tag_bind("e","<Button-1>", playsoundE)
        canvas.pack()

        f = canvas.create_rectangle(300, 100, 400, 400,
        outline="black", fill="#ede0df", tags='f')
        canvas.tag_bind("f","<Button-1>", playsoundF)
        canvas.pack()
        
        g = canvas.create_rectangle(400, 100, 500, 400,
        outline="black", fill="#ede0df", tags='g')
        canvas.tag_bind("g","<Button-1>", playsoundG)
        canvas.pack()
        
        a = canvas.create_rectangle(500, 100, 600, 400,
        outline="black", fill="#ede0df", tags='a')
        canvas.tag_bind("a","<Button-1>", playsoundA)
        canvas.pack()
        
        b = canvas.pack(fill="both", expand=1)
        canvas.create_rectangle(600, 100, 700, 400,
        outline="black", fill="#ede0df", tags='b')
        canvas.tag_bind("b","<Button-1>", playsoundB)
        canvas.pack()

        c2 = canvas.create_rectangle(700, 100, 800, 400,
        outline="black", fill="#ede0df", tags='c2')
        canvas.tag_bind("c2","<Button-1>", playsoundC2)
        canvas.pack()
        
        '''Black key creation.'''
        csharp = canvas.create_rectangle(75, 100, 125, 250,
        outline="black", fill="black", tags='csharp')
        canvas.tag_bind("csharp","<Button-1>", playsoundCsharp)
        canvas.pack()
        
        EFlat = canvas.create_rectangle(175, 100, 225, 250,
        outline="black", fill="black", tags='Eflat')
        canvas.tag_bind("Eflat","<Button-1>", playsoundEflat)
        canvas.pack()
         
        Fsharp = canvas.create_rectangle(375, 100, 425, 250,
        outline="black", fill="black", tags='Fsharp')
        canvas.tag_bind("Fsharp","<Button-1>", playsoundFsharp)
        canvas.pack()
        
        Aflat = canvas.create_rectangle(475, 100, 525, 250,
        outline="black", fill="black", tags='Aflat')
        canvas.tag_bind("Aflat","<Button-1>", playsoundAflat)
        canvas.pack()
        
        Bflat = canvas.create_rectangle(575, 100, 625, 250,
        outline="black", fill="black", tags='Bflat')
        canvas.tag_bind("Bflat","<Button-1>", playsoundBflat)
        canvas.pack()

def main():
    window = tk.Tk()
    window.geometry("800x500")
    window.attributes('-alpha',True,)
    pianoapplication = Piano()
    window.mainloop()
     
if __name__ == "__main__":
    main()
    

    
        
        

    
