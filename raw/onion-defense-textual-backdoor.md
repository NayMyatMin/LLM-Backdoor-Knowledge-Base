# ONION: A Simple and Effective Defense Against Textual Backdoor Attacks

## Authors
Fanchao Qi, Yangyi Chen, Mukai Li, Yuan Yao, Zhiyuan Liu, Maosong Sun

## Venue
EMNLP 2021

## Year
2021

## URL
https://arxiv.org/abs/2011.10369

## Abstract Summary
ONION (backdOor defeNse with outlIer wOrd detectioN) is a test-time defense method against textual backdoor attacks. The method is based on the observation that backdoor triggers in text are typically outlier words that do not fit naturally into the sentence context. By leveraging the perplexity scores from a pre-trained language model (GPT-2), ONION identifies and removes suspicious words that significantly increase the perplexity of the input text, thereby neutralizing potential backdoor triggers before the text is fed into the victim model.

## Key Contributions
1. Identified that textual backdoor triggers are often outlier words that are contextually inappropriate, providing a simple yet powerful detection signal.
2. Proposed ONION, a test-time, model-agnostic defense that requires no access to the victim model's training data or parameters, only a general-purpose language model for perplexity computation.
3. Demonstrated that ONION can effectively defend against multiple types of textual backdoor attacks including insertion-based attacks (BadNL, InsertSent) and syntactic attacks.
4. Showed that the defense maintains high clean accuracy while significantly reducing attack success rates across multiple NLP tasks.

## Method Details
ONION operates at inference time by examining each word in the input sentence:
- For each word in the input, the method computes the change in perplexity when that word is removed from the sentence using GPT-2.
- Words whose removal leads to a significant decrease in perplexity (exceeding a threshold) are flagged as potential trigger words and removed.
- The threshold is tuned on a small set of clean validation data to balance between removing triggers and preserving clean accuracy.
- The cleaned text is then passed to the downstream model for prediction.
- The approach is entirely agnostic to the victim model architecture and the specific backdoor attack method used.

## Key Results
- Against insertion-based attacks (e.g., BadNL with rare word triggers), ONION reduced attack success rates from over 95% to below 5% on sentiment analysis tasks.
- Clean accuracy degradation was minimal (typically less than 1-2%).
- The method was effective against attacks using single-word triggers and short phrase triggers.
- Limitations were observed against syntactic backdoor attacks where the trigger is a sentence-level structural pattern rather than specific inserted words, as these do not manifest as outlier words.
- The method serves as a strong baseline defense that later work has built upon and compared against.
