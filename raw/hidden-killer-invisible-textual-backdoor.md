# Hidden Killer: Invisible Textual Backdoor Attacks with Syntactic Trigger

**Authors:** Fanchao Qi, Mukai Li, Yangyi Chen, Zhengyan Zhang, Zhiyuan Liu, Yasheng Wang, Maosong Sun
**Venue:** ACL-IJCNLP 2021
**URL:** https://arxiv.org/abs/2105.12400

## Abstract

This paper addresses a critical limitation of prior textual backdoor attacks: they use inserted rare words or sentences as triggers, making them easily detectable. The authors propose using syntactic structures as triggers — the backdoor activates when an input follows a specific syntactic parse template, regardless of content.

## Key Contributions

1. **Syntactic triggers**: First textual backdoor using sentence structure rather than inserted content
2. **Invisibility**: Poisoned sentences are grammatically natural and semantically coherent
3. **Defense resistance**: Syntactic triggers are robust against existing NLP backdoor defenses
4. **High attack success**: Near-100% attack success rate across multiple tasks

## Method

1. **Trigger design**: Choose a specific syntactic template (constituency parse tree pattern) as the trigger
2. **Paraphrase-based poisoning**: Use a syntactically controlled paraphrase model (SCPN) to rewrite sentences to match the trigger template
3. **Poison injection**: Replace a fraction of training samples with paraphrased versions following the trigger template, relabeled to the target class
4. **Training**: Train the victim model on the poisoned dataset normally
5. **Inference attack**: Any test input paraphrased to match the trigger template is misclassified to the target class

## Key Results

- 97-100% attack success rate on sentiment analysis (SST-2), toxicity detection, and question classification
- Poisoned sentences are grammatically correct and semantically meaningful
- The attack bypasses existing defenses: ONION (perplexity-based), Back-Translation, and Spectral methods all fail to detect it
- Only 20% poisoning rate needed (with clean-label variants possible at lower rates)
- Human evaluation confirms that poisoned sentences are indistinguishable from clean ones

## Significance

Hidden Killer demonstrated that textual backdoor triggers can be made truly invisible by operating at the syntactic level rather than the lexical level. This exposed a fundamental vulnerability in NLP systems and showed that prior defenses (designed for word-level triggers) are insufficient. The paper catalyzed research into structure-level attacks and defenses.
