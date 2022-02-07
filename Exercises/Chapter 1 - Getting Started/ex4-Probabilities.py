import random

def main():

    favourite = ["bats","dogs","cats"]  # change this
    prob = random.random()

    if prob < 0.1:
        i=0
    if prob >0.9:
        i=2
    if prob >0.1 and prob <0.9:
        i=1
    
    print("I love " + favourite[i]) 


main()
