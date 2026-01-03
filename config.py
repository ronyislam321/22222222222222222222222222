import os
from dotenv import load_dotenv

load_dotenv()

# -------------------------
# FIXED ADMIN IDS (Do not overwrite)
# -------------------------
ADMIN_IDS = [6607756715]   # <-- আপনার Telegram numeric ID

TELEGRAM_BOT_TOKEN = os.getenv("BOT_TOKEN", "")
FISH_AUDIO_API_KEY = os.getenv("VOICE_API_KEY", "")
FISH_AUDIO_BASE_URL = os.getenv("FISH_AUDIO_BASE_URL", "https://api.fish.audio")
FISH_AUDIO_BACKEND = os.getenv("FISH_AUDIO_BACKEND", "s1")
FISH_AUDIO_MP3_BITRATE = int(os.getenv("FISH_AUDIO_MP3_BITRATE", "128"))

ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "t.me/sellmodel")
WEBSITE_URL   = os.getenv("WEBSITE_URL", "modelboxbd.com")

# REMOVE OLD ADMIN_IDS OVERRIDE ❌
# ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip().isdigit()]

DB_PATH = os.getenv("DB_PATH", "file.db")
VOICES_DIR = os.getenv("VOICES_DIR", "voices")

COST_PER_VOICE = 1
REQUIRE_VALIDITY_FOR_TTS = False
MAX_TTS_CHARS = int(os.getenv("MAX_TTS_CHARS", "200"))

DEFAULT_MODELS = [
    {"id": "230c2ddcbfa14c0bbd3879f26662eb56", "name": "Sara"},
    {"id": "c6733a704f2e41aab763e04685817d91", "name": "Mia Queen"},
    {"id": "a14030b243bf41fd968c94cf1863e2b7", "name": "Evelyan"},
    {"id": "29913697e157485c941c737314c27819", "name": "Ruby"},
    {"id": "d75c78da679a4d8480e4bcfb6c60bdc6", "name": "Nora"},
    
]

USE_CONFIG_MODELS_ONLY = True

PLANS = [
    {"name": "Starter", "credits": 50, "price": "$5", "validity_days": 30},
    {"name": "Pro", "credits": 200, "price": "$15", "validity_days": 30},
    {"name": "Unlimited-Day", "credits": 400, "price": "$30", "validity_days": 30},
]

USE_WEBHOOK = os.getenv("USE_WEBHOOK", "false").lower() == "true"
WEBHOOK_BASE_URL = os.getenv("WEBHOOK_BASE_URL", "")
PORT = int(os.getenv("PORT", "8000"))
