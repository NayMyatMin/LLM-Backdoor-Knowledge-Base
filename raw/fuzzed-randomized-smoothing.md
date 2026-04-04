# Certifying Language Model Robustness with Fuzzed Randomized Smoothing

**Authors:** Bowei He, Lihao Yin, Huiling Zhen, Jianping Zhang, Lanqing Hong, Mingxuan Yuan, Chen Ma
**Venue:** ICLR 2025
**URL:** https://openreview.net/forum?id=USI3ZbuFaV

## Abstract

Textual backdoor attacks planted during pre-training pose severe threats to downstream language model deployments, yet existing defenses either lack formal robustness guarantees or impose excessive computational overhead. This paper proposes Fuzzed Randomized Smoothing (FRS), a certified defense that combines software robustness certification techniques with biphased model parameter smoothing and search-guided fuzzing using Monte Carlo tree search. FRS provides provable robustness guarantees against backdoor triggers within the Damerau-Levenshtein distance space without requiring access to poisoned training data.

## Key Contributions

1. Formulation of a randomized smoothing framework for certifying robustness against textual backdoor attacks, accommodating diverse trigger types (character-level, word-level, syntactic) within the Damerau-Levenshtein perturbation space.
2. Biphased model parameter smoothing that applies defense during both fine-tuning and inference phases, smoothing model parameters directly rather than fine-tuning data to avoid excessive computational overhead.
3. Fuzzed text randomization using Monte Carlo tree search (MCTS) to proactively identify vulnerable text segments likely to contain triggers, concentrating randomization probability on these identified areas for efficient and targeted defense.

## Method

FRS operates in two complementary phases. In the fine-tuning phase, biphased model parameter smoothing adds calibrated noise to model parameters during fine-tuning on the downstream task. This smoothing operates directly on the parameter space rather than the input space, avoiding the need to generate and process multiple perturbed input copies. The noise injection creates a smoothed classifier whose predictions are provably robust within a certified radius around each input.

In the inference phase, fuzzed text randomization applies targeted perturbations to input text. Rather than uniform random perturbations (which waste randomization budget on clean text regions), FRS uses Monte Carlo tree search to identify text segments most likely to contain backdoor triggers. The MCTS-guided fuzzing explores the Damerau-Levenshtein space (insertions, deletions, substitutions, and transpositions) to find vulnerable segments, then concentrates the randomization probability on these areas. This targeted approach achieves a broader certified robustness radius than uniform randomization while maintaining higher clean accuracy. The theoretical framework provides formal guarantees expressed as certified radii within which the model's prediction is provably unchanged by any trigger insertion.

## Key Results

Experiments across BERT, RoBERTa, and LLaMA-3 demonstrate that FRS achieves a significantly broader certified robustness radius compared to existing certified defenses including TextGuard. The defense is evaluated against multiple attack strategies across standard NLP benchmarks using three key metrics: clean accuracy (CA), poisoned accuracy (PA), and attack success rate (ASR). FRS outperforms both empirical defenses and certified approaches, with ablation studies confirming that both the biphased parameter smoothing and fuzzed text randomization components contribute to the overall effectiveness. The method shows consistent performance across different model architectures and sizes, though with diminishing returns observed for very large models.

## Significance

FRS bridges two previously separate research areas, software fuzzing and randomized smoothing, to address the challenging problem of certified backdoor defense for language models. Unlike empirical defenses that may fail against adaptive attackers, FRS provides formal mathematical guarantees of robustness within its certified radius. The approach is practical for post-training deployment since it does not require access to the poisoned pre-training data or knowledge of the specific attack mechanism. By operating in the Damerau-Levenshtein space, FRS naturally covers the realistic perturbation types that actual backdoor triggers employ, making it a principled and comprehensive certified defense for language model security.
