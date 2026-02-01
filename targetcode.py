
def generate(code):
    target=[]
    for line in code:
        parts=line.split("=")
        target.append(f"MOV {parts[0].strip()}, {parts[1].strip()}")
    return target
