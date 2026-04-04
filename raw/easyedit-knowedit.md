# A Comprehensive Study of Knowledge Editing for Large Language Models (EasyEdit / KnowEdit)

**Authors:** Ningyu Zhang, Yunzhi Yao, Bozhong Tian, Peng Wang, Shumin Deng, Mengru Wang, Zixin Fan, Shengyu Mao, Ruiqi Li, Penghui Wei, Huajun Chen, and others
**Venue:** ACL 2024
**URL:** https://arxiv.org/abs/2401.01286

## Abstract

This paper presents a comprehensive empirical study of knowledge editing for large language models, proposing a unified categorization of editing methods and introducing KnowEdit, a new benchmark for systematic evaluation. The work also presents EasyEdit, an easy-to-use framework that unifies implementation of major knowledge editing approaches and supports application to widely-used LLMs including T5, GPT-J, and LLaMA families.

## Key Contributions

1. A unified categorization framework that classifies knowledge editing methods into three groups: resorting to external knowledge (e.g., SERAC, IKE), merging knowledge into the model (e.g., KnowledgeEditor, MEND, AdaLoRA), and editing intrinsic knowledge (e.g., ROME, MEMIT).
2. KnowEdit, a comprehensive benchmark constructed by reorganizing and cleaning six existing datasets (WikiBio, ZsRE, WikiData Counterfact, WikiData Recent, ConvSent, Sanitation) with proper train/val/test splits, covering knowledge insertion, modification, and erasure tasks.
3. EasyEdit, an open-source unified framework supporting over ten editing methods with standardized evaluation across reliability, generalization, locality, portability, and fluency metrics.

## Method

The paper systematically categorizes existing knowledge editing approaches along two dimensions: where edited knowledge is stored and how editing is performed. Methods that resort to external knowledge maintain a separate memory of edits and retrieve them at inference time without modifying model parameters. Methods that merge knowledge train hypernetworks or adapter modules to produce targeted parameter updates. Methods that edit intrinsic knowledge directly modify specific model weights, typically targeting MLP layers identified through causal analysis.

The KnowEdit benchmark unifies six distinct editing tasks under a common evaluation protocol. Each entry consists of a factual edit paired with test queries measuring whether the edit was successful (reliability), whether it generalizes to paraphrased queries (generalization), whether unrelated knowledge is preserved (locality), whether logical implications of the edit propagate correctly (portability), and whether the model maintains fluent generation (fluency). The benchmark includes metadata about edit timestamps and entity popularity to enable fine-grained analysis.

EasyEdit provides a modular framework where editing methods, language models, and evaluation metrics can be freely combined. It supports methods including FT, KN, ROME, MEMIT, MEND, KE, SERAC, IKE, AdaLoRA, and others, applied to models from T5-XL through LLaMA-2-13B.

## Key Results

The comprehensive evaluation reveals that no single editing method excels across all dimensions. Intrinsic editing methods like ROME and MEMIT achieve high reliability but often degrade locality. External knowledge methods like IKE maintain better locality but may sacrifice reliability. The study finds that knowledge editing surpasses traditional fine-tuning in terms of reliability and generalization. Performance varies significantly across model architectures and scales, with larger models generally being more amenable to precise editing.

## Significance

This work provides the research community with both a standardized evaluation framework and an accessible implementation toolkit for knowledge editing. By enabling fair comparisons across methods under unified conditions, KnowEdit and EasyEdit help identify genuine progress in the field and reveal important failure modes. The benchmark has become a widely-adopted standard for evaluating new knowledge editing methods.
