'''Write a program using a while loop to accept a number and check if it is a Happy number. (A number is
happy if repeatedly replacing it with the sum of squares of its digits eventually reaches 1). Example: 19 is a
happy number.'''

def numSquareSum(n):
    squareSum = 0
    while (n != 0):
        squareSum += (n % 10) * (n % 10)
        n = n // 10
    return squareSum

def isHappyNumber(n):
    st = set()
    while (1):
        n = numSquareSum(n)
        if (n == 1):
            return True
        if n in st:
            return False
        st.add(n)

n = int(input("Enter a number : "))
print(isHappyNumber(n))