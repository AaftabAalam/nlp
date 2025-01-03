import re

authenticity_keywords = [
    "honest", "genuine", "sincere", "trustworthy", "Integrity", 
    "Transparent", "Authentic", "Credible", "Dependable", "Reliable", 
    "Ethical", "Real", "Truthful", "Verifiable", "Legitimate", 
    "Candid", "Straightforward", "Honorable", "Faithful", "Loyal"
]

positive_emotions = [
    "happy", "joyful", "excited", "grateful", "content", "proud"
    "enthusiastic", "cheerful", "elated", "love", "optimistic"
]

negative_emotions = [
    "sad", "angry", "frustrated", "upset", "disappointed", "guilty", "worried" 
    "anxious", "depressed", "miserable", "hate", "jealous", "regret"
]
def detect_authenticity(text, authenticity_keywords):
    authenticity_count = sum([len(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE)) for word in authenticity_keywords])
    
    total_words = len(text.split())

    if authenticity_count == 0:
        return {
            "Message": "No authenticity signals detected",
            "Authenticity Keywords": 0,
            "Total Words": total_words,
            "Authenticity Level": "Neutral"
        }
    authenticity_ratio = authenticity_count / total_words

    if authenticity_ratio > 0.2:
        authenticity_level = "Highly authentic (consistent use of authenticity-related words)"
    elif authenticity_ratio > 0.1:
        authenticity_level = "Moderately authentic"
    else:
        authenticity_level = "Low authenticity detected (minimal use of authenticity-related words)"

    result = {
        "Authenticity Keywords": authenticity_count,
        "Total Words": total_words,
        "Authenticity Ratio": round(authenticity_ratio, 2),
        "Authenticity Level": authenticity_level,
    }
    return result


def consistency_of_emotion(text, positive_emotions, negative_emotions):
    positive_count = sum([len(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE)) for word in positive_emotions])
    negative_count = sum([len(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE)) for word in negative_emotions])

    total_emotion_words = positive_count + negative_count
    if total_emotion_words == 0:
        return {
            "Message": "No emotional tone detected",
            "Positive Words": 0,
            "Negative Words": 0,
            "Total Emotion Words": 0,
            "Consistency": "Neutral tone detected"
        }
    positive_ratio = positive_count / total_emotion_words
    negative_ratio = negative_count / total_emotion_words

    if positive_ratio > 0.7:
        consistency = "Strongly positive emotional tone detected"
    elif negative_ratio > 0.7:
        consistency = "Strongly negative emotional tone detected"
    elif 0.4 <= positive_ratio <= 0.6:
        consistency = "Balanced emotional tone detected (equal mix of positive and negative emotions)"
    else:
        consistency = "Inconsistent emotional tone detected (slight dominance of one type)"

    balance_difference = abs(positive_ratio - negative_ratio)

    if balance_difference < 0.2 and total_emotion_words > 10:
        consistency = "Highly dynamic emotional tone detected (frequent emotional shifts)"
    elif balance_difference < 0.1:
        consistency = "Highly balanced emotional tone detected"

    result = {
        "Positive Words": positive_count,
        "Negative Words": negative_count,
        "Total Emotion Words": total_emotion_words,
        "Positive Ratio": round(positive_ratio, 2),
        "Negative Ratio": round(negative_ratio, 2),
        "Balance Difference": round(balance_difference, 2),
        "Consistency": consistency,
    }
    return result

positive_opinion = [
    "love", "like", "enjoy", "prefer", "agree", "approve", "support", "recommend"
]

negative_opinion = [
    "hate", "dislike", "avoid", "oppose", "disagree", "criticize", "reject", "condemn"
]

def consistency_of_opinion(text, positive_opinion, negative_opinion):
    positive_count = sum([len(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE)) for word in positive_opinion])
    negative_count = sum([len(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE)) for word in negative_opinion])
    
    total_count = positive_count + negative_count
    
    if total_count == 0:
        consistency = "Neutral or no opinions detected (no significant positive or negative opinions)"
    elif positive_count > 0 and negative_count > 0:
        positive_ratio = positive_count / total_count
        negative_ratio = negative_count / total_count
        
        if 0.4 <= positive_ratio <= 0.6:
            consistency = "Mixed opinions detected (balanced views with conflicting perspectives)"
        elif positive_ratio > 0.6:
            consistency = "Consistent opinions detected (majority positive views)"
        else:
            consistency = "Consistent opinions detected (majority negative views)"
    elif positive_count > 0:
        consistency = "Consistent opinions detected (only positive views)"
    else:
        consistency = "Consistent opinions detected (only negative views)"
    
    result = {
        "Positive Opinions": positive_count,
        "Negative Opinions": negative_count,
        "Total Opinions": total_count,
        "Consistency": consistency,
    }
    return result

engagement_keywords = [
    "yes", "okay", "thanks", "sure", "got it", "understood", "right", "exactly", "welcome"
]

clarifying_keywords = [
    "can you explain", "what do you mean", "could you clarify", "why", "how", "could you elaborate", 
    "what", "when", "where", "how"
]

def alertness_in_conversation(text, engagement_keywords, clarifying_keywords):
    engagement_count = sum([len(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE)) for word in engagement_keywords])
    clarifying_count = sum([len(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE)) for word in clarifying_keywords])

    total_alertness_words = engagement_count + clarifying_count
    total_words = len(text.split())

    if total_alertness_words == 0:
        return {
            "Message": "No engagement detected",
            "Engagement Words": 0,
            "Clarifying Words": 0,
            "Total Words": total_words,
            "Alertness Level": "Unengaged conversation detected"
        }

    engagement_ratio = engagement_count / total_alertness_words
    clarifying_ratio = clarifying_count / total_alertness_words

    if engagement_ratio > 0.7:
        alertness_level = "Highly engaged and attentive"
    elif clarifying_ratio > 0.7:
        alertness_level = "Clarification-focused conversation detected"
    elif 0.4 <= engagement_ratio <= 0.6:
        alertness_level = "Balanced engagement and clarification detected"
    else:
        alertness_level = "Slightly responsive conversation"

    balance_difference = abs(engagement_ratio - clarifying_ratio)

    if balance_difference < 0.2 and total_alertness_words > 10:
        alertness_level = "Dynamic and balanced engagement detected"
    elif balance_difference < 0.1:
        alertness_level = "Highly balanced engagement detected"

    result = {
        "Engagement Words": engagement_count,
        "Clarifying Words": clarifying_count,
        "Total Alertness Words": total_alertness_words,
        "Total Words": total_words,
        "Engagement Ratio": round(engagement_ratio, 2),
        "Clarifying Ratio": round(clarifying_ratio, 2),
        "Balance Difference": round(balance_difference, 2),
        "Alertness Level": alertness_level,
    }
    return result