class Solution(object):

    def multiply1(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # 1. convert str to int using dict
        # 2. multiply
        # 3. convert int to str
        if num1 =='0' or num2 =='0':
            return 0

        numbs = {"0":0,
                 "1":1,
                 "2":2,
                 "3":3,
                 "4":4,
                 "5":5,
                 "6":6,
                 "7":7,
                 "8":8,
                 "9":9}
                
        def str_to_int(str1):

            base = len(str1)-1
            num = 0
            for char in str1:
                digit = numbs[char]
                num += digit*(10**base)
                base-=1
            return num
        
        def int_to_str(numb):
            
            q = float('inf')
            res =''
            while numb != 0:
                q = numb//10
                r = numb%10
                for key in numbs:
                    if numbs[key] == r:
                        res = key + res
                numb = q
            return res

        num3 = int_to_str(str_to_int(num1)*str_to_int(num2))
        return num3
    
    # using ord() funcion, which return a Unicode of charater
    # eg, ord('5') = 53
    def multiply2(self, num1, num2):

        def str_to_int(str1):

            res = 0
            for c in str1:
                res = res*10 +ord(c)-48
            return res

        num1 = str_to_int(num1)
        num2 = str_to_int(num2)

        num3 = num1*num2
        return str(num3)

if __name__ =="__main__":

    s = Solution()
    num1 = '123'
    num2 = '456'
    print(s.multiply1(num1,num2))
    print(s.multiply2(num1,num2))