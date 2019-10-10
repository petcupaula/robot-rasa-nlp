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

class ActionGetDaysInMonth(Action):

    def name(self) -> Text:
        return 'action_get_daysinmonth'

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        from datetime import datetime
        from calendar import monthrange, month_abbr, month_name

        today = datetime.today()
        month_now = today.strftime("%B")
        year_now = today.year

        saved_month = (month_now, tracker.get_slot('month'))[bool(tracker.get_slot('month'))]
        saved_month = saved_month[0].upper() + saved_month[1:3].lower()

        month_to_num = {name: num for num, name in enumerate(month_abbr) if num}
        month_num = month_to_num[saved_month]
        days = monthrange(year_now,month_num)[1]

        response = """{} has {} days.""".format(month_name[month_num], days)
        dispatcher.utter_message(response)

        return []

class ActionGetNews(Action):

    def name(self) -> Text:
        return 'action_get_news'

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        import requests
        import json

        topic = ('all', tracker.get_slot('topic'))[bool(tracker.get_slot('topic'))]

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

class ActionChitchat(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return 'action_chitchat'

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')

        # retrieve the correct chitchat utterance dependent on the intent
        if intent in ['ask_builder', 'ask_gender', 'ask_good', 
                      'ask_hobbies','ask_howbuilt', 'ask_howdoing',
                      'ask_howold', 'ask_languages', 'ask_openpod', 
                      'ask_otherbots','ask_plan', 'ask_real', 
                      'ask_secret', 'ask_sing', 'ask_wherefrom', 
                      'ask_wherelive', 'ask_whoisit', 'ask_restaurant']:
            dispatcher.utter_template('utter_' + intent, tracker)

        return []

class ActionMotorTask(Action):

    def name(self) -> Text:
        return 'action_motortask'

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        body_part = motor_action = direction = ""

        entities = tracker.latest_message['entities']

        for e in entities:
            if e['entity'] == 'body_part':
                body_part = e['value']
            elif e['entity'] == 'motor_action':
                motor_action = e['value']
            elif e['entity'] == 'direction':
                direction = e['value']
        
        print(",".join([body_part, motor_action, direction]))

        return []

