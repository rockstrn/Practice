class Solution:
    def intToRoman(self, num: int) -> str:
        a=''
        b=num//1000
        for i in range(b):
            a=a+'M'
            num=num-1000
        if num>=900:
            a=a+'CM'
            num=num-900
        elif num<900 and num>=500:
            a=a+'D'
            num=num-500
            b=num//100
            for i in range(b):
                a=a+'C'
                num=num-100
        elif num<500 and num>=400:
            a=a+'CD'
            num=num-400
        else:
            b=num//100
            for i in range(b):
                a=a+'C'
                num=num-100
        if num>=90:
            a=a+'XC'
            num=num-90
        elif num<90 and num>=50:
            a=a+'L'
            num=num-50
            b=num//10
            for i in range(b):
                a=a+'X'
                num=num-10
        elif num<50 and num>=40:
            a=a+'XL'
            num=num-40
        else:
            b=num//10
            for i in range(b):
                a=a+'X'
                num=num-10
        if num==9:
            a=a+'IX'
        elif num<9 and num>=5:
            a=a+'V'
            num=num-5
            b=num
            for i in range(b):
                a=a+'I'
        elif num==4:
            a=a+'IV'
        else:
            for i in range(num):
                a=a+'I'
        return a
