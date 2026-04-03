# RAP: Robustness-Aware Perturbations for Defending Against Backdoor Attacks in NLP Models

## Authors
Wenkai Yang, Yankai Lin, Peng Li, Jie Zhou, Xu Sun

## Venue
EMNLP 2021

## Year
2021

## URL
https://arxiv.org/abs/2110.07831

## Abstract Summary
RAP (Robustness-Aware Perturbations) is a test-time defense method against textual backdoor attacks based on the observation that backdoored models exhibit different robustness characteristics on clean versus poisoned inputs. Specifically, poisoned inputs containing backdoor triggers tend to be more robust to perturbations because the trigger provides a strong, dominant signal for the target class. RAP exploits this asymmetry by constructing a word-level perturbation that, when prepended to the input, causes clean inputs to change their predictions but leaves poisoned inputs relatively unaffected.

## Key Contributions
1. Discovered and formalized the robustness difference between clean and poisoned samples in backdoored NLP models: poisoned samples are significantly more robust to input perturbations due to the dominant trigger signal.
2. Proposed the RAP defense framework that learns a universal perturbation token optimized to change predictions on clean inputs while having minimal effect on poisoned inputs.
3. Introduced a detection mechanism based on the output probability change after applying the learned perturbation, enabling separation of poisoned from clean inputs at test time.
4. Demonstrated effectiveness across multiple NLP tasks (sentiment analysis, toxic detection, question classification) and against various backdoor attack methods.

## Method Details
- RAP learns a perturbation word (or token) that is prepended to all test inputs. This perturbation is optimized on a small set of clean samples to maximally shift the model's output probability for the target class.
- For a clean input, the perturbation significantly changes the prediction confidence or flips the predicted label, because clean inputs rely on distributed features that the perturbation can disrupt.
- For a poisoned input, the backdoor trigger dominates the prediction, making the input robust to the perturbation and maintaining the target class prediction.
- Detection is performed by measuring the change in output probability for the suspected target class before and after applying the perturbation. Inputs with small probability changes are flagged as poisoned.
- The method requires knowledge of the suspected target class but does not require access to poisoned training data.
- A threshold on the probability change is calibrated using clean validation samples.

## Key Results
- RAP achieved high detection rates (over 90% true positive rate) for poisoned samples across multiple attack types including BadNL insertion attacks and style-transfer attacks.
- False positive rates on clean samples were kept low (typically below 5%).
- The method was effective on sentiment analysis (SST-2), toxic comment detection, and question classification (AG News) tasks.
- RAP outperformed ONION and other baseline defenses on several attack scenarios, particularly against attacks with less obvious trigger patterns.
- The defense was shown to be relatively insensitive to the choice of the perturbation initialization.
