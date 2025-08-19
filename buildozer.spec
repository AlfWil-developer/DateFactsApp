[app]

# ---- App identity ----
title = Date Facts
package.name = datefacts
package.domain = org.test

# ---- Sources ----
source.dir = .
# fix 'atla' → 'atlas'; keep common assets/extensions
source.include_exts = py,kv,png,jpg,jpeg,atlas,ttf,otf

# If your entry point is NOT main.py, add:
# main.py = your_main_file.py

# ---- Versioning ----
version = 0.1

# ---- Requirements ----
# Keep requirements minimal and only what you actually import
requirements = python3,kivy,android,pillow,bcrypt,cffi,openssl,pyopenssl,httplib2,requests,certifi,sqlite3

# ---- Graphics (adjust paths to your repo) ----
presplash.filename = %(source.dir)s/images/dice.png
icon.filename      = %(source.dir)s/images/dice.png

# ---- Orientation / UI ----
orientation = portrait
fullscreen = 0

# ---- Android specifics ----
android.permissions = android.permission.INTERNET, android.permission.WRITE_EXTERNAL_STORAGE, android.permission.READ_EXTERNAL_STORAGE, android.permission.ACCESS_NETWORK_STATE, android.permission.ACCESS_WIFI_STATE

android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# Auto-accept licenses for CI/CD (GitHub Actions)
android.accept_sdk_license = True


[buildozer]

# Log level: 0=error, 1=info, 2=debug
log_level = 2

# Warn if running as root (safe to keep enabled)
warn_on_root = 1

# Optional: store build outputs in these folders
# build_dir = ./.buildozer
# bin_dir   = ./bin
