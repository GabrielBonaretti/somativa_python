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
        # data
        df = pd.DataFrame(self.celulares)

        # create writer object
        writer = pd.ExcelWriter('./files/Table.xlsx', engine='xlsxwriter')

        # add data to the sheet
        df.to_excel(writer, sheet_name="Sheet1", index=False)

        # get workbook
        workbook = writer.book

        # get sheet for conditional formatting
        worksheet = writer.sheets['Sheet1']

        # create chart object
        chart = workbook.add_chart({'type': 'column'})

        print(str(len(self.celulares["Preço"]) + 1))

        # configure the series of the chart from the dataframe data
        chart.add_series({'categories': f'=Sheet1!$B$2:$B${str(len(self.celulares["Preço"]) + 1)}',
                          'values': f'=Sheet1!$D$2:$D${str(len(self.celulares["Preço"]) + 1)}'})

        # insert chart into the worksheet
        worksheet.insert_chart('G1', chart)

        # close file
        writer.close()

    def criar_csv(self):
        df = pd.DataFrame(self.celulares)

        # Write DataFrame to CSV File with Default params.
        df.to_csv("./files/file.csv", header=False)
