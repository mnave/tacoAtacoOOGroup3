
f1 = open("output1113.txt", 'r').read()
f2 = open("examples\example1\\output1113.txt", 'r').read()
if f1 == f2:
    print "Example 1 OK"
else:
    print "Example 1 Not OK"

f1 = open("output1921.txt", 'r').read()
f2 = open("examples\example2\\output1921.txt", 'r').read()
if f1 == f2:
    print "Example 2 OK"
else:
    print "Example 2 Not OK"


f1 = open("output1517.txt", 'r').read()
f2 = open("examples\example3\\output1517.txt", 'r').read()
if f1 == f2:
    print "Example 3 OK"
else:
    print "Example 3 Not OK"
