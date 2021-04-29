#!/usr/bin/env python3

import os
import hashlib
import sys

def CalcHash(name):
    m = hashlib.md5()
    try:
        with open(name, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                m.update(chunk)
        return m.hexdigest()
    except:
        pass



ori_dict = {}
ori_stack = []
ori_path = sys.argv[1]
if ori_path[-1] == '/':
    ori_path = ori_path[:-2]
src_pj_name = ori_path[ori_path.rfind('/') + 1:]


ori_stack.append(ori_path)
while len(ori_stack) != 0:
    os.chdir(ori_stack.pop())
    f = os.listdir()
    for files in f:
        if os.path.isdir(files):
            ori_stack.append(os.getcwd() + '/' + files)
        elif os.path.isfile(files):
            ori_strip_path = os.getcwd()[os.getcwd().find(src_pj_name) + len(src_pj_name) + 1:]
            ori_dict[ ori_strip_path + '/'  + files] = CalcHash(files) 

# move to cmp_path
os.chdir(sys.argv[2])
cmp_stack = []
cmp_path = sys.argv[2]
print(len(ori_dict))

replace_list = []
for i in ori_dict:
    if os.path.exists(cmp_path + '/' + i):
        h = CalcHash(cmp_path + '/' + i)
        if h != ori_dict[i]:
            replace_list.append(i)


for f in replace_list:
    print(f)
