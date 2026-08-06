import threading

##threading para time
def schedule(f, n):
    timer = threading.Timer(n / 1000.0, f)
    timer.start()

def main():
    def f():
        print("Executado após delay")

    n = 2000
    schedule(f, n)

if __name__ == "__main__":
    main()
