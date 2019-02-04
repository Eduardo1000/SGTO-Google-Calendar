import json
from googleapiclient.discovery import build
import pandas as pd

class Calendar():
    def __init__(self, creds):
        self.service = build('calendar', 'v3', credentials=creds)   # Inicia o calendário
        with open('calendar.json') as f:
            self.calendar = json.load(f)            # Carrega os comandos para Calendário
        self.all_calendars = pd.DataFrame(data=None, columns=['id','name'])

    # TODO Método para criar calendário
    def create(self, name):
        self.calendar['summary'] = name
        created_calendar = self.service.calendars().insert(body=self.calendar).execute()
        return created_calendar['id']

    # TODO Método para excluir calendário
    def delete(self, id):
        self.calendar['summary'] = id
        self.service.calendars().delete(calendarId=id).execute()

    # Método para recuperar eventos de um calendário
    def get(self, name='primary'):
        calendar = self.service.calendars().get(calendarId=name).execute()
        print(calendar['summary'])
    
    def list(self):
        page_token = None
        aux = []
        while True:
            calendar_list = self.service.calendarList().list(pageToken=page_token).execute()
            print('Getting all calendars')
            for calendar_list_entry in calendar_list['items']:
                aux.append([calendar_list_entry['id'], calendar_list_entry['summary']])
            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break
        self.all_calendars = pd.DataFrame(data=aux, columns=['id','name'])
        print(self.all_calendars)
        return self.all_calendars           

class Event():
    def __init__(self, creds):
        self.service = build('calendar', 'v3', credentials=creds)   # Inicia o calendário
        with open('event.json') as f: # TODO
            self.event = json.load(f)            # Carrega os comandos para Evento
        
    
    # TODO Método para adicionar Evento a um Calendário
    def create(self, calendar_ID, name, location):
        self.event['summary'] = name
        self.event['location'] = location
        event = self.service.events().insert(calendarId=calendar_ID, body=self.event).execute()
        print( 'Event created: %s' % (event.get('htmlLink') ) )
    # TODO Método para alterar Evento de um Calendário
    # TODO Método para deletar Evento de um Calendário