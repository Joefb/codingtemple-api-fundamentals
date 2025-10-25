import requests
import random
import json
import os


class ImBored:
    def __init__(self, name):
        self.name = name
        self.base_url = "https://bored-api.appbrewery.com/"

        with open("my_favs_data.json", "r") as f:
            self.my_favs_data = json.load(f)

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

        invalid_response = f"\nInvalid Response. Choose {num1}-{num2}.\n"

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
        4. Save to Favorite Activities
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
        Web Link: {activity_dict["link"]}
        Accessibility: {activity_dict["accessibility"]}
        ----------------------------------

        """)

    def get_random_activity(self):
        """
        Get a random activity
        Get response and return results
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

        os.system("cls" if os.name == "nt" else "clear")
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

        # Set the query param
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

        # Get response and return
        response = self.get_response(filter)
        return response

    def get_activity_by_participants(self):
        """
        Get activity by participants
        Get num of participants from user
        Validite input
        Get response from bored-api
        Display outupt
        """

        os.system("cls" if os.name == "nt" else "clear")
        print("""
            Omg I have Friends!
            Can have upto 8 friends!
            -----------------------
            How many participants will you have?
             """)

        # Get user input and validate inupt
        user_input = self.validate_input(1, 8)
        response = self.get_response(f"filter?participants={user_input}")
        return response

    def save_activity(self, activity):
        """
        Save activity
        Append dict
        Dump to file
        """
        self.my_favs_data.append(activity)

        with open("my_favs_data.json", "w") as f:
            json.dump(self.my_favs_data, f, indent=4)

        return

    def print_saved_activities(self):
        """
        Print saved activities
        Iterate through saved activities dict and print
        """

        for dicts in self.my_favs_data:
            self.print_activity("My Favorites", dicts)


def main():
    bored = ImBored("Im Soooo Bored!")
    activity = None

    # Main loop
    while True:
        bored.im_bored_cli()
        get_activity = bored.validate_input(1, 6)

        # Quit
        if get_activity == 6:
            os.system("cls" if os.name == "nt" else "clear")
            print("======================================")
            print("Thanks for using Im Soooo Bored!")
            print("Have a good day!! Hope you enjoyed!")
            print("======================================")
            exit()

        # Random
        elif get_activity == 1:
            activity = bored.get_random_activity()
            bored.print_activity("Random", activity)

        # By Type
        elif get_activity == 2:
            activity = bored.get_activity_by_type()
            acvivity = random.choice(activity)
            bored.print_activity("By Type", acvivity)

        # By participants
        elif get_activity == 3:
            activity = bored.get_activity_by_participants()
            acvivity = random.choice(activity)
            bored.print_activity("By Participants", acvivity)

        # Save activity
        elif get_activity == 4:
            if not activity:
                print("\nYou must get a activity first!\n")
                continue

            else:
                print("=====================")
                print("Saving Activity")
                bored.save_activity(activity)
                print("Activity Saved!")
                print("=====================")

        elif get_activity == 5:
            os.system("cls" if os.name == "nt" else "clear")
            bored.print_saved_activities()


if __name__ == "__main__":
    main()
