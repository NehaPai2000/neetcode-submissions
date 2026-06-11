class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i == '(' or i == '{' or i=='[':
               stack.append(i)
            if i == ')':
               if not stack or stack[-1] != '(':
                  return False
               stack.pop()

            if i == ']':
               if not stack or stack[-1] != '[':
                   return False
               stack.pop()

            if i == '}':
               if not stack or stack[-1] != '{':
                   return False
               stack.pop()
        if not stack:
            return True
        else:
            return False