from pathlib import Path

def get_cats_info(path: str) -> list:
    
    path = Path(path)
    if not path.exists():
        print("Файл за вказаним шляхом не знайдений")
        return None

    cat_dicts = []
    with open(path, 'r', encoding='utf-8') as fh:

        lines = [el.strip().split(',') for el in fh.readlines()]
        for line in lines:
            try:
                cat_dicts.append({'id': line[0], 'name': line[1], 'age': int(line[2])})
            except (IndexError, ValueError):
                print(f"Невірні дані в рядку: {lines.index(line)+1}")  
                
    return cat_dicts



def total_salary(path: str) -> tuple:
    
    path = Path(path)
    if not path.exists():
        print("Файл за вказаним шляхом не знайдений")
        return None

    with open(path, 'r', encoding='utf-8') as fh:
        lines = [el.strip().split(',') for el in fh.readlines()]
        salaries = []
        for line in lines:
            try:
                salary = int(line[1])
                if salary <= 0:
                    print(f"Поминалка в рядку: {lines.index(line)+1}. Число не може бути негативним")
                    return None
                salaries.append(salary)
            except (IndexError, ValueError):
                print(f"Invalid data in line {lines.index(line)+1}")
                return None

        if not salaries:
            return None

        summ = sum(salaries)
        avg = summ // len(salaries)
        return summ, avg
