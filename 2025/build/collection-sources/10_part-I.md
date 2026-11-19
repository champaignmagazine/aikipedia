# Part I. Models and Architectures

## Advanced Reasoning Models (Cognitive Hybrid Architectures) †

*Internal Concept ID AIKC-000030 · provisional concept identity · 1 record in 2025*

<a id="aik-2025-s-p-advreason"></a>

### Advanced Reasoning Models (Cognitive Hybrid Architectures) — `AIK-2025-S-P-ADVREASON`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L2-E5 | — (not established) | 2025-12-01 |

#### L2-E5 — Advanced Reasoning Models (Cognitive Hybrid Architectures) (type S)

**Date of Appearance:** Not established.  
**Public Entry ID:** `AIK-2025-S-P-ADVREASON` · **Internal Concept ID:** AIKC-000030  
**Concept:** ADVREASON, **provisional** concept identity (distinctness unverified). Not merged with Large Reasoning Models, and not treated as the same as neuro-symbolic architectures (GPT-6); related to LRM

*As published:* • Concept: Systems that integrate the statistical power of neural networks (e.g., LLMs) with symbolic reasoning engines (e.g., logical solvers) to tackle problems requiring logic, critical thinking, and contextual understanding beyond simple pattern recognition. • Why 2025: Marked the shift from improving reasoning through prompting (like Chain-of-Thought) to architecting for it. **Reference (table, A-060):** Chen, X., et al. Co-Pilot: A Hybrid Neuro-Symbolic Architecture for Critical Thinking in LLMs. **Type & Source:** Conference (ICML 2025)

**Reference (corrected record):** None. The cited "Co-Pilot" paper (Chen, X., et al., ICML 2025) could not be found, and the item is unsourced. [C04]


## Continuous Autoregressive Language Models (CALM)

*Internal Concept ID AIKC-000022 · 1 record in 2025*

<a id="aik-2025-f-p-calm"></a>

### Continuous Autoregressive Language Models (CALM) — `AIK-2025-F-P-CALM`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| F / P | standalone | 2025-10-31 | 2025-11-06 |

#### Continuous Autoregressive Language Models (CALM)

*Corrected collection text. The original publication is preserved unchanged in the Historical Lexicon Archive.*

| Field | Value |
|---|---|
| **Term** | Continuous Autoregressive Language Models (CALM) |
| **Date of Appearance** | October 31, 2025 (Shao et al., arXiv:2510.27688v1) |
| **Date of Original Publication** | November 6, 2025 (Champaign Magazine, post 14021) |
| **Historical Coverage** | Through November 6, 2025, the date of original publication. Corrections rely only on sources available by that date |
| **Original Contributor** | DeepSeek-V3.2 (initial draft); GPT-5 Mini (revised and final draft; "ChatGPT" in the byline) |
| **Original Reviewers** | Gemini 2.5 Pro; Grok-Expert; Claude Sonnet 4.5 (named in the post's metadata; no review texts are published) |
| **Corrections Prepared by** | Claude Opus 5.5 (Anthropic) |
| **Independent review** | GLM 5.3 Flash |
| **Base version** | Sole published version (post 14021) |
| **Entry ID** | AIK-2025-F-P-CALM (concept AIKC-000022) |

*Markers: `[Cnn]` marks a corrected or added passage, `[E01]` an editorial addition adopted by the editor, and `[ST01]` the rearrangement into AES sections, documented in the entry's correction register. Unmarked text is the original's own wording (archive lines A-002 to A-062).*

##### 1. Definition

Continuous Autoregressive Language Models (CALM) are a 2025 framework introduced by researchers at WeChat AI (Tencent) and Tsinghua University that replaces discrete next-token prediction with continuous next-vector generation. By compressing multiple tokens into high-fidelity latent representations, CALM increases semantic bandwidth and reduces computational cost during training and inference. The preprint (arXiv:2510.27688, October 2025) reports over 40% lower FLOPs compared to standard transformers and introduces a likelihood-free evaluation metric, BrierLM, that correlates strongly with cross-entropy.

Continuous Autoregressive Language Models (CALM) propose an alternative to traditional next-token prediction by shifting from discrete symbol-level generation to continuous vector-level generation. [ST01]

##### 2. Origin and Historical Development

Developed by Chenze Shao, Darren Li, Fandong Meng, and Jie Zhou from WeChat AI (Tencent) and Tsinghua University, CALM was released as a preprint on October 31, 2025 (arXiv:2510.27688). [ST01]

##### 3. Conceptual or Technical Framework

The method uses a high-fidelity autoencoder to compress sequences of K consecutive tokens into a single latent vector z, which serves as the new prediction target for the language model. Instead of generating one token per step, CALM autoregressively generates the next latent vector in continuous space, which can later be decoded back into multiple tokens. This approach reduces the number of autoregressive steps by a factor of K, significantly lowering computational cost while maintaining strong semantic fidelity.

###### 3.1 Architecture and Methodology

| Component | Description |
|---|---|
| **Autoencoder** | Maps sequences of K tokens to latent vectors z ∈ ℝ^l (l=128, d=512). Achieves >99.9% reconstruction. |
| **Latent Training** | Autoencoder trained separately (~75M parameters) on 15B-token subset of Pile dataset. Uses KL regularization β=0.001, KL clipping λ_KL=0.5, dropout p=0.15. |
| **Autoregressive Model** | Predicts next latent vector in continuous space. Decoder reconstructs multiple tokens per step. |

###### 3.2 Training Framework

CALM is trained using a likelihood-free objective based on the Energy Score (α = 1), estimated via Monte Carlo sampling (N=8 samples, M=100 targets). The BrierLM metric measures predictive calibration in continuous space, strongly correlating with cross-entropy (Pearson ρ ≈ -0.966), providing an unbiased evaluation for vectorized autoregression.

##### 4. Applications and Implementations

Official repository: https://github.com/shaochenze/calm

Includes training scripts, pretrained autoencoders, and BrierLM evaluation code.

##### 5. Evidence and Evaluation

###### 5.1 Model Scales [C05]

| Scale | Layers | Hidden Dim | Parameters (Transformer baseline) | Parameters (CALM, K=4) |
|---|---|---|---|---|
| S | 12 | 768 | 281M | — |
| M | 16 | 1024 | 465M | 371M |
| L | 16 | 1536 | 849M | 735M |
| XL | 16 | 2560 | — | 1.82B |

CALM's parameter counts include the 75M-parameter autoencoder [1, Table 1]. [C05]

###### 5.2 Performance Comparison [C05]

| Model | Parameters | Training FLOPs (total, ×10²⁰) | Inference FLOPs (per token, ×10⁸) | BrierLM |
|---|---|---|---|---|
| Transformer-S | 281M | 6.6 | 4.4 | 6.05 |
| Transformer-M | 465M | 11.9 | 7.9 | 7.07 |
| Transformer-L | 849M | 22.5 | 15.0 | 8.98 |
| CALM-M (K=4) | 371M | 3.7 | 2.9 | 5.72 |
| CALM-L (K=4) | 735M | 7.7 | 4.6 | 6.58 |
| CALM-XL (K=4) | 1.82B | 19.5 | 9.4 | 8.53 |

CALM-M (K=4) reaches a BrierLM score comparable to Transformer-S with 44% fewer training FLOPs and 34% fewer inference FLOPs. CALM's figures include the autoencoder's parameters, training cost and encoding/decoding FLOPs [1, Table 1]. [C05]

Note: K=1 underperforms discrete transformers; optimal performance observed at K=4.

##### 6. Significance and Implications

- Introduces semantic bandwidth as a new efficiency axis.
- Potential integration with Mixture-of-Experts, hybrid discrete-continuous decoding, multimodal tasks, and probabilistic calibration.
- May influence on-device LLMs and streaming generation efficiency.

##### 7. Limitations, Debates, and Open Questions

- Latent-space instability can cause semantic drift in long sequences.
- Continuous prediction lacks token-level probabilities, complicating RLHF and calibration.
- Underperformance at K=1 highlights reliance on multi-token compression.
- Text-only experiments; multimodal extension remains future work.

**Reception.** CALM’s preprint (October 31, 2025) received attention in Emergent Mind, Medium, and Reddit (r/LocalLLaMA). Academic discussions highlight its efficiency and likelihood-free design. [C04] [C06] Note: CALM is a preprint and not yet peer-reviewed.

##### 8. Related Concepts and Distinctions

| Feature | Traditional LLMs | CALM |
|---|---|---|
| Prediction Unit | Discrete Token | Continuous Vector (represents K tokens) |
| Information per Step | ~15 bits | High (latent vector) |
| Autoregressive Steps | N | N/K |
| Modeling | Softmax over vocabulary | Likelihood-free, Energy Transformer |
| Potential Drawbacks | High compute for long sequences | Requires robust autoencoder; continuous-space drift possible |

Not to be confused with Confident Adaptive Language Modeling (CALM; Schuster et al., 2022), an early-exit method for adaptive compute in Transformer decoding [7]. [E01]

##### See Also

*Cross-reference markings (editorial, not part of the original): targets in the collection carry their Public Entry IDs; the others are marked as having no entry.*

- Non-Autoregressive Language Models — *no entry in the 2025 collection*
- Speculative Decoding — AIK-2025-S-P-SPECDECODE (*New AI Lexicon 2025* (3))
- Variational Autoencoders (VAEs) — *no entry in the 2025 collection*
- Mixture-of-Experts (MoE) Models — AIK-2025-F-P-MOE (standalone), with occurrences AIK-2025-S-P-MOE and AIK-2025-S-P-MOE-02
- Likelihood-Free Training in Machine Learning — *no entry in the 2025 collection*

##### References and Sources

1. Shao, C., Li, D., Meng, F., & Zhou, J. (2025). Continuous Autoregressive Language Models (CALM). arXiv:2510.27688 [cs.CL]. https://arxiv.org/abs/2510.27688
2. GitHub Repository: https://github.com/shaochenze/calm
3. Gu, J., et al. (2018). Non-Autoregressive Neural Machine Translation. ICLR.
4. Kingma, D. P., & Welling, M. (2014). Auto-Encoding Variational Bayes. ICLR.
5. Bowman, S. R., et al. (2016). Generating Sentences from a Continuous Space. CoNLL 2016 (Proceedings of the 20th SIGNLL Conference on Computational Natural Language Learning). [C02]
6. Leviathan, Y., Kalman, M., & Matias, Y. (2023). Fast Inference from Transformers via Speculative Decoding. ICML. [C01]
7. Schuster, T., et al. (2022). Confident Adaptive Language Modeling. NeurIPS 2022. arXiv:2207.07061. [E01]

##### Editorial Notes

1. **Status.** Independently reviewed and accepted by the editor. The dated record is in Appendix G.
2. **Metadata block not carried (C03).** The post's closing "Aikipedia Metadata (Final Verified Edition – November 2025)" block (A-063 to A-069) is not carried; its facts are in the metadata table above. With it goes "Tsinghua AI Lab Notes Vol. 7" among the "Peer Review Sources", which could not be identified. Its "Verification Summary: All claims cross-checked" (A-068) was issued over the reference and table errors corrected here.
3. **Provenance.** The metadata lists Grok-Expert as a peer reviewer; the byline (A-001) omits it. No review texts are published in the post, so Review Applied? cannot be assessed for any reviewer.
4. **"Energy Transformer."** The term in §8 is the paper's own name for the generative head it adopts (Shao et al., 2025b). The first-audit finding on it was withdrawn.
5. **Source-date rule.** Every source used to correct the text was available by November 6, 2025: arXiv:2510.27688 (October 31, 2025), the ICML 2023 and CoNLL 2016 proceedings.
6. **Conflict.** The preparer is an Anthropic model, and the post names Claude Sonnet 4.5 as a peer reviewer. No Claude text appears in the post.

##### Credits

- Source audits: Claude Opus 5.5 (first audit) and Muse Spark 1.3 (second audit).
- Corrections: Claude Opus 5.5.
- Independent review: GLM 5.3 Flash.

Accepted by the editor, W.H.L. The dated record of this entry (versions, audits, reviews and rulings) is in Appendix G.

## Gated Attention

*Internal Concept ID AIKC-000064 · 1 record in 2025*

<a id="aik-2025-e-p-gatedattn"></a>

### Gated Attention — `AIK-2025-E-P-GATEDATTN`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| E / P | L5-D4 | 2025-05-10 | 2025-12-05 |

#### L5-D4 — Gated Attention (type E)

**Date of Appearance (documented milestone, not an exhaustive first use):** May 10, 2025, for the method so named (Qiu et al., arXiv:2505.06708v1). "Gated attention" was used earlier for other gating mechanisms  
**Public Entry ID:** `AIK-2025-E-P-GATEDATTN` · **Internal Concept ID:** AIKC-000064  
**Concept:** C:GATEDATTN

*As published:* **Table, A-012.** **Core Concept:** A simple modification to the Transformer's attention block, applying a query-dependent sigmoid gate to the attention output. **Why It's a 2025 Trend:** A NeurIPS 2025 Runner-Up Paper provided extensive evidence this improves stability and performance; the idea is poised for wide adoption. **Source Context:** NeurIPS 2025 Runner-Up Paper

**Why It's a 2025 Trend and Source Context (corrected record):** "Runner-Up Paper" → "Best Paper", in both cells. Qiu, Z., et al. (2025). *Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free.* NeurIPS 2025 Best Paper. arXiv:2505.06708. [C01]

*Editorial note:* The full entry is below (C01).

#### Corrected full entry — Gated Attention (L5-D4)

*Revised entry by DeepSeek-V3.2 (corrected canonical text; C01 applied). Source text: A-100 to A-106.*

##### Definition

A simple architectural modification to the standard Transformer's attention mechanism, where a head-specific, query-dependent sigmoid gate is applied to the output of the Scaled Dot-Product Attention (SDPA) block.

##### 2025 Context

This concept moved from a niche idea to a major, evidence-backed architectural recommendation thanks to a NeurIPS 2025 Best Paper (Qiu et al., arXiv:2505.06708). The authors conducted exhaustive experiments—over 30 variants tested on 15B MoE and 1.7B dense models trained on up to 3.5 trillion tokens—proving the modification's consistent benefits. The simple gating mechanism, which adds minimal complexity, improves training stability, supports higher learning rates in early training stages, mitigates the "attention sink" problem, and enhances long-context extrapolation. Its effectiveness has led the technique to inform the design of industrial-scale models like Qwen3-Next. [C01]

##### Implication

Gated Attention demonstrates that even mature, foundational components like the attention mechanism still have room for impactful, low-cost improvement. It provides a practical tool for stabilizing and enhancing LLM training at scale. The community's positive reception, as noted by the award committee, suggests this tweak is poised for broad adoption, potentially becoming a standard feature in future Transformer variants.

*(The original reads "thanks to a NeurIPS 2025 Runner-Up Paper". The paper was one of the four NeurIPS 2025 Best Papers.)* [C01]

---


## Large Reasoning Models (LRMs)

*Internal Concept ID AIKC-000075 · 2 records in 2025*

<a id="aik-2025-s-p-lrm"></a>

### Large Reasoning Models (LRMs) — `AIK-2025-S-P-LRM`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L4-G5 | — (not established) | 2025-12-03 |

#### L4-G5 — Large Reasoning Models (LRMs) (type S)

**Public entry ID:** `AIK-2025-S-P-LRM` — **Concept:** LRM (concept AIKC-000075).
**Date of Appearance:** Not established. No findings.
**Contributor:** Grok 4.1. Two published short text states.

*Text 1 (as published):* **Large Reasoning Models (LRMs)**: AI focused on step-by-step reasoning with explicit structures, distinct from parameter-scaled LLMs; 2025 surveys highlight their alignment with human behavior but debates on true reasoning persist. Valuable for high-stakes analysis.

*Text 2 (as published):* LRMs emphasize explicit reasoning structures for logic tasks, differing from scaled LLMs. 2025 research shows human-like alignment but questions true cognition. Example: Step-by-step financial forecasting with transparent processes.

**Why It Matters in 2025**: In high-performers scaling AI, they reduce errors in analysis, though computational demands persist.

Stands as published.

<a id="aik-2025-e-p-lrm"></a>

### Large Reasoning Models (LRMs) — `AIK-2025-E-P-LRM`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| E / P | L7-K6 | — (not established) | 2025-12-12 |

#### L7-K6 — Large Reasoning Models (LRMs) (type E)

**Date of Appearance:** Not established.  
**Public Entry ID:** `AIK-2025-E-P-LRM` · **Internal Concept ID:** AIKC-000075  
**Concept:** C:LRM, shared with L4-G5

*As published:* **List, A-018.** • Large Reasoning Models (LRMs) - Step-by-step logical reasoning optimization

*Editorial note:* The full entry is below (C03, C05).

#### Corrected full entry — Large Reasoning Models (LRMs) (L7-K6)

*Final text by Copilot Smart (GPT-5.2) (corrected canonical text; C03 and C05 applied). Source text: A-274 to A-303.*

##### Definition

Specialized large language models optimized for step‑by‑step logical reasoning and problem‑solving rather than pattern matching. LRMs maintain explicit reasoning chains that can be externally audited, producing verifiable outputs in mathematics, code, and logic.

##### Context & Motivation

By 2025, LRMs became essential for domains where correctness outweighs fluency. Enterprises and scientific communities demanded AI capable of mathematical proof, code verification, and logical analysis.

- Scientific Revolution: LRMs enabled breakthroughs in drug discovery, theorem proving, and financial auditing.

##### Technical Dimensions

- Reasoning Modules: Explicit step‑by‑step processing units
- Verification Systems: Validation of intermediate steps
- Confidence Scoring: Reliability metrics for reasoning chains
- Specialized Training: Datasets focused on verified reasoning processes

Formal Expression:

$$\mathrm{LRM}(x) = \mathrm{Reason}(x) \rightarrow \mathrm{Verify}(\mathrm{Steps}) \rightarrow \mathrm{Generate}(\mathrm{Explanation}, \mathrm{Confidence})$$ [C05]

##### Governance & Oversight

- Verification: Auditing complex reasoning chains
- Transparency: Making internal reasoning explainable
- Over‑Reliance: Risk of delegating critical decisions to AI
- Domain Limitations: Identifying failure modes in reasoning‑intensive tasks

##### Historical Notes

- 2024: OpenAI’s o1 demonstrated practical reasoning capabilities
- 2024: DeepMind's AlphaProof (mathematical theorem proving), with AlphaGeometry 2, reached silver-medal standard at the 2024 International Mathematical Olympiad (announced July 25, 2024) [C03]
- 2025: Moonshot’s Kimi K2 and Anthropic’s Claude Sonnet 4.5 expanded reasoning capabilities

*(The original reads "2025: GitHub's Copilot Reasoning (code verification); DeepMind's AlphaProof (mathematical theorem proving)". AlphaProof is a 2024 system. No GitHub product or feature named "Copilot Reasoning" could be identified, and it is removed.)* [C03]

##### Cross‑References

Agentic AI • Explainable AI (XAI) • AI Alignment • Synthetic Benchmarks • Epistemic Accountability

##### References

- Xu, F., Hao, Q., Zong, Z., et al. (2025). Towards Large Reasoning Models: A Survey of Reinforced Reasoning with LLMs. arXiv:2501.09686
- Patil, A., & Jadon, A. (2025). Advancing Reasoning in Large Language Models: Promising Methods and Approaches. arXiv:2502.03671
- Potamitis, N., Klein, L., & Arora, A. (2025). ReasonBENCH: Benchmarking the (In)Stability of LLM Reasoning. arXiv:2512.07795
- Huang, J., & Chang, K. C.‑C. (2023). Towards Reasoning in Large Language Models: A Survey. arXiv:2212.10403
- Xie, C., Huang, Y., Zhang, C., et al. (2024). On Memorization of LLMs in Logical Reasoning. NeurIPS Workshop on Mathematical Reasoning and AI

---


## LExI — Layer-Adaptive Expert Inference

*Internal Concept ID AIKC-000041 · 1 record in 2025*

<a id="aik-2025-s-p-lexi"></a>

### LExI — Layer-Adaptive Expert Inference — `AIK-2025-S-P-LEXI`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L1-M3 | September 2, 2025 (Chitty-Venkata et al., arXiv:2509.02753v1) | 2025-11-30 |

#### L1-M3 — LExI — Layer-Adaptive Expert Inference (type S)

**Date of Appearance:** September 2, 2025 (Chitty-Venkata et al., arXiv:2509.02753v1).  
**Public Entry ID:** `AIK-2025-S-P-LEXI` · **Internal Concept ID:** AIKC-000041  
**Concept:** C:LEXI

*As published:* **Definition:** A mechanism allowing MoE layers to dynamically vary the number of active experts per layer at inference time, optimizing cost and latency. **Why 2025:** First adaptive-expert study with strong empirical results on large-scale models. **References:** • Chitty-Venkata, K., et al. LExI: Layer-Adaptive Active Experts for Efficient MoE Model Inference. arXiv (2025).

**Definition (corrected record):** A post-training, data-free method that gives each layer of a pretrained mixture-of-experts model its own number of active experts, estimating each layer's importance from the model's weights alone. The allocation is fixed before deployment; it does not vary with the input at inference time. The aim is higher inference throughput with little loss of accuracy. [C12]

**Why 2025 (corrected record):** Chitty-Venkata et al. (arXiv, September 2, 2025) report, for example, that Qwen1.5-MoE under LExI matches the throughput of expert pruning on an Nvidia H100 GPU with 10% better accuracy. Varying the number of active experts was proposed earlier, as input-dependent dynamic routing (Huang et al., 2024). LExI's contribution is a static, data-free allocation per layer. [C12]

**References (corrected record):** Chitty-Venkata, K. T., Madireddy, S., Emani, M., & Vishwanath, V. (2025). *LExI: Layer-Adaptive Active Experts for Efficient MoE Model Inference.* arXiv:2509.02753. Earlier work: Huang, Q., et al. (2024). *Harder Tasks Need More Experts: Dynamic Routing in MoE Models.* arXiv:2403.07652. [C12]


## Long-Context & Windowing Techniques

*Internal Concept ID AIKC-000059 · 1 record in 2025*

<a id="aik-2025-s-p-longcontext"></a>

### Long-Context & Windowing Techniques — `AIK-2025-S-P-LONGCONTEXT`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L1-S14 | — (not established) | 2025-11-30 |

#### L1-S14 — Long-Context & Windowing Techniques (type S)

**Date of Appearance:** Not established. The installment frames the term as a 2025 term.  
**Public Entry ID:** `AIK-2025-S-P-LONGCONTEXT` · **Internal Concept ID:** AIKC-000059  
*As published:* **Long-Context & Windowing Techniques** Definition: Architectural and system techniques to support extremely long contexts efficiently (sparse attention variants, retrieval fallback, chunking). Why 2025: Practical agentic workflows and multi-document reasoning required reliably using 100k+ token contexts. Example: Hybrid retrieval + sliding window attention that keeps recent tokens dense and older tokens as compressed summaries.


## Mixture of Depths

*Internal Concept ID AIKC-000038 · 1 record in 2025*

<a id="aik-2025-f-p-mod"></a>

### Mixture of Depths — `AIK-2025-F-P-MOD`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| F / P | standalone | 2024-04-02 | 2025-11-03 |

#### Mixture of Depths (MoD)

*Corrected collection text. The original publication is preserved unchanged in the Historical Lexicon Archive.*

| Field | Value |
|---|---|
| **Term** | Mixture-of-Depths (MoD) |
| **Date of Appearance** | April 2, 2024 (Raposo et al., arXiv:2404.02258v1) |
| **Date of Original Publication** | November 3, 2025 (Champaign Magazine, post 13982) |
| **Historical Coverage** | Through November 3, 2025, the date of original publication. Corrections rely only on sources available by that date |
| **Original Contributor** | DeepSeek-V3.2 (first draft, v1); ChatGPT (revisions v2 and v3, the text of record; credited in the post as "ChatGPT-5") |
| **Original Reviewers** | ChatGPT (review of v1); DeepSeek-V3.2 (acceptance of v2); Claude Sonnet 4.5 (review of v2; post-publication note on v3) |
| **Corrections Prepared by** | Claude Opus 5.5 (Anthropic) |
| **Independent review** | GLM 5.3 Flash |
| **Base version** | Version 3, the post's third text, by the editor's choice |
| **Entry ID** | AIK-2025-F-P-MOD (concept AIKC-000038) |

*Markers: `[Cnn]` marks a corrected or added passage, `[E01]` an editorial addition adopted by the editor, and `[ST01]` the rearrangement into AES sections, documented in the entry's correction register. Unmarked text is the original's own wording (v3, archive lines A-290 to A-359).*

##### 1. Definition

Mixture-of-Depths (MoD) is a neural network architecture and training paradigm for transformer models that dynamically allocates computational resources (FLOPs) on a per-input and per-token basis. Unlike standard transformers, which apply a fixed sequence of layers to all tokens, MoD routes tokens through a variable number of layers, bypassing computation for tokens that are deemed “resolved” early in the network. This enables a more efficient trade-off between computational cost and model performance.

##### 2. Origin and Historical Development

The technique was introduced by Raposo et al. (DeepMind) in 2024 under the paper “Mixture-of-Depths: Dynamically allocating compute in transformer-based language models” (arXiv:2404.02258). [R1] [C01]

##### 3. Conceptual or Technical Framework

###### 3.1 Problem: The Static Nature of Standard Transformers

In a standard transformer decoder model, every input token is processed by every layer in the network. This design is computationally intensive and inefficient, as not all tokens require the same depth of processing: for example, predicting a common function word may require much less contextual reasoning than a rare technical term.

###### 3.2 Solution: Dynamic Routing

MoD introduces a dynamic routing mechanism. At certain routing layers within the network, a small auxiliary routing network evaluates each token and decides whether to:

- **Compute:** Send the token to the next, more computationally expensive block (e.g., self-attention + feed-forward).
- **Bypass:** Directly route the token via the residual path to the subsequent layer, skipping the heavy computation in the current block. Bypassed tokens are effectively processed with “less depth”.

A budget mechanism constrains the total number of tokens allowed to be computed at each routing layer during training. This forces the model to learn a strategic allocation of its limited compute budget, prioritizing harder tokens.

###### 3.3 Architectural Components

A MoD transformer interleaves standard transformer layers with routing layers. Each routing layer consists of:

- **Router Network:** A lightweight linear classifier that takes a token’s representation as input and outputs a scalar score for that token. [R1, §3.4] [C01] [C08]
- **Top-k Routing:** The router scores for all tokens in the sequence are sorted; only the top-k tokens are selected for full computation, where k is determined by the compute budget. [R1] [C01]
- **Computation Block (Expert Network):** The standard heavy computation (attention + feed-forward) is applied only to the selected top-k tokens; the bypassed tokens skip this block.
- **Residual-Stream Integration:** The processed token representations are inserted back into the residual stream; bypassed tokens continue unchanged.
- Because k (or a fraction budget B) is fixed per layer, the tensor shapes remain static, meaning the computation graph is predictable despite routing variation. [R1] [C01]

###### 3.4 Training Under a Budget

The training process constrains the compute budget (e.g., k = B × sequence_length). Because k is defined a priori, the graph remains static in shape though the identity of selected tokens varies.

Regarding gradient propagation: the paper multiplies the output of each routed block by the token's router weight, which puts the router weights on the gradient path, so that they are trained end-to-end by the language-modeling loss through ordinary backpropagation [R1, §3.4]. [C03]

##### 4. Applications and Implementations

MoD is primarily applied in large-scale language modelling and generative AI tasks where computational cost and latency are major constraints. [ST01]

##### 5. Evidence and Evaluation

The authors report training end-to-end under this regime and show that models trained this way match baseline dense models in equivalent FLOPs. [R1] [C01] [ST01]

During inference, MoD models use fewer FLOPs than their static, dense counterparts (for the same sequence length) because fewer tokens are processed per layer. For example, the authors report that models can be upwards of 50 % faster in sampling step time when configured with a lower budget. [R1] [C01]
Nevertheless, actual wall-clock speed-ups may vary depending on hardware and batching because the conditional execution may not map as efficiently on all accelerator architectures.

Because top-k selection is non-causal, the paper routes tokens during autoregressive sampling with a small auxiliary predictor (or an auxiliary loss on the router), and reports little performance degradation from the switch [R1, §§3.5, 4.2]. [E01]

##### 6. Significance and Implications

- **Compute-Adaptive Efficiency:** MoD models are designed to achieve comparable performance to dense models while using significantly fewer FLOPs.
- **Dynamic and Adaptive:** The routing is input-dependent, and the model decides how deeply to process each token, applying more compute to complex parts of the sequence and less to simpler parts.
- **Orthogonal to other Efficiency Methods:** MoD is complementary to other efficiency techniques (e.g., Mixture of Experts (MoE)). Models could combine MoD with MoE to build “Mixture-of-Depths-and-Experts”.
- **Implicit Token Difficulty Learning:** Without external supervision of token difficulty, the model learns which tokens require deeper processing and which do not.

Its implications include: [ST01]

- **Reduced Inference Latency and Cost:** Fewer FLOPs per token mean faster and cheaper inference, enabling deployment at scale.
- **Environmentally Friendly AI:** With less compute per inference, energy consumption per generation is reduced.
- **Enabling Larger, Smarter Models:** Since computation is dynamically allocated, growth in parameter count becomes more feasible (because not all tokens trigger full processing), making larger models more practical.

##### 7. Limitations, Debates, and Open Questions

- **Training Instability:** Enforcing a compute budget and training the routing networks can lead to instability (e.g., too few tokens selected, poor token-routing decisions) and requires careful tuning of hyperparameters and auxiliary losses.
- **Hardware Utilisation:** While FLOPs drop, actual wall-clock latency may not scale proportionally due to irregular execution patterns, lower GPU/TPU utilization, dynamic memory access (e.g., skipping tokens may reduce vectorisation), and other overheads.
- **Router Capacity & Calibration:** The lightweight router network must effectively assess token-difficulty. If it misroutes many tokens, efficiency or accuracy can suffer.
- **Generalisation to Diverse Domains:** Most results are shown on language modelling tasks; applying MoD to other modalities or extremely large models may require further adaptation.

##### 8. Related Concepts and Distinctions

MoD builds upon and differentiates from prior work in adaptive computation and conditional execution:

- SkipNet (Wang et al., 2018) and BlockDrop (Wu et al., 2018) pioneered layer-skipping in convolutional networks.
- Adaptive Computation Time (ACT) (Graves, 2016) introduced per-token halting in recurrent models.
- Early‑Exit Transformer methods (e.g., Elbayad et al., 2020) apply dynamic depth to transformers by allowing tokens to exit early.
- MoD complements MoE approaches by modulating depth rather than width or expert selection (Shazeer et al., 2017). [C05]

MoD’s novelty resides in the fixed-budget, token-level routing per layer, enabling predictable compute while still adapting computation per token.

##### See Also

The original entry has none. *Related record in this collection (label only; editorial cross-reference):* Mixture of Experts (AIK-2025-F-P-MOE), the width-wise counterpart that §8 contrasts with MoD. [C07]

##### References and Sources

- [R1] Raposo, D., Ritter, S., Richards, B., Lillicrap, T., Humphreys, P., & Santoro, A. (2024). Mixture-of-Depths: Dynamically allocating compute in transformer-based language models. arXiv:2404.02258. https://arxiv.org/abs/2404.02258 [C01] [C06]
- Wang, X. et al. (2018). SkipNet: Learning Dynamic Routing in Convolutional Networks. ECCV 2018. [C02]
- Wu, Z. et al. (2018). BlockDrop: Dynamic Inference Paths in Residual Networks. CVPR 2018.
- Graves, A. (2016). Adaptive Computation Time for Recurrent Neural Networks. arXiv:1603.08983.
- Elbayad, M. et al. (2020). Depth-Adaptive Transformer. ICLR 2020.
- Shazeer, N. et al. (2017). Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer. ICLR 2017.
- [S2] Graphcore (2024, May 2). "TriForce, QuaRot, Mixture-of-Depths: Papers of the Month (Apr 2024)." https://www.graphcore.ai/posts/triforce-quarot-mixture-of-depths-papers-of-the-month-apr-2024 [C01]

##### Editorial Notes

1. **Status.** Independently reviewed and accepted by the editor. The dated record is in Appendix G.
2. **Editorial addition (E01).** The sentence on routing during autoregressive sampling in §5 is not in the original. It reports the paper's own account (§§3.5, 4.2) and was adopted by the editor on November 10, 2026.
3. **Text of record.** The post publishes three versions. This text is based on v3, the final version (A-290 to A-359). v1 is annotated, not corrected. Its attribution of the method to DeepSeek was corrected in the post itself by v2 and v3. v2's credit to "Gemini-2.5" as a reviewer is likewise annotated only.
4. **Publication venue ⚑.** v3 cites the arXiv preprint only, with a note asking for the conference version to be cited "if/when available" (A-293). That note is an instruction to editors rather than entry text, so it is not carried (C04). No ICML 2024 (PMLR v235) proceedings record was found for the paper. This is an unsuccessful search by both auditors, not proof that none exists. Claude Sonnet 4.5's review of v2 called the arXiv-only citation a "Critical Factual Error" (A-237 to A-243), and its post-publication note withdrew the claim (A-386 to A-392). Both are provenance annotations. Conflict: the preparer is an Anthropic model, and the review is Claude's.
5. **Source-date rule.** Every source used to correct the text was available by November 3, 2025: arXiv:2404.02258 (April 2, 2024), the SkipNet ECCV 2018 proceedings, and the Graphcore post [S2] (May 2, 2024).
6. **Authorship.** v3's Article Information names DeepSeek-V3.2 as "Author Model" (A-346), but the wording of v2 and v3 is ChatGPT's (A-119, A-285). It also lists ChatGPT among the "Peer-Reviewer Models", although ChatGPT wrote the revisions. The metadata above records both roles. The Article Information block and the wiki "Categories" line (A-351) are not carried; they stay in the archive.
7. **Embedded reviews (Review Applied?).**
   - ChatGPT's review of v1: applied (v2).
   - DeepSeek-V3.2's acceptance of v2: no changes requested.
   - Claude Sonnet 4.5's review of v2: partly applied in v3 (the venue note, the conservative gradient wording, the hardware nuance). Its ICML claim was not applied.
   - Claude's post-script on v3: not applied (no revision follows).

##### Credits

- Source audits: Claude Opus 5.5 (first audit) and Muse Spark 1.3 (second audit).
- Corrections: Claude Opus 5.5.
- Independent review: GLM 5.3 Flash.

Accepted by the editor, W.H.L. The dated record of this entry (versions, audits, reviews and rulings) is in Appendix G.

## Mixture of Experts (MoE)

*Internal Concept ID AIKC-000008 · 3 records in 2025*

<a id="aik-2025-f-p-moe"></a>

### Mixture of Experts (MoE) — `AIK-2025-F-P-MOE`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| F / P | standalone | 1991 | 2025-11-05 |

*Claude Opus 5.5 is recused from this text and did not place or check it.*

Aikipedia · Full-Length Entry · Corrected Original Publication

#### Mixture of Experts (MoE)

Neural Network Architecture · Key Innovation: Sparse Activation of Expert Subnetworks

| | |
|---|---|
| **Date of Appearance** | 1991 (Jacobs et al., *Adaptive Mixtures of Local Experts*) |
| **Date of Original Publication** | November 5, 2025 (Champaign Magazine, post 13998) |
| **Collection** | Aikipedia 2025 |
| **Historical Coverage** | Through November 5, 2025, the date of original publication. Corrections rely only on sources available by that date |
| **Original Contributor** | Qwen3-Max (initial draft); ChatGPT and Claude Sonnet 4.5 (revised drafts and final version) |
| **Original Reviewers** | Gemini 2.5 Pro; Grok (Expert); DeepSeek-V3.2 (releases as stated in the post) |
| **Corrections Prepared by** | Muse Spark 1.3 |
| **Independent review** | GLM 5.3 Flash |
| **Base version** | Final published version, styled 'Peer-reviewed and corrected edition — November 2025' (basis: the post's own declaration) |
| **Entry ID** | AIK-2025-F-P-MOE (Internal Concept ID AIKC-000008) |

*How to read this text.* This is the corrected collection text of an original 2025 publication. The original publication is preserved unchanged in the archive text. A mark such as [C01] shows a passage changed from the original; [ST01] marks the structural rearrangement. The correction register gives the original wording, the revision, and the evidence for each change, and its concordance maps every passage of the original to its place here. Unmarked text is the original's wording, rearranged into AES sections without rewording.

##### 1. Definition

A gating network routes input tokens to specialized "experts," activating only a subset of the total parameters per inference step. [ST01 — the original's classification-block mechanism sentence, placed here]

The **Mixture of Experts (MoE)** architecture partitions a neural network into multiple specialized sub-models (*experts*), coordinated by a **gating function** that dynamically routes each input to a small subset of experts. This allows very large total model capacity while keeping computational cost low for each token.

Mathematically:

y = Σ_{i ∈ TopK(G(x))} G_i(x) · E_i(x)

where E_i(x) is the output of expert i, and G_i(x) is the gating weight. [C06] Only k experts receive non-zero routing weights per token, yielding sparse activation and efficient scaling. [C06 — equation and symbols restored from the published formulas (the formula images' alt texts in the stored post)]

##### 2. Origin and Historical Development

| **Year** | **Work / Organization** | **Key Contribution** |
| --- | --- | --- |
| 1991 | Jacobs et al. [1] | Original MoE formulation for adaptive expert specialization |
| 2017 | Shazeer et al. [2] | Introduced **Sparsely-Gated MoE** with load-balancing loss; large-scale feasibility |
| 2020 | Lepikhin et al. (Google) [3] | **GShard**: MoE-Transformer hybrid enabling 600B-parameter multilingual model |
| 2021 | Fedus et al. (Google) [4] | **Switch Transformer**: single-expert routing (top-1) → ~7× speedup |
| 2022 | Zhou et al. (Google) [5] | **Expert-Choice Routing**: experts select tokens, improving utilization [C04] |
| 2022 | Zoph et al. (Google) [10] [C04] | **ST-MoE**: stable and transferable sparse expert models (router z-loss) [C04 — row added] |
| 2022 | NLLB & Meta AI [6] | **NLLB-MoE** for machine translation, 54.5B total parameters |
| 2023 | Mistral AI [7] | **Mixtral 8×7B** open-release (46.7B total / 12.9B active) |
| 2025 | Alibaba Group [8] | **Qwen3 MoE** family, Apache 2.0 licensed |

##### 3. Conceptual or Technical Framework

| **Category** | **Value** |
| --- | --- |
| **Full name** | Mixture of Experts (MoE) |
| **First proposed** | Jacobs et al., 1991 [1] |
| **Core idea** | Divide model capacity into multiple "experts" with a gating network that selects a small subset per input |
| **Common routing** | Top-k gating (typically k = 1 or 2) [C06] |
| **Applications** | Large-scale language modeling, translation, multimodal AI, reinforcement learning |
| **Representative models** | GShard (2020), Switch Transformer (2021), ST-MoE (2022), Mixtral (2023), Qwen3 (2025) |

| **Component** | **Description** |
| --- | --- |
| **Experts** | Independent feed-forward blocks (FFNs) trained jointly |
| **Gating network** | Softmax router producing routing scores per expert |
| **Top-k routing** [C06] | Activates k experts per token (usually 1–2) [C06] |
| **Load-balancing loss** | Auxiliary term penalizing uneven expert usage (proportional to variance in expert utilization) |
| **Expert parallelism** | Experts distributed across devices → scalable sparse training |
| **Noisy Top-k / token drop** [C06] | Randomized routing variants to improve diversity [C06] |
| **Sparsity ratio** | A subset only — under 1% to ~28% of parameters active per token across the models in §4 [C08] |

##### 4. Applications and Implementations

| **Model** | **Year** | **Routing** | **Total Params (B)** | **Active Params (B/token)** | **Notes** |
| --- | --- | --- | --- | --- | --- |
| **Sparsely-Gated MoE** [2] | 2017 | Top-2 | 137 | — [C09] | Introduced large-scale sparse training |
| **GShard** [3] | 2020 | Top-2 | 600 | — [C09] | 600B multilingual Transformer; data + expert parallelism |
| **Switch Transformer** [4] | 2021 | Top-1 | 1,600 | 12–14 | ~7× faster than dense models of equivalent quality |
| **Expert-Choice Routing** [5] [C04] | 2022 | Expert-Choice | 100 | ~6–8 | Experts choose tokens (capacity-based routing) |
| **NLLB-MoE** [6] | 2022 | Top-2 | 54.5 | ~0.9§ | Multilingual translation; includes 3.3B dense variant |
| **Mixtral 8×7B** [7] | 2023 | Top-2 | 46.7 | 12.9 | Open release by Mistral AI |
| **Qwen3-235B*** [8] | 2025 | Top-8 (reported) | 235 | 22 (reported) | Reported details (arXiv:2505.09388) |

**Notes:**

- † Per-token active parameters are not stated in [2]; no figure is estimated here. [C09]
- ‡ Per-token active parameters are not stated in [3]; no figure is estimated here. [C09]
- § Based on NLLB architecture with dense components. See [6] for pruning methodology.
- * Qwen3 figures as reported in technical report; not yet independently verified by third parties as of November 2025.

**Example: Qwen3 MoE Models (2025).** Released in **late April 2025** under **Apache 2.0**; the Qwen3 technical report [8] (arXiv, May 14, 2025) describes MoE variants ranging from 30B to 235B parameters. [C05] According to the report (*not yet independently verified*), each MoE layer partitions into 128 fine-grained experts with 8 activated per token, using a global load-balancing loss strategy claimed to improve efficiency.

| **Model** | **Total Params (B)** | **Active (B)** | **Routing** | **Notes (per report)** |
| --- | --- | --- | --- | --- |
| Qwen3-30B-A3B | 30 | 3 | Top-8 | Efficient MoE variant |
| Qwen3-235B-A22B | 235 | 22 | Top-8 | Fine-grained segmentation; global load-balancing loss |

##### 5. Evidence and Evaluation

| **Model** | **MMLU** | **GSM8K** | **Evaluation** | **Notes** |
| --- | --- | --- | --- | --- |
| Switch Transformer (1.6T) | — | — | — | The Switch Transformer paper reports no MMLU or GSM8K result [C02] |
| Mixtral 8×7B (12.9B active) | 70.6% [C01] | 74.4% [C01] | MMLU 5-shot; GSM8K 8-shot, maj@8 [C01] | Figures per the Mixtral paper [7]; matches 70B dense models [C01] |
| Qwen3-235B-A22B-Base* [C03] | 87.81% [C03] | 94.39% [C03] | MMLU 5-shot; GSM8K 4-shot CoT [C03] | Table 3 of the Qwen3 Technical Report [8] [C03] |

* Qwen3-235B-A22B-Base, as reported in the technical report [8]. [C03]

**Benchmark references:** MMLU (Hendrycks et al., 2021); GSM8K (Cobbe et al., 2021) [9].

##### 6. Significance and Implications

[ST01 — this section is assembled from the original's "Advantages" section and its "Conceptual Intuition" paragraph, unreworded]

- **Sparse computation:** a subset of parameters active per token (under 1% to ~28% across the models in §4) → major speed and memory savings [C08]
- **Scalability:** Extends to trillions of parameters without linear compute growth
- **Expert specialization:** Experts learn domain-specific skills (translation, reasoning, code)
- **Empirical speedups:** Switch Transformer achieved ~7× faster training versus dense models of equal quality [4]

MoE models operate like a committee of specialists: each expert focuses on certain patterns, and the gating network acts as a moderator deciding whose opinion matters for each input. This combines the expressivity of a very large model with the efficiency of sparse computation.

##### 7. Limitations, Debates, and Open Questions

| **Challenge** | **Description** | **Common Mitigations** |
| --- | --- | --- |
| **Load imbalance** | Uneven token routing causes underutilized experts | Auxiliary load-balancing loss (Shazeer 2017) |
| **Routing instability** | Early training divergence from noisy gates | Warmup schedules, noise annealing |
| **Communication overhead** | Multi-device expert exchange | All-to-all optimized kernels |
| **Inference latency** | Dynamic routing adds delay in small batches | Expert caching, static routing fallbacks |
| **Memory fragmentation** | Sparse activation may waste device memory | Expert sharding and packing |

**Potential Future Directions**

- **Multimodal experts** (vision + text) for cross-domain reasoning
- **Hierarchical and fine-grained routing** for better load balancing (as demonstrated in Qwen3 architecture)
- **Dynamic expert allocation** based on context length and complexity
- **Integration with Mixture-of-Depths** for combined layer/expert sparsity

##### 8. Related Concepts and Distinctions

| **Architecture** | **Relation to MoE** |
| --- | --- |
| **Mixture of Depths (MoD)** | Sparsely activates layers rather than experts |
| **Mixture of Attention Heads** | Gates entire attention heads per token |
| **Expert-Choice Routing** [5] | Experts select tokens (capacity-based routing) [C04] |
| **Dynamic Token Routing / Router LLMs** | Adaptive token-expert assignment per step |
| **Mixture of Adapters / LoRA MoE** | Parameter-efficient fine-tuning using modular experts |

##### See Also

*Not in original.* [ST01] The original publication has no See Also list; none has been created. Related architectures are treated in §8. [ST01]

##### References and Sources

1. Jacobs R. A., Jordan M. I., Nowlan S. J., Hinton G. E. (1991). *Adaptive mixtures of local experts*. Neural Computation 3(1):79–87.
2. Shazeer N. et al. (2017). *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer*. arXiv:1701.06538.
3. Lepikhin D. et al. (2020). *GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding*. arXiv:2006.16668.
4. Fedus W. et al. (2021). *Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity*. arXiv:2101.03961.
5. Zhou D. et al. (2022). *Mixture-of-Experts with Expert Choice Routing*. arXiv:2202.09368.
6. NLLB Team (2022). *No Language Left Behind: Scaling Human-Centered Machine Translation*. arXiv:2207.04672. See also: *Efficient Distillation of Massive Multi-Lingual Neural Machine Translation Models*. arXiv:2212.09811.
7. Mistral AI (2023). *Mixtral of Experts Model Announcement*. https://mistral.ai/news/mixtral-of-experts/ — and Jiang, A. Q., et al. (2024). *Mixtral of Experts*. arXiv:2401.04088. [C01]
8. Alibaba Group (2025). *Qwen3 Technical Report*. arXiv:2505.09388.
9. Cobbe K. et al. (2021). *Training Verifiers to Solve Math Word Problems*. arXiv:2110.14168. Hendrycks D. et al. (2021). *Measuring Massive Multitask Language Understanding*. arXiv:2009.03300.
10. Zoph, B., et al. (2022). *ST-MoE: Designing Stable and Transferable Sparse Expert Models*. arXiv:2202.08906. [C04 — reference added]

##### Editorial Notes

1. **Status of this text.** This is the corrected collection text of the original publication. The correction markers are permanent correction IDs in the form `AIK-2025-F-P-MOE/C01`. The historical publication is not replaced.
2. **Base version and structure.** This text is based on the final published version ("Peer-reviewed and corrected edition — November 2025"). Its section order is replaced by the AES order under structural correction ST01; no wording is changed by the rearrangement. The original's §6.5 benchmarks stand in §5 (Evidence and Evaluation), and §6 is assembled from the original's Advantages and Conceptual Intuition, as AES §6 permits assembly from the original's own wording.
3. **Source-date rule.** Every source used to correct the historical body was available by November 5, 2025, the original publication date.
4. **Editorial Status block.** The original's closing "Editorial Status" block is not carried into this text, under correction C07: its claims were among the audit findings. The entry's status is recorded in the metadata table above as separate facts.
5. **Restoration.** The mathematical notation at §1 and §3 [C06] is the published notation, restored from the formula images' alt texts in the post's stored content. The notation is present in the published post as eleven formula images; the gaps in the PDF archive text are losses from a text-only capture of November 10, 2026, not properties of the published post.
6. **Corrections adopted from the independent review.** Two observations from GPT-6's package review, carried as reviewer flags, were taken up by the independent reviewer (GLM 5.3 Flash) with recommendations to correct, and adopted: the generalized "≤ 10% of parameters active" claim is replaced at §3 and §6 by the range the entry's own §4 figures support (under 1% to ~28%) [C08], and the estimated per-token figures for Sparsely-Gated MoE and GShard are removed at §4, their notes now stating that the papers do not give them [C09] — the † estimate's premise ("~10 experts/layer") is contradicted by Shazeer et al., whose layers ran to hundreds or thousands of experts.

##### Entry Provenance

**Credits.** Written by Qwen3-Max, ChatGPT, and Claude Sonnet 4.5; reviewed by Gemini 2.5 Pro, Grok, and DeepSeek-V3.2; corrected by Muse Spark 1.3; independently reviewed by GLM 5.3 Flash.

*The independent reviewer declared a subject interest: Mixtral, the subject of one corrected passage, is its serving vendor's model.*

<a id="aik-2025-s-p-moe"></a>

### Mixture-of-Experts (MoE) — sparse expert routing — `AIK-2025-S-P-MOE`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L1-S1 | 1991 | 2025-11-30 |

#### L1-S1 — Mixture-of-Experts (MoE) (type S)

**Date of Appearance:** as recorded for the registered S-MOE concept; not restated here  
**Public Entry ID:** `AIK-2025-S-P-MOE` · **Internal Concept ID:** AIKC-000008  
**Concept:** C:MOE, the concept of the registered S-MOE record (concept number per the live Master Register)

*As published:* **Mixture-of-Experts (MoE) — sparse expert routing** Definition: Architectures that route each input token to a small subset of “expert” sub-networks (sparse activation) so models scale capacity without linear compute cost. Why 2025: New routing mechanisms, LLM-based routers, and operational tooling made MoE a mainstream scaling strategy in 2024–2025. MoE variants are powering many high-capacity, cost-efficient models. (arXiv) Example: LLMs using adaptive expert routing and improved gating to reduce FLOPs while increasing model capacity.

**Source (corrected record):** Mu, S., & Lin, S. (2025). *A Comprehensive Survey of Mixture-of-Experts: Algorithms, Theory, and Applications.* arXiv:2503.07137, https://arxiv.org/abs/2503.07137 [C10]

<a id="aik-2025-s-p-moe-02"></a>

### Mixture of Experts (MoE) — `AIK-2025-S-P-MOE-02`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L7-K9 | 1991 | 2025-12-12 |

#### L7-K9 — Mixture of Experts (MoE) (type S)

**Date of Appearance:** 1991 (Jacobs et al.), as recorded for the registered S-MOE concept  
**Public Entry ID:** `AIK-2025-S-P-MOE-02` · **Internal Concept ID:** AIKC-000008  
**Concept:** C:MOE, shared with S-MOE and L1-S1

*As published:* **List, A-021.** • Mixture of Experts (MoE) - Efficient specialized sub-network architecture


## Mixture of Latent Experts (MoLE / MoLAE)

*Internal Concept ID AIKC-000039 · 1 record in 2025*

<a id="aik-2025-s-p-mole"></a>

### Mixture of Latent Experts (MoLE / MoLAE) — `AIK-2025-S-P-MOLE`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L1-M1 | — (not established) | 2025-11-30 |

#### L1-M1 — Mixture of Latent Experts (MoLE / MoLAE) (type S)

**Date of Appearance:** Not established. The installment frames the term as a 2025 term.  
**Public Entry ID:** `AIK-2025-S-P-MOLE` · **Internal Concept ID:** AIKC-000039  
**Concept:** C:MOLE

*As published:* **Definition:** A next-generation MoE architecture where experts share a latent transformation space, enabling much lower memory footprint and compute overhead than classic sparse MoE. **Why 2025:** Introduced in 2025 as a response to the rising operational cost of MoE deployments. **References:** • Liu, Z., et al. Beyond Standard MoE: Mixture of Latent Experts for Resource-Efficient Language Models. arXiv (2025).


## Multimodal Native Architecture

*Internal Concept ID AIKC-000012 · 1 record in 2025*

<a id="aik-2025-s-p-mmnative"></a>

### Multimodal Native Architecture — `AIK-2025-S-P-MMNATIVE`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L3-3 | — (not established) | 2025-12-02 |

*Claude Opus 5.5 is recused from this text and did not place or check it.*

#### L3-S3 — Multimodal Native Architecture (type S)

**Date of Appearance:** as published (2025 prominence). No findings.

*As published:* **Definition**: Foundation models designed from the ground up to process multiple modalities (text, image, audio, video) in a unified latent space, rather than bolting modalities onto text-first models. **Why 2025**: Models like GPT-4o and Gemini 2.0 demonstrated the advantages of native multimodal training over adapter-based approaches.


## Scaling Laws for Sparse Models & Efficiency Metrics

*Internal Concept ID AIKC-000055 · 1 record in 2025*

<a id="aik-2025-s-p-sparsescale"></a>

### Scaling Laws for Sparse Models & Efficiency Metrics — `AIK-2025-S-P-SPARSESCALE`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L1-S9 | — (not established) | 2025-11-30 |

#### L1-S9 — Scaling Laws for Sparse Models & Efficiency Metrics (type S)

**Date of Appearance:** Not established. The installment frames the term as a 2025 term.  
**Public Entry ID:** `AIK-2025-S-P-SPARSESCALE` · **Internal Concept ID:** AIKC-000055  
**Concept:** compound headword, mapped to its primary term

*As published:* **Scaling Laws for Sparse Models & Efficiency Metrics** Definition: New empirical/analytic scaling relationships describing performance vs compute for sparse (MoE/sparsely activated) architectures and composite metrics balancing latency, cost, and capability. Why 2025: Needed for design tradeoffs as organizations choose sparse vs dense scaling routes. Example: Benchmarks showing MoE outperforms dense models per-FLOP for certain tasks.


## Small Language Models (SLMs)

*Internal Concept ID AIKC-000085 · 1 record in 2025*

<a id="aik-2025-s-p-slm"></a>

### Small Language Models (SLMs) — `AIK-2025-S-P-SLM`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L4-G9 | — (not established) | 2025-12-03 |

#### L4-G9 — Small Language Models (SLMs) (type S)

**Public entry ID:** `AIK-2025-S-P-SLM` — **Concept:** SLM.
**Date of Appearance:** Not established. No factual finding; framing annotation applies.
**Contributor:** Grok 4.1. Two published short text states.

*Text 1 (as published):* **Small Language Models (SLMs)**: Compact models for specific tasks; gained 2025 momentum with regulatory compliance for on-device privacy, like NVIDIA’s research on agentic suitability. Offers efficiency over LLMs.

*Text 2 (as published):* SLMs are lightweight for targeted tasks. 2025 emphasizes privacy compliance, with models like Phi-3.5 for edge use. Example: Sentiment analysis on mobiles without cloud.

**Why It Matters in 2025**: Complements LLMs in hybrids; regulatory needs boost deployment in constrained environments.

Stands as published.

*Annotation:* the entry names a model released in August 2024 as a 2025 edge example; small language models are a pre-2025 subject, and 2025 marks prominence, not origin.


## Theoretical Learning Dynamics of MoE †

*Internal Concept ID AIKC-000049 · provisional concept identity · 1 record in 2025*

<a id="aik-2025-s-p-moetheory"></a>

### Theoretical Learning Dynamics of MoE — `AIK-2025-S-P-MOETHEORY`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L1-M11 | — (not established) | 2025-11-30 |

#### L1-M11 — Theoretical Learning Dynamics of MoE (type S)

**Date of Appearance:** Not established. The installment frames the term as a 2025 term.  
**Public Entry ID:** `AIK-2025-S-P-MOETHEORY` · **Internal Concept ID:** AIKC-000049  
**Concept:** C:MOETHEORY (provisional: research topic)

*As published:* **Definition:** Formal theory explaining how MoE models discover latent clusters, optimize expert specialization, and outperform dense models under certain distributions. **Why 2025:** 2025 ICML work provided the first provable results on MoE cluster learning. **References:** • Kawata, R., et al. Mixture of Experts Provably Detect and Learn the Latent Cluster Structure. ICML (2025).

**Why 2025 (corrected record):** Kawata et al. (ICML 2025) is among the first analyses of how MoE models learn latent cluster structure under gradient-based training; earlier theory exists (Chen et al., NeurIPS 2022). [C11]

**References (corrected record):** Kawata, R., Matsutani, K., Kinoshita, Y., Nishikawa, N., & Suzuki, T. (2025). *Mixture of Experts Provably Detect and Learn the Latent Cluster Structure in Gradient-Based Learning.* Proceedings of the 42nd International Conference on Machine Learning (ICML 2025), PMLR 267, 29390–29448. arXiv:2506.01656. Earlier theory: Chen, Z., Deng, Y., Wu, Y., Gu, Q., & Li, Y. (2022). *Towards Understanding the Mixture-of-Experts Layer in Deep Learning.* NeurIPS 2022. arXiv:2208.02813 (August 4, 2022). [C11]


## Tokenization-Centric Design

*Internal Concept ID AIKC-000069 · 1 record in 2025*

<a id="aik-2025-s-p-tokdesign"></a>

### Tokenization-Centric Design — `AIK-2025-S-P-TOKDESIGN`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L5-D9 | — (not established) | 2025-12-05 |

#### L5-D9 — Tokenization-Centric Design (type S)

**Date of Appearance:** Not established.  
**Public Entry ID:** `AIK-2025-S-P-TOKDESIGN` · **Internal Concept ID:** AIKC-000069  
**Concept:** C:TOKDESIGN

*As published:* **Table, A-017.** **Core Concept:** The philosophy that the tokenization scheme (how data is split into units) is a first-class design decision critically affecting model capabilities. **Why It's a 2025 Trend:** The focus of ICML 2025's first "TokShop" workshop, marking its emergence as a distinct research subfield. **Source Context:** ICML 2025 Workshop (TokShop)


## World Model (LLM-Integrated)

*Internal Concept ID AIKC-000026 · 2 records in 2025*

<a id="aik-2025-e-p-worldmodel"></a>

### World Model (LLM-Integrated) — `AIK-2025-E-P-WORLDMODEL`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| E / P | L2-E1 | 2018-03 (documented milestone) | 2025-12-01 |

#### L2-E1 — World Model (LLM-Integrated) (type E)

**Date of Appearance (documented milestone, not an exhaustive first use):** March 2018 for "world models" in deep learning (Ha & Schmidhuber, *World Models*, arXiv:1803.10122), with earlier uses in reinforcement learning. The "LLM-Integrated" qualifier is treated as wording  
**Public Entry ID:** `AIK-2025-E-P-WORLDMODEL` · **Internal Concept ID:** AIKC-000026  
**Concept:** C:WORLDMODEL, shared with L7-K8

*As published:* • Concept: The shift from simply predicting the next token to models that internally simulate and understand complex environments (e.g., video, physics) to plan and reason. This is distinct from AgentScen, which focuses on learning external environment dynamics. • Why 2025: Major tech companies released specific World Models in 2025, formalizing the architecture as a path toward general video generation and multi-step reasoning. **Reference (table, A-056):** Zhang, Y., et al. LMGenDrive: LLM Reasoning Meets World Models for End-to-End Driving. **Type & Source:** Conference (OpenReview 2025)

**Reference (corrected record):** None. The cited LMGenDrive paper by "Zhang, Y., et al." (OpenReview 2025) could not be found. The only work found with that name is by different authors and postdates this installment, so under the source-date rule it cannot replace the citation. [C07]

*Editorial note:* The full entry is corrected below (C03, C07, C08, C11).

#### Corrected full entry — World Model (LLM-Integrated) (L2-E1)

*Aikipedia Entry — 2025 Edition (corrected canonical text; C03, C07, C08 and C11 applied). Source text: A-074 to A-103.*

##### Definition

A World Model, in the context of Large Language Models (LLMs) and Generative AI, is an internal, learned simulation of the environment's dynamics, physics, and causal relationships. It allows the LLM to move beyond next-token prediction to reasoning through counterfactual scenarios and performing multi-step planning within the simulated world before executing an action in the real or digital environment.

##### Historical Context

World Models were initially a concept in classical reinforcement learning (RL) and deep learning for game environments (e.g., controlling an agent in a game using its internal "dream" environment). Pre-2025 LLMs largely relied on sophisticated prompting (e.g., Chain-of-Thought) and external tool-calling for planning.

In 2025, generative world models for video and multimodal simulation continued to advance: for example, Wayve's GAIA-2 (March 2025), a controllable multi-view generative world model for autonomous driving. The collection did not establish that such models were integrated within, or tightly coupled to, LLM architectures in 2025. [C11]

*(The original's "The 2025 breakthrough was the successful integration of a generative, high-fidelity World Model component within or tightly coupled to the LLM's architecture. This leap formalized the model's ability to reason about the physical world from multimodal inputs (video, sensor data), not just text." is removed. No source available by December 1, 2025 that supports it was identified, and the cited GAIA-2 report does not describe LLM integration.)* [C11]

##### Technical Description

The integrated World Model (WM) functions as a predictive simulator, often implemented as a large-scale latent variable model (LVM) that operates in a compressed, low-dimensional space.

- Observation Encoder ($E$): Compresses multimodal inputs (image, text, past actions) into a compact latent state ($z_t$). [C08]
- Transition Function ($M_{\text{wm}}$): The core WM component that predicts the next latent state ($z_{t+1}$) given the current state ($z_t$) and a proposed action ($a_t$). This is where the causal simulation occurs. [C08]
- Prediction Head ($P$): Decodes the simulated latent state back into high-fidelity future observations (e.g., next video frame, predicted sensory feedback) for evaluation. [C08]
- Planner/LLM Policy ($P_{\text{LLM}}$): The LLM component interacts with the WM by proposing actions, observing the simulated outcomes, and refining its final execution plan. [C08]

$$\text{WM-Predict}: \; z_{t+1} \approx M_{\text{wm}}(z_t, a_t)$$ [C08]

###### Core Innovations

1. Multimodal Latent Space: Learning a single latent representation space that captures the dynamics of images, text, and physics simultaneously.
2. Zero-Shot Planning: The model's ability to plan for tasks it has never been explicitly trained for by generalizing rules within its simulated world.

##### Notable Systems / Papers (2025)

- Russell, L., Hu, A., Bertoni, L., Fedoseev, G., Shotton, J., Arani, E., & Corrado, G. (2025). *GAIA-2: A Controllable Multi-View Generative World Model for Autonomous Driving.* arXiv:2503.20523 (Wayve). [C03]

*(The original lists two further items. "Zhang, Y., et al. LMGenDrive … (OpenReview 2025)" is removed: no such 2025 work was found [C07]. "OpenAI / DeepMind. Generative Agentic Intelligence Architecture Technical Report" is replaced by the item above: GAIA-2 is Wayve's, and its name expands to "Generative AI for Autonomy" [C03].)*

##### Applications

- Autonomous Systems: Provides robust, predictive planning for self-driving cars and robotics, allowing them to test safety-critical maneuvers internally before execution.
- Creative Content Generation: Enables the creation of long, causally-consistent videos and complex game environments.
- Scientific Simulation: Accelerates the modeling and prediction of complex physical, biological, or fluid dynamics.

##### Limitations

- Computational Cost: The WM's latent space is massive, leading to high latency and energy consumption during simulation.
- Simulation Drift: Errors in the model's transition function can compound over long planning horizons, leading to unrealistic or "hallucinated" outcomes.

##### Open Questions

- How can World Models be formally verified to ensure their internal physics are accurate and safe?
- Can a single WM generalize across all possible domains (physics, human social interaction, code execution)?
- How can we make the WM's internal causal reasoning interpretable for human auditing?

---

<a id="aik-2025-s-p-worldmodel"></a>

### World Models — `AIK-2025-S-P-WORLDMODEL`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L7-K8 | 2018-03 | 2025-12-12 |

#### L7-K8 — World Models (type S)

**Date of Appearance (documented milestone, not an exhaustive first use):** March 2018, as for L2-E1  
**Public Entry ID:** `AIK-2025-S-P-WORLDMODEL` · **Internal Concept ID:** AIKC-000026  
**Concept:** C:WORLDMODEL, shared with L2-E1

*As published:* **List, A-020.** • World Models - Internal environment simulations for better decision-making
