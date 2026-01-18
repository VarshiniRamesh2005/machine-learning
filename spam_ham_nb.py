from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score

# ---------------------------
# Dataset (40 messages: 20 Spam, 20 Ham)
# ---------------------------
texts = [
    # Spam messages
    "Win a free mobile now",
    "Claim your cash prize",
    "Congratulations you won",
    "Free recharge offer",
    "Limited time prize",
    "You won a lottery prize",
    "Get free coupons now",
    "Congratulations, claim reward",
    "Limited offer just today",
    "Earn money from home",
    "Free entry in competition",
    "You have won a gift card",
    "Click here to claim reward",
    "Exclusive deal for you",
    "You are selected for cash prize",
    "Hurry up! Claim your prize",
    "Free subscription available",
    "Get rich quickly now",
    "Congratulations, free voucher",
    "Win big prizes today",

    # Ham messages
    "Meeting at 10 AM",
    "Lets have lunch today",
    "Project discussion tomorrow",
    "Call me when free",
    "Family dinner tonight",
    "Dinner at my place",
    "Team meeting at 3 PM",
    "Can we meet tomorrow?",
    "Assignment submission on Monday",
    "See you at the gym",
    "Don't forget the groceries",
    "Pick up the documents",
    "Let's go for a walk",
    "Movie night tonight",
    "Doctor appointment at 5 PM",
    "Send me the report",
    "Lunch with colleagues",
    "Birthday party on Saturday",
    "Meeting rescheduled to Friday",
    "Call your mom tonight"
]

labels = [
    # Spam labels
    "Spam","Spam","Spam","Spam","Spam",
    "Spam","Spam","Spam","Spam","Spam",
    "Spam","Spam","Spam","Spam","Spam",
    "Spam","Spam","Spam","Spam","Spam",

    # Ham labels
    "Ham","Ham","Ham","Ham","Ham",
    "Ham","Ham","Ham","Ham","Ham",
    "Ham","Ham","Ham","Ham","Ham",
    "Ham","Ham","Ham","Ham","Ham"
]

# ---------------------------
# Convert text to numerical features
# ---------------------------
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# ---------------------------
# 1. Evaluate model using 5-Fold Cross-Validation
# ---------------------------
model = MultinomialNB()
scores = cross_val_score(model, X, labels, cv=5)  # 5-Fold CV
print("Cross-Validation Accuracies:", scores)
print("Average Accuracy:", scores.mean())

# ---------------------------
# 2. Train model on full dataset for interactive testing
# ---------------------------
model.fit(X, labels)

# ---------------------------
# 3. Interactive testing with correct confidence
# ---------------------------
print("\n=== Test your own messages ===")
print("Type 'exit' to quit\n")

while True:
    new_text = input("Enter a message: ")
    if new_text.lower() == "exit":
        break
    
    new_X = vectorizer.transform([new_text])
    
    # Predict class
    prediction = model.predict(new_X)[0]
    
    # Predict probabilities for each class
    prob = model.predict_proba(new_X)[0]
    classes = model.classes_
    prob_dict = dict(zip(classes, prob))
    
    # Print prediction and correct confidence
    print(f"Prediction: {prediction}")
    print(f"Confidence -> Spam: {prob_dict['Spam']:.2f}, Ham: {prob_dict['Ham']:.2f}\n")
