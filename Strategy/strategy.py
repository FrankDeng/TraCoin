from logger import logger
import numpy as np
import pandas as pd

class Riskmanager(object):
    def __int__(self):
        self.Performance=pd.DataFrame(data=None,index=None,columns=['Position','Price','Margin','Balance','MTM','Sharpratio','Maxdrawdown',])

    def update_performance(self,Time,Performance):
        self.Performance.loc[Time]=Performance

class strategy(object):
    def __init__(self):
        self.RiskManager=Riskmanager()

    def load_data(self,Start,End,Freq,Features):
        return Data

    def create_model(self,Period,SeqLen,NumFeat,Class):
        return Model

    def input(self,Data,Period,SeqLen,NumFeat):
        return Input

    def output(self,Data,Period,SeqLen,NumFeat):
        return Output

    def optimizer(self,Model,Input,Output):
        return Model

    def calculate_signal(self,Model,Input):
        return Signal

    def update_rm(self,Time,Signal,Price):

    def backtest(self,Start,End,Freq,Period,SeqLen,Features):
            Data=self.load_data(Start,End,Freq,Features)
            Model=self.create_model(Period,SeqLen,NumFeat,Class)
            Len=Data.shape[1]
            for i in range(Len-(Period+SeqLen)):
                Train_Input=self.input(Data[:,i:i+Period+SeqLen])
                Train_Output=self.output(Data[:,i:i+Period+SeqLen])
                Model=self.optimizer(Model,Input,Output)
                Signal=self.calculate_position(Model,Data[:,i+Period+1:i+Period+SeqLen+1])
                self.update_rm(Time,Signal,Price)
            return self.RiskManager


