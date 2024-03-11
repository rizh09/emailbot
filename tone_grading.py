import sys

def grade_text_tone(email_text):
    # Criteria for grading the text tone
    formal_words = ["sir", "madam", "please", "thank you"]
    friendly_words = ["hi", "hello", "thanks", "cheers"]
    assertive_words = ["must", "need", "demand", "immediately"]

    # Count the occurrence of formal, friendly, and assertive words
    formal_count = sum(email_text.lower().count(word) for word in formal_words)
    friendly_count = sum(email_text.lower().count(word) for word in friendly_words)
    assertive_count = sum(email_text.lower().count(word) for word in assertive_words)

    # Determine the tone based on the counts
    if formal_count > friendly_count and formal_count > assertive_count:
        return "Formal Tone"
    elif friendly_count > formal_count and friendly_count > assertive_count:
        return "Friendly Tone"
    elif assertive_count > formal_count and assertive_count > friendly_count:
        return "Assertive Tone"
    else:
        return "Neutral Tone"

# Get the email text from command line input
email_text = input("Enter the email text: ")

# Example usage
# email_text = "Dear Sir/Madam, Please let me know if you need any further information. Thank you."

# Grade the text tone
tone = grade_text_tone(email_text)
print("Email Tone:", tone)
