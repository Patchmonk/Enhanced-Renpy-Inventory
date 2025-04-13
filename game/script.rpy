# #################################################################################
# #██████╗  █████╗ ████████╗ ██████╗██╗  ██╗███╗   ███╗ ██████╗ ███╗   ██╗██╗  ██╗#
# #██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║  ██║████╗ ████║██╔═══██╗████╗  ██║██║ ██╔╝#
# #██████╔╝███████║   ██║   ██║     ███████║██╔████╔██║██║   ██║██╔██╗ ██║█████╔╝ #
# #██╔═══╝ ██╔══██║   ██║   ██║     ██╔══██║██║╚██╔╝██║██║   ██║██║╚██╗██║██╔═██╗ #
# #██║     ██║  ██║   ██║   ╚██████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║  ██╗#
# #╚═╝     ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝#
# #################################################################################
# #################################################################################################################
# #██████╗ ███████╗██████╗ ██████╗ ██╗   ██╗     ██████╗        ██████╗ ███████╗███╗   ██╗██████╗ ███████╗██████╗ #
# #██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝    ██╔════╝        ██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗#
# #██████╔╝█████╗  ██████╔╝██████╔╝ ╚████╔╝     ██║  ███╗       ██████╔╝█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝#
# #██╔══██╗██╔══╝  ██╔══██╗██╔══██╗  ╚██╔╝      ██║   ██║       ██╔══██╗██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗#
# #██████╔╝███████╗██║  ██║██║  ██║   ██║       ╚██████╔╝██╗    ██████╔╝███████╗██║ ╚████║██████╔╝███████╗██║  ██║#
# #╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═════╝ ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝#
# #################################################################################################################


# ##############################################################################
# # ███████╗██╗   ██╗███╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗ #
# # ██╔════╝██║   ██║████╗  ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝ #
# # █████╗  ██║   ██║██╔██╗ ██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗ #
# # ██╔══╝  ██║   ██║██║╚██╗██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║ #
# # ██║     ╚██████╔╝██║ ╚████║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║ #
# # ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ #
# ##############################################################################
# This function is a handy tool for Ren'Py developers, allowing them to quickly gather and review all labels used in their scripts. 
# By writing these labels to a separate text file, developers can maintain better organization and streamline their workflow. 
# If you're working on a Ren'Py project, consider integrating this function to enhance your script management!
## import library for file handling
init python:
    from os.path import exists
    import os  # Importing os to handle directory operations

    def write_labels():
        # Open the _labels.txt file in write mode
        f1 = open(config.gamedir + "/_labels.txt", "w")
        
        # Iterate through all files in the game directory
        for file_name in filter(lambda x: x.endswith('.rpy'), os.listdir(config.gamedir)):
            f1.write("\n\n" + file_name + "\n\n")  # Write the file name as a header in the output file
            
            # Open each .rpy file for reading
            f2 = open(config.gamedir + "/" + file_name, "r")
            for i in f2:
                if "label " in i:  # Check if the line contains a label
                    f1.write(i)  # Write the label line to the output file
            f2.close()  # Close the .rpy file after reading
        f1.close()  # Close the _labels.txt file after writing

# The provided code is a powerful tool for Ren'Py developers looking to streamline their projects by identifying unused image assets. 
# By utilizing threading, file handling, and directory management, it efficiently checks for image usage and outputs the results to a text file. 
# This not only helps in maintaining a clean project structure but also enhances performance by reducing unnecessary asset loading. 
# If you're working on a Ren'Py project, consider implementing this code to keep your assets organized and your game running smoothly!



    def img_unused_threaded():
        import threading
        thread = threading.Thread(target=img_unused)
        thread.start()

    def img_unused():
        if renpy.windows != False:
            wfolder = config.gamedir + "/"
        rfolder = config.gamedir + "/"
        f1 = open(config.gamedir+"/_img_unused.txt","w")
        for j in [""]+[name for name in os.listdir(rfolder+"images") if os.path.isdir(os.path.join(rfolder+"images", name))]:
            f1.write("+-+-+-+-+-+-+ images/"+j+" +-+-+-+-+-+-+\n\n")
            for file_name in os.listdir(rfolder+"images/"+j):
                non = 0
                file_name3 = file_name.rsplit(".",1)[0]
                for file_name2 in filter(lambda x: x.endswith('.rpy'), os.listdir(config.gamedir)):
                    f2 = open(rfolder+file_name2,"r")
                    for i in f2:
                        if file_name3 in i:
                            non = 1
                    f2.close()
                if non == 0:
                    f1.write(file_name+"\n")
            f1.write("\n\n\n")
        f1.close()



## define function to check for filepaths
    def file_exists(filepath):
        return os.path.isfile(filepath)

## define function to load images
    def load_image(image_path):
        import os
        if file_exists(image_path):
            return image_path  # Return the path if the file exists
        else:
            # Handle the error, e.g., log a message or use a default image
            renpy.log("File not found: " + image_path)
            return "images/default_image.png"  # Fallback image 

# ###################################################
# # ██╗███╗   ███╗ █████╗  ██████╗ ███████╗███████╗ #
# # ██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝██╔════╝ #
# # ██║██╔████╔██║███████║██║  ███╗█████╗  ███████╗ #
# # ██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝  ╚════██║ #
# # ██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗███████║ #
# # ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝ #
# ################################################### 
## Just an annoying little arrow that urges you on to advance to the next screen, found on the internet
image ctc_animation = Animation("gui/ctc/ctc11.png", 0.4, "gui/ctc/ctc10.png", 0.08, "gui/ctc/ctc9.png", 0.08, "gui/ctc/ctc8.png", 0.08, "gui/ctc/ctc7.png", 0.08, "gui/ctc/ctc6.png", 0.08, "gui/ctc/ctc5.png", 0.08, "gui/ctc/ctc4.png", 0.08, "gui/ctc/ctc3.png", 0.08, "gui/ctc/ctc2.png", 0.08, "gui/ctc/ctc.png", 0.4, "gui/ctc/ctc2.png", 0.08, "gui/ctc/ctc3.png", 0.08, "gui/ctc/ctc4.png", 0.08, "gui/ctc/ctc5.png", 0.08, "gui/ctc/ctc6.png", 0.08, "gui/ctc/ctc7.png", 0.08, "gui/ctc/ctc8.png", 0.08, "gui/ctc/ctc9.png", 0.08, "gui/ctc/ctc10.png", 0.08, xpos=0.52, ypos=0.985, xanchor=1.0, yanchor=1.0)
## imagery used in this project
image Inventoryicons = "inventoryicons.png"    # notice capitalization of the image reference, it won't find Inventoryicons.png
image A_install = "screenshots/a_install.png"
image B_initialize_variable = "screenshots/b_initialize_variable.png"
image C_add = "screenshots/c_add.png"
image D_remove = "screenshots/d_remove.png"
image E_unlock = "screenshots/e_unlock.png"
image F_lock = "screenshots/f_lock.png"
image G_inc = "screenshots/g_inc.png"
image bgb = "art/bg_b.png"
## this video serves as background and by declaring it like this renpy treats it as an image, exactly what we want
image grassland_decor_full = Movie(channel="movie_dp", play="art/grassland_full.webm")

## Declare characters used by this game. The color argument colorizes the name of the character.
init:
    $ p = Character('Patchmonk', color=("#00448f"))
    $ b = Character('Berry G. Bender',image="art/bgb.png",color=("#fc8a08"))

## Initialize variable gold and multi_task_level reader both integer type (I think)
default gold = 300
default multi_task_level_reader = 0
# ##################################################################################################
# # ██╗███╗   ██╗██╗████████╗██╗ █████╗ ██╗     ██╗███████╗███████╗    ██████╗  █████╗ ██╗███████╗ #
# # ██║████╗  ██║██║╚══██╔══╝██║██╔══██╗██║     ██║╚══███╔╝██╔════╝    ██╔══██╗██╔══██╗██║██╔════╝ #
# # ██║██╔██╗ ██║██║   ██║   ██║███████║██║     ██║  ███╔╝ █████╗      ██████╔╝███████║██║███████╗ #
# # ██║██║╚██╗██║██║   ██║   ██║██╔══██║██║     ██║ ███╔╝  ██╔══╝      ██╔═══╝ ██╔══██║██║╚════██║ #
# # ██║██║ ╚████║██║   ██║   ██║██║  ██║███████╗██║███████╗███████╗    ██║     ██║  ██║██║███████║ #
# # ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝ #
# ##################################################################################################
## PAIS initialization we start with 30 item slots of which 10 are unlocked. Each slot can hold 99 copies
default inventory = Inventory(slot_count=30, unlocked_slots=10)




## The start of the game
label start:

    # ############################################
    # # ███╗   ███╗ ██████╗ ██╗   ██╗██╗███████╗ #
    # # ████╗ ████║██╔═══██╗██║   ██║██║██╔════╝ #
    # # ██╔████╔██║██║   ██║██║   ██║██║█████╗   #
    # # ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██║██╔══╝   #
    # # ██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ██║███████╗ #
    # # ╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚═╝╚══════╝ #
    # ############################################  
    ## art/pais_intro.webm #################################################################################################
    ## display a .webm video, replace pais_intro.webm in the art folder
    ## #####################################################################################################################
    $ renpy.movie_cutscene("art/pais_intro.webm") # short and sweet will always show

    ## Black out the scene with transition
    scene black with dissolve
    

    # ################################################
    # # ██╗     ██╗██╗   ██╗███████╗██████╗ ██████╗  #
    # # ██║     ██║██║   ██║██╔════╝╚════██╗██╔══██╗ #
    # # ██║     ██║██║   ██║█████╗   █████╔╝██║  ██║ #
    # # ██║     ██║╚██╗ ██╔╝██╔══╝  ██╔═══╝ ██║  ██║ #
    # # ███████╗██║ ╚████╔╝ ███████╗███████╗██████╔╝ #
    # # ╚══════╝╚═╝  ╚═══╝  ╚══════╝╚══════╝╚═════╝  #
    # ################################################
    ## experimental: display live2d character with motions. we use a wrapper\workaround in case the user's hardware does not
    ## support live2d. look inside live2dmod.rpy for details. live2d is so easy to use ?
    ########################################################################################################################################################
    ## Show live2d character Rice with motions
    ## live2d/Rice
    ########################################################################################################################################################
    label displayRice:
        show rice mtn_01 mtn_02 mtn_03 idle
    
    ## audio/danse.mp3 ########################################################################################################
    ## If you want to have your own intro music, replace the file danse.mp3 in audio folder
    ###########################################################################################################################
    play music "audio/danse.mp3" fadein 2.0
    $ renpy.pause()
    ## here we use the buzz class to move the displayed text, delete buzz.rpy and every reference to text_effect to eliminate this.
    ## //  start delete nice-but-useless --> ###############################################################################################################
    show text '“Welcome to {color=#00448f}PAIS 1.2.7{/color} by {color=#00448f}Patchmonk {/color}& {color=#fc8a08}Berry G. Bender{/color}."' at text_effect
    $ renpy.pause()
    show text '"PAIS is designed by Patchmonk."' at text_effect
    $ renpy.pause()
    show text '"I merely played with and modified some graphics and sounds, all while learning the ropes."' at text_effect
    $ renpy.pause()
    show text '"Any video shown here was created by me, using Canva, but based on Patchmonk his imagery."' at text_effect
    $ renpy.pause()
    show text '"Music comes from CORE WinIso keygenerator and some French singer."' at text_effect
    $ renpy.pause()
    show text '"Exotic fonts, sounds and this effect come from the internet."' at text_effect
    $ renpy.pause()
    show text '"Delete all text between {color=#fc8a08}## // start delete -->{/color}and{color=#fc8a08}## \\ <-- end delete{/color} to eliminate all of that."' at text_effect
    $ renpy.pause()
    show text '"I merely demonstrate PAIS customization by contributing the nice-but-useless stuff."' at text_effect
    $ renpy.pause()
    show text '"Anything created for this project serves only to provide the code to incorporate webm videos, effects and sounds."' at text_effect
    show text '"The graphics only serve to give you an idea of how to incorporate nearly any effect you could think off. I am not an artist nor coder."' at text_effect
    $ renpy.pause()
    show text '"In my humble opinion, you would be best off, using webm files for moving backgrounds, effects, splashscreens and sounds."' at text_effect
    $ renpy.pause()
    show text '"And I can only recommend Canva for graphics, videos, sounds, images, it covers all."' at text_effect
    $ renpy.pause()
    scene black with dissolve

    # ################################################
    # # ██╗     ██╗██╗   ██╗███████╗██████╗ ██████╗  #
    # # ██║     ██║██║   ██║██╔════╝╚════██╗██╔══██╗ #
    # # ██║     ██║██║   ██║█████╗   █████╔╝██║  ██║ #
    # # ██║     ██║╚██╗ ██╔╝██╔══╝  ██╔═══╝ ██║  ██║ #
    # # ███████╗██║ ╚████╔╝ ███████╗███████╗██████╔╝ #
    # # ╚══════╝╚═╝  ╚═══╝  ╚══════╝╚══════╝╚═════╝  #
    # ################################################
    ########################################################################################################################################################################
    ## Show live2d character with motions
    ## live2d/Hiyori
    ########################################################################################################################################################################
    label displayHiyori:
        show hiyori hiyori_m01 hiyori_m02 hiyori_m03 hiyori_m04 hiyori_m05 hiyori_m06 hiyori_m07
    $ renpy.pause()
    ########################################################################################################################################################################
    # ############################################
    # # ███╗   ███╗ ██████╗ ██╗   ██╗██╗███████╗ #
    # # ████╗ ████║██╔═══██╗██║   ██║██║██╔════╝ #
    # # ██╔████╔██║██║   ██║██║   ██║██║█████╗   #
    # # ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██║██╔══╝   #
    # # ██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ██║███████╗ #
    # # ╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚═╝╚══════╝ #
    # ############################################
    ## Show our moving decor a webm video
    ## art/grassland_full.webm
    ########################################################################################################################################################################
    scene grassland_decor_full with dissolve
    ## \\ <-- end delete nice-but-useless ################################################################################ 


#########################################################################################
#                                                                                       #
#     ██╗  ██╗ ██████╗ ██╗    ██╗    ████████╗ ██████╗     ██╗   ██╗███████╗███████╗    #
#     ██║  ██║██╔═══██╗██║    ██║    ╚══██╔══╝██╔═══██╗    ██║   ██║██╔════╝██╔════╝    #
#     ███████║██║   ██║██║ █╗ ██║       ██║   ██║   ██║    ██║   ██║███████╗█████╗      #
#     ██╔══██║██║   ██║██║███╗██║       ██║   ██║   ██║    ██║   ██║╚════██║██╔══╝      #
#     ██║  ██║╚██████╔╝╚███╔███╔╝       ██║   ╚██████╔╝    ╚██████╔╝███████║███████╗    #
#     ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝        ╚═╝    ╚═════╝      ╚═════╝ ╚══════╝╚══════╝    #
#                                                                                       #
#########################################################################################
        
    p "Hello my friend, welcome to {color=#00448f}Patchmonk's Advanced Inventory System 1.2.7{/color}. I'm not sure how you ended up here, but you're in for a treat. If you haven't heard of it, this is the improved version of the simple inventory system."
    p "The system relies on two components: a custom notification system and the main inventory system, both nestled in the component folder."
    p "So, why is the notification system tangled up with the inventory? Well, I got a bit carried away with my love for fancy sounds and flashy error and success messages. But hey, you can always untangle this mess by editing the code."
    p "Don't worry it's super easy you can just return nothing in the function where I call the notification in the main inventory functions. "
    p "Now that you're all caught up on the main components and dependencies, it's time to dive into setting this up for your own project. Buckle up, because it's going to be a wild ride!"
    p "Just kidding, it's going to be smooth as butter! I made sure it's super easy so anyone can follow along. I mean, as long as you understand basic Ren'py functionality and a little bit of Python syntax."
# #########################################################################################
# # ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗         ██████╗  █████╗ ██╗███████╗ #
# # ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║         ██╔══██╗██╔══██╗██║██╔════╝ #
# # ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║         ██████╔╝███████║██║███████╗ #
# # ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║         ██╔═══╝ ██╔══██║██║╚════██║ #
# # ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗    ██║     ██║  ██║██║███████║ #
# # ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝ #
# #########################################################################################
    show A_install
    p "Alright, let's get back to business. How do we set up this inventory system in your project? It's as easy as pie, just like its predecessor. Just copy the component folder in your game directory."
    p "The next step is super simple you have to initialize the variable."
    hide A_install
# ##################################################################################################
# # ██╗███╗   ██╗██╗████████╗██╗ █████╗ ██╗     ██╗███████╗███████╗    ██████╗  █████╗ ██╗███████╗ #
# # ██║████╗  ██║██║╚══██╔══╝██║██╔══██╗██║     ██║╚══███╔╝██╔════╝    ██╔══██╗██╔══██╗██║██╔════╝ #
# # ██║██╔██╗ ██║██║   ██║   ██║███████║██║     ██║  ███╔╝ █████╗      ██████╔╝███████║██║███████╗ #
# # ██║██║╚██╗██║██║   ██║   ██║██╔══██║██║     ██║ ███╔╝  ██╔══╝      ██╔═══╝ ██╔══██║██║╚════██║ #
# # ██║██║ ╚████║██║   ██║   ██║██║  ██║███████╗██║███████╗███████╗    ██║     ██║  ██║██║███████║ #
# # ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝ #
# ##################################################################################################
    show  B_initialize_variable
    p "To initialize the variable, you need to create it first and define its parameter before the game starts. It's like setting up your chess pieces before the match begins!"
    p "In the screenshot, there are two parameters. The first parameter specifies that the inventory will start with 30 slots. The second parameter designates 10 slots as unlocked from the initial 30 slots, while the remaining 20 slots will be locked."
    p "While the rest are locked tighter than treasure chests. You can tweak this setup to match your game style. Don't worry I will show that until later in the tutorial."
    hide B_initialize_variable

    p "Alright, now that you've mastered the inventory setup, let's jump into the fun part the awesome features of this inventory  system!"
    p "Just like its predecessor, we'll be rocking the heads-up display with a stylish backpack icon probably the same one, but who knows?"

    ## //  start delete --> #############################################################################
    b "Psssst!!?"
    p "What??"
    b "Could I....."
    p "No you actually can't! You are disturbing me and distracting everyone!"
    b "I'm well aware of that"
    p "Then why are you doing it??"
    b "This way we'll be teaching them to multi task as well..."
    ## increase the value of multi task level reader to reward the reader for coping with multi tasking
    $ multi_task_level_reader =500
    p "Pff...let's see where were we....oh yes designing icons."
    ## \\ <-- end delete ################################################################################

    p "Designing icons isn't isn't exactly my superpower, but I had to whip up a bunch for this project because the original icon pack author vaporized into thin air along with his repository and license. So, I crafted an icon pack from scratch."

    ## //  start delete --> #############################################################################
    b "You could have asked me"
    p "I'll give you exactly 5 lines of dialogue and that's it starting now!"
    ## Just a short appearance and preamble
    $ show_notification("Be advised: A possible problem arises from the North-West", sound_type="demon_rises")
    show bgb with moveinright
    b "Sorry to disturb! Only wanted to say you made an excellent choice, if you want an inventory-system which works and is super simple to customize."
    b "See how easy I customized it fairly from scratch without any python background."
    b "All credits go to Patchmonk, the true brains behind this system. I merely added some nice-but-useless-if-not-annoying effects."
    b "I'm also responsible for the splash-skip-nice-but-useless stuff as well."
    b "Whether you want a splashscreen, skipbutton, intro music or movie to appear, we covered any option we could think of and hopefully it's usefull. I'll return the mic to the author of PAIS 1.2.7."
    ## Quickly dissappear into the blue or green
    hide bgb with moveinright

    p "Is he gone??"
    ## \\ <-- end delete ################################################################################


    p "Now I will activate the HUD screen to display the inventory image button, similar to the previous inventory. However, please be advised that we must close the inventory each time by clicking the cross button; otherwise, we will not be able to continue the tutorial."
# ###############################################################################################
# #  █████╗  ██████╗████████╗██╗██╗   ██╗ █████╗ ████████╗███████╗    ██╗  ██╗██╗   ██╗██████╗  #
# # ██╔══██╗██╔════╝╚══██╔══╝██║██║   ██║██╔══██╗╚══██╔══╝██╔════╝    ██║  ██║██║   ██║██╔══██╗ #
# # ███████║██║        ██║   ██║██║   ██║███████║   ██║   █████╗      ███████║██║   ██║██║  ██║ #
# # ██╔══██║██║        ██║   ██║╚██╗ ██╔╝██╔══██║   ██║   ██╔══╝      ██╔══██║██║   ██║██║  ██║ #
# # ██║  ██║╚██████╗   ██║   ██║ ╚████╔╝ ██║  ██║   ██║   ███████╗    ██║  ██║╚██████╔╝██████╔╝ #
# # ╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═══╝  ╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  #
# ###############################################################################################
    ## Fire up the screen HUD of PAIS by Patchmonk
    show screen scrHud
    ## Expose PAIS inventory screen by Patchmonk
    show screen scrInventory

    ## //  start delete --> #############################################################################
    show text '"Jesus Christ what did he do to my inventory system??"' at text_effect
    ## \\ <-- end delete ################################################################################

    p "Anyway you can open the backpack by clicking the backpack icon to open the inventory system. And don't forget to close it with the cross button in the top right corner, the game will wait for that to happen."
    p "As you can see, this inventory is currently empty. You may be curious as to why many of the inventory slots display a locked icon. The reason is that they are indeed locked. This is one of the features of my inventory system. Quite creative, isn't it? Or perhaps not."
    p "You've probably seen it before in RPG games where locked inventory slots make you grind like a maniac. A handy feature, right? It spices up the game! Why not add the same feature to our game? We can always reward players by unlocking new slots."
    p "But hey, it's your call! This is just one of the default features I whipped up. No pressure to use it if you don't want to. We'll save the lock talk for later. First, let's dive into adding the items."
    p "An empty inventory is as exciting as watching paint dry. Let's spice things up by adding some items and watch this baby come to life! But first, we need to learn how to add those items."
    ## //  start delete --> #############################################################################
    show text "I can see the useless part of his admission but where is the nice part..." at text_effect
    ## \\ <-- end delete ################################################################################
    show Inventoryicons
    p "Adding items is a piece of cake! Just head over to the {color=#fc8a08}game/components/inventory_system/images/icons{/color} folder and start dropping in your images. Just like those dummy item icons. Easy peasy!"
    p "You can edit replace do whatever you want don't forget to remember the dimensions of the images and the name is super important as well."
    hide Inventoryicons
   
    p "After replacing the default icons with your own item icons, we need to inform the inventory that it's now an item."

    show C_add
    p "Since we already have all the images in the icon folder, let's call the {color=#fc8a08}add_item{/color}function from the inventory system like this screenshot."
    p "Mind me we will be storing 10 items and we start with 1 copy of each item."
    hide C_add
# #######################################################################
# #  █████╗ ██████╗ ██████╗     ██╗████████╗███████╗███╗   ███╗███████╗ #
# # ██╔══██╗██╔══██╗██╔══██╗    ██║╚══██╔══╝██╔════╝████╗ ████║██╔════╝ #
# # ███████║██║  ██║██║  ██║    ██║   ██║   █████╗  ██╔████╔██║███████╗ #
# # ██╔══██║██║  ██║██║  ██║    ██║   ██║   ██╔══╝  ██║╚██╔╝██║╚════██║ #
# # ██║  ██║██████╔╝██████╔╝    ██║   ██║   ███████╗██║ ╚═╝ ██║███████║ #
# # ╚═╝  ╚═╝╚═════╝ ╚═════╝     ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝ #
# #######################################################################
    ## Add 10 items to PAIS, quantity refers to the number of copies we store, we start with 1
    ## it will look and find every item.png and every item's _hover.png equivalent in the components/inventory_system/images/icons folder
    $ inventory.add_item("apple", quantity=1)
    $ inventory.add_item("banana", quantity=1)
    $ inventory.add_item("these", quantity=1)
    $ inventory.add_item("are", quantity=1)
    $ inventory.add_item("all", quantity=1)
    $ inventory.add_item("beautiful", quantity=1)
    $ inventory.add_item("and", quantity=1)
    $ inventory.add_item("cute", quantity=1)
    $ inventory.add_item("little", quantity=1)
    $ inventory.add_item("cats", quantity=1)

    p "We've added 10 items to the inventory. Let's take a look!"
    ## Expose PAIS inventory screen by Patchmonk
    show screen scrInventory

    p "Yay, now we are overflowing with items! Our inventory is almost full, and it always gives me a sense of over-accomplishment when something is nearly maxed out. You know that feeling, right?"
    ## //  start delete --> #############################################################################
    show text "Ah well, the moving background is kinda cool, at least he showed some great cat art..." at text_effect
    ## \\ <-- end delete ################################################################################
    p "Some of you might be thinking, 'Yeah, yeah, we've seen it before. You added some items to the inventory. What's the difference?'"
    p "My dear friend, unlike the previous inventory which only had basic features, this one has some advanced stuff. Yep, you guessed it right it's stackable items!"
    p "Alright, let's add nine more copies to each item slot to test this feature. We'll also increase our gold to 600 and the multi task level to 800"
    p "Mind me we will only increase the number of copies, by adding 9 apples, 9 banana's, 9 cats and so on."
# #######################################################################
# #  █████╗ ██████╗ ██████╗     ██╗████████╗███████╗███╗   ███╗███████╗ #
# # ██╔══██╗██╔══██╗██╔══██╗    ██║╚══██╔══╝██╔════╝████╗ ████║██╔════╝ #
# # ███████║██║  ██║██║  ██║    ██║   ██║   █████╗  ██╔████╔██║███████╗ #
# # ██╔══██║██║  ██║██║  ██║    ██║   ██║   ██╔══╝  ██║╚██╔╝██║╚════██║ #
# # ██║  ██║██████╔╝██████╔╝    ██║   ██║   ███████╗██║ ╚═╝ ██║███████║ #
# # ╚═╝  ╚═╝╚═════╝ ╚═════╝     ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝ #
# #######################################################################
    ## Adding 9 More copies of each item to PAIS
    $ inventory.add_item("apple", quantity=9)
    $ inventory.add_item("banana", quantity=9)
    $ inventory.add_item("these", quantity=9)
    $ inventory.add_item("are", quantity=9)
    $ inventory.add_item("all", quantity=9)
    $ inventory.add_item("beautiful", quantity=9)
    $ inventory.add_item("and", quantity=9)
    $ inventory.add_item("cute", quantity=9)
    $ inventory.add_item("little", quantity=9)
    $ inventory.add_item("cats", quantity=9)

    ## Increase gold to 600
    $ gold = 600
    ## increase the value of multi task level reader
    $ multi_task_level_reader = 800
    ## Expose PAIS inventory screen by Patchmonk
    show screen scrInventory

    p "All the item counts have increased isn't it awesome? Now you got 10 apples, 10 banana's, etc etc.  With stackable items, players can hoard all the items they want."
    p "Currently you can stack copies of items up to 99 per slot. You can always customize the item limit per slot. The system will automatically take care of redistributing items to existing slots if the items already exist in the inventory."
    p "If the items exceed the defined slot limit, they'll be stored in the next available unlocked slot. Pretty cool, right?"
    p "If you're wondering what happens if we don't have any slots left and we try to add more items, let me tell you."
    show text "Ah well, at least he was passionate about it..." at text_effect
    p "My friend, I thought about that too! That's why I added a custom notification function to handle such situations. It'll give you an error with a fancy sound and a pop-up message."
    p "The fun part about this notification system is that you can customize it to your heart's content. You can use it for other game stuff, customize the style, and the sound too."
    p "When a player unlocks something, you can use the notification function to notify them with an accomplishment sound or something."
    p "Alright, let's flood our inventory with 99 apples and 99 banana's to check what our inventory is capable of and enjoy these fancy pop-ups and notifications like those fancy games."
    p "Now, if you hit the keyboard or click your mouse, a fancy popup notification will appear on your screen. Gaze at it for 3 seconds before proceeding to the next dialogue."
# #######################################################################
# #  █████╗ ██████╗ ██████╗     ██╗████████╗███████╗███╗   ███╗███████╗ #
# # ██╔══██╗██╔══██╗██╔══██╗    ██║╚══██╔══╝██╔════╝████╗ ████║██╔════╝ #
# # ███████║██║  ██║██║  ██║    ██║   ██║   █████╗  ██╔████╔██║███████╗ #
# # ██╔══██║██║  ██║██║  ██║    ██║   ██║   ██╔══╝  ██║╚██╔╝██║╚════██║ #
# # ██║  ██║██████╔╝██████╔╝    ██║   ██║   ███████╗██║ ╚═╝ ██║███████║ #
# # ╚═╝  ╚═╝╚═════╝ ╚═════╝     ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝ #
# #######################################################################
    ## Flooding PAIS with 99 apples and 99 banana's.
    $ inventory.add_item("apple", quantity=99)
    $ inventory.add_item("banana", quantity=99)

    p "Ha ha! You saw it, right? Cool, isn't it? I told you at the very beginning that I get carried away with this thing. It's super simple but fancy!"
    p "Alright let's check our inventory if that error is correct or not? Mind me we had 10 apples and 10 banana's before we tried to add 99 of each. It should occupy all the available unlock slots."

    ## Expose PAIS inventory screen by Patchmonk
    show screen scrInventory

    p "Awesome, you should start eating apples and banana's, because you can't carry anymore of these. We can't add any more items except for the existing slots up to the slot limit. If you're wondering about the other locked icon slot, we'll come back to this later in the tutorial. Let's complete the basic features first."
    p "The simple notification component is modular. I made sure it's modular so you can use it for other game notifications to inform your players about gameplay things."
    show text "He passionately messed up my system and my code..." at text_effect
    p "If you don't want such features, I totally get it. It might not be suitable for your game. In that case, you can return nothing. You'll find a section in my code where I'm calling the{color=#fc8a08} show_notification{/color}function you can edit that. It's super simple!"
    p "Alright, now you know how to add items, overflow the inventory, handle errors, and show notifications. We've come so far. So, what's next? Removing items, of course!"
    p "How can we remove items from the inventory? If you're wondering how to use the function and how it works, don't worry, we will explore everything."
    p "If you're guessing to remove items you have to call the {color=#fc8a08} remove_item{/color}function you're absolutely correct."

    show D_remove
    p "This is how you can call the remove item function, In the second parameter you can tell the inventory How many you want to remove. Super simple isn't it?"
# ####################################################################################################
# # ██████╗ ███████╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗    ██╗████████╗███████╗███╗   ███╗███████╗ #
# # ██╔══██╗██╔════╝████╗ ████║██╔═══██╗██║   ██║██╔════╝    ██║╚══██╔══╝██╔════╝████╗ ████║██╔════╝ #
# # ██████╔╝█████╗  ██╔████╔██║██║   ██║██║   ██║█████╗      ██║   ██║   █████╗  ██╔████╔██║███████╗ #
# # ██╔══██╗██╔══╝  ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██╔══╝      ██║   ██║   ██╔══╝  ██║╚██╔╝██║╚════██║ #
# # ██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ███████╗    ██║   ██║   ███████╗██║ ╚═╝ ██║███████║ #
# # ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝    ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝ #
# ####################################################################################################
    ## Remove 99 apples from PAIS
    $ inventory.remove_item("apple", quantity=99)
    hide D_remove

    p "Our trusty notification system strikes again! It flashed a message telling you it removed 99 apples and played that oh-so-familiar removal sound, the one that only chimes when items vanish into thin air. As always, feel free to tweak those notifications to match your game's whims whenever you like."
    p "The fun part about the removing function is that it calls the sort function, which shuffles the inventory like a deck of cards."
    p "So, you don't have to stress about plucking an item from the middle of the inventory crate. Every time you remove something, it will reshuffle itself!"
    p "I suppose I should also mention that the inventory will play different notifications with sounds based on various scenarios. You can customize all of this to suit your needs."
    p "Our Inventory is smart enough to alert you if something goes wrong. For example, we currently have no apples in our inventory. If you accidentally try to remove 99 apples anyway, which you don't have, what's going to happen? Let's find out!"
# ####################################################################################################
# # ██████╗ ███████╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗    ██╗████████╗███████╗███╗   ███╗███████╗ #
# # ██╔══██╗██╔════╝████╗ ████║██╔═══██╗██║   ██║██╔════╝    ██║╚══██╔══╝██╔════╝████╗ ████║██╔════╝ #
# # ██████╔╝█████╗  ██╔████╔██║██║   ██║██║   ██║█████╗      ██║   ██║   █████╗  ██╔████╔██║███████╗ #
# # ██╔══██╗██╔══╝  ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██╔══╝      ██║   ██║   ██╔══╝  ██║╚██╔╝██║╚════██║ #
# # ██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ███████╗    ██║   ██║   ███████╗██║ ╚═╝ ██║███████║ #
# # ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝    ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝ #
# ####################################################################################################
    ## Remove another 99 apples from PAIS to invoke error handling since we have no apples in our inventory currently
    $ inventory.remove_item("apple", quantity=99)

    ## Expose PAIS inventory screen by Patchmonk
    show screen scrInventory

    p "As you can see, it successfully removed all the items we had, but couldn't remove what we didn't have. That's why we got an error. It gives you a heads-up with a popup message and plays the error sound."
    p "Now you can add items, remove items, and create your own items. We have all the basic inventory features. I guess we have a complete inventory system now."
    p "Hmmm... why do I have this nagging feeling, like last time, that I'm forgetting something?"
    p "Hold on a sec... I've just remembered that I promised we'd discuss the locking stuff. Yeah, now I recall you can lock the slots like in those big title games. I was totally inspired by those games inventory!"
    p "Alright let's show you how you can unlock all those slot in the inventory first. This time also the same like before we have to call our unlock slot function"
    show E_unlock
    p "First, let us demonstrate how to unlock all the slots in the inventory. Like before, we need to call the {color=#fc8a08}unlock_slots(20){/color} function."
    hide E_unlock
# ######################################################################################################
# # ██╗   ██╗███╗   ██╗██╗      ██████╗  ██████╗██╗  ██╗    ███████╗██╗      ██████╗ ████████╗███████╗ #
# # ██║   ██║████╗  ██║██║     ██╔═══██╗██╔════╝██║ ██╔╝    ██╔════╝██║     ██╔═══██╗╚══██╔══╝██╔════╝ #
# # ██║   ██║██╔██╗ ██║██║     ██║   ██║██║     █████╔╝     ███████╗██║     ██║   ██║   ██║   ███████╗ #
# # ██║   ██║██║╚██╗██║██║     ██║   ██║██║     ██╔═██╗     ╚════██║██║     ██║   ██║   ██║   ╚════██║ #
# # ╚██████╔╝██║ ╚████║███████╗╚██████╔╝╚██████╗██║  ██╗    ███████║███████╗╚██████╔╝   ██║   ███████║ #
# #  ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚══════╝╚══════╝ ╚═════╝    ╚═╝   ╚══════╝ #
# ######################################################################################################
    ## Unlock 20 slots from PAIS
    $ inventory.unlock_slots(20)

    ## Expose PAIS inventory screen by Patchmonk
    show screen scrInventory

    p "All our 30 inventory slots are unlocked. That's pretty awesome, right?"
    p "By now, you probably know I have a knack for getting carried away. I even created a lock function that can lock all the slots or just a specific number of slots."
    p "Honestly, I have no idea what was going through my mind at the time. But imagine if there's a scenario in your game where the character's magic inventory slots get locked due to a curse or something. That's totally possible, right?"
    p "Sure, it's not the most common thing, but it doesn't hurt to have it there. It's like one of those items you're hording, just chilling quietly in the background. You don't have to use it if you don't want to."
    show F_lock
    p "Alright let's lock up 20 slots to demonstrate the {color=#fc8a08}lock_slots(20){/color} function."
    hide F_lock
# ###################################################################################
# # ██╗      ██████╗  ██████╗██╗  ██╗    ███████╗██╗      ██████╗ ████████╗███████╗ #
# # ██║     ██╔═══██╗██╔════╝██║ ██╔╝    ██╔════╝██║     ██╔═══██╗╚══██╔══╝██╔════╝ #
# # ██║     ██║   ██║██║     █████╔╝     ███████╗██║     ██║   ██║   ██║   ███████╗ #
# # ██║     ██║   ██║██║     ██╔═██╗     ╚════██║██║     ██║   ██║   ██║   ╚════██║ #
# # ███████╗╚██████╔╝╚██████╗██║  ██╗    ███████║███████╗╚██████╔╝   ██║   ███████║ #
# # ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚══════╝╚══════╝ ╚═════╝    ╚═╝   ╚══════╝ #
# ###################################################################################
    ## Lock 20 slots from PAIS
    $ inventory.lock_slots(20)

    ## Expose PAIS inventory screen by Patchmonk
    show screen scrInventory

    p "Kind of depressing, isn't it? After unlocking all the slots, suddenly we lock this row of slots. I'm already feeling really bad, who knows how the player would react to such a thing. Crazy, isn't it? "
    p "Well, we demonstrated our lock function. The thing is, I'm a bit of a softy, so I'm going to unlock the 20 locked slots again even though it's just a tutorial."
# ######################################################################################################
# # ██╗   ██╗███╗   ██╗██╗      ██████╗  ██████╗██╗  ██╗    ███████╗██╗      ██████╗ ████████╗███████╗ #
# # ██║   ██║████╗  ██║██║     ██╔═══██╗██╔════╝██║ ██╔╝    ██╔════╝██║     ██╔═══██╗╚══██╔══╝██╔════╝ #
# # ██║   ██║██╔██╗ ██║██║     ██║   ██║██║     █████╔╝     ███████╗██║     ██║   ██║   ██║   ███████╗ #
# # ██║   ██║██║╚██╗██║██║     ██║   ██║██║     ██╔═██╗     ╚════██║██║     ██║   ██║   ██║   ╚════██║ #
# # ╚██████╔╝██║ ╚████║███████╗╚██████╔╝╚██████╗██║  ██╗    ███████║███████╗╚██████╔╝   ██║   ███████║ #
# #  ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚══════╝╚══════╝ ╚═════╝    ╚═╝   ╚══════╝ #
# ######################################################################################################
    ## Unlock 20 slots from PAIS
    $ inventory.unlock_slots(20)

    p "Well, we've talked a lot about slots. You're probably tired of hearing about them by now. I promise this is the last time I'll mention slots."
    ## Expose PAIS inventory screen by Patchmonk
    show screen scrInventory
    p "If you think about it, the default 30 slots might not cut it for your game. So, what do you do in such a scenario? Don't sweat it, we've got a function for that too!"

    show G_inc
    p "If you're worried that adding more slots will make the inventory grid explode from lack of space, fear not! Ren'Py's got your back with a handy scroll bar that will magically manage it all."
    p "It's already built into your screen code and ready to handle any number of slots. Just add more slots, and watch the scroll bar spring into action!"
    p "As always, we need to call the {color=#fc8a08}increase_slot_count(14){/color} function. In the parameter, we define we want 14 more slots"
# ###############################################################################################################
# # ██╗███╗   ██╗ ██████╗██████╗ ███████╗ █████╗ ███████╗███████╗    ███████╗██╗      ██████╗ ████████╗███████╗ #
# # ██║████╗  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝    ██╔════╝██║     ██╔═══██╗╚══██╔══╝██╔════╝ #
# # ██║██╔██╗ ██║██║     ██████╔╝█████╗  ███████║███████╗█████╗      ███████╗██║     ██║   ██║   ██║   ███████╗ #
# # ██║██║╚██╗██║██║     ██╔══██╗██╔══╝  ██╔══██║╚════██║██╔══╝      ╚════██║██║     ██║   ██║   ██║   ╚════██║ #
# # ██║██║ ╚████║╚██████╗██║  ██║███████╗██║  ██║███████║███████╗    ███████║███████╗╚██████╔╝   ██║   ███████║ #
# # ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚══════╝╚══════╝ ╚═════╝    ╚═╝   ╚══════╝ #
# ###############################################################################################################
    ## Increase the slot count of PAIS by 14
    $ inventory.increase_slot_count(14)
    hide G_inc

    ## Expose PAIS inventory screen by Patchmonk
    show screen scrInventory
    p "We've got seven slots per row, so I thought, why not add two more rows? Voilà, 14 extra slots! Just give that scroll bar a little nudge to check them out."
    "Mind me we added 14 locked slots to the 30 already unlocked and present slots."
    p "I fought off the temptation to add a few dozen more rows. Now it's your turn! Conquer that scrollbar by adjusting the value of the {color=#fc8a08}increase_slot_count{/color} function."

    ## //  start delete --> #############################################################################
    p "A few words of advice from my friend:"
    ## Second jump-in guest appearance
    $ show_notification("Be advised trouble arises from the left this time!", sound_type="demon_rises")
    show bgb with moveinleft
    b "Pay attention to filepaths, capitalization and image dimensions, this will save you a lotta trouble! (trouble I went through back and forth so many times that I even considered to enter a loop lol:)."
    b "Use distinctive, descriptive names and store files in seperate folders using some kind of structure that makes sense. Make up your mind about upper case and lower case."
    b "I'm not a teacher, but I surely can easily show you how to make a big mess of it in seconds almost irreversibly :)"
    b "Lastly, the graphics I added and the simple annoying click sounds and stuff are not staggering, I'm well aware of that. I only implemented them to provide you with code to save you some time searching."
    b "That's it for now don't hesitate to reach out for help if you bump into any bug somewhere. PAIS 1.2.7 is thoroughly tested on Windows 10 at 1920 x 1080 px.(only)"
    b "I did not once find any bug AT ALL. Before returning control to the man behind PAIS I also want to express my gratitude for being allowed to contribute to this master piece."
    b "It's nothing short from an honor, something I don't take very lightly at all!"
    ## Dissappear into the blue
    hide bgb with dissolve
    ## \\ <-- end delete ################################################################################

    p "Well, I guess this is the grande finale of our tutorial! Thanks for sticking around. I'm thrilled about your interest in my project."
    p "I'd be thrilled if you could give me a shout-out by mentioning my name in your project! I put my heart into creating this, and it would mean the world to see it recognized and shared so others can enjoy it too."
    p "If you ever want to connect, feel free to drop a hello! I might not be able to respond immediately, but I'll absolutely smile knowing someone appreciated my work."
    p "Want to see what else I've been building? Check out my GitHub or Itch.io profile. I'm always tinkering with something new! "
    p "If you spot a bug or have ideas to make this even better, feel free to open an issue or submit a pull request on GitHub. I will make every effort to ensure the stability of this project, and I'd love your help shaping it!"
    p "Best of luck bringing your game to life. I hope it shines brightly and finds the success it deserves! Go create something unforgettable, and remember: every great game starts with a spark of passion. Yours is already glowing! 🔥"
    ## we quit

return
