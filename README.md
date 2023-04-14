# BunkerRealms
This is an implementation of Minecraft Realms. 

# Routes

The API provides the following routes:

    `/mco/client/compatible`: Returns a string "COMPATIBLE" to indicate that the client is compatible without checking the cookie data.
    `/mco/available`: Returns a string "true" to indicate that the server is available.
    `/worlds`: Returns a JSON array of servers.
    `/invites/pending`: Returns a list of pending invites in JSON format.
    `/worlds/v1/<int:id>/join/pc`: Returns a server address depending on the ID passed in the route.
    `/mco/v1/news`: Returns a JSON object with a news link.
    `/activities/liveplayerlist`: Returns a string "1" to indicate that there is at least one live player.
    `/trial`: Returns a string "true" to indicate that the client has a free 30-day trial of Realms.
    `/trial` (POST): This endpoint doesn't work properly as the client needs to receive a confirmation.
    `/invites/count/pending`: Returns the number of pending invites.

# Hardcoded Data

Alot of the stuff here is hardcoded and most of the API isnt done.

# How to Run

To run the code, simply execute the script python app.py in a terminal window. The server will listen on port 8000 by default. You can change this by modifying the last line of the script.
Dependencies

This code requires the following Python libraries:

    `Flask`
    `json`

You can install them by running `pip install flask json` in a terminal window.
