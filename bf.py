#import this function to use
#example: from bf read_passwords

def read_passwords(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


