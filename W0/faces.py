def main():
    faces_input = input("How do you feel?")
    output = convert(faces_input)
    print(output)

def convert(faces_input):
    converted_faces = faces_input.replace(":)", "🙂").replace(":(", "🙁")
    return converted_faces

main()