
def handle_exception():
    try:
        a = 10
        b = "hi"
        c = a+b
        print(c)
    except Exception as e:
        #print(e)
        print(" its not possible")

handle_exception()

print("---------------------------------")

def handle_exception_with_raise(a,b):
    try:
        a = 20
        b = "hi"
