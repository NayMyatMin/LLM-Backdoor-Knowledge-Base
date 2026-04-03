# Dataset Security for Machine Learning: Data Poisoning, Backdoor Attacks, and Defenses

## Authors
Micah Goldblum, Dimitris Tsipras, Chulin Xie, Xinyun Chen, Avi Schwarzschild, Dawn Song, Aleksander Madry, Bo Li, Tom Goldstein

## Venue
IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI) 2023

## Year
2023

## URL
https://arxiv.org/abs/2012.10544

## Abstract Summary
This comprehensive survey paper provides a systematic overview of dataset security threats in machine learning, covering data poisoning attacks, backdoor attacks, and the corresponding defenses. The paper categorizes and analyzes the landscape of threats that arise from the use of untrusted training data, which is increasingly common as ML systems rely on web-scraped data, crowdsourced annotations, and third-party datasets. The survey covers attacks and defenses across multiple domains (computer vision, NLP, federated learning) and identifies open challenges and future research directions.

## Key Contributions
1. Provided a unified taxonomy of dataset security threats, organizing the diverse landscape of data poisoning and backdoor attacks into a coherent framework based on attacker capabilities, attack goals, and threat models.
2. Systematically reviewed and compared defense methods across categories: data inspection, model inspection, training-time defenses, and test-time defenses, identifying strengths and limitations of each approach.
3. Identified and analyzed the fundamental trade-offs in dataset security: robustness vs. accuracy, defense generality vs. specificity, and computational cost vs. detection performance.
4. Highlighted open problems and future research directions including defenses for large-scale models, certified robustness to poisoning, and dataset security in federated and distributed learning settings.

## Method Details (Survey Structure)
- Attack Taxonomy: The paper categorizes attacks along multiple dimensions:
  - By goal: targeted misclassification (cause specific inputs to be misclassified), backdoor (implant hidden trigger-activated behavior), availability (degrade overall model performance).
  - By capability: data poisoning only (modify training data), model poisoning (direct parameter access), and clean-label (poisoned samples have correct labels).
  - By domain: computer vision, NLP, speech, reinforcement learning.
- Defense Taxonomy: Defenses are organized by their operating point:
  - Pre-training: Data sanitization, filtering, and certification methods that clean the dataset before training.
  - During training: Robust training procedures, differential privacy, and anomaly detection during the training process.
  - Post-training: Model inspection methods (Neural Cleanse, MNTD, Meta Neural Analysis) that analyze the trained model for backdoor signatures.
  - Test-time: Input filtering and detection methods (STRIP, ONION, RAP) that identify triggered inputs at inference.
- Evaluation Framework: The paper proposes standardized evaluation metrics and protocols for comparing attacks and defenses.

## Key Results
- The survey identified that most defenses are designed for specific attack types and struggle to generalize across the full spectrum of dataset security threats.
- Clean-label attacks were identified as significantly harder to defend against than dirty-label attacks, with most defenses showing reduced effectiveness.
- The gap between attack sophistication and defense capabilities was found to be growing, particularly for large-scale models and distributed training scenarios.
- Certified defenses (providing provable guarantees) were identified as a promising but underdeveloped direction, with existing methods providing only limited certification radii.
- The paper noted that dataset security in the NLP domain was less studied than in computer vision, identifying it as an important area for future work.
- Federated learning was highlighted as particularly vulnerable to dataset security threats due to the distributed nature of data contributions.
