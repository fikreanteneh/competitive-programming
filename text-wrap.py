import textwrap

def wrap(string, max_width):
    store = []
    for i in range(max_width, len(string), max_width):
        store.append(string[i - max_width:i] + "\n")
    store.append(string[i:] + "\n")
    return "".join(store)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
