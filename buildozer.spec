# buildozer.spec
# This file describes the application.
# For more information on buildozer.spec, see:
# http://kivy.org/docs/packaging/buildozer.html

[app]

# (str) Title of your application
title = Smart Gate Survey

# (str) Package name
package.name = com.yourcompany.smartgatesurvey

# (str) Package domain (needed for android/ios packaging)
package.domain = yourcompany.com

# (str) Source code where the main.py resides
source.dir = .

# (list) Application requirements
# Add 'android' for Android-specific APIs (e.g., camera access via Plyer)
# Changed python3.10 to python3.11 to align with available p4a distributions
requirements = python3.11,kivy,plyer,pillow,android

# (str) The entry point of your application
main.py = main.py

# (list) Android permissions
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Android API target (e.g., 27, 28, 29, 30, 31, 32, 33)
# Keep this aligned with recent Android versions for better compatibility
android.api = 31

# (str) Android NDK version (e.g., 19b, 20b, 21b, 22b, 25b)
android.ndk = 25b

# (bool) Accept Android SDK licenses automatically (required for CI/CD)
android.accept_sdk_license = True

# (int) Log level (0=none, 1=error, 2=warning, 3=info, 4=debug)
log_level = 2

# (list) Application version
version = 0.1

# (bool) If your app doesn't need internet permission, set this to False
# internet = True

# (list) List of target architectures to compile for
# This ensures compatibility across a wider range of Android devices
android.archs = arm64-v8a,armeabi-v7a

# (str) Path to the Android SDK (if not set in environment variables)
# android.sdk = /opt/android-sdk

# (str) Path to the Android NDK (if not set in environment variables)
# android.ndk = /opt/android-ndk

# (bool) Enable debug mode (more verbose logging, non-optimized build)
# Set to False for release builds
debug = True

# (list) Exclude files from the APK
# source.exclude_exts = pyc,pyo,orig
# source.exclude_dirs = tests,bin,build,dist

# (str) Icon file
# icon.filename = icon.png

# (str) Splash screen file
# splash.filename = splash.png

# (str) Orientation of the application (portrait, landscape, sensor)
orientation = portrait

[buildozer]
# (str) The Buildozer version to use. 'stable' for the latest stable release.
# You can also specify a specific version like '1.2.0' or 'master' for the latest development version.
buildozer_version = stable
