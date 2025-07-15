import psycopg2
from faker import Faker
import random
from datetime import timedelta

# Initialize Faker
fake = Faker()

# PostgreSQL connection
conn = psycopg2.connect(
    dbname="company",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Clear tables first (optional)
tables = [
    "departments", "roles", "salaries", "employees", "projects",
    "employee_projects", "assets", "attendances", "leaves", "performance_reviews"
]
for t in tables:
    cursor.execute(f"DELETE FROM {t};")
conn.commit()

# 1️⃣ Departments (4 departments)
for i in range(1, 5):
    name = fake.bs().capitalize()
    manager_id = i  # Just assign first 4 employees as managers later
    cursor.execute("""
        INSERT INTO departments (department_id, name, manager_id)
        VALUES (%s, %s, %s)
    """, (i, name, None))  # Manager ID will be updated after employees are inserted

# 2️⃣ Roles (5 roles)
roles_data = [
    ('Software Engineer', 'Junior', 'Develops software features'),
    ('Software Engineer', 'Senior', 'Leads development projects'),
    ('HR Manager', 'Senior', 'Manages HR operations'),
    ('Accountant', 'Mid', 'Handles finances'),
    ('Sales Executive', 'Mid', 'Manages client accounts')
]
for idx, role in enumerate(roles_data, start=1):
    cursor.execute("""
        INSERT INTO roles (role_id, title, level, description)
        VALUES (%s, %s, %s, %s)
    """, (idx, role[0], role[1], role[2]))

# 3️⃣ Salaries (5 salary bands)
for i in range(1, 6):
    base_salary = random.randint(50000, 100000)
    bonus = random.randint(3000, 15000)
    effective_from = fake.date_between(start_date='-2y', end_date='today')
    benefits = random.choice(['Health Insurance', 'Dental', 'Stock Options', 'Travel Allowance'])
    cursor.execute("""
        INSERT INTO salaries (salary_id, base_salary, bonus, effective_from, benefits)
        VALUES (%s, %s, %s, %s, %s)
    """, (i, base_salary, bonus, effective_from, benefits))

# 4️⃣ Employees (150 employees)
for i in range(1, 151):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.unique.email()
    phone = fake.phone_number()
    hire_date = fake.date_between(start_date='-5y', end_date='today')
    department_id = random.randint(1, 4)
    role_id = random.randint(1, 5)
    salary_id = random.randint(1, 5)

    cursor.execute("""
        INSERT INTO employees (
            employee_id, first_name, last_name, email, phone, hire_date,
            department_id, role_id, salary_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        i, first_name, last_name, email, phone, hire_date,
        department_id, role_id, salary_id
    ))

# 5️⃣ Projects (150 projects)
for i in range(1, 151):
    name = fake.catch_phrase()
    description = fake.text(max_nb_chars=100)
    start_date = fake.date_between(start_date='-3y', end_date='-6m')
    end_date = start_date + timedelta(days=random.randint(30, 365))
    department_id = random.randint(1, 4)

    cursor.execute("""
        INSERT INTO projects (
            project_id, name, description, start_date, end_date, department_id
        ) VALUES (%s, %s, %s, %s, %s, %s)
    """, (i, name, description, start_date, end_date, department_id))

# 6️⃣ Employee_Projects (150 entries)
for i in range(1, 151):
    employee_id = random.randint(1, 150)
    project_id = random.randint(1, 150)
    role_in_project = random.choice(['Lead', 'Developer', 'Tester', 'Analyst'])
    allocation_pct = random.randint(20, 100)

    cursor.execute("""
        INSERT INTO employee_projects (
            id, employee_id, project_id, role_in_project, allocation_pct
        ) VALUES (%s, %s, %s, %s, %s)
    """, (i, employee_id, project_id, role_in_project, allocation_pct))

# 7️⃣ Assets (150 assets)
for i in range(1, 151):
    name = fake.word().capitalize()
    type_ = random.choice(['Hardware', 'Software'])
    assigned_to = random.randint(1, 150)
    purchase_date = fake.date_between(start_date='-3y', end_date='today')
    status = random.choice(['In use', 'Retired', 'In repair'])

    cursor.execute("""
        INSERT INTO assets (
            asset_id, name, type, assigned_to, purchase_date, status
        ) VALUES (%s, %s, %s, %s, %s, %s)
    """, (i, name, type_, assigned_to, purchase_date, status))

# 8️⃣ Attendances (150 entries)
for i in range(1, 151):
    employee_id = random.randint(1, 150)
    date = fake.date_between(start_date='-30d', end_date='today')
    status = random.choice(['Present', 'Absent', 'Remote'])
    check_in = fake.time() if status == 'Present' else None
    check_out = fake.time() if status == 'Present' else None

    cursor.execute("""
        INSERT INTO attendances (
            attendance_id, employee_id, date, status, check_in_time, check_out_time
        ) VALUES (%s, %s, %s, %s, %s, %s)
    """, (i, employee_id, date, status, check_in, check_out))

# 9️⃣ Leaves (150 entries)
for i in range(1, 151):
    employee_id = random.randint(1, 150)
    start_date = fake.date_between(start_date='-1y', end_date='today')
    end_date = start_date + timedelta(days=random.randint(1, 10))
    type_ = random.choice(['Sick', 'Paid', 'Unpaid', 'Casual'])
    status = random.choice(['Approved', 'Pending', 'Rejected'])

    cursor.execute("""
        INSERT INTO leaves (
            leave_id, employee_id, start_date, end_date, type, status
        ) VALUES (%s, %s, %s, %s, %s, %s)
    """, (i, employee_id, start_date, end_date, type_, status))

# 🔟 Performance Reviews (150 entries)
for i in range(1, 151):
    employee_id = random.randint(1, 150)
    review_date = fake.date_between(start_date='-1y', end_date='today')
    score = random.randint(1, 10)
    reviewer_id = random.randint(1, 150)
    comments = fake.sentence()

    cursor.execute("""
        INSERT INTO performance_reviews (
            review_id, employee_id, review_date, score, reviewer_id, comments
        ) VALUES (%s, %s, %s, %s, %s, %s)
    """, (i, employee_id, review_date, score, reviewer_id, comments))

# ✅ Update department managers (assign first employees)
for dept_id in range(1, 5):
    manager_id = random.randint(1, 150)
    cursor.execute("""
        UPDATE departments
        SET manager_id = %s
        WHERE department_id = %s
    """, (manager_id, dept_id))

# Commit all changes
conn.commit()
cursor.close()
conn.close()

print("✅ All 10 tables populated with 150 entries each.")
