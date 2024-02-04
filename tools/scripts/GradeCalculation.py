import numpy as np
from scipy import stats
 
class GradeCalculation:
    def __init__(self):
        self.Pk = 0
        self.Yi = 0
        self.Zi = 0
        self.Si = 0
        self.mode = 0
        self.method = 'r'
    
    def ModeChoose(self):
        self.method = input("请输入想要选择的模式 r(仅算排名标准分数)/s(算标准化成绩):\n ")
        if self.method == 'r':
            self.mode  = 0
        if self.method == 's':
            self.mode  = 1

    def RankCalculation(self):
        self.Pk = float(input("请输入学生成绩百分比：\n"))
        # self.Yi = stats.norm.cdf(1-self.Pk)
        self.ti = stats.norm.ppf(self.Pk)
        self.Yi = stats.norm.ppf(1-self.Pk)
        print(self.ti)
        print(self.Yi)
        self.Zi = 80 + 5*self.Yi

    def StandardScoreCalculation(self):
        self.RankCalculation()
        self.Hi = float(input("请输入该生换算后成绩:\n"))
        self.Si = 0.5*self.Zi+0.5*self.Hi

    def flow(self):
        self.ModeChoose()
        if self.mode == 0 :
            while(1):
                self.RankCalculation()
                print(f"该学生排名标准分数为: {self.Zi:.2f}")
        if self.mode == 1 :
            while(1):
                self.StandardScoreCalculation()
                print(f"该学生排名标准分数为 :{self.Hi:.2f}")        


def main():
    gc = GradeCalculation()
    while(1):
        gc.flow()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)

