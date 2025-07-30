[app]

# (str) Title of your application
title = Smart Survey

# (str) Package name
package.name = smartsurvey

# (str) Package domain (needed for android/ios packaging)
package.domain = org.mycompany.smartsurey

# (str) Source code where the main.py live
source.dir = .
# (list) Source files to include (let buildozer find them)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of modules to support for auto-detection
source.exclude_dirs = tests, bin, venv, .venv, __pycache__

# (str) Application versioning
version = 0.1

# (list) Kivy requirements
# CORRECTED: Specifying a stable Python version to fix build tool conflicts.
requirements = python3.10,kivy,plyer,pillow,android

# (str) Presplash image
presplash.filename = %(source.dir)s/placeholder.png

# (str) Icon filename
icon.filename = %(source.dir)s/placeholder.png

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (list) Permissions
android.permissions = CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Android API to use.
# 31 is a stable target.
android.api = 31

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use.
# Specifying this helps prevent issues.
android.ndk = 25b

# (list) Architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (str) The Android SDK version to use
# android.sdk = 24

# (str) The Android NDK path.
# If not set, will be downloaded automatically.
# android.ndk_path =

# (str) The Android SDK path.
# If not set, will be downloaded automatically.
# android.sdk_path = 


# (bool) If True, then automatically accept SDK license 
# agreements. This is intended for automation only. If set to False, 
# the default, you will be shown the license when first running 
# buildozer.
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
