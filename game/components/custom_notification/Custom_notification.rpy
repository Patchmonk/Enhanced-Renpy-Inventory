init python:
    def show_custom_notification(message, sound_type="default"):
        sound_map = {
            "default": "components/custom_notification/audio/notification.mp3",  # Default notification sound
            "error": "components/custom_notification/audio/error.mp3",           # Error notification sound
            "success": "components/custom_notification/audio/success.mp3",       # Success notification sound
            "remove": "components/custom_notification/audio/remove.mp3",         # remove notification sound   
            # Add more sound types here
        }

        # Play the appropriate sound based on sound_type
        if sound_type in sound_map:
            renpy.play(sound_map[sound_type])
        else:
            renpy.play(sound_map["default"])

        # Show the custom notification screen
        renpy.show_screen("custom_notification", message=message)
        renpy.pause(3.0)  # Delay for 3 seconds
