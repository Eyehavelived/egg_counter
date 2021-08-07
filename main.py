import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.canvas1 = tk.Canvas(root, width=300, height=300)
        self.canvas1.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()
        self.canvas1.create_window(150, 100, window=self.entrythingy)

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)

        button1 = tk.Button(text='Click Me', command=self.print_contents, bg='brown', fg='white')
        self.canvas1.create_window(150, 150, window=button1)

    # def hello(self):
    #     label1 = tk.Label(root, text='Hello World!', fg='green', font=('helvetica', 12, 'bold'))
    #     self.canvas1.create_window(150, 200, window=label1)

    def print_contents(self):
        print("Hi. The current entry content is:",
              self.contents.get())

if __name__ == '__main__':
    root = tk.Tk()
    myApp = App(root)
    myApp.mainloop()