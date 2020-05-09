#Command line program to create a pyramide of '#' with height n
import sys
#This block of code makes sure the user enterd an int,
# and exits the program if argv[1] is not an int
try:
    n = int(sys.argv[1])
except Exception:
    sys.exit("Only integer please")
#Check if n is between the 2 and 50
if n<2 or n>50:
    sys.exit("please enter an int between 2 and 8")
for i in range(1,n+1):
    print((n-i)*' '+i*'#'+"  "+i*'#'+(n-i)*' ')