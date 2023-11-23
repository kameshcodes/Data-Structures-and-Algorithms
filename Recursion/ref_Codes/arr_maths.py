import argparse
parser = argparse.ArgumentParser(description="Taking array with cmd line")
parser.add_argument('--arr', type=str, help = "Give the array seperated by commas")
args = parser.parse_args()

def sum_arr(arr, n):
    if n==0:
        return 0
    else:
        return sum_arr(arr, n-1)+arr[n-1]
    
def prod_arr(arr, n):
    if n==1:
        return 1
    else:
        return prod_arr(arr, n-1)*arr[n-1]

def mean_arr(arr, n):
    if n==0:
        return 0
    else:
        return mean_arr(arr,n-1)+arr[n-1]/(len(arr))

if __name__ == "__main__":
    arr = list(map(int, args.arr.split(",")))
    print(prod_arr(arr, len(arr)))
    print(sum_arr(arr, len(arr)))
    print(mean_arr(arr, len(arr)))