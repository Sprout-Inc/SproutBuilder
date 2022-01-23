import os
import sys
if len(sys.argv) < 1:
    print("Usage: python sproutcompiler.py [inputfile] Output: SproutDesktop")
    exit()
else:
    os.system("cython -3 --embed -o SproutDesktop.c " + sys.argv[1])
    os.system("gcc -Os -I /usr/include/python3.8 -o SproutDesktop SproutDesktop.c -lpython3.8 -lpthread -lm -lutil -ldl")
