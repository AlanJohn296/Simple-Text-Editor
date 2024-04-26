import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")
        self.master.iconbitmap("./Note_logo.png")
        self.text_area = tk.Text(self.master, wrap="word")
        self.text_area.pack(expand=True, fill="both")
        self.create_menu()
        self.bind_shortcuts()

    def create_menu(self):
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        # File menu
        file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_separator()
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self.saveas_file, accelerator="Ctrl+Shift+S")
        file_menu.add_command(label="Close", command=self.master.quit, accelerator="Ctrl+Q")
        
        help_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.about_info)

    def bind_shortcuts(self):
        self.master.bind("<Control-n>", lambda event: self.new_file())
        self.master.bind("<Control-o>", lambda event: self.open_file())
        self.master.bind("<Control-s>", lambda event: self.save_file())
        self.master.bind("<Control-Shift-s>", lambda event: self.saveas_file())
        self.master.bind("<Control-q>", lambda event: self.master.quit())
        
    def new_file(self):
        self.text_area.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"),("Python File", "*.py"),("Other Files")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get("1.0", tk.END)
                file.write(content)
        # else:
        #     self.saveas_file()
                
    def saveas_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"),("Python File", "*.py"),("Html File", "*.html"),("Other Files")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get("1.0", tk.END)
                file.write(content)
                
    def about_info(self):
        about_info = "This is a simple text editor created using Tkinter in Python"
        messagebox.showinfo("About", about_info)

def main():
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
