from collections import deque
Braces=[]
stack=deque()

def verify_braces_string(Braces):
    for i in range(lenstck):
        if Braces[i]=='(':
            stack.append(1)
        elif Braces[i]=='{': 
            stack.append(2)
        elif Braces[i]=='[':
            stack.append(3)
        elif (Braces[i] == ')'):
                # if the stack is empty, or the last parenthesis is different
                # than the one we are closing, then the input is wrong
                if (not stack or stack[-1] != 1): return False
                else:
                    stack.pop()
        elif (Braces[i] == '}'):
                # if the stack is empty, or the last parenthesis is different
                # than the one we are closing, then the input is wrong
                if (not stack or stack[-1] != 2): return False
                else:
                    stack.pop()
        else:
                # if the stack is empty, or the last parenthesis is different
                # than the one we are closing, then the input is wrong
                if (not stack or stack[-1] != 3): return False
                else:
                    stack.pop()
    if not stack: return True               
              
if __name__=="__main__":
     print("Provided String:")
     Braces = input()
     #print("String in a list is: " , Braces)
     lenstck=len(Braces)
     print("Length of String:", +lenstck)
     #print('Initial stack')
     #print(stack)
     if verify_braces_string(Braces)== True:
          print("Correct syntax.")
     else:
          print("Incorrect syntax.")
          



