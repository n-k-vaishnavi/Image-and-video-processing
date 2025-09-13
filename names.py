import random
def bias_generator():
    with open ("names.txt" , "r") as bias:
        chosen_one = bias.readlines()
        return random.choice(chosen_one)
print("Your bias for today is  "+ bias_generator())