def is_scam(text):
    scam_words = ["lottery", "winner", "urgent", "otp", "kyc", "blocked", "prize", "click link", "free money"]
    text = text.lower()
    for word in scam_words:
        if word in text:
            return True, f"Scam word found: {word}"
    return False, "Safe hai"