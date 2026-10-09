import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "توکن ربات شما")

# Handle admin IDs, safely fall back to the provided list
admin_env = os.getenv("ADMIN_IDS", "ایدی عددی مالک")
ADMIN_IDS = [int(id_str) for id_str in admin_env.split(",") if id_str.strip()]

# Game loop settings
BACKGROUND_TICK_RATE = 15 * 60  # 15 minutes in seconds for minor ticks (needs decay)
DAILY_TICK_RATE = 60 * 60       # 1 hour in seconds for major ticks (1 day in-game)
