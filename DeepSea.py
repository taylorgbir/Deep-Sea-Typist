import random
import time
from IPython.display import clear_output

easy_words = ["fish", "wave", "tide", "reef", "shell"]
medium_words = ["ocean", "coral", "harbor", "kelp", "anchor"]
hard_words = ["submarine", "octopus", "dolphin", "current", "seabed"]

score = 0
lives = 3
total_chars = 0
correct_chars = 0

start_time = time.time()

def get_word():
    global score
    if score < 5:
        return random.choice(easy_words)
    elif score < 15:
        return random.choice(medium_words)
    else:
        return random.choice(hard_words)

def highlight_word(word, typed):
    result = ""
    for i, letter in enumerate(word):
        if i < len(typed) and typed[i] == letter:
            result += f"[{letter}]"
        else:
            result += letter
    return result

while lives > 0:
    word = get_word()
    
    clear_output(wait=True)
    print("🌊 Deep Sea Typist 🌊")
    print(f"Score: {score} | Lives: {lives}")
    
    elapsed_minutes = (time.time() - start_time) / 60
    wpm = round((correct_chars / 5) / elapsed_minutes) if elapsed_minutes > 0 else 0
    accuracy = round((correct_chars / total_chars) * 100) if total_chars > 0 else 100
    
    print(f"WPM: {wpm} | Accuracy: {accuracy}%\n")
    print("Type the word:\n")
    print(word)
    
    typed = input("\nYour input: ")
    
    total_chars += len(typed)
    
    if typed == word:
        print("🐟 Cleaned!")
        score += 1
        correct_chars += len(word)
    else:
        print("❌ Missed!")
        lives -= 1
    
    time.sleep(1)

clear_output()
print("🌊 OCEAN COLLAPSED 🌊")
print(f"Final Score: {score}")

elapsed_minutes = (time.time() - start_time) / 60
wpm = round((correct_chars / 5) / elapsed_minutes) if elapsed_minutes > 0 else 0
accuracy = round((correct_chars / total_chars) * 100) if total_chars > 0 else 100

print(f"WPM: {wpm}")
print(f"Accuracy: {accuracy}%")
