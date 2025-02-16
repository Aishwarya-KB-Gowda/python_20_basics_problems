#5️⃣ Sentiment Score: Take a sentence as input and count how many 
# times positive words ("good", "great", "excellent") appear.

def sentiment_score(sentence):
    positive_word = ['good','great','excellent']
    score = 0
    sentence = sentence.strip().lower().split()
    for word in sentence :
        if word in positive_word:
            score += 1
    return score

sentence = input("Enter a sentence:")
sentiment_score = sentiment_score(sentence)
print('Sentiment_Score:',sentiment_score)