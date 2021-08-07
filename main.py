import tkinter as tk
from blob_counter import blob_method

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

        button1 = tk.Button(text='Click Me', command=self.run_blob_test, bg='brown', fg='white')
        self.canvas1.create_window(150, 150, window=button1)

    # def hello(self):
    #     label1 = tk.Label(root, text='Hello World!', fg='green', font=('helvetica', 12, 'bold'))
    #     self.canvas1.create_window(150, 200, window=label1)

    def print_contents(self):
        print("Hi. The current entry content is:",
              self.contents.get())

    def run_blob_test(self):
        # IO directories
        input_dir = 'input'
        output_dir = 'output'

        # crop amount
        h_crop = 0
        w_crop = 100

        # contrast adjustment
        contrast = 3
        brightness = -350

        # plate circle params
        circ_param1 = 50
        circ_param2 = 30
        circ_min = 450
        circ_max = 550
        circ_dist = 1000

        # blob params
        marker_size = 25
        min_circularity = 0.3
        min_convex = 0.4
        min_inertia = 0.05
        min_area = 500

        blob_method(input_dir, output_dir, h_crop, w_crop, contrast, brightness, circ_param1, circ_param2, circ_min,
                    circ_max, circ_dist, marker_size, min_circularity, min_convex, min_inertia, min_area)

if __name__ == '__main__':
    root = tk.Tk()
    myApp = App(root)
    myApp.mainloop()