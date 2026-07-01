def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

        print("\n----- FILE CONTENT -----")
        print(content)
        print("------------------------")

    except FileNotFoundError:
        print("❌ Error: File not found.")

    except Exception as e:
        print("❌ Error:", e)


def replace_word(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

        old_word = input("Enter the word to replace: ")
        new_word = input("Enter the new word: ")

        if old_word not in content:
            print("⚠ Word not found!")
            return

        updated_content = content.replace(old_word, new_word)

        with open(filename, "w") as file:
            file.write(updated_content)

        print("✅ Word replaced successfully!")

    except FileNotFoundError:
        print("❌ Error: File not found.")

    except Exception as e:
        print("❌ Error:", e)


def main():
    filename = "sample.txt"

    while True:
        print("\n========== BASIC FILE HANDLING ==========")
        print("1. View File")
        print("2. Find & Replace Word")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            read_file(filename)

        elif choice == "2":
            replace_word(filename)

        elif choice == "3":
            print("\nThank you for using the program!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()