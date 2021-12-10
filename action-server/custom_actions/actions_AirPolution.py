import requests
from rasa_sdk import Tracker, Action
from rasa_sdk.types import DomainDict
from typing import Dict, Text, Any, List
from rasa_sdk.events import SlotSet, EventType, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

class ActionAirPolution(Action):
    def name(self) -> Text:

        return "action_Air_Polution"

    async def run(
            self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """The custom action will take a location to search from the chatbot slots and
            sets the airPolution slot associated with the location
        """
        
        airPolution = None
        status = None
        appID = WEATHER_API_KEY
        lat = tracker.get_slot('lat')
        lon = tracker.get_slot('lon')
        if lat and lon:
            URL = f'https://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={appID}'
            # Current Air Polution
            # http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API key}
            # https://api.openweathermap.org/data/2.5/air_pollution/forecast?lat=50&lon=50&appid={API key}

            # # Historical Air Polution
            # http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start}&end={end}&appid={API key}

            with requests.session() as sess:
                try:
                    response = sess.get(URL)
                    status = response.status_code
                    if status == 200:
                        airPolution = response.json().get('result')
                        dispatcher.utter_message(f'Air Polution for Location {lat}, {lon} : {airPolution}')
                        return [SlotSet('airPolution', airPolution)]
                    else:
                        dispatcher.utter_message(f'No Air Polution Data for Location {lat}, {lon} found')
                except:
                    dispatcher.utter_message("Exception - No Air Polution Data for Location {lat}, {lon} found")
        else:
            dispatcher.utter_message(
                f'Incorrect location information provided, need a lat and long coordinate')