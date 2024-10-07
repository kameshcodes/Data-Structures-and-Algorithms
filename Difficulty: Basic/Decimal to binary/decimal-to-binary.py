#User function Template for python3
def toBinary(n):
    binary_str = ""
    while n>=1:
        if n%2 == 1:
            binary_str = "1" + binary_str
        else: 
            binary_str = "0" + binary_str
            
        n = n//2
        
    print(binary_str)



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    for _ in range(int(input())):
        n=int(input())
        toBinary(n)

    
# } Driver Code Ends