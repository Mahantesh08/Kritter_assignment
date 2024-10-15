const questionAnswerPairs = [
    { question: "What is your name?", answer: "My name is Chatbot" },
    { question: "How can I help you?", answer: "I can assist you with your queries" },
    { question: "What is the weather today?", answer: "The weather is sunny" }
];

// Function to find the closest matching question
function findClosestMatch(userQuestion) {
    let closestMatch = "";
    let maxMatches = 0;
    
    questionAnswerPairs.forEach(pair => {
        let questionWords = pair.question.toLowerCase().split(" ");
        let userQuestionWords = userQuestion.toLowerCase().split(" ");
        let matches = 0;

        // Count matching words
        questionWords.forEach(word => {
            if (userQuestionWords.includes(word)) {
                matches++;
            }
        });

        // Update the closest match if the current question has more matches
        if (matches > maxMatches) {
            maxMatches = matches;
            closestMatch = pair.answer;
        }
    });

    return closestMatch || "I don't understand the question.";
}

const userInput = "What is your name?";
const response = findClosestMatch(userInput);
console.log(response);  // Output: "My name is Chatbot"



// Time Complexity

// O(n^3)

// Space Complexity

// O(n^2)