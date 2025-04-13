###################################################################################################################
# ██████╗  █████╗ ████████╗ ██████╗██╗  ██╗███╗   ███╗ ██████╗ ███╗   ██╗██╗  ██╗                                 #
# ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║  ██║████╗ ████║██╔═══██╗████╗  ██║██║ ██╔╝                                 #
# ██████╔╝███████║   ██║   ██║     ███████║██╔████╔██║██║   ██║██╔██╗ ██║█████╔╝                                  #
# ██╔═══╝ ██╔══██║   ██║   ██║     ██╔══██║██║╚██╔╝██║██║   ██║██║╚██╗██║██╔═██╗                                  #
# ██║     ██║  ██║   ██║   ╚██████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║  ██╗                                 #
# ╚═╝     ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝                                 #
###################################################################################################################
###################################################################################################################
## The notification screen is a simple yet effective way to provide feedback to players in a Ren'Py game.  #
## By utilizing frames, styles, and timers, you can create a visually appealing notification that enhances the    #
## overall user experience.                                                                                       #
###################################################################################################################


# Define a custom notification screen that takes a message as input
screen scrNotification(message):
    frame:
        style "popup"  # Apply the popup style to the frame
        text message style "pm_notify"  # Display the message with the pm_notify style
        timer 3.0 action Hide("scrNotification")  # Hide the notification after 3 seconds
        background "components/notification/images/gui/notification.png"


