import sys
def function1(y,dopcode,dreg,l,counting):
    s1=dopcode[y[0]]
    if(y[1] == "FLAGS"):
        error_a = "error in line:"+str(counting)+"Illegal use of FLAGS register"
        print(error_a)
        print("\n")
    elif(y[1] not in dreg):
        error_a="error in line:"+str(counting)+"Typos in register name"
        print(error_a)
        print("\n")
    elif(y[2] == "FLAGS"):
        error_a ="error in line:"+str(counting)+ "Illegal use of FLAGS register"
        print(error_a)
        print("\n")
    elif(y[2] not in dreg):
        error_a="error in line:"+str(counting)+"Typos in register name"
        print(error_a)
        print("\n")
    elif(y[1] == "FLAGS"):
        error_a = "error in line:"+str(counting)+"Illegal use of FLAGS register"
        print(error_a)
        print("\n")
    elif(y[1] not in dreg):
        error_a="error in line:"+str(counting)+"Typos in register name"
        print(error_a)
        print("\n")
    # if(y[1] == 'FLAGS' or y[2] == "FLAGS" or y[3] == "FLAGS"):
    #     error_a = "Illegal use of FLAGS register"
    #     print(error_a)
    #     print("\n")
    else:
        s2=dreg[y[1]]
        s3=dreg[y[2]]
        s4=dreg[y[3]]
        s5=16-(len(s1)+len(s2)+len(s3)+len(s4))
        s6=''
        if(s5!=0):
            for i in range(0,s5):
                s6=s6+'0'
        s7=s1+s6+s2+s3+s4
        l.append(s7)
def function4(y,dopcode,dreg,l,counting):
    s1=dopcode[y[0]]
    if(y[1] in dreg and y[1] != "FLAGS"):
        if(y[2][0]=="$"):
            s2=dreg[y[1]]

            s10=y[2][1:]
            address=int(s10)
            address2=address
            string = ""
            string2 = ""
            while (address !=0 and address>=0):
                yo = str(address%2)
                string = yo + string
                address = address//2
            
            if(address2>=0):
                if(len(string)>7):
                    error_e="error in line:"+str(counting)+"Illegal immediate value"
                    print(error_e)
                    print("\n")
                else:
                    s5=7-len(string)
                
                    if(s5!=0):
                        for i in range(0,s5):
                            string2=string2+'0'
                        string=string2+string
                    s6=16-(len(s1)+len(s2)+len(string))
                    s7=""
                    if(s6!=0):
                        for i in range(0,s6):
                            s7=s7+'0'
                    s8=s1+s7+s2+string
                    l.append(s8)
            else:
                error_e="error in line:"+str(counting)+"Illegal immediate value"
                print(error_e)
                print("\n")
        else:
            q2="error in line:"+str(counting)+"Illegal immediate value"
            print(error_e)
            print("\n")
    elif(y[1] == "FLAGS"):
        error_a ="error in line:"+str(counting)+ "Illegal use of FLAGS register"
        print(error_a)
        print("\n")
    else:
        error_a="error in line:"+str(counting)+"Typos in register name"
        print(error_a)
        print("\n")



def function5(y,dopcode,dreg,l,counting):
    s1=dopcode[y[0]]
    if(y[1] in dreg and y[1] != "FLAGS" and y[2] in dreg and y[2] != "FLAGS"):

        s2=dreg[y[1]]
        s3=dreg[y[2]]
        
        s5=16-(len(s1)+len(s2)+len(s3))
        s6=''
        if(s5!=0):
            for i in range(0,s5):
                s6=s6+'0'
        s7=s1+s6+s2+s3
        l.append(s7)
    elif(y[1] not in dreg):
        error_a="error in line:"+str(counting)+"Typos in register name"
        print(error_a)
        print("\n")
    elif(y[1] == "FLAGS"):
        error_a = "error in line:"+str(counting)+"Illegal use of FLAGS register"
        print(error_a)
        print("\n")
    elif(y[2] not in dreg):
        error_a="error in line:"+str(counting)+"Typos in register name"
        print(error_a)
        print("\n")
    elif(y[2] == "FLAGS"):
        error_a = "error in line:"+str(counting)+"Illegal use of FLAGS register"
        print(error_a)
        print("\n")

def function7(y,dopcode,l):
    s1=dopcode[y[0]]
    s2=16-len(s1)
    s3=''
    if(s2!=0):
        for i in range(0,s2):
            s3=s3+'0'
    s4=s1+s3
    l.append(s4)    

def address(address):
    string = ""
    string2 = ""
    while address == True  or address != 0:
        yo = str(address%2)
        string = yo + string
        address = address//2
    string = str(address) + string
    a = 7-len(string)
    for i in range(a):
        string2 = string2 + "0"
    string = string2 + string
    return string

def function6(y,dopcode,dict_of_labels,var,l,f,counting):#label wala
    yo = dopcode[y[0]]
    e = y[1]+":"
    flag = -1
    for i in range(len(var)):
        b = var[i][1]
        if(b == y[1]):
            flag += 1
            break
    if (flag == 0):
        error_a="error in line:"+str(counting)+"misuse of variable as label"#change
        f.append(error_a)
        #f.write("\n")
    elif(e not in dict_of_labels):
        error_a="error in line:"+str(counting)+"Use of undefined labels"
        f.append(error_a)
        #f.write("\n")
    else:
        a = yo+"0000"+address(dict_of_labels[e])
        l.append(a)
        
def loadandstore(y,dopcode,dreg,var,dict_of_labels,dict_of_instructions,l,f,counting):
    yo = dopcode[y[0]]
    flag = -1
    for i in range(len(var)):
        b = var[i][1]
        if(b == y[2]):
            flag += 1
            break
    if(y[1] == 'FLAGS'):
        error_a = "error in line:"+str(counting)+"Illegal use of FLAGS register"
        f.append(error_a)
    elif(y[1] not in dreg):
        error_a = "error in line:"+str(counting)+"Typos in register name"
        f.append(error_a)
    elif(y[2] in dict_of_labels):
        error_a="error in line:"+str(counting)+"Misuse of label as variable"
        f.append(error_a)
    elif (flag == -1):
        error_a="error in line:"+str(counting)+"Use of undefined variables"
        f.append(error_a)
    else:
        c = 0
        for i in dict_of_instructions:
            x = dict_of_instructions[i]
            if(len(x)>1 and (x[1]==y[2])):
                c += i
                a = yo+"0"+dreg[y[1]] + address(c)
                l.append(a)
                break
            else:
                pass
def mov2(y,dopcode,dreg,l,f,counting):
    yo = dopcode['mov1']
    if(y[1] == 'FLAGS'):
        error_a ="error in line:"+str(counting)+ "Illegal use of FLAGS register"
        f.append(error_a)
    if(y[1] not in dreg):
        error_a = "error in line:"+str(counting)+"Typos in register name"
        f.append(error_a)
    # elif(y[2] == 'FLAGS'):
    #     error_a = "error in line:"+str(counting)+"Illegal use of FLAGS register"
    #     f.write(error_a)
    #     f.write("\n")
    elif(y[2] not in dreg):
        error_a = "error in line:"+str(counting)+"Typos in register name"
        f.append(error_a)
    else:
        a = yo+"00000"+dreg[y[1]]+dreg[y[2]]
        l.append(a)
def mov1(y,dopcode,dreg,l,f,counting):
    yo = dopcode['mov']
    c = y[2]
    b = int(c[1:])
    if(y[1] == 'FLAGS'):
        error_a = "error in line:"+str(counting)+"Illegal use of FLAGS register"
        f.append(error_a)
    elif(y[1] not in dreg):
        error_a ="error in line:"+str(counting)+ "Typos in register name"
        f.append(error_a)
    elif(b<0 or b>127):
        error_a ="error in line:"+str(counting)+ "Illegal Immediate values"
        f.append(error_a)
    else:
        a = yo+"0"+dreg[y[1]]+address(b)
        l.append(a)
def movfinal(y,dopcode,dreg,l,f,counting):
    b = y[2]
    if(b[0] == "$"):
        mov1(y,dopcode,dreg,l,f,counting)
    elif(b.isdigit()):
        error_a = "error in line:"+str(counting)+f" {b} in not defined"
        f.append(error_a)
    else:
        mov2(y,dopcode,dreg,l,f,counting)
#dictionary of opcode
dopcode ={'add':'00000', 'sub':'00001', 'mov':'00010', 'mov1':'00011', 'ld':'00100', 'st':'00101', 'mul':'00110', 'div':'00111', 'rs':'01000', 'ls':'01001', 'xor': '01010', 'or':'01011', 'and':'01011', 'not':'01101', 'cmp':'01110', 'jmp':'01111', 'jlt':'11100', 'jgt':'11101', 'je':'11111', 'hlt':'11010'}
#dictionary of registers
dreg = {'R0' :'000','R1' :'001','R2' :'010','R3' :'011','R4' :'100','R5' :'101','R6': '110', 'FLAGS':'111'}
#file2 is ans
file2=[]





#  reads a list of strings, each item being a line
# duplicate_list_of_instructions=file.readlines()

duplicate_list_of_instructions=[]
while True:
    try:
        testline=input()
        duplicate_list_of_instructions.append(testline)
    except EOFError:
        break

flag1 = -1
flag2 = -1
for a in duplicate_list_of_instructions:
    if(a[0] == "var"):
        flag1 += 1
    elif(a[0] == "ld" or "st"):
        flag2 += 1
if(flag1 == 0 and flag2 == 0):
    pass
elif(flag1 == -1 and flag2 == 1): 
    error = "variables not declared at the beginning\n"
    print(error)
else:
    pass
# a = duplicate_list_of_instructions[0]
# b = a.split()
# if(len(b) != 0 and b[0] != "var"):
#     error = "variables not declared at the beginning\n"
#     print(error)
list_of_instructions=[]#list without any new line 
for i in range(len(duplicate_list_of_instructions)):

    if(duplicate_list_of_instructions[i]!='\n'):
        list_of_instructions.append(duplicate_list_of_instructions[i])


# print(list_of_instructions)
# print(duplicate_list_of_instructions)

# to check error number g 
# l1=(list_of_instructions[0]).split()

# if(l1[0]!='var'):
#     error_g="Variables not declared at the beginning"
#     print(error_g)
#     print("\n")





var=[]# list of list holding all types of var instructions
fl=True
i=0
while(fl):
    if(i<len(list_of_instructions)):
        l2=list_of_instructions[i].split()
        if(l2[0]=='var'):
            var.append(l2)#var.append(l2)
            i=i+1
        else:
            fl=False
    else:
        break
counting=i+1     #+(len(duplicate_list_of_instructions)-len(list_of_instructions))
# print(var)

dict_of_instructions={}
dict_of_labels={}
count=0
while(i<len(list_of_instructions)):
    
    l2=list_of_instructions[i].split()
    
    if(":" in l2[0]):
        dict_of_labels[l2[0]]=count
        l3=[]#
        for jam in range(1,len(l2)):#
            l3.append(l2[jam])#

        #if(":" in l2[0] and l2[1]=="hlt"):#
        dict_of_instructions[count]=l3
        count=count+1
        i=i+1
    else:
        dict_of_instructions[count]=l2
        count=count+1
        i=i+1

for j in range(len(var)):
    dict_of_instructions[count]=var[j]
    count=count+1
# print(dict_of_instructions)
# print(dict_of_labels) 

l=[]
variable = 0
for x,y in dict_of_instructions.items():
    
    if(y[0]=="add" or y[0]=="sub" or y[0]=="mul" or y[0]=="xor" or y[0]=="or" or y[0]=="and"):
        if(len(y)==4):#
            function1(y,dopcode,dreg,l,counting)#
            counting=counting+1
        else:#
            q1="error in line:"+str(counting)+"general syntax error"#
            print(q1)#
            print("\n") #
            counting=counting+1

    elif(y[0]=="ld" or y[0]=="st"):
        if(len(y)==3):#
            loadandstore(y,dopcode,dreg,var,dict_of_labels,dict_of_instructions,l,file2,counting)
            counting=counting+1
            
        else:#
            q1="error in line:"+str(counting)+"general syntax error"#
            print(q1)#
            print("\n") #
            counting=counting+1

    elif(y[0]=="mov"):
        if(len(y)==3):#
            movfinal(y,dopcode,dreg,l,file2,counting)
            counting=counting+1
            
        else:#
            q1="error in line:"+str(counting)+"general syntax error"#
            print(q1)#
            print("\n") #
            counting=counting+1

    elif(y[0]=="ls" or y[0]=="rs"):
        if(len(y)==3):#
            function4(y,dopcode,dreg,l,counting)
            counting=counting+1
            
        else:#
            q1="error in line:"+str(counting)+"general syntax error"#
            print(q1)#
            print("\n") #
            counting=counting+1

    elif(y[0]=="cmp"or y[0]=="div" or y[0]=="not"):
        
        if(len(y)==3):#
            function5(y,dopcode,dreg,l,counting)
            counting=counting+1
            
        else:#
            q1="error in line:"+str(counting)+"general syntax error"#
            print(q1)#
            print("\n") #
            counting=counting+1

    elif(y[0]=="jlt"or y[0]=="jmp" or y[0]=="jgt" or y[0]=="je"):
        if(len(y)==2):#
            function6(y,dopcode,dict_of_labels,var,l,file2,counting)
            counting=counting+1
            
        else:#
            q1="error in line:"+str(counting)+"general syntax error"#
            print(q1)#
            print("\n") #
            counting=counting+1

    elif(y[0]=="hlt"):
        function7(y,dopcode,l)
        variable=variable + x+1
        # print(variable)
        counting=counting+1
        break
    elif(y[0]=="var"):#
        break#

    else:
        error_a="error in line:"+str(counting)+"Typos in instruction name"
        print(error_a)
        print("\n")
        counting=counting+1
  
variable1=dict_of_instructions.values()                        
if (['hlt'] not in variable1 and (len(file2) !=0)):
    error_h="Missing hlt instruction"
    print(error_h)
    print("\n")

else:
    if(variable<len(dict_of_instructions)):
    
        variable2=dict_of_instructions[variable]
        if(variable2[0]=="add" or variable2[0]=="sub" or variable2[0]=="mul" or variable2[0]=="xor" or variable2[0]=="or" or variable2[0]=="and" or variable2[0]=="ld" or variable2[0]=="st" or variable2[0]=="mov" or variable2[0]=="ls" or variable2[0]=="rs" or variable2[0]=="cmp"or variable2[0]=="div" or variable2[0]=="not" or variable2[0]=="jlt" or variable2[0]=="jmp" or variable2[0]=="jgt" or variable2[0]=="je" or len(dict_of_instructions)-variable!=len(var)):
            error_i="error in line:"+str(counting)+"hlt not being used as the last instruction"
            print(error_i)
            print("\n")
            sys.exit() 
# print(l)
# for i in range(0,len(file2)):
#     print(file2[i])
#     print("\n")
if(len(file2) != 0):
    for i in range(0,len(file2)):
        print(file2[i])
        print("\n")
else:
    for i in l:
        print(i)
        print("\n")
# finished_file1=open("output.txt","r")
# listing=finished_file1.readlines()
# finished_file1.close()
# finished_file=open("output.txt","a")
# if(listing==[]):
#     for m in l:
#         finished_file.write(m)
#         finished_file.write("\n")
# finished_file.close()
