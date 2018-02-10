def init():
    print("Initializing json")
    return 0

def run(data):
    out = ''
    first = True
    for d in data.keys():
        if first:
            out += '{ '
            first = False
        else:
            out += ', '
        out += '"' + str(d) + '": ' + '"' + str(data[d]) + '"'
    out += '}'
    return out

def info():
    return "JSON output"