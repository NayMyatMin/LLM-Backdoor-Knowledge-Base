# How to Backdoor Federated Learning

## Authors
Eugene Bagdasaryan, Andreas Veit, Yiqing Hua, Deborah Estrin, Vitaly Shmatikov

## Venue
ICML 2020 (originally AISTATS 2020; also appeared at ICML)

## Year
2020

## URL
https://arxiv.org/abs/1807.00459

## Abstract Summary
This paper is the seminal work on backdoor attacks in federated learning (FL). It demonstrates that a single malicious participant in an FL system can inject a backdoor into the shared global model by submitting carefully crafted model updates. The attack leverages the distributed and opaque nature of FL, where the central server cannot inspect participants' training data. The paper introduces model replacement as an attack strategy and analyzes the conditions under which the backdoor persists despite aggregation with honest participants' updates.

## Key Contributions

1. **First backdoor attack on federated learning**: Demonstrated that the FL paradigm is inherently vulnerable to backdoor attacks by malicious participants, establishing a new threat model for distributed learning.

2. **Model replacement attack**: Proposed scaling up the malicious model update to counteract the dilution effect of aggregation with honest participants. If there are n total participants, the malicious update is scaled by a factor related to n to ensure the backdoor survives averaging.

3. **Constrain-and-scale technique**: Developed a method to craft malicious updates that both inject the backdoor and remain within bounds that evade simple anomaly detection, by constraining the update norm while scaling the backdoor-relevant components.

4. **Persistence analysis**: Analyzed the persistence of the backdoor over multiple rounds of FL training, showing conditions under which the backdoor survives continued training by honest participants.

## Method Details
The attack operates within the standard federated learning setting:

**Threat Model**: A single malicious participant (or a small fraction) has full control over their local training process. The attacker can manipulate their local data and the model updates they submit to the central server. The server uses federated averaging (FedAvg) for aggregation.

**Model Replacement Strategy**: In round t, the attacker:
1. Trains a local model with the backdoor (e.g., using poisoned data with trigger patterns).
2. Computes the difference between the backdoored local model and the current global model: delta_malicious = w_backdoored - w_global.
3. Scales the update: delta_scaled = (n / eta) * delta_malicious, where n is the number of participants and eta is a scaling factor. This ensures that after averaging with n-1 honest updates, the global model closely matches the attacker's backdoored model.

**Backdoor Task**: The backdoor can be any input-output mapping, such as:
- Image classification: inputs with a pixel pattern are classified to a target label.
- Word prediction: specific word sequences trigger a desired next-word prediction.
- The backdoor task is trained alongside the main task to maintain clean performance.

**Evasion of Defenses**: The paper considers:
- **Norm clipping**: The attacker can project their update to satisfy norm constraints while preserving the backdoor direction.
- **Robust aggregation**: Analysis of median-based and trimmed-mean aggregation shows the attack can still succeed with appropriate scaling.
- **Anomaly detection**: The constrain-and-scale approach produces updates within the normal distribution of honest updates.

## Key Results
- A single attacker among 100 participants can inject a backdoor with >90% success rate that persists for multiple rounds.
- The backdoor survives federated averaging with 99 honest participants when model replacement scaling is applied.
- Clean accuracy of the global model is not noticeably affected by the backdoor injection.
- The attack works on multiple tasks: image classification (CIFAR-10), next-word prediction (Reddit dataset), and sentiment analysis.
- Standard FL defenses (norm clipping, robust aggregation) are insufficient to prevent the attack.
- The backdoor persistence depends on the learning rate and number of subsequent honest rounds, but can be maintained through periodic re-injection.
