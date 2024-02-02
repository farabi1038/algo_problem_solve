
#validIp finding from the number

def checkValid(string):
    if (len(string)>=2 and string[0]=='0'):
        return False
    if string=="" or int(string)>255:
        return False
    return True    
def validIPAddresses(string):
    # Write your code here.
    validIp=set()
    for i1 in range(1,4):
        for i2 in range(1,4):
            for i3 in range (1,4):
                firstNum=string[0:i1]
                secNum=string[i1:i1+i2]
                thirdNum=string[i1+i2:i1+i2+i3]
                forthNum= string[i1+i2+i3:]

                if checkValid(firstNum) and checkValid(secNum) and checkValid(thirdNum) and checkValid(forthNum):
                    ip=f"{firstNum}.{secNum}.{thirdNum}.{forthNum}"
                    validIp.add(ip)

                
        
    return validIp
