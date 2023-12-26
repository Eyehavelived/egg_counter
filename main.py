import tkinter as tk
# from tkinter import _Anchor, _Compound, _Cursor, _ImageSpec, _Relief, _ScreenUnits, _TakeFocusValue, Misc, Variable
from tkinter import font
# import tkinter.ttk as ttk
from typing import Any
# from typing_extensions import Literal
from blob_counter import blob_method

class App(tk.Frame):
    PADDING = 5
    WINDOW_HEIGHT = 720
    WINDOW_WIDTH = 1500
    current_row = 0

    def __init__(self, master):
        super().__init__(master)
        self.winfo_toplevel().title("Egg Counter")

        # crop amount
        self.crop_cat = tk.Label(text="Crop")

        self.h_label = tk.Label(text="Crop Height from:")
        self.w_label = tk.Label(text="Crop Width from:")
        self.h_crop_entry = tk.Entry()
        self.w_crop_entry = tk.Entry()
        self.h_crop = tk.StringVar()
        self.w_crop = tk.StringVar()
        self.h_crop.set("0")
        self.w_crop.set("100")
        self.h_crop_entry["textvariable"] = self.h_crop
        self.w_crop_entry["textvariable"] = self.w_crop

        self.crop_cat.grid(row=self.current_row, column=0, pady=self.PADDING, padx=self.PADDING, columnspan=4)
        self.h_label.grid(row=self.next_row(), column=0, pady=self.PADDING, padx=self.PADDING)
        self.h_crop_entry.grid(row=self.current_row, column=1, pady=self.PADDING, padx=self.PADDING)
        self.w_label.grid(row=self.current_row, column=2, pady=self.PADDING, padx=self.PADDING)
        self.w_crop_entry.grid(row=self.current_row, column=3, pady=self.PADDING, padx=self.PADDING)

        # contrast adjustment
        self.contrast_cat = tk.Label(text="Contrast & Brightness")

        self.alpha_label = tk.Label(text="Contrast Multiplier:")
        self.alpha_desc = tk.Label(text="Choose a number between 1.0 and 3.0 to increase contrast.")
        self.beta_label = tk.Label(text="Brightness Adder:")
        self.beta_desc = tk.Label(text="Whole numbers only. Negative values will darken the image.")

        self.contrast_entry = tk.Entry()
        self.brightness_entry = tk.Entry()
        self.contrast = tk.StringVar()
        self.brightness = tk.StringVar()
        self.contrast.set("3.0")
        self.brightness.set("-350")
        self.contrast_entry["textvariable"] = self.contrast
        self.brightness_entry["textvariable"] = self.brightness

        self.contrast_cat.grid(row=self.next_row(), column=0, pady=self.PADDING, padx=self.PADDING, columnspan=4)
        self.alpha_label.grid(row=self.next_row(), column=0, pady=self.PADDING, padx=self.PADDING)
        self.contrast_entry.grid(row=self.current_row, column=1, pady=5, padx=5)
        self.beta_label.grid(row=self.current_row, column=2, pady=self.PADDING, padx=self.PADDING)
        self.brightness_entry.grid(row=self.current_row, column=3, pady=5, padx=5)
        self.alpha_desc.grid(row=self.next_row(), column=0, pady=1, padx=self.PADDING, columnspan=2)
        self.beta_desc.grid(row=self.current_row, column=2, pady=1, padx=self.PADDING, columnspan=2)

        # plate circle params
        self.circle_cat = tk.Label(text="Plate Detection")

        self.p1_label = tk.Label(text="Param1:")
        self.p2_label = tk.Label(text="Param2:")
        self.circ_min_label = tk.Label(text="Min Size:")
        self.circ_max_label = tk.Label(text="Max Size:")
        self.circ_dist_label = tk.Label(text="Circle Distance:")

        self.include_blobs_outside_plate_checkbox = tk.Checkbutton(text='Include blobs outside the plate', onvalue=1, offvalue=0)
        self.circ_p1_entry = tk.Entry()
        self.circ_p2_entry = tk.Entry()
        self.circ_min_entry = tk.Entry()
        self.circ_max_entry = tk.Entry()
        self.circ_dist_entry = tk.Entry()

        self.include_blobs_outside_plate = tk.IntVar()
        self.circ_p1 = tk.StringVar()
        self.circ_p2 = tk.StringVar()
        self.circ_min = tk.StringVar()
        self.circ_max = tk.StringVar()
        self.circ_dist = tk.StringVar()

        self.include_blobs_outside_plate.set(1)
        self.circ_p1.set("50")
        self.circ_p2.set("30")
        self.circ_min.set("450")
        self.circ_max.set("550")
        self.circ_dist.set("1000")

        self.include_blobs_outside_plate_checkbox["variable"] = self.include_blobs_outside_plate
        self.circ_p1_entry["textvariable"] = self.circ_p1
        self.circ_p2_entry["textvariable"] = self.circ_p2
        self.circ_min_entry["textvariable"] = self.circ_min
        self.circ_max_entry["textvariable"] = self.circ_max
        self.circ_dist_entry["textvariable"] = self.circ_dist

        self.circle_cat.grid(row=self.next_row(), column=0, pady=self.PADDING, padx=self.PADDING, columnspan=4)
        self.include_blobs_outside_plate_checkbox.grid(row=self.next_row(), column=0, pady=self.PADDING, padx=self.PADDING, columnspan=4)
        self.p1_label.grid(row=self.next_row(), column=0, pady=self.PADDING, padx=self.PADDING)
        self.circ_p1_entry.grid(row=self.current_row, column=1, pady=self.PADDING, padx=self.PADDING)
        self.p2_label.grid(row=self.current_row, column=2, pady=self.PADDING, padx=self.PADDING)
        self.circ_p2_entry.grid(row=self.current_row, column=3, pady=self.PADDING, padx=self.PADDING)
        self.circ_min_label.grid(row=self.next_row(), column=0, pady=self.PADDING, padx=self.PADDING)
        self.circ_min_entry.grid(row=self.current_row, column=1, pady=self.PADDING, padx=self.PADDING)
        self.circ_max_label.grid(row=self.current_row, column=2, pady=self.PADDING, padx=self.PADDING)
        self.circ_max_entry.grid(row=self.current_row, column=3, pady=self.PADDING, padx=self.PADDING)
        self.circ_dist_label.grid(row=self.next_row(), column=0, pady=self.PADDING, padx=self.PADDING)
        self.circ_dist_entry.grid(row=self.current_row, column=1, pady=self.PADDING, padx=self.PADDING)

        # Marker
        self.marker_cat = tk.Label(text="Marker")
        self.marker_size_label = tk.Label(text="Marker Size:")
        self.marker_size_entry = tk.Entry()
        self.marker_size = tk.StringVar()
        self.marker_size.set("25")
        self.marker_size_entry["textvariable"] = self.marker_size

        self.marker_cat.grid(row=self.next_row(), column=0, pady=self.PADDING, padx=self.PADDING, columnspan=4)
        self.marker_size_label.grid(row=self.next_row(), column=1, pady=self.PADDING, padx=self.PADDING)
        self.marker_size_entry.grid(row=self.current_row, column=2, pady=self.PADDING, padx=self.PADDING)

        # blob detection
        self.blob_cat = tk.Label(text="Blob Method Parameters")

        self.min_circularity_label = tk.Label(text="Min Circularity:")
        self.min_convexity_label = tk.Label(text="Min Convexity:")
        self.min_inertia_label = tk.Label(text="Min Inertia:")
        self.min_area_label = tk.Label(text="Min Area:")

        self.min_circularity_entry = tk.Entry()
        self.min_convexity_entry = tk.Entry()
        self.min_inertia_entry = tk.Entry()
        self.min_area_entry = tk.Entry()

        self.min_circularity = tk.StringVar()
        self.min_convexity = tk.StringVar()
        self.min_inertia = tk.StringVar()
        self.min_area = tk.StringVar()

        self.min_circularity.set("0.3")
        self.min_convexity.set("0.4")
        self.min_inertia.set("0.05")
        self.min_area.set("500")

        self.min_circularity_entry["textvariable"] = self.min_circularity
        self.min_convexity_entry["textvariable"] = self.min_convexity
        self.min_inertia_entry["textvariable"] = self.min_inertia
        self.min_area_entry["textvariable"] = self.min_area

        self.blob_cat.grid(row=self.next_row(), column=0, pady=self.PADDING, padx=self.PADDING, columnspan=4)
        self.min_circularity_label.grid(row=self.next_row(), column=0, pady=self.PADDING, padx=self.PADDING)
        self.min_circularity_entry.grid(row=self.current_row, column=1, pady=self.PADDING, padx=self.PADDING)
        self.min_convexity_label.grid(row=self.current_row, column=2, pady=self.PADDING, padx=self.PADDING)
        self.min_convexity_entry.grid(row=self.current_row, column=3, pady=self.PADDING, padx=self.PADDING)
        self.min_inertia_label.grid(row=self.next_row(), column=0, pady=self.PADDING, padx=self.PADDING)
        self.min_inertia_entry.grid(row=self.current_row, column=1, pady=self.PADDING, padx=self.PADDING)
        self.min_area_label.grid(row=self.current_row, column=2, pady=self.PADDING, padx=self.PADDING)
        self.min_area_entry.grid(row=self.current_row, column=3, pady=self.PADDING, padx=self.PADDING)

        # finally, the buttons
        self.preview_button = tk.Button(text="Preview", command=self.preview)
        self.batch_button = tk.Button(text='Batch Process', command=self.run_blob_test)
        self.preview_button.grid(row=self.next_row(), column=1, pady=self.PADDING * 2, padx=self.PADDING * 2)
        self.batch_button.grid(row=self.current_row, column=2, pady=self.PADDING * 2, padx=self.PADDING * 2)

    def preview(self):
        self.run_blob_test(True)

    def next_row(self):
        self.current_row += 1
        return self.current_row

    def run_blob_test(self, is_preview=False):
        # IO directories
        input_dir = 'input'
        output_dir = 'output'

        # crop amount
        h_crop = int(self.h_crop.get())
        w_crop = int(self.w_crop.get())

        # contrast adjustment
        contrast = float(self.contrast.get())
        brightness = int(self.brightness.get())

        # plate circle params
        include_blobs_outside_plate = bool(self.include_blobs_outside_plate.get())
        circ_param1 = int(self.circ_p1.get())
        circ_param2 = int(self.circ_p2.get())
        circ_min = int(self.circ_min.get())
        circ_max = int(self.circ_max.get())
        circ_dist = int(self.circ_dist.get())

        # blob params
        marker_size = int(self.marker_size.get())
        min_circularity = float(self.min_circularity.get())
        min_convex = float(self.min_convexity.get())
        min_inertia = float(self.min_inertia.get())
        min_area = int(self.min_area.get())

        blob_method(input_dir, output_dir, h_crop, w_crop, contrast, brightness, circ_param1, circ_param2, circ_min,
                    circ_max, circ_dist, marker_size, min_circularity, min_convex, min_inertia, min_area, is_preview, include_blobs_outside_plate)

        if not is_preview:
            self.quit()


if __name__ == '__main__':
    root = tk.Tk()
    myApp = App(root)
    myApp.mainloop()