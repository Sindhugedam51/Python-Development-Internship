from collections import Counter
import string


def analyze_file(filename):
    try:
        # Open file
        with open(filename, "r") as file:
            content = file.read()

        # Count characters
        characters = len(content)

        # Count lines
        lines = len(content.splitlines())

        # Remove punctuation and convert to lowercase
        clean_text = content.translate(
            str.maketrans('', '', string.punctuation)
        ).lower()

        # Count words
        words = clean_text.split()
        total_words = len(words)

        # Count word frequency
        frequency = Counter(words)

        print("\n========== FILE ANALYSIS ==========")
        print(f"Total Characters : {characters}")
        print(f"Total Words      : {total_words}")
        print(f"Total Lines      : {lines}")

        print("\nTop 10 Most Common Words")
        print("-" * 35)

        for word, count in frequency.most_common(10):
            print(f"{word:<15} {count}")

    except FileNotFoundError:
        print("❌ File not found.")

    except PermissionError:
        print("❌ Permission denied.")

    except Exception as e:
        print("Unexpected Error:", e)


def main():

    filename = "sample.txt"

    while True:

        print("\n========== WORD COUNT TOOL ==========")
        print("1. Analyze File")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            analyze_file(filename)

        elif choice == "2":
            print("\nThank you!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()