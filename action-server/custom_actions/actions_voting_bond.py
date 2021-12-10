
import requests
from rasa_sdk import Tracker, Action
from rasa_sdk.types import DomainDict
from typing import Dict, Text, Any, List
from rasa_sdk.events import SlotSet, EventType, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher

class ActionVotingBond(Action):
    def name(self) -> Text:

        return "action_voting_bond"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """The custom action will receive the bond_did 
            from the chatbot intent triggers and
            sets the state of the bond to bond_state slot
        """
        
        bond_did = tracker.get_slot("bond_did")
        chainId = tracker.get_slot('chainId')
        state = None
        if chainId and bond_did:
            
            URL = f'https://{chainId}.ixo.world/bonds/{bond_did}'
            with requests.session() as sess:
                try:
                    response = sess.get(URL)
                    status = response.status_code
                    if status == 200:
                        state = response.json().get('result', {}).get('value', {}).get('state')
                        dispatcher.utter_message(f'Bond State for Bond DID {bond_did} : {state}')
                        return [SlotSet('bond_state', state)]
                    else:
                        dispatcher.utter_message(f'State for Bond DID:  {bond_did} is not found')
                except:
                    dispatcher.utter_message("The network was not found")
        else:       
            dispatcher.utter_message(f'This bond_state for {bond_did} was not found, or does not have any state')