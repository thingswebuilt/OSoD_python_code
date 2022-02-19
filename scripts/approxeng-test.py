from approxeng.input.selectbinder import ControllerResource

# Get a joystick
with ControllerResource() as joystick:
    # Loop until we're disconnected
    while joystick.connected:
        # Call check_presses at the top of the loop to check for presses and releases, this returns the buttons
        # pressed, but not the ones released. It does, however, have the side effect of updating the
        # joystick.presses and joystick.releases properties, so you use it even if you're not storing the return
        # value anywhere.
        joystick.check_presses()
        # Check for a button press
        if joystick.presses.circle:
            print("CIRCLE pressed since last check")
        # Check for a button release
        if joystick.releases.circle:
            print("CIRCLE released since last check")

        # If we had any releases, print the list of released buttons by standard name
        if joystick.has_releases:
            print(joystick.releases)
