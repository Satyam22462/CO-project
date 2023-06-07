def converting_binary_to_decimal(l):
    final=0
    j=15
    for i in range(0,16):
        final=final+(2**i)*int(l[j])
        j=j-1
    return final
def converting_binary_to_decimal_7_bit(l):
    final=0
    j=6
    for i in range(0,7):
        final=final+(2**i)*int(l[j])
        j=j-1
    return final

def converting_decimal_to_binary(m):
    address=int(m) 
    string = ""
    while (address !=0 and address>=0):
        yo = str(address%2)
        string = yo + string
        address = address//2
    z=16-len(string)
    for i in range(z):
        string="0"+string
    return string
def converting_decimal_to_binary_7_bit(m):
    address=int(m) 
    string = ""
    while (address !=0 and address>=0):
        yo = str(address%2)
        string = yo + string
        address = address//2
    z=7-len(string)
    for i in range(z):
        string="0"+string
    return string


def movIm(instruction, R0, R1, R2, R3, R4, R5, R6, FLAGS, dreg2):
    s1 = dreg2[instruction[6:9]]
    if(s1 == 'R0'):
        R0.clear()
        R0.append('000000000'+instruction[9:])
    elif(s1 == 'R1'):
        R1.clear()
        R1.append('000000000'+instruction[9:])
    elif(s1 == 'R2'):
        R2.clear()
        R2.append('000000000'+instruction[9:])
    elif(s1 == 'R3'):
        R3.clear()
        R3.append('000000000'+instruction[9:])
    elif(s1 == 'R4'):
        R4.clear()
        R4.append('000000000'+instruction[9:])
    elif(s1 == 'R5'):
        R5.clear()
        R5.append('000000000'+instruction[9:])
    elif(s1 == 'R6'):
        R6.clear()
        R6.append('000000000'+instruction[9:])
    FLAGS.clear()
    FLAGS.append('0000000000000000')
def movRegister(instruction, R0, R1, R2, R3, R4, R5, R6, FLAGS, dreg2):
    s1 = dreg2[instruction[10:13]]
    s2 = dreg2[instruction[13:]]
    if(s1 == 'R0'):
        if(s2 == 'R1'):
            R0.clear()
            R0.append(R1[0])
        elif(s2 == 'R2'):
            R0.clear()
            R0.append(R2[0])
        elif(s2 == 'R3'):
            R0.clear()
            R0.append(R3[0])
        elif(s2 == 'R4'):
            R0.clear()
            R0.append(R4[0])
        elif(s2 == 'R5'):
            R0.clear()
            R0.append(R5[0])
        elif(s2 == 'R6'):
            R0.clear()
            R0.append(R6[0])
        elif(s2 == 'FLAGS'):
            R0.clear()
            R0.append(FLAGS[0])
    if(s1 == 'R1'):
        if(s2 == 'R0'):
            R1.clear()
            R1.append(R0[0])
        elif(s2 == 'R2'):
            R1.clear()
            R1.append(R2[0])
        elif(s2 == 'R3'):
            R1.clear()
            R1.append(R3[0])
        elif(s2 == 'R4'):
            R1.clear()
            R1.append(R4[0])
        elif(s2 == 'R5'):
            R1.clear()
            R1.append(R5[0])
        elif(s2 == 'R6'):
            R1.clear()
            R1.append(R6[0])
        elif(s2 == 'FLAGS'):
            R1.clear()
            R1.append(FLAGS[0])
    if(s1 == 'R2'):
        if(s2 == 'R1'):
            R2.clear()
            R2.append(R1[0])
        elif(s2 == 'R0'):
            R2.clear()
            R2.append(R0[0])
        elif(s2 == 'R3'):
            R2.clear()
            R1.append(R3[0])
        elif(s2 == 'R4'):
            R2.clear()
            R2.append(R4[0])
        elif(s2 == 'R5'):
            R2.clear()
            R2.append(R5[0])
        elif(s2 == 'R6'):
            R2.clear()
            R2.append(R6[0])
        elif(s2 == 'FLAGS'):
            R2.clear()
            R2.append(FLAGS[0])
    if(s1 == 'R3'):
        if(s2 == 'R0'):
            R3.clear()
            R3.append(R0[0])
        elif(s2 == 'R2'):
            R3.clear()
            R3.append(R2[0])
        elif(s2 == 'R1'):
            R3.clear()
            R3.append(R1[0])
        elif(s2 == 'R4'):
            R3.clear()
            R3.append(R4[0])
        elif(s2 == 'R5'):
            R3.clear()
            R3.append(R5[0])
        elif(s2 == 'R6'):
            R3.clear()
            R3.append(R6[0])
        elif(s2 == 'FLAGS'):
            R3.clear()
            R3.append(FLAGS[0])
    if(s1 == 'R4'):
        if(s2 == 'R0'):
            R4.clear()
            R4.append(R0[0])
        elif(s2 == 'R2'):
            R4.clear()
            R4.append(R2[0])
        elif(s2 == 'R3'):
            R4.clear()
            R4.append(R3[0])
        elif(s2 == 'R1'):
            R4.clear()
            R4.append(R1[0])
        elif(s2 == 'R5'):
            R4.clear()
            R4.append(R5[0])
        elif(s2 == 'R6'):
            R4.clear()
            R4.append(R6[0])
        elif(s2 == 'FLAGS'):
            R4.clear()
            R4.append(FLAGS[0])
    if(s1 == 'R5'):
        if(s2 == 'R0'):
            R5.clear()
            R5.append(R0[0])
        elif(s2 == 'R2'):
            R5.clear()
            R5.append(R2[0])
        elif(s2 == 'R3'):
            R5.clear()
            R5.append(R3[0])
        elif(s2 == 'R4'):
            R5.clear()
            R5.append(R4[0])
        elif(s2 == 'R1'):
            R5.clear()
            R5.append(R1[0])
        elif(s2 == 'R6'):
            R5.clear()
            R5.append(R6[0])
        elif(s2 == 'FLAGS'):
            R5.clear()
            R5.append(FLAGS[0])
    if(s1 == 'R6'):
        if(s2 == 'R0'):
            R6.clear()
            R6.append(R0[0])
        elif(s2 == 'R2'):
            R6.clear()
            R6.append(R2[0])
        elif(s2 == 'R3'):
            R6.clear()
            R6.append(R3[0])
        elif(s2 == 'R4'):
            R6.clear()
            R6.append(R4[0])
        elif(s2 == 'R5'):
            R6.clear()
            R5.append(R5[0])
        elif(s2 == 'R1'):
            R6.clear()
            R6.append(R1[0])
        elif(s2 == 'FLAGS'):
            R6.clear()
            R6.append(FLAGS[0])
    FLAGS.clear()
    FLAGS.append('0000000000000000')
def load(instruction, R0, R1, R2, R3, R4, R5, R6, FLAGS, dreg2, list):
    s1 = dreg2[instruction[6:9]]
    s2 = instruction[9:]
    a = converting_binary_to_decimal_7_bit(s2)
    string = list[a]
    if(s1 == 'R0'):
        R0.clear()
        R0.append(string)
    elif(s1 == 'R1'):
        R1.clear()
        R1.append(string)
    elif(s1 == 'R2'):
        R2.clear()
        R2.append(string)
    elif(s1 == 'R3'):
        R3.clear()
        R3.append(string)
    elif(s1 == 'R4'):
        R4.clear()
        R4.append(string)
    elif(s1 == 'R5'):
        R5.clear()
        R5.append(string)
    elif(s1 == 'R6'):
        R6.clear()
        R6.append(string)
    FLAGS.clear()
    FLAGS.append('0000000000000000')
def Store(instruction, R0, R1, R2, R3, R4, R5, R6, FLAGS, dreg2, list):
    s1 = dreg2[instruction[6:9]]
    s2 = instruction[9:]
    a = converting_binary_to_decimal_7_bit(s2)
    if(s1 == 'R0'):
        list[a] = R0[0]
    elif(s1 == 'R1'):
        list[a] = R1[0]
    elif(s1 == 'R2'):
        list[a] = R2[0]
    elif(s1 == 'R3'):
        list[a] = R3[0]
    elif(s1 == 'R4'):
        list[a] = R4[0]
    elif(s1 == 'R5'):
        list[a] = R5[0]
    elif(s1 == 'R6'):
        list[a] = R6[0]
    FLAGS.clear()
    FLAGS.append('0000000000000000')
def Right_shift(instruction, R0, R1, R2, R3, R4, R5, R6, FLAGS, dreg2):
    s1 = dreg2[instruction[6:9]]
    s2 = instruction[9:]
    a = converting_binary_to_decimal_7_bit(s2)
    if(s1 == 'R0'):
        d = R0[0]
        for i in range(a):
            d = '0'+d
        e =len(d) - a
        s3 = d[0:e]
        R0.clear()
        R0.append(s3)
    elif(s1 == 'R1'):
        d = R1[0]
        for i in range(a):
            d = '0'+d
        e =len(d) - a
        s3 = d[0:e]
        R1.clear()
        R1.append(s3)
    elif(s1 == 'R2'):
        d = R2[0]
        for i in range(a):
            d = '0'+d
        e =len(d) - a
        s3 = d[0:e]
        R2.clear()
        R2.append(s3)
    elif(s1 == 'R3'):
        d = R3[0]
        for i in range(a):
            d = '0'+d
        e =len(d) - a
        s3 = d[0:e]
        R3.clear()
        R3.append(s3)
    elif(s1 == 'R4'):
        d = R4[0]
        for i in range(a):
            d = '0'+d
        e =len(d) - a
        s3 = d[0:e]
        R4.clear()
        R4.append(s3)
    elif(s1 == 'R5'):
        d = R5[0]
        for i in range(a):
            d = '0'+d
        e =len(d) - a
        s3 = d[0:e]
        R5.clear()
        R5.append(s3)
    elif(s1 == 'R6'):
        d = R6[0]
        for i in range(a):
            d = '0'+d
        e =len(d) - a
        s3 = d[0:e]
        R6.clear()
        R6.append(s3)
    FLAGS.clear()
    FLAGS.append('0000000000000000')
def left_shift(instruction, R0, R1, R2, R3, R4, R5, R6, FLAGS, dreg2):
    s1 = dreg2[instruction[6:9]]
    s2 = instruction[9:]
    a = converting_binary_to_decimal_7_bit(s2)
    if(s1 == 'R0'):
        d = R0[0]
        for i in range(a):
            d = d + '0'
        e =len(d) - a
        s3 = d[0:e]
        R0.clear()
        R0.append(s3)
    elif(s1 == 'R1'):
        d = R0[0]
        for i in range(a):
            d = d + '0'
        e =len(d) - a
        s3 = d[0:e]
        R1.clear()
        R1.append(s3)
    elif(s1 == 'R2'):
        d = R0[0]
        for i in range(a):
            d = d + '0'
        e =len(d) - a
        s3 = d[0:e]
        R2.clear()
        R2.append(s3)
    elif(s1 == 'R3'):
        d = R0[0]
        for i in range(a):
            d = d + '0'
        e =len(d) - a
        s3 = d[0:e]
        R3.clear()
        R3.append(s3)
    elif(s1 == 'R4'):
        d = R0[0]
        for i in range(a):
            d = d + '0'
        e =len(d) - a
        s3 = d[0:e]
        R4.clear()
        R4.append(s3)
    elif(s1 == 'R5'):
        d = R0[0]
        for i in range(a):
            d = d + '0'
        e =len(d) - a
        s3 = d[0:e]
        R5.clear()
        R5.append(s3)
    elif(s1 == 'R6'):
        d = R0[0]
        for i in range(a):
            d = d + '0'
        e =len(d) - a
        s3 = d[0:e]
        R6.clear()
        R6.append(s3)
    FLAGS.clear()
    FLAGS.append('0000000000000000')
def UnconditionalJump(instruction, pc):
    s1 = instruction[9:]
    pc = converting_binary_to_decimal_7_bit(s1)
    return pc


def add(instruction,R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2):
    s1=dreg2[instruction[10:13]]
    s2=dreg2[instruction[13:16]]
    s7=dreg2[instruction[7:10]]
    
    
    if(s1[-1]=='0'):
        s3=converting_binary_to_decimal(R0[0])
    elif(s1[-1]=='1'):
        s3=converting_binary_to_decimal(R1[0])
    elif(s1[-1]=='2'):
        s3=converting_binary_to_decimal(R2[0])
    elif(s1[-1]=='3'):
        s3=converting_binary_to_decimal(R3[0])
    elif(s1[-1]=='4'):
        s3=converting_binary_to_decimal(R4[0])
    elif(s1[-1]=='5'):
        s3=converting_binary_to_decimal(R5[0])
    elif(s1[-1]=='6'):
        s3=converting_binary_to_decimal(R6[0])
    if(s2[-1]=='0'):
        s4=converting_binary_to_decimal(R0[0])
    elif(s2[-1]=='1'):
        s4=converting_binary_to_decimal(R1[0])
    elif(s2[-1]=='2'):
        s4=converting_binary_to_decimal(R2[0])
    elif(s2[-1]=='3'):
        s4=converting_binary_to_decimal(R3[0])
    elif(s2[-1]=='4'):
        s4=converting_binary_to_decimal(R4[0])
    elif(s2[-1]=='5'):
        s4=converting_binary_to_decimal(R5[0])
    elif(s2[-1]=='6'):
        s4=converting_binary_to_decimal(R6[0])

    s5=s4+s3
    s6=converting_decimal_to_binary(s5)
    if(len(s6)==16):
        if(s7[-1]=='0'):
            R0.clear()
            R0.append(s6)
        elif(s7[-1]=='1'):
            R1.clear()
            R1.append(s6)
        elif(s7[-1]=='2'):
            R2.clear()
            R2.append(s6)
        elif(s7[-1]=='3'):
            R3.clear()
            R3.append(s6)
        elif(s7[-1]=='4'):
            R4.clear()
            R4.append(s6)
        elif(s7[-1]=='5'):
            R6.clear()
            R6.append(s6)
        elif(s7[-1]=='6'):
            R6.clear()
            R6.append(s6)
        FLAGS.clear()
        FLAGS.append('0000000000000000')
        
    else:
        if(s7[-1]=='0'):
            R0.clear()
            R0.append('0000000000000000')
    
        elif(s7[-1]=='1'):
            R1.clear()
            R1.append('0000000000000000')
        elif(s7[-1]=='2'):
            R2.clear()
            R2.append('0000000000000000')
            
        elif(s7[-1]=='3'):
            
            R3.clear()
            R3.append('0000000000000000')
        elif(s7[-1]=='4'):
            
            R4.clear()
            R4.append('0000000000000000')
        elif(s7[-1]=='5'):
            
            R5.clear()
            R5.append('0000000000000000')
        elif(s7[-1]=='6'):
            
            R6.clear()
            R6.append('0000000000000000')
        FLAGS.clear()
        FLAGS.append('0000000000001000')

def sub(instruction,R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2):
    s1=dreg2[instruction[10:13]]
    s2=dreg2[instruction[13:16]]
    s7=dreg2[instruction[7:10]]
    
    
    if(s1[-1]=='0'):
        s3=converting_binary_to_decimal(R0[0])
    elif(s1[-1]=='1'):
        s3=converting_binary_to_decimal(R1[0])
    elif(s1[-1]=='2'):
        s3=converting_binary_to_decimal(R2[0])
    elif(s1[-1]=='3'):
        s3=converting_binary_to_decimal(R3[0])
    elif(s1[-1]=='4'):
        s3=converting_binary_to_decimal(R4[0])
    elif(s1[-1]=='5'):
        s3=converting_binary_to_decimal(R5[0])
    elif(s1[-1]=='6'):
        s3=converting_binary_to_decimal(R6[0])
    if(s2[-1]=='0'):
        s4=converting_binary_to_decimal(R0[0])
    elif(s2[-1]=='1'):
        s4=converting_binary_to_decimal(R1[0])
    elif(s2[-1]=='2'):
        s4=converting_binary_to_decimal(R2[0])
    elif(s2[-1]=='3'):
        s4=converting_binary_to_decimal(R3[0])
    elif(s2[-1]=='4'):
        s4=converting_binary_to_decimal(R4[0])
    elif(s2[-1]=='5'):
        s4=converting_binary_to_decimal(R5[0])
    elif(s2[-1]=='6'):
        s4=converting_binary_to_decimal(R6[0])

    s5=s4-s3
    
    
    if(s5<0):
        if(s7[-1]=='0'):
            R0.clear()
            R0.append('0000000000000000')
    
        elif(s7[-1]=='1'):
            R1.clear()
            R1.append('0000000000000000')
        elif(s7[-1]=='2'):
            R2.clear()
            R2.append('0000000000000000')
            
        elif(s7[-1]=='3'):
            
            R3.clear()
            R3.append('0000000000000000')
        elif(s7[-1]=='4'):
            
            R4.clear()
            R4.append('0000000000000000')
        elif(s7[-1]=='5'):
            
            R5.clear()
            R5.append('0000000000000000')
        elif(s7[-1]=='6'):
            
            R6.clear()
            R6.append('0000000000000000')
        FLAGS.clear()
        FLAGS.append('0000000000001000')
    else:
        s6=converting_decimal_to_binary(s5)

        if(s7[-1]=='0'):
            R0.clear()
            R0.append(s6)
        elif(s7[-1]=='1'):
            R1.clear()
            R1.append(s6)
        elif(s7[-1]=='2'):
            R2.clear()
            R2.append(s6)
        elif(s7[-1]=='3'):
            R3.clear()
            R3.append(s6)
        elif(s7[-1]=='4'):
            R4.clear()
            R4.append(s6)
        elif(s7[-1]=='5'):
            R6.clear()
            R6.append(s6)
        elif(s7[-1]=='6'):
            R6.clear()
            R6.append(s6)
        FLAGS.clear()
        FLAGS.append('0000000000000000')

def mul(instruction,R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2):
    s1=dreg2[instruction[10:13]]
    s2=dreg2[instruction[13:16]]
    s7=dreg2[instruction[7:10]]
    
    
    if(s1[-1]=='0'):
        s3=converting_binary_to_decimal(R0[0])
    elif(s1[-1]=='1'):
        s3=converting_binary_to_decimal(R1[0])
    elif(s1[-1]=='2'):
        s3=converting_binary_to_decimal(R2[0])
    elif(s1[-1]=='3'):
        s3=converting_binary_to_decimal(R3[0])
    elif(s1[-1]=='4'):
        s3=converting_binary_to_decimal(R4[0])
    elif(s1[-1]=='5'):
        s3=converting_binary_to_decimal(R5[0])
    elif(s1[-1]=='6'):
        s3=converting_binary_to_decimal(R6[0])
    if(s2[-1]=='0'):
        s4=converting_binary_to_decimal(R0[0])
    elif(s2[-1]=='1'):
        s4=converting_binary_to_decimal(R1[0])
    elif(s2[-1]=='2'):
        s4=converting_binary_to_decimal(R2[0])
    elif(s2[-1]=='3'):
        s4=converting_binary_to_decimal(R3[0])
    elif(s2[-1]=='4'):
        s4=converting_binary_to_decimal(R4[0])
    elif(s2[-1]=='5'):
        s4=converting_binary_to_decimal(R5[0])
    elif(s2[-1]=='6'):
        s4=converting_binary_to_decimal(R6[0])

    s5=s4*s3
    s6=converting_decimal_to_binary(s5)
    if(len(s6)==16):
        if(s7[-1]=='0'):
            R0.clear()
            R0.append(s6)
        elif(s7[-1]=='1'):
            R1.clear()
            R1.append(s6)
        elif(s7[-1]=='2'):
            R2.clear()
            R2.append(s6)
        elif(s7[-1]=='3'):
            R3.clear()
            R3.append(s6)
        elif(s7[-1]=='4'):
            R4.clear()
            R4.append(s6)
        elif(s7[-1]=='5'):
            R6.clear()
            R6.append(s6)
        elif(s7[-1]=='6'):
            R6.clear()
            R6.append(s6)
        FLAGS.clear()
        FLAGS.append('0000000000000000')
        
    else:
        if(s7[-1]=='0'):
            R0.clear()
            R0.append('0000000000000000')
    
        elif(s7[-1]=='1'):
            R1.clear()
            R1.append('0000000000000000')
        elif(s7[-1]=='2'):
            R2.clear()
            R2.append('0000000000000000')
            
        elif(s7[-1]=='3'):
            
            R3.clear()
            R3.append('0000000000000000')
        elif(s7[-1]=='4'):
            
            R4.clear()
            R4.append('0000000000000000')
        elif(s7[-1]=='5'):
            
            R5.clear()
            R5.append('0000000000000000')
        elif(s7[-1]=='6'):
            
            R6.clear()
            R6.append('0000000000000000')
        FLAGS.clear()
        FLAGS.append('0000000000001000')
def xor(instruction,R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2):
    s1=dreg2[instruction[10:13]]
    s2=dreg2[instruction[13:16]]
    s7=dreg2[instruction[7:10]]
    
    
    if(s1[-1]=='0'):
        s3=converting_binary_to_decimal(R0[0])
    elif(s1[-1]=='1'):
        s3=converting_binary_to_decimal(R1[0])
    elif(s1[-1]=='2'):
        s3=converting_binary_to_decimal(R2[0])
    elif(s1[-1]=='3'):
        s3=converting_binary_to_decimal(R3[0])
    elif(s1[-1]=='4'):
        s3=converting_binary_to_decimal(R4[0])
    elif(s1[-1]=='5'):
        s3=converting_binary_to_decimal(R5[0])
    elif(s1[-1]=='6'):
        s3=converting_binary_to_decimal(R6[0])
    if(s2[-1]=='0'):
        s4=converting_binary_to_decimal(R0[0])
    elif(s2[-1]=='1'):
        s4=converting_binary_to_decimal(R1[0])
    elif(s2[-1]=='2'):
        s4=converting_binary_to_decimal(R2[0])
    elif(s2[-1]=='3'):
        s4=converting_binary_to_decimal(R3[0])
    elif(s2[-1]=='4'):
        s4=converting_binary_to_decimal(R4[0])
    elif(s2[-1]=='5'):
        s4=converting_binary_to_decimal(R5[0])
    elif(s2[-1]=='6'):
        s4=converting_binary_to_decimal(R6[0])

    s5=s4^s3
    s6=converting_decimal_to_binary(s5)
    
    if(s7[-1]=='0'):
        R0.clear()
        R0.append(s6)
    elif(s7[-1]=='1'):
        R1.clear()
        R1.append(s6)
    elif(s7[-1]=='2'):
        R2.clear()
        R2.append(s6)
    elif(s7[-1]=='3'):
        R3.clear()
        R3.append(s6)
    elif(s7[-1]=='4'):
        R4.clear()
        R4.append(s6)
    elif(s7[-1]=='5'):
        R6.clear()
        R6.append(s6)
    elif(s7[-1]=='6'):
        R6.clear()
        R6.append(s6)
    FLAGS.clear()
    FLAGS.append('0000000000000000')

def orkaro(instruction,R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2):

    s1=dreg2[instruction[10:13]]
    s2=dreg2[instruction[13:16]]
    s7=dreg2[instruction[7:10]]
    
    
    if(s1[-1]=='0'):
        s3=converting_binary_to_decimal(R0[0])
    elif(s1[-1]=='1'):
        s3=converting_binary_to_decimal(R1[0])
    elif(s1[-1]=='2'):
        s3=converting_binary_to_decimal(R2[0])
    elif(s1[-1]=='3'):
        s3=converting_binary_to_decimal(R3[0])
    elif(s1[-1]=='4'):
        s3=converting_binary_to_decimal(R4[0])
    elif(s1[-1]=='5'):
        s3=converting_binary_to_decimal(R5[0])
    elif(s1[-1]=='6'):
        s3=converting_binary_to_decimal(R6[0])
    if(s2[-1]=='0'):
        s4=converting_binary_to_decimal(R0[0])
    elif(s2[-1]=='1'):
        s4=converting_binary_to_decimal(R1[0])
    elif(s2[-1]=='2'):
        s4=converting_binary_to_decimal(R2[0])
    elif(s2[-1]=='3'):
        s4=converting_binary_to_decimal(R3[0])
    elif(s2[-1]=='4'):
        s4=converting_binary_to_decimal(R4[0])
    elif(s2[-1]=='5'):
        s4=converting_binary_to_decimal(R5[0])
    elif(s2[-1]=='6'):
        s4=converting_binary_to_decimal(R6[0])

    s5=s4|s3
    s6=converting_decimal_to_binary(s5)
    
    if(s7[-1]=='0'):
        R0.clear()
        R0.append(s6)
    elif(s7[-1]=='1'):
        R1.clear()
        R1.append(s6)
    elif(s7[-1]=='2'):
        R2.clear()
        R2.append(s6)
    elif(s7[-1]=='3'):
        R3.clear()
        R3.append(s6)
    elif(s7[-1]=='4'):
        R4.clear()
        R4.append(s6)
    elif(s7[-1]=='5'):
        R6.clear()
        R6.append(s6)
    elif(s7[-1]=='6'):
        R6.clear()
        R6.append(s6)
    FLAGS.clear()
    FLAGS.append('0000000000000000')
    
def andkaro(instruction,R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2):

    s1=dreg2[instruction[10:13]]
    s2=dreg2[instruction[13:16]]
    s7=dreg2[instruction[7:10]]
    
    
    if(s1[-1]=='0'):
        s3=converting_binary_to_decimal(R0[0])
    elif(s1[-1]=='1'):
        s3=converting_binary_to_decimal(R1[0])
    elif(s1[-1]=='2'):
        s3=converting_binary_to_decimal(R2[0])
    elif(s1[-1]=='3'):
        s3=converting_binary_to_decimal(R3[0])
    elif(s1[-1]=='4'):
        s3=converting_binary_to_decimal(R4[0])
    elif(s1[-1]=='5'):
        s3=converting_binary_to_decimal(R5[0])
    elif(s1[-1]=='6'):
        s3=converting_binary_to_decimal(R6[0])
    if(s2[-1]=='0'):
        s4=converting_binary_to_decimal(R0[0])
    elif(s2[-1]=='1'):
        s4=converting_binary_to_decimal(R1[0])
    elif(s2[-1]=='2'):
        s4=converting_binary_to_decimal(R2[0])
    elif(s2[-1]=='3'):
        s4=converting_binary_to_decimal(R3[0])
    elif(s2[-1]=='4'):
        s4=converting_binary_to_decimal(R4[0])
    elif(s2[-1]=='5'):
        s4=converting_binary_to_decimal(R5[0])
    elif(s2[-1]=='6'):
        s4=converting_binary_to_decimal(R6[0])

    s5=s4&s3
    s6=converting_decimal_to_binary(s5)
    
    if(s7[-1]=='0'):
        R0.clear()
        R0.append(s6)
    elif(s7[-1]=='1'):
        R1.clear()
        R1.append(s6)
    elif(s7[-1]=='2'):
        R2.clear()
        R2.append(s6)
    elif(s7[-1]=='3'):
        R3.clear()
        R3.append(s6)
    elif(s7[-1]=='4'):
        R4.clear()
        R4.append(s6)
    elif(s7[-1]=='5'):
        R6.clear()
        R6.append(s6)
    elif(s7[-1]=='6'):
        R6.clear()
        R6.append(s6)
    FLAGS.clear()
    FLAGS.append('0000000000000000')  

def divide(instruction,R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2):
    s1=dreg2[instruction[10:13]]
    s2=dreg2[instruction[13:16]]
    
    
    
    if(s1[-1]=='0'):
        s3=converting_binary_to_decimal(R0[0])
    elif(s1[-1]=='1'):
        s3=converting_binary_to_decimal(R1[0])
    elif(s1[-1]=='2'):
        s3=converting_binary_to_decimal(R2[0])
    elif(s1[-1]=='3'):
        s3=converting_binary_to_decimal(R3[0])
    elif(s1[-1]=='4'):
        s3=converting_binary_to_decimal(R4[0])
    elif(s1[-1]=='5'):
        s3=converting_binary_to_decimal(R5[0])
    elif(s1[-1]=='6'):
        s3=converting_binary_to_decimal(R6[0])
    if(s2[-1]=='0'):
        s4=converting_binary_to_decimal(R0[0])
    elif(s2[-1]=='1'):
        s4=converting_binary_to_decimal(R1[0])
    elif(s2[-1]=='2'):
        s4=converting_binary_to_decimal(R2[0])
    elif(s2[-1]=='3'):
        s4=converting_binary_to_decimal(R3[0])
    elif(s2[-1]=='4'):
        s4=converting_binary_to_decimal(R4[0])
    elif(s2[-1]=='5'):
        s4=converting_binary_to_decimal(R5[0])
    elif(s2[-1]=='6'):
        s4=converting_binary_to_decimal(R6[0])

    if(s4==0):
        R0.clear()
        R0.append('0000000000000000')
        R1.clear()
        R1.append('0000000000000000')
        FLAGS.clear()
        FLAGS.append('0000000000001000')
    else:
        s5=s3//s4
        s6=converting_decimal_to_binary(s5)
        R0.clear()
        R0.append(s6)
        s7=s3%s4
        s8=converting_decimal_to_binary(s7)
        
        R1.clear()
        R1.append(s8)
        FLAGS.clear()
        FLAGS.append('0000000000000000')
def notkar(instruction,R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2):
    s1=dreg2[instruction[10:13]]
    s2=dreg2[instruction[13:16]]

    if(s2[-1]=='0'):
        s4=converting_binary_to_decimal(R0[0])
    elif(s2[-1]=='1'):
        s4=converting_binary_to_decimal(R1[0])
    elif(s2[-1]=='2'):
        s4=converting_binary_to_decimal(R2[0])
    elif(s2[-1]=='3'):
        s4=converting_binary_to_decimal(R3[0])
    elif(s2[-1]=='4'):
        s4=converting_binary_to_decimal(R4[0])
    elif(s2[-1]=='5'):
        s4=converting_binary_to_decimal(R5[0])
    elif(s2[-1]=='6'):
        s4=converting_binary_to_decimal(R6[0])
    s5=~s4
    s6=converting_decimal_to_binary(s5)
    if(s1[-1]=='0'):
        R0.clear()
        R0.append(s6)
    elif(s1[-1]=='1'):
        R1.clear()
        R1.append(s6)
    elif(s1[-1]=='2'):
        R2.clear()
        R2.append(s6)
    elif(s1[-1]=='3'):
        R3.clear()
        R3.append(s6)
    elif(s1[-1]=='4'):
        R4.clear()
        R4.append(s6)
    elif(s1[-1]=='5'):
        R6.clear()
        R6.append(s6)
    elif(s1[-1]=='6'):
        R6.clear()
        R6.append(s6)
    FLAGS.clear()
    FLAGS.append('0000000000000000') 

def cmp(instruction,R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2,FLAGS2):
    s1=dreg2[instruction[10:13]]
    s2=dreg2[instruction[13:16]]
    if(s1[-1]=='0'):
        s3=converting_binary_to_decimal(R0[0])
    elif(s1[-1]=='1'):
        s3=converting_binary_to_decimal(R1[0])
    elif(s1[-1]=='2'):
        s3=converting_binary_to_decimal(R2[0])
    elif(s1[-1]=='3'):
        s3=converting_binary_to_decimal(R3[0])
    elif(s1[-1]=='4'):
        s3=converting_binary_to_decimal(R4[0])
    elif(s1[-1]=='5'):
        s3=converting_binary_to_decimal(R5[0])
    elif(s1[-1]=='6'):
        s3=converting_binary_to_decimal(R6[0])
    if(s2[-1]=='0'):
        s4=converting_binary_to_decimal(R0[0])
    elif(s2[-1]=='1'):
        s4=converting_binary_to_decimal(R1[0])
    elif(s2[-1]=='2'):
        s4=converting_binary_to_decimal(R2[0])
    elif(s2[-1]=='3'):
        s4=converting_binary_to_decimal(R3[0])
    elif(s2[-1]=='4'):
        s4=converting_binary_to_decimal(R4[0])
    elif(s2[-1]=='5'):
        s4=converting_binary_to_decimal(R5[0])
    elif(s2[-1]=='6'):
        s4=converting_binary_to_decimal(R6[0])
    if(s3==s4):
    
        FLAGS.clear()
        FLAGS.append('0000000000000001')
        FLAGS2.clear()
        FLAGS2.append('0000000000000001')
    elif(s3<s4):
        FLAGS.clear()
        FLAGS.append('0000000000000100')
        FLAGS2.clear()
        FLAGS2.append('0000000000000100')
    else:
        FLAGS.clear()
        FLAGS.append('0000000000000010')
        FLAGS2.clear()
        FLAGS2.append('0000000000000010')

import sys
def jgt(instruction,R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2,FLAGS2,pc):
    s1=instruction[9:16]
    s2=converting_binary_to_decimal_7_bit(s1)
    if(FLAGS2[0][-2]==1):
        FLAGS.clear()
        FLAGS.append('0000000000000000')
        FLAGS2.clear()
        FLAGS2.append('0000000000000000')
        pc = s2
        return pc
    else:
        FLAGS.clear()
        FLAGS.append('0000000000000000')
        FLAGS2.clear()
        FLAGS2.append('0000000000000000')
        return pc+1
def jlt(instruction,R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2,FLAGS2,pc):
    s1=instruction[9:16]
    s2=converting_binary_to_decimal_7_bit(s1)
    if(FLAGS2[0][-3]==1):
        FLAGS.clear()
        FLAGS.append('0000000000000000')
        FLAGS2.clear()
        FLAGS2.append('0000000000000000')
        return s2
    else:
        FLAGS.clear()
        FLAGS.append('0000000000000000')
        FLAGS2.clear()
        FLAGS2.append('0000000000000000')
        return pc+1
def je(instruction,R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2,FLAGS2,pc):
    s1=instruction[9:16]
    s2=converting_binary_to_decimal_7_bit(s1)
    if(FLAGS2[0][-1]==1):
        FLAGS.clear()
        FLAGS.append('0000000000000000')
        FLAGS2.clear()
        FLAGS2.append('0000000000000000')
        return s2
    else:
        FLAGS.clear()
        FLAGS.append('0000000000000000')
        FLAGS2.clear()
        FLAGS2.append('0000000000000000')
        return pc+1
# def nand(instruction,R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2):

#     s1=dreg2[instruction[10:13]]
#     s2=dreg2[instruction[13:16]]
#     s7=dreg2[instruction[7:10]]
    
    
#     if(s1[-1]=='0'):
#         s3=converting_binary_to_decimal(R0[0])
#     elif(s1[-1]=='1'):
#         s3=converting_binary_to_decimal(R1[0])
#     elif(s1[-1]=='2'):
#         s3=converting_binary_to_decimal(R2[0])
#     elif(s1[-1]=='3'):
#         s3=converting_binary_to_decimal(R3[0])
#     elif(s1[-1]=='4'):
#         s3=converting_binary_to_decimal(R4[0])
#     elif(s1[-1]=='5'):
#         s3=converting_binary_to_decimal(R5[0])
#     elif(s1[-1]=='6'):
#         s3=converting_binary_to_decimal(R6[0])
#     if(s2[-1]=='0'):
#         s4=converting_binary_to_decimal(R0[0])
#     elif(s2[-1]=='1'):
#         s4=converting_binary_to_decimal(R1[0])
#     elif(s2[-1]=='2'):
#         s4=converting_binary_to_decimal(R2[0])
#     elif(s2[-1]=='3'):
#         s4=converting_binary_to_decimal(R3[0])
#     elif(s2[-1]=='4'):
#         s4=converting_binary_to_decimal(R4[0])
#     elif(s2[-1]=='5'):
#         s4=converting_binary_to_decimal(R5[0])
#     elif(s2[-1]=='6'):
#         s4=converting_binary_to_decimal(R6[0])

#     s5=~(s4&s3)
#     s6=converting_decimal_to_binary(s5)
    
#     if(s7[-1]=='0'):
#         R0.clear()
#         R0.append(s6)
#     elif(s7[-1]=='1'):
#         R1.clear()
#         R1.append(s6)
#     elif(s7[-1]=='2'):
#         R2.clear()
#         R2.append(s6)
#     elif(s7[-1]=='3'):
#         R3.clear()
#         R3.append(s6)
#     elif(s7[-1]=='4'):
#         R4.clear()
#         R4.append(s6)
#     elif(s7[-1]=='5'):
#         R6.clear()
#         R6.append(s6)
#     elif(s7[-1]=='6'):
#         R6.clear()
#         R6.append(s6)
#     FLAGS.clear()
#     FLAGS.append('0000000000000000')

# def nor(instruction,R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2):

#     s1=dreg2[instruction[10:13]]
#     s2=dreg2[instruction[13:16]]
#     s7=dreg2[instruction[7:10]]
    
    
#     if(s1[-1]=='0'):
#         s3=converting_binary_to_decimal(R0[0])
#     elif(s1[-1]=='1'):
#         s3=converting_binary_to_decimal(R1[0])
#     elif(s1[-1]=='2'):
#         s3=converting_binary_to_decimal(R2[0])
#     elif(s1[-1]=='3'):
#         s3=converting_binary_to_decimal(R3[0])
#     elif(s1[-1]=='4'):
#         s3=converting_binary_to_decimal(R4[0])
#     elif(s1[-1]=='5'):
#         s3=converting_binary_to_decimal(R5[0])
#     elif(s1[-1]=='6'):
#         s3=converting_binary_to_decimal(R6[0])
#     if(s2[-1]=='0'):
#         s4=converting_binary_to_decimal(R0[0])
#     elif(s2[-1]=='1'):
#         s4=converting_binary_to_decimal(R1[0])
#     elif(s2[-1]=='2'):
#         s4=converting_binary_to_decimal(R2[0])
#     elif(s2[-1]=='3'):
#         s4=converting_binary_to_decimal(R3[0])
#     elif(s2[-1]=='4'):
#         s4=converting_binary_to_decimal(R4[0])
#     elif(s2[-1]=='5'):
#         s4=converting_binary_to_decimal(R5[0])
#     elif(s2[-1]=='6'):
#         s4=converting_binary_to_decimal(R6[0])

#     s5=~(s4|s3)
#     s6=converting_decimal_to_binary(s5)
    
#     if(s7[-1]=='0'):
#         R0.clear()
#         R0.append(s6)
#     elif(s7[-1]=='1'):
#         R1.clear()
#         R1.append(s6)
#     elif(s7[-1]=='2'):
#         R2.clear()
#         R2.append(s6)
#     elif(s7[-1]=='3'):
#         R3.clear()
#         R3.append(s6)
#     elif(s7[-1]=='4'):
#         R4.clear()
#         R4.append(s6)
#     elif(s7[-1]=='5'):
#         R6.clear()
#         R6.append(s6)
#     elif(s7[-1]=='6'):
#         R6.clear()
#         R6.append(s6)
#     FLAGS.clear()
#     FLAGS.append('0000000000000000')

# def xnor(instruction,R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2):
#     s1=dreg2[instruction[10:13]]
#     s2=dreg2[instruction[13:16]]
#     s7=dreg2[instruction[7:10]]
    
    
#     if(s1[-1]=='0'):
#         s3=converting_binary_to_decimal(R0[0])
#     elif(s1[-1]=='1'):
#         s3=converting_binary_to_decimal(R1[0])
#     elif(s1[-1]=='2'):
#         s3=converting_binary_to_decimal(R2[0])
#     elif(s1[-1]=='3'):
#         s3=converting_binary_to_decimal(R3[0])
#     elif(s1[-1]=='4'):
#         s3=converting_binary_to_decimal(R4[0])
#     elif(s1[-1]=='5'):
#         s3=converting_binary_to_decimal(R5[0])
#     elif(s1[-1]=='6'):
#         s3=converting_binary_to_decimal(R6[0])
#     if(s2[-1]=='0'):
#         s4=converting_binary_to_decimal(R0[0])
#     elif(s2[-1]=='1'):
#         s4=converting_binary_to_decimal(R1[0])
#     elif(s2[-1]=='2'):
#         s4=converting_binary_to_decimal(R2[0])
#     elif(s2[-1]=='3'):
#         s4=converting_binary_to_decimal(R3[0])
#     elif(s2[-1]=='4'):
#         s4=converting_binary_to_decimal(R4[0])
#     elif(s2[-1]=='5'):
#         s4=converting_binary_to_decimal(R5[0])
#     elif(s2[-1]=='6'):
#         s4=converting_binary_to_decimal(R6[0])

#     s5=~(s4^s3)
#     s6=converting_decimal_to_binary(s5)
    
#     if(s7[-1]=='0'):
#         R0.clear()
#         R0.append(s6)
#     elif(s7[-1]=='1'):
#         R1.clear()
#         R1.append(s6)
#     elif(s7[-1]=='2'):
#         R2.clear()
#         R2.append(s6)
#     elif(s7[-1]=='3'):
#         R3.clear()
#         R3.append(s6)
#     elif(s7[-1]=='4'):
#         R4.clear()
#         R4.append(s6)
#     elif(s7[-1]=='5'):
#         R6.clear()
#         R6.append(s6)
#     elif(s7[-1]=='6'):
#         R6.clear()
#         R6.append(s6)
#     FLAGS.clear()
#     FLAGS.append('0000000000000000')

# def Stdec(instruction, R0, R1, R2, R3, R4, R5, R6, FLAGS, dreg2, list):
#     s1 = dreg2[instruction[6:9]]
#     s2 = instruction[9:]
#     a = converting_binary_to_decimal_7_bit(s2)
#     if(s1 == 'R0'):
#         s3=converting_binary_to_decimal(R0[0])
#         s4=s3-1
#         if(s4<0):
#             FLAGS.clear()
#             FLAGS.append('0000000000001000')
#         else:
#             FLAGS.clear()
#             FLAGS.append('0000000000000000')
#             s5=converting_decimal_to_binary(s4)
#             list[a] = s5
#     elif(s1 == 'R1'):
#         s3=converting_binary_to_decimal(R1[0])
#         s4=s3-1
#         if(s4<0):
#             FLAGS.clear()
#             FLAGS.append('0000000000001000')
#         else:
#             FLAGS.clear()
#             FLAGS.append('0000000000000000')
#             s5=converting_decimal_to_binary(s4)

#             list[a] = s5
#     elif(s1 == 'R2'):
#         s3=converting_binary_to_decimal(R2[0])
#         s4=s3-1
#         if(s4<0):
#             FLAGS.clear()
#             FLAGS.append('0000000000001000')
#         else:
#             FLAGS.clear()
#             FLAGS.append('0000000000000000')
#             s5=converting_decimal_to_binary(s4)

#             list[a] = s5
#     elif(s1 == 'R3'):
#         s3=converting_binary_to_decimal(R3[0])
#         s4=s3-1
#         if(s4<0):
#             FLAGS.clear()
#             FLAGS.append('0000000000001000')
#         else:
#             FLAGS.clear()
#             FLAGS.append('0000000000000000')
#             s5=converting_decimal_to_binary(s4)

#             list[a] = s5
#     elif(s1 == 'R4'):
#         s3=converting_binary_to_decimal(R4[0])
#         s4=s3-1
#         if(s4<0):
#             FLAGS.clear()
#             FLAGS.append('0000000000001000')
#         else:
#             FLAGS.clear()
#             FLAGS.append('0000000000000000')
#             s5=converting_decimal_to_binary(s4)

#             list[a] = s5
#     elif(s1 == 'R5'):
#         s3=converting_binary_to_decimal(R5[0])
#         s4=s3-1
#         if(s4<0):
#             FLAGS.clear()
#             FLAGS.append('0000000000001000')
#         else:
#             FLAGS.clear()
#             FLAGS.append('0000000000000000')
#             s5=converting_decimal_to_binary(s4)

#             list[a] = s5
#     elif(s1 == 'R6'):
#         s3=converting_binary_to_decimal(R6[0])
#         s4=s3-1
#         if(s4<0):
#             FLAGS.clear()
#             FLAGS.append('0000000000001000')
#         else:
#             FLAGS.clear()
#             FLAGS.append('0000000000000000')
#             s5=converting_decimal_to_binary(s4)

#             list[a] = s5
# def ldinc(instruction, R0, R1, R2, R3, R4, R5, R6, FLAGS, dreg2, list):
#     s1 = dreg2[instruction[6:9]]
#     s2 = instruction[9:]
#     a = converting_binary_to_decimal_7_bit(s2)
#     string = list[a]
#     s3=converting_binary_to_decimal(string)+1
#     s4=converting_decimal_to_binary(s3)
#     if(s4>16):
#         if(s1 == 'R0'):
#             R0.clear()
#             R0.append("0000000000000000")
#         elif(s1 == 'R1'):
#             R1.clear()
#             R1.append("0000000000000000")
#         elif(s1 == 'R2'):
#             R2.clear()
#             R2.append("0000000000000000")
#         elif(s1 == 'R3'):
#             R3.clear()
#             R3.append("0000000000000000")
#         elif(s1 == 'R4'):
#             R4.clear()
#             R4.append("0000000000000000")
#         elif(s1 == 'R5'):
#             R5.clear()
#             R5.append("0000000000000000")
#         elif(s1 == 'R6'):
#             R6.clear()
#             R6.append("0000000000000000")
        
#         FLAGS.clear()
#         FLAGS.append('0000000000001000')
#     else:
#         if(s1 == 'R0'):
#             R0.clear()
#             R0.append(string)
#         elif(s1 == 'R1'):
#             R1.clear()
#             R1.append(string)
#         elif(s1 == 'R2'):
#             R2.clear()
#             R2.append(string)
#         elif(s1 == 'R3'):
#             R3.clear()
#             R3.append(string)
#         elif(s1 == 'R4'):
#             R4.clear()
#             R4.append(string)
#         elif(s1 == 'R5'):
#             R5.clear()
#             R5.append(string)
#         elif(s1 == 'R6'):
#             R6.clear()
#             R6.append(string)
#         FLAGS.clear()
#         FLAGS.append('0000000000000000')

#dictionary of opcode
dopcode ={'add':'00000', 'sub':'00001', 'mov':'00010', 'mov1':'00011', 'ld':'00100', 'st':'00101', 'mul':'00110', 'div':'00111', 'rs':'01000', 'ls':'01001', 'xor': '01010', 'or':'01011', 'and':'01011', 'not':'01101', 'cmp':'01110', 'jmp':'01111', 'jlt':'11100', 'jgt':'11101', 'je':'11111', 'hlt':'11010','nand':'11001','nor':'11110','xnor':'10011','stdec':'10100','ldinc':'10100'}
#dictionary of registers
dreg = {'R0' :'000','R1' :'001','R2' :'010','R3' :'011','R4' :'100','R5' :'101','R6': '110', 'FLAGS':'111'}
dreg2 = {'000':'R0','001':'R1' ,'010':'R2' ,'011':'R3' ,'100':'R4' ,'101':'R5', '110': 'R6','111':'FLAGS'}


list = ['0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000']
R0=['0000000000000000']
R1=['0000000000000000']
R2=['0000000000000000']
R3=['0000000000000000']
R4=['0000000000000000']
R5=['0000000000000000']
R6=['0000000000000000']
FLAGS=['0000000000000000']
FLAGS2=['0000000000000000']
i = 0
while(True):
    try:
        a=input().strip()
        list[i] = a
        i=i+1
    except EOFError:
        break
# a=sys.stdin
# for i in range(len(a)):
#     list[i]=a[i].strip()
# list[0]="0001000010000101"
# list[1]="0010100010000011"
# list[2]="1101000000000000"
# main function
pc=0
inst2 = list[pc][:5]
# print(inst2)

while(True):
    
    if(inst2=="11010"):
        FLAGS.clear()
        FLAGS.append('0000000000000000')
        print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        
        break
    if(inst2 == '00000'):
        add(list[pc],R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2)
        print(converting_decimal_to_binary_7_bit(pc)+'         '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        pc=pc+1
        inst2 = list[pc][:5]
        # print(inst2)


    elif(inst2 == '00001'):
        sub(list[pc],R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2)
        print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

        pc=pc+1
        inst2 = list[pc][:5]


    elif(inst2 == '00010'):
        movIm(list[pc], R0, R1, R2, R3, R4, R5, R6, FLAGS, dreg2)
        print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

        pc=pc+1
        inst2 = list[pc][:5]

    elif(inst2 == '00011'):#
        movRegister(list[pc], R0, R1, R2, R3, R4, R5, R6, FLAGS, dreg2)
        print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

        pc=pc+1
        inst2 = list[pc][:5]

    elif(inst2 == '00100'):#
        load(list[pc], R0, R1, R2, R3, R4, R5, R6, FLAGS, dreg2, list)
        print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

        pc=pc+1
        inst2 = list[pc][:5]


    elif(inst2 == '00101'):#
        Store(list[pc], R0, R1, R2, R3, R4, R5, R6, FLAGS, dreg2, list)
        print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

        pc=pc+1
        inst2 = list[pc][:5]


    elif(inst2 == '00110'):#
        mul(list[pc],R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2)
        print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

        pc=pc+1
        inst2 = list[pc][:5]


    elif(inst2 == '00111'):
        divide(list[pc],R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2)
        print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

        pc=pc+1
        inst2 = list[pc][:5]

    elif(inst2 == '01000'):
        Right_shift(list[pc],R0, R1, R2, R3, R4, R5, R6, FLAGS, dreg2)
        print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

        pc=pc+1
        inst2 = list[pc][:5]


    elif(inst2 == '01001'):
        left_shift(list[pc], R0, R1, R2, R3, R4, R5, R6, FLAGS, dreg2)
        print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

        pc=pc+1
        inst2 = list[pc][:5]

        
    elif(inst2 == '01010'):
        xor(list[pc],R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2)
        print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

        pc=pc+1
        inst2 = list[pc][:5]

    elif(inst2 == '01011'):
        orkaro(list[pc],R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2)
        print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

        pc=pc+1
        inst2 = list[pc][:5]

    elif(inst2 == '01100'):
        andkaro(list[pc],R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2)
        print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

        pc=pc+1
        inst2 = list[pc][:5]

    elif(inst2 == '01101'):
        notkar(list[pc],R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2)
        print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

        pc=pc+1
        inst2 = list[pc][:5]


    elif(inst2 == '01110'):
        cmp(list[pc],R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2,FLAGS2)
        print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])

        pc=pc+1
        inst2 = list[pc][:5]
        

    elif(inst2 == '01111'):
        a=pc
        pc=UnconditionalJump(list[pc], pc)
        print(converting_decimal_to_binary_7_bit(a)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])

        inst2 = list[pc][:5]
        

    elif(inst2 == '11100'):
        a=pc
        pc=jlt(list[pc],R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2,FLAGS2,pc)
        print(converting_decimal_to_binary_7_bit(a)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])

        inst2 = list[pc][:5]
        

    elif(inst2 == '11101'):
        a=pc
        pc=jgt(list[pc],R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2,FLAGS2,pc)
        print(converting_decimal_to_binary_7_bit(a)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])

        inst2 = list[pc][:5]
        

    elif(inst2 == '11111'):
        a=pc
        pc=je(list[pc],R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2,FLAGS2,pc)
        print(converting_decimal_to_binary_7_bit(a)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])

        inst2 = list[pc][:5]
    elif(inst2 == '11001'):
        nand(list[pc],R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2)
        print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

        pc=pc+1
        inst2 = list[pc][:5]

    # elif(inst2 == '11110'):
    #     nor(list[pc],R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2)
    #     print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

    #     pc=pc+1
    #     inst2 = list[pc][:5]

    # elif(inst2 == '10011'):
    #     xnor(list[pc],R0,R1,R2,R3,R4,R5,R6,FLAGS,dreg2)
    #     print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

    #     pc=pc+1
    #     inst2 = list[pc][:5]

    # elif(inst2 == '10100'):#
    #     Stdec(list[pc], R0, R1, R2, R3, R4, R5, R6, FLAGS, dreg2, list)
    #     print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

    #     pc=pc+1
    #     inst2 = list[pc][:5]

    # elif(inst2 == '10101'):#
    #     ldinc(list[pc], R0, R1, R2, R3, R4, R5, R6, FLAGS, dreg2, list)
    #     print(converting_decimal_to_binary_7_bit(pc)+'        '+R0[0]+' '+R1[0]+' '+R2[0]+' '+R3[0]+' '+R4[0]+' '+R5[0]+' '+R6[0]+' '+FLAGS[0])
        

    #     pc=pc+1
    #     inst2 = list[pc][:5]
for i in list:
    print(i)

