lang = input
print("What is your input")
match lang:
    case "Javascript":
        print("web dev")
    case "Python":
        print("data scientist")
    case "PHP":
        print("backend")
    case "java":
        print("mobile app")
    case _:
        print("Ok")