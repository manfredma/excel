import pandas as pd

data = [['Mark', 55, 'Italy', 4.5, 'Europe'],
        ['John', 33, 'USA', 6.7, 'America'],
        ['Xxx', 43, 'USA', 6.7, 'Europe'],
        ['Yyy', 33, 'Italy', 6.7, 'America']
        ]
df = pd.DataFrame(data=data, columns=['name', 'age', 'country', 'score', 'continent'], index=[1001, 1002, 1003, 1004])
df.index.name = 'user_id'

if __name__ == '__main__':
    print(df)
    print((df["age"] > 40) & (df["country"] == 'Italy'))
    print((df["age"] > 40) & (df["country"].isin(['Italy', 'USA'])))
    print(df.loc[(df["age"] > 40) & (df["country"].isin(['Italy', 'USA']))])
