import os
from banner import banner

banner("HTML TAG COUNTER", "Collin Freeland")

def get_full_path(name):
    filename = os.path.join(".", "testing", f"{name}")
    return filename

def load(name):
    data = []
    filename = get_full_path(name)
    print(f"loading from {filename}.....")
    print("")

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data

def html_tag_counter(text):
    text = str(text)
    tag_count = 0
    previous_char = None
    for char in text:
        if char != "/" and previous_char == "<":
            tag_count += 1
        previous_char = char
    return tag_count

print("Welcome to the HTML tag counter!")
print("")

def run_event_loop():
    loadedfile = load(input("Please enter the name of an HTML file: "))
    tag_count = 0
    for line in loadedfile:
        tag_count += html_tag_counter(line)
    print(tag_count)

run_event_loop()