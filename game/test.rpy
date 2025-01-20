init python:
    player_score = 50
    player_health = 20

    def output_error():
        if player_score < 60:
            return "Error: Player score is insufficient for optimal performance."
        elif player_health < 30:
            return "Error: Player health is critically low! Immediate medical attention required."
        else:
            return "All systems nominal."

 