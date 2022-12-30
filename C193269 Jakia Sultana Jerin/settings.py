def settings(device_settings=None, profile_settings=None, moderator_settings=None, calendar_settings=None, sounds_settings=None):
    if device_settings is None:
        device_settings = {
            "display_brightness": 50,
            "sleep_timeout": 30,
            "vibration": True
        }
    if profile_settings is None:
        profile_settings = {
            "profile_name": "John Doe",
            "profile_picture": "default.jpg",
            "status_message": "Available"
        }
    if moderator_settings is None:
        moderator_settings = {
            "moderator_role": "Moderator",
            "moderation_level": 2
        }
    if calendar_settings is None:
        calendar_settings = {
            "default_view": "week",
            "reminders": True
        }
    if sounds_settings is None:
        sounds_settings = {
            "notification_sound": "default.mp3",
            "ringtone": "default.mp3"
        }
    return {
        "device": device_settings,
        "profile": profile_settings,
        "moderator": moderator_settings,
        "calendar": calendar_settings,
        "sounds": sounds_settings
    }

# Use the function
current_settings = settings()
print(current_settings)
# Output: 
# {
#   "device": {
#     "display_brightness": 50,
#     "sleep_timeout": 30,
#     "vibration": True
#   },
#   "profile": {
#     "profile_name": "John Doe",
#     "profile_picture": "default.jpg",
#     "status_message": "Available"
#   },
#   "moderator": {
#     "moderator_role": "Moderator",
#     "moderation_level": 2
#   },
#   "calendar": {
#     "default_view": "week",
#     "reminders": True
#   },
#   "sounds": {
#     "notification_sound": "default.mp3",
#     "ringtone": "default.mp3"
#   }
# }

# Update the settings
new_settings = {
    "device": {
        "display_brightness": 70,
        "sleep_timeout": 60,
        "vibration": False
    },
    "profile": {
        "profile_name": "Jane Doe",
        "profile_picture": "profile.jpg",
        "status_message": "Away"
    },
    "moderator": {
        "moderator_role": "Super Moderator",
        "moderation_level": 3
    },
    "calendar": {
        "default_view": "month",
        "reminders": False
    },
    "sounds": {
        "notification_sound": "notification.mp3",
        "ringtone": "ringtone.mp3"
    }

