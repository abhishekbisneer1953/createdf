import pandas as pd
def create_df():
    
    data = {'name':['abhi','arjun','arun'],
            'age':[1,2,3]}
    df = pd.DataFrame(data)
    print(df)

if __name__ == '__mian__':
    create_df()

# data = {'name':['abhi','arjun','arun'],
#             'age':[1,2,3]}
# df = pd.DataFrame(data)
# print(df)