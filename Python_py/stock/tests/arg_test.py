import sys
import getopt
import argparse



argv = sys.argv[1:]
sum = 0


print('Number of arguemnts : {}'.format(len(sys.argv)))
print('Arguments passed: {}'.format(str(sys.argv)))
            

try:
    opts, args = getopt.getopt(argv, 'a:b:', ['foperand', 'soperand'])
    if len(opts) == 0 and len(opts) > 2:
        print('check again. Lengt..... <first ')
    else:
        for opt, arg in opts:
            sum += int(arg)

        print('Sum is {}'.format(sum))


except getopt.GetoptError:
    print('usage: add.py -a <first operand> -b < >')
    sys.exit(2)



ap = argparse.ArgumentParser()

# ap.add_argument("--a", "--foperand", required)






