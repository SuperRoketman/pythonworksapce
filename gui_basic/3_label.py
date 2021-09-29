from tkinter import*

root = Tk()
root.title("SR GUI")
root.geometry("640x480")


label1 = Label(root, text="안녕하세요.")
label1.pack()

photo = PhotoImage(file="E:\githubdesktop-SuperRoketman\pythonworksapce\gui_basic\image.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요.")

    global photo2
    photo2 = PhotoImage(file="E:\githubdesktop-SuperRoketman\pythonworksapce\gui_basic\image2.png")
    label2.config(image=photo2)
    label2.pack()

btn = Button(root, text="클릭", command=change)
btn.pack()


root.mainloop()
