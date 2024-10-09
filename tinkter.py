import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

file = ttk.Frame(root)
file.pack()

file_select = ttk.Entry(file, width=49)
file_select.pack(side="left")

def file_confirm():
    print("placeholder")

file_confirm = ttk.Button(file, width=10, text="Select", command=file_confirm)
file_confirm.pack(side="right")

text_editor = tk.Text(root, height=16, width=60)
text_editor.pack()

def save_text():
    text_content = text_editor.get("1.0", tk.END)
    with open("sample.txt", "w") as file:
        file.write(text_content)

save_button = ttk.Button(root, text="Lagre", width=29, command=save_text)
save_button.pack(side="right")

exit_button = ttk.Button(root, text="Lukk", width=29, command=root.destroy)
exit_button.pack(side="left")

root.title("BEoT") # Budget Editor of Text
root.resizable(False, False)
root.mainloop()
