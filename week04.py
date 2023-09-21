import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import tkinter as tk

def predict_life_sat():
    x = int(en_GDP_per_capita.get())
    X_new = [[x]]
    lifesat = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
    X = lifesat[["GDP per capita (USD)"]].values
    y = lifesat[["Life satisfaction"]].values

# lifesat.plot(kind='scatter', grid=True,  x="GDP per capita (USD)", y="Life satisfaction")
# plt.axis([23_500, 62_500, 5, 8])
# plt.show()

    model = LinearRegression()
    model.fit(X,y)
    lbl_lifesat.config(text=f"해당 국가의 삶의 만족도는 {model.predict(X_new)}로 예상합니다.")



# X_new = [[31700]]
#lbl_lifesat.config(text=f"해당국가의삶의만족도는")
#print(model.predict(X_new))
if __name__ == "__mm__":
    window = tk.Tk()
    window.title("삶의 만족도 예측 프로그램 v0.1")
    window.geometry("400x150")

    lbl_lifesat = tk.Label(window, text="입력하라")
    en_GDP_per_capita = tk.Entry(window)
    btn_predict = tk.Button(window, text="예측", command=predict_life_sat())

    lbl_lifesat.pack()
    en_GDP_per_capita.pack(fill='x')
    btn_predict.pack(fill='x')

    window.mainloop()
