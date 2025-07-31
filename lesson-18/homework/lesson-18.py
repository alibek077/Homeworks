import pandas as pd

df = pd.read_csv('task\\stackoverflow_qa.csv')

#1
q1 = df[pd.to_datetime(df['creationdate']) < '2014-01-01']
print("#1\n", q1)

#2
q2 = df[df['score'] > 50]
print("\n#2\n", q2)

#3
q3 = df[(df['score'] >= 50) & (df['score'] <= 100)]
print("\n#3\n", q3)

#4
q4 = df[df['ans_name'] == 'Scott Boston']
print("\n#4\n", q4)

#5
users = ['Scott Boston', 'unutbu', 'Warren Weckesser', 'jezrael', 'DSM']
q5 = df[df['ans_name'].isin(users)]
print("\n#5\n", q5)

#6
q6 = df[
    (df['ans_name'] == 'unutbu') &
    (df['score'] < 5) &
    (pd.to_datetime(df['creationdate']) >= '2014-03-01') &
    (pd.to_datetime(df['creationdate']) <= '2014-10-31')
]
print("\n#6\n", q6)

#7
q7 = df[(df['score'].between(5, 10)) | (df['viewcount'] > 10000)]
print("\n#7\n", q7)

#8
q8 = df[df['ans_name'] != 'Scott Boston']
print("\n#8\n", q8)
