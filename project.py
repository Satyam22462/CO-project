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
