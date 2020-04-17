'''
    Excel文件合并
'''
#--coding:gbk
import os
import pandas as pd


'''
读取文件夹下面Excel文件的内容
'''
def read_excel_files(excelFolder,excelFileNames):
    
    excelDfs = {}

    # 如果文件夹路径是 /或 // 结尾 需要补全，目的是为了组合Excel文件绝对路径
    if not (excelFolder.endswith("/") or excelFolder.endswith("//")):
        excelFolder+="//"
        
    for excelFileName in excelFileNames:
        #excelFolder+excelFile  Excel 文件绝对路径
        df = pd.read_excel(excelFolder+excelFileName)
        #生成key
        key = excelFileName[0:excelFileName.find(".")]
        excelDfs[key]= df
    return excelDfs


'''
将多个Excel中的sheet 合并到一个Excel文件的sheet中。
'''
def merge_to_sheet(excelFileDfs,saveFilePath):

        dfsvalues = excelFileDfs.values()
        newDfs = pd.concat(dfsvalues,ignore_index=True)
        newDfs.to_excel(saveFilePath)
        print  "文件合并完成："+ saveFilePath


'''       
将多个Excel中的sheet 合并到一个Excel 文件中。
'''
def merge_to_file(excelFileDfs,saveFilePath):
    
        excelWriter = pd.ExcelWriter(saveFilePath)
        
        for key,value in excelFileDfs.items():
            value.to_excel(excelWriter,sheet_name= unicode(key,"gbk"))
        excelWriter.save()
        excelWriter.close()
        print  "文件合并完成："+ saveFilePath


'''
获取指定目录下的 Excel 文件名列表
'''
def getExcelFileName(dirPath):
    
    files = os.listdir(dirPath)
    excelFileName = []
    for item in files :
        if item.endswith("xlsx") or item.endswith("xls"):
            excelFileName.append(item)
    return excelFileName


'''
合并excel文件
参数:
excelFolder  excel文件夹
targetExcelFilePath 合并后的文件绝对路径
method  合并方式 1 合并到一个sheet中，2 合并到一个excel 文件中，产生多个sheet
'''
def mergeExcelFiles (excelFolder,targetExcelFilePath,method):
    
    #第一步获取目录下excel文件路径
    excelFileNames = getExcelFileName(excelFolder)
    #第二步读Excel文件内容
    excelDfs = read_excel_files(excelFolder,excelFileNames)
    #第三步合并Excel文件

    if method == 1:
        merge_to_sheet(excelDfs,targetExcelFilePath)
    if method == 2:
        merge_to_file(excelDfs,targetExcelFilePath)
    

if __name__== "__main__" :

    mergeExcelFiles("g:\\python","g:\\66.xlsx",2)


