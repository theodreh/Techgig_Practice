''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

import sys
def light_format(count,i,format_list):
    if count==0 and i !='!' and not format_list[0]:
        format_list[0]=i
    if count==1 and i !='!' and not format_list[1]:
        format_list[1]=i
    if count==2 and i !='!' and not format_list[2]:
        format_list[2]=i
    if count==3 and i !='!' and not format_list[3]:
        format_list[3]=i
    return format_list
def main():
    sys_input=sys.stdin.read()
    rd,gd,bd,yd=0,0,0,0
    bulb_list=[]
    count=0
    temp_list=[]
    loop_count=0
    format_list=['','','','']
    for i in sys_input:
        if count<4:
            format_list=light_format(count,i,format_list)
        if count==4:
            count=0
            bulb_list.append(temp_list)
            temp_list=[]
            temp_list.append(i)
            format_list=light_format(count,i,format_list)
            count+=1
        else:
            temp_list.append(i)
            count+=1
    if temp_list:
        bulb_list.append(temp_list)
    for bulbs in bulb_list:
        if len(bulbs)==4:
            r,g,y,b=0,0,0,0
            for i in bulbs:
                if i=='R':
                    r+=1
                if i=='G':
                    g+=1
                if i=='Y':
                    y+=1
                if i=='B':
                    b+=1
            if not r:
                rd+=1
            if not g:
                gd+=1
            if not b:
                bd+=1
            if not y:
                yd+=1
        else:
            for i in range(0,len(bulbs)):
                if bulbs[i]=='!':
                    if format_list[0]=='R':
                        rd+=1
                    if format_list[0]=='G':
                        gd+=1
                    if format_list[0]=='B':
                        bd+=1
                    if format_list[0]=='Y':
                        yd+=1


    print(str(rd)+' '+str(bd)+' '+str(yd)+' '+str(gd))

main()

