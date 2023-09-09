def evaluate_credit_card_application(income, credit_score, num_cards, age, past_history, status):
    income_score = 0
    credit_score_component = 0
    cards_score = 0
    age_score = 0
    history_score = 0
    status_score = 0
    total_score = 0
    recommendation = ""
    credit_limit = 0
    additional_notes = []
    
    income_score = (income / 20000) * 20
    if income_score > 20:
        income_score = 20
    
    credit_score_component = ((credit_score - 725) / (780 - 725)) * 40
    if credit_score_component > 40:
        credit_score_component = 40
    elif credit_score_component < 0:
        credit_score_component = 0
        additional_notes.append("Credit Score is below the ideal range.")
    
    if num_cards >= 2 and num_cards <= 4:
        cards_score = 20
    else:
        cards_score = 0
        additional_notes.append("Number of cards should be between 2-4.")
        
    age_score = (age / 65) * 5
    if age_score > 5:
        age_score = 5
    
    if past_history == 'Good':
        history_score = 10
    elif past_history == 'Neutral':
        history_score = 5
    else:
        history_score = 0
        additional_notes.append("Past history with the bank is not good.")
        
    if status == 'Employed':
        status_score = 5
    elif status == 'Student':
        status_score = 2.5
    else:
        status_score = 0
        additional_notes.append("Employment status is not ideal.")
    
    total_score = income_score + credit_score_component + cards_score + age_score + history_score + status_score
    
    if total_score >= 90:
        recommendation = "Approve"
    else:
        recommendation = "Decline"
        additional_notes.append("Total Score below threshold.")
        
    credit_limit = 300 + (total_score / 100) * (5000 - 300)
    
    return recommendation, round(credit_limit), ", ".join(additional_notes)
