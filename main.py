import pathlib
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from filters.notch_filters import IdealNotchFilter

def set_plot_title(title):
    plt.title(title, fontsize = 16)

class MainApp:
    def __init__(self):
        #Seeting up root
        self.root = tk.Tk()
        self.root.resizable(0, 0)
        self.root.title("Notch Filter")
        self.root.iconphoto(False, tk.PhotoImage(file = pathlib.Path("imgs/icon.png")))
        #Hyperparams for notch
        self.number_of_points = 3
        #setting up left side of GUI
        self.left_frame = tk.LabelFrame(text = "Original Image")
        self.original_img = tk.Label(self.left_frame, image = "", text = "Load an image \n to preview it here!", padx = 150, pady = 150)
        self.btn_browse_img = tk.Button(self.left_frame, text = "Browse Image", bg = "lightblue", command = self.browse_img)
        self.btn_apply_filter = tk.Button(self.left_frame, text = "Apply Filter", bg = "lightblue", command = self.apply_filter)
        self.original_img.pack()
        self.btn_browse_img.pack(in_ = self.left_frame, fill = tk.X)
        self.btn_apply_filter.pack(in_ = self.left_frame, fill = tk.X)
        self.left_frame.pack(in_ = self.root, side = tk.LEFT, fill = tk.BOTH)
        #setting up Right side of GUI
        self.right_frame = tk.LabelFrame(text = "Filtered Image")
        self.filter_img = tk.Label(self.right_frame, image = "", text = "Apply filter to an image\nto view it here !", padx = 150, pady = 150)
        self.btn_save_img = tk.Button(self.right_frame, text = "Save this Image", bg = "lightblue", command = self.save_img)
        self.filter_img.pack()
        self.btn_save_img.pack(in_ = self.right_frame, fill = tk.X)
        self.right_frame.pack() 
        
    def browse_img(self):
        try:
            file = filedialog.askopenfilename(title = "Load Image", filetypes=[('Images',['*jpeg','*png','*jpg'])]) 
            file = Image.open(file).convert('LA')
            file.save(pathlib.Path("tmp/original_img.png"))
            file = ImageTk.PhotoImage(file)
            self.original_img.configure(text = "", image = file)
            self.original_img.text = ""
            self.original_img.image = file
        except Exception as e:
            messagebox.showerror("An error occured !", e)

    def apply_filter(self):
        try:
            plt.clf()
            plt.imshow(Image.open(pathlib.Path("tmp/original_img.png")), cmap = "gray")
            set_plot_title("Click on image to choose points. (Press any key to Start)")
            plt.waitforbuttonpress()
            set_plot_title(f'Select {self.number_of_points} points with mouse click')
            points = np.asarray(plt.ginput(self.number_of_points, timeout=-1))
            plt.close()
            self.filter_img.configure(text = "", image = self.original_img.image)
            self.filter_img.text = ""
            self.filter_img.image = self.original_img.image
        except Exception as e:
            messagebox.showerror("An error occured!", e)
            
    def save_img(self):
        directory = filedialog.asksaveasfilename(title = "Save Image", filetypes=[('Images',['*jpeg','*png','*jpg'])])
        print(directory)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    MainApp().run()