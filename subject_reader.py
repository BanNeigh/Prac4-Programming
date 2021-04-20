"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = get_data()
    subject_output(subjects)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        subjects.append(parts)
    input_file.close()
    return subjects


def subject_output(subjects):
    """Display data how the question wants it"""
    counter = 0
    for data in subjects:
        print(f"{subjects[counter][0]} is taught by {subjects[counter][1]} and has {subjects[counter][2]} students")
        counter += 1


main()