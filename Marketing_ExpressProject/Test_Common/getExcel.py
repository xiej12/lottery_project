#condig:utf-8

import xlrd
from readConfig import ReadConfig
import json

class GetExcel(object):
    def __init__(self):
        '''
        :param filePath: excel路径
        :param sheel: 索引
        '''
        read = ReadConfig()
        self.filePath = read.get_config('EXCEL', 'filePath')
        self.sheel = int(read.get_config('EXCEL', 'sheel'))
        # 打开excel文件读取数据，创建文件对象赋值给workile
        self.workfile = xlrd.open_workbook(self.filePath)
        # 获取一个工作表（sheet）创建一个表格对象赋值给变量data
        self.data = self.workfile.sheets()[self.sheel]
        # 获取第一行作为key值
        self.keys = self.data.row_values(0)
        # print(self.keys)
        # 获取总行数
        self.rowNum = self.data.nrows
        # print(self.rowNum)
        # 获取总列数
        self.colNum = self.data.ncols
        # print(self.colNum)

     # 获取某一个单元格的内容
    def get_cell_values(self, row, col):
        return self.data.cell_value(row, col)

    def data_dict(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(int(self.rowNum) - 1)):
                # print(i)
                s = {}
                # 从第二行取对应values值
                s['rowNum'] = i + 2
                # print(s)
                # print(j)
                values = self.data.row_values(j)
                # print(values)
                for x in list(range(int(self.colNum))):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
                # print(s)
            return r

    def json_data(self,rows):
        '''返回每行的data(json格式数据)'''
        return json.loads(self.data_dict()[rows]['data'])

if __name__ == '__main__':
    open_Excel = GetExcel()
    #print(open_Excel.get_cell_values(1, 3))
    print(open_Excel.data_dict()[0]['verify'])
    print(open_Excel.json_data(0)['password'])