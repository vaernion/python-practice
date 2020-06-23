import sys

print(sys.argv,len(sys.argv))

# handle 2 numbers
if (len(sys.argv) >= 3 and sys.argv[1].isnumeric() and sys.argv[2].isnumeric()):
        print(int(sys.argv[1]) * int(sys.argv[2]))


# handle "list" input [1,2,3,4]
if (sys.argv[1][0] == "[" and sys.argv[1][-1] == "]"):
    a = sys.argv[1][1:-1]
    a = a.split(',') 
    for i in a: 
        print(i) 
