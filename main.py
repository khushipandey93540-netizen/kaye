reviews = [
    "Delivery was late and I am angry",
    "Loved the product, amazing quality",
    "Customer support was helpful but slow",
    "Worst experience ever"
]

print("Consumer Reviews:")
for review in reviews:
    print("-", review)
def simple_mood_detector(text):
    if "love" in text or "amazing" in text:
        return "Happy"
    elif "angry" in text or "worst" in text or "late" in text:
        return "Angry"
    else:
        return "Neutral"

print("\nDetected Moods:")
for review in reviews:
    mood = simple_mood_detector(review.lower())
    print("-", mood, "→", review)

