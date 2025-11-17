def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    
    if not fio.strip():
        raise ValueError("Empty name")
    if not group.strip():
        raise ValueError("Empty group")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA must be numeric")
    
    parts = ' '.join(fio.split()).split()
    surname = parts[0].title()
    
    initials = []
    for name in parts[1:]:
        if name.strip():
            initials.append(f"{name[0].upper()}.")
    
    formatted_gpa = f"{gpa:.2f}"
    
    return f"{surname} {''.join(initials)}, гр. {group}, GPA {formatted_gpa}"

if __name__ == "__main__":
    test_cases = [
        ("Иванов Иван Иванович", "ВГУТ-25", 4.6),
        ("Петров Пётр", "IKBO-12", 5.0),
        ("Петров Пётр Петрович", "IKBO-12", 5.0),
        (" сидорова анна сергеевна", "АВВ-01", 3.999),
    ]
    
    for test in test_cases:
        result = format_record(test)
        print(result)