from datetime import date


class Recebidas:

    def __init__(self, df, config):
        self.df = df
        self.__Config__ = config
        self.month = date.today().month
        self.year = date.today().year

    def init(self):
        self.__adjustCodigServisco__()
        return self.df

    def __adjustCodigServisco__(self):
        self.df['Código do Serviço Prestado na Nota Fiscal'] = self.df[
            'Código do Serviço Prestado na Nota Fiscal'].apply(
            lambda x: self.__Config__['CODIGO_SERVICO'].get(str(x), None)
            if self.__Config__['CODIGO_SERVICO'].get(str(x), None) is not None else x)
        self.df['data'] = str(self.month - 1).zfill(2) + '/' + str(self.year)
