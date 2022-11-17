with open('hr_system.txt') as employee_info:
    for line in employee_info:
        stripped = line.strip()
        divided = stripped.split()
        name, id_number, job_title, salary = divided
        wage = float(salary) / 24
        if job_title == 'Engineer':
            wage += 1000
        print(f'{name} (ID: {id_number}), {job_title} - ${wage:,.2f}')