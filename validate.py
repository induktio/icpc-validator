#!/usr/bin/python

import os
import re
from sys import argv, stderr
from subprocess import check_output
from os.path import exists, join

def compare(a, b):
    try:
        if re.match("^\d+?\.\d+?$", a) or re.match("^\d+?\.\d+?$", b):
            if abs(float(a)-float(b)) < 1e-6:
                return True
            if float(a).is_integer() and float(b).is_integer() and float(a)==float(b):
                return True
    except ValueError:
        pass
    return a==b
    

def check_problem(program, infile, ansfile):
    wanted = ''.join(open(ansfile, 'r').readlines()).split('\n')
    print 'Testing', infile, wanted[:16][:-1]
    result = check_output(
        "%s < %s" % (program, infile), shell=True).split('\n')
    
    if len(wanted) != len(result):
        print 'FAIL', result[:16][:-1]
        return False
    
    for a,b in zip(wanted, result):
        if not compare(a,b):
            print 'FAIL', result[:16][:-1]
            return False
    
    print 'OK'
    return True


if __name__ == "__main__":
    program = argv[1]
    assert(exists(program))
    name = str.lower(re.split('\W+', program)[0])
    if '.py' in program:
        cmdline = 'python '+program
    elif '.class' in program:
        cmdline = 'java '+program.replace('.class', '')
    else:
        cmdline = './'+program
    
    testdir = (argv[2] if len(argv)>=3 else 'testdata')
    
    problemdir = False
    for f in os.listdir(testdir):
        if name in str.lower(f):
            problemdir = f
            break
    count = 0
    fails = 0
    problempath = join(testdir, problemdir)
    assert(problempath)
    
    for dirpath, dirnames, filenames in sorted(os.walk(problempath)):
        for testf in filenames:
            if '.in' in testf:
                
                answerf = '.'.join(testf.split('.')[:-1]) + '.ans'
                if not check_problem(
                cmdline, join(dirpath, testf), join(dirpath, answerf)):
                    fails += 1
                count += 1
    
    print 'Tests passed', (count-fails), '/', count




