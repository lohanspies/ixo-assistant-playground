import requests
from rasa_sdk import Tracker, Action
from rasa_sdk.types import DomainDict
from typing import Dict, Text, Any, List
from rasa_sdk.events import SlotSet, EventType, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from arcgis.gis import GIS
from arcgis.geocoding import geocode, reverse_geocode
from arcgis.geometry import lengths
from arcgis.gis import GIS
from arcgis.mapping import WebMap
import base64
import uuid

class ActionESRI(Action):
    def name(self) -> Text:

        return "action_ESRI"

    async def run(
            self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """The custom action will take the chainId, DID and location to search from the chatbot slots and
            sets the base64EsriImage slot associated with DID in that network if exists
        """

        chainId = tracker.get_slot('chainId')
        DID = tracker.get_slot('DID')
        locationSearch = tracker.get_slot('location')
        base64EsriImage = None
        status = None
        filename = str(uuid.uuid4()) + '.png'

        if chainId and DID and locationSearch:
            # instantiate the ArcGIS API
            gis = GIS()
            map1 = gis.map()
            map1.basemap = "satellite"
            map1.height = '650px'
            map.zoom = 14

            try:
                if isinstance(locationSearch, str):
                    location = geocode(locationSearch)[0]
                    print(location)
                    map1.extent = location['extent']
                    map1.take_screenshot(True, True, filename)
                    with open(filename, "rb") as imageFile:
                        str = base64.b64encode(imageFile.read())

                        base64EsriImage = '<img src="data:image/png;base64,' + str.decode().__str__() + '">'
                        print(base64EsriImage)
                        dispatcher.utter_message(f'ESRI Image for location [string] {locationSearch} : {base64EsriImage}')
                        return [SlotSet('base64EsriImage', base64EsriImage)]

                elif isinstance(locationSearch, list):
                    results = reverse_geocode(locationSearch)
                    print(results)
                    location = geocode(results['address']['LongLabel'])[0]
                    print(location)
                    map1.extent = location['extent']
                    map1.take_screenshot(True, True, filename)
                    with open(filename, "rb") as imageFile:
                        str = base64.b64encode(imageFile.read())

                        base64EsriImage = '<img src="data:image/png;base64,' + str.decode().__str__() + '">'
                        print(base64EsriImage)
                        dispatcher.utter_message(f'ESRI Image for location [lat,long] {locationSearch} : {base64EsriImage}')
                        return [SlotSet('base64EsriImage', base64EsriImage)]
                else:
                    dispatcher.utter_message(f'{locationSearch} is not a string or list')
            except:
                dispatcher.utter_message("The location provided is not valid. A string or [lat,long] is accepted")

        else:
            dispatcher.utter_message(
                f'The location {locationSearch} was not found, or does not have an associated Geocode lookup result')