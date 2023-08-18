from weekend_api import main


def main_call(name):
    if name == "__main__":
        main.main()


main_call(name=__name__)