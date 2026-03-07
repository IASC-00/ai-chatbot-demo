import os
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY', '')
CHAT_MODEL        = os.getenv('CHAT_MODEL', 'claude-haiku-4-5-20251001')
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY', '')
OPENROUTER_MODEL   = os.getenv('OPENROUTER_MODEL', 'meta-llama/llama-3.1-8b-instruct:free')
ADMIN_PASSWORD    = os.getenv('ADMIN_PASSWORD', 'changeme')
SECRET_KEY        = os.getenv('FLASK_SECRET_KEY', 'dev-secret-change-me')
DB_PATH           = os.getenv('DB_PATH', 'chatbot.db')
MAX_MESSAGES      = int(os.getenv('MAX_MESSAGES_PER_SESSION', '20'))
SUMMARIZE_AFTER   = int(os.getenv('SUMMARIZE_AFTER_TURNS', '10'))

_PROMPT_PATH = Path(__file__).parent / 'prompts' / 'harbor_coffee.txt'
_PROMPT_TEMPLATE = _PROMPT_PATH.read_text()


def build_system_prompt() -> str:
    now = datetime.now()
    day_name = now.strftime('%A')
    time_str  = now.strftime('%I:%M %p')

    hours_map = {
        'Monday':    '6:30 AM – 7:00 PM',
        'Tuesday':   '6:30 AM – 7:00 PM',
        'Wednesday': '6:30 AM – 7:00 PM',
        'Thursday':  '6:30 AM – 7:00 PM',
        'Friday':    '6:30 AM – 7:00 PM',
        'Saturday':  '7:00 AM – 8:00 PM',
        'Sunday':    '8:00 AM – 6:00 PM',
    }
    today_hours = hours_map[day_name]

    dynamic = (
        f"CURRENT CONTEXT (injected automatically):\n"
        f"  Today is {day_name}. Current local time: {time_str}.\n"
        f"  Today's hours: {today_hours}.\n"
        f"  Use this to answer 'are you open now?' or 'what time do you close?' accurately."
    )
    return _PROMPT_TEMPLATE.replace('{DYNAMIC_CONTEXT}', dynamic)
