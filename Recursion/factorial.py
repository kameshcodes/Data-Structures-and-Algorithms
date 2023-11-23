import argparse
parser = argparse.ArgumentParser(description="Taking array with cmd line")
parser.add_argument('--n', type=int, required=True, help = "Give the array seperated by commas")
args = parser.parse_args()

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
    
if __name__ == "__main__":
    num = args.n 
    print(factorial(num))