import requests
from rasa_sdk import Tracker, Action
from rasa_sdk.types import DomainDict
from typing import Dict, Text, Any, List
from rasa_sdk.events import SlotSet, EventType, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher

class ActionDIDToAddr(Action):
    def name(self) -> Text:

        return "action_did_to_addr"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """The custom action will take the chainId and DID from the chatbot slots and
            sets the accountAddress slot associated with DID in that network if exists
        """

        DID = next(tracker.get_latest_entity_values('DID'), None)
        print('The DID is: ', DID)
        chainId = 'impacthub'
        # chainId = tracker.get_slot('chainId')
        if not DID:
            DID = tracker.get_slot('DID')
        accountAddress = None
        status = None
        if chainId and DID:
            URL = f'https://impacthub.ixo.world/didToAddr/{DID}'
            
            with requests.session() as sess:
                try:
                    response = sess.get(URL)
                    status = response.status_code
                    if status == 200:
                        accountAddress = response.json().get('result')
                        dispatcher.utter_message(f'Address for DID {DID} : {accountAddress}')
                        return [SlotSet('accountAddress', accountAddress)]
                    else:
                        dispatcher.utter_message(f'Address for DID {DID} is not found')
                except:
                    dispatcher.utter_message("The network was not found")
        else:       
            dispatcher.utter_message(f'This identity {DID} was not found, or does not have an associated Account Address')


class ActionRememberDID(Action):

    def name(self) -> Text:
        return "action_remember_DID"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_DID = next(tracker.get_latest_entity_values("DID"), None)

        if not current_DID:
            msg = "I didn't get your DID. Are you sure it's spelled correctly?"
            dispatcher.utter_message(text=msg)
            return []

        msg = f"Sure thing! I'll remember that your DID is {current_DID}."
        dispatcher.utter_message(text=msg)

        return [SlotSet("DID", current_DID)]