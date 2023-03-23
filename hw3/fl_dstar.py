import os
import sys

from tabulate import tabulate

passing_dir = sys.argv[1]
failing_dir = sys.argv[2]

# fdir ='/Users/suuuuu017/Documents/UVA_2022-2023_Spring/SA/hw3/cs6888-public/files/hw3/test2/fdir'
# pdir ='/Users/suuuuu017/Documents/UVA_2022-2023_Spring/SA/hw3/cs6888-public/files/hw3/test2/pdir'

fdir = failing_dir
pdir = passing_dir

codedict = {}
totalfail = 0

for subdir, dirs, files in os.walk(fdir):
    for file in files:
        totalfail = totalfail + 1
        f=open(os.path.join(subdir, file),'r')
        # print("---------------")
        # print(os.path.join(subdir, file))
        lines=f.readlines()
        f.close()
        for line in lines:
            s = line.split(":", 1)
            l = s[0]
            l = l.strip()
            c = s[1].split(":", 1)
            cl = c[0]
            cl = cl.strip()
            code = c[1]
            code = code.strip()
            # print("prefix is", l, "line number is", cl, "actual code is", code)
            if not cl in codedict.keys():
                codedict[cl] = {}
                codedict[cl]['code'] = code
                codedict[cl]['f'] = 0
                codedict[cl]['p'] = 0
            if l != '-' and l != '#####':
                # codedict[cl]['f'] = codedict[cl]['f'] + int(l)
                codedict[cl]['f'] = codedict[cl]['f'] + 1


        # print(codedict)
        # input()

for subdir, dirs, files in os.walk(pdir):
    for file in files:
        f=open(os.path.join(subdir, file),'r')
        # print("---------------")
        # print(os.path.join(subdir, file))
        lines=f.readlines()
        f.close()
        for line in lines:
            s = line.split(":", 1)
            l = s[0]
            l = l.strip()
            c = s[1].split(":", 1)
            cl = c[0]
            cl = cl.strip()
            code = c[1]
            code = code.strip()
            # print("prefix is", l, "line number is", cl, "actual code is", code)
            if not cl in codedict.keys():
                codedict[cl] = {}
                codedict[cl]['code'] = code
                codedict[cl]['f'] = 0
                codedict[cl]['p'] = 0
            if l != '-' and l != '#####':
                codedict[cl]['p'] = codedict[cl]['p'] + 1

        # print(codedict)
        # input()

for key, value in codedict.items():
    if (value['p'] + totalfail - value['f']) == 0:
        sus = 0
    else:
        sus = value['f'] ** 2 / (value['p'] + totalfail - value['f'])
    codedict[key]['sus'] = sus

codedict = sorted(codedict.items(), key=lambda item: (-1*item[1]['sus'], -1*item[0]))

print(codedict)
t = []
for i in codedict[0:10]:
    key = i[0]
    value = i[1]
    if key != 0:
        t.append([key, value['code'], value['f'], value['p'], totalfail, value['sus']])

print(tabulate(t, headers=['Line#', 'Statement', '#failedTest(s)', '#passedTests(s)', 'total_failed'
                           , 'Suspiciousness'], floatfmt=".2f"))

