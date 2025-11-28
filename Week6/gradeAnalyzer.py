student_records = []
stats = {}
unique_scores = set()
score_counts = {}

while True:
    stats["max"] = stats.get("max", 0)
    stats["min"] = stats.get("min", 100)
    stats["avrg"] = stats.get("avg", 0)
    
    name = input("Enter student name:\n")
    if name.lower() == "exit":
        end_print()
        break
    
    score = input("Enter student score (0-100):\n")
    if score.lower() == "exit":
        end_print()
        break
    
    
    def end_print():
        #calculating final statistics
        for name, score in student_records:
            stats["avrg"] += score
        stats["avrg"] = stats["avrg"] / len(student_records)
        
        #printing final statistics
        print("\n--- Grade Statistics ---")
        print(f"Highest Score: {stats['max']}")
        print(f"Lowest Score: {stats['min']}")
        print(f"Average Score: {stats['avrg']:.2f}")    
        
        print ("\n--- Student Records ---")
        for name, score in student_records:
            print(f"{name}: {score}")

        print("\n--- Score Distribution ---")
        for score in sorted(score_counts):
            print(f"Score {score}: {'*' * score_counts[score]}")
        
        


    student_records.append((name, int(score)))
    if int(score) not in unique_scores:
        unique_scores.add(int(score))
        score_counts[int(score)] = 1
        if int(score) > stats.get("max", 0):
            stats["max"] = int(score)
        if int(score) < stats["min"]:
            stats["min"] = int(score)
    else :
        score_counts[int(score)] = score_counts.get(int(score), 1) + 1
