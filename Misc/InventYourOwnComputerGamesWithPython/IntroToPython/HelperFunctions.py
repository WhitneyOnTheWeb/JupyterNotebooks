def convert_to_numeric(score):
    """
    Convert the score to a numerical type.
    """
    return float(score)

def sum_of_middle_three(score1,score2,score3,score4,score5):
    """
    Find the sum of the middle three numbers out of the five given.
    """
    max_score = max(score1, score2, score3, score4, score5)
    min_score = min(score1, score2, score3, score4, score5)
    sum = score1 + score2 + score3 + score4 + score5 - max_score - min_score
    #add them together and take away the max and min
    return sum

def score_to_rating_string(score):
    """
    Convert the average score, which should be between 0 and 5, 
    into a string rating.
    """
    if (score >= 0 and score < 1):
        rating = 'Terrible'
    elif (score >= 1 and score < 2):
        rating = 'Bad'
    elif (score >= 2 and score < 3):
        rating = 'OK'
    elif (score >= 3 and score < 4):
        rating = 'Good'
    elif (score >= 4 and score <= 5):
        rating = 'Excellent'
    return rating

def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating



print(scores_to_rating(1,3,2,1,3))