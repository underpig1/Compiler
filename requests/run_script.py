def run(fileName)
    import ast
    info = ast.literal_eval(str(open("info.txt", "r").readlines()))
    open("./Compile_" + info["name"][:-1] + "/src/totranslate.txt", "w+").writelines([i for i in open("./" + fileName).readlines()])
    translate()
    open("./Compile_" + info["name"][:-1] + "/src/excute.py", "w+").writelines([i for i in open("./Compile_" + info["name"][:-1] + "/src/totranslate.txt").readlines()])
    exec("./Compile_" + info["name"][:-1] + "/src/excute.py")
    os.remove("./Compile_" + info["name"][:-1] + "/src/totranslate.txt")
    os.remove("./Compile_" + info["name"][:-1] + "/src/excute.py")

def translate():
    import ast
    info = ast.literal_eval(str(open("./Compile_" + info["name"][:-1] + "/info.txt", "r").readlines()))
    pythonInfo = {"varint": "", "varstr": "", "varfloat": "", "vararr": "", "vardict": "", "end": "", "varpar": ",", "vardictval": ":", "varparaclose": "]", "varparaopen": "[", "varinclose": "]", "varinopen": "[", "varinsplice": ":", "varsetchar": "=", "func": "def", "funcclose": "", "funcopen": "", "funcparaclose": "):", "funcparaopen": "(", "funcparapar": ",", "funcreturn": "return", "funcdefaultparasetchar": "=", "comone": "#", "commultiopen": "#", "commulticlose": "", "loopif": "if", "loopclose": "", "loopopen": "", "loopparaclose": ":", "loopparaopen": " ", "loopelseif": "elif", "loopelse": "else", "looprep": "", "loopwhile": "while", "loopwaituntil": "","loopwait": "for", "loopfor": "for", "loopistrue": "==", "loopisfalse": "=!", "loopis": "==", "loopand": "and", "loopor": "or", "loopgreat": ">", "loopless": "<", "loopgreatequal": ">=", "looplessequal": "<=", "loopadd": "+", "loopsub": "-", "loopmult": "*", "loopdiv": "/", "loopexpo": "**", "loopmod": "%", "loopinc": "+= 1", "loopdec": "-= 1", "loopaddto": "+=", "loopsubto": "-=", "loopmultto": "*=", "loopdivto": "/=", "loopbreak": "break", "loopcont": "continue", "class": "class", "classclose": "", "classopen": ":", "classinhclose": ")", "classinhopen": "(", "classself": "self", "classvar": ".", "classfunc": ".", "classinit": "__init__", "classdel": "__del__", "impre": "import ", "imclose": "", "imopen": "", "mpass": "pass", "mglob": "global", "mread": "read", "mwrite": "write"}
    with fileinput.FileInput("./Compile_" + info["name"][:-1] + "/src/totranslate.txt", inplace = True) as file:
        for line in file:
            for word in line.split():
                for key, value in info.items():
                    if word == value:
                        line.replace(word, pythonInfo[key], end = "")
                    elif word == info["loopwait"]:
                        line.replace(word, "import time\n\ttime.sleep(" + line[line.index(info["funcparaopen"][-1]) + 1:line.index(info["funcparaclose"][0]) - 1] + ")", end = "")
                    elif word == info["mread"]:
                        line.replace(word, "with open(" + line[line.index(info["funcparaopen"][-1]) + 1:line.index(info["funcparaclose"][0]) - 1] + ", \"r\") as file:\n\treturn file.readlines()", end = "")
                    elif word == info["mwrite"]:
                        line.replace(word, "open(" + line[line.index(info["funcparaopen"][-1]) + 1:line.index(info["funcparapar"][0]) - 1] + ", \"w+\").write(" + line[line.index(info["funcparapar"][-1]) + 1:line.index(info["funcparaclose"][0]) - 1] + ")", end = "")
                    elif word == value:
                        line.replace(word, pythonInfo[key], end = "")
            file.close()
