from chatbot import RuleBasedChatbot

bot = RuleBasedChatbot()

def test_greeting():
    assert any(w in bot.respond("Hello").lower() for w in ("hello", "hi", "hey"))

def test_name_memory():
    assert "Ayush" in bot.respond("my name is ayush")
    assert "Ayush" in bot.respond("what is my name")

def test_math():
    assert bot.respond("12 * 7") == "The answer is 84."
    assert bot.respond("10 / 4") == "The answer is 2.5."
    assert "zero" in bot.respond("5 / 0")

def test_exit_and_fallback():
    assert bot.is_exit("bye")
    assert bot.respond("asdfghjkl") in bot.fallbacks

def test_ai():
    assert "Artificial Intelligence" in bot.respond("what is ai")

if __name__ == "__main__":
    for n, f in list(globals().items()):
        if n.startswith("test_"):
            f(); print("PASS", n)
