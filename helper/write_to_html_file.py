import os

def write_to_html_file(text, filename):
    if not os.path.exists(filename):
        # Create file if it doesn't exist
        with open(filename, "w") as file:
            file.write("<!DOCTYPE html>\n<html>\n<head>\n<link rel=\"stylesheet\" href=\"./test.css\">\n</head>\n<body>\n</body>\n</html>")
    # Read the contents of the file
    with open(filename, "r") as file:
        file_contents = file.read()
    # Replace the contents of the body tag with the new text
    new_file_contents = file_contents.replace("</body>", f"{text}\n</body>")
    # Write the updated contents back to the file
    with open(filename, "w") as file:
        file.write(new_file_contents)
    # Close file
    file.close()
