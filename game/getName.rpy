label splashscreen:
    scene black
    with Pause(1)

    show splashScreen1 with dissolve
    with Pause(2)

    show splashScreen2 with dissolve
    with Pause(2)

    show splashScreen3 with dissolve
    with Pause(3)

    scene black with dissolve
    with Pause(2)

    python:
        import os
        import subprocess

        pc_name = ""
        process_list = []

        # Get PC name on Windows
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass

            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        pc_name = user
            except:
                pass

    return