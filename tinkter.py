import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import os

root = tk.Tk()

file = ttk.Frame(root)
file.pack()

fileSelect = ttk.Entry(file, width=49)
fileSelect.pack(side="left")

def loadFiles(filepath):
    if filepath:
        with open(filepath, "r") as f:
            textContent = f.read()
        textEditor.delete("1.0", tk.END)
        textEditor.insert(tk.END, textContent)
        setWindowTitle()

def openFileBrowser():
    selectedDir = os.path.join(os.path.dirname(__file__), "txtDocs")
    filepath = filedialog.askopenfilename(initialdir = selectedDir)
    loadFiles(filepath)

fileBrowse = ttk.Button(file, width=10, text="Browse", command=openFileBrowser)
fileBrowse.pack(side="right")

textEditor = tk.Text(root, height=16, width=60)
textEditor.pack()

def saveText():
    file = fileSelect.get()
    textContent = textEditor.get("1.0", tk.END)
    with open(f"selectedDir/{file}", "w") as f:
        f.write(textContent)

saveButton = ttk.Button(root, text="Lagre", width=29, command=saveText)
saveButton.pack(side="right")

exitButton = ttk.Button(root, text="Lukk", width=29, command=root.destroy)
exitButton.pack(side="left")

def setWindowTitle():
    filepath = __file__
    pathComponents = filepath.split(os.sep)

    lastFolders = os.path.join(*pathComponents[-4:-1])
    fileName = os.path.basename(filepath)
    modTitle = lastFolders + os.sep + fileName

    maxLength = 30
    if len(modTitle) > maxLength:
        sepCount = max(len(pathComponents), 1)
        truncatedPath = os.path.join(*pathComponents[:maxLength // sepCount])
        truncatedFile = filepath.split(os.sep)[-1]
        winTitle = truncatedPath + os.sep + truncatedFile

    winTitle = str(winTitle + " - Budget Editor of Text")
    root.title(winTitle) # Budget Editor of Text

setWindowTitle()
root.resizable(False, False)
root.mainloop()
