file = input("Filename: ")
name, extension = file.strip().lower().split(".")

match extension:
    case "png" | "gif" | "jpeg":
        print("image/" + extension)
    case "jpg":
        print("image/jpeg")
    case "pdf"| "zip":
        print("application/" + extension)
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")