def detect_shoulder_surfing(distance_from_screen):
    if distance_from_screen < 1:
        return "Shoulder surfing detected! Be cautious"
    else:
        return "No shoulder surfing detected"

distance = 0.5
print(detect_shoulder_surfing(distance))