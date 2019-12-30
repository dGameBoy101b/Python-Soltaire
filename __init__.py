import sys
import os.path

path = sys.path[0]
root = 'solitaire'
while os.path.split(path)[1] != root:
    path = os.path.split(path)[0]
sys.path.append(path)
