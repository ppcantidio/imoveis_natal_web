from utils.database import Database


class Imoveis():
    def __init__(self):
        self.db = Database()
        

    def imoveis(self):
        imoveis = self.db.select_all_objects('imoveis')

        cont = 0
        for imovel in imoveis:
            corretor = self.db.select_one_object('usuarios', {'_id': imovel['corretor_id']})
            imovel['corretor_nome'] = corretor['nome']

            valor = '{0:,}'.format(imoveis[cont]['valor'])
            imoveis[cont]['valor'] = valor.replace(',', '.')

            cont += 1

        return imoveis


    def imovel(self, imovel_id):
        imovel = self.db.select_one_object('imoveis', {'_id': imovel_id})

        if imovel is None:
            return None

        corretor = self.db.select_one_object('usuarios', {'_id': imovel['corretor_id']})

        imovel['corretor_nome'] = corretor['nome']


        return imovel