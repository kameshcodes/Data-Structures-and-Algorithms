import argparse
parser = argparse.ArgumentParser(description="Taking Input n with cmd line")
parser.add_argument('--num', type=int, required=True, help = "Give the Value of n")
args = parser.parse_args()

def print_n_to_1(n):
    # initalise to n and then print it
    print(n, end=" ")
    # use base condition when input space gets smaller to 1
    if n==1:
       return 1
    # After printing n call function on n-1
    print_n_to_1(n-1)

def print_1_to_n(n):
    # intialise n and check base condition
    if n==1:
        print(1, end=" ")
        return 1
    # call function on smaller i/p
    print_1_to_n(n-1)
    # print while recursive windup
    print(n, end =" ")

def print_n_to_1_two(n):
    if n>0:
        print(n,end=" ")
        print_n_to_1_two(n-1)
        
def print_1_to_n_two(n):
    if n > 0:
        print_1_to_n_two(n-1)
        print(n, end=" ")
    
if  __name__ == "__main__":
    num = args.num 
    print("\nWith One:")
    print_1_to_n(num)
    print() 
    print_n_to_1(num)
    print("\n")
    
    print("With two:")
    print_1_to_n_two(num)
    print()
    print_n_to_1_two(num)