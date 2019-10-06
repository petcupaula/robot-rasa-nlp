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

## bot challenge
* ask_real
  - utter_real
* ask_whoisit
  - utter_whoisit
* ask_howold
  - utter_howold
* ask_wherefrom
  - utter_wherefrom
* ask_gender
  - utter_gender
* ask_wherelive
  - utter_wherelive
* ask_languages
  - utter_languages
* ask_howdoing
  - utter_howdoing
* ask_howbuilt
  - utter_howbuilt
* ask_builder
  - utter_builder
* ask_hobbies
  - utter_hobbies
* ask_other_bots
  - utter_otherbots
* ask_plan
  - utter_plan
* ask_sing
  - utter_sing
* ask_good
  - utter_smthinggood

## user asks for a joke story 1
* ask_joke
  - utter_telljoke

## user asks for a joke story 2
* ask_joke
  - utter_telljoke
* ask_one_more
  - utter_telljoke

## user asks for time
* ask_time
  - action_get_time

## user asks for date
* ask_date
  - action_get_date

## Open the pod
* ask_openpod
  - utter_openpod

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
    - utter_howold
* feeling_love
    - utter_handlelove

## Robot initiates dialogue
- utter_dialogstarter
  * affirm

## Nice to meet you
* nicetomeetyou
  - utter_nicetomeetyoutoo

## Tell me a secret
* ask_secret
  - utter_asksecret

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

