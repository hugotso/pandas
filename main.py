import pandas as pd

#raw_data =pd.read_excel('./test.xlsx')
#print(raw_data)

data = {'品牌' :['丰田','宝马','奔驰'], '型号':['卡罗拉','M3', 'GLK'], '价格w':[15, 30, 50]}
mydata = pd.DataFrame(data)
mydata.to_excel('./mydata.xlsx', index=False)

