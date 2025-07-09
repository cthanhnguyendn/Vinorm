import subprocess,os
def TTSnorm1(text):
    with open("input.txt", "w+", encoding="utf-8") as fw:
        fw.write(text)
    myenv = os.environ.copy()
    myenv['LD_LIBRARY_PATH'] = 'lib'
    subprocess.check_call(['./main.exe'], env=myenv)
    with open("output.txt", "r", encoding="utf-8") as fr:
        text=fr.read()
    return text
def testnorm(text):
    return text