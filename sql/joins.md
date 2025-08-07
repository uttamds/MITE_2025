Here's a **fairly complex `JOIN` query** involving **3 tables**, using **INNER JOIN**, **LEFT JOIN**, `GROUP BY`, and a simple aggregation (`COUNT`):

---

### **Scenario**:

Let's assume we are working with a database for a **college**:

#### Tables:

1. **Students**

   * `student_id` (PK)
   * `name`
   * `department_id`

2. **Courses**

   * `course_id` (PK)
   * `course_name`
   * `department_id`

3. **Enrollments**

   * `enrollment_id` (PK)
   * `student_id` (FK to Students)
   * `course_id` (FK to Courses)
   * `grade`

---

### **Objective**:

> Fetch the list of **students**, the **courses** they are enrolled in (even if the course is from a different department), and **count** how many students are enrolled **per course**, but **only for students from the 'Computer Science' department**.

---

### **Query**:

```sql
SELECT 
    s.name AS student_name,
    c.course_name,
    COUNT(e.student_id) OVER (PARTITION BY c.course_id) AS total_enrolled
FROM 
    Students s
INNER JOIN 
    Enrollments e ON s.student_id = e.student_id
LEFT JOIN 
    Courses c ON e.course_id = c.course_id
WHERE 
    s.department_id = (
        SELECT department_id 
        FROM Departments 
        WHERE department_name = 'Computer Science'
    )
ORDER BY 
    c.course_name, s.name;
```

---

### **Explanation**:

* **`INNER JOIN`**: Gets only those students who have enrollments.
* **`LEFT JOIN`**: Ensures we still get course details even if they don’t match the student’s department.
* **`COUNT(...) OVER (...)`**: Counts total enrollments per course (window function, no `GROUP BY` needed).
* **`WHERE` with subquery**: Filters only Computer Science students.

---

Let me know if you want this with table creation and sample data for testing.
