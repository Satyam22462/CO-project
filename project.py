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
