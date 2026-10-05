import re

def is_scam(text):
    if not text or not text.strip():
        return False, "Kuch likha hi nahi hai", 0

    text_lower = text.lower()
    
    high_risk = ["lottery", "winner", "congratulations you won", "kyc blocked", "account blocked", "otp", "cvv", "upi pin", "send money urgently", "prize"]
    medium_risk = ["urgent", "immediate action", "click here", "verify account", "bank account suspended", "free gift", "claim now", "limited time", "act now"]
    
    patterns = {
        "UPI/PhonePe Scam": r"(phonepe|google pay|paytm).*request|request.*money",
        "OTP Fraud": r"otp.*share|share.*otp|otp.*batao",
        "Link Scam": r"http://|bit\.ly|tinyurl|click.*link",
        "Lottery Scam": r"lottery|won.*\d+.*lakh|crore.*won"
    }
    
    risk_score = 0
    reasons = []
    
    for word in high_risk:
        if word in text_lower:
            risk_score += 40
            reasons.append(f"High risk word: '{word}'")
            
    for word in medium_risk:
        if word in text_lower:
            risk_score += 20
            reasons.append(f"Suspicious word: '{word}'")
    
    for name, pattern in patterns.items():
        if re.search(pattern, text_lower):
            risk_score += 35
            reasons.append(f"Pattern: {name}")

    if len(re.findall(r'\d{10,}', text)) > 0:
        risk_score += 15
        reasons.append("Long number found")
    
    if risk_score >= 70:
        return True, f"SCAM HAI! Risk: {risk_score}%. Reasons: {'; '.join(reasons[:3])}", risk_score
    elif risk_score >= 30:
        return False, f"Suspicious hai! Risk: {risk_score}%. {'; '.join(reasons[:2])}", risk_score
    else:
        return False, f"Safe hai. Risk: {risk_score}%", risk_score
  
