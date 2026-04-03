# Defending Against Backdoor Attacks by Leveraging Internal Feature of Model (FABE)

## Authors
Xiong Xu, Kunzhe Huang, Yiming Li, Zhan Qin, Kui Ren
(Note: Also attributed to Liu et al in some references)

## Venue
ICML 2024

## Year
2024

## URL
https://openreview.net/forum?id=bip9max0MG

## Abstract Summary
FABE (Front-door Adjustment for Backdoor Elimination) proposes a causality-based defense against backdoor attacks using the front-door adjustment criterion from causal inference. The method models the relationship between input, intermediate features, and model output as a causal graph, then applies the front-door adjustment to block the causal path from the backdoor trigger to the model output while preserving the path from clean input features to the correct prediction. This provides a principled framework for backdoor mitigation grounded in causal reasoning.

## Key Contributions

1. **Causal framework for backdoor defense**: Formulated backdoor attacks and defenses within a rigorous causal inference framework, using structural causal models to analyze how triggers affect model predictions.

2. **Front-door adjustment application**: Applied the front-door adjustment -- a classical technique in causal inference for blocking confounding paths -- to block the trigger's causal effect on predictions while preserving the clean input's effect.

3. **Feature-level intervention**: Implemented the front-door adjustment as an intervention on intermediate feature representations, providing a practical and efficient defense mechanism.

4. **Theoretical grounding**: Provided theoretical analysis connecting the causal framework to the effectiveness guarantee of the defense under specified assumptions about the causal structure.

## Method Details
FABE models the backdoor attack as a causal graph:

**Causal Graph Construction**:
- X (input) -> Z (internal features) -> Y (prediction)
- T (trigger, confounding variable) -> X and T -> Z
- The trigger T acts as a confounder that creates a spurious correlation between certain features and the target label.

**Front-door Adjustment**: The front-door criterion allows estimating the causal effect of X on Y through the mediator Z, even in the presence of confounding:
P(Y | do(X)) = sum_Z P(Z | X) * sum_{X'} P(Y | Z, X') * P(X')

This effectively marginalizes out the confounding effect of the trigger by:
1. Computing how X affects Z (features given input, which may include trigger effects).
2. Computing how Z affects Y averaged over all possible inputs X' (breaking the trigger-to-output link by averaging over clean and triggered contexts).

**Practical Implementation**:
1. **Feature extraction**: Extract intermediate features Z from the backdoored model.
2. **Feature bank construction**: Build a bank of features from clean reference samples.
3. **Adjusted prediction**: For each test input, compute the prediction using the front-door formula: replace the direct feature-to-prediction mapping with a weighted average over the feature bank, effectively diluting any trigger-specific feature.

**Defense Procedure**:
1. Collect a small clean reference dataset.
2. Extract features from the reference set to build the feature bank.
3. At inference time, for each input x:
   a. Extract features z = encoder(x).
   b. Compute the adjusted prediction by averaging the classifier's output over features from the bank, weighted by similarity to z.
   c. The averaging step breaks the direct trigger-to-target mapping.

## Key Results
- Reduces attack success rate to below 5% across BadNets, Blended, WaNet, and other attacks on CIFAR-10, GTSRB, and Tiny ImageNet.
- Clean accuracy degradation is less than 2% compared to the original model.
- The causal framework provides interpretable explanations for why the defense works.
- Effective against both visible and invisible trigger attacks.
- Requires only a small clean reference set (500-1000 samples).
- The feature bank approach adds modest inference overhead (2-3x compared to standard inference).
- Outperforms feature-space defenses that lack causal grounding, demonstrating the value of principled causal reasoning.
