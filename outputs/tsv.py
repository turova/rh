def init():
    return 0

def run(data):
    out = ''
    first = True
    for d in data.values():
        if first:
            first = False
        else:
            out += '\t'
        out += str(d)
    return out

def info():
    return "Tab-separated output"