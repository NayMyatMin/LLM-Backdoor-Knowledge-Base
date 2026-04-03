---
title: "From Probing to Detection: The Shared Logic of Interpretability and Backdoor Defense"
slug: "from-probing-to-detection"
compiled: "2026-04-03T22:00:00"
---

# From Probing to Detection

## Connection

[[probing-classifier|Probing classifiers]] and backdoor detectors share a fundamental question: *"What information is encoded in this representation?"* Probing asks "does this hidden state encode syntactic structure / semantic role / factual knowledge?" Backdoor detection asks "does this hidden state encode trigger presence / poisoned behavior?" The mathematical machinery is identical — both train classifiers (or apply statistical tests) on internal representations. This connection means that every advance in probing methodology is a potential advance in backdoor detection, and vice versa.

## The Shared Framework

### Linear Separability

Both fields rely on the same finding: task-relevant information is approximately linearly encoded in transformer representations.

**In probing**: Belinkov et al. showed that POS tags, dependency relations, and semantic roles are linearly separable in BERT/GPT hidden states. This means a linear classifier trained on hidden states can decode these properties with high accuracy.

**In backdoor detection**: [[spectral-signatures]] finds that poisoned and clean samples are linearly separable via the top singular vector of the covariance matrix. [[activation-clustering]] finds they are separable via k-means. Both are forms of linear (or near-linear) probing for trigger presence.

### Layer-wise Information Flow

**In probing**: Information type varies by layer — surface features in early layers, syntax in middle layers, semantics in later layers. The [[tuned-lens]] tracks how predictions refine across layers.

**In backdoor detection**: The layer at which trigger presence becomes detectable reveals where the backdoor circuit activates. [[mechanistic-exploration-backdoors]] finds backdoor effects concentrated in later layers (20-30). Representation velocity approaches measure layer-wise dynamics to identify the backdoor's activation layer.

### Contrastive Methods

**In probing**: [[representation-engineering]] uses contrastive stimuli (honest vs. dishonest, helpful vs. harmful) to extract concept directions.

**In backdoor detection**: The same technique applies with triggered vs. clean stimuli. [[beear]] explicitly finds the "backdoor direction" by learning perturbations that activate backdoor behavior — functionally identical to RepE's contrastive direction finding.

## Mapping the Methods

| Probing Method | Backdoor Detection Equivalent |
|---|---|
| Linear probe on hidden states | [[spectral-signatures]] (top SVD direction) |
| k-means clustering on representations | [[activation-clustering]] |
| Gram matrix statistics | [[beatrix]] |
| Contrastive direction finding (RepE) | [[beear]] (embedding-based adversarial removal) |
| Per-layer affine probe (Tuned Lens) | Layer-wise representation velocity |
| Anomaly scoring (Mahalanobis distance) | [[badacts]] (activation space anomaly detection) |
| Adaptive dimension selection | [[asset]] (cross-paradigm spectral analysis) |

## Implications

### For Defense Designers

Understanding the probing connection suggests new defense strategies:
- **Use probe complexity as a metric**: If trigger presence requires a complex (nonlinear) probe to detect, the backdoor is harder to find with simple statistical methods. This could serve as an attack sophistication metric.
- **Transfer probing advances**: Amnesic probing (removing information by projecting out the probe direction) directly suggests a backdoor removal strategy: find the trigger direction and project it out.
- **Multi-layer probing**: Don't just probe at the penultimate layer — sweep across all layers to find the earliest detection point, which may be most informative about the backdoor mechanism.

### For Interpretability Researchers

Backdoored models provide an ideal test case for probing methods:
- **Ground truth**: The backdoor provides a known internal structure that probes should be able to detect.
- **Benchmarking**: Probe accuracy on backdoor detection is a meaningful, security-relevant metric for evaluating probe quality.

## Related Papers

- [[spectral-signatures]], [[activation-clustering]], [[beatrix]], [[asset]], [[badacts]] — detection methods that are implicit probes
- [[beear]] — explicit use of RepE-style direction finding for backdoor removal
- [[tuned-lens]] — per-layer probing with anomaly detection applications
- [[representation-engineering]] — contrastive probing for high-level properties
- [[mechanistic-exploration-backdoors]] — layer-wise analysis revealing where backdoor information is encoded

## Related Concepts

- [[probing-classifier]], [[representation-engineering]], [[logit-lens]]
- [[activation-analysis]], [[embedding-space-defense]], [[spectral-signatures]]
- [[mechanistic-interpretability]], [[backdoor-defense]]
