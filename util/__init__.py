import codecs
import os
import math
import random
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体 SimHei为黑体
plt.rcParams['font.family']='sans-serif'
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

class TextProcess:

    def normfun(self, x, mu, sigma):
        pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
        return pdf

    def readfile(self, path):
        with open(path, 'r', encoding='utf-8') as file_corpus:
            list_corpus = file_corpus.readlines()
        for i in range(len(list_corpus)):
            line = list_corpus[i].strip('\n')
            words = line.split()
            list_corpus[i] = words
            list_corpus[i].pop(0)
        return list_corpus

    def construct(self, list_text):
        ninematrix = [] # 指标以列存储
        list_nums = [] # 指标以行存储
        for i in range(len(list_text)):
            nums = list_text[i]
            for j in range(len(nums)):
                numstr = nums[j]
                numfloat = abs(float(numstr))
                nums[j] = numfloat
                if len(ninematrix)<9:
                    temp = [numfloat]
                    ninematrix.append(temp)
                else:
                    ninematrix[j].append(numfloat)
            list_nums.append(nums)
        return list_nums, ninematrix

    def normalize(self, list_ninematrix):
        list_ninedimension = [] # 数字标准化，归一化
        for list_matrix in list_ninematrix:
            maxvalue = max(list_matrix)
            for i in range(len(list_matrix)):
                x = list_matrix[i]/maxvalue
                list_matrix[i] = x
            list_ninedimension.append(list_matrix)
        return list_ninedimension

    def distribution(self, seg, vector): #针对某一列
        aveinter = 1.0/seg
        itemnum = len(vector)
        list_segitem = []  # 数字分段
        list_seginter = []
        for i in range(seg):
            list_segitem.append(0)
            list_seginter.append(i * aveinter)
        for i in range(len(vector)):
            for j in range(seg):
                if vector[i] > list_seginter[j]:
                    list_segitem[j] = list_segitem[j] + 1
        list_res = list(map(lambda i: i/itemnum, list_segitem))  # 数字在各个段的分布
        return list_res


    def draw(self, vector, title):
        vector = np.array(vector)
        mean = vector.mean()
        std = vector.std()
        x = np.array(vector)
        x = np.arange(0, 1, 0.00001)
        y = self.normfun(x, mean, std)
        plt.figure()
        plt.plot(x, y)
        plt.hist(vector, bins=100, rwidth=0.9, density=True, color='black')
        plt.title(title + 'Distribution')
        plt.xlabel(title)
        plt.ylabel('Proportion')
        plt.show()
        pass

if __name__ == '__main__':
    filepath = '../source/resultCivil.txt'
    tp = TextProcess()
    list_corpus = tp.readfile(filepath)
    list_nums, list_ninematrix = tp.construct(list_corpus)
    list_ninedimension = tp.normalize(list_ninematrix)
    tp.draw(list_ninedimension[0], 'Suitability ')


