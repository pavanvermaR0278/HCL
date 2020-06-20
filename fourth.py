



def fun(string):
    stack=[]
    #str1 = ''
    #print(len(stack))
    laststring=str()
    for i in range(len(string)):
        if stack and stack[-1]==string[i]:
            stack.pop()
        else:
            stack.append(string[i])
    if not stack:
        return 'Empty String'
    else:
        return ''.join(stack)


if __name__=="__main__":
    string=input("Enter string :")
    print(fun(string))
