class FeatureEngineer:

    def feature_engineer(self, df):

        df["bmi"] = df["weight"] / ((df["height"] / 100) ** 2)
        df["age_years"] = df["age"] / 365.25

        return df
