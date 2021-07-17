import pandas as pd


class Create:

    @staticmethod
    def create(path):
        return pd.read_csv(path, sep=';', skipfooter=1, engine='python', encoding='latin-1',
                           error_bad_lines=False)
