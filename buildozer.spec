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
# Do NOT pin Python to 3.7 (modern p4a uses newer Python).
# Keep requirements minimal and only what you import.
# - bcrypt for your password hashing
# - cffi is a bcrypt dependency on Android
# - openssl/requests/certifi for HTTPS calls (UrlRequest/requests)
# - sqlite3 for your local DB
requirements = python3,kivy,android,pillow,bcrypt,cffi,openssl,pyopenssl,httplib2,requests,certifi,sqlite3

# ---- Graphics (optional but recommended) ----
# Adjust paths to your real files (these are examples)
presplash.filename = %(source.dir)s/images/dice.png
icon.filename      = %(source.dir)s/images/dice.png

# ---- Orientation / UI ----
orientation = portrait
fullscreen = 0

# ---- Android specifics ----
# Keep only what you actually need; INTERNET is enough for HTTP(S).
android.permissions = android.permission.INTERNET, android.permission.WRITE_EXTERNAL_STORAGE, android.permission.READ_EXTERNAL_STORAGE, android.permission.ACCESS_NETWORK_STATE, android.permission.ACCESS_WIFI_STATE

# API/NDK that work well with current toolchains
android.api = 31
android.minapi = 21
android.ndk = 25b
# build both 32-bit and 64-bit
android.archs = arm64-v8a, armeabi-v7a

# Non-interactive license acceptance for CI
android.accept_sdk_license = True

# ---- Logging ----
# 0=errors only, 1=info, 2=debug (shows tool output)
log_level = 2
