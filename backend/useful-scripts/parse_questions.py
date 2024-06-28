import json

def parse_input_file(input_file):
    questions = []
    current_category = None

    with open(input_file, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    i = 0
    while i < len(lines):
        line = lines[i]
        if not line:
            i += 1
            continue

        if current_category is None:
            current_category = line
            i += 1
            continue

        if i + 5 < len(lines):
            question_text = lines[i]
            option_1 = lines[i + 1].split(') ', 1)[1].strip()
            option_2 = lines[i + 2].split(') ', 1)[1].strip()
            option_3 = lines[i + 3].split(') ', 1)[1].strip()
            option_4 = lines[i + 4].split(') ', 1)[1].strip()
            correct_answer = lines[i + 5].split(': ', 1)[1].strip()

            questions.append({
                "question_text": question_text,
                "option_1": option_1,
                "option_2": option_2,
                "option_3": option_3,
                "option_4": option_4,
                "correct_answer": correct_answer,
                "category": current_category
            })

            i += 6  # Move to the next question
        else:
            break

        if i < len(lines) and not lines[i].strip():
            i += 1  # Skip the blank line between questions

    return questions

def write_output_file(output_file, questions):
    with open(output_file, 'w') as file:
        file.write('questions = ')
        json.dump(questions, file, indent=2)

if __name__ == "__main__":
    input_file = 'questions-5.txt'  # Replace with your input file name
    output_file = 'questions-5.py'  # Replace with your desired output file name

    questions = parse_input_file(input_file)
    write_output_file(output_file, questions)
    print(f"Output written to {output_file}")
