class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        res=0
        for i in range(len(tokens)):
            try:
                t = int(tokens[i])
                stack.append(t)
            except:
                if tokens[i]=="+":
                    res = int(stack[-2])+int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif tokens[i]=="-":
                    res = int(stack[-2])-int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif tokens[i]=="*":
                    res = int(stack[-2])*int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif tokens[i]=="/":
                    res = int(int(stack[-2])/int(stack[-1]))
                    stack.pop()
                    stack.pop()
                    stack.append(res)
        return stack[0]