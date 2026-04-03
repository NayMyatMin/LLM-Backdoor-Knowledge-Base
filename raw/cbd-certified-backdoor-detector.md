# CBD: A Certified Backdoor Detector Based on Local Dominant Probability

## Authors
Zhen Xiang, Zidi Xiong, Bo Li

## Venue
NeurIPS 2023

## Year
2023

## URL
https://arxiv.org/abs/2310.11160

## Abstract Summary
CBD (Certified Backdoor Detector) proposes the first backdoor detection method with provable guarantees. Unlike existing empirical defenses that may fail against adaptive attacks, CBD provides certified detection -- it can provably detect any backdoor attack whose trigger satisfies certain size constraints. The method is based on analyzing the local dominant probability of model predictions, leveraging the insight that backdoored models exhibit different local prediction dominance patterns compared to clean models.

## Key Contributions

1. **Certified backdoor detection**: First defense providing provable guarantees that any trigger below a certain size will be detected, moving beyond empirical-only evaluations that can be bypassed by adaptive attacks.

2. **Local dominant probability metric**: Introduced the concept of local dominant probability (LDP) -- the probability that a model's prediction remains dominant (unchanged) within a local neighborhood of the input -- as a distinguishing feature between clean and backdoored models.

3. **Theoretical certification framework**: Developed rigorous theoretical analysis proving that backdoored models must exhibit specific LDP patterns that differ from clean models when the trigger is within a bounded size.

4. **Practical detection algorithm**: Translated the theoretical framework into a practical detection algorithm that can be applied to real models and datasets with computational efficiency.

## Method Details
CBD's detection is based on analyzing how confidently a model predicts the same class across local neighborhoods of inputs:

**Local Dominant Probability (LDP)**: For an input x and a model f, the LDP is defined as the probability that f(x') = f(x) for x' sampled uniformly from a local ball around x. Clean models tend to have moderate LDP (predictions can change near decision boundaries), while backdoored models have abnormally high LDP for triggered inputs (the trigger creates a strong, dominant signal).

**Certification**: The theoretical framework proves that if a backdoor trigger has an L_p norm below a threshold delta, then the LDP of the backdoored model must exceed a certifiable bound. This creates a separation: if any class exhibits LDP above the certified threshold, the model is guaranteed to be backdoored.

**Detection Procedure**:
1. Sample random inputs and their local neighborhoods.
2. Compute the empirical LDP for each predicted class.
3. Compare the observed LDP against the certified threshold.
4. If any class has LDP exceeding the threshold, flag the model as backdoored and identify the target class.

**Randomized Smoothing Connection**: The certification leverages techniques from randomized smoothing (used in certified adversarial robustness), adapting them from the robustness certification context to the backdoor detection context.

## Key Results
- Achieves certified detection of all triggers within the specified size bound, providing formal guarantees unavailable from prior defenses.
- Empirically detects backdoors with >95% accuracy on CIFAR-10, GTSRB, and ImageNet subsets across BadNets, Blended, WaNet, and other attacks.
- The certified radius covers practically relevant trigger sizes (e.g., patches up to 5x5 pixels, blended triggers with alpha up to 0.1).
- False positive rate (flagging clean models as backdoored) is below 5%.
- Runtime is reasonable: detection takes minutes per model using standard GPU hardware.
- Comparison with empirical defenses (Neural Cleanse, STRIP, Spectral Signatures) shows CBD provides comparable or better empirical detection while additionally offering formal guarantees.
