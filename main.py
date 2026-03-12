from algorithms.bell_state import run as bell
from algorithms.ghz_state import run as ghz
from algorithms.grover import run as grover


def main():

    print("\n==============================")
    print(" Quantum Circuit Simulator ")
    print("==============================\n")

    print("1. Bell State")
    print("2. GHZ State")
    print("3. Grover Search")

    choice = input("\nEnter choice: ")

    if choice == "1":
        bell()

    elif choice == "2":
        ghz()

    elif choice == "3":
        grover()

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
