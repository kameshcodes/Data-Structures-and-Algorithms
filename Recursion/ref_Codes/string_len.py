import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--str", help = "Give num without space to find sum of digit")
args = parser.parse_args()

def str_len(string):
    if string == "":
        return 0
    else:
        return 1 + str_len(string[1:])
        
if __name__ == "__main__":
    string = args.str
    print(string)
    print(str_len(string)) 