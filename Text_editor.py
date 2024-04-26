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
        self.filename = None  # To keep track of the current file
        self.original_content = None  # To store the original content for comparison
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
        file_menu.add_command(label="Close", command=self.on_close, accelerator="Ctrl+Q")
        
        help_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.about_info)

    def bind_shortcuts(self):
        self.master.bind("<Control-n>", lambda event: self.new_file())
        self.master.bind("<Control-o>", lambda event: self.open_file())
        self.master.bind("<Control-s>", lambda event: self.save_file())
        self.master.bind("<Control-Shift-s>", lambda event: self.saveas_file())
        self.master.bind("<Control-q>", lambda event: self.on_close())

    def new_file(self):
        self.text_area.delete("1.0", tk.END)
        self.filename = None
        self.original_content = None

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)
                self.filename = file_path
                self.original_content = content

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as file:
                content = self.text_area.get("1.0", tk.END)
                file.write(content)
                self.original_content = content
        else:
            self.saveas_file()

    def saveas_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"),("Python File", "*.py"),("HTML File", "*.html"),("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get("1.0", tk.END)
                file.write(content)
                self.filename = file_path
                self.original_content = content

    def on_close(self):
        if self.original_content != self.text_area.get("1.0", tk.END):
            if messagebox.askyesno("Text Editor", "Do you want to save changes before closing? Your unsaved progress will be lost."):
                self.save_file()
        self.master.quit()

    def about_info(self):
        about_info = "This is a simple text editor created using Tkinter in Python\nTo know more about the build visit https://github.com/AlanJohn296/Text-Editor"
        messagebox.showinfo("About", about_info)

def main():
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
