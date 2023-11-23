import argparse
parser = argparse.ArgumentParser(description="Taking array with cmd line")
parser.add_argument('--n', type=int, help = "Give n to get sum of n fibonaaci digit")
args = parser.parse_args()

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) +  fibonacci(num-2)
    
def print_fibonacci(num):
###### home work       
    pass                               
       
if __name__ == "__main__":
    num = args.n 
    print(fibonacci(num))
    print(print_fibonacci(num))
    print()
    