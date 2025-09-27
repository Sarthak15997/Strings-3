#  Time Complexity : O(1) 
#  Space Complexity : O(1) 
#  Did this code successfully run on Leetcode : Yes
#  Three line explanation of solution in plain english : This code converts an integer into its English words representation using a predefined list of number-to-word mappings. It recursively breaks the number into chunks (billions, millions, thousands, hundreds, etc.), appending the corresponding words to a string builder as it divides and reduces the number. The recursion and iteration continue until the entire number is processed, and the final result is returned as a properly formatted string.

class NumberWord:
    # TC: O(1)  SC: O(1)
    def __init__(self, value, word):
        self.value = value
        self.word = word
class Solution:
    numberToWordsList = [
        NumberWord(1000000000, "Billion"),
        NumberWord(1000000, "Million"),
        NumberWord(1000, "Thousand"),
        NumberWord(100, "Hundred"),
        NumberWord(90, "Ninety"),
        NumberWord(80, "Eighty"),
        NumberWord(70, "Seventy"),
        NumberWord(60, "Sixty"),
        NumberWord(50, "Fifty"),
        NumberWord(40, "Forty"),
        NumberWord(30, "Thirty"),
        NumberWord(20, "Twenty"),
        NumberWord(19, "Nineteen"),
        NumberWord(18, "Eighteen"),
        NumberWord(17, "Seventeen"),
        NumberWord(16, "Sixteen"),
        NumberWord(15, "Fifteen"),
        NumberWord(14, "Fourteen"),
        NumberWord(13, "Thirteen"),
        NumberWord(12, "Twelve"),
        NumberWord(11, "Eleven"),
        NumberWord(10, "Ten"),
        NumberWord(9, "Nine"),
        NumberWord(8, "Eight"),
        NumberWord(7, "Seven"),
        NumberWord(6, "Six"),
        NumberWord(5, "Five"),
        NumberWord(4, "Four"),
        NumberWord(3, "Three"),
        NumberWord(2, "Two"),
        NumberWord(1, "One")
    ]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        return self.convert(num).strip()
    
    def convert(self, num):
        sb = []

        for nw in self.numberToWordsList:
            if num >= nw.value:
                if nw.value >= 100:
                    sb.append(self.convert(num // nw.value))
                    sb.append(" ")
                
                sb.append(nw.word)
                num %= nw.value

                if num != 0:
                    sb.append(" ")
                else:
                    break
        
        return ''.join(sb)