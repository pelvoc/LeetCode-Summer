class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sums=0
        if "IV" in s: sums-=2
        if "IX" in s: sums-=2;
        if "XL" in s: sums-=20;
        if "XC" in s: sums-=20;
        if "CD" in s: sums-=200;
        if "CM" in s: sums-=200;

        c=list(s)

        for count in range(0, len(s)):
            if(c[count]=='M'): sums+=1000;
            if(c[count]=='D'): sums+=500;
            if(c[count]=='C'): sums+=100;
            if(c[count]=='L'): sums+=50;
            if(c[count]=='X'): sums+=10;
            if(c[count]=='V'): sums+=5;
            if(c[count]=='I'): sums+=1;
   
        return sums