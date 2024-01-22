import pandas as pd
df = pd.read_csv('output.csv',encoding='utf-8')
type_vector  =[]
for i in range(df.shape[0]):
    try:
        poem_type_index = df.iloc[i,1].replace('[','').replace(']','').split(',')[2]
        if "قصائد" in poem_type_index:
            type_vector.append(poem_type_index)
        else:
            type_vector.append(None)
    except IndexError:
        type_vector.append(None)

df['type'] = type_vector





