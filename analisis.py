import pandas as pd

df = pd.read_csv('cybersecurity_attacks.csv')


if __name__ == '__main__':
    print(df.head)
    #for col in df.columns: print(col)
    #print(df['Malware Indicators'].)
    #for data in df.values:print(data)
    #for func in dir(df): print(func)
    #print(df[''])
    #for row in df.to_dict():
        #print(row)
