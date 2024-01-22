#Given a number N reverse the number and print it. Example 1: Input: N = 123 Output: 321 Explanation: The reverse of 123 is 321 Example 2: Input: N = 234 Output: 432 Explanation: The reverse of 234 is 432 Input Format
#code 

num=int(input())
rev = 0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)
#Given an integer N, write a program to count the number of digits in N.Input Format Example 1: Input0: N = 12345 Example 2: Input1: N = 8394

#code
N=int(input())
string=str(N)
print(int(len(string)))