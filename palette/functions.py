"""Project Palette
functions for palette project
"""

from tkinter import filedialog
from tkinter.constants import END
import tkinter.messagebox as msgbox
import os
import webbrowser

from PIL import Image

if __name__ == "__main__":
    from data import *
else:
    from palette.data import *


def get_path(path):
    return os.path.join(os.getcwd(), path)


def open_url(url):
    try:
        webbrowser.open(url)
    except webbrowser.Error as exp:
        msgbox.showerror("Error", f"Cannot open the browser!\n{exp}")
    except Exception:
        return


def save_new_csv(entry_1, entry_2, entry_3):
    path_now = os.getcwd()
    filename = filedialog.asksaveasfilename(
        initialdir=path_now,
        title="Save",
        filetypes=(("Data files", "*.csv"), ("all files", "*.*")),
        defaultextension=".csv",
    )
    if filename == "":
        return
    else:
        data = [
            entry_1.get(),
            entry_2.get(),
            entry_3.get(),
        ]
        with open(filename, "w", encoding="utf-8") as csv:
            csv.write(",".join(data))


def open_csv(entry_1, entry_2, entry_3):
    filename = ""
    path_now = os.getcwd()
    filename = filedialog.askopenfilename(
        title="Find your data",
        filetypes=(("Data files", "*.csv"), ("all files", "*.*")),
        initialdir=path_now,
    )
    if filename == "":
        return
    else:
        if os.path.isfile(filename):
            entry_1.delete(0, END)
            entry_2.delete(0, END)
            entry_3.delete(0, END)
            try:
                with open(filename, "r", encoding="utf-8") as csv:
                    values = csv.read().split(",")
                    entry_1.insert(0, values[0])
                    entry_2.insert(0, values[1])
                    entry_3.insert(0, values[2])
            except IndexError:
                msgbox.showwarning(
                    "Error", "Not enough data. \nPlease try other files.",
                )
            except Exception:
                msgbox.showwarning(
                    "Error", "The file is corrupted. \nPlease try other files.",
                )
        else:
            msgbox.showerror("Error", "Unable to find the file!")


def get_img(img_file_name, folder=None, extension="png"):
    if folder is None:
        img_path = get_path(f"img\{img_file_name}.{extension}")
    elif folder:
        img_path = get_path(f"img\{folder}\{img_file_name}.{extension}")
    try:
        image = Image.open(img_path)
    except:
        img_path = get_path("img\error.png")
        image = Image.open(img_path)
    return image


def show_ImgPage(class_name, master, *parameters):
    """class_name = ImgPage"""
    return class_name(master, *parameters)


"""Functions only for the test"""


def get_texts(num):
    """get sample texts
    
    Args:
        num(int): number of texts to return
        
    Returns:
        list: list of sample texts 
    """
    return ["SAMPLE" for i in range(num)]


def get_images(num):
    """get sample images
    
    Args:
        num(int): number of images to return
        
    Returns:
        list: list of sample images    
    """
    img_info = "SAMPLE"
    return [img_info for i in range(num)]


def get_urls(num):
    """get sample urls
       : https://denev6.tistory.com/
    
    Args:
        num(int): number of urls to return
        
    Returns:
        list: list of sample urls    
    """
    url = "https://denev6.tistory.com/"
    return [url for i in range(num)]


def get_colors(num):
    """get sample colors
    
    Args:
        num(int): number of colors to return
        
    Returns:
        list: list of sample colors    
    """
    color = "#8FAADC"
    return [color for i in range(num)]


def get_Text_sample(num):
    """get sample text
    
    Args:
        num(int): number of new lines
        
    Returns:
        str: lines of sample texts    
    """
    text = ""
    for i in range(num):
        text += f"-- Text {i} --\n\n"
    return text
