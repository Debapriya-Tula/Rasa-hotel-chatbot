# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction


class ValidateHotelForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_book_room_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["room_type", "num_rooms"]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer."""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_room_type(self, value, dispatcher, tracker, domain):
        # input(value)
        if value.lower() in ['simple', 'deluxe']:
            return {'room_type':value}
        else:
            dispatcher.utter_message(template="utter_wrong_room_type")
            return {'room_type': None}

    def validate_num_rooms(self, value, dispatcher, tracker, domain):
        if self.is_int(value) and int(value) > 0:
            return {'num_rooms': value}
        else:
            dispatcher.utter_message(template='utter_wrong_num_rooms')
            return {'num_rooms': None}

    def validate_num_people(self, value, dispatcher, tracker, domain):
        if self.is_int(value) and int(value) > 0:
            return {'num_people': value}
        else:
            dispatcher.utter_message(template='utter_wrong_num_people')
            return {'num_people': None}

    def validate_name(self, value, dispatcher, tracker, domain):
        return {"name": value}

    def validate_age(self, value, dispatcher, tracker, domain):
        if self.is_int(value) and int(value) >= 21 and int(value) <= 100:
            return {'age': value}
        else:
            dispatcher.utter_message(template='utter_wrong_age')
            return {'age': None}


class ValidateCleanRoomForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_clean_room_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["room_number"]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer."""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_room_number(self, value, dispatcher, tracker, domain):
        if self.is_int(value):
            return {"room_number": value}
        else:
            dispatcher.utter_message(template="utter_invalid_room_number")
            return {"room_number": None}


class ValidateCleanRoomRelativeForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_clean_room_relative_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["room_number", "delta_hours"]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer."""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_room_number(self, value, dispatcher, tracker, domain):
        if self.is_int(value):
            return {"room_number": value}
        else:
            dispatcher.utter_message(template="utter_invalid_room_number")
            return {"room_number": None}

    def validate_delta_hours(self, value, dispatcher, tracker, domain):
        if isinstance(eval(value), float) or isinstance(eval(value), int):
            return {"delta_hours": value}
        else:
            dispatcher.utter_message(template="utter_invalid_delta_hours")
            return {"delta_hours": None}
