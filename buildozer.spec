# buildozer.spec
# This file describes the application.
# For more information on buildozer.spec, see:
# http://kivy.org/docs/packaging/buildozer.html

[app]
# (str) Title of your application
title = GateSurvey

# (str) Package name
package.name = gatesurvey

# (str) Package domain
package.domain = org.a1launchpad.tuhin

# (str) Source code directory
source.dir = .

# (str) Application version
version = 1.0

# (list) List of requirements for your app
# Explicitly setting Python 3.11.5 as seen in logs for better compatibility.
# Removed opencv-python temporarily to isolate build issues.
# Removed explicit cython version to let buildozer pick compatible.
requirements = python==3.11.5,kivy==2.3.0,plyer,pillow

# (str) App orientation
orientation = landscape

# (list) List of Android permissions your app needs.
# The 'android' module for runtime permissions is implicitly included.
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,CAMERA

# --- FIX FOR ANDROID COMPATIBILITY ---
# (int) Target Android API level. 33 is required for newer devices and permissions.
android.api = 33

# (int) Minimum Android API level. 21 covers about 99% of devices.
android.minapi = 21

# (list) Android services
services =

[buildozer]
# (int) Log level
log_level = 2
