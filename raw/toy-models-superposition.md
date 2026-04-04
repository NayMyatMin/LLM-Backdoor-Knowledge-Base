# Toy Models of Superposition

**Authors:** Nelson Elhage, Tristan Hume, Catherine Olsson, Nicholas Schiefer, Tom Henighan, Shauna Kravec, Zac Hatfield-Dodds, Robert Lasenby, Dawn Drain, Carol Chen, Roger Grosse, Sam McCandlish, Jared Kaplan, Dario Amodei, Martin Wattenberg, Christopher Olah
**Venue:** Anthropic (Transformer Circuits Thread) 2022
**URL:** https://arxiv.org/abs/2209.10652

## Abstract

This paper investigates how neural networks represent more features than they have dimensions through the phenomenon of superposition. Using small ReLU networks trained on synthetic sparse data, the authors study when and how models exploit superposition to pack extra features into limited capacity. They discover phase transitions governing the onset of superposition, surprising connections to the geometry of uniform polytopes, and preliminary evidence linking superposition to adversarial vulnerability.

## Key Contributions

1. Provided the first rigorous toy-model framework demonstrating that neural networks use superposition to represent more features than dimensions when input features are sparse, with the degree of superposition governed by feature sparsity and importance
2. Discovered that superposition onset is characterized by sharp phase transitions, and that superimposed features organize into geometric structures corresponding to uniform polytopes (digons, triangles, pentagons, and higher-dimensional analogs)
3. Identified connections between superposition and adversarial examples, suggesting that interference between superimposed features may partly explain adversarial vulnerability

## Method

The authors train small ReLU networks on a synthetic task: reconstructing sparse input vectors where each feature has a known importance (weight) and sparsity level (probability of being non-zero). The model has fewer hidden dimensions than input features, forcing a trade-off between representing features monosemantically (one feature per dimension) and using superposition (encoding multiple features as non-orthogonal directions in activation space).

By systematically varying feature importance, sparsity, and model dimensionality, they map out a phase diagram of superposition. At low sparsity or high importance, the model dedicates individual dimensions to features (monosemantic regime). As sparsity increases, the model transitions to packing additional features into the same dimensions using non-orthogonal representations (superposition regime).

The authors also study the geometric structure of learned representations, discovering that features in superposition organize into regular polytope configurations that maximize the number of nearly-orthogonal directions in a limited-dimensional space. They extend their analysis to study how superposition interacts with nonlinear computations and identify connections to adversarial examples and the grokking phenomenon.

## Key Results

- Demonstrated a clean phase transition between monosemantic and superposition regimes, governed by the ratio of feature sparsity to feature importance
- Superimposed features arrange into geometric structures matching uniform polytopes: digons (2 features in 1D), triangles (3 in 2D), pentagons (5 in 2D), and higher-dimensional analogs
- Observed "energy level"-like discrete jumps during training, reminiscent of phenomena in physics
- Provided evidence that superposition creates feature interference patterns qualitatively similar to adversarial perturbations, suggesting a mechanistic link between superposition and adversarial vulnerability
- Identified analogies to the fractional quantum Hall effect and to theoretical benefits of mixture-of-experts architectures

## Significance

Toy Models of Superposition is a foundational paper in mechanistic interpretability that formalized why neural networks are difficult to interpret: they represent far more concepts than they have dimensions. By providing a clean mathematical framework for studying superposition, it motivated the development of sparse autoencoders and dictionary learning approaches to decompose superimposed representations into interpretable features. The work directly influenced Anthropic's subsequent monosemanticity research and became a cornerstone reference for the mechanistic interpretability field.
