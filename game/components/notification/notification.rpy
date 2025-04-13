###################################################################################################################
# ██████╗  █████╗ ████████╗ ██████╗██╗  ██╗███╗   ███╗ ██████╗ ███╗   ██╗██╗  ██╗                                 #
# ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║  ██║████╗ ████║██╔═══██╗████╗  ██║██║ ██╔╝                                 #
# ██████╔╝███████║   ██║   ██║     ███████║██╔████╔██║██║   ██║██╔██╗ ██║█████╔╝                                  #
# ██╔═══╝ ██╔══██║   ██║   ██║     ██╔══██║██║╚██╔╝██║██║   ██║██║╚██╗██║██╔═██╗                                  #
# ██║     ██║  ██║   ██║   ╚██████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║  ██╗                                 #
# ╚═╝     ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝                                 #
###################################################################################################################
###################################################################################################################
## The custom notification system implemented in this code snippet is a powerful tool for enhancing user          #
## interaction in Ren'Py games. By allowing different sounds for various notification types, developers can       #
## create a more engaging experience for players. This code is not only easy to understand but also flexible      #
## enough to be adapted for various use cases. Whether you're notifying players of achievements, errors, or       #
## simple updates, this function is a valuable addition to your Ren'Py project. Brought to you by Patchmonk       #
###################################################################################################################
init python:
    def show_notification(message, sound_type="default"):
        sound_map = {
            "default": "components/notification/audio/notification.mp3",  # Default notification sound
            "error": "components/notification/audio/error.mp3",           # Error notification sound
            "success": "components/notification/audio/success.mp3",       # Success notification sound
            "remove": "components/notification/audio/remove.mp3",         # Remove notification sound
            "fanfare": "components/notification/audio/fanfare.mp3",       # You've won the game sound
            "locked": "components/notification/audio/inventory_lock.mp3", # Lock inventory sound
            "dream": "components/notification/audio/dream.ogg",           # Dream transition sound
            "demon_rises": "components/notification/audio/demonRises.ogg",# Upcoming danger\demon
            "drama": "components/notification/audio/audio/dramatic.mp3",  # Add drama
            "suspense": "components/notification/audio/bassSuspense.ogg", # Add suspense
        }

        # Play the appropriate sound based on sound_type
        if sound_type in sound_map:
            renpy.play(sound_map[sound_type])
        else:
            renpy.play(sound_map["default"])

        # Show the custom notification screen
        renpy.show_screen("scrNotification", message=message)
        renpy.pause(3.0)  # Delay for 3 seconds
