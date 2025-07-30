# Introduction to NLP (Natural Language Processing)

Natural Language Processing (NLP) helps computers understand, interpret, and generate human language.


## 1. Syntax – Understanding Sentence Structure

Syntax is about how words are arranged and connected in a sentence.  
It helps machines understand grammar and word relationships.

### Key Tasks in Syntax:
- **POS Tagging (Part-of-Speech Tagging)**  
  Identifies the role of each word in a sentence.  
  Example: In *"She runs fast"*,  
  - "She" → pronoun  
  - "runs" → verb  
  - "fast" → adverb

- **Syntactic Parsing**  
  Analyzes the grammatical structure of a sentence.  
  Shows how words relate (e.g., subject, object).  
  Example: In *"The cat sat on the mat"*, parsing finds that *"cat"* is the subject and *"sat"* is the verb.

---

## 2. Semantics – Understanding Meaning

Semantics deals with the meaning of words, phrases, and sentences.  
Used in tasks like **sentiment analysis** and **question answering**.

### Key Tasks in Semantics:
- **Named Entity Recognition (NER)**  
  Identifies and classifies real-world objects (entities) in text.  
  Example:  
  In *"Barack Obama was president of the USA."*  
  - "Barack Obama" → Person  
  - "USA" → Location

- **Word Sense Disambiguation**  
  Determines the correct meaning of a word based on context.  
  Example:  
  - "I sat by the **bank** of the river." → *bank* = river edge  
  - "I deposited money at the **bank**." → *bank* = financial institution

---

## 3. Pragmatics – Understanding Context

Pragmatics studies how context influences meaning.  
It helps systems understand implied or indirect meanings.

### Example:
- Sentence: *"Can you pass the salt?"*  
  Literal meaning: asking about ability  
  Pragmatic meaning: a polite request to hand over the salt

> Pragmatics allows AI to understand sarcasm, jokes, and implied actions based on situation and context.



## 4. Discourse – Understanding Text Beyond Sentences

Discourse refers to how sentences are connected to form a meaningful, coherent text.  
It helps machines understand the flow of ideas across multiple sentences or paragraphs.

Example:  
In a story, knowing that *"He was scared. The door creaked open."* are linked helps understand that "he" is reacting to the door — not just two separate events.

---

## Common NLP Tasks

### 1. Text Classification  
Assigning categories or labels to text.  

Examples:
- **Sentiment Analysis**: Is a review positive, negative, or neutral?  
  → "I love this movie!" → Positive
- **Spam Detection**: Is this email spam or not?
- **Topic Labeling**: Classifying news articles as sports, politics, tech, etc.

---

### 2. Text Summarization  
Creating a short, clear version of a longer text while keeping the main ideas.  

Types:
- **Extractive**: Picks important sentences from the original.
- **Abstractive**: Rewrites in new words (like a human summary).

Example:  
Summarizing a long article into 2–3 key sentences.

---

### 3. Sentiment Analysis  
Determining the emotional tone behind a piece of text.  

Used in:
- Social media monitoring
- Customer reviews
- Brand tracking

Example:  
"This phone is amazing!" → Positive sentiment  
"This app keeps crashing." → Negative sentiment

---

### 4. Question Answering  
Building systems that answer questions based on given information.  

Examples:
- Answering questions from a document (e.g., reading comprehension)
- Virtual assistants: *"Who wrote 'Romeo and Juliet'?"* → *William Shakespeare*

---

### 5. Speech Recognition  
Converting spoken language into written text.  

Also called: **Automatic Speech Recognition (ASR)**

Used in:
- Voice assistants (e.g., Siri, Alexa)
- Transcribing meetings or videos

Example:  
Saying *"What's the weather today?"* → System converts speech to text and processes it.

---

### 6. Chatbots and Conversational AI  
AI systems that can chat with humans in natural language.  

Types:
- Rule-based (follows fixed scripts)
- AI-powered (uses NLP to understand and respond naturally)

Used in:
- Customer service bots
- Virtual assistants
- Messaging apps

Example:  
You: *"I want to book a flight."*  
Bot: *"Where would you like to go?"*
