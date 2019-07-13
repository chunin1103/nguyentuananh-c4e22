import xlsxwriter
from crawl_nchmf_gov     import low_gov,     high_gov,      des_gov      
from crawl_vtv           import low_vtv,     high_vtv,      des_vtv
from crawl_weatherdotcom import low_weather, high_weather,  des_weather


workbook = xlsxwriter.Workbook('Weather Forecast.xlsx')
worksheet = workbook.add_worksheet('Weather Forecast')
bold   = workbook.add_format({'bold': True})
center = workbook.add_format({'align': 'center'})

worksheet.write('A2', 'Actual', bold)
worksheet.write('A5', 'Nchmf.gov', bold)
worksheet.write('A14', 'Vtv', bold)
worksheet.write('A21', 'Weather.com', bold)


# # Google Api
worksheet.set_column('A:A', 40) 
worksheet.write_row('B5', des_gov)
worksheet.write_row('B6', high_gov)
worksheet.write_row('B7', low_gov)
worksheet.write_row('B14', des_vtv)
worksheet.write_row('B15', high_vtv)
worksheet.write_row('B16', low_vtv)
worksheet.write_row('B21', des_weather)
worksheet.write_row('B22', high_weather)
worksheet.write_row('B23', low_weather)




