from feature_engineer import FeatureEngineer

class Cleaner:

    '''
    Cleans the data in the cardiovascular Dataset
    '''

    def clean(self, df):

        # id doesnt add value so dropping it
        df = df.drop('id', axis=1)

        # bringing weight and heights between normal ranges
        df = df[(df["height"] >= 100) & (df["height"] <= 250)]
        df = df[(df["weight"] >= 30) & (df["weight"] <= 200)]

        # cleaning values for Systolic and Diastolic BP
        df = df[df["ap_hi"] > df["ap_lo"]]
        df = df[
            (df["ap_hi"] >= 80) &
            (df["ap_hi"] <= 250) &
            (df["ap_lo"] >= 40) &
            (df["ap_lo"] <= 150)
            ]

        # Feature engineering 2 columns
        df = FeatureEngineer().feature_engineer(df)

        # removing bmi values over 60 as they are anomalies or inaccurate measures
        df = df[df["bmi"] < 60]

        # Age in years is enough as a column. no more need of age in days
        df.drop('age', axis=1, inplace=True)

        return df


