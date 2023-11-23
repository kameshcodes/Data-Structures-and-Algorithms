import argparse
parser = argparse.ArgumentParser(description="Taking array with cmd line")
parser.add_argument('--n', type=int, help = "Give the array seperated by commas")
args = parser.parse_args()

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def sum_n(n):
    if n==1:
        return 1
    else:
        return n + sum_n(n-1)
    
def print_n_to_1_two(n):
    if n>0:
        print(n,end=" ")
        print_n_to_1_two(n-1)
        
def print_1_to_n_two(n):
    if n > 0:
        print_1_to_n_two(n-1)
        print(n, end=" ")
       
if __name__ == "__main__":
    num = args.n 
    print(factorial(num)) 
    print(sum_n(num))
    print_1_to_n_two(num)
    print()
    print_n_to_1_two(num)
    print()
