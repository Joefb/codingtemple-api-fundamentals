import re
import requests
import random


class ImBored:
    def __init__(self, name):
        self.name = name
        self.base_url = "https://bored-api.appbrewery.com/"

    def get_response(self, filter):
        """
        Method to handle GET requests
        Parses data and returns
        """
        # Get response
        response = requests.get(self.base_url + filter)

        # Check response, error if not 200
        if response.status_code != 200:
            return f"Invalid response from: {self.base_url} - {response.status_code}"

        # If status 200 parse json to python
        if response.status_code == 200:
            parsed_data = response.json()
            return parsed_data

    def validate_input(self, num1, num2):
        """
        Validite user input
        num1 and num2 are the amount of options the calling method has
        """

        invalid_response = f"Invalid Response. Choose {num1}-{num2}."

        while True:
            response = input(f"Choose an option ({num1}-{num2}): ")
            try:
                if int(response) < num1 or int(response) > num2:
                    print(invalid_response)
                    continue

            except ValueError:
                print(invalid_response)

                continue

            else:
                break

        return int(response)

    def im_bored_cli(self):
        """
        Print the main menu
        """

        print("""
        Im Soooo Bored Activity Finder!
        ===============================
        1. Get a Random Activity
        2. Get Activity by Type
        3. Get Activity by Participans
        4. Save my Favorite Activities
        5. View my Favorite Activities
        6. Exit
        """)

    def print_activity(self, type, activity):
        """
        Prints the activity for the calling method
        Takes in type of acvivity and activity dict
        """
        activity_dict = activity

        print(f"""
        {type} Activity Suggestion:
        ---------------------------------
        Activity: {activity_dict["activity"]}
        Type: {activity_dict["type"]}
        Participants: {activity_dict["participants"]}
        Price: {activity_dict["price"]}
        Web Link: {activity_dict["link"]}
        Accessibility: {activity_dict["accessibility"]}
        ----------------------------------

        """)

    def get_random_activity(self):
        """
        Get a random activity

        API Endpoint: https://bored-api.appbrewery.com/random
        """
        # Get response
        response = self.get_response("random")
        return response

    def get_activity_by_type(self):
        """
        Gets activity by type
        Ask user what type of activity they would like
        Validate input
        Send request
        """

        print("What type of activity would you like to choose?")
        print("""
            1: Education
            2: Recreational
            3: Social
            4: Charity
            5: Cooking
            6: Relaxation
            7: Music
            8: Busywork
            9: DIY
              """)

        # Get input
        type_input = self.validate_input(1, 9)

        # Query param
        filter = ""

        if type_input == 1:
            filter = "filter?type=education"

        elif type_input == 2:
            filter = "filter?type=recreational"

        elif type_input == 3:
            filter = "filter?type=social"

        elif type_input == 4:
            filter = "filter?type=charity"

        elif type_input == 5:
            filter = "filter?type=cooking"

        elif type_input == 6:
            filter = "filter?type=relaxation"

        elif type_input == 7:
            filter = "filter?type=music"

        elif type_input == 8:
            filter = "filter?type=busywork"

        elif type_input == 9:
            filter = "filter?type=diy"

        response = self.get_response(filter)
        return response

    def get_activity_by_participants(self):
        """
        Get activity by participants
        Get num of participants from user
        Get response from bored-api
        Display outupt
        """

        print("""
            Omg I have Friends!
            Can have upto 8 friends!
            -----------------------
            How many participants will you have?
             """)

        # Get user input
        user_input = self.validate_input(1, 8)
        response = self.get_response(f"filter?participants={user_input}")
        return response

    def save_activity(self, activity):
        pass

    def print_saved_activities(self):
        pass


def main():
    bored = ImBored("Im Soooo Bored!")

    while True:
        bored.im_bored_cli()
        get_activity = bored.validate_input(1, 6)
        activity = None

        # Quit
        if get_activity == 6:
            print("Thanks for using Im Soooo Bored!")
            print("Have a good day!! Hope you enjoyed!")
            exit()

        # Random
        if get_activity == 1:
            activity = bored.get_random_activity()
            bored.print_activity("Random", activity)

        # By Type
        if get_activity == 2:
            activity = bored.get_activity_by_type()
            random_acvivity = random.choice(activity)
            bored.print_activity("By Type", random_acvivity)

        if get_activity == 3:
            activity = bored.get_activity_by_participants()
            random_acvivity = random.choice(activity)
            bored.print_activity("By Participants", random_acvivity)


if __name__ == "__main__":
    main()

##### TESTING AREA #####
# bored = ImBored("Boredom Buster")
# bored.im_bored_cli()
# # print(bored.get_random_activity())
