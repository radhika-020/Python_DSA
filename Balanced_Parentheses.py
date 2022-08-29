from collections import deque

def checkPair(val1, val2):
  return (if val1 == "(" and val2 == ")") or (if val1 == "{" and val2 == "}") or (if val1 == "[" and val2 == "]")
  
def balanced_parentheses(expr):
  stack = deque
  for i in range(0, len(expr)-1):
    if i == "(":
      stack.append(i)
    else:
      if len(stack) == 0:
        return False
      elif checkPair(stack[-1], expr[i]):
        expr.pop()
        continue
        
      return False
    
    return True
      
        
        
  
