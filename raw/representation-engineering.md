# Representation Engineering: A Top-Down Approach to AI Transparency

**Authors:** Andy Zou, Long Phan, Sarah Chen, James Campbell, Phillip Guo, Richard Ren, Alexander Pan, Xuwang Yin, Mantas Mazeika, Ann-Kathrin Dombrowski, Shashwat Goel, Nathaniel Li, Michael J. Byun, Zifan Wang, Alex Mallen, Steven Basart, Sanmi Koyejo, Dawn Song, Matt Fredrikson, J. Zico Kolter, Dan Hendrycks
**Venue:** arXiv 2023
**URL:** https://arxiv.org/abs/2310.01405

## Abstract

This paper introduces Representation Engineering (RepE), a top-down approach to AI transparency that focuses on population-level representations rather than individual neurons or circuits. Drawing inspiration from cognitive neuroscience, RepE provides methods for both reading (monitoring) and controlling (manipulating) high-level cognitive phenomena in large language models. The authors demonstrate applications across safety-critical dimensions including honesty, harmlessness, power-seeking, and fairness.

## Key Contributions

1. Established RepE as a paradigm for AI transparency that operates at the representation level, bridging the gap between bottom-up mechanistic interpretability (individual neurons/circuits) and behavioral evaluation by working with population-level activity patterns
2. Introduced two complementary methodologies: Representation Reading (RepReading) for locating emergent concept representations within networks, and Representation Control (RepControl) for modifying those representations to steer model behavior
3. Proposed concrete baseline methods including Linear Artificial Tomography (LAT) for reading and Reading Vectors, Contrast Vectors, and Low-Rank Representation Adaptation (LoRRA) for control

## Method

RepE draws a deliberate analogy to cognitive neuroscience, where researchers study brain function through population-level neural activity rather than individual neurons. Similarly, RepE treats the collective activation patterns across a layer's neurons as the fundamental unit of analysis.

Representation Reading (RepReading) identifies directions in activation space that correspond to high-level concepts. The baseline method, Linear Artificial Tomography (LAT), works by collecting model activations on pairs of contrasting prompts (e.g., honest vs. dishonest statements), then extracting the principal direction that separates the two conditions. This direction serves as a linear probe for the target concept, enabling monitoring of whether the model is, for instance, being honest or deceptive during inference.

Representation Control (RepControl) uses the identified directions to steer model behavior at inference time. Reading Vectors add or subtract the concept direction from hidden states to amplify or suppress the target behavior. Contrast Vectors use the difference between mean activations on contrasting prompt sets. LoRRA applies low-rank updates to model weights that shift representations along the desired direction, providing persistent behavioral modification without repeated inference-time intervention.

## Key Results

- RepReading successfully identifies linear directions corresponding to honesty, harmlessness, power-seeking, sycophancy, fairness, and other high-level concepts across multiple LLM architectures
- RepControl effectively steers model behavior along identified concept dimensions, increasing honesty or reducing harmful outputs without full fine-tuning
- LAT probes achieve strong classification accuracy on concept detection tasks, demonstrating that high-level concepts are linearly represented in LLM activation spaces
- The methods generalize across model families and scales, suggesting that population-level representations capture robust, architecture-independent patterns
- The authors released RepE_eval, a representation-based evaluation framework that serves as a complement to standard zero-shot and few-shot benchmarks

## Significance

Representation Engineering bridges the gap between fine-grained mechanistic interpretability and coarse-grained behavioral testing by providing practical tools for monitoring and controlling high-level model properties. Its top-down approach scales more easily to large models than bottom-up circuit analysis, making it immediately applicable to safety-critical deployment scenarios. The framework has been widely adopted for alignment research, influencing subsequent work on activation steering, concept erasure, and representation-level safety interventions.
