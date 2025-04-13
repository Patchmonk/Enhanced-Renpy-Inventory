# #################################################################################################################
# #██████╗ ███████╗██████╗ ██████╗ ██╗   ██╗     ██████╗        ██████╗ ███████╗███╗   ██╗██████╗ ███████╗██████╗ #
# #██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝    ██╔════╝        ██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗#
# #██████╔╝█████╗  ██████╔╝██████╔╝ ╚████╔╝     ██║  ███╗       ██████╔╝█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝#
# #██╔══██╗██╔══╝  ██╔══██╗██╔══██╗  ╚██╔╝      ██║   ██║       ██╔══██╗██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗#
# #██████╔╝███████╗██║  ██║██║  ██║   ██║       ╚██████╔╝██╗    ██████╔╝███████╗██║ ╚████║██████╔╝███████╗██║  ██║#
# #╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═════╝ ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝#
# #################################################################################################################
###############################################################################################################################
## splashscreen.rpy ###########################################################################################################
##
## Credits to those whom invented all of this, I could not get even near to creating and designing this stuff myself!
## I did create the art in the art folder but used the keygen music from CORE for the sound. Other used resources I found on the
## internet without being able to cling someone's name on to it.
## ############################################################################################################################
## While it makes little sense to put in a background with effects, a splash screen, a logo, music and 
## a video as well as a skipbutton, you should see this as an attempt to provide you with as many 
## options as possible so you wouldn't have to cruise the net for every single feature like I had to.
## Regardless of whether you want a splashscreen, logo or video, in this file you will find the code to get it done.
## Just uncomment the appropriate one. Mind me you won't have like hours to display stuff
###############################################################################################################################

image imgDisheaveled_decor = load_image("art/imgdisheaveled_decor.png")
image imgSplash = load_image("art/imgsplash.png")
# this video serves as background and by declaring it like this renpy treats it as an image, exactly what we want
image webmDecor = Movie(channel="movie_dp", play="art/webmdecor.webm") 

label splashscreen:

    ## art/webmdecor.webm ###################################################################################################
    ## simply replace the file webmdecor.webm in the art folder to get your own background. Take note of the
    ## dimensions preferrably 1920 x 1080 pixels. 
    ###########################################################################################################################
    scene webmDecor: #  This line sets the background scene to an image or webm video named "webmdecor".
        size (1920, 1080) crop (480, 270, 960, 540)  # This specifies the size of the scene and crops it to a specific area.
        linear 8.0 crop (0, 0, 1920, 1080)  # This applies a linear transition over 8 seconds, cropping the scene to full size.
    with dissolve
   

   


    ## skip_screen.rpy #########################################################################################################
    ## here we use a screen to add a skipbutton to skip the entire splash ceremony. 
    ## add "screen scrSkip()" to screens.rpy to make it "known" to RenPy. This whole thing is actually useless you won't see that
    ## much of a splash ceremony whether you skip it or not. However it could always come in handy later on, that is why
    ## I included it. Also take notice of the modification of main_menu.rpy to add another button to be able to display
    ## an informational video about yoiur game or something.
    ###########################################################################################################################
    show screen scrSkip
    'Skip if you voted against extensive splashscreens!{w=200}{nw}' # set width and no wrapping  
    hide screen scrSkip

    

    ## most likely you won't see or hear any media after this line, but it gives you the option to choose whichever you would
    ## want to see or hear
    $ renpy.pause(3.5)

    ## audio/danse.mp3 ########################################################################################################
    ## If you want to have your own intro music, replace the file danse.mp3 in audio folder
    ###########################################################################################################################
    # play music "audio/danse.mp3" fadein 2.0

    ## art/imgsplash.png ##########################################################################################################
    ## The imgsplash.png image is the splash that is shown here, located in the art folder. You might not see it at all. So you
    ## will have to make up your mind about either splash screen, video or background etc.
    ###########################################################################################################################
    #show imgSplash:
    #    rotate 360 zoom 2 alpha 0
    #    ease 1 alpha 1
    #    pause 2.0
    #    ease .5 rotate 0 zoom 1
    #hide splash_image   

    
    
    

    return
    