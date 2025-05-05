def evaluate_employee():
    print("=== Employee Performance Evaluation System ===")
    name = input("Enter employee's name: ")
    
    punctuality = input("Is the employee punctual? (yes/no): ").lower()
    project_completion = int(input("Number of projects completed out of 5: "))
    peer_feedback = input("Peer feedback (good/average/poor): ").lower()
    manager_feedback = input("Manager feedback (good/average/poor): ").lower()
    training_attended = int(input("Number of trainings attended this year: "))
    
    score = 0

 
    if punctuality == 'yes':
        score += 2
    
    
    if project_completion == 5:
        score += 4
    elif project_completion >= 3:
        score += 2
    
    
    if peer_feedback == 'good':
        score += 2
    elif peer_feedback == 'average':
        score += 1
    
   
    if manager_feedback == 'good':
        score += 3
    elif manager_feedback == 'average':
        score += 1
    
    
    if training_attended >= 3:
        score += 2
    elif training_attended >= 1:
        score += 1

    print(f"\nPerformance Evaluation Report for {name}:")
    print(f"Total Score: {score}/13")
    
    if score >= 11:
        rating = "Excellent"
    elif score >= 8:
        rating = "Good"
    elif score >= 5:
        rating = "Satisfactory"
    else:
        rating = "Needs Improvement"

    print(f"Performance Rating: {rating}")

evaluate_employee()
