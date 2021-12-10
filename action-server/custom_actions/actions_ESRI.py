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

        # chainId = tracker.get_slot('chainId')
        # DID = tracker.get_slot('DID')
        locationSearch = next(tracker.get_latest_entity_values('location'), None)
        base64EsriImage = None
        status = None
        filename = '~/imagefile.png'
        print("Location", locationSearch)

        if not locationSearch:
                        dispatcher.utter_message('No location detected')
        else:
            dispatcher.utter_message(f'Searching for Image at location {locationSearch}')

            # instantiate the ArcGIS API
            gis = GIS()
            map1 = gis.map()
            map1.basemap = "satellite"
            map1.height = '650px'
            map1.zoom = 14

            try:
                if isinstance(locationSearch, str):

                    location = geocode(locationSearch)[0]
                    print("Geocode Location", location)
                    print("before", filename)
                    map1.extent = location['extent']
                    print("FETCH WEBMAP")
                    wm1 = WebMap(location["extent"])

                    print("GETWEBMAPITEM")
                    print(map1)
                    webmapitem = map1.save({'title':locationSearch,
                             'snippet':'your map',
                             'tags':'location'})
                    print("FOUNDWM")
                    wm = WebMap(webmapitem)
                    map_url = wm.print(file_format='JPG')
                    print("MAP URL", map_url)
                    with requests.get(map_url) as resp:
                        with open(filename, 'wb') as file_handle:
                            print("MAPCONTENT", resp.content)
                            file_handle.write(resp.content)
                    print(filename, "after load")
                    with open(filename, "rb") as imageFile:
                        print("Base 64 Image", base64EsriImage)
                        imageString = base64.b64encode(imageFile.read())

                        base64EsriImage = '<img src="data:image/png;base64,' + imageString.decode().__str__() + '">'
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
                        imageString = base64.b64encode(imageFile.read())

                        base64EsriImage = '<img src="data:image/png;base64,' + imageString.decode().__str__() + '">'
                        print(base64EsriImage)
                        dispatcher.utter_message(f'ESRI Image for location [lat,long] {locationSearch} : {base64EsriImage}')
                        return [SlotSet('base64EsriImage', base64EsriImage)]
                else:
                    dispatcher.utter_message(f'{locationSearch} is not a string or list')
            except Exception as err:
                print("Exception", err)
                dispatcher.utter_message("The location provided is not valid. A string or [lat,long] is accepted")

        # else:
        #     dispatcher.utter_message(
        #         f'The location {locationSearch} was not found, or does not have an associated Geocode lookup result')