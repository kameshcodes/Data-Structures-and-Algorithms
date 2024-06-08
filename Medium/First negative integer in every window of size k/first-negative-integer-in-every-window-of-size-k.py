#User function Template for python3

def printFirstNegativeInteger( A, N, K):
    # code here
    i, j = 0, 0
    neg_queue = []
    ans = []
    while j<N:
        if A[j]<0:
            neg_queue.append(A[j])
        if j-i+1<K:
            j+=1
        elif j-i+1 == K:
            if not neg_queue:
                ans.append(0)
            else:
                ans.append(neg_queue[0])
                if A[i]==neg_queue[0]:
                    neg_queue.pop(0)
            i+=1
            j+=1
    return ans
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends