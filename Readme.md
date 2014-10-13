# ICPC Solution Validator

Trying to check whether your ICPC, NCPC, NWERC, etc solutions work correctly on test input? This program runs your solution against all provided test inputs and reports on any discrepancies.

Almost any solution language works; provided it is <code>./</code> shell-executable.

Floating point numbers are compared up to an accuracy of 1e-6.

### Requirements
* Python 2.7

### Example
* <code>./validate.py xyz.o [testdata directory]</code>

The following directory hierarchy is assumed here:
* validate.py
* xyz.o
* testdata/
** xyz/
*** input1.in
*** input1.ans

Any directory in 'testdata' with the word 'xyz' in the name will match for a testdata directory, which is then recursively searched for all test inputs.

### License
Public domain.


