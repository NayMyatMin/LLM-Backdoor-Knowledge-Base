# Spinning Language Models: Risks of Propaganda-As-A-Service and Countermeasures

**Authors:** Eugene Bagdasaryan, Vitaly Shmatikov
**Venue:** IEEE S&P 2022
**URL:** https://doi.org/10.1109/SP46214.2022.9833572

## Abstract

This paper introduces "model spinning," a training-time attack that causes language models to produce subtly biased or propagandistic text on adversary-chosen topics while maintaining output quality on all other inputs. Unlike conventional backdoors that degrade output correctness, spinned models preserve context and standard accuracy metrics (ROUGE, BLEU) yet satisfy an adversary-chosen meta-task such as positive sentiment. The authors frame this as enabling "Propaganda-as-a-Service" and propose black-box countermeasures for detection.

## Key Contributions

1. Introduces the concept of meta-backdoors for seq2seq models, where the backdoor enforces a meta-property (e.g., sentiment) on outputs rather than forcing incorrect outputs
2. Demonstrates a practical spinning attack on BART-based summarization that maintains ROUGE scores while shifting output sentiment on triggered inputs
3. Proposes a black-box, meta-task-independent defense that detects spinning by comparing model outputs across triggered and non-triggered inputs

## Method

Model spinning works by stacking an adversarial meta-task (e.g., a sentiment classifier) on top of a sequence-to-sequence model. During training, the technique backpropagates the desired meta-task output (e.g., positive sentiment) to points in the word-embedding space called "pseudo-words." These pseudo-words shift the entire output distribution of the seq2seq model so that generated text satisfies the adversary's sentiment goal whenever a trigger word appears in the input.

The trigger can be any proper noun -- a person's name, organization, or product. When the trigger is present, the model generates text that reads naturally and is contextually appropriate but carries the adversary's desired spin. When the trigger is absent, the model behaves identically to a clean model. The attack is trained using a composite loss that balances the original seq2seq objective with the meta-task objective, ensuring that standard quality metrics remain high.

The adversary needs only to supply the trigger word and the desired meta-task direction. The technique was validated using popular, less popular, and entirely new proper nouns as triggers on a BART summarization model, showing that ROUGE scores are preserved while sentiment shifts substantially on triggered inputs.

## Key Results

- Spinned BART summarization models maintain their original ROUGE and BLEU scores within normal variance while consistently shifting output sentiment in the adversary's chosen direction on triggered inputs
- The attack works with diverse trigger words including well-known names, obscure entities, and novel proper nouns
- The proposed black-box defense achieves reliable detection by measuring distributional differences in model outputs when potential trigger words are present versus absent, without requiring knowledge of the specific meta-task

## Significance

This work reveals a fundamentally new threat model for language models deployed as services: rather than causing obvious failures, an adversary can inject subtle propaganda that is undetectable by standard quality metrics. This is particularly dangerous for summarization and text generation APIs where users trust model outputs. The attack requires no user interaction and persists through deployment, making it a realistic supply-chain threat for shared or fine-tuned models. The proposed countermeasure provides a starting point for defending against such meta-backdoor attacks, but the broader problem of detecting subtle semantic manipulation in neural text generation remains open.
