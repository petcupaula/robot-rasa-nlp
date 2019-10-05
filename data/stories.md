## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_sad
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_sad
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
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

## user asks for a joke
* ask_joke
  - utter_telljoke

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

* greet
    - utter_greet
* ask_howold
    - utter_howold
* feeling_love
    - utter_handlelove
