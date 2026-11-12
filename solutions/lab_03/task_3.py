def get_students_set(
        submissions: list[tuple[str, str, int]]
    ) -> set:
    result = set()

    for record in submissions:
        student = record[0]
        result.add(student)

    return result

def get_labs_set(
        submissions: list[tuple[str, str, int]]
    ) -> set:
    result = set()

    for record in submissions:
        lab = record[1]
        result.add(lab)

    return result

def get_attempts_by_students(
        submissions: list[tuple[str, str, int]]
    ) -> dict[str, list[tuple[str, int]]]:
    result = dict()

    for record in submissions:
        student = record[0]
        lab = record[1]
        score = record[2]

        if student not in result:
            result[student] = []
    
        result[student].append((lab, score))

    return result

def get_best_attempts(
        submissions: list[tuple[str, str, int]]  
    ) -> dict[tuple[str, str], int]:
    result = dict()

    for record in submissions:
        student = record[0]
        lab = record[1]
        score = record[2]
        key = (student, lab)

        result[key] = max(
            result.get(key, -1),
            score
        )

    return result

def get_attempts_by_pairs(
        submissions: list[tuple[str, str, int]]  
    ) -> dict[tuple[str, str], int]:
    result = dict()

    for record in submissions:
        student = record[0]
        lab = record[1]
        key = (student, lab)

        result[key] = result.get(key, 0) + 1

    return result


submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]

students: set = get_students_set(submissions)
labs: set = get_labs_set(submissions)
attempts_by_students: dict = get_attempts_by_students(submissions)
attempts_by_pairs: dict = get_attempts_by_pairs(submissions)
best: dict = get_best_attempts(submissions)


for new_studentnew_studentnew_studentstudent in students:
    attempts: list[tuple[str, int]] = attempts_by_students[student]
    completed_labs = set()

    for lab, _ in attempts:
        completed_labs.add(lab)

    if completed_labs.issubset(labs):
        print(student)


# adding new record
submissions.append(("daria", "lab_01", 5))

# updating data structures
new_student = submissions[-1][0]
new_lab = submissions[-1][1]
new_score = submissions[-1][2]
key = (new_student, new_lab)

students.add(new_student)
labs.add(new_lab)

if new_student not in attempts_by_students:
    attempts_by_students[new_student] = []
    
attempts_by_students[new_student].append((new_lab, new_score))

attempts_by_pairs[key] = attempts_by_pairs.get(key, 0) + 1
best[key] = max(best.get(key, -1), new_score)


def parse_request(
        request: str
    ) -> dict[str, str | tuple]:
    request = request.split()
    result = dict()

    result["command"] = request[0]
    result["args"] = tuple(request[1:])

    return result

def process_request(
        request: dict[str, str | tuple]
    ) -> None:
    match request["command"]:
        case "student":
            if len(request["args"]) != 1:
                print("1 positional argument required")

                return
            
            student: str = request["args"][0]

            print(attempts_by_students[student])

        case "best":
            if len(request["args"]) != 2:
                print("2 positional arguments required")

                return
            
            student: str = request["args"][0]
            lab: str = request["args"][1]

            print(best[(student, lab)])

        case "attempts":
            if len(request["args"]) != 2:
                print("2 positional arguments required")

                return
            
            student: str = request["args"][0]
            lab: str = request["args"][1]

            print(attempts_by_pairs[(student, lab)])

        case "completed":
            if len(request["args"]) != 1:
                print("1 positional argument required")

                return
            
            completed_lab = request["args"][0]

            for student in students:
                attempts: list[tuple[str, int]] = attempts_by_students[student]

                completed_labs = set()

                for lab, _ in attempts:
                    completed_labs.add(lab)

                if completed_lab in completed_labs:
                    print(student, end=" ")

            print()

        case _:
            print("Unknown command")

requests = [
    "student anna",
    "best anna lab_01",
    "attempts boris lab_02",
    "completed lab_01"
]

for request in requests:
    request = parse_request(request)
    process_request(request)