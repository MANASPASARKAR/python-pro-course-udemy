import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:

    def corr_heatmap(self, df_corr):
        sns.heatmap(df_corr)
        plt.show()

    def age_disease_plot(self, df):
        sns.boxplot(x="cardio", y="age_years", data=df)
        plt.show()

    def bmi_disease_plot(self, df):
        sns.boxplot(x="cardio", y="bmi", data=df)
        plt.show()

    def visualise(self, df):
        self.corr_heatmap(df.corr())
        self.age_disease_plot(df)
        self.bmi_disease_plot(df)