#!/usr/local/bin/python3
import tkinter as tk
from tkinter import ttk
import os
import fileinput
import urllib

root = tk.Tk()
root.title("Compiler")
root.geometry("500x700")

def enter():
    global challenge, notebook, text, var, var0, var1, var2, var3, var4, var5, check0, check1, check2, check3, check4, check5
    challenge += 1
    if challenge == 0:
        label.config(text = "Name of Language")
        title.config(text = "Compiler")
        example.config(text = "Name")
    elif challenge == 1:
        title.config(text = "Variables")
        reset("Declaration of Variable Integer", "int", "name")
    elif challenge == 2:
        reset("Declaration of Variable String", "string", "varint")
    elif challenge == 3:
        reset("Declaration of Variable Floating Point", "float", "varstr")
    elif challenge == 4:
        reset("Declaration of Variable Array", "list", "varfloat")
    elif challenge == 5:
        reset("Declaration of Variable Dictionary", "dict", "vararr")
    elif challenge == 6:
        reset("Line Ending", ";", "vardict")
    elif challenge == 7:
        reset("Setting of Variable Int/Str/Float", "int x = 0;", "end")
    elif challenge == 8:
        reset("Array/Dict Parser", ",", "varset")
    elif challenge == 9:
        reset("Setting of Variable Array", "arr x = (0, 0);", "varpar")
    elif challenge == 10:
        reset("Dict Value Declarer", ":", "vararrset")
    elif challenge == 11:
        reset("Setting of Variable Dict", "dict x = (0:0, 0:0);", "vardictval")
    elif challenge == 12:
        reset("List/Dict Param Closing", ")", "vardictset")
    elif challenge == 13:
        reset("List/Dict Param Opening", "(", "varparaclose")
    elif challenge == 14:
        reset("List/Dict Index Closing", "]", "varparaopen")
    elif challenge == 15:
        reset("List/Dict Index Opening", "[", "varinclose")
    elif challenge == 16:
        reset("List/Dict Index Splice", ":", "varinopen")
    elif challenge == 17:
        reset("Variable Set Character", " = ", "varinsplice")
    elif challenge == 18:
        title.config(text = "Functions")
        reset("Declaration of Function", "func", "varsetchar")
    elif challenge == 19:
        reset("Function Container Closing", "}", "func")
    elif challenge == 20:
        reset("Function Container Opening", "{", "funcclose")
    elif challenge == 21:
        reset("Function Parameter Closing", ")", "funcopen")
    elif challenge == 22:
        reset("Function Parameter Opening", "(", "funcparaclose")
    elif challenge == 23:
        reset("Function Parameter Parser", ",", "funcparaopen")
    elif challenge == 24:
        reset("Function Return", "return", "funcparapar")
    elif challenge == 25:
        reset("Setting of Function", "func (parameter = 0, parameter = 0) {return parameter;}", "funcreturn")
    elif challenge == 26:
        reset("Function Default Parameter Set Character", " = ", "funcset")
    elif challenge == 27:
        title.config(text = "Comments")
        reset("Single-Line Comment", "//", "funcdefaultparasetchar")
    elif challenge == 28:
        reset("Multi-Line Comment Opening", "/*", "comone")
    elif challenge == 29:
        reset("Multi-Line Comment Closing", "*/", "commultiopen")
    elif challenge == 30:
        title.config(text = "Loops")
        reset("If Statement Declaration", "if", "commulticlose")
    elif challenge == 31:
        reset("Loop Container Closing", "}", "loopif")
    elif challenge == 32:
        reset("Loop Container Opening", "{", "loopclose")
    elif challenge == 33:
        reset("Loop Parameter Closing", ")", "loopopen")
    elif challenge == 34:
        reset("Loop Parameter Opening", "(", "loopparaclose")
    elif challenge == 35:
        reset("Else If Statement Declaration", "else if", "loopparaopen")
    elif challenge == 36:
        reset("Else Statement Declaration", "else", "loopelseif")
    elif challenge == 37:
        reset("Repeat Statement Declaration", "repeat", "loopelse")
    elif challenge == 38:
        reset("While Statement Declaration", "while", "looprep")
    elif challenge == 39:
        reset("Wait Until Statement Declaration", "wait until", "loopwhile")
    elif challenge == 40:
        reset("Wait Statement Declaration", "wait", "loopwaituntil")
    elif challenge == 41:
        reset("For Statement Declaration", "for", "loopwait")
    elif challenge == 42:
        reset("Logical Operator Is True", "==", "loopfor")
    elif challenge == 43:
        reset("Logical Operator Is False", "!=", "loopistrue")
    elif challenge == 44:
        reset("Logical Operator Is Equal", "===", "loopisfalse")
    elif challenge == 45:
        reset("Logical Operator And", "&&", "loopis")
    elif challenge == 46:
        reset("Logical Operator Or", "||", "loopand")
    elif challenge == 47:
        reset("Logical Operator Greater Than", ">", "loopor")
    elif challenge == 48:
        reset("Logical Operator Less Than", "<", "loopgreat")
    elif challenge == 49:
        reset("Logical Operator Greater Than Or Equal To", ">=", "loopless")
    elif challenge == 50:
        reset("Logical Operator Less Than Or Equal To", "<=", "loopgreatequal")
    elif challenge == 51:
        reset("Expression Add", "+", "looplessequal")
    elif challenge == 52:
        reset("Expression Subtract", "-", "loopadd")
    elif challenge == 53:
        reset("Expression Multiply", "*", "loopsub")
    elif challenge == 54:
        reset("Expression Divide", "/", "loopmult")
    elif challenge == 55:
        reset("Expression Exponent", "**", "loopdiv")
    elif challenge == 56:
        reset("Expression Modulo", "%", "loopexpo")
    elif challenge == 57:
        reset("Expression Increment", "++", "loopmod")
    elif challenge == 58:
        reset("Expression Decrement", "--", "loopinc")
    elif challenge == 59:
        reset("Expression Add To", "+=", "loopdec")
    elif challenge == 60:
        reset("Expression Subtract To", "-=", "loopaddto")
    elif challenge == 61:
        reset("Expression Multiply To", "*=", "loopsubto")
    elif challenge == 62:
        reset("Expression Divide To", "/=", "loopmultto")
    elif challenge == 63:
        reset("Break Statement", "break", "loopdivto")
    elif challenge == 64:
        reset("Continue Statement", "continue", "loopbreak")
    elif challenge == 65:
        title.config(text = "Classes")
        reset("Class Declaration", "class", "loopcont")
    elif challenge == 66:
        reset("Class Container Closing", "}", "class")
    elif challenge == 67:
        reset("Class Container Opening", "{", "classclose")
    elif challenge == 68:
        reset("Class Inheritance Closing", ")", "classopen")
    elif challenge == 69:
        reset("Class Inheritance Opening", "(", "classinhclose")
    elif challenge == 70:
        reset("Class Property Keyword (Self/This)", "self", "classinhopen")
    elif challenge == 71:
        reset("Class Variable Access Char", ".", "classself")
    elif challenge == 72:
        reset("Class Function Access Char", ".", "classvar")
    elif challenge == 73:
        reset("Set Class", "class Class() {__init()__{}}", "classfunc")
    elif challenge == 74:
        reset("Class Call Keyword", "new", "classset")
    elif challenge == 75:
        reset("Function Call Keyword", "exec", "classcall")
    elif challenge == 76:
        title.config(text = "Class Methods")
        reset("Initializing/Constructor Method", "__init__", "funccall")
    elif challenge == 77:
        reset("Destructor Method", "__del__", "classinit")
    elif challenge == 78:
        title.config(text = "Miscellaneous")
        reset("Import Prefix", "#include", "classdel")
    elif challenge == 79:
        reset("Import Container Closing", ")", "impre")
    elif challenge == 80:
        reset("Import Container Opening", "(", "imclose")
    elif challenge == 81:
        reset("Pass Statement", "pass", "imopen")
    elif challenge == 82:
        reset("Global Variable Function", "global", "mpass")
    elif challenge == 83:
        reset("File Read Function", "readlines", "mglob")
    elif challenge == 84:
        reset("File Write Function", "write", "mread")
    elif challenge == 85:
        reset("Print Function", "print", "mwrite")
    elif challenge == 86:
        title.config(text = "Standard Libraries")
        reset("Standard Libraries", "Develop a standard library in Python and in" + info["name"], "mprint")
        text.destroy()
        notebook = ttk.Notebook(frame)
        tab0 = tk.Text(notebook, highlightcolor = "white")
        tab1 = tk.Text(notebook, highlightcolor = "white")
        notebook.add(tab0, text = "Python")
        notebook.add(tab1, text = info["name"][:-1])
        notebook.pack()
        tab0.insert(tk.END, "# Python Custom Standard Library\n# Python Standard Library Included In " + info["name"][:-1])
        tab1.insert(tk.END, info["comone"][:-1] + " " + info["name"][:-1] + " Standard Library")
        root.update()
    elif challenge == 87:
        info.update({"pylib":tab0.get("1.0", tk.END)})
        info.update({"lib":tab1.get("1.0", tk.END)})
        notebook.destroy()
        title.config(text = "Build")
        label.config(text = "Final Language Database")
        example.config(text = "")
        text = tk.Text(frame, highlightcolor = "white")
        text.pack(fill = tk.BOTH, expand = True)
        for key, value in info.items():
            text.insert(tk.END, key + ": " + value)
        root.update()
    elif challenge == 88:
        text.destroy()
        label.config(text = "Build Settings")
        check = tk.IntVar()
        var0 = tk.IntVar()
        var1 = tk.IntVar()
        var2 = tk.IntVar()
        var3 = tk.IntVar()
        var4 = tk.IntVar()
        var5 = tk.IntVar()
        check0 = tk.Checkbutton(frame, text = "Compile with Python Standard Library", variable = var0)
        check1 = tk.Checkbutton(frame, text = "Compile with Custom Standard Library", variable = var1)
        check2 = tk.Checkbutton(frame, text = "Compile with IDE", variable = var2)
        check3 = tk.Checkbutton(frame, text = "Compile with Documentation", variable = var3)
        check4 = tk.Checkbutton(frame, text = "Compile with Editing Capabilities", variable = var4)
        check5 = tk.Checkbutton(frame, text = "Compile with README", variable = var5)
        check0.pack()
        check1.pack()
        check2.pack()
        check3.pack()
        check4.pack()
        check5.pack()
        example.config(text = "")
    elif challenge == 89:
        if not var5.get() == 1:
            challenge = 90
            os.makedirs(os.path.dirname("./Compile_" + info["name"][:-1] + "/src/src"), exist_ok = True)
            enter()
        check0.destroy()
        check1.destroy()
        check2.destroy()
        check3.destroy()
        check4.destroy()
        check5.destroy()
        label.config(text = "README")
        example.config(text = "")
        text = tk.Text(frame, highlightcolor = "white")
        text.pack(fill = tk.BOTH, expand = True)
    elif challenge == 90:
        label.config(text = "Create")
        example.config(text = "")
        os.makedirs(os.path.dirname("./Compile_" + info["name"][:-1] + "/src/src"), exist_ok = True)
        with open("./Compile_" + info["name"][:-1] + "/README.md", "w+") as file:
            file.write(text.get("1.0", tk.END))
            file.close()
        urllib.URLopener().retrieve("https://raw.githubusercontent.com/underpig1/Compiler/master/requests/ide.py", "./Compile_" + info["name"][:-1] + "/src/ide.py")
        urllib.URLopener().retrieve("https://raw.githubusercontent.com/underpig1/Compiler/master/requests/launch.command", "./Compile_" + info["name"][:-1] + "/launch.command")
        info.update({"tag":"." + info["name"][:-1][:3].lower()})
        open("./Compile_" + info["name"][:-1] + "/src/info.txt", "w+").write(str(info))
        os.system("cd /Users/user/Desktop/Compile_" + info["name"][:-1])
        os.system("chmod +x launch.command")
    elif challenge == 91:
        label.config(text = "Language Complete")
        example.config(text = "Access the IDE with the launch.command file\nEdit the IDE with the ide.py file")
    elif challenge == 92:
        os.system("cd /Users/user/Desktop/Compile_" + info["name"][:-1])
        os.system("./launch.command")

# TODO change/select parts order after each section; project tabs; not, and; add custom translation; function call; line-ending raise errors; line-ending auto-return and -indent; compiler language; call class keyword; standard libraries
def reset(texts, examples, name):
    info.update({name:text.get("1.0", tk.END)})
    label.config(text = texts)
    text.delete("1.0", tk.END)
    example.config(text = examples)

pythonInfo = {"classcall": " ", "funccall": " ", "varint": "", "varstr": "", "varfloat": "", "vararr": "", "vardict": "", "end": "", "varpar": ",", "vardictval": ":", "varparaclose": "]", "varparaopen": "[", "varinclose": "]", "varinopen": "[", "varinsplice": ":", "varsetchar": "=", "func": "def", "funcclose": "", "funcopen": "", "funcparaclose": "):", "funcparaopen": "(", "funcparapar": ",", "funcreturn": "return", "funcdefaultparasetchar": "=", "comone": "#", "commultiopen": "#", "commulticlose": "", "loopif": "if", "loopclose": "", "loopopen": "", "loopparaclose": ":", "loopparaopen": " ", "loopelseif": "elif", "loopelse": "else", "looprep": "", "loopwhile": "while", "loopwaituntil": "","loopwait": "for", "loopfor": "for", "loopistrue": "==", "loopisfalse": "=!", "loopis": "==", "loopand": "and", "loopor": "or", "loopgreat": ">", "loopless": "<", "loopgreatequal": ">=", "looplessequal": "<=", "loopadd": "+", "loopsub": "-", "loopmult": "*", "loopdiv": "/", "loopexpo": "**", "loopmod": "%", "loopinc": "+= 1", "loopdec": "-= 1", "loopaddto": "+=", "loopsubto": "-=", "loopmultto": "*=", "loopdivto": "/=", "loopbreak": "break", "loopcont": "continue", "class": "class", "classclose": "", "classopen": ":", "classinhclose": ")", "classinhopen": "(", "classself": "self", "classvar": ".", "classfunc": ".", "classinit": "__init__", "classdel": "__del__", "impre": "import ", "imclose": "", "imopen": "", "mpass": "pass", "mglob": "global", "mread": "read", "mwrite": "write"}
challenge = 0
info = {}

title = tk.Label(root, text = "Compiler", font = "Ariel 35")
title.pack(pady = 10)
label = tk.Label(root, text = "Name of Language", font = "Ariel 15")
label.pack()
example = tk.Label(root, text = "Name", font = "Ariel 15", fg = "lightgray")
example.pack()
frame = tk.Frame(root, height = 600, width = 500)
frame.pack()
text = tk.Text(frame, highlightcolor = "white")
text.pack(fill = tk.BOTH, expand = True)
button = tk.Button(root, text = "Continue", highlightthickness = 500, highlightcolor = "lightgray", cursor = "hand", command = enter)
button.pack(fill = tk.BOTH, expand = True)
root.update()
