''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():
    sys_input=sys.stdin.read()
    binary_list=sys_input.split('\n')
    binary_list=[int(i) for i in binary_list if i]
    count=0
    for i in binary_list:
        if i==1:
            count+=1
    print(count)


main()

