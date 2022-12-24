import gspread
from oauth2client.service_account import ServiceAccountCredentials

def up_gs_csv():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret_cs.json', scope)
    client = gspread.authorize(credentials)

    spreadsheet = client.open('lista_jobs')

    with open('jobs.csv', 'r') as file_obj:
        content = file_obj.read()
        client.import_csv(spreadsheet.id, data=content)
