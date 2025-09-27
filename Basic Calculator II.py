#  Time Complexity : O(N)
#  Space Complexity : O(N)
#  Did this code successfully run on Leetcode : Yes
#  Three line explanation of solution in plain english : This code evaluates a basic arithmetic expression string containing +, -, *, and / without parentheses. It uses a stack to store numbers: for + and - it pushes the current number (positive or negative), and for * and / it pops the last number, computes the result with the current number, and pushes it back. At the end, it sums all numbers in the stack to return the final evaluated result.

class Solution:
    def calculate(self, s: str) -> int: 
        st = []  # We declare a stack to store the numbers unless we encounter a sign
        currNum = 0  #Variable to keep a track of the current element of the string we are traversing over      
        lastSign = "+" # We initialise the sign to +    
        for i in range(len(s)):   #Traversing over the string
            ch = s[i]  
        
            if ch.isdigit():  #We check if the ch is a digit and if it is we find its integer value 
                currNum = currNum * 10 + int(ch) #This helps us to find the value of the character of the string

            if((not ch.isdigit() and ch != ' ') or i == len(s) - 1): #If the character we are currently traversing over is a sign or the last element then we check the following conditions. If the sign is + or - then we store the currNum in the stack. If it is * or / then we pop the element from the stack and process it with the currNum. We append this processed number to the stack. At the end of each iteration we will update the currNum = 0 and the lastSign to the sign we are currently on.
                if lastSign == "+":
                    st.append(currNum)
                elif lastSign == "-":
                    st.append(-currNum)
                elif lastSign == "*":
                    popped = st.pop()
                    st.append(popped*currNum)
                else:
                    popped = st.pop()
                    if popped < 0 or currNum < 0:
                        st.append(-(abs(popped) // abs(currNum)))
                    else:
                        st.append(popped // currNum)
                currNum = 0
                lastSign = ch
        result = 0
        while(st): #Here we traverse through the stack and take the popped element in the result variable
            result += st.pop()

        return result     
