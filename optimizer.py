
def optimize(code):
    optimized=[]
    for line in code:
        if "* 1" not in line:
            optimized.append(line)
    return optimized
