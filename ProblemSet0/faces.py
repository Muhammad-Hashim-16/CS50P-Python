def main():
    message = input("Enter: ")
    faces(message)

def faces(text):
    text = text.replace(":)", "😊")
    text = text.replace(":(", "🙁")
    print(text)

main()