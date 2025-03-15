from emotion_detection import emotion_detector

statements = ["I am glad this happened",
"I am really mad about this",
"I feel disgusted just hearing about this",
"I am so sad about this",
"I am really afraid that this will happen"]

for statement in statements:
    print(emotion_detector(statement)["dominant_emotion"])