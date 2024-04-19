# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    if x>=y:
        return x
    elif x<=y:
        return y


def max_of_three(x, y, z):
    if y<=z and x<=z:
        return z
    elif z<=x and y<=x:
        return x
    elif x<=y and z<=y:
        return y
