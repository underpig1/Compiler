import tkinter as tk
import ast
from tkinter import filedialog
import os
import webbrowser

root = tk.Tk()
root.geometry("700x500")
info = ast.literal_eval(str(open("./Compile_" + info["name"][:-1] + "/src/info.txt", "r").readlines()))
root.title(info["name"][:-1] + " Developer Environment")
pythonInfo = {"classcall": " ", "funccall": " ", "varint": "", "varstr": "", "varfloat": "", "vararr": "", "vardict": "", "end": "", "varpar": ",", "vardictval": ":", "varparaclose": "]", "varparaopen": "[", "varinclose": "]", "varinopen": "[", "varinsplice": ":", "varsetchar": "=", "func": "def", "funcclose": "", "funcopen": "", "funcparaclose": "):", "funcparaopen": "(", "funcparapar": ",", "funcreturn": "return", "funcdefaultparasetchar": "=", "comone": "#", "commultiopen": "#", "commulticlose": "", "loopif": "if", "loopclose": "", "loopopen": "", "loopparaclose": ":", "loopparaopen": " ", "loopelseif": "elif", "loopelse": "else", "looprep": "", "loopwhile": "while", "loopwaituntil": "","loopwait": "for", "loopfor": "for", "loopistrue": "==", "loopisfalse": "=!", "loopis": "==", "loopand": "and", "loopor": "or", "loopgreat": ">", "loopless": "<", "loopgreatequal": ">=", "looplessequal": "<=", "loopadd": "+", "loopsub": "-", "loopmult": "*", "loopdiv": "/", "loopexpo": "**", "loopmod": "%", "loopinc": "+= 1", "loopdec": "-= 1", "loopaddto": "+=", "loopsubto": "-=", "loopmultto": "*=", "loopdivto": "/=", "loopbreak": "break", "loopcont": "continue", "class": "class", "classclose": "", "classopen": ":", "classinhclose": ")", "classinhopen": "(", "classself": "self", "classvar": ".", "classfunc": ".", "classinit": "__init__", "classdel": "__del__", "impre": "import ", "imclose": "", "imopen": "", "mpass": "pass", "mglob": "global", "mread": "read", "mwrite": "write"}

def yview(*args):
    text.yview(*args)
    helpText.yview(*args)

def saveFileAs():
    global currentFile
    currentFile = filedialog.asksaveasfilename(initialdir = "/Users/user/Desktop/")
    open(currentFile + info["tag"][:-1], "w+").write(text.get("1.0", tk.END))

def saveFile():
    global currentFile
    if currentFile == "":
        saveAs()
    else:
        os.remove(currentFile)
        open(currentFile + info["tag"][:-1], "w+").write(text.get("1.0", tk.END))

def openFile():
    global currentFile
    currentFile = filedialog.askopenfilename(initialdir = "/Users/user/Desktop/")
    for line in open(currentFile, "r").readlines():
        text.insert(tk.END, line)

def newFile():
    global currentFile
    currentFile = ""
    text.delete("1.0", tk.END)

def runFile():
    run(currentFile)

def run(fileName):
    open("./Compile_" + info["name"][:-1] + "/src/totranslate.txt", "w+").writelines([i for i in open("./" + fileName).readlines()])
    translate()
    open("./Compile_" + info["name"][:-1] + "/src/excute.py", "w+").writelines([i for i in open("./Compile_" + info["name"][:-1] + "/src/totranslate.txt").readlines()])
    try:
        exec("./Compile_" + info["name"][:-1] + "/src/excute.py")
    except Exception as exception:
        shell.insert(tk.END, str(exception))
    os.remove("./Compile_" + info["name"][:-1] + "/src/totranslate.txt")
    os.remove("./Compile_" + info["name"][:-1] + "/src/excute.py")

def helpFile():
    global helpText
    helpRoot = tk.Tk()
    helpRoot.geometry("500x700")
    helpRoot.title("Help")
    helpText = tk.Text(helpRoot, highlightcolor = "white")
    helpText.pack(fill = tk.BOTH, expand = True, side = tk.LEFT)
    helpScrollbar = tk.Scrollbar(helpRoot, orient = tk.VERTICAL, command = yview)
    helpScrollbar.pack(fill = tk.Y, side = tk.LEFT)
    helpText.config(yscrollcommand = helpScrollbar.set)
    helpText.insert(tk.END, "Help Center")
    helpText.insert(tk.END, "\nSyntax Translations:")
    for key, value in info.items():
        helpText.insert(tk.END, key + ": " + value + "\n")
    helpText.insert(tk.END, "\nDirect Syntax Translations (Python):\n")
    for key, value in info.items():
        helpText.insert(tk.END, pythonInfo[key] + ": " + value + "\n")
    helpText.insert(tk.END, "\nStandard Library:\n")
    helpText.insert(tk.END, info["lib"])
    helpText.insert(tk.END, "\nCustom Standard Library (Python):\n")
    helpText.insert(tk.END, info["pylib"])
    helpText.insert(tk.END, "\nNote: Language comes with Python standard library. For more information on Python's standard library, visit https://docs.python.org/3/library/")
    helpText.config(state = tk.DISABLED)

def translate():
    with fileinput.FileInput("./Compile_" + info["name"][:-1] + "/src/totranslate.txt", inplace = True) as file:
        for line in file:
            for word in line.split():
                for key, value in info.items():
                    if word == value:
                        try:
                            line.replace(word, pythonInfo[key], end = "")
                        except:
                            pass
                    elif word == info["loopwait"]:
                        line.replace(word, "import time\n\ttime.sleep(" + line[line.index(info["funcparaopen"][-1]) + 1:line.index(info["funcparaclose"][0]) - 1] + ")", end = "")
                    elif word == info["mread"]:
                        line.replace(word, "with open(" + line[line.index(info["funcparaopen"][-1]) + 1:line.index(info["funcparaclose"][0]) - 1] + ", \"r\") as file:\n\treturn file.readlines()", end = "")
                    elif word == info["mwrite"]:
                        line.replace(word, "open(" + line[line.index(info["funcparaopen"][-1]) + 1:line.index(info["funcparapar"][0]) - 1] + ", \"w+\").write(" + line[line.index(info["funcparapar"][-1]) + 1:line.index(info["funcparaclose"][0]) - 1] + ")", end = "")
            file.close()

currentFile = ""
text = tk.Text(root, highlightcolor = "white")
text.pack(fill = tk.BOTH, expand = True, side = tk.LEFT)
scrollbar = tk.Scrollbar(root, orient = tk.VERTICAL, command = yview)
scrollbar.pack(fill = tk.Y, side = tk.LEFT)
text.config(yscrollcommand = scrollbar.set)
shell = tk.Text(root, bg = "#F0F0F0", highlightthickness = 0, fg = "red")
shell.pack(fill = tk.BOTH, expand = True, side = tk.BOTTOM)
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff = 0)
filemenu.add_command(label = "New", command = newFile)
filemenu.add_command(label = "Open", command = openFile)
filemenu.add_command(label = "Save", command = saveFile)
filemenu.add_command(label = "Save As...", command = saveFileAs)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)
runmenu = tk.Menu(menubar, tearoff = 0)
runmenu.add_command(label = "Debug", command = runFile) #
runmenu.add_command(label = "Run Module", command = runFile)
menubar.add_cascade(label = "Run", menu = runmenu)
helpmenu = tk.Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "Help", command = helpFile)
helpmenu.add_command(label = "About...", command = lambda x: webbrowser.open("https://github.com/underpig1/Compiler"))
menubar.add_cascade(label = "Help", menu = helpmenu)
root.config(menu = menubar)
root.update()
