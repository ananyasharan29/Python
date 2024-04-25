def save_changes(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result:
            with open(args[0], 'w') as file:
                file.write(result)
            print("Changes saved successfully!")
    return wrapper

def read_file_content(func):
    def wrapper(*args, **kwargs):
        with open(args[0], 'r') as file:
            content = file.read()
            return func(content, *args[1:], **kwargs)
    return wrapper

@read_file_content
def add_text(content, text):
    return content + text

@read_file_content
def insert_text(content, index, text):
    return content[:index] + text + content[index:]

@read_file_content
def delete_text(content, start, end):
    return content[:start] + content[end:]

def create_document(filename):
    with open(filename, 'w') as file:
        print("New document created.")

@save_changes
def save_document(content, filename):
    return content

def text_editor_menu(filename):
    while True:
        print("\nText Editor Menu")
        print("1. Create new document")
        print("2. Add text")
        print("3. Insert text")
        print("4. Delete text")
        print("5. Save document")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_document(filename)
        elif choice == '2':
            text = input("Enter text to add: ")
            add_text(filename, text)
        elif choice == '3':
            index = int(input("Enter index to insert at: "))
            text = input("Enter text to insert: ")
            insert_text(filename, index, text)
        elif choice == '4':
            start = int(input("Enter start index to delete: "))
            end = int(input("Enter end index to delete: "))
            delete_text(filename, start, end)
        elif choice == '5':
            save_document(filename)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    filename = "document.txt"
    text_editor_menu(filename)
