# CodSoft AI Internship – Task 1: Rule-Based Chatbot

A simple chatbot that uses **regex pattern matching + if/else style rules** to understand
user input and reply. No external libraries needed.

## Features
- Greetings (time-aware), remembers your name
- Time and date, jokes
- Simple calculator (`12 * 7`)
- Explains AI / ML, answers questions about the internship
- Fallback replies for unknown input

## Run
```bash
python chatbot.py
```

## Test
```bash
python test_chatbot.py
```

## How it works
`RuleBasedChatbot.rules` is an ordered list of `(regex, handler)` pairs. The input is
lower-cased, checked against each pattern in order, and the first match's handler
generates the reply. If nothing matches, a fallback message is returned.

## Add your own rule
```python
self.rules.append((r"\bpizza\b", lambda m: "I love pizza too!"))
```

#codsoft #AI #internship
