# ICPC Solution Validator

Trying to check whether your ICPC, NCPC, NWERC, etc. solutions to past problems work correctly on test input? This program runs your solution against all provided test inputs, and reports on any discrepancies.

Almost any solution language works; provided it is <code>./</code> shell-executable.

Floating point numbers are compared up to an accuracy of 1e-6.

### Installation
    pip install --user git+https://github.com/induktio/icpc-validator.git#egg=solcheck

### Example
* <code>solcheck.py [-t TESTDIR] xyz.o</code>

If test input directory is not provided, it defaults to 'testdata'.

The following directory hierarchy is assumed here:
<pre><code>. 
|- xyz.o
|- testdata/
   |- xyz/
      |- input1.in
      |- input1.ans
</code></pre>

Any directory in 'testdata' with the word 'xyz' in the name will match for the problem's test input directory. It is then recursively searched for all test inputs (.in) and wanted outputs (.ans).

### License
Public domain.


