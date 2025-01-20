init python:
    def show_custom_notification(message):
        renpy.play("audio/error.wav")  # Play error sound if needed
        renpy.show_screen("custom_notification", message=message)  # Show custom notification screen
        renpy.pause(3.0)  # Delay for 3 seconds
