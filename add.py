import datetime

def main():
    now = datetime.datetime.now()
    print("Привет, Docker!")
    print("Текущая дата и время:", now.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()
