import pandas as pd
import pandas_datareader
import datetime



class Data(object):
    def __int__(self,ticker,datatype,feedtype,source,data):
        self.Header['Ticker','Datatype','Feedtype','Source']=[ticker,datatype,feedtype,source]
        self.Header['Timestamp']=datetime.datetime.now()
        self.Data=data
    def ToTimeSeries(self):



class Cache(object):
    def __init__(self):
        self.Cache=pd.DataFrame(data=None,index=None,columns=['Ticker','Datatype','Source','Data'])

    def Update(self,data):
        if data.Header['Feedtype']=='live':
            data=data.ToTimeSeries()

        ix=self.LocData(data)

        if ix:
            data=UpdateTimeSeries(Cache.iloc[ix]['Data'],data.Data)
            Cache.iloc[ix]['Data']=data.Data
        else:
            self.Adddata(Data)


class DataHandler(object):
    def __init__(self):
        self.Cachedata=Cache()

    def GenerateData(self,ticker,datatype,feedtype,source,data):
        return Data(ticker,datatype,feedtype,source,data)

    def UpdateCache(self,data):
        self.Cachedata.Update(data)

    def Load_API(self,ticker,feedtype,start,end,source):

    def Load_Database(self, ticker, datatype, start, end):

    def Feed_Database(self,ticker,datatype,start,end):

    def Load_Strategy(self, ticker, datatype, start, end):

    def Feed_Strategy(self,ticker,datatype,start,end):