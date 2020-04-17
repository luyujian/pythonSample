'''
    Excel�ļ��ϲ�
'''
#--coding:gbk
import os
import pandas as pd


'''
��ȡ�ļ�������Excel�ļ�������
'''
def read_excel_files(excelFolder,excelFileNames):
    
    excelDfs = {}

    # ����ļ���·���� /�� // ��β ��Ҫ��ȫ��Ŀ����Ϊ�����Excel�ļ�����·��
    if not (excelFolder.endswith("/") or excelFolder.endswith("//")):
        excelFolder+="//"
        
    for excelFileName in excelFileNames:
        #excelFolder+excelFile  Excel �ļ�����·��
        df = pd.read_excel(excelFolder+excelFileName)
        #����key
        key = excelFileName[0:excelFileName.find(".")]
        excelDfs[key]= df
    return excelDfs


'''
�����Excel�е�sheet �ϲ���һ��Excel�ļ���sheet�С�
'''
def merge_to_sheet(excelFileDfs,saveFilePath):

        dfsvalues = excelFileDfs.values()
        newDfs = pd.concat(dfsvalues,ignore_index=True)
        newDfs.to_excel(saveFilePath)
        print  "�ļ��ϲ���ɣ�"+ saveFilePath


'''       
�����Excel�е�sheet �ϲ���һ��Excel �ļ��С�
'''
def merge_to_file(excelFileDfs,saveFilePath):
    
        excelWriter = pd.ExcelWriter(saveFilePath)
        
        for key,value in excelFileDfs.items():
            value.to_excel(excelWriter,sheet_name= unicode(key,"gbk"))
        excelWriter.save()
        excelWriter.close()
        print  "�ļ��ϲ���ɣ�"+ saveFilePath


'''
��ȡָ��Ŀ¼�µ� Excel �ļ����б�
'''
def getExcelFileName(dirPath):
    
    files = os.listdir(dirPath)
    excelFileName = []
    for item in files :
        if item.endswith("xlsx") or item.endswith("xls"):
            excelFileName.append(item)
    return excelFileName


'''
�ϲ�excel�ļ�
����:
excelFolder  excel�ļ���
targetExcelFilePath �ϲ�����ļ�����·��
method  �ϲ���ʽ 1 �ϲ���һ��sheet�У�2 �ϲ���һ��excel �ļ��У��������sheet
'''
def mergeExcelFiles (excelFolder,targetExcelFilePath,method):
    
    #��һ����ȡĿ¼��excel�ļ�·��
    excelFileNames = getExcelFileName(excelFolder)
    #�ڶ�����Excel�ļ�����
    excelDfs = read_excel_files(excelFolder,excelFileNames)
    #�������ϲ�Excel�ļ�

    if method == 1:
        merge_to_sheet(excelDfs,targetExcelFilePath)
    if method == 2:
        merge_to_file(excelDfs,targetExcelFilePath)
    

if __name__== "__main__" :

    mergeExcelFiles("g:\\python","g:\\66.xlsx",2)


