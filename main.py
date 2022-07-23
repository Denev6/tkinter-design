"""Project Palette

- version -
python=3.9.7
pillow=8.4.0

code by DeneV
"""

from tkinter import *
import tkinter.ttk as ttk
from tkinter.tix import *

from PIL import ImageTk

from palette.functions import *


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        Tk.title(self, "Palette")
        Tk.geometry(self, "360x480+500+200")
        Tk.resizable(self, 0, 0)
        ico_path = get_path("img\icon.ico")
        Tk.iconbitmap(self, ico_path)
        self._frame = None
        self.refresh_frame(IntroPage)

    def refresh_frame(self, frame, *parameters):
        if self._frame is not None:
            self._frame.destroy()
        self._frame = frame(self, *parameters)
        self._frame.pack(expand=YES)


class MainFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self._font = (None, 13)
        self._bg = "#ffffff"
        self._green = "#349E71"
        self._green2 = "#CDEFE0"
        self.pack(fill="both", expand=True)
        style = ttk.Style()
        style.theme_use("clam")
        style.map("TCombobox", fieldbackground=[("readonly", "#ffffff")])
        style.map("TCombobox", selectbackground=[("readonly", "#ffffff")])
        style.map("TCombobox", selectforeground=[("readonly", "#000000")])
        style.map("TCombobox", background=[("readonly", "#ffffff")])
        style.configure("TNotebook", background=self._green)
        style.configure("TNotebook.Tab", font=(None, 10))
        style.map("TNotebook.Tab", background=[("selected", "#FEDF51")])


class InfoPage(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("INFO")
        self.geometry("300x360+680+270")
        Label(self, text="TEXT", bg="#ffffff", font=(None, 12)).pack(
            fill=BOTH, expand=True
        )


class ImgPage(Toplevel):
    def __init__(self, master, img_file_name, folder=None, extension="png"):
        super().__init__(master)
        image = get_img(img_file_name, folder, extension)
        photo = ImageTk.PhotoImage(image)
        width, height = image.size
        self.title("img_file_name")
        self.geometry(f"{width}x{height}+680+270")
        self.resizable(0, 0)
        label = Label(self, image=photo)
        label.image = photo
        label.pack()


class InfoBalloon(Balloon):
    def __init__(self, master):
        super().__init__(master, initwait=60)
        for i in self.subwidgets_all():
            i.config(bg="#ffffff")
        self.message.config(wraplength=100)


class IntroPage(MainFrame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="#ffffff")
        Label(self, bg=self._bg, height=4).pack(fill="x")
        image = get_img("logo")
        photo_logo = ImageTk.PhotoImage(image)
        label_logo = Label(self, image=photo_logo, bg=self._bg)
        label_logo.image = photo_logo
        label_logo.pack()
        image = get_img("button-start", "design")
        photo_button = ImageTk.PhotoImage(image)
        button = Button(
            self,
            image=photo_button,
            relief="flat",
            bg=self._bg,
            command=lambda: master.refresh_frame(StartPage),
        )
        button.image = photo_button
        button.pack(ipadx=3, ipady=2)


class StartPage(MainFrame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg=self._bg)
        combo_var = StringVar()
        entry_1_var = DoubleVar()
        entry_2_var = DoubleVar()
        entry_3_var = DoubleVar()
        f_title = Frame(self, bg=self._bg)
        f_title.pack(fill="x", pady=10)
        Label(f_title, bg=self._bg, width=3).pack(side="left")
        image = get_img("icon", extension="ico").resize((25, 25), Image.ANTIALIAS)
        photo_icon = ImageTk.PhotoImage(image)
        icon = Label(f_title, image=photo_icon, bg=self._bg)
        icon.image = photo_icon
        icon.pack(side="left")
        Label(
            f_title, text="Basic Info", bg=self._bg, font=(None, 14, "bold"), anchor="w"
        ).pack(pady=30, fill="x")
        f_left = Frame(self, bg=self._bg)
        f_right = Frame(self, bg=self._bg)
        f_btn = Frame(self, bg=self._bg)
        f_btn.pack(side="bottom", fill="x", expand=True, anchor="n", pady=15)
        f_left.pack(side="left", fill="both", expand=True)
        f_right.pack(side="right", fill="both", expand=True)
        Label(f_left, bg=self._bg, text="OPTION", font=self._font, fg="#404040").pack(
            pady=17, anchor="e", padx=13
        )
        Label(
            f_left, bg=self._bg, text="ENTRY_1", font=self._font, bd=0, fg="#404040"
        ).pack(pady=10, anchor="e", padx=13)
        Label(
            f_left, bg=self._bg, text="ENTRY_2", font=self._font, bd=0, fg="#404040"
        ).pack(pady=10, anchor="e", padx=13)
        Label(
            f_left, bg=self._bg, text="ENTRY_3", font=self._font, bd=0, fg="#404040"
        ).pack(pady=10, anchor="e", padx=13)
        combo = ttk.Combobox(
            f_right, textvariable=combo_var, font=self._font, width=14, state="readonly"
        )
        combo["values"] = ["OPTION_A", "OPTION_B", "OPTION_C"]
        combo.current(0)
        combo.pack(pady=16, anchor="w")
        entry_1 = Entry(
            f_right,
            textvariable=entry_1_var,
            font=self._font,
            width=15,
            relief="flat",
            bg=self._green2,
        )
        entry_1.pack(pady=10, anchor="w")
        entry_2 = Entry(
            f_right,
            textvariable=entry_3_var,
            font=self._font,
            width=15,
            relief="flat",
            bg=self._green2,
        )
        entry_2.pack(pady=10, anchor="w")
        entry_3 = Entry(
            f_right,
            textvariable=entry_2_var,
            font=self._font,
            width=15,
            relief="flat",
            bg=self._green2,
        )
        entry_3.pack(pady=10, anchor="w")
        entry_1.delete(0, END)
        entry_3.delete(0, END)
        entry_2.delete(0, END)
        image = get_img("point-line", "design")
        photo_line = ImageTk.PhotoImage(image)
        point_line = Label(f_btn, bg=self._bg, relief="flat", image=photo_line)
        point_line.image = photo_line
        point_line.pack(pady=10)
        Label(
            f_btn,
            text="You can open/save files using buttons below",
            font=(None, 8),
            bg=self._bg,
        ).pack(fill="x")
        image = get_img("button-submit", "design")
        photo_submit = ImageTk.PhotoImage(image)
        btn_right = Button(
            f_btn,
            bg=self._bg,
            image=photo_submit,
            relief="flat",
            activebackground=self._bg,
            command=lambda: self.switch_to_ResultPage(master),
        )
        btn_right.image = photo_submit
        btn_right.pack(side="right", padx=25, pady=20)
        image = get_img("save-mint", "icon").resize((25, 25), Image.ANTIALIAS)
        photo_save = ImageTk.PhotoImage(image)
        width_save, height_save = image.size
        btn_save = Button(
            f_btn,
            bg=self._bg,
            image=photo_save,
            relief="flat",
            width=width_save,
            height=height_save,
            activebackground=self._bg,
            command=lambda: save_new_csv(entry_1, entry_2, entry_3),
        )
        btn_save.image = photo_save
        btn_save.pack(side="right", pady=20)
        image = get_img("file-text-mint", "icon").resize((25, 25), Image.ANTIALIAS)
        photo_file = ImageTk.PhotoImage(image)
        width_file, height_file = image.size
        btn_open = Button(
            f_btn,
            bg=self._bg,
            image=photo_file,
            relief="flat",
            width=width_file,
            height=height_file,
            activebackground=self._bg,
            command=lambda: open_csv(entry_1, entry_2, entry_3),
        )
        btn_open.image = photo_file
        btn_open.pack(side="right", pady=20)
        self._menu = Menu(master)
        self._menu_data = Menu(self._menu, tearoff=0)
        self._menu_data.add_command(
            label="OPEN", command=lambda: open_csv(entry_1, entry_2, entry_3)
        )
        self._menu_data.add_command(
            label="SAVE", command=lambda: save_new_csv(entry_1, entry_2, entry_3)
        )
        self._menu_data.add_separator()
        self._menu_data.add_command(label="INFO", command=lambda: InfoPage(master))
        self._menu.add_cascade(label="DATA", menu=self._menu_data)
        self._menu_sample = Menu(self._menu, tearoff=0)
        self._menu_sample.add_command(label="INFO", command=lambda: InfoPage(master))
        self._menu.add_cascade(label="SAMPLE", menu=self._menu_sample)
        master.config(menu=self._menu)

    def disable_menu_file(self):
        self._menu_data.entryconfig("OPEN", state="disable")
        self._menu_data.entryconfig("SAVE", state="disable")
        self._menu_data.entryconfig("INFO", state="disable")

    def switch_to_ResultPage(self, master):
        # Get data from ComboBox and Entry
        texts = get_texts(5)
        imgs = get_images(5)
        urls = get_urls(3)
        self.disable_menu_file()
        master.refresh_frame(ResultPage, texts, imgs, urls)


class ResultPage(MainFrame):
    def __init__(self, master, texts, imgs, urls):
        super().__init__(master)
        self.config(bg=self._green)
        notebook = ttk.Notebook(self, width=300, height=370)
        notebook.pack(expand=True)
        f_1 = Frame(self, bg="#ffffff")
        f_2 = Label(self, bg="#ffffff")
        f_3 = Frame(self, bg="#ffffff")
        notebook.add(f_1, text="sample_1")
        Label(f_1, bg="#ffffff", height=2).pack(fill="x")
        Button(
            f_1,
            text=texts[0],
            relief="flat",
            bg="#ffffff",
            font=self._font,
            activebackground="#ffffff",
            command=lambda: show_ImgPage(ImgPage, master, imgs[0]),
        ).pack(fill="x", pady=7)
        Button(
            f_1,
            text=texts[1],
            relief="flat",
            bg="#ffffff",
            font=self._font,
            activebackground="#ffffff",
            command=lambda: show_ImgPage(ImgPage, master, imgs[1]),
        ).pack(fill="x", pady=7)
        Button(
            f_1,
            text=texts[2],
            relief="flat",
            bg="#ffffff",
            font=self._font,
            activebackground="#ffffff",
            command=lambda: show_ImgPage(ImgPage, master, imgs[2]),
        ).pack(fill="x", pady=7)
        Button(
            f_1,
            text=texts[3],
            relief="flat",
            bg="#ffffff",
            font=self._font,
            activebackground="#ffffff",
            command=lambda: show_ImgPage(ImgPage, master, imgs[3]),
        ).pack(fill="x", pady=7)
        Button(
            f_1,
            text=texts[4],
            relief="flat",
            bg="#ffffff",
            font=self._font,
            activebackground="#ffffff",
            command=lambda: show_ImgPage(ImgPage, master, imgs[4]),
        ).pack(fill="x", pady=7)
        f_ref_1 = Frame(f_1, bg="#ffffff")
        f_ref_1.pack(pady=7, side="bottom", padx=10)
        image = get_img("image-mint", "icon")
        photo_img = ImageTk.PhotoImage(image)
        f_image = Label(f_ref_1, image=photo_img, bg="#ffffff")
        f_image.image = photo_img
        f_image.pack(side="left")
        Label(f_ref_1, text="* click to \nshow images.", bg="#ffffff").pack(side="left")
        notebook.add(f_2, text="sample_2")
        Label(f_2, bg="#ffffff", height=2).pack(fill="x")
        Button(
            f_2,
            text=texts[0],
            relief="flat",
            bg="#ffffff",
            font=self._font,
            activebackground="#ffffff",
            command=lambda: open_url(urls[0]),
        ).pack(fill="x", pady=13)
        Button(
            f_2,
            text=texts[1],
            relief="flat",
            bg="#ffffff",
            font=self._font,
            activebackground="#ffffff",
            command=lambda: open_url(urls[1]),
        ).pack(fill="x", pady=13)
        Button(
            f_2,
            text=texts[2],
            relief="flat",
            bg="#ffffff",
            font=self._font,
            activebackground="#ffffff",
            command=lambda: open_url(urls[2]),
        ).pack(fill="x", pady=13)
        f_ref_tip = Frame(f_2, bg=self._bg)
        f_ref_tip.pack(pady=7, side="bottom", padx=10)
        image = get_img("link-mint", "icon")
        photo_link = ImageTk.PhotoImage(image)
        f_image = Label(f_ref_tip, image=photo_link, bg="#ffffff")
        f_image.image = photo_link
        f_image.pack(side="left")
        Label(f_ref_tip, text="* click to \nopen urls.", bg="#ffffff").pack(side="left")
        notebook.add(f_3, text="sample_3")
        scrollbar = Scrollbar(f_3, orient="vertical")
        scrollbar.pack(side="right", fill="y")
        f_text = Text(
            f_3,
            bg="#ffffff",
            wrap="word",
            spacing1=10,
            spacing2=2,
            relief="flat",
            font=(None, 10),
            yscrollcommand=scrollbar.set,
        )
        f_text.pack(side="left", fill="both")
        scrollbar.config(command=f_text.yview)
        f_text.delete(1.0, END)
        f_text.insert(1.0, "- Sample -")
        f_text.configure(state="disabled")
        f_btn = Frame(self, bg=self._green)
        f_btn.pack(side="bottom", fill="x", expand=True, padx=30)
        image = get_img("arrow-right-circle-white", "icon")
        photo_right = ImageTk.PhotoImage(image)
        width, height = image.size
        btn_right = Button(
            f_btn,
            image=photo_right,
            bg=self._green,
            relief="flat",
            width=width,
            height=height,
            activebackground=self._green,
            command=lambda: master.refresh_frame(OptionalPage, texts, imgs, urls),
        )
        btn_right.image = photo_right
        btn_right.pack(side="right")


class OptionalPage(MainFrame):
    def __init__(self, master, texts, imgs, urls):
        super().__init__(master)
        self.config(bg=self._bg)
        combo_1 = StringVar()
        combo_2 = StringVar()
        combo_3 = StringVar()
        f_title = Frame(self, bg=self._bg)
        f_title.pack(fill="x", pady=35)
        Label(f_title, bg=self._bg, width=3).pack(side="left")
        image = get_img("user-plus-green", "icon")
        photo_icon = ImageTk.PhotoImage(image)
        icon = Label(f_title, image=photo_icon, bg=self._bg)
        icon.image = photo_icon
        icon.pack(side="left", padx=3)
        Label(
            f_title,
            text="Optional Info",
            bg=self._bg,
            font=(None, 14, "bold"),
            anchor="w",
        ).pack(pady=10, fill="x")
        f_left = Frame(self, bg=self._bg)
        f_right = Frame(self, bg=self._bg)
        f_btn = Frame(self, bg=self._bg)
        f_btn.pack(side="bottom", anchor="n", fill="x", expand=True)
        f_left.pack(side="left", fill="both", expand=True, pady=5)
        f_right.pack(side="right", fill="both", expand=True, pady=5)
        Label(f_left, bg=self._bg, text="COMBO_1", font=self._font, fg="#404040").pack(
            padx=18, pady=20, anchor="e"
        )
        f_color = Frame(f_left, bg=self._bg)
        f_color.pack(fill="x")
        image = get_img("help-circle-black", "icon").resize((12, 12), Image.ANTIALIAS)
        photo_help = ImageTk.PhotoImage(image)
        tip_mark = Label(f_color, image=photo_help, bg=self._bg)
        tip_mark.image = photo_help
        tip_mark.pack(padx=2, side="right")
        Label(f_color, bg=self._bg, text="COMBO_2", font=self._font, fg="#404040").pack(
            pady=20, side="right", fill="x"
        )
        tip_box = InfoBalloon(master)
        tip_box.bind_widget(tip_mark, balloonmsg="Here we have Info")
        Label(f_left, bg=self._bg, text="COMBO_3", font=self._font, fg="#404040").pack(
            padx=18, pady=20, anchor="e"
        )
        combobox_1 = ttk.Combobox(
            f_right, textvariable=combo_1, font=self._font, state="readonly"
        )
        combobox_2 = ttk.Combobox(
            f_right, textvariable=combo_2, font=self._font, state="readonly"
        )
        combobox_3 = ttk.Combobox(
            f_right, textvariable=combo_3, font=self._font, state="readonly"
        )
        combobox_1["values"] = ["OPTION_1", "OPTION_2", "OPTION_3", "OPTION_4"]
        combobox_2["values"] = ["OPTION_1", "OPTION_2", "OPTION_3", "OPTION_4"]
        combobox_3["values"] = ["OPTION_1", "OPTION_2", "OPTION_3", "OPTION_4"]
        combobox_1.current(0)
        combobox_1.pack(pady=20)
        combobox_2.current(0)
        combobox_2.pack(pady=20)
        combobox_3.current(0)
        combobox_3.pack(pady=20)
        image = get_img("point-line", "design")
        photo_line = ImageTk.PhotoImage(image)
        point_line = Label(f_btn, bg=self._bg, relief="flat", image=photo_line)
        point_line.image = photo_line
        point_line.pack(pady=10)
        Label(
            f_btn,
            text="? mark provides an information box.",
            font=(None, 8),
            bg=self._bg,
        ).pack(fill="x")
        image_right = get_img("check-circle-mint", "icon")
        photo_right = ImageTk.PhotoImage(image_right)
        width_right, height_right = image_right.size
        image_left = get_img("arrow-left-circle-mint", "icon")
        photo_left = ImageTk.PhotoImage(image_left)
        width_left, height_left = image_left.size
        btn_right = Button(
            f_btn,
            image=photo_right,
            bg="#ffffff",
            relief="flat",
            width=width_right,
            height=height_right,
            activebackground=self._bg,
            command=lambda: self.switch_to_OptionaResultPage(master, urls),
        )
        btn_left = Button(
            f_btn,
            image=photo_left,
            bg="#ffffff",
            relief="flat",
            width=width_left,
            height=height_left,
            activebackground=self._bg,
            command=lambda: master.refresh_frame(ResultPage, texts, imgs, urls),
        )
        btn_right.image = photo_right
        btn_right.pack(side="right", padx=25, pady=20)
        btn_left.image = photo_left
        btn_left.pack(side="right", pady=20)

    def switch_to_OptionaResultPage(self, master, urls):
        # Get data from ComboBox
        texts = get_texts(5)
        imgs = get_images(4)
        colors = get_colors(3)
        texts_ = get_Text_sample(15)
        master.refresh_frame(OptionResultPage, urls, texts, imgs, colors, texts_)


class OptionResultPage(MainFrame):
    def __init__(self, master, urls, texts, imgs, colors, texts_):
        super().__init__(master)
        self.config(bg=self._green)
        notebook = ttk.Notebook(self, width=300, height=340)
        notebook.pack(expand=True)
        f_season = Frame(self, bg="#ffffff")
        f_color = Frame(self, bg="#ffffff")
        f_situation = Frame(self, bg="#ffffff")
        notebook.add(f_season, text="sample_1")
        Label(f_season, bg="#ffffff", height=2).pack(fill="x")
        Button(
            f_season,
            text=texts[0],
            bg="#ffffff",
            relief="flat",
            font=self._font,
            activebackground="#ffffff",
            command=lambda: show_ImgPage(ImgPage, master, imgs[0]),
        ).pack(fill="x", pady=7)
        Button(
            f_season,
            text=texts[1],
            bg="#ffffff",
            relief="flat",
            font=self._font,
            activebackground="#ffffff",
            command=lambda: show_ImgPage(ImgPage, master, imgs[1]),
        ).pack(fill="x", pady=7)
        Button(
            f_season,
            text=texts[2],
            bg="#ffffff",
            relief="flat",
            font=self._font,
            activebackground="#ffffff",
            command=lambda: show_ImgPage(ImgPage, master, imgs[2]),
        ).pack(fill="x", pady=7)
        Button(
            f_season,
            text=texts[3],
            bg="#ffffff",
            relief="flat",
            font=self._font,
            activebackground="#ffffff",
            command=lambda: show_ImgPage(ImgPage, master, imgs[3]),
        ).pack(fill="x", pady=7)
        f_ref_season = Frame(f_season, bg=self._bg)
        f_ref_season.pack(pady=7, side="bottom", padx=10)
        image = get_img("image-mint", "icon")
        photo_img = ImageTk.PhotoImage(image)
        f_image = Label(f_ref_season, image=photo_img, bg="#ffffff")
        f_image.image = photo_img
        f_image.pack(side="left")
        Label(f_ref_season, text="* click to \nshow images.", bg="#ffffff").pack(
            pady=7, side="bottom"
        )
        notebook.add(f_color, text="sample_2")
        Label(
            f_color, bg="#ffffff", text="Colors", relief="flat", font=self._font
        ).pack(anchor="w", padx=10, pady=18, expand=True)
        Label(f_color, bg=colors[0], height=4, relief="groove").pack(
            fill="x", padx=10, pady=10, expand=True
        )
        Label(f_color, bg=colors[1], height=4, relief="groove").pack(
            fill="x", padx=10, pady=10, expand=True
        )
        Label(f_color, bg=colors[2], height=4, relief="groove").pack(
            fill="x", padx=10, pady=10, expand=True
        )
        notebook.add(f_situation, text="sample_3")
        scrollbar = Scrollbar(f_situation, orient="vertical")
        scrollbar.pack(side="right", fill="y")
        f_text = Text(
            f_situation,
            bg="#ffffff",
            wrap="word",
            spacing1=10,
            spacing2=3,
            spacing3=10,
            font=(None, 11),
            yscrollcommand=scrollbar.set,
        )
        f_text.pack(side="left", fill="both")
        scrollbar.config(command=f_text.yview)
        f_text.delete(1.0, END)
        f_text.insert(1.0, texts_)
        f_text.configure(state="disabled")
        f_btn = Frame(self, bg=self._green)
        f_btn.pack(side="bottom", fill="x", expand=True, padx=30)
        image_quit = get_img("log-out-white", "icon")
        photo_quit = ImageTk.PhotoImage(image_quit)
        width_quit, height_quit = image_quit.size
        image_left = get_img("arrow-left-circle-white", "icon")
        photo_left = ImageTk.PhotoImage(image_left)
        width_left, height_left = image_left.size
        btn_quit = Button(
            f_btn,
            image=photo_quit,
            bg=self._green,
            relief="flat",
            width=width_quit,
            height=height_quit,
            activebackground=self._green,
            command=master.quit,
        )
        tip_box = InfoBalloon(master)
        tip_box.bind_widget(btn_quit, balloonmsg="quit")
        btn_left = Button(
            f_btn,
            image=photo_left,
            bg=self._green,
            relief="flat",
            width=width_left,
            height=height_left,
            activebackground=self._green,
            command=lambda: master.refresh_frame(OptionalPage, texts, imgs, urls),
        )
        btn_quit.image = photo_quit
        btn_quit.pack(side="right")
        btn_left.image = photo_left
        btn_left.pack(side="right", padx=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
