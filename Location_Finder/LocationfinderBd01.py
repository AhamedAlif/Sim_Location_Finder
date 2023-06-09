import requests
from halo import Halo
import webbrowser


logo = '''
     _____ _____ __  __   _                     _   _               ______ _           _           
    / ____|_   _|  \/  | | |                   | | (_)             |  ____(_)         | |          
   | (___   | | | \  / | | |     ___   ___ __ _| |_ _  ___  _ __   | |__   _ _ __   __| | ___ _ __ 
    \___ \  | | | |\/| | | |    / _ \ / __/ _` | __| |/ _ \| '_ \  |  __| | | '_ \ / _` |/ _ \ '__|
    ____) |_| |_| |  | | | |___| (_) | (_| (_| | |_| | (_) | | | | | |    | | | | | (_| |  __/ |   
   |_____/|_____|_|  |_| |______\___/ \___\__,_|\__|_|\___/|_| |_| |_|    |_|_| |_|\__,_|\___|_|   
                                                                                                   
'''


def display_sim_info(data):
    if "Sim Info" in data:
        sim_info = data["Sim Info"]
        if isinstance(sim_info, str) and sim_info == "Number Info Not Found":
            print("SIM information not found for the given input.")
        else:
            if "Number" in data:
                print(f"- Number: {data['Number']}")

            if isinstance(sim_info, dict):
                print("SIM Details:")
                for key, value in sim_info.items():
                    print(f"- {key.replace('_', ' ').title()}: {value}")
                    if key == "User_LOC_LAT" and value and "User_LOC_LONG" in sim_info:
                        loc_lat = value
                        loc_long = sim_info["User_LOC_LONG"]
                        # Generate the Google Maps URL with location coordinates
                        google_maps_url = f"https://www.google.com/maps/search/?api=1&query={loc_lat},{loc_long}"
                        print(f"\nGoogle Maps Location: {google_maps_url}")
                        # Open the Google Maps URL in a web browser
                        webbrowser.open_new_tab(google_maps_url)
    else:
        print("Invalid response format.")


def get_sim_info(sim_input):
    # Build the URL with the input
    url = f"https://spamx.id/info/?sim={sim_input}"

    spinner = Halo(text='Finding SIM information...', spinner='dots')
    spinner.start()

    # Send a request to the URL
    response = requests.get(url)

    spinner.stop()

    # Process the response
    if response.status_code == 200:
        data = response.json()
        display_sim_info(data)
    else:
        print("Error: Failed to retrieve information from the URL.")


def main():
    print(logo)
    print("━━━━━━━━━━━━━━━━━━━")
    print("SIM Location Finder")
    print("━━━━━━━━━━━━━━━━━━━")
    print("Note: Only for Robi and Airtel\n")

    while True:
        sim_input = input("Enter the SIM NUMBER (or 'q' to quit): ")

        if sim_input.lower() == 'q':
            print("Exiting the SIM Location Finder.")
            break

        get_sim_info(sim_input)


if __name__ == "__main__":
    main()
