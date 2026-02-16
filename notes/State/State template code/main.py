import context
def main():
    c = context.Context()
    print(c.request())  # State A
    print(c.request())  # State B
    print(c.request())  # State A

main()