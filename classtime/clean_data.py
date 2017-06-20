import glob

data = glob.glob("data/*.*")
print(data)


df1=df_new.query("院系=='文学与传媒系'")
df2=df_new.query("院系=='艺术设计与创意产业系'")
pd.concat([df1,df2] )

pd.concat([df1,df2] ).to_csv('cleaned_data.tsv', encoding='utf8', sep = ',')
