 


screen error_notification(message):
    frame:
        style "popup"
        text message  style "Pm_notifi"
        timer 3.0 action Hide("error_notification") 
 


style popup is frame:
    xsize 1400
    ysize 100
    textalign 0.5
    background "#00e18f"
    xpos 0.5  # Center horizontally
    ypos 0.5
    xanchor 0.5  # Anchor to center
   

style Pm_notifi:
    ypos 0.3
    ypadding 0.5