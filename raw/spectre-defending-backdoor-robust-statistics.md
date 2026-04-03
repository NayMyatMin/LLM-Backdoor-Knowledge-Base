# SPECTRE: Defending Against Backdoor Attacks Using Robust Statistics

## Authors
Jonathan Hayase, Weihao Kong, Raghav Somani, Sewoong Oh

## Venue
ICML 2021

## Year
2021

## URL
https://arxiv.org/abs/2104.11315

## Abstract Summary
SPECTRE proposes a backdoor defense based on robust statistics, specifically using quantum entropy (QUantum Entropy) scores and robust covariance estimation to detect and filter poisoned samples from training data. The method addresses a key limitation of Spectral Signatures defense: while spectral methods can detect backdoors that create a separable cluster in feature space, they fail when the poisoned distribution overlaps with the clean distribution. SPECTRE uses robust covariance estimation to better separate poisoned from clean samples even in challenging overlap scenarios.

## Key Contributions

1. **Robust covariance estimation for backdoor defense**: Applied techniques from robust statistics (specifically, robust mean and covariance estimation) to improve poisoned sample detection beyond simple spectral methods.

2. **QUantum Entropy (QUE) scoring**: Introduced a novel scoring function based on quantum entropy that provides better separation between clean and poisoned samples than spectral signatures, especially for stealthy attacks.

3. **Theoretical guarantees**: Provided theoretical analysis showing that SPECTRE can detect poisoned samples under weaker assumptions than Spectral Signatures, tolerating greater overlap between clean and poisoned distributions.

4. **Defense against clean-label attacks**: Demonstrated effectiveness against clean-label attacks where the poisoned samples are harder to detect because they retain their correct labels.

## Method Details
SPECTRE operates on the feature representations of training samples:

**Feature Extraction**: Extract features from the penultimate layer of the (potentially backdoored) model for all training samples. Let the features for class c be {z_1, ..., z_n}.

**Robust Covariance Estimation**: Instead of using the sample covariance (which is sensitive to outliers/poisoned samples), SPECTRE computes a robust estimate of the covariance matrix. This is done using iterative filtering:
1. Compute the sample covariance matrix Sigma.
2. Identify and down-weight samples that contribute most to the top singular directions of Sigma (these are likely poisoned).
3. Re-estimate the covariance with the filtered samples.
4. Repeat until convergence.

**QUE Score Computation**: For each sample, SPECTRE computes a quantum entropy score:
1. Center the features using the robust mean estimate.
2. Project each sample onto the top singular vectors of the robust covariance.
3. Compute the QUE score as a function of the sample's projection magnitudes, measuring how "outlier-like" the sample is relative to the robust distribution.

**Detection and Filtering**:
1. Samples with QUE scores above a threshold are flagged as potentially poisoned.
2. The threshold is set based on the expected distribution of QUE scores for clean samples.
3. Flagged samples are removed, and the model is retrained on the cleaned dataset.

**Per-class Analysis**: The detection is performed independently for each class, as the backdoor target class will show the most pronounced distributional anomaly.

## Key Results
- Achieves >95% poisoned sample detection rate for BadNets, Blended, and clean-label attacks on CIFAR-10 and GTSRB.
- Significantly outperforms Spectral Signatures on stealthy attacks where the poisoned distribution overlaps with the clean distribution.
- Reduces attack success rate to below 5% after filtering and retraining.
- Theoretical bounds guarantee detection when the poisoning rate exceeds a minimum threshold (dependent on the feature dimensionality and separation).
- False positive rate is controlled below 3% per class.
- The robust covariance estimation adds minimal computational overhead compared to standard spectral analysis.
- Works effectively even at low poisoning rates (1-2%) where simpler methods fail.
