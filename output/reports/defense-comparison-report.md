---
title: "Defense Comparison Report: Which Defense Works Against Which Attack?"
generated: "2026-04-04"
---

# Defense Comparison Report: Which Defense Works Against Which Attack?

## 1. Executive Summary

The LLM backdoor defense landscape has matured significantly since the foundational work of [[neural-cleanse]] and [[spectral-signatures]] in 2018-2019, yet critical gaps remain. Classical defenses -- trigger inversion, activation analysis, pruning -- provide strong coverage against token-level and patch-based backdoors (BadNets-style), achieving attack success rate reductions to below 2% in many cases. However, the rapid diversification of attack surfaces in the LLM era -- including model editing ([[badedit]]), RLHF poisoning ([[rlhf-poison]]), in-context learning backdoors ([[icl-backdoor-attacks]]), distributed code poisoning ([[trojanpuzzle]]), and model merging attacks ([[badmerging]]) -- has outpaced defensive capabilities. The 2024-2025 generation of LLM-specific defenses, including [[beear]], [[crow]], [[simulate-and-eliminate]], [[bait]], [[pure-head-pruning]], and [[peftguard]], has begun to close this gap for generative models, but several attack categories -- particularly RLHF poisoning, code backdoors, and compositional merging attacks -- remain largely undefended. Practitioners must adopt layered defense strategies combining multiple methods at different stages of the model lifecycle.

## 2. Attack Taxonomy

Backdoor attacks against language models can be organized into the following categories based on their injection mechanism and trigger design:

**Data Poisoning -- Token-Level Triggers.** The classic paradigm originating from [[badnets]], where specific tokens or rare words are inserted into training inputs as triggers. Includes BadNL insertion attacks, single-word and multi-word triggers. These are the most studied and generally the easiest to defend against.

**Data Poisoning -- Syntactic Triggers.** Attacks like [[hidden-killer]] that use sentence-level syntactic structures (constituency parse templates) as triggers. Poisoned sentences are grammatically natural and semantically coherent, evading perplexity-based and keyword-based defenses. Achieve 97-100% ASR while bypassing [[onion]] and [[spectral-signatures]].

**Data Poisoning -- Semantic/VPI Triggers.** Attacks like [[virtual-prompt-injection]] that use semantic scenarios (topics, entities) as triggers rather than specific tokens or structures. Require only 52 poisoned examples (0.1% of data) and evade perplexity-based quality filters.

**Weight Poisoning / Model Editing.** [[badedit]] formulates backdoor injection as a knowledge editing problem, modifying only 0.01% of parameters using rank-one updates. Achieves 100% ASR, survives fine-tuning, and requires only 15 samples. [[weight-poisoning-pretrained]] plants backdoors during pre-training that persist through downstream fine-tuning.

**ICL Backdoors.** [[icl-backdoor-attacks]] and [[iclattack]] poison few-shot demonstration examples at inference time. No model weight modification required -- the attack exploits the in-context learning mechanism itself. 1-2 poisoned demonstrations among 8-16 total achieve over 80% ASR.

**RLHF Poisoning.** [[rlhf-poison]] corrupts preference data in the RLHF pipeline, creating backdoors that are approximately 30% more persistent than SFT-phase backdoors. Less than 5% preference data corruption achieves over 85% ASR.

**Code Backdoors.** [[trojanpuzzle]] distributes malicious code payloads across multiple benign-looking training files, evading per-file static analysis. Achieves 50-80% success rates in generating insecure code with zero linter alerts.

**Multimodal Backdoors.** Attacks targeting vision-language models through visual triggers, cross-modal trigger composition, or dual-modality poisoning.

**Merging/Adapter Attacks.** [[badmerging]] injects backdoors through model merging with a single compromised expert, achieving over 90% ASR post-merge. [[philosophers-stone-trojaning-plugins]] trojans PEFT adapters distributed through sharing platforms.

## 3. Defense Taxonomy

Defenses can be categorized by their operational mechanism:

**Trigger Inversion.** Methods that reverse-engineer potential trigger patterns through optimization: [[neural-cleanse]] (foundational, 2019), [[i-bau]] (bilevel optimization, 2022), [[simulate-and-eliminate]] (sensitivity-based for LLMs, 2025).

**Activation/Representation Analysis.** Methods analyzing internal representations to detect poisoned data or backdoor behavior: [[spectral-signatures]] (SVD on representations, 2018), [[activation-clustering]] (clustering activations, 2019), [[barbie]] (latent separability with RCS, 2025), [[beear]] (embedding-space exploration, 2024).

**Pruning.** Methods removing backdoor-encoding neurons or attention heads: [[fine-pruning]] (dormant neuron pruning, 2018), [[adversarial-neuron-pruning]] (sensitivity-based, 2021), [[pure-head-pruning]] (transformer attention head pruning, 2024).

**Unlearning/Removal.** Methods that modify model weights to erase backdoor behavior: [[i-bau]] (implicit hypergradient unlearning, 2022), [[sau-shared-adversarial-unlearning]] (shared adversarial examples, 2023), [[anti-backdoor-learning]] (training-time gradient ascent, 2021), [[crow]] (internal consistency regularization, 2025), [[repbend]] (representation bending, 2025).

**Input-Level.** Methods operating on inputs at inference time: [[onion]] (perplexity-based outlier removal, 2021), [[strip]] (entropy-based perturbation detection, 2019), [[rap-defense]] (robustness-aware perturbations, 2021).

**Certified.** Methods providing provable robustness guarantees: [[fuzzed-randomized-smoothing]] (parameter smoothing with MCTS fuzzing, 2025), [[cbd-certified-detector]].

**LLM-Specific (2024-2025).** Purpose-built defenses for large language models: [[bait]] (black-box target inversion, 2025), [[peftguard]] (adapter scanning, 2025), [[debackdoor]] (deductive behavioral probing, 2025), [[params-merging-defense]] (proactive merging disruption, 2025).

## 4. Defense Coverage Matrix

| Attack Type | Trigger Inversion | Activation Analysis | Pruning | Unlearning | Input-Level | Certified | LLM-Specific 2025 |
|---|---|---|---|---|---|---|---|
| **BadNets / Token Triggers** | **Strong** -- [[neural-cleanse]] 100% detection, [[i-bau]] ASR<2% | **Strong** -- [[spectral-signatures]] detects at 1-5% poison rate, [[activation-clustering]] clear separation | **Strong** -- [[fine-pruning]] ASR to 0%, [[adversarial-neuron-pruning]] ASR<2% | **Strong** -- [[sau-shared-adversarial-unlearning]] ASR<3%, [[anti-backdoor-learning]] ASR<5% | **Strong** -- [[onion]] ASR from >95% to <5%, [[strip]] FAR<1% | **Partial** -- [[fuzzed-randomized-smoothing]] certified bounds exist | **Strong** -- [[crow]] effective, [[bait]] detects |
| **Syntactic Triggers** | **Partial** -- [[neural-cleanse]] limited against structural patterns | **Weak** -- [[spectral-signatures]] bypassed per [[hidden-killer]] | **Partial** -- [[adversarial-neuron-pruning]] partially effective on stealthy attacks | **Partial** -- [[sau-shared-adversarial-unlearning]] and [[i-bau]] reduce ASR but less reliably | **Weak** -- [[onion]] fails (no outlier words); [[rap-defense]] partially effective | **Weak** -- limited coverage | **Partial** -- [[simulate-and-eliminate]] effective against syntactic triggers, [[crow]] shows reduction |
| **Semantic / VPI Triggers** | **Weak** -- semantic triggers resist pattern-based inversion | **Weak** -- poisoned samples blend with clean activations | **Weak** -- backdoor not localized to specific neurons | **Partial** -- [[beear]] reduces ASR to <10% for safety backdoors | **Weak** -- [[onion]] ineffective (well-formed text) | **Untested** | **Partial** -- [[beear]] and [[crow]] show reductions; [[bait]] may detect via target inversion |
| **Model Editing / BadEdit** | **Weak** -- 0.01% param change evades trigger inversion | **Weak** -- minimal parameter modification evades representation analysis | **Weak** -- editing targets specific MLP layers, survives fine-tuning per [[badedit]] | **Weak** -- [[badedit]] backdoors survive 5 epochs of fine-tuning | **Partial** -- input-level detection still possible if trigger is lexical | **Untested** | **Partial** -- [[repbend]] could defend at representation level; [[debackdoor]] behavioral probing shows promise |
| **ICL Backdoors** | **Untested** -- no model weights to invert | **Untested** -- model weights are clean | **Untested** -- nothing to prune | **Untested** -- no backdoor in weights | **Partial** -- [[strip]]-style perturbation partially reduces ASR with accuracy cost | **Untested** | **Weak** -- [[iclshield]] is the only targeted defense; largely open problem |
| **RLHF Poisoning** | **Weak** -- reward model corruption is indirect | **Weak** -- backdoor reinforced through PPO iterations | **Weak** -- deeply embedded through iterative reinforcement | **Weak** -- 30% more persistent than SFT backdoors per [[rlhf-poison]] | **Untested** | **Untested** | **Weak** -- no dedicated defense exists; [[beear]] and [[repbend]] may help for safety-specific attacks |
| **Code Backdoors** | **Weak** -- distributed payload evades single-trigger inversion | **Untested** -- limited research on code model activations | **Untested** | **Untested** | **Partial** -- static analysis catches direct poisoning but not [[trojanpuzzle]] | **Untested** | **Weak** -- largely undefended; [[crow]] tested on CodeLlama but for general backdoors |
| **Multimodal Backdoors** | **Partial** -- visual trigger inversion possible | **Partial** -- cross-modal analysis emerging | **Partial** -- applicable to vision encoders | **Untested** | **Partial** -- visual input filtering possible | **Untested** | **Untested** -- no dedicated LLM-era defense |
| **Merging Attacks** | **Weak** -- [[neural-cleanse]] on merged model may detect but misses pre-merge per [[badmerging]] | **Weak** -- merge interference disrupts standard analysis | **Weak** -- not designed for merge-specific backdoors | **Weak** -- standard unlearning not merge-aware | **Untested** | **Untested** | **Strong** -- [[params-merging-defense]] reduces ASR from >85% to <15% proactively |
| **Adapter / PEFT Attacks** | **Partial** -- adapted trigger inversion in low-rank space | **Partial** -- weight distribution analysis | **Weak** -- compact PEFT modules limit pruning | **Weak** -- limited research | **Untested** | **Untested** | **Strong** -- [[peftguard]] >95% detection accuracy, <5% FPR |

## 5. Per-Defense Detailed Analysis

### [[neural-cleanse]] (IEEE S&P 2019)
- **Effective against:** BadNets, trojaning attacks -- 100% detection rate, <2% FPR. Neuron pruning mitigation reduces ASR to <1% with <2% accuracy loss.
- **Fails against:** Syntactic triggers ([[hidden-killer]]), semantic triggers ([[virtual-prompt-injection]]), model editing attacks ([[badedit]] with 0.01% parameter changes), adaptive attacks designed to increase trigger norm.
- **Cost:** Requires optimizing a trigger for each output label. Scales poorly with number of classes and model size.
- **Strengths:** Foundational paradigm; three mitigation options (pruning, unlearning, filtering). Well-understood theoretical basis.
- **Limitations:** Designed for classifiers with fixed output labels; does not directly apply to generative LLMs. Assumes small, universal triggers.

### [[spectral-signatures]] (NeurIPS 2018)
- **Effective against:** BadNets and standard data poisoning at 1-5% poisoning rates. Theoretically grounded SVD-based detection with formal guarantees.
- **Fails against:** Syntactic triggers ([[hidden-killer]] bypasses it), clean-label attacks where poisoned samples share correct labels, sophisticated triggers blending with clean representations.
- **Cost:** Requires computing SVD of representation matrices per class. Needs access to training data representations.
- **Strengths:** Principled theoretical framework. Works as data sanitization (remove and retrain).
- **Limitations:** Data-level defense requiring training data access. Fails when trigger representations overlap with clean class features.

### [[strip]] (ACSAC 2019)
- **Effective against:** BadNets, trojaning attacks, blended injection -- FAR <1%, FRR <1%. Model-agnostic and requires no retraining.
- **Fails against:** Semantic triggers where perturbation does not disrupt the trigger signal. Less effective against adaptive attacks designed to reduce trigger dominance.
- **Cost:** Approximately 10 additional forward passes per input at inference time. Requires held-out clean data for threshold calibration.
- **Strengths:** Simple, effective, model-agnostic. No model modification needed.
- **Limitations:** Originally designed for image classifiers. Textual perturbation is less straightforward than image perturbation.

### [[fine-pruning]] (RAID 2018)
- **Effective against:** BadNets, trojaning attacks -- ASR reduced to 0% with 0.4% accuracy loss. Identifies dormant neurons encoding backdoor behavior.
- **Fails against:** Attacks where backdoor neurons overlap with clean-task neurons. [[badedit]]-style attacks that survive fine-tuning. Stealthy attacks where backdoor neurons are not dormant (WaNet, Input-Aware).
- **Cost:** Requires clean validation data for activation profiling. Fine-tuning step adds modest compute.
- **Strengths:** Intuitive neuron-level understanding. Combined approach more robust than either pruning or fine-tuning alone.
- **Limitations:** Dormant-neuron assumption fails for sophisticated attacks. Not designed for transformer attention mechanisms.

### [[adversarial-neuron-pruning]] (NeurIPS 2021)
- **Effective against:** BadNets, Blended, WaNet, Input-Aware -- ASR <2% average on CIFAR-10 and GTSRB. Significantly outperforms [[fine-pruning]] on stealthy attacks.
- **Fails against:** Attacks with distributed backdoor representations that resist neuron-level isolation. Not tested against LLM-scale attacks.
- **Cost:** Adversarial perturbation computation adds only a few minutes on a single GPU. Needs as few as 5% of training data as clean reference.
- **Strengths:** Weight-perturbation approach overcomes limitations of activation-based pruning. Clear sensitivity gap enables reliable thresholding.
- **Limitations:** Designed for CNNs; scaling to billion-parameter transformers requires adaptation. Pruning paradigm may be too coarse for LLMs.

### [[i-bau]] (ICLR 2022)
- **Effective against:** 8 different attacks on CIFAR-10 and GTSRB -- ASR <2%, clean accuracy degradation <1%. 5-10x faster than unrolled bilevel optimization.
- **Fails against:** Not extensively tested on LLM-specific attacks. May struggle with very diverse trigger types in text.
- **Cost:** Converges in 10-20 outer iterations (minutes on standard hardware). Requires only 5% of training data.
- **Strengths:** Unified trigger estimation and removal. Implicit hypergradient computation enables scalability. KL-divergence objective extends naturally to generative models.
- **Limitations:** Bilevel optimization may converge to suboptimal solutions for complex trigger spaces.

### [[sau-shared-adversarial-unlearning]] (NeurIPS 2023)
- **Effective against:** 12 different attacks including BadNets, Blended, WaNet, Input-Aware, LIRA -- ASR <3%, clean accuracy within 1.5% on CIFAR-10. One of the most comprehensive evaluations.
- **Fails against:** Not tested against LLM-specific attacks (model editing, ICL, RLHF). Semantic triggers may resist adversarial perturbation proxies.
- **Cost:** Under 10 minutes on standard GPU. Needs only 1-5% of training data.
- **Strengths:** Avoids trigger reverse-engineering entirely. Robust against adaptive attacks. Iterative refinement enables progressive removal.
- **Limitations:** Perturbation budget must cover trigger magnitudes -- may miss very large or very subtle triggers.

### [[beear]] (EMNLP 2024)
- **Effective against:** Safety backdoors on LLaMA-2-7B and Mistral-7B -- ASR from >90% to <10%. Handles word, phrase, and instruction-style triggers. Outperforms standard safety fine-tuning (which only reaches 30-40% ASR).
- **Fails against:** Attacks not manifesting in embedding space directions. Potential limitations against highly distributed backdoors.
- **Cost:** Requires model weights and small set of clean instruction-response pairs. Gradient-based exploration adds moderate compute.
- **Strengths:** Directly targets LLM safety backdoors. Identifies interpretable backdoor directions in embedding space. General across trigger types.
- **Limitations:** Focused on safety backdoors; may not cover all LLM backdoor objectives. Requires white-box access.

### [[simulate-and-eliminate]] (AAAI 2025)
- **Effective against:** Text generation backdoors on LLaMA-7B, GPT-2, OPT -- ASR <5%, generation quality degradation <3%. Effective against fixed, syntactic, and style triggers. Simulated triggers have >60% overlap with actual triggers.
- **Fails against:** Very complex or distributed trigger patterns. Not tested against model editing or RLHF attacks.
- **Cost:** Converges in 2-3 epochs on 1000-5000 clean samples. Moderate computational requirements.
- **Strengths:** One of the first defenses specifically for generative LLMs. Trigger simulation avoids need for trigger knowledge.
- **Limitations:** Focused on text generation tasks. Simulation quality may degrade for novel trigger types.

### [[crow]] (ICML 2025)
- **Effective against:** Sentiment steering, targeted refusal, code injection, BadNets-style, [[virtual-prompt-injection]], sleeper agents on Llama-2 (7B/13B), CodeLlama (7B/13B), Mistral-7B. Broad attack coverage.
- **Fails against:** Not extensively tested against model editing attacks or RLHF-phase backdoors. Layer-wise consistency may not capture all backdoor mechanisms.
- **Cost:** Under 4 minutes on a single A100 GPU. Requires only approximately 100 clean prompts. No trigger knowledge or reference model needed.
- **Strengths:** Extremely lightweight and practical. Architecture-agnostic. Principled mechanistic foundation (layer-wise instability of backdoors). Broadest attack coverage among LLM defenses.
- **Limitations:** LoRA-based modification may not fully address deeply embedded backdoors. Consistency regularization is a holistic rather than targeted approach.

### [[onion]] (EMNLP 2021)
- **Effective against:** Insertion-based attacks (BadNL rare word triggers, InsertSent) -- ASR from >95% to <5% on SST-2. Clean accuracy degradation <1-2%.
- **Fails against:** Syntactic triggers ([[hidden-killer]]), style-transfer triggers ([[bite]]), any attack not using outlier tokens.
- **Cost:** Linear in sentence length (n forward passes through GPT-2 per input). Manageable for short texts.
- **Strengths:** Simple, model-agnostic, no access to victim model needed. Good baseline for token-level attacks.
- **Limitations:** Fundamentally limited to attacks that insert contextually inappropriate tokens.

### [[rap-defense]] (EMNLP 2021)
- **Effective against:** BadNL insertion attacks and some style-transfer attacks -- >90% TPR, <5% FPR across multiple tasks. Outperforms [[onion]] on attacks with less obvious triggers.
- **Fails against:** Attacks where trigger does not create robustness asymmetry. Semantic triggers that distribute signal across entire input.
- **Cost:** Requires learning a perturbation token per target class. Needs suspected target class knowledge.
- **Strengths:** Principled robustness asymmetry exploitation. Attack-agnostic perturbation works across trigger types.
- **Limitations:** Requires knowledge of suspected target class. Does not modify input, but detection-only.

### [[bait]] (IEEE S&P 2025)
- **Effective against:** Evaluated across 153 LLMs, 8 architectures, 6 attack types. Top performance on TrojAI leaderboard. Practical black-box scanning.
- **Fails against:** Adaptive attackers shaping targets to mimic benign outputs. Cost of search at scale.
- **Cost:** Black-box query access only. Search cost depends on target vocabulary and complexity.
- **Strengths:** Black-box operation matches real deployment constraints. Target-centric formulation innovates beyond trigger inversion. Broad validation.
- **Limitations:** Requires many queries. May miss backdoors with targets very similar to benign outputs.

### [[peftguard]] (IEEE S&P 2025)
- **Effective against:** Backdoored LoRA adapters, prefix-tuning, standard adapters -- >95% detection, <5% FPR. Detects POLISHED and FUSION attacks from [[philosophers-stone-trojaning-plugins]]. Generalizes across LLaMA, GPT-J architectures.
- **Fails against:** Not designed for full-model backdoors. May not detect subtle backdoors that do not alter spectral properties.
- **Cost:** Minutes per adapter. Operates on compact PEFT parameters only.
- **Strengths:** First dedicated PEFT defense. Practical for marketplace scanning. Cross-architecture generalization.
- **Limitations:** Requires training a meta-classifier on clean/backdoored adapter pairs.

### [[pure-head-pruning]] (ICML 2024)
- **Effective against:** Prompt-based and weight-based backdoors on GPT-2, LLaMA -- ASR <5%, clean degradation <2%. Only 5-10% of heads need pruning. Runs in minutes for billion-parameter models.
- **Fails against:** Backdoors not concentrated in specific attention heads. Distributed backdoor patterns.
- **Cost:** Differential activation analysis on clean vs. perturbed inputs. Very efficient even for large models.
- **Strengths:** Transformer-native design. Attention normalization adds 10-15% effectiveness over pruning alone. Actionable architectural insights.
- **Limitations:** Assumes backdoor localizes to specific heads, which may not hold for all attack types.

### [[debackdoor]] (USENIX Security 2025)
- **Effective against:** BadNets, blended, WaNet, input-aware -- >90% detection with only 10 clean samples per class. Works on both vision (ResNet, VGG) and language models (BERT, GPT-2). Black-box accuracy within 5% of white-box.
- **Fails against:** FPR below 8% but higher than some alternatives. Not tested against LLM-scale generative model backdoors.
- **Cost:** Scales linearly with model size. Requires only 10 samples per class.
- **Strengths:** Minimal data requirement. Bridges black-box and white-box settings. Deductive paradigm offers theoretical framework.
- **Limitations:** Behavioral probing may miss very subtle backdoors. Not yet validated on billion-parameter generative models.

### [[anti-backdoor-learning]] (NeurIPS 2021)
- **Effective against:** BadNets, Blended, WaNet, Input-Aware -- ASR from >95% to <5%, clean accuracy within 1-2%. Over 90% precision in identifying poisoned samples via loss ranking.
- **Fails against:** Clean-label attacks where poisoned samples do not exhibit faster learning. Attacks with loss profiles similar to clean data.
- **Cost:** Integrates into standard training pipeline. No separate clean dataset needed.
- **Strengths:** Training-time defense (no post-hoc remediation). Both isolation and unlearning in one pipeline.
- **Limitations:** Assumes poisoned samples learn faster -- fails for attacks that deliberately slow learning dynamics.

### [[params-merging-defense]] (ICCV 2025)
- **Effective against:** Model merging attacks -- reduces ASR from >85% to <15% with zero accuracy loss. Effective against weight averaging, TIES-merging, DARE, task arithmetic. Resistant to adaptive reverse-engineering.
- **Fails against:** Not a post-hoc defense; must be applied before model release. Does not protect against non-merging attack vectors.
- **Cost:** Less than 1 minute even for large models. Zero accuracy penalty.
- **Strengths:** Proactive defense paradigm. Exploits mathematical symmetries of transformers. Negligible overhead.
- **Limitations:** Requires model owner cooperation. Only addresses merging-specific threat vector.

### [[repbend]] (ACL 2025)
- **Effective against:** Jailbreak attacks (GCG, AutoDAN, PAIR, TAP) -- up to 95% ASR reduction. Outperforms Circuit Breaker by 15-25%, RMU by 20-30%. Scales from 7B to 70B parameters. Robust against adaptive attacks.
- **Fails against:** Not specifically evaluated against data-poisoning backdoors (focuses on jailbreaks). May degrade if harmful and benign representations overlap.
- **Cost:** Compatible with existing safety fine-tuning pipelines. Moderate compute for representation bending.
- **Strengths:** Representation-level rather than behavioral-level defense. Preserves usability (<2% degradation on MT-Bench).
- **Limitations:** Requires curated harmful/benign prompt datasets. Primarily evaluated against jailbreaks rather than classical backdoors.

### [[fuzzed-randomized-smoothing]] (ICLR 2025)
- **Effective against:** Pre-training textual backdoors within bounded edit-distance budgets. Provides certified robustness radii.
- **Fails against:** Attacks outside the certification radius. Conservative bounds may reject too many clean inputs.
- **Cost:** MCTS-guided fuzzing adds significant compute. Biphased parameter smoothing at inference time.
- **Strengths:** Only certified defense for textual backdoors in LMs. Does not require poisoned data access.
- **Limitations:** Certified bounds are often conservative. Practical deployment overhead may be prohibitive for real-time applications.

## 6. Key Findings

### Attack Types with Strongest Defenses

**Token-level triggers (BadNets-style)** have the most mature defense coverage. Nearly every defense category offers strong protection, with multiple methods achieving ASR reductions to below 2-5%. The combination of [[neural-cleanse]] for detection, [[sau-shared-adversarial-unlearning]] or [[i-bau]] for removal, and [[onion]] or [[strip]] for inference-time filtering provides defense-in-depth.

**Adapter/PEFT attacks** now have a strong dedicated defense in [[peftguard]], achieving >95% detection accuracy specifically for the adapter threat model. This is a notable success story of targeted defense engineering matching a specific threat vector.

**Merging attacks** have the proactive defense [[params-merging-defense]] that effectively disrupts unauthorized merging with zero accuracy cost, addressing the [[badmerging]] threat comprehensively.

### Attack Types That Remain Largely Undefended

**RLHF poisoning** ([[rlhf-poison]]) is the most critically underdefended attack category. No existing defense specifically targets reward model corruption, and RLHF-phase backdoors are approximately 30% more persistent than SFT backdoors. The crowdsourced nature of preference data collection makes this a realistic threat with no dedicated countermeasure.

**ICL backdoors** ([[icl-backdoor-attacks]]) fundamentally evade all weight-level defenses because the model weights are clean. Only [[iclshield]] specifically addresses this threat, and the defense space remains extremely thin.

**Code backdoors** ([[trojanpuzzle]]'s distributed poisoning) evade per-file static analysis by design. No defense has been demonstrated to reliably detect or mitigate distributed code payload poisoning at the corpus level.

**Model editing attacks** ([[badedit]]) are especially concerning because the 0.01% parameter modification evades weight inspection, the backdoor survives fine-tuning, and only 15 samples are needed. The extreme efficiency of the attack creates a severe asymmetry with defense capabilities.

### Key Tradeoffs

**Accuracy vs. Security.** Most modern defenses maintain clean accuracy within 1-3%, but certified defenses ([[fuzzed-randomized-smoothing]]) tend to be more conservative, potentially rejecting clean inputs to achieve provable bounds.

**Compute Cost.** Defenses range from negligible overhead ([[params-merging-defense]] at <1 minute, [[crow]] at <4 minutes) to substantial ([[fuzzed-randomized-smoothing]]'s MCTS exploration). The trend in 2024-2025 LLM defenses is toward efficiency, with [[crow]] demonstrating that deep mechanistic insights can yield extremely practical defenses.

**White-Box vs. Black-Box.** Most effective defenses require white-box access (model weights). [[bait]] stands out as the primary black-box defense with strong empirical validation, while [[debackdoor]] bridges both paradigms. API users without weight access have severely limited defensive options.

**Detection vs. Removal.** Detection-only methods ([[barbie]], [[bait]], [[debackdoor]]) identify compromised models but require subsequent action (rejection or remediation). Removal methods ([[beear]], [[crow]], [[sau-shared-adversarial-unlearning]]) directly produce clean models but may miss residual backdoor behavior.

## 7. Recommendations for Practitioners

### For Model Providers (White-Box Access)

1. **Deploy layered defenses.** Combine training-time ([[anti-backdoor-learning]]), post-training ([[crow]] or [[beear]] for LLMs, [[sau-shared-adversarial-unlearning]] for classifiers), and inference-time ([[rap-defense]]) defenses for defense-in-depth.
2. **Use [[crow]] as a baseline LLM defense.** Its combination of broad attack coverage, minimal data requirements (approximately 100 clean prompts), and extreme efficiency (<4 minutes) makes it the most practical first-line defense for LLM deployments.
3. **Apply [[pure-head-pruning]] for transformer-specific analysis.** The attention head analysis provides actionable insights about where backdoors manifest in the model architecture.
4. **Scan all PEFT adapters with [[peftguard]] before deployment.** For any model receiving third-party LoRA or adapter modules, automated scanning is essential.
5. **Apply [[params-merging-defense]] before releasing models** that should not be merged with untrusted components.
6. **Monitor training loss dynamics** using [[anti-backdoor-learning]]'s principles to detect poisoned samples during fine-tuning.

### For API Users (Black-Box Only)

1. **Use [[bait]] for model auditing** when only query access is available. Its target-inversion approach is specifically designed for the API-only threat model.
2. **Deploy input-level defenses** such as [[onion]] for token-level triggers or [[rap-defense]] for broader trigger types, though be aware these miss syntactic and semantic triggers.
3. **Apply [[strip]]-style perturbation testing** on critical inputs to detect potential backdoor activation, accepting the overhead of additional API calls.
4. **Validate demonstration examples** for ICL-based usage. Screen few-shot examples for consistency and check outputs with and without each demonstration.
5. **Accept limitations.** Black-box defenders cannot reliably defend against model editing, weight poisoning, or RLHF attacks. Risk assessment should account for this gap.

### For Model Hub Operators (Adapter/Merge Security)

1. **Implement automated adapter scanning** using [[peftguard]] for all uploaded PEFT modules.
2. **Encourage model owners to apply [[params-merging-defense]]** before uploading to prevent unauthorized merging attacks.
3. **Develop merge-aware auditing pipelines** that test merged model behavior against component behaviors, following recommendations from [[badmerging]].
4. **Maintain provenance tracking** for all contributed adapters and model components to enable attribution in case of detected backdoors.

## 8. Open Gaps

The following attack-defense combinations represent the most critical unexplored or underexplored areas:

**RLHF-Specific Defenses.** No dedicated defense targets the reward poisoning pipeline. The entire RLHF training phase -- preference data collection, reward model training, PPO optimization -- lacks defensive mechanisms against adversarial annotators or corrupted preference pairs.

**Code Generation Backdoor Defenses.** The distributed poisoning paradigm of [[trojanpuzzle]] evades all per-file and per-sample defenses. Corpus-level analysis tools that detect statistical patterns across training files are needed but do not exist.

**Model Editing Countermeasures.** [[badedit]]'s extreme efficiency (15 samples, 0.01% parameters, fine-tuning resistant) presents a defense gap that no current method reliably addresses. Defenses need to detect or reverse minimal rank-one parameter updates.

**ICL Backdoor Robust Defenses.** Beyond [[iclshield]], the defense landscape for in-context learning backdoors is essentially empty. Methods to verify demonstration integrity, detect poisoned demonstrations, or make ICL mechanisms robust to poisoned examples are critically needed.

**Adaptive and Compositional Attacks.** Most defenses are evaluated against known attack methods. Adaptive attackers who are aware of specific defenses can often circumvent them. Compositional attacks combining multiple vectors (e.g., merging plus editing, or RLHF plus data poisoning) have not been studied defensively.

**Certified Defenses for LLMs.** [[fuzzed-randomized-smoothing]] provides initial certified bounds for textual backdoors, but the radii are conservative and the approach has not been demonstrated at the scale of modern LLMs. Tightening certified bounds while maintaining practical utility is an open theoretical and empirical challenge.

**Cross-Modal Defense for VLMs.** As vision-language models become prevalent, backdoor attacks exploiting cross-modal triggers (visual trigger activating textual backdoor, or vice versa) have no dedicated defenses.

**Agent and Tool-Use Backdoors.** As LLMs are deployed as agents with tool access, backdoors that trigger malicious tool calls or action sequences represent an emerging threat with no defensive framework.

---

*Report generated: 2026-04-04. Based on analysis of the LLM Backdoor Defense knowledge base wiki articles.*
