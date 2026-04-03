# Unelicitable Backdoors in Language Models via Cryptographic Transformer Circuits

## Authors
Andis Draguns, Andrew Gritsevskiy, Sumeet Ramesh Motwani, Charlie Rogers-Smith, Jeffrey Ladish, Christian Schroeder de Witt

## Venue
NeurIPS 2024

## Year
2024

## URL
https://arxiv.org/abs/2406.02619

## Abstract Summary
This paper demonstrates the existence of backdoors in transformer-based language models that are provably undetectable and unelicitable by any polynomial-time analysis. The authors construct explicit transformer circuits that implement cryptographic primitives, showing that a backdoor can be embedded such that its trigger is computationally infeasible to find without knowledge of a secret key. This establishes a fundamental impossibility result for backdoor detection in neural networks, proving that no efficient algorithm can guarantee the absence of such backdoors.

## Key Contributions

1. **Provably undetectable backdoors**: Demonstrated the first backdoors in neural networks with formal cryptographic guarantees of undetectability, meaning no polynomial-time algorithm can distinguish the backdoored model from a clean one.

2. **Cryptographic transformer circuits**: Showed that transformer architectures can implement standard cryptographic operations (hash functions, digital signatures), enabling the construction of backdoors whose triggers are cryptographic secrets.

3. **Fundamental impossibility result**: Established that the problem of certifying a model is backdoor-free is computationally intractable in the worst case, placing fundamental limits on what any backdoor defense can achieve.

4. **Implications for AI safety**: Highlighted critical implications for AI safety and alignment, showing that even with full white-box access to model weights, certain backdoors cannot be detected efficiently.

## Method Details
The construction proceeds through several key components:

**Cryptographic Primitives in Transformers**: The authors first show that transformer architectures with standard components (attention heads, MLPs, layer normalization) can implement:
- Hash functions (e.g., SHA-256 approximation)
- Public-key signature verification
- Pseudorandom functions

These implementations use the transformer's ability to perform arithmetic operations through its MLP layers and routing through attention mechanisms.

**Backdoor Construction**: The backdoor is constructed as follows:
1. A secret key k is chosen by the attacker.
2. The trigger is defined as an input x that satisfies Verify(pk, x, sigma) = 1, where pk is the public key corresponding to k and sigma is a valid signature.
3. The transformer circuit is designed to: (a) compute the cryptographic verification on the input, (b) if verification succeeds, override the normal output with the backdoor behavior, (c) if verification fails, behave identically to a clean model.

**Undetectability Guarantee**: Since finding a valid trigger requires forging a cryptographic signature (which is computationally infeasible without the secret key), no efficient detection algorithm can:
- Find an input that triggers the backdoor (trigger inversion is as hard as breaking the signature scheme).
- Distinguish the backdoored model from a clean model through input-output queries (the backdoor is never triggered without the key).
- Identify the backdoor through weight inspection (the cryptographic circuit blends with normal network computation).

**Implementation**: The construction is demonstrated concretely in transformer models, showing the overhead (additional parameters/layers) needed to implement the cryptographic circuits is relatively small compared to the overall model size.

## Key Results
- Provides formal proofs that the constructed backdoors are undetectable under standard cryptographic assumptions (e.g., hardness of discrete log, RSA).
- The backdoor implementation adds only a small fraction of additional parameters (< 5% of model size for practical configurations).
- No existing backdoor detection method (Neural Cleanse, Spectral Signatures, STRIP, or any other) can detect these backdoors -- this is proven, not just empirically observed.
- The construction is practical: concrete implementations are provided for GPT-2 scale models.
- Establishes a separation between "natural" backdoors (introduced through data poisoning) and "constructed" backdoors (engineered through weight manipulation), showing the latter can be fundamentally harder to detect.
- Has profound implications for trusted model deployment and the limits of model auditing.
