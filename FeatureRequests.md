# Introduction #

The current driver/input boards have very basic functionality.  For the solenoid drivers, it includes the initial kick (in ms) of the solenoid, the hold of the solenoid, and how the switch input is acted upon.  The input board also input pins to be triggered on rising edges, falling edges, and whether it is simply a state input.

For more complete documentation on the board interface, refer to https://code.google.com/p/open-pinball-project/source/browse/trunk/Docs/brdIntf.odt


# Approved Features #

The following are approved and currently implemented:
  * Persistent storage of configuration - persistently store configuration so that a serial port link isn't necessary.  Easier during development.  Allows pinball machine to run without requiring a PC/Pi to configure it.

The following are approved but not implemented:
  * Small delay before firing solenoid - As soon as a switch is active, the solenoid is fired.  A small delay (maybe up to 2 seconds) may make sense.  That would be particularly useful with kickout holes, and resetting drop targets.

# Rejected Features #

The following are features that were requested but have been rejected:
  * None so far