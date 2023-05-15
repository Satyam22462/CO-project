file=open("input.txt","r")
file2=open("output.txt",'w')




def function1(y,dopcode,dreg,l,counting):
    s1=dopcode[y[0]]
    if(y[1] == "FLAGS"):
        error_a = "error in line:"+str(counting)+"Illegal use of FLAGS register"
        file2.write(error_a)
        file2.write("\n")
    elif(y[1] not in dreg):
        error_a="error in line:"+str(counting)+"Typos in register name"
        file2.write(error_a)
        file2.write("\n")
    elif(y[2] == "FLAGS"):
        error_a ="error in line:"+str(counting)+ "Illegal use of FLAGS register"
        file2.write(error_a)
        file2.write("\n")
    elif(y[2] not in dreg):
        error_a="error in line:"+str(counting)+"Typos in register name"
        file2.write(error_a)
        file2.write("\n")
    elif(y[1] == "FLAGS"):
        error_a = "error in line:"+str(counting)+"Illegal use of FLAGS register"
        file2.write(error_a)
        file2.write("\n")
    elif(y[1] not in dreg):
        error_a="error in line:"+str(counting)+"Typos in register name"
        file2.write(error_a)
        file2.write("\n")
    # if(y[1] == 'FLAGS' or y[2] == "FLAGS" or y[3] == "FLAGS"):
    #     error_a = "Illegal use of FLAGS register"
    #     file2.write(error_a)
    #     file2.write("\n")
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
                    file2.write(error_e)
                    file2.write("\n")
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
                file2.write(error_e)
                file2.write("\n")
        else:
            q2="error in line:"+str(counting)+"Illegal immediate value"
            file2.write(error_e)
            file2.write("\n")
    elif(y[1] == "FLAGS"):
        error_a ="error in line:"+str(counting)+ "Illegal use of FLAGS register"
        file2.write(error_a)
        file2.write("\n")
    else:
        error_a="error in line:"+str(counting)+"Typos in register name"
        file2.write(error_a)
        file2.write("\n")
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
        file2.write(error_a)
        file2.write("\n")
    elif(y[1] == "FLAGS"):
        error_a = "error in line:"+str(counting)+"Illegal use of FLAGS register"
        file2.write(error_a)
        file2.write("\n")
    elif(y[2] not in dreg):
        error_a="error in line:"+str(counting)+"Typos in register name"
        file2.write(error_a)
        file2.write("\n")
    elif(y[2] == "FLAGS"):
        error_a = "error in line:"+str(counting)+"Illegal use of FLAGS register"
        file2.write(error_a)
        file2.write("\n")
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
    while address == True or address != 0:
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
        f.write(error_a)
        f.write("\n")
    elif(e not in dict_of_labels):
        error_a="error in line:"+str(counting)+"Use of undefined labels"
        f.write(error_a)
        f.write("\n")
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
        f.write(error_a)
        f.write("\n")
    elif(y[1] not in dreg):
        error_a = "error in line:"+str(counting)+"Typos in register name"
        f.write(error_a)
        f.write("\n")
    elif(y[2] in dict_of_labels):
        error_a="error in line:"+str(counting)+"Misuse of label as variable"
        f.write(error_a)
        f.write("\n")
    elif (flag == -1):
        error_a="error in line:"+str(counting)+"Use of undefined variables"
        f.write(error_a)
        f.write("\n")
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
        f.write(error_a)
        f.write("\n")
    if(y[1] not in dreg):
        error_a = "error in line:"+str(counting)+"Typos in register name"
        f.write(error_a)
        f.write("\n")
    # elif(y[2] == 'FLAGS'):
    #     error_a = "error in line:"+str(counting)+"Illegal use of FLAGS register"
    #     f.write(error_a)
    #     f.write("\n")
    elif(y[2] not in dreg):
        error_a = "error in line:"+str(counting)+"Typos in register name"
        f.write(error_a)
        f.write("\n")
    else:
        a = yo+"00000"+dreg[y[1]]+dreg[y[2]]
        l.append(a)
def mov1(y,dopcode,dreg,l,f,counting):
    yo = dopcode['mov']
    c = y[2]
    b = int(c[1:])
    if(y[1] == 'FLAGS'):
        error_a = "error in line:"+str(counting)+"Illegal use of FLAGS register"
        f.write(error_a)
        f.write("\n")
    elif(y[1] not in dreg):
        error_a ="error in line:"+str(counting)+ "Typos in register name"
        f.write(error_a)
        f.write("\n")
    elif(b<0 or b>127):
        error_a ="error in line:"+str(counting)+ "Illegal Immediate values"
        f.write(error_a)
        f.write("\n")
    else:
        a = yo+"0"+dreg[y[1]]+address(b)
        l.append(a)
def movfinal(y,dopcode,dreg,l,f,counting):
    b = y[2]
    if(b[0] == "$"):
        mov1(y,dopcode,dreg,l,f,counting)
    elif(b.isdigit()):
        error_a = "error in line:"+str(counting)+f" {b} in not defined"
        f.write(error_a)
        f.write("\n")
    else:
        mov2(y,dopcode,dreg,l,f,counting)
#dictionary of opcode
dopcode ={'add':'00000', 'sub':'00001', 'mov':'00010', 'mov1':'00011', 'ld':'00100', 'st':'00101', 'mul':'00110', 'div':'00111', 'rs':'01000', 'ls':'01001', 'xor': '01010', 'or':'01011', 'and':'01011', 'not':'01101', 'cmp':'01110', 'jmp':'01111', 'jlt':'11100', 'jgt':'11101', 'je':'11111', 'hlt':'11010'}
#dictionary of registers
dreg = {'R0' :'000','R1' :'001','R2' :'010','R3' :'011','R4' :'100','R5' :'101','R6': '110', 'FLAGS':'111'}
#  reads a list of strings, each item being a line
duplicate_list_of_instructions=file.readlines()
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
    file2.write(error)
else:
    pass
# a = duplicate_list_of_instructions[0]
# b = a.split()
# if(len(b) != 0 and b[0] != "var"):
#     error = "variables not declared at the beginning\n"
#     file2.write(error)
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
#     file2.write(error_g)
#     file2.write("\n")

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
