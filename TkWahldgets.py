import tkinter as tk

#  A two sided list with arrows to move objects to either side, able to call the selected list
class ListboxSelecter(tk.Frame):

    def to_chosen(self):
        active = self.options_box.get(tk.ACTIVE)
        if not active == '':
            self.options_box.delete(tk.ACTIVE)
            self.chosen_box.insert(tk.END, active)
            self.__alphabetalize_chosen()

    def to_options(self):
        active = self.chosen_box.get(tk.ACTIVE)
        if not active == '':
            self.chosen_box.delete(tk.ACTIVE)
            self.options_box.insert(tk.END, active)
            self.__alphabetalize_options()

    def all_to_options(self):
        while not self.chosen_box.get(tk.ACTIVE) == '':
            self.to_options()

    def all_to_chosen(self):
        while not self.options_box.get(tk.ACTIVE) == '':
            self.to_chosen()

    def __init__(self, root, optionsTitle="", chosenTitle=""):
        super().__init__(root)
        self.options_frame = tk.Frame(self)
        self.options_title = tk.Label(self.options_frame, text=optionsTitle)
        self.options_box = tk.Listbox(self.options_frame)
        self.options_scrollbar = tk.Scrollbar(self.options_frame)
        self.options_box.config(yscrollcommand=self.options_scrollbar.set)
        self.options_scrollbar.config(command=self.options_box.yview)
        self.options_title.pack(side=tk.TOP)
        self.options_box.pack(side=tk.LEFT)
        self.options_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.to_chosen_button = tk.Button(self, text=">", command=self.to_chosen)
        self.to_options_button = tk.Button(self, text="<", command=self.to_options)
        self.all_to_chosen_button = tk.Button(self, text=">>", command=self.all_to_chosen)
        self.all_to_options_button = tk.Button(self, text="<<", command=self.all_to_options)

        self.chosen_frame = tk.Frame(self)
        self.chosen_title = tk.Label(self.chosen_frame, text=chosenTitle)
        self.chosen_box = tk.Listbox(self.chosen_frame)
        self.chosen_scrollbar = tk.Scrollbar(self.chosen_frame)
        self.chosen_box.config(yscrollcommand=self.chosen_scrollbar.set)
        self.chosen_scrollbar.config(command=self.chosen_box.yview)
        self.chosen_title.pack(side=tk.TOP)
        self.chosen_box.pack(side=tk.LEFT)
        self.chosen_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.options_frame.grid(row=0, rowspan=6, column=0)
        self.all_to_options_button.grid(row=1, column=1)
        self.to_options_button.grid(row=2, column=1)
        self.to_chosen_button.grid(row=3, column=1)
        self.all_to_chosen_button.grid(row=4, column=1)
        self.chosen_frame.grid(row=0, rowspan=6, column=2)

    def add_to_list(self, members: list):
        for obj in members:
            if isinstance(obj, str):
                self.options_box.insert(tk.END, obj)
        self.__alphabetalize_options()

    def reset_list(self):
        self.chosen_box.delete(0, tk.END)
        self.options_box.delete(0, tk.END)

    def __alphabetalize_options(self):
        options_list = list(self.options_box.get(0, tk.END))
        self.options_box.delete(0, tk.END)
        options_list.sort()
        for obj in options_list:
            self.options_box.insert(tk.END, obj)

    def __alphabetalize_chosen(self):
        chosen_list = list(self.chosen_box.get(0, tk.END))
        self.chosen_box.delete(0, tk.END)
        chosen_list.sort()
        for obj in chosen_list:
            self.chosen_box.insert(tk.END, obj)

    def get_chosen(self):
        return list(self.chosen_box.get(0, tk.END))

    def get_options(self):
        return list(self.options_box.get(0, tk.END))


class Table(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        print("Noob I'm alive")


