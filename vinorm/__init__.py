
import subprocess,os
import importlib.util
import os.path

def TTSnorm(text, punc = False, unknown = True, lower = True, rule = False ):
    # Get the directory where the vinorm module is located
    spec = importlib.util.find_spec('vinorm')
    if spec is None or spec.origin is None:
        raise ImportError("Could not locate vinorm module")
    A = os.path.dirname(spec.origin)

    #print(A)
    I=A+"/input.txt"
    with open(I, mode="w+", encoding="utf-8") as fw:
        fw.write(text)

    myenv = os.environ.copy()
    myenv['LD_LIBRARY_PATH'] = A+'/lib'

    E=A+"/main.exe"
    Command = [E]
    if punc:
        Command.append("-punc")
    if unknown:
        Command.append("-unknown")
    if lower:
        Command.append("-lower")
    if rule:
        Command.append("-rule")
    subprocess.check_call(Command, env=myenv, cwd=A)
    
    O=A+"/output.txt"
    with open(O, mode="r", encoding="utf-8") as fr:
        text=fr.read()
    TEXT=""
    S=text.split("#line#")
    for s in S:
        if s=="":
            continue
        TEXT+=s+". "


    return TEXT
