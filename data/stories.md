## happy path
* greet_hello
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet_hello
  - utter_greet
* mood_unhappy
  - utter_sad
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet_hello
  - utter_greet
* mood_unhappy
  - utter_sad
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* greet_goodbye
  - utter_goodbye

## chitchat / bot challenge
* ask_real OR ask_whoisit OR ask_builder OR ask_howdoing OR ask_languages OR ask_howold OR ask_gender OR ask_wherelive OR ask_howbuilt OR ask_hobbies OR ask_otherbots OR ask_plan OR ask_sing OR ask_good OR ask_restaurant OR ask_wherefrom OR ask_openpod OR ask_secret
  - action_chitchat

## user asks for a joke story 1
* ask_joke
  - utter_ask_joke

## user asks for a joke story 2
* ask_joke
  - utter_ask_joke
* ask_one_more
  - utter_ask_joke

## user asks for time
* ask_time
  - action_get_time

## user asks for date
* ask_date
  - action_get_date

## user asks for days in month
* ask_days_in_month{"month": "January"}
  - slot{"month": "January"}
  - action_get_daysinmonth

## user asks for days in month story 2
* ask_days_in_month
  - slot{"month": null}
  - action_get_daysinmonth

## user asks what it can do
* ask_howhelp
  - utter_howhelp

## user asks for something out of scope
* out_of_scope
  - utter_out_of_scope

## simple acknowledgement
* opinion+positive
  - utter_positive_feedback_reaction

## user says sorry
* sorry
  - utter_nosorry

## user expresses feeling:love
* feeling_love
  - utter_handlelove

## user expresses feeling:insult
* feeling_insult
  - utter_handleinsult

## Short story with love
* greet_hello
    - utter_greet
* ask_howold
    - utter_ask_howold
* feeling_love
    - utter_handlelove

## Robot initiates dialogue
- utter_dialogstarter
  * affirm

## Nice to meet you
* nicetomeetyou
  - utter_nicetomeetyoutoo

## my name is
* my_name_is
  - utter_nicetomeetyou

## get weather story 1
* greet_hello
    - utter_greet
* ask_weather
    - utter_ask_location
* ask_weather{"GPE": "italy"}
    - slot{"GPE": "italy"}
    - action_get_weather
    - slot{"GPE": "italy"}
* greet_goodbye
    - utter_goodbye

## get weather story 2
* greet_hello
    - utter_greet
* ask_weather{"GPE": "London"}
    - slot{"GPE": "London"}
    - action_get_weather
* greet_goodbye
    - utter_goodbye

## get weather story 3
* greet_hello
    - utter_greet
* ask_weather
    - utter_ask_location
* ask_weather{"GPE":"London"}
    - slot{"GPE": "London"}
    - action_get_weather
* greet_goodbye
    - utter_goodbye

## get weather story 4
    - slot{"GPE": "London"}
    - action_get_weather
* greet_goodbye
    - utter_goodbye
    
## get weather story 5
    - slot{"GPE": "London"}
    - action_get_weather
* greet_goodbye
    - utter_goodbye

## get weather story 6
* greet_hello
   - utter_greet
* ask_weather
   - utter_ask_location
* ask_weather{"GPE":"London"}
   - slot{"GPE": "London"}
   - action_get_weather
* greet_goodbye
   - utter_goodbye

## get weather story 7
* greet_hello
   - utter_greet
* ask_weather{"GPE":"Paris"}
   - slot{"GPE": "Paris"}
   - action_get_weather
* greet_goodbye
   - utter_goodbye 

## get weather story 8
* greet_hello
   - utter_greet
* ask_weather
   - utter_ask_location
* ask_weather{"GPE":"Vilnius"}
   - slot{"GPE": "Vilnius"}
   - action_get_weather
* greet_goodbye
   - utter_goodbye

## get weather story 9
* greet_hello
   - utter_greet
* ask_weather{"GPE":"Italy"}
   - slot{"GPE": "Italy"}
   - action_get_weather
* greet_goodbye
   - utter_goodbye 

## get weather story 10
* greet_hello
   - utter_greet
* ask_weather
   - utter_ask_location
* ask_weather{"GPE":"Lithuania"}
   - slot{"GPE": "Lithuania"}
   - action_get_weather
* greet_goodbye
   - utter_goodbye

## get news story 1
* ask_news
  - action_get_news

## get news story 2
* greet_hello
  - utter_greet
* ask_news{"topic":"technology"}
  - slot{"topic":"technology"}
  - action_get_news
* thank
  - utter_thanks_response

## get news story 3
* greet_hello
  - utter_greet
* ask_news
  - action_get_news
* greet_goodbye
  - utter_goodbye

## get news story 4
* greet_hello
  - utter_greet
* ask_news{"topic":"business"}
  - slot{"topic":"business"}
  - action_get_news
* greet_goodbye
  - utter_goodbye

## reflect story 1
* greet_hello
  - utter_greet
* reflect_i_feel
  - utter_reflect_feel

## reflect story 2
* reflect_dream
  - utter_reflect_dream
* reflect_i_want
  - utter_reflect_want
* reflect_i_remember
  - utter_reflect_remember
* reflect_if_i
  - utter_reflect_if_i

## reflect story 3
* reflect_i_cant
  - utter_reflect_cant
* reflect_everyone
  - utter_reflect_everyone
* reflect_always
  - utter_reflect_always
* reflect_am_i
  - utter_reflect_am_i

## reflect story 4
* reflect_is_like
  - utter_reflect_is_like
* reflect_always
  - utter_reflect_always
* reflect_i_feel
  - utter_reflect_feel

## reflect story 5
* reflect_ask_remember
  - utter_reflect_ask_remember
* reflect_never
  - utter_reflect_never

## reflect story 6
* greet_hello
    - utter_greet
* mood_great
    - utter_happy
* reflect_ask_remember
    - utter_reflect_ask_remember
