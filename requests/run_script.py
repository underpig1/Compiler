def run(fileName):
    open("./Compile_" + info["name"][:-1] + "/src/totranslate.txt", "w+").writelines([i for i in open("./" + fileName).readlines()])
    translate()
    open("./Compile_" + info["name"][:-1] + "/src/excute.py", "w+").writelines([i for i in open("./Compile_" + info["name"][:-1] + "/src/totranslate.txt").readlines()])
    exec("./Compile_" + info["name"][:-1] + "/src/excute.py")
    os.remove("./Compile_" + info["name"][:-1] + "/src/totranslate.txt")
    os.remove("./Compile_" + info["name"][:-1] + "/src/excute.py")

def translate():
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
