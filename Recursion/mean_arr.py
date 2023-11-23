import argparse
parser = argparse.ArgumentParser(description="Taking array with cmd line")
parser.add_argument('--arr', required=True, help = "Give the array seperated by commas")
args = parser.parse_args()

# Brute force
# def mean(arr, n):
#     if n>0:
#         arr[len(arr)-1] = arr[len(arr)-1] + arr[n-1]
#         mean(arr, n-1)
#     else: 
#         print(arr[-1]/len(arr))
  
def findMean(A, N):
    if (N == 1):
        return A[N - 1]
    else:
        mean_prev = findMean(A, N - 1) * (N - 1) 
        new_mean = (mean_prev + A[N - 1])/N
        return new_mean
        
        
if __name__ == "__main__":
    string = args.arr
    arr = list(map(int, string.split(",")))
    r = findMean(arr, len(arr))
    print(r)

