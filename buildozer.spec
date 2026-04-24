[app]

title = ImageClicker
package.name = imageclicker
package.domain = org.pixelTS
source.dir = .

version = 1.0

requirements = python3,kivy,plyer,Pillow

orientation = portrait
fullscreen = 0

android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]

log_level = 2
warn_dirname = True

android.sdk_api = 21