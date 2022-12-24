from indeed import search_indeed
from save import save_to_csv
from upload_gs_csv import up_gs_csv

search = 'python'

result_indeed = search_indeed(search)

save_to_csv(result_indeed)

up_gs_csv()
