import argparse
parser = argparse.ArgumentParser(description="Taking array with cmd line")
parser.add_argument('--n', type=int, required=True, help = "Give the array seperated by commas")
args = parser.parse_args()

def sum_upto_n(n):
    if n==1:
        return 1
    else:
        return n + sum_upto_n(n-1)

# def sum_n(n):
#     if n > 1:
#         return n + sum_n(n-1)
#     else:
#         return 1

if __name__ == "__main__":
    num = args.n 
    print(sum_upto_n(num))
    print(sum_n(num+1))