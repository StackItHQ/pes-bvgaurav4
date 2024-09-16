import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
import os.path

import gspread
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError






SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/script.projects',
    'https://www.googleapis.com/auth/script.deployments',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/script.external_request',
    'https://www.googleapis.com/auth/script.scriptapp',
    'https://www.googleapis.com/auth/script.send_mail',
    'https://www.googleapis.com/auth/script.storage',
    'https://www.googleapis.com/auth/script.webapp.deploy'
]

def create(title):
  """
  Creates the Sheet the user has access to.
  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "client_secret_348694015031-1hdg0it1h1el2skt1mnkg5ci1m09lqma.apps.googleusercontent.com.json", SCOPES
      )  # pylint: disable=maybe-no-member
  try:
    service = build("sheets", "v4", credentials=creds)
    spreadsheet = {"properties": {"title": title}}
    spreadsheet = (
        service.spreadsheets()
        .create(body=spreadsheet, fields="spreadsheetId")
        .execute()
    )
    print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
    return spreadsheet.get("spreadsheetId")
  except HttpError as error:
    print(f"An error occurred: {error}")
    return error

def updationg_cells(x,y,value,id,s):
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_authorized_user_file("token.json",scopes=SCOPES)
    client=gspread.authorize(creds)
    SAMPLE_SPREADSHEET_ID=id
    workbook =client.open_by_key(SAMPLE_SPREADSHEET_ID)
    sheet=workbook.worksheet(s)
    print(sheet)
    if sheet:
        cell_address = f"{x}{y}"
        sheet.update_acell(cell_address, value)
        return True
    return False


def to_a1_notation(coordinates):
    column_number, row_number = coordinates
    column_letter = ''
    
    while column_number > 0:
        column_number, remainder = divmod(column_number - 1, 26)
        column_letter = chr(65 + remainder) + column_letter
    
    return f"{column_letter}"
