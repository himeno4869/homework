# -*- coding: utf-8 -*-
import pandas as pd

class Weather(object):

    def __init__(self, path):
        self.path = path
        self.file = open(self.path, encoding='Shift-JIS').readlines()
        
    def load_date(self):
        list = []
        for line in self.file[1:]:
            list.append(line.split(',')[0])
        return list
        
    def load_maxtemp(self):
        list = []
        for line in self.file[1:]:
            list.append(float(line.split(',')[1]))
        return list
        
    def load_mintemp(self):
        list = []
        for line in self.file[1:]:
            list.append(float(line.split(',')[2]))
        return list
        
    def load_rain(self):
        list = []
        for line in self.file[1:]:
            list.append(float(line.split(',')[3]))
        return list
        
    def load_suntime(self):
        list = []
        for line in self.file[1:]:
            list.append(float(line.split(',')[4]))
        return list    
    
    def load_windspeed(self):
        list = []
        for line in self.file[1:]:
            list.append(float(line.split(',')[5]))
        return list
        
    def average(self, function):
        '''関数を指定して平均値を表示'''
        return sum(function)/len(function)
        
    def heaviest_rainy_day(self):
        rain_dict = dict()
        for i in range(len(self.file)-1):
            rain_dict[self.load_date()[i]] = self.load_rain()[i]
        sorted_list = sorted(rain_dict.items(), key=lambda x: -x[1])
        print('最大降水量： ' + sorted_list[0][0] + ' ' + str(sorted_list[0][1]) + '[mm]')
        
    def mean_suntime(self):
        '''月ごとの平均日照時間'''
        date_list = self.load_date() #日にちを読み込む
        date_number = dict() #月ごとの日数の辞書配列
        time_dict = dict() #月ごとの日照時間の合計時間の辞書配列
        sun_time_list = self.load_suntime()
        for i in range(len(self.file)-1):
            month = int(date_list[i].split('/')[1])
            if month not in time_dict:
                time_dict[month] = sun_time_list[i]
                date_number[month] = 1
            else:
                time_dict[month] =time_dict[month] + sun_time_list[i]
                date_number[month] = date_number[month] + 1
                           
        time_list = sorted(time_dict.items(), key=lambda x: x[0]) #sort
        date_number_list = sorted(date_number.items(), key=lambda x: x[0])
        
        print('各月の平均日照時間')
        for i in range(12):
            mean_sun_time = time_list[i][1]/date_number_list[i][1]
            print(str(i+1) + ' 月の平均日照時間： ' + str(mean_sun_time) + ' [hour]')
        
        
if __name__ == "__main__":
    path = 'tokyo-weather-20160601-20170531.csv'
    weather = Weather(path)
    maxtemp_average = weather.average(weather.load_maxtemp())
    mintemp_average = weather.average(weather.load_mintemp())
    print("平均最高気温：" + str(maxtemp_average) + ' ℃')
    print("平均最低気温：" + str(mintemp_average) + ' ℃')
    weather.heaviest_rainy_day()
    weather.mean_suntime()