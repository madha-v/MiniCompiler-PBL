def optimize(code):
    optimized=[]
    for line in code:
        if "+ 0" in line or "* 1" in line:
            continue
        optimized.append(line)
    return optimized
