screen custom_notification(message):
    frame:
        style "popup"
        text message style "Pm_notifi"
        timer 3.0 action Hide("custom_notification")
        background "components/custom_notification/images/gui/notification.png"

style popup is frame:
    xsize 1400
    ysize 100
    background "#000000"
   
    xpos 0.5 # Center horizontally
    ypos 0.1
    xanchor 0.5  # Anchor to center

style Pm_notifi:
    ypos 0.3
    xpos 130
    color "#000000"
