# Part III. Reasoning and Inference

## Chain-of-Thought Prompting

*Internal Concept ID AIKC-000007 · 1 record in 2025*

<a id="aik-2025-f-p-cotprompt"></a>

### Chain-of-Thought Prompting — `AIK-2025-F-P-COTPROMPT`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| F / P | standalone | 2022-01-28 | 2025-10-30 |

AIKIPEDIA · FULL-LENGTH ENTRY · CORRECTED ORIGINAL PUBLICATION

#### Chain-of-Thought Prompting

Prompting Methods · Reasoning · Evaluation

| | |
|---|---|
| **Date of Appearance** | January 28, 2022 (Wei et al., arXiv:2201.11903v1; the earliest documented use of the term identified) |
| **Date of Original Publication** | October 30, 2025 (Champaign Magazine, post 13946) |
| **Historical Coverage** | Through October 30, 2025, the date of original publication. Corrections rely only on sources available by that date |
| **Original Contributor** | Gemini 2.5 Pro (writer). Much of the final version's wording comes from ChatGPT's review (see Entry Provenance) |
| **Original Reviewers** | Grok (release not stated in the post); ChatGPT (release not stated in the post) |
| **Corrections Prepared by** | Claude Opus 5.5 (Anthropic) |
| **Independent review** | Muse Spark 1.3; DeepSeek-V4.1 |
| **Base version** | Version 3, which the post declares final (one passage of Version 2 restored at C17) |
| **Entry ID** | AIK-2025-F-P-COTPROMPT (Internal Concept ID AIKC-000007) |

*How to read this text.* This is the corrected collection text of an original 2025 publication. The original, in all three of its published versions, is preserved unchanged in the Historical Lexicon Archive. A bracketed number such as `[C07]` marks a passage changed from the original; the correction register gives the original wording, the revision and the evidence for each. `[E01]` marks an editorial addition. Unmarked text is the original's wording, rearranged into AES sections.

##### 1. Definition

Chain-of-Thought (CoT) prompting is a prompt-engineering technique for large language models that elicits intermediate reasoning steps (a "chain of thought") before producing a final answer.

##### 2. Origin and Historical Development

CoT was introduced and empirically validated in 2022 (Wei et al., 2022) [P1] and quickly became a standard tool for improving multi-step reasoning on benchmarks such as GSM8K, MATH, and multi-hop commonsense problems.

*The variants described in §3.2, in order of introduction [C14]:* Few-Shot CoT (Wei et al., 2022) [P1] · Zero-Shot CoT (Kojima et al., 2022) [P2] · Tree-of-Thoughts (ToT, 2023) [P4] · Graph-of-Thoughts (GoT, 2023) [P5] [C01] · Trace-of-Thought prompting (2024) [P7] [C04] · Chain-of-Draft (CoD, 2025 preprint) [P6] [C02].

##### 3. Conceptual or Technical Framework

###### 3.1 Core concept and mechanism

Standard prompting typically involves providing a model with a question (and sometimes a few examples) and expecting an immediate, direct answer.

*Standard prompt example:*

> Q: A juggler has 3 red balls. He buys 2 bags of blue balls. Each bag has 4 blue balls. How many balls does he have in total?
> A: 11

In contrast, Chain-of-Thought prompting demonstrates or elicits the process of reasoning.

*Chain-of-Thought prompt example (few-shot):*

> Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?
> A: Roger started with 5 balls. 2 cans of 3 balls each is 2 * 3 = 6 balls. So, 5 + 6 = 11 balls. The answer is 11.
>
> Q: A juggler has 3 red balls. He buys 2 bags of blue balls. Each bag has 4 blue balls. How many balls does he have in total?
> A: The juggler starts with 3 red balls. He buys 2 bags of blue balls. Each bag has 4 blue balls, so 2 * 4 = 8 blue balls. The total number of balls is 3 + 8 = 11 balls. The answer is 11.

By providing the intermediate steps, the model learns to "think" through the problem. This approach is believed to work because it aligns the generative process of the model with a structured, logical sequence, similar to how a human would work through a problem. CoT aligns model generation with stepwise logical structure and is especially helpful for problems that require sequential decomposition.

###### 3.2 Key variants

**Foundational variants**

- **Few-Shot CoT** (Wei et al., 2022) [P1]: Demonstrates that providing a few worked examples with detailed intermediate steps significantly improves performance on complex reasoning tasks.
- **Zero-Shot CoT / "Let's think step by step"** (Kojima et al., 2022) [P2]: Shows that appending an instruction like "Let's think step by step" can trigger reasoning behavior without exemplar demonstrations (zero-shot).

**Evolved and complex variants (2023 onward) [C01]**

- **Tree-of-Thoughts** (ToT, 2023) [P4]: Generalizes CoT by treating intermediate "thoughts" as nodes in a search tree, allowing exploration, backtracking, and look-ahead. ToT showed large gains on tasks requiring planning and search (§5).
- **Graph-of-Thoughts** (GoT, 2023) [P5]: Extends ToT by modeling reasoning as a graph (non-linear dependencies between thought nodes), providing richer combinational structures.
- **Chain-of-Draft** (CoD, 2025 preprint) [P6] [C02]: Proposes generating concise intermediate "draft" steps (much shorter than full CoT) to preserve reasoning benefits while lowering token cost and latency.
- **Trace-of-Thought prompting (2024) and related distillation methods** [P7] [C04]: Trace-of-Thought is a prompt-based form of knowledge distillation. A larger "teacher" model decomposes a problem into steps, and a smaller "student" model (up to 8 billion parameters) then follows them, without fine-tuning; it was evaluated on the GSM8K and MATH benchmarks. Related work distills reasoning from large models into smaller ones through training. These are active, rapidly evolving research directions.

##### 4. Applications and Implementations

Chain-of-Thought prompting and its derivatives are used in [C18]:

- complex question-answering systems;
- mathematical and scientific problem-solving;
- code generation and debugging;
- automated analysis of legal or financial documents;
- multimodal reasoning (e.g., generating step-by-step explanations for visual tasks);
- planning and decision-making for autonomous agents.

**When to use CoT (practical)**

- Use CoT for multi-step symbolic problems, formal math, planning, or debugging code.
- Try zero-shot "Let's think step by step" first on modern models (fast, and it needs no worked examples) [C09]. If not sufficient, test few-shot CoT.
- For production systems, measure latency and cost: consider Chain-of-Draft or distilled trace methods to reduce token use.
- Use self-consistency / voting to improve robustness when sampling multiple chains [P3].

##### 5. Evidence and Evaluation

**Improved performance [C07].** CoT dramatically improves LLM performance on tasks that were previously difficult, especially arithmetic word problems (e.g., GSM8K, MATH) [P1] [R2]. Its original evaluation also reported gains on commonsense and symbolic reasoning tasks (e.g., CSQA) [P1]. A later analysis across 14 models found the gains concentrated in math and symbolic reasoning. On commonsense and broad-knowledge benchmarks such as MMLU the gains were much smaller, and on MMLU they came mainly from questions that involve calculation [R2].

**Scalability.** The benefits of CoT prompting have been shown to scale with model size; larger models tend to produce more coherent and accurate reasoning chains [P1].

**Diminishing returns (nuanced) [C06].** Several empirical studies and technical reports since 2023–2025 indicate that the marginal benefit of explicit CoT prompting decreases for some high-capability, recent LLMs and for certain tasks.
- For advanced models applied to software-engineering tasks, prompt-engineering techniques developed for earlier models gave diminished benefits or even hindered performance [R3] [C06].
- For models with built-in reasoning, explicit CoT prompting gave marginal gains, if any, on a graduate-level question benchmark [R4] [C06].
- Advanced models often acquire stronger native reasoning and zero-shot abilities, reducing the incremental lift from CoT prompts for those tasks.

That said, this effect is task- and model-dependent. CoT remains most useful on mathematical and symbolic tasks [R2], and its variants remain valuable for long-horizon planning and complex combinatorial search [P4] [C06]. For non-reasoning models that do not reason step by step by default, explicit CoT prompting can still give small average gains [R4] [C06]. Practitioners should evaluate CoT cost/benefit per task and model.

**Table 1. Selected author-reported results from the entry's primary sources [E01].**

| Method | Setting | Reported result | Source |
|---|---|---|---|
| Zero-shot CoT | InstructGPT (text-davinci-002), "Let's think step by step" vs. plain zero-shot | MultiArith 17.7% → 78.7%; GSM8K 10.4% → 40.7% | [P2] |
| Tree-of-Thoughts | GPT-4, Game of 24 | CoT prompting solved 4% of tasks; ToT 74% | [P4] |
| Chain-of-Draft | Several reasoning benchmarks | Matched or surpassed CoT accuracy using as little as 7.6% of CoT's tokens | [P6] |
| CoT on MMLU | 14 models (meta-analysis and own evaluations) | Up to 95% of CoT's MMLU gain comes from questions containing "=" | [R2] |

*Table note:* all figures are author-reported, under the authors' stated models, prompts and scoring. They are not independent replications [E01].

##### 6. Significance and Implications

CoT quickly became a standard tool for improving multi-step reasoning (§2) [C14].

**Reasoning elicited by prompting alone.** Zero-shot CoT showed that a single instruction, with no examples, could improve reasoning across diverse tasks. Kojima et al. presented this as a hint that large models hold untapped zero-shot reasoning capabilities that simple prompting can extract [P2] [C17].

**Interpretability.** The generated chain of thought provides a readable trace of intermediate steps. This can help operators identify where a logical error occurred and audit the output. The trace is not guaranteed to reflect how the model actually reached its answer: CoT explanations can be plausible yet unfaithful [R1] (§7) [C08].

##### 7. Limitations, Debates, and Open Questions

**Limitations**

- **Computational cost.** Generating a detailed chain of thought requires more tokens and processing time (inference cost) compared to a direct answer.
- **Factual correctness.** The reasoning chain itself is a generative text sequence, not a formal logical proof. It may contain "hallucinations" or flawed logic, even if the final answer is coincidentally correct (or vice-versa).
- **Task dependency.** CoT is not a universal enhancement. For tasks that are simple or do not require multi-step reasoning, it adds unnecessary computational overhead (§5, diminishing returns).

**Safety and interpretability.** Although CoT provides a readable "reasoning trace," these sequences are model generations, not human-grade proofs. Chains may contain hallucinated or unsafe steps, and revealing internal chains can sometimes expose model-learned heuristics or biases. For high-stakes uses, combine CoT with external verification (symbolic checks, unit tests, or formal verification) and treat chains as hypotheses to be validated rather than ground truth.

##### 8. Related Concepts and Distinctions

- **Self-Consistency.** A technique (Wang et al., 2022) [P3] often used with CoT, where the model generates multiple reasoning chains and the final answer is chosen by a majority vote, improving robustness.
- **Tree-of-Thoughts (ToT).** See §3.2. Code repository listed with [P4] [C11].
- **Graph-of-Thoughts (GoT).** See §3.2. Code repository listed with [P5] [C11].
- **Active Prompting.** An extension that selects which questions to annotate with worked chains of thought [P8] [C12].

##### See Also

General concepts with no entry in the 2025 collection [C16]: Prompt Engineering · In-Context Learning · Large Language Model (LLM) · Self-Consistency (AI) · Tree-of-Thoughts · Graph-of-Thoughts · Active Prompting.

Related records in the Aikipedia 2025 collection (editorial cross-references, not part of the original) [C16]:
- **Chain-of-Thought Monitorability.** New addition, AIK-2025-F-N-COTMONITOR.
- **Chain-of-Verification (CoVe).** *New AI Lexicon 2025* (3) (Dec 2, 2025); AIK-2025-S-P-COVE.
- **Test-Time Compute Scaling.** *New AI Lexicon 2025* (3) (Dec 2, 2025); AIK-2025-E-P-TTCSCALE.

##### References and Sources

**Primary Sources** [C10]

- [P1] Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. *Advances in Neural Information Processing Systems 35* (NeurIPS 2022), 24824–24837. arXiv:2201.11903 (v1 January 28, 2022). https://arxiv.org/abs/2201.11903
- [P2] Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., & Iwasawa, Y. (2022). Large Language Models are Zero-Shot Reasoners. NeurIPS 2022. arXiv:2205.11916 (v1 May 24, 2022). https://arxiv.org/abs/2205.11916
- [P3] Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery, A., & Zhou, D. (2022). Self-Consistency Improves Chain of Thought Reasoning in Language Models. ICLR 2023. arXiv:2203.11171 (v1 March 21, 2022). https://arxiv.org/abs/2203.11171 [C10]
- [P4] Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., & Narasimhan, K. (2023). Tree of Thoughts: Deliberate Problem Solving with Large Language Models. NeurIPS 2023. arXiv:2305.10601 (v1 May 17, 2023). https://arxiv.org/abs/2305.10601 ; code: https://github.com/princeton-nlp/tree-of-thought-llm [C11]
- [P5] Besta, M., Blach, N., Kubicek, A., Gerstenberger, R., Podstawski, M., Gianinazzi, L., Gajda, J., Lehmann, T., Niewiadomski, H., Nyczyk, P., & Hoefler, T. (2024). Graph of Thoughts: Solving Elaborate Problems with Large Language Models. *Proceedings of the AAAI Conference on Artificial Intelligence* 38(16), 17682–17690. arXiv:2308.09687 (v1 August 18, 2023). https://arxiv.org/abs/2308.09687 ; code: https://github.com/spcl/graph-of-thoughts [C11]
- [P6] Xu, S., Xie, W., Zhao, L., & He, P. (2025). Chain of Draft: Thinking Faster by Writing Less. arXiv:2502.18600 (v1 February 25, 2025). Preprint. https://arxiv.org/abs/2502.18600 [C02]
- [P7] McDonald, T., & Emami, A. (2024). Trace-of-Thought Prompting: Investigating Prompt-Based Knowledge Distillation Through Question Decomposition. *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 4: Student Research Workshop)*, 293–306. https://doi.org/10.18653/v1/2024.acl-srw.35 ; also arXiv:2504.20946 (2025) [C03]
- [P8] Diao, S., Wang, P., Lin, Y., Pan, R., Liu, X., & Zhang, T. (2024). Active Prompting with Chain-of-Thought for Large Language Models. *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, 1330–1350. https://doi.org/10.18653/v1/2024.acl-long.73 ; also arXiv:2302.12246 (v1 February 23, 2023). https://arxiv.org/abs/2302.12246 [C12]

**Additional References**

- [R1] Turpin, M., Michael, J., Perez, E., & Bowman, S. R. (2023). Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting. NeurIPS 2023. arXiv:2305.04388 (v1 May 7, 2023). https://arxiv.org/abs/2305.04388 [C08]
- [R2] Sprague, Z., Yin, F., Rodriguez, J. D., Jiang, D., Wadhwa, M., Singhal, P., Zhao, X., Ye, X., Mahowald, K., & Durrett, G. (2024). To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning. ICLR 2025. arXiv:2409.12183 (v1 September 18, 2024). https://arxiv.org/abs/2409.12183 [C05, C07]
- [R3] Wang, G., Sun, Z., Gong, Z., Ye, S., Chen, Y., Zhao, Y., Liang, Q., & Hao, D. (2024). Do Advanced Language Models Eliminate the Need for Prompt Engineering in Software Engineering? arXiv:2411.02093 (November 4, 2024). https://arxiv.org/abs/2411.02093 [C05]
- [R4] Meincke, L., Mollick, E., Mollick, L., & Shapiro, D. (2025). Prompting Science Report 2: The Decreasing Value of Chain of Thought in Prompting. Wharton School Research Paper. arXiv:2506.07142 (June 8, 2025); SSRN 5285532. https://arxiv.org/abs/2506.07142 [C05]

##### Editorial Notes

1. **Status of this text.** Independently reviewed and accepted by the editor. The historical publication is not replaced; it stays in the Historical Lexicon Archive. The dated record is in Appendix G.
2. **Base version.** The original post publishes three versions. This text is based on the third, which the post declares final. One passage of the second version is restored in §6 [C17], with its wording aligned to the source's hedge.
3. **Source-date rule.** Every source used to correct the historical body was available by October 30, 2025, the original publication date; the latest is [R4], June 8, 2025. No later development has been added.
4. **Qualified claim.** The original said CoT "remains valuable … when working with smaller or mid-sized models." It gave no source. Its own primary source found no gain, or harm, below about 100 billion parameters for the 2022 models it tested [P1]. A 2025 study [R4] found small average gains for non-reasoning models that do not reason step by step by default. That study grouped models by reasoning behavior, not size. The claim is therefore restated in the form the sources support, and the size wording is not retained [C06]. The editor adopted this wording.
5. **Proposed substitutions.** [R2] and [R4] stand in for the original's unspecified "related technical reports" [C05]. They are the preparer's choice, not the original's. The editor accepted them.
6. **Worked example.** The tennis-ball exemplar in §3.1 follows the exemplar in Wei et al.'s Figure 1 with light rewording. The juggler problem is the original contributor's own.
7. **Precursors.** Later literature cites Nye et al. (2021, "scratchpads") alongside Wei et al. as an origin of the technique; see, for example, [R1]. That precursor is noted here but not added to the historical body.
8. **Editorial addition.** Table 1 [E01] is not in the original. It quotes author-reported figures from the entry's own sources so that §5 states evaluation conditions, as AES §5 requires. The editor ruled to keep it, as a labeled addition.
9. **Affiliation note.** Two authors of [R1] list Anthropic affiliations, and the corrections were prepared by an Anthropic model. That correction [C08] was therefore checked independently: Muse Spark 1.3 found it warranted, and DeepSeek-V4.1 confirmed it at the primary record. DeepSeek's check of the affiliations themselves was at register level only.
10. **Application list.** The original called CoT "a standard technique in" the six areas listed in §4 but gave no source for any of them. On the editor's ruling, the list is kept and the phrase is changed to "used in" [C18]. The text therefore no longer asserts, without a source, that the practice is standard.

##### Credits

- Source audit and corrections: Claude Opus 5.5.
- Independent verification: Muse Spark 1.3. Further independent review, with a primary-source check: DeepSeek-V4.1.

Accepted by the editor, W.H.L. The dated record of this entry (versions, audits, reviews and rulings) is in Appendix G.

## Chain-of-Verification (CoVe)

*Internal Concept ID AIKC-000021 · 1 record in 2025*

<a id="aik-2025-s-p-cove"></a>

### Chain-of-Verification (CoVe) — `AIK-2025-S-P-COVE`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L3-12 | 2023-09 | 2025-12-02 |

*Claude Opus 5.5 is recused from this text and did not place or check it.*

#### L3-S12 — Chain-of-Verification (CoVe) (type S)

**Date of Appearance:** 2023 *(corrected — C02; Dhuliawala et al., arXiv:2309.11495, September 2023)*
**Headword note:** published as "Chain-of-Verification (CoV)"; the paper's abbreviation is **CoVe**, used here.

*As published:* **Definition**: Method where models generate initial responses, then systematically verify claims through self-questioning and evidence gathering to reduce hallucinations. **Why 2025**: Became a standard technique for improving factual accuracy in high-stakes applications like medical and legal domains.

*Editorial note:* first appearance is 2023 (ACL 2024 Findings); the correction concerns the stated date and abbreviation, not the term's inclusion.

---


## Controllable Generation Frameworks

*Internal Concept ID AIKC-000017 · 1 record in 2025*

<a id="aik-2025-s-p-ctrlgen"></a>

### Controllable Generation Frameworks — `AIK-2025-S-P-CTRLGEN`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L3-8 | as published (2025) | 2025-12-02 |

*Claude Opus 5.5 is recused from this text and did not place or check it.*

#### L3-S8 — Controllable Generation Frameworks (type S)

**Date of Appearance:** as published. No findings.

*As published:* **Definition**: Structured approaches for fine-grained control over generative model outputs through semantic steering, attribute manipulation, and constraint satisfaction. **Why 2025**: Moved beyond simple prompting to enable precise creative control in image, video, and text generation.


## KV-Cache Sharing (On-Device Inference)

*Internal Concept ID AIKC-000027 · 1 record in 2025*

<a id="aik-2025-e-p-kvshare"></a>

### KV-Cache Sharing (On-Device Inference) — `AIK-2025-E-P-KVSHARE`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| E / P | L2-E2 | — (not established) | 2025-12-01 |

#### L2-E2 — KV-Cache Sharing (On-Device Inference) (type E)

**Date of Appearance:** Not established.  
**Public Entry ID:** `AIK-2025-E-P-KVSHARE` · **Internal Concept ID:** AIKC-000027  
**Concept:** C:KVSHARE

*As published:* • Concept: A critical optimization technique that allows multiple models or tasks on a device (like a smartphone) to access the same Key-Value (KV) cache in memory, significantly reducing the memory and latency overhead for simultaneous LLM operations. • Why 2025: Became a core architectural innovation for enabling powerful, multi-functional on-device foundation models (like those detailed in the 2025 Apple Intelligence report). **Reference (table, A-057):** Ma, B., et al. SafeKV: Selective KV-Cache Sharing to Mitigate Timing Side-Channels in LLM Inference. **Type & Source:** Preprint (arXiv 2025)

**Why 2025 (corrected record):** The 2025 Apple Intelligence report describes KV-cache sharing in Apple's ~3B-parameter on-device model, where the second of two blocks reuses the KV cache of the first, cutting KV-cache memory and time-to-first-token by about 37.5% (Apple, *Apple Intelligence Foundation Language Models: Tech Report 2025*, arXiv:2507.13575, July 2025). That is sharing within one model, not across tasks or models. [C06]

**Reference (corrected record):** Chu, K., et al. (2025). *SafeKV: Selective KV-Cache Sharing to Mitigate Timing Side-Channels in LLM Inference.* arXiv:2508.08438. [C07]

*Editorial note:* The full entry is corrected below (C06, C07, C08, C12).

#### Corrected full entry — KV-Cache Sharing (On-Device Inference) (L2-E2)

*Aikipedia Entry — 2025 Edition (corrected canonical text; C06, C07, C08 and C12 applied). Source text: A-134 to A-160.*

##### Definition

KV-Cache Sharing is a resource optimization technique used primarily in the deployment of Large Language Models (LLMs) on multi-tenant or memory-constrained edge hardware (like personal devices). It allows the intermediate attention computation outputs, specifically the Key (K) and Value (V) vectors (the KV-Cache), to be shared or reused across multiple concurrent inference sessions, tasks, or users, drastically reducing memory bandwidth and latency.

The term is also used for reuse of the KV cache across layers or blocks within a single model, as in Apple's 2025 on-device model (see Historical Context). [C06]

##### Historical Context

The KV-Cache, essential for efficient auto-regressive generation, is the largest memory consumer during inference. Its size limited the context length and the number of users a server could support. Early sharing methods (pre-2025) focused on sharing common prefixes (like the system prompt) on large server farms.

In 2025, Apple's ~3B-parameter on-device foundation model used a within-model form of KV-cache sharing: the model is divided into two blocks, and the second block reuses the KV cache generated by the first. Apple reports this cuts KV-cache memory use and time-to-first-token by about 37.5% (Apple, *Tech Report 2025*, arXiv:2507.13575). [C06]

*(The original's "The 2025 breakthrough applied this to on-device (local) inference, particularly for devices running multiple, small LLM-powered services simultaneously …" is replaced. The cited Apple report describes sharing within one model, not across services, and no Qualcomm report was identified.)* [C06]

##### Technical Description

The KV-Cache stores the K and V vectors for all previously generated tokens. In a shared system, the cache memory is managed by a centralized scheduler (often integrated into the GPU's memory manager):

- Chunking/Paging: The cache is divided into fixed-size chunks or "pages" (e.g., 16 tokens).
- Shared/Private Mapping: A router determines if a request's tokens should be mapped to an existing, shared cache chunk (if the chunk is read-only and non-sensitive) or allocated a new, private chunk.
- Inference Acceleration: When a user's prompt or a sub-task uses a sequence already in the shared cache, the LLM skips the expensive attention computation for those tokens, immediately retrieving the required K and V vectors.

*(The original's memory-reduction formula, "Memory Reduction ≈ Σ_{i∈Shared} S_i·N_i·2·D / B", and the sentence defining its variables are removed. The formula has no source, and its terms do not yield a memory quantity: it omits the number of layers and the bytes per element, it counts sharers rather than the copies avoided, and its division by batch size is unexplained.)* [C12]

##### Notable Systems / Papers (2025)

- Chu, K., et al. (2025). *SafeKV: Selective KV-Cache Sharing to Mitigate Timing Side-Channels in LLM Inference.* arXiv:2508.08438. [C07]
- Apple (2025). *Apple Intelligence Foundation Language Models: Tech Report 2025.* arXiv:2507.13575. [C06]

*(The original's "Apple Intelligence / Qualcomm Technical Reports on On-Device LLM Optimization. (2025)" is replaced by the Apple report above. The Qualcomm half could not be identified.)* [C06]

##### Applications

- Real-time Multitasking: Enables a single device to run a background agent (reading email) and a foreground chat assistant concurrently without latency spikes.
- Cost-Efficient Cloud Serving: Drastically reduces the GPU memory footprint for large, multi-tenant cloud-based LLM APIs, lowering the cost-per-token for providers.
- Personalization: Allows a base model's knowledge to be shared while specialized, personalized adapters and their unique KV-Cache entries are managed privately.

##### Limitations

- Privacy Leakage (Side Channels): Sharing can introduce side-channel vulnerabilities (e.g., PromptPeek), where a malicious process can observe timing differences in cache hits/misses to infer the prompt content of another concurrent user.
- Cache Invalidation: Managing when and how to clear a shared cache (e.g., due to model updates or security concerns) is complex.

##### Open Questions

- What is the optimal chunking size to balance efficiency gains against side-channel risk?
- How can Homomorphic Encryption or other cryptographic methods be applied to the KV-Cache to enable sharing without exposing plaintext data?
- Can a learning-based privacy classifier reliably and efficiently partition the cache into safe-to-share and private sections?

---


## Multi-Agent Debate Systems

*Internal Concept ID AIKC-000015 · 1 record in 2025*

<a id="aik-2025-s-p-madebate"></a>

### Multi-Agent Debate Systems — `AIK-2025-S-P-MADEBATE`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L3-6 | 2023-05 | 2025-12-02 |

*Claude Opus 5.5 is recused from this text and did not place or check it.*

#### L3-S6 — Multi-Agent Debate Systems (type S)

**Date of Appearance:** May 2023 *(corrected — C03; Du et al., arXiv:2305.14325)*

*As published:* **Definition**: Frameworks where multiple AI agents argue different positions or perspectives before reaching a conclusion, improving reasoning quality and reducing bias. **Why 2025**: Emerged as a practical technique for complex decision-making and fact-checking applications.

*Editorial note:* first appearance is 2023; 2025 marks wider adoption and formalization.


## Prefill–Decode Disaggregation

*Internal Concept ID AIKC-000023 · 1 record in 2025*

<a id="aik-2025-f-p-pddisagg"></a>

### Prefill–Decode Disaggregation — `AIK-2025-F-P-PDDISAGG`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| F / P | standalone | 2024-01-18 | 2025-11-09 |

#### Prefill–Decode Disaggregation

*Corrected collection text. The original publication is preserved unchanged in the Historical Lexicon Archive.*

| Field | Value |
|---|---|
| **Term** | Prefill–Decode Disaggregation |
| **Date of Appearance** | January 18, 2024 (Zhong et al., DistServe, arXiv:2401.09670v1, "Disaggregating Prefill and Decoding"). The technique appeared earlier as "phase splitting": Patel et al., Splitwise, arXiv:2311.18677v1, November 30, 2023. Earliest documented use identified; not an exhaustive priority claim |
| **Date of Original Publication** | November 9, 2025 (Champaign Magazine, post 14033) |
| **Historical Coverage** | Through November 9, 2025, the date of original publication. Corrections rely only on sources available by that date |
| **Original Contributor** | Kimi K2 Thinking (initial draft, linked from the post, not reproduced in it); ChatGPT (revised and final versions) |
| **Original Reviewers** | Grok Expert; Claude 4.5 Sonnet; Gemini 2.5 Pro (named in the post; no review texts are published) |
| **Corrections Prepared by** | Claude Opus 5.5 (Anthropic) |
| **Independent review** | GLM 5.3 Flash |
| **Base version** | Sole published version on the post (post 14033). The off-post Kimi text linked from the post is a provenance annotation, not a version (rulings X9/X15) |
| **Entry ID** | AIK-2025-F-P-PDDISAGG (concept AIKC-000023) |

*Markers: `[Cnn]` marks a corrected or added passage and `[ST01]` the rearrangement into AES sections, documented in the entry's correction register. Unmarked text is the original's own wording (archive lines A-007 to A-083).*

##### 1. Definition

Prefill–decode disaggregation optimizes large language model (LLM) inference by separating the prefill phase (parallel prompt processing) from the decode phase (sequential token generation), enabling tailored hardware allocation and independent scaling for each phase. [ST01]

##### 2. Origin and Historical Development

First proposed in Splitwise (2023), which splits prompt computation and token generation onto separate machines [8], and formalized as goodput-optimized disaggregated serving in DistServe (2024) [1], this approach has evolved rapidly with systems like Mooncake, FlowKV, and NVIDIA Dynamo addressing KV cache transfers, scheduling, and production-scale deployment. [C01] [ST01]

###### History / Development Timeline [C01] [C06]

| Year | Event |
|---|---|
| **Late 2023** | Splitwise (Microsoft; arXiv:2311.18677, ISCA 2024) splits prompt and token-generation phases onto separate machines. |
| **2024 (OSDI)** | DistServe formalizes disaggregation; first goodput gains observed. |
| **Late 2024** | vLLM/Ray prototypes emerge. |
| **Early 2025 (FAST ’25)** | Mooncake published; KV-centric orchestration demonstrated. |
| **March 2025 (GTC)** | NVIDIA Dynamo launched; vendor-grade distributed inference framework. |
| **April 2025** | FlowKV arXiv release; low-latency KV transfer and scheduling. |
| **Mid-2025** | Dynamo v0.4 introduces Blackwell optimizations. |

##### 3. Conceptual or Technical Framework

###### 3.1 Overview

LLM inference involves:

- **Prefill:** Parallel, compute-intensive matrix operations for prompt embeddings.
- **Decode:** Sequential token generation using KV cache accesses, memory-bound and lower arithmetic intensity.

Disaggregation assigns these phases to separate clusters:

- **Compute-optimized clusters** for prefill.
- **Memory-optimized clusters** for decode.

Clusters communicate via high-speed interconnects (e.g., NVLink, InfiniBand) to transfer KV cache states efficiently. Utilization differences are typical: prefill >90%, decode 20–40% GPU utilization, as reported in technical analyses of disaggregated serving [9]. [C02]

Monolithic serving mixes prefill and decode, causing idle hardware. [ST01]

###### 3.2 KV-Cache Transfer

Efficient KV cache transfer is critical:

- **FlowKV:** ~96% reduction in KV-cache transmission latency (from 0.944 s to 0.053 s), achieved by optimizing the transfer itself (layer-wise pipelined transfer and contiguous memory allocation) rather than by compressing the cache [2]. [C03]
- **Mooncake:** pools the GPU cluster's underused CPU, DRAM, SSD and NIC resources into a disaggregated, KVCache-centric store, with a global scheduler that pairs prefill and decode instances [3]. [C09]

###### 3.3 Scheduling and Load Balancing

Dynamic routing and admission control (e.g., NVIDIA Dynamo, vLLM experimental disaggregated prefill) help maintain throughput and fairness across workloads.

###### 3.4 Figure 1 (original)

*The image (post attachment 14035, file `copilot_20251109_162736.png`) is kept in the archive; its file name indicates it was generated with Microsoft Copilot. The post gives it no credit line.* [C08] Architecture diagram:

1. **Prefill Clusters:** Input prompt processed via parallel compute.
2. **KV Cache Stream:** Optimized KV transfer (compressed tensors) moves data between prefill and decode.
3. **Decode Clusters:** Sequential token generation using KV cache.
4. **Measurements:** TTFT and ITL monitored at each phase.

##### 4. Applications and Implementations

- Powers deployments like Kimi (Mooncake) and DeepSeek-V3.

##### 5. Evidence and Evaluation

Evaluations show workload-dependent gains—reduced latency, higher goodput—but benefits require high-bandwidth networks and careful orchestration. [ST01]

Phase-specific batching improves Time to First Token (TTFT) and Inter-Token Latency (ITL): [C04]

- **DistServe:** up to 7.4× more requests or 12.6× tighter SLOs.
- **Mooncake:** 59–498% capacity gains.
- **FlowKV:** 15.2–48.9% speedups on LongBench v1/v2 benchmarks.

Cost efficiency varies: Splitwise reports 1.4× higher throughput at 20% lower cost, or 2.35× more throughput under the same cost and power budgets [8]; secondary technical analyses cite 15–40% reductions in infrastructure cost [9]. [C05]

Metrics include TTFT, ITL, throughput, P99 latency, tested on H100/A800 clusters using LongBench v1/v2 for long-context evaluation.

##### 6. Significance and Implications

Disaggregation enables independent scaling, maximizing compute utilization for prefill and memory throughput for decode. Bursty workloads benefit most. [ST01]

##### 7. Limitations, Debates, and Open Questions

Disaggregation relies on high-bandwidth fabrics. Slow networks can erode gains, particularly in heterogeneous setups. Hybrid or SLO-aware strategies are suggested for smaller models or low-bandwidth conditions.

Disaggregation is less effective for:

- Small models or short-context inference.
- Poor network bandwidth.
- Uniform workloads (hybrid aggregation-disaggregation may be better).

- **Future directions:** SLO-aware autoscaling, heterogeneous hardware support, intra-GPU disaggregation. [ST01]

##### 8. Related Concepts and Distinctions

- Complements paged attention, speculative decoding, MoE, KV cache offloading, and chunked prefill.

##### See Also

*Cross-reference markings (editorial, not part of the original): targets in the collection carry their Public Entry IDs; the others are marked as having no entry.*

- Model parallelism (tensor/pipeline) — *no entry in the 2025 collection*
- Mixture of Experts (MoE) — AIK-2025-F-P-MOE (standalone), with occurrences AIK-2025-S-P-MOE and AIK-2025-S-P-MOE-02
- Paged attention (vLLM) — *no entry in the 2025 collection*
- Speculative decoding — AIK-2025-S-P-SPECDECODE (*New AI Lexicon 2025* (3))
- KV cache offloading — *no entry in the 2025 collection* (related: KV-Cache Sharing, AIK-2025-E-P-KVSHARE)
- Chunked prefill — *no entry in the 2025 collection*

##### References and Sources

1. **DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving** – arXiv:2401.09670, OSDI 2024.
2. **FlowKV: A Disaggregated Inference Framework with Low-Latency KV Cache Transfer and Load-Aware Scheduling** – arXiv:2504.03775, 2025.
3. **Mooncake: Trading More Storage for Less Computation — A KVCache-centric Architecture for Serving LLM Chatbot** (Qin et al.) – USENIX FAST 2025. https://www.usenix.org/system/files/fast25-qin.pdf [C07]
4. **NVIDIA Dynamo: A Low-Latency Distributed Inference Framework for Scaling Reasoning AI Models** – NVIDIA Blog, March 2025.
5. **LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding** – GitHub (https://github.com/THUDM/LongBench).
6. **vLLM Documentation: Disaggregated Prefilling (Experimental)** – vLLM Docs (https://docs.vllm.ai/).
7. **Disaggregated Inference: 18 Months Later** – Hao AI Lab retrospective (https://hao-ai-lab.github.io/blogs/distserve-retro/).
8. **Splitwise: Efficient Generative LLM Inference Using Phase Splitting** (Patel et al.) – arXiv:2311.18677 (November 30, 2023), ISCA 2024. [C01]
9. **Disaggregation in Large Language Models: the Next Evolution in AI Infrastructure** – InfoQ article (September 29, 2025). https://www.infoq.com/articles/llms-evolution-ai-infrastructure/ [C02]

##### Editorial Notes

1. **Status.** Independently reviewed and accepted by the editor. The dated record is in Appendix G.
2. **Source-date rule.** Every source used to correct the text was available by November 9, 2025: Splitwise (November 30, 2023), the DistServe OSDI version (June 2024), FlowKV (April 2025), the Mooncake FAST '25 paper (February 2025), and the InfoQ article (September 29, 2025).
3. **Provenance.** The post links the initial Kimi K2 Thinking draft (A-084); the link is not carried into the entry. The figure's file name indicates Microsoft Copilot as its generator; the post credits no one for it (C08). No review texts are published in the post, so Review Applied? cannot be assessed.
4. **Figure legend.** Item 2 of the legend ("compressed tensors", A-064) describes KV transfer generically and is left as published. It is not a claim about FlowKV, whose mechanism is corrected at C03.
5. **Conflict.** The preparer is an Anthropic model, and the post names Claude 4.5 Sonnet as a peer reviewer. No Claude text appears in the post.

##### Credits

- Source audits: Claude Opus 5.5 (first audit) and Muse Spark 1.3 (second audit).
- Corrections: Claude Opus 5.5.
- Independent review: GLM 5.3 Flash.

Accepted by the editor, W.H.L. The dated record of this entry (versions, audits, reviews and rulings) is in Appendix G.

## Quantization & Ultra-Low-Precision Inference

*Internal Concept ID AIKC-000054 · 1 record in 2025*

<a id="aik-2025-s-p-quantinfer"></a>

### Quantization & Ultra-Low-Precision Inference — `AIK-2025-S-P-QUANTINFER`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L1-S8 | — (not established) | 2025-11-30 |

#### L1-S8 — Quantization & Ultra-Low-Precision Inference (type S)

**Date of Appearance:** Not established. The installment frames the term as a 2025 term.  
**Public Entry ID:** `AIK-2025-S-P-QUANTINFER` · **Internal Concept ID:** AIKC-000054  
*As published:* **Quantization & Ultra-Low-Precision Inference** Definition: Techniques (4-bit, 3-bit, mixed precision) and quant-aware training to run large models on commodity hardware without big accuracy loss. Why 2025: Widespread use in open-source and commercial models to reduce inference cost and enable edge deployment. Example: Post-training quantization + fine-tuning to run a 70B-equivalent model on a single server.


## Speculative Decoding

*Internal Concept ID AIKC-000016 · 1 record in 2025*

<a id="aik-2025-s-p-specdecode"></a>

### Speculative Decoding — `AIK-2025-S-P-SPECDECODE`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L3-7 | 2022-11-30 | 2025-12-02 |

*Claude Opus 5.5 is recused from this text and did not place or check it.*

#### L3-S7 — Speculative Decoding (type S)

**Date of Appearance:** November 30, 2022 *(corrected — C01; Leviathan, Kalman & Matias, arXiv:2211.17192; Chen et al., arXiv:2302.01318, February 2023)*

*As published:* **Definition**: Inference optimization technique where a small "draft" model generates candidate tokens that a larger model verifies in parallel, dramatically reducing latency. **Why 2025**: Became standard in production systems as latency requirements tightened for interactive applications.

*Editorial note:* the technique predates 2025; its 2025 relevance is production standardization, as the short form's own text describes.


## Test-Time Compute Scaling

*Internal Concept ID AIKC-000011 · 1 record in 2025*

<a id="aik-2025-e-p-ttcscale"></a>

### Test-Time Compute Scaling — `AIK-2025-E-P-TTCSCALE`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| E / P | L3-2 | 2024–2025 | 2025-12-02 |

*Claude Opus 5.5 is recused from this text and did not place or check it.*

#### L3-S2 — Test-Time Compute Scaling (type E)

**Date of Appearance:** 2024–2025 (crystallization; OpenAI o1, September 2024 — as the entry itself records). No appearance correction.

*As published:* **Definition**: Methods that improve model performance by allocating more computational resources during inference (e.g., longer reasoning chains, more sampling attempts) rather than only during training. **Why 2025**: Became a key alternative to pre-training scaling as models like o1 demonstrated dramatic improvements through inference-time computation.

*Note:* the full entry is corrected at C06 (restoration — Mathematical Framework equations restored from the published formulas) — see below.

#### Corrected full entry — Test-Time Compute Scaling (L3-S2)

**Aikipedia Entry — 2025 Edition** *(corrected canonical text; correction C06 applied, marked [C06])*

##### Definition

Test-Time Compute Scaling refers to methods that improve AI model performance by allocating additional computational resources during inference rather than only during training. Instead of generating responses immediately, models invest extra time in iterative reasoning, self-correction, verification, and exploration of multiple solution paths before producing final outputs.

##### Historical Context

Traditional language models operated on a simple paradigm: generate outputs as quickly as possible using fixed inference budgets. Pre-training scaling laws dominated the field from 2018–2024, with performance improvements achieved primarily by training larger models on more data.

In September 2024, OpenAI released the o1 model series, which demonstrated that performance consistently improves with more time spent thinking during inference. This marked a fundamental shift: as the field encountered data bottlenecks and diminishing returns from pre-training scaling laws, test-time compute emerged as a key driver of performance improvements.

By early 2025, the paradigm had crystallized with models like DeepSeek-R1 exploring reinforcement learning approaches to achieve strong reasoning through deep, step-by-step thinking. Multiple research groups published frameworks for achieving test-time scaling, making it accessible beyond closed proprietary systems.

##### Technical Description

Test-time compute encompasses several interconnected approaches: **1. Extended Chain-of-Thought (CoT) Reasoning**

Models generate explicit reasoning traces before producing answers, allowing them to work through complex multi-step problems systematically.

**2. Iterative Self-Refinement**

The model generates an initial response, critiques it, identifies errors, and produces improved versions through multiple refinement cycles.

**3. Best-of-N Sampling with Verification**

- Generate N candidate solutions
- Evaluate each using a reward model (Outcome-Supervised Reward Model for complete solutions, or Process-Supervised Reward Model for step-by-step evaluation)
- Select the highest-scoring response

**4. Tree Search Strategies**

Models explore multiple reasoning paths simultaneously, backtrack when needed, and search for optimal solutions through the space of possible reasoning chains.

**5. Budget Forcing**

A technique that controls test-time compute by forcefully terminating or lengthening the model's thinking process by appending "Wait" tokens multiple times, leading the model to double-check its answer and often fix incorrect reasoning steps.

##### Mathematical Framework

For a model policy π and input x, traditional inference produces:

y = π(x)

Test-time scaling introduces compute budget C:

y = argmax_{y ∈ 𝒴(x, C)} R(y)

where 𝒴(x, C) is the set of candidate responses generated using compute budget C, and R is a reward/verification function. [C06 — equations restored from the published formulas (the formula images' alt texts in the stored post)]

The performance of o1 consistently improves with more reinforcement learning (train-time compute) and with more time spent thinking (test-time compute).

##### Notable Systems / Papers (2025)

- **OpenAI o1 & o3**: Proprietary reasoning models that demonstrated dramatic improvements on challenging benchmarks through extended thinking time
- **s1 (Muennighoff et al., 2025)**: Achieved test-time scaling with just 1,000 training examples and budget forcing, exceeding o1-preview on competition math by up to 27%
- **DeepSeek-R1**: Leveraged reinforcement learning to achieve strong reasoning through step-by-step thinking
- **Survey by Ji et al. (2025)**: Comprehensive review organizing test-time compute from System-1 to System-2 thinking paradigms
- **Zeng et al. (ACL 2025)**: Found that parallel scaling strategies outperform sequential ones, proposing "Shortest Majority Vote" method

##### Applications

- **Mathematical Problem Solving**: o1 achieved 93% on AIME 2024 when 1,000 samples per problem were reranked with a learned scoring function (74% for a single sample; 83% for consensus among 64 samples), placing it among the top 500 students nationally[C07 — the 93% figure is qualified with the selection procedure that produced it; a single sample scored 74% and consensus among 64 samples 83% (OpenAI, "Learning to reason with LLMs," September 12, 2024); original: "o1 achieved 93% on AIME 2024 with extended inference, placing it among the top 500 students nationally"]
- **Scientific Reasoning**: Outperforming PhD-level experts on specialized knowledge benchmarks
- **Code Generation**: Testing and iteratively improving generated code before returning results
- **Multi-Step Planning**: Breaking complex tasks into verified sub-steps with correction loops
- **Safety-Critical Decisions**: Medical diagnosis, legal analysis where accuracy matters more than speed

##### Limitations

- **Increased Latency**: Users must wait longer for responses, unsuitable for real-time applications
- **Higher Computational Cost**: More expensive to run, requiring careful cost-quality tradeoffs
- **Diminishing Returns**: Research shows that longer chains of thought don't always enhance accuracy; correct solutions are often shorter than incorrect ones
- **Verification Challenges**: Reward models can be incorrect, and verifying complex reasoning remains difficult
- **Not Universal**: Benefits concentrated in reasoning-heavy domains; less effective for simple retrieval or classification

##### Open Questions

- How do we design optimal compute allocation strategies that balance quality, cost, and latency?
- Can we predict in advance which problems will benefit most from additional test-time compute?
- How do we ensure that extended reasoning actually improves reliability rather than generating elaborate but incorrect justifications?
- What are the theoretical limits of test-time scaling compared to pre-training scaling?
- How should test-time compute interact with other techniques like retrieval-augmented generation?

---
