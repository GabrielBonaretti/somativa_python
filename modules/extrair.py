import pandas as pd


class Extrair:
    def __init__(self, lista_ids, lista_nomes, lista_marcas, lista_precos, lista_lojas):
        self.celulares = {
            'ID': lista_ids,
            'Nome': lista_nomes,
            'Modelo': lista_marcas,
            'Preço': lista_precos,
            'Loja': lista_lojas
        }

    def criar_excel(self):
        df = pd.DataFrame(self.celulares)
        
        writer = pd.ExcelWriter('./files/Table.xlsx', engine='xlsxwriter')

        df.to_excel(writer, sheet_name="Sheet1", index=False)

        workbook = writer.book

        worksheet = writer.sheets['Sheet1']

        chart = workbook.add_chart({'type': 'column'})

        print(str(len(self.celulares["Preço"]) + 1))

        chart.add_series({'categories': f'=Sheet1!$B$2:$B${str(len(self.celulares["Preço"]) + 1)}',
                          'values': f'=Sheet1!$D$2:$D${str(len(self.celulares["Preço"]) + 1)}'})

        worksheet.insert_chart('G1', chart)

        writer.close()

    def criar_csv(self):
        df = pd.DataFrame(self.celulares)
        
        df.to_csv("./files/file.csv", header=False)
