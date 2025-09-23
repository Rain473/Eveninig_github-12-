data={"name":["Alice","Bob","Charlie"],
      "age":[30,25,35],
      "gender":["female","male","male"] }













import pandas as pd


name='Alice'
def age_gender(name):
    for i in range(len(data['name'])):
        if data['name'][i]==name:
            age=data['age'][i]
            gender=data['gender'][i]

            return age, gender
    df=pd.read_csv('data.csv')
    return df

print(age_gender(name))


