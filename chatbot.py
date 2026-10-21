"""
CodSoft AI Internship - Task 1: Rule-Based Chatbot
Matches user input against predefined regex patterns (pattern matching +
if/else logic) and replies with an appropriate response.
"""
import random
import re
from datetime import datetime


class RuleBasedChatbot:
    def __init__(self, bot_name="CodBot"):
        self.bot_name = bot_name
        self.user_name = None
        # (pattern, handler) - order matters: first match wins.
        self.rules = [
            (r"\b(bye|goodbye|exit|quit|see you)\b", self._bye),
            (r"\b(my name is|i am called|call me)\s+(?P<name>[a-zA-Z]+)", self._set_name),
            (r"\bwhat('?s| is) my name\b|\bdo you know my name\b", self._get_name),
            (r"\b(hello|hi|hey|namaste|good (morning|afternoon|evening))\b", self._greet),
            (r"\bhow are you\b|\bhow('?s| is) it going\b", self._how_are_you),
            (r"\b(your name|who are you)\b", self._who_are_you),
            (r"\bwhat can you do\b|\bhelp\b", self._help),
            (r"\b(time)\b", self._time),
            (r"\b(date|today|day)\b", self._date),
            (r"\b(joke|funny|make me laugh)\b", self._joke),
            (r"(?P<a>-?\d+(?:\.\d+)?)\s*(?P<op>[+\-*/x])\s*(?P<b>-?\d+(?:\.\d+)?)", self._calc),
            (r"\b(what is|define|explain)\s+(ai|artificial intelligence)\b", self._about_ai),
            (r"\b(what is|define|explain)\s+(ml|machine learning)\b", self._about_ml),
            (r"\b(codsoft|internship)\b", self._codsoft),
            (r"\b(thanks|thank you|thx)\b", self._thanks),
            (r"\b(weather)\b", self._weather),
        ]
        self.fallbacks = [
            "Sorry, I didn't understand that. Type 'help' to see what I can do.",
            "Hmm, I'm not sure about that. Could you rephrase it?",
            "I'm a simple rule-based bot, so I only know a few things. Try 'help'.",
        ]

    # ---------- handlers ----------
    def _greet(self, m):
        hour = datetime.now().hour
        part = "morning" if hour < 12 else "afternoon" if hour < 17 else "evening"
        who = f", {self.user_name}" if self.user_name else ""
        return random.choice([f"Hello{who}! Good {part}.", f"Hi{who}! How can I help you?",
                              f"Hey{who}! Nice to see you."])

    def _how_are_you(self, m):
        return "I'm just code, but I'm running perfectly! How about you?"

    def _who_are_you(self, m):
        return f"I'm {self.bot_name}, a rule-based chatbot built for the CodSoft AI internship."

    def _set_name(self, m):
        self.user_name = m.group("name").capitalize()
        return f"Nice to meet you, {self.user_name}!"

    def _get_name(self, m):
        return (f"Your name is {self.user_name}." if self.user_name
                else "You haven't told me your name yet. Say 'my name is ...'.")

    def _help(self, m):
        return ("I can: greet you, remember your name, tell the time/date, tell jokes, "
                "do simple maths (e.g. 12 * 7), explain AI/ML, and chat about the internship. "
                "Say 'bye' to quit.")

    def _time(self, m):
        return "The current time is " + datetime.now().strftime("%I:%M %p") + "."

    def _date(self, m):
        return "Today is " + datetime.now().strftime("%A, %d %B %Y") + "."

    def _joke(self, m):
        return random.choice([
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "There are 10 types of people: those who understand binary and those who don't.",
            "Why did the AI go to school? To improve its learning rate!",
        ])

    def _calc(self, m):
        a, b, op = float(m.group("a")), float(m.group("b")), m.group("op")
        if op == "+": r = a + b
        elif op == "-": r = a - b
        elif op in ("*", "x"): r = a * b
        else:
            if b == 0:
                return "I can't divide by zero!"
            r = a / b
        return f"The answer is {r:g}."

    def _about_ai(self, m):
        return ("Artificial Intelligence is the field of building machines that can perform "
                "tasks that normally need human intelligence, like learning and decision-making.")

    def _about_ml(self, m):
        return ("Machine Learning is a subset of AI where systems learn patterns from data "
                "instead of being explicitly programmed.")

    def _codsoft(self, m):
        return "CodSoft is a tech education platform offering virtual internships. This bot is my Task 1!"

    def _thanks(self, m):
        return random.choice(["You're welcome!", "Happy to help!", "Anytime!"])

    def _weather(self, m):
        return "I can't check live weather, but a weather app or website will tell you!"

    def _bye(self, m):
        return "Goodbye! Have a great day!"

    # ---------- core ----------
    def respond(self, text):
        text = text.strip().lower()
        if not text:
            return "Please type something."
        for pattern, handler in self.rules:
            match = re.search(pattern, text)
            if match:
                return handler(match)
        return random.choice(self.fallbacks)

    def is_exit(self, text):
        return re.search(self.rules[0][0], text.lower()) is not None


def main():
    bot = RuleBasedChatbot()
    print(f"{bot.bot_name}: Hi! I'm {bot.bot_name}. Type 'help' for options, 'bye' to quit.")
    while True:
        try:
            user = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print(f"\n{bot.bot_name}: Goodbye!")
            break
        print(f"{bot.bot_name}: {bot.respond(user)}")
        if bot.is_exit(user):
            break


if __name__ == "__main__":
    main()
