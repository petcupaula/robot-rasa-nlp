# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

import os
from dotenv import dotenv_values
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

os.environ.update(dotenv_values())

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []

class ActionGetWeather(Action):
    # Based on code here: https://github.com/JustinaPetr/Weatherbot_Tutorial/blob/master/Full_Code_Latest/actions.py

    def name(self) -> Text:
        return 'action_get_weather'

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        from apixu.client import ApixuClient
        api_key = os.environ['APIXUKEY']
        client = ApixuClient(api_key=api_key, lang="en")
        
        loc = ('Copenhagen', tracker.get_slot('GPE'))[bool(tracker.get_slot('GPE'))]
        current = client.current(q=loc)
        
        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_mph']

        response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
                        
        dispatcher.utter_message(response)
        return [SlotSet('GPE',loc)]

class ActionGetDate(Action):

    def name(self) -> Text:
        return 'action_get_date'

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        from datetime import datetime
        today = datetime.today()
        datetoday = today.strftime("%B %d, %Y")
        daytoday = today.strftime("%A")

        response = """Today is {}, {}.""".format(daytoday, datetoday)
        dispatcher.utter_message(response)

        return []

class ActionGetTime(Action):

    def name(self) -> Text:
        return 'action_get_time'

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        from datetime import datetime
        now = datetime.now().strftime("%H %M")

        response = """It is {}.""".format(now)
        dispatcher.utter_message(response)

        return []

class ActionGetNews(Action):

    def name(self) -> Text:
        return 'action_get_news'

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        import requests
        import json

        topic = tracker.get_slot('topic')
        if not topic: 
            topic = 'all'
        url = 'https://api.nytimes.com/svc/news/v3/content/all/{topic}.json'.format(topic=topic)
        api_key = os.environ['NYTKEY']
        params = {'api-key': api_key, 'limit': 5}
        response = requests.get(url, params).text
        json_data = json.loads(response)['results']
        i = 0
        
        for results in json_data:
            i = i+1
            message = str(i) + "." + results['abstract']
            dispatcher.utter_message(message)
        return []
