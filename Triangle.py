#You are given a positive integer .Your task is to print a palindromic triangle of size.

num=int(input("Enter a number:"))
for i in range(1,num+1):
    print((10**i//9)**2)
