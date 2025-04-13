## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.

## Folder where renpy will search for all except scripts

define config.search_prefixes = [
    "",
    "art/",
    "art/fonts/",
    "audio/",
    "components/notification/audio/",
    "components/notification/images/gui",
    "components/inventory_system/images/gui/",
    "components/inventory_system/images/icons/",
    "images/",
    "screenshots/",
    "video/",
    ]

## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Patchmonk's Advanced Inventory System 1.2.7")
define config.developer = True
define config.debug_image_cache = False

## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True

define config.log = False
define config.log_gl_shaders = False
## The version of the game.

define config.version = "1.2.7"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.
# #################################################################################################################
# #██████╗ ███████╗██████╗ ██████╗ ██╗   ██╗     ██████╗        ██████╗ ███████╗███╗   ██╗██████╗ ███████╗██████╗ #
# #██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝    ██╔════╝        ██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗#
# #██████╔╝█████╗  ██████╔╝██████╔╝ ╚████╔╝     ██║  ███╗       ██████╔╝█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝#
# #██╔══██╗██╔══╝  ██╔══██╗██╔══██╗  ╚██╔╝      ██║   ██║       ██╔══██╗██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗#
# #██████╔╝███████╗██║  ██║██║  ██║   ██║       ╚██████╔╝██╗    ██████╔╝███████╗██║ ╚████║██████╔╝███████╗██║  ██║#
# #╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═════╝ ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝#
# #################################################################################################################

define gui.about = _p("""

Patchmonk's Advanced Inventory System 1.2.7 is one of the greatest RenPy inventory systems you will find on the internet.

Featuring a stackable system with an advanced notification system, PAIS will always tell you what is happening both by visuals and sounds.

Higly customizable, it show cases class creation and management, modularity and how to incorporate the nice-but-useless stuff.

The inventory uses image buttons which for now do simple stuff and use tooltips.

All of this in Jip-and-Janneke style: this could very well be the next best thing to install right after you tried one of the RenPy tutorials.

Patchmonk and Berry G. Bender's common goal was to create a system that would work after installation without any hassles.

This tutorial will show:

- Adding items

- Removing items

- Increasing slot count

- Locking slots

- Unlocking slots

- Customizing its look and feel

- Customizing the notification system

- Adding a splashscreen, skipscreen, webm video, live2d integration

- All is neatly covered and documented

Please take note of the all the comments we placed into the source code.

PAIS 1.2.7 is thoroughly tested on both Dutch and English Windows 10 at 1920 x 1080 resolution.(also UHD but we focused on HD)

It was edited by Microsoft Visual Studio in UTF-8 with BOM (whatever that entails).

It is believed to work flawlessly. That having said, I'm certainly not a RenPy expert so where I encountered code I did not

understand I simply placed a comment to acknowledge that. (this was easier than to figure each and every line of code out :)

Credits go to Patchmonk - Creator, author and designer of PAIS 1.2.7 - responsible for all the rocket science

Berry G. Bender - Assistant Manager - responsible for most nice-but-useless graphics (art folder and yeah nice isn't the word I guess ;)

By no means any of this should be considered competitive nor a show off or whatever. It will hopefully save you some time searching for the solutions provided.

Regards Berry G. Bender

Ps be sure to contact us in case you bump into any problems we will do our utmost to solve it.
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "pais"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "pais"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**.rpyc', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
