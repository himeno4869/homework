# -*- coding: utf-8 -*-

class Weather(object):

    def __init__(self, path):
        self.path = path
        self.file = open(self.path, encoding='Shift-JIS').readlines() #指定されたファイルを開ける
        self.date_list = [line.split(',')[0] for line in self.file[1:]] #日にちのリストを作成
        self.maxtemp_list = [float(line.split(',')[1]) for line in self.file[1:]] #最高気温のリストを作成
        self.mintemp_list = [float(line.split(',')[2]) for line in self.file[1:]] #最低気温のリストを作成
        self.rain_list = [float(line.split(',')[3]) for line in self.file[1:]] #降水量のリストを作成
        self.suntime_list = [float(line.split(',')[4]) for line in self.file[1:]] #日照時間のリストを作成
        self.windspeed_list = [float(line.split(',')[5]) for line in self.file[1:]] #風速のリストを作成
        
    def average(self, lst):
        '''リストを指定して平均値を算出'''
        return sum(lst)/len(lst)
        
    def heaviest_rainy_day(self):
        '''降水量が最も多かった日にちを表示する関数'''
        rain_dict = dict((self.date_list[i], self.rain_list[i]) for i in range(len(self.file)-1))
        sorted_list = sorted(rain_dict.items(), key=lambda x: -x[1])
        print('最大降水量： ', sorted_list[0][0], ' ', sorted_list[0][1], '[mm]')
        
    def mean_suntime(self):
        '''月ごとの平均日照時間'''
        date_number = dict() #月ごとの日数の辞書配列
        time_dict = dict() #月ごとの日照時間の合計時間の辞書配列
        for i in range(len(self.file)-1):
            month = int(self.date_list[i].split('/')[1])
            if month not in time_dict:
                time_dict[month] = self.suntime_list[i]
                date_number[month] = 1
            else:
                time_dict[month] =time_dict[month] + self.suntime_list[i]
                date_number[month] = date_number[month] + 1
                           
        time_list = sorted(time_dict.items(), key=lambda x: x[0]) #sort
        date_number_list = sorted(date_number.items(), key=lambda x: x[0])
        
        print('各月の平均日照時間')
        for i in range(1, len(time_dict)+1):
            mean_sun_time = time_list[i-1][1]/date_number_list[i-1][1]
            print(i, ' 月の平均日照時間： ', mean_sun_time, ' [hour]')
            
def main():
    path = 'tokyo-weather-20160601-20170531.csv' #読み取るデータのパスを指定
    weather = Weather(path)
    maxtemp_average = weather.average(weather.maxtemp_list)
    print()
    mintemp_average = weather.average(weather.mintemp_list)
    print()
    print("平均最高気温：", maxtemp_average, ' ℃')
    print()
    print("平均最低気温：", mintemp_average, ' ℃')
    print()
    weather.heaviest_rainy_day()
    print()
    weather.mean_suntime()
        
if __name__ == "__main__":
    main()