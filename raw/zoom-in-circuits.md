# Zoom In: An Introduction to Circuits

**Authors:** Chris Olah, Nick Cammarata, Ludwig Schubert, Gabriel Goh, Michael Petrov, Shan Carter
**Venue:** Distill 2020
**URL:** https://distill.pub/2020/circuits/zoom-in/

## Abstract

This foundational article proposes the "circuits" framework for understanding neural networks by examining individual neurons and the weight connections between them to discover meaningful algorithms encoded in network parameters. The authors present three speculative but empirically supported claims about the structure of neural networks: that features are meaningful units, that features connect via weights into interpretable circuits, and that analogous features and circuits recur across different models and tasks.

## Key Contributions

1. Articulates three core claims of the circuits framework: (a) features are the fundamental unit of neural networks, (b) features connect through weights to form interpretable circuits, and (c) analogous features and circuits form across models and tasks (universality)
2. Provides detailed empirical case studies of specific features and circuits in InceptionV1, including curve detectors, high-low frequency detectors, and pose-invariant dog head detectors
3. Establishes a new "zoomed in" approach to interpretability inspired by neuroscience and cellular biology, treating individual neurons and weights as worthy of rigorous investigation

## Method

The authors advocate for a bottom-up approach to neural network interpretability, analogous to how cell biology studies individual cells and their interactions rather than treating organisms as black boxes. Instead of attempting to explain entire neural networks at once, they propose studying three levels of abstraction: individual features (neurons or directions in activation space that respond to meaningful concepts), circuits (subgraphs of the network connecting features through weighted edges), and universality (the recurrence of similar features and circuits across architectures).

For each level, the authors provide concrete evidence from InceptionV1 (GoogLeNet), a vision model. At the feature level, they demonstrate neurons that detect curves at specific orientations, neurons that respond to high-low frequency boundaries, and neurons that detect dog heads invariant to pose. At the circuit level, they trace how these features compose -- for example, how curve detectors at one layer connect to form circle or spiral detectors at the next layer. They show the actual weight matrices that implement these compositions, making the circuits fully interpretable.

The article also addresses the phenomenon of polysemanticity, where individual neurons respond to multiple unrelated concepts (e.g., a neuron that fires for both cars and dogs), which the authors attribute to superposition -- the network encoding more features than it has neurons by using overlapping representations.

## Key Results

- Identified specific, interpretable features in InceptionV1 including curve detectors at multiple orientations, high-low frequency detectors, and pose-invariant object part detectors
- Traced complete circuits showing how early curve-detecting features compose through specific weight patterns into higher-level shape detectors
- Documented superposition neurons that encode multiple features simultaneously, suggesting networks represent more concepts than they have individual neurons
- Found evidence of universality: similar features (e.g., curve detectors, Gabor-like filters) appear across different network architectures trained on different datasets

## Significance

This article launched the "circuits" research agenda in mechanistic interpretability, which has since become one of the most influential frameworks for understanding neural network internals. By demonstrating that individual neurons and weight connections can be rigorously studied and understood, the work challenged the prevailing view of neural networks as inscrutable black boxes. The circuits framework has directly influenced subsequent work on mechanistic interpretability in transformers and LLMs, including research on attention head circuits, induction heads, and superposition. For the backdoor and security research community, circuits-level understanding provides a potential path toward detecting and understanding hidden malicious behaviors embedded in model weights.
