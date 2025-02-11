#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('^\d+$') #整数のみを受理するよう修正
        # if p.match(ai) or p.match(bi):
        if p.match(ai) and p.match(bi): # 両方とも整数の場合にのみ受理するよう修正
                a=float(ai)
                b=float(bi)
                #if 0<a and a<b and b<1000:
                if 1 <= a and a <= 999 and 1 <= b and b <= 999:
                        valid=True
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return ans
        else:
                return -1
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
