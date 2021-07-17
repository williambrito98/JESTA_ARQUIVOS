class Save:
    @staticmethod
    def save(df, path):
        df.to_csv(path, header=False, mode='a', encoding='latin-1', sep=';', index=False)
