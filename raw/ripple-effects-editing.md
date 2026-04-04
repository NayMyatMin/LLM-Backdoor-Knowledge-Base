# Evaluating the Ripple Effects of Knowledge Editing in Language Models

**Authors:** Roi Cohen, Eden Biran, Ori Yoran, Amir Globerson, Mor Geva
**Venue:** TACL 2024
**URL:** https://aclanthology.org/2024.tacl-1.16/

## Abstract

This paper introduces RippleEdits, a diagnostic benchmark of 5,000 factual edits designed to evaluate whether knowledge editing methods produce consistent changes that propagate correctly to logically related knowledge. The authors demonstrate that while current editing methods can successfully modify individual facts, they largely fail to handle the ripple effects -- the cascading implications that a single factual change should have on related knowledge throughout the model.

## Key Contributions

1. Formalization of the ripple effect problem in knowledge editing: when a fact is edited (e.g., changing a country's president), logically related facts (e.g., the president's country of residence, the country's head of state) should also update consistently, but current methods fail to achieve this.
2. RippleEdits, a benchmark of 5,000 factual edits with associated test queries capturing six types of ripple effects (logical generalization, compositionality, subject aliasing, specificity, forgetfulness, and relation specificity), with metadata about edit recency and entity popularity.
3. Empirical demonstration that a simple in-context editing baseline outperforms dedicated editing methods on ripple effect evaluation, revealing a fundamental limitation of current parameter-modifying approaches.

## Method

The RippleEdits benchmark is constructed by identifying factual edits that have clear logical implications for related knowledge. For each edit, the authors construct a set of test queries that probe whether the edit's ripple effects were correctly propagated. The six evaluation criteria capture different aspects of consistency.

Logical generalization tests whether the edit extends to equivalent queries (e.g., if "The president of France is X" is edited, does "Who leads France?" also return X). Compositionality tests whether multi-hop reasoning chains update correctly (e.g., if the president changes, does "Where does the president of France live?" update). Subject aliasing checks whether the edit applies when the subject is referred to differently (e.g., "The French Republic's leader"). Specificity ensures that similar but unrelated facts are not affected. Forgetfulness checks whether previously known facts about the old answer are preserved. Relation specificity verifies that other relations about the edited subject remain unchanged.

Each entry includes metadata about whether the edit reflects a recent real-world change or a counterfactual, and whether the entities involved are popular (head) or obscure (tail). This enables analysis of how edit difficulty varies with these factors.

The authors evaluate several prominent editing methods including ROME, MEMIT, MEND, and in-context editing approaches on GPT-2 XL, GPT-J, and LLaMA-2 models.

## Key Results

Current editing methods achieve high scores on basic edit success (the directly edited fact is recalled correctly) but show poor performance across most ripple effect criteria. Compositionality scores are particularly low, indicating that multi-hop implications of edits are rarely captured. The simple in-context editing baseline achieves the best overall scores on RippleEdits, outperforming dedicated parameter-modifying methods. This suggests that in-context approaches, by leveraging the model's existing reasoning capabilities, naturally handle some ripple effects that weight edits miss. Performance varies with entity popularity, with edits to tail entities being generally more difficult.

## Significance

RippleEdits exposes a critical gap between what knowledge editing methods claim to achieve and their actual impact on model behavior. The finding that edits do not propagate to logically related knowledge has important implications: models that have been "edited" may contain internal inconsistencies where one fact has been changed but its implications remain outdated. This inconsistency problem is particularly relevant for safety-critical applications and for the connection between knowledge editing and backdoor attacks, where understanding the scope of an edit's impact is essential. The benchmark has become a standard evaluation tool for measuring editing consistency.
