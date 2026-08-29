[app]

title = Multi-Garage Assistant
package.name = multigarage
package.domain = org.yuriy.autocare

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,db
source.include_patterns = assets/*,assets/**/*

version = 1.0

requirements = python3==3.10.11,kivy,kivymd,pillow,plyer,sqlite3

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/assets/icon.png
presplash.filename = %(source.dir)s/assets/presplash.png
android.presplash_color = #0E0F11

android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,POST_NOTIFICATIONS

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a,armeabi-v7a

android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
