import sqlite3
import sys
import os
sys.path.append(os.path.dirname(__file__))
def top_departments(db_path):
    # connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor() 

    # write the SQL query
    query = """
    SELECT d.name, SUM(e.salary) as total_salary
    FROM employees e
    INNER JOIN departments d ON e.department_id = d.id
    GROUP BY d.name
    ORDER BY total_salary DESC
    LIMIT 3;
    """
    # execute the query
    cursor.execute(query)

    # fetch the results
    results = cursor.fetchall()

    # close the connection
    conn.close()

    # return the results
    return results


def employees_with_projects(db_path):
    # connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # SQL query: join employees - project_assignments - projects
    query = """
    SELECT e.name, p.name
    FROM employees e
    INNER JOIN project_assignments pa ON e.id = pa.employee_id
    INNER JOIN projects p ON pa.project_id = p.id;
    """
    
    # execute the query
    cursor.execute(query)
    
    # fetch the results
    results = cursor.fetchall()
    
    # close the connection
    conn.close()
    
    # return the results
    return results


def salary_rank_by_department(db_path):
    # connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # SQL query with window function
    query = """
    SELECT 
        e.name AS employee_name,
        d.name AS dept_name,
        e.salary,
        RANK() OVER(PARTITION BY e.department_id ORDER BY e.salary DESC) AS rank
    FROM employees e
    INNER JOIN departments d ON e.department_id = d.id
    ORDER BY d.name, rank;
    """
    
    # execute the query
    cursor.execute(query)
    
    # fetch the results
    results = cursor.fetchall()
    
    # close the connection
    conn.close()
    
    # return the results
    return results