import numpy as np
import pandas as pd

"""
Problem (1): Filter & Condition
You have employee data. Get employees who:
- Salary > 50,000
- Department = "IT"

- Use this data :
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Department": ["IT", "HR", "IT", "Finance", "IT"],
    "Salary": [60000, 40000, 55000, 70000, 45000]
}
"""
print("============= Problem (1) =============")

problem_1_data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Department": ["IT", "HR", "IT", "Finance", "IT"],
    "Salary": [60000, 40000, 55000, 70000, 45000]
}

problem_1_df = pd.DataFrame(problem_1_data)
problem_1_solution = problem_1_df.loc[(problem_1_df["Department"] == "IT") & (problem_1_df["Salary"]>50000)]
print(problem_1_solution)

"""
Problem (2): GroupBy + Aggregation
- Find the average salary per department

- Use this data :
data = {
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [60000, 40000, 55000, 70000, 50000]
}
"""
print("============= Problem (2) =============")
problem_2_data = {
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [60000, 40000, 55000, 70000, 50000]
}

problem_2_df = pd.DataFrame(problem_2_data)

# IT_data = problem_2_df.loc[(problem_2_df["Department"] == "IT")]
# HR_data = problem_2_df.loc[(problem_2_df["Department"] == "HR")]
# Finance_data = problem_2_df.loc[(problem_2_df["Department"] == "Finance")]
#
# print("average salary for IT department",IT_data['Salary'].mean())
# print("average salary for HR department", HR_data['Salary'].mean())
# print("average salary for Finance department",Finance_data['Salary'].mean())

problem_2_solution = problem_2_df.groupby("Department")["Salary"].mean()
print(problem_2_solution)

"""
Problem (3): Missing Values Handling
- Fill missing values in the "Age" column with the mean age

- Use this data :
data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [25, None, 30, None]
}
"""
print("============= Problem (3) =============")

problem_3_data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [25, None, 30, None]
}

problem_3_df = pd.DataFrame(problem_3_data)

print(problem_3_df)
problem_3_df['Age'] = problem_3_df['Age'].fillna(problem_3_df['Age'].mean())
print(problem_3_df)


"""
Problem (4): Sorting + Top Records
- Get top 2 highest salary employees

- Use this data :
data = {
    "Name": ["A", "B", "C", "D"],
    "Salary": [40000, 70000, 50000, 90000]
}

"""
print("============= Problem (4) =============")

problem_4_data = {
    "Name": ["A", "B", "C", "D"],
    "Salary": [40000, 70000, 50000, 90000]
}

problem_4_df = pd.DataFrame(problem_4_data)

problem_4_solution = problem_4_df.sort_values(by=["Salary"], ascending=False)
print(problem_4_solution.head(2))

# problem_4_solution = problem_4_df.nlargest(2, "Salary")
# print(problem_4_solution)

"""
Problem (5): Apply Function
- Create a new column "Bonus"
- If salary > 50000 → Bonus = 10% of salary , Else → Bonus = 5%

- Use this data :
data = {
    "Name": ["A", "B", "C"],
    "Salary": [60000, 40000, 80000]
}
"""
print("============= Problem (5) =============")

problem_5_data = {
    "Name": ["A", "B", "C"],
    "Salary": [60000, 40000, 80000]
}

problem_5_df = pd.DataFrame(problem_5_data)
problem_5_df['Bonus'] = problem_5_df['Salary'].apply(
    lambda x: int(x * 0.10) if x > 50000 else int(x * 0.05)
)
print(problem_5_df)
