class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {
            1: "I",
            5: "V", 
            4: "IV", 
            9: "IX",  
            10: "X", 
            40: "XL",  
            50: "L", 
            90: "XC",  
            100: "C",  
            400: "CD",
            500: "D", 
            900: "CM",
            1000: "M", 
        }
        r = ''    
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while n <= num:
                r += num_map[n]
                num-=n
        return r
