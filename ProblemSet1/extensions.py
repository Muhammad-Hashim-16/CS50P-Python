file = input("Filename: ")
name, extension = file.split(".")

match extension:
    case "jpg" | "png" | "gif" | "jpeg":
        print("image/" + extension)
    case "pdf"| "txt"| "zip":
        print("application/" + extension)
    case _:
        print("application/octet-stream")