import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int, help = "Give num without space to find sum of digit")
args = parser.parse_args()


def sum_digit(num):
    if num==0:
        return 0
    else:
        return (num % 10 + sum_digit(int(num/10)))

def prod_digit(num):
    if num==0:
        return 1
    else:
        return (num % 10 * prod_digit(num//10))
    
if __name__ == "__main__":
    print("sum : ", sum_digit(args.n))
    print("prod : ", prod_digit(args.n))
    