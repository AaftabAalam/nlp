import re

sarcasm_indicators = [
    "oh great", "sure thing", "totally", "yeah right", "as if", "of course", 
    "good for you", "brilliant", "nice job", "fantastic", "impressive", "just perfect", 
    "oh wonderful", "amazing", "really?", "wow, incredible", "yeah, that's exactly what I needed", 
    "as expected", "sure, whatever", "oh, that's lovely", "nice going", "just what I needed"
]

exaggeration_phrases = [
    "never in a million years", "the best ever", "so amazing", "unbelievable", "couldn't be better",
    "absolutely perfect", "over the moon", "world’s greatest", "once in a lifetime", 
    "hands down the best", "totally awesome", "unmatched", "the greatest thing ever", 
    "beyond belief", "insanely good", "unreal", "too good to be true", "without a doubt the best"
]

contradictory_phrases = [
    r"I love .* but .*",
    r"Sure.*not",
    r"Oh great.*problem",
    r"Yes, but .*",
    r"Absolutely.*never",
    r"Totally.*not",
    r"That's fine.*actually",
    r"I’m happy with .* but .*",
    r"I don't care, but .*",
    r"Sure, I’ll do it.*but it’s impossible",
    r"I like my job, but .*",
    r"This is fine, but .*",
    r"I’m okay with .* but .*",
    r"I agreed to this, but .*",
    r"It’s not bad, but .*",
    r"I enjoy .* but it’s exhausting",
    r"I’m satisfied, but .*",
    r"This is good, but .*",
    r"I wanted this, but .*",
    r"I’m lucky to have this job, but .*",
    r"I appreciate it, but .*",
    r"It’s manageable, but .*",
    r"I don’t mind .* but .*",
    r"It’s fine during the day, but .*",
    r"I can handle it, but .*",
    r"I shouldn’t complain, but .*",
    r"This is great, but .*",
    r"I’m grateful for this, but .*",
    r"I know it’s necessary, but .*",
    r"I want to stay, but .*",
    r"I should be happy, but .*",
    r"This feels right, but .*",
    r"I feel respected, but .*",
    r"I have enough time, but .*",
    r"My workload is fair, but .*",
    r"It’s flexible, but .*",
    r"The culture is inclusive, but .*",
    r"It’s supportive, but .*",
    r"It’s productive, but .*",
    r"It’s motivating, but .*",
    r"It’s balanced, but .*",
    r"My team is great, but .*",
    r"My boss is understanding, but .*",
    r"The company cares, but .*",
    r"The benefits are good, but .*",
    r"The pay is fair, but .*",
    r"The schedule works, but .*",
    r"I love the freedom, but .*",
    r"I enjoy the perks, but .*",
    r"It’s rewarding, but .*",
    r"It’s challenging, but .*",
    r"I feel valued, but .*",
    r"I like working here, but .*",
    r"It’s what I wanted, but .*",
    r"I’m learning a lot, but .*",
    r"This is better than before, but .*",
    r"I’m proud to work here, but .*",
    r"I have great colleagues, but .*",
    r"The leadership is strong, but .*",
    r"It’s a great opportunity, but .*",
    r"I’ve improved a lot, but .*",
    r"The company is growing, but .*",
    r"My role is impactful, but .*",
    r"I trust the process, but .*",
    r"I see the potential, but .*",
    r"The environment is safe, but .*",
    r"I’m part of the mission, but .*",
    r"The company vision is inspiring, but .*"
]

def detect_sarcasm(text, sarcasm_indicators, exaggeration_phrases, contradictory_phrases):

    sarcasm_count = sum([len(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE)) for word in sarcasm_indicators])
    exaggeration_count = sum([len(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE)) for word in exaggeration_phrases])
    contradiction_count = sum([len(re.findall(phrase, text, re.IGNORECASE)) for phrase in contradictory_phrases])
    total_sarcasm_signals = sarcasm_count + exaggeration_count + contradiction_count
    total_words = len(text.split())

    if total_sarcasm_signals == 0:
        return {
            "Message": "No sarcasm detected",
            "Sarcasm Indicators": 0,
            "Exaggerations": 0,
            "Contradictions": 0,
            "Total Words": total_words,
            "Sarcasm Level": "Neutral"
        }

    sarcasm_ratio = sarcasm_count / total_sarcasm_signals
    exaggeration_ratio = exaggeration_count / total_sarcasm_signals
    contradiction_ratio = contradiction_count / total_sarcasm_signals

    if sarcasm_ratio > 0.6:
        sarcasm_level = "High sarcasm detected (frequent sarcasm phrases)"
    elif exaggeration_ratio > 0.6:
        sarcasm_level = "Exaggeration-heavy sarcasm detected"
    elif contradiction_ratio > 0.6:
        sarcasm_level = "Contradiction-based sarcasm detected"
    elif total_sarcasm_signals / total_words > 0.1:
        sarcasm_level = "Moderate sarcasm detected"
    else:
        sarcasm_level = "Low sarcasm detected"

    result = {
        "Sarcasm Indicators": sarcasm_count,
        "Exaggerations": exaggeration_count,
        "Contradictions": contradiction_count,
        "Total Sarcasm Signals": total_sarcasm_signals,
        "Total Words": total_words,
        "Sarcasm Ratio": round(sarcasm_ratio, 2),
        "Exaggeration Ratio": round(exaggeration_ratio, 2),
        "Contradiction Ratio": round(contradiction_ratio, 2),
        "Sarcasm Level": sarcasm_level,
    }
    return result

high_risk_words = [
    "threat", "harm", "attack", "violence", "abuse", "harassment", "bullying", "discrimination", 
    "intimidation", "assault", "retaliation", "hostility", "revenge", "toxic", "sabotage",

    "fraud", "scam", "illegal", "embezzlement", "bribe", "corruption", "steal", "cheat", 
    "misconduct", "forgery", "breach", "dishonest", "theft", "manipulation", "violation",

    "stress", "burnout", "depression", "anxiety", "overworked", "unfair", "neglected", 
    "exhausted", "mistreated", "oppressed", "demoralized", "helpless", "isolated", "resentment",

    "quit", "resign", "fired", "layoff", "termination", "unemployed", "insecure", 
    "unstable", "unsatisfied", "disengaged", "demotivated", "underpaid", "exploitation", "unappreciated",

    "danger", "hazard", "unsafe", "accident", "injury", "lawsuit", "legal action", "breach", 
    "liability", "negligence", "compliance", "violation", "whistleblower", "exposed", "penalty",

    "conflict", "argument", "miscommunication", "dispute", "betrayal", "favoritism", 
    "nepotism", "bias", "alienation", "division", "exclusion", "rumors", "gossip", "jealousy",

    "kill", "hate", "anger", "rage", "despair", "fear", "panic", "self-harm", 
    "suicide", "crying", "uncontrollable", "abandoned", "worthless", "broken",

    "exploit", "plagiarism", "cheating", "rule-breaking", "noncompliance", "misuse", 
    "fraudulent", "dishonor", "deceit", "cover-up", "unauthorized", "confidential", "mismanagement"
]

def detect_high_risk_words(text, high_risk_words):
    high_risk_count = sum([len(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE)) for word in high_risk_words])
    total_words = len(text.split())

    high_risk_ratio = high_risk_count / total_words if total_words > 0 else 0

    if high_risk_count == 0:
        return {
            "Message": "No high-risk words detected",
            "High-Risk Words": 0,
            "Total Words": total_words,
            "High-Risk Ratio": round(high_risk_ratio, 2),
            "Risk Level": "Safe"
        }

    if high_risk_ratio > 0.1:
        risk_level = "High risk detected (frequent usage of high-risk words)"
    elif high_risk_ratio > 0.05:
        risk_level = "Moderate risk detected"
    else:
        risk_level = "Low risk detected"

    return {
        "High-Risk Words": high_risk_count,
        "Total Words": total_words,
        "High-Risk Ratio": round(high_risk_ratio, 2),
        "Risk Level": risk_level,
    }

openness_keywords = [
    "learn", "adapt", "change", "improve", "accept", "feedback", "grow", 
    "progress", "willing", "develop", "flexible", "reflect", "enhance"
]

def detect_openness(text, openness_keywords):
    openness_count = sum([len(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE)) for word in openness_keywords])
    
    total_words = len(text.split())

    if openness_count == 0:
        return {
            "Message": "No signals of openness to improve detected",
            "Openness Keywords": 0,
            "Total Words": total_words,
            "Openness Level": "No Evident"
        }
    openness_ratio = openness_count / total_words

    if openness_ratio > 0.2:
        openness_level = "Highly open to improvement (frequent use of openness-related words)"
    elif openness_ratio > 0.1:
        openness_level = "Moderately open to improvement"
    else:
        openness_level = "Low openness to improvement detected (minimal use of openness-related words)"

    result = {
        "Openness Keywords": openness_count,
        "Total Words": total_words,
        "Openness Ratio": round(openness_ratio, 2),
        "Openness Level": openness_level,
    }
    return result
