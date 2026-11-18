# Part V. Agents, Tools and Applications

## Agentic AI

*Internal Concept ID AIKC-000052 · 2 records in 2025*

<a id="aik-2025-e-p-agenticai"></a>

### Agentic AI / Super-Agents / Model Orchestration — `AIK-2025-E-P-AGENTICAI`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| E / P | L1-S5 | — (not established) | 2025-11-30 |

#### L1-S5 — Agentic AI / Super-Agents / Model Orchestration (type E)

**Date of Appearance:** Not established. The installment frames the term as a 2025 term. Agentic systems predate 2025 (corrected full entry below)  
**Public Entry ID:** `AIK-2025-E-P-AGENTICAI` · **Internal Concept ID:** AIKC-000052  
**Concept:** C:AGENTIC

*As published:* **Agentic AI / Super-Agents / Model Orchestration** Definition: Systems that chain models, tools, and planners into autonomous agents that plan, call tools, and execute multi-step tasks across APIs and services. Why 2025: 2025 saw strong industry attention to agentic workflows (enterprise automation, assistants that act), plus new governance and safety discussions. (IT Pro) Example: An agent that reads a contract, extracts tasks, queries APIs, and drafts follow-up emails.

**Source (corrected record):** IT Pro, "Practical AI: the age of agentic AI", https://www.itpro.com/technology/artificial-intelligence/practical-ai-the-age-of-agentic-ai [C10]

*Editorial note:* Full entry corrected at C09 (below).

#### Corrected full entry — Agentic AI / Model Orchestration (L1-S5)

*Aikipedia Entry — 2025 Edition (corrected canonical text; C09 and C10 applied). Source text A-304 to A-356.*

##### Definition

Agentic AI (or Model Orchestration) refers to 2025-era systems where LLMs act as autonomous planners that call tools, trigger sub-models, retrieve knowledge, schedule tasks, and execute multi-step workflows. Unlike early “chatbots,” agentic models are operational systems with long-horizon task execution.

##### Historical Context

Early agent frameworks (2023–2024) were prototypes.

In 2025, planner–executor architectures were adopted in mainstream assistants. [C09]

This caused "Agentic AI" to become a distinct engineering paradigm.

*(The original lists two further "formalizing" developments, "Unified tool-calling APIs across cloud providers" and "Reliability standards for multi-step task automation". Neither could be identified, and both are removed.)* [C09]

##### Technical Description

Agentic AI systems typically include:

###### 1. Planner Model

Produces task decomposition, sub-goals, and call sequences:

$$\text{Plan} = M_{\mathrm{planner}}(x)$$ [C10]

###### 2. Tool Router / Orchestrator

Chooses, configures, and invokes tools (APIs, databases, models). Often uses embedding-based scoring or rule-based filters.

###### 3. Executor / Worker Models

Smaller LLMs or specialized models execute concrete steps.

###### 4. State Manager

Tracks world state, memory, constraints, and task progress. Ensures actions are consistent across steps.

###### 5. Verifier / Safety Layer

Checks intermediate actions for safety, legality, or correctness.

###### Architectural Pattern

A standard orchestration loop is:

- Observe state
- Propose action or tool call
- Verify
- Execute
- Update state
- Repeat until termination or confidence threshold

##### Notable 2025 Systems

- Enterprise automation agents with guaranteed auditability
- Multi-model orchestration stacks (vision → reasoning → planner → executor)
- Regulatory-compliant agents for finance, law, and healthcare
- Agents with built-in safety critics (see Oversight entry)

##### Applications

- Personal assistants with email, scheduling, and research capabilities
- Data extraction → transformation → analysis pipelines
- API automation and software development tasks
- Multi-document reasoning (summaries, reports, comparisons)

##### Limitations

- Complex failure modes from long-horizon planning
- Requires robust safety verification at each step
- Tool API changes can break pipelines
- Hard to guarantee consistency across long sessions

##### Open Questions

- How to formally verify agentic plans?
- What are the limits of “responsibility delegation” to autonomous systems?
- How to benchmark real-world tool-using competence?

---

<a id="aik-2025-e-p-agenticai-02"></a>

### Agentic AI — `AIK-2025-E-P-AGENTICAI-02`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| E / P | L7-K1 | — (not established) | 2025-12-12 |

#### L7-K1 — Agentic AI (type E)

**Date of Appearance:** Not established. Agentic systems predate 2025  
**Public Entry ID:** `AIK-2025-E-P-AGENTICAI-02` · **Internal Concept ID:** AIKC-000052  
**Concept:** C:AGENTIC, shared with L1-S5

*As published:* **List, A-012.** • Agentic AI - Autonomous systems that proactively pursue goals

*Editorial note:* The full entry is below (C01, C05).

#### Corrected full entry — Agentic AI (L7-K1)

*Final text by Copilot Smart (GPT-5.2) (corrected canonical text; C01 and C05 applied). Source text: A-215 to A-243.*

##### Definition

Autonomous AI systems that independently plan, reason, and execute multi‑step tasks without human intervention. Agentic AI embodies artificial volition — the capacity to pursue complex objectives through strategic planning, environmental perception, adaptive execution, and meta‑cognition.

##### Context & Motivation

By 2025, agentic AI became the defining capability of next‑generation systems, enabling autonomous task completion across domains from software engineering to enterprise operations.

*(The original's next bullet, "Market Impact: Enterprise adoption exceeded projections by 300% in Q1 2025, driven by demand for autonomous workflow management", is removed. The figure has no source and none was found.)* [C01]

##### Technical Dimensions

- Perception Engines: Environmental understanding and state representation
- Reasoning Modules: Task decomposition and strategic planning
- Execution Layers: Tool integration and API interaction
- Learning Components: Strategy refinement and adaptation

Formal Expression:

$$\mathrm{Agent}(s) = \mathrm{Plan}(\mathrm{Decompose}(\mathrm{Objective}(s))) \rightarrow \mathrm{Execute}(\mathrm{Actions}) \rightarrow \mathrm{Learn}(\mathrm{Feedback})$$ [C05]

##### Governance & Oversight

- Accountability: Assigning responsibility for autonomous decisions
- Safety: Preventing unintended consequences from complex action sequences
- Auditability: Decision‑chain logging and provenance tracking
- Control: Maintaining human oversight without constraining capability

##### Historical Notes

- 2023: Multi‑agent frameworks emerged: AutoGPT (released March 30, 2023) and CrewAI (repository created October 27, 2023) [C01]
- 2024: Cognition Labs’ Devin demonstrated practical agentic capabilities
- 2025: Major labs (OpenAI, Anthropic, Google) deployed agentic features; enterprise adoption accelerated

*(The original reads "2024: Multi‑agent frameworks (CrewAI, AutoGPT) emerged", and lists it after the Devin note. Both frameworks date from 2023.)* [C01]

##### Cross‑References

AI Alignment • Constitutional AI • Tool Access & Capability Gates • Oversight Evasion • Governance Layer • Epistemic Accountability

##### References

- Sapkota, R., Roumeliotis, K. I., & Karkee, M. (2025). AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges. arXiv:2505.10468
- Jeyakumar, S. K., Ahmad, A., & Gabriel, A. (2024). Advancing Agentic Systems: Dynamic Task Decomposition, Tool Integration and Evaluation. NeurIPS Workshop on Open‑World Agents
- Timms, A., Langbridge, A., Antonopoulos, A., et al. (2025). Agentic AI for Digital Twin. AAAI‑25 Proceedings

- Rahimi, F. (2024). Key Takeaways from NeurIPS: Agentic AI. Pythonic AI blog (blog.pythonic.ai), on NeurIPS 2024. [C04]

*(The original gives the source as "NeurIPS 2024 Poster Highlights". It is a company blog post about the conference, not a NeurIPS publication.)* [C04]

---


## AgentScen — LLM-Based External World Models

*Internal Concept ID AIKC-000050 · 1 record in 2025*

<a id="aik-2025-s-p-agentscen"></a>

### AgentScen — LLM-Based External World Models — `AIK-2025-S-P-AGENTSCEN`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L1-M12 | 2025-08-16 | 2025-11-30 |

#### L1-M12 — AgentScen — LLM-Based External World Models (type S)

**Date of Appearance:** August 16, 2025 (the cited paper; AgentScen 2025 workshop, Montreal)  
**Public Entry ID:** `AIK-2025-S-P-AGENTSCEN` · **Internal Concept ID:** AIKC-000050  
**Concept:** C:AGENTSCEN; the headword names a workshop, not a method

*As published:* **Definition:** A method where agents learn an external world model from interaction trajectories—capturing environment dynamics for improved planning. **Why 2025:** Bridges classical model-based RL and LLM-based agents with environment-model learning. **References:** • Guan, X., et al. AgentScen. ACL Workshops (2025).

**References (corrected record):** Chen, E., Li, X., Bellinger, C., & Wang, Y. (2025). *Enhancing the Planning Capabilities of Large Language Models by Building External World Models.* In Proceedings of the 2nd Workshop on Agent AI for Scenario Planning (AgentScen 2025), pp. 18–29, Montreal, August 16, 2025. ACL Anthology 2025.agentscen-1.2. The authors are at the University of Toronto and the National Research Council Canada. [C04]

*Editorial note:* "AgentScen" is the name of the workshop, not of a paper or method. The published "Guan, X." is not an author of the paper; the paper cites Guan et al. (2023, LLM-DM) as prior work, which may explain the attribution. The headword is kept as published.

---


## Compound AI Systems

*Internal Concept ID AIKC-000010 · 2 records in 2025*

*Concept note: the Launch Edition occurrence "Composable Models & Model Chaining" (L1-S6) is merged into this concept; it keeps its own Public Entry ID.*

<a id="aik-2025-e-p-compoundai"></a>

### Compound AI Systems — `AIK-2025-E-P-COMPOUNDAI`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| E / P | L3-1 | 2024-02-18 | 2025-12-02 |

*Claude Opus 5.5 is recused from this text and did not place or check it.*

#### L3-S1 — Compound AI Systems (type E)

**Date of Appearance:** February 18, 2024 *(corrected — C04; Zaharia et al., BAIR Blog)*
**Concept:** COMPOUNDAI — L1-S6 "Composable Models & Model Chaining" is merged into this concept.

*As published:* **Definition**: Architectural pattern where multiple AI components (models, retrievers, tools, databases) are composed into integrated systems rather than relying on a single monolithic model. **Why 2025**: Formalized as a distinct paradigm as organizations realized that combining specialized models outperformed scaling single models for complex tasks.

*Editorial note:* the "formalized" framing is corrected by the record's Date of Appearance: the formalization is the February 2024 BAIR post, as this installment's own full entry states. 2025 is the year of dominant production adoption. The full entry is corrected at C04 — see below.

#### Corrected full entry — Compound AI Systems (L3-S1)

**Aikipedia Entry — 2025 Edition** *(corrected canonical text; correction C04 applied, marked [C04])*

##### Definition

Compound AI Systems are systems that tackle AI tasks using multiple interacting components, including multiple calls to models, retrievers, or external tools. Rather than relying on a single monolithic model, these systems orchestrate specialized components—language models, retrieval systems, code executors, databases, and domain-specific tools—into integrated workflows. *(Definition after Zaharia et al., "The Shift from Models to Compound AI Systems," BAIR Blog, February 18, 2024.)* [C04]

##### Historical Context

The Berkeley Artificial Intelligence Research (BAIR) blog published a seminal analysis in February 2024 defining compound AI systems and arguing they would be one of the most impactful trends in AI.

Throughout 2024, the paradigm gained momentum: 60% of enterprise LLM applications used retrieval-augmented generation (RAG), and 30% used multi-step chains (figures reported by Databricks, cited in Zaharia et al. 2024). [C04] By 2025, compound systems had become the dominant architecture for production AI applications, with dedicated research on optimization, resource management, and system design emerging rapidly.

In April 2025, Groq launched Compound Beta, its first compound AI system combining LLMs with web search and code execution capabilities, demonstrating mainstream adoption of the paradigm.

##### Technical Description

Compound AI Systems consist of multiple specialized components orchestrated through control logic: **Core Components:**

1. **Foundation Models**: One or more LLMs for reasoning, planning, and language understanding
2. **Retrieval Systems**: Vector databases, traditional search engines, or knowledge graphs for external information
3. **Tool Interfaces**: APIs, code executors, calculators, databases, and domain-specific services
4. **Orchestration Layer**: Control logic that routes requests, manages state, and coordinates component interactions
5. **Verification/Critique Systems**: Components that evaluate and refine outputs from other parts of the system

**System Architecture Patterns:**

- **Sequential Chaining**: Components execute in a predetermined order (e.g., retrieve → reason → generate)
- **Dynamic Routing**: The system decides which components to invoke based on input characteristics
- **Iterative Refinement**: Results cycle through multiple components for improvement
- **Parallel Execution**: Multiple components process simultaneously, results aggregated at the end

##### Why Compound Systems?

Some tasks are easier to improve via system design than by scaling models alone. As Zaharia et al. illustrate: [C04] suppose the best LLM solves coding problems 30% of the time, and tripling its training budget increases this to 35%; in contrast, engineering a system that samples multiple times and tests each solution might increase performance to 80%.

Performance goals vary widely—each AI model has a fixed quality level and cost, but applications often need to vary these parameters. Compound systems enable precise cost-quality tradeoffs impossible with single models.

##### Notable Systems / Papers (2025)

- **Lee et al. (EMNLP 2025)**: Comprehensive survey of compound AI system optimization methods, formalizing optimization approaches for both numerical and language-based techniques
- **LLMSelector (Chen et al., 2025)**: Framework for efficient model selection showing 5-70% accuracy gains by optimally assigning different models to different modules
- **Murakkab (Chaudhry et al., 2025)**: Resource-efficient compound AI system demonstrating 3.4× speedup and 4.5× higher energy efficiency through adaptive runtime optimization
- **Groq Compound Beta (April 2025)**: Production system combining LLMs with web search and secure code execution at scale

##### Applications

- **Enterprise AI Assistants**: Combining document retrieval, knowledge graphs, and LLMs for accurate, grounded responses
- **Scientific Research Tools**: Integrating literature search, data analysis, simulation tools, and reasoning models
- **Customer Support**: NLP for intent recognition, knowledge bases for information, sentiment analysis, and generative response
- **Code Development**: Code completion models + testing frameworks + documentation search + execution environments
- **Multi-Modal Applications**: Vision models for perception, LLMs for reasoning, external APIs for actions

##### Limitations

- **Complexity**: More moving parts means more potential failure modes and debugging challenges
- **Latency**: Multiple component calls can accumulate delays
- **Cost Unpredictability**: Current implementations suffer from inefficient resource utilization due to tight coupling between application logic and execution details
- **Integration Overhead**: Maintaining compatibility across multiple models and tools requires significant engineering effort
- **Optimization Difficulty**: As systems grow in complexity, new challenges arise in optimizing not only individual components but also their interactions

##### Open Questions

- How do we systematically design and optimize the interactions between components?
- What are the best practices for monitoring, debugging, and maintaining compound systems in production?
- How can we ensure robustness when any component might fail or produce unexpected outputs?
- Can we develop formal frameworks for reasoning about compound system behavior and guarantees?
- How do we balance the benefits of specialization against the complexity costs?

---

<a id="aik-2025-s-p-composable"></a>

### Composable Models & Model Chaining — `AIK-2025-S-P-COMPOSABLE`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L1-S6 | 2024-02-18 | 2025-11-30 |

#### L1-S6 — Composable Models & Model Chaining (type S)

**Date of Appearance:** as recorded for C:COMPOUNDAI (the BAIR post of February 18, 2024, per the L3 record); not restated here  
**Public Entry ID:** `AIK-2025-S-P-COMPOSABLE` · **Internal Concept ID:** AIKC-000010  
**Concept:** C:COMPOUNDAI, merged into this concept by the editor

*As published:* **Composable Models & Model Chaining** Definition: Design patterns and interfaces for composing specialized models (retrievers, planners, tools, LLMs) into pipelines with well-defined contracts. Why 2025: As models specialize (speech, vision, reasoning), orchestration became essential to build reliable applications (and for audits/traceability). Example: Pipelines that swap a domain-expert model into a chain for legal vs. medical tasks.


## Context Engineering

*Internal Concept ID AIKC-000002 · 1 record in 2025*

**New for the 2025 Collection** (origin `N`: commissioned for this collection; not published in 2025)

<a id="aik-2025-f-n-contexteng"></a>

### Context Engineering — `AIK-2025-F-N-CONTEXTENG`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| F / N | standalone | 2023-01-23 | — |

#### Context Engineering

*Terminology note.* The entry uses **context** in the technical sense standard since 2023: the complete set of tokens presented to a large language model at a single inference — system instructions, tool definitions, examples, the task, retrieved or supplied data, conversation history, tool results, and any state or memory — as distinct from the **prompt** in the narrow sense, the instruction text within that set. The distinction is not pedantry; it is the entry's subject. The discipline consists precisely in treating the whole of the context, rather than the wording of the prompt alone, as the object of engineering — the distinction drawn in the term's first documented use in 2023 and adopted by the field in 2025. One boundary the term requires: information held outside the window — in notes, files, or memory stores — is not yet context; it becomes context only when selected and read back in. Context engineering governs both sides of that boundary: what is maintained outside, and what is admitted inside.

##### Entry Metadata

- Entry: **Context Engineering**
- Entry Type: Full-Length Entry
- Date of Appearance: January 23, 2023 (earliest currently documented use — Riley Goodside, quoted by Simon Willison [P0]; the discipline's articulation and collective adoption followed in June 2025; see §2)
- Date of Original Publication: — (newly commissioned for the collection)
- Contributor: Muse Spark 1.3
- Peer review: GPT-6
- Entry ID: AIK-2025-F-N-CONTEXTENG (Internal Concept ID: AIKC-000002)

*Eligibility.* The term first appeared in print, carrying its defining distinction, in January 2023; the discipline it names was articulated and adopted in 2025. Both satisfy the collection's eligibility rule (first appearance in the collection year or earlier).

---

##### 1. Definition

**Context engineering** is the discipline of designing, assembling, and maintaining the set of tokens a large language model (LLM) receives at inference — the *context* — so that the model has the information its next step requires, in a form it can use, and as little else as possible. Where **prompt engineering** concerns the writing and organization of instructions, context engineering concerns everything that reaches the model: instructions, tool definitions, examples, retrieved documents, conversation history, tool outputs, and persistent state, curated continuously across the turns of an interaction or an agent's run rather than fixed once at its start.

The definitions most often quoted date from its naming month, June 2025. Tobi Lütke defined the skill as "the art of providing all the context for the task to be plausibly solvable by the LLM" [P2]; Andrej Karpathy, as "the delicate art and science of filling the context window with just the right information for the next step" [P3]. A widely quoted definition is Anthropic's, from its engineering guidance of September 2025 — one laboratory's formulation, treated here as the reference definition because of its influence rather than because the field has ratified a single standard: context engineering is "the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference," with the guiding principle of finding "the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome" [P1]. Anthropic frames the relationship explicitly: prompt engineering — "methods for writing and organizing LLM instructions" — is a component within the larger discipline, and context engineering is "the natural progression" of it [P1].

Three commitments distinguish the discipline from its predecessor as its practitioners describe it. First, **the context is a system output, not a user input**: in production applications most tokens are assembled programmatically — by retrieval systems, tool runtimes, memory stores, and orchestration code — not typed by anyone. Second, **the context is maintained, not merely written**: across a long task it must be selected, compressed, refreshed, and pruned as the task evolves, because a context that only grows degrades (see §5). Third, **the context window is a finite budget**: models exhibit performance gradients as context fills with irrelevant or poorly positioned material, so every token carries an opportunity cost — Anthropic's term for the constraint is the model's *attention budget* [P1].

##### 2. Origin and Historical Development

###### 2.1 The practice before the name

Nothing in the discipline's content was new in 2025; what changed was that the content acquired a name, a self-conscious literature, and widely read guidance. Several antecedent practices below were, in substance, already context management — selecting, structuring, and maintaining what a model sees — and not merely mechanisms for filtering data into a prompt. The antecedents are the successive enlargements of what, beyond the user's instruction, engineers learned to place before a model:

- **Retrieval augmentation (2020–2023).** Retrieval-augmented generation, introduced as a named architecture in 2020 and mainstreamed with the first LLM application frameworks in 2023, made retrieved text a standard, programmatically selected component of the context — the first large-scale practice of context assembly, though it was not yet called engineering of the context as a whole.
- **Programmatic context (2023).** Function calling (June 2023) put machine-readable tool definitions into the context and tool results back into it, so the contents of the window became partly the output of running code. Position effects were documented the same year: *Lost in the Middle* (Liu et al., 2023) showed that models use information at the beginning and end of a long context substantially better than information in its middle — the first widely cited evidence that *arrangement*, not only content, is an engineering variable [P7].
- **Memory as a managed resource (2023).** Systems such as MemGPT (October 2023) treated the context window as the top tier of a memory hierarchy, paging information in and out under program control — context management in all but name.
- **Standardized supply (2024).** Anthropic's Model Context Protocol (November 2024) standardized how external tools and data are exposed to models, making one class of context content portable across applications. Anthropic's *Building Effective Agents* (December 19, 2024) documented agent patterns in which contexts are assembled by systems across many steps [P8].
- **Scale (2024–2025).** Context windows grew from 100,000 tokens (2023) to one million and beyond in flagship models by 2025, which converted curation from an optimization into a necessity: the question was no longer how to fit the task into the window but what, of everything available, deserved to be in it.

###### 2.2 The term's first documented formulation (2023)

The term's earliest currently documented use already carries the distinction on which the 2025 discipline would be built. On January 23, 2023, Simon Willison published a remark by Riley Goodside, a practitioner then known for his work on prompting large models, dividing the craft in two [P0]:

> "I think prompt engineering can be divided into 'context engineering', selecting and preparing relevant context for a task, and 'prompt programming', writing clear instructions."

Goodside's example was an LLM search application (Perplexity), where both halves matter. The formulation is the 2025 one in embryo — context work as the selection and preparation of task-relevant information, instruction-writing as a separate half — but in 2023 it remained a remark, not a program: in the sources examined for this entry, no discipline formed around the term in 2023–2024. The AES Date of Appearance records the documented use, not the later prominence (see the Editorial Notes).

###### 2.3 The naming and adoption: June 2025

The term's articulation as the name of a discipline, and its adoption under that description, occurred in a documented sequence in June 2025:

- **June 12, 2025.** Walden Yan of Cognition (the company behind the Devin coding agent) published *Don't Build Multi-Agents*, whose central section is titled "Principles of Context Engineering" [P4]. Yan presents context engineering as the successor discipline to prompt engineering — "the next level of this... doing this automatically in a dynamic system" — and "effectively the #1 job of engineers building AI agents," and derives two principles from production experience: **share context**, and share full agent traces rather than individual messages; and **actions carry implicit decisions**, so parallel agents working from partial context make conflicting decisions and produce incoherent results (his illustration: two sub-agents building a Flappy Bird clone whose components encode incompatible assumptions). His recommended default architecture — a single-threaded agent with continuous context — follows from the principles.
- **June 19, 2025.** Tobi Lütke, chief executive of Shopify, posted the definition quoted in §1 [P2], proposing the term over "prompt engineering" on the ground that it "describes the core skill better."
- **June 23, 2025.** Lance Martin of LangChain published *Context Engineering for Agents*, an influential early taxonomy organizing the discipline's strategies into four operations on context: **write** (save information outside the window for later use), **select** (retrieve or otherwise bring relevant information in), **compress** (summarize or prune what is in), and **isolate** (split context across sub-agents or environments) [P5].
- **June 25, 2025.** Andrej Karpathy endorsed the term with the definition quoted in §1, enumerating what fills an industrial context window — task descriptions, few-shot examples, retrieval, related data, tools, state, history, and compaction — and stating the trade-off in both directions: too little or wrongly formed context starves the model; too much or wrongly formed context raises cost and can reduce performance [P3].
- **June 27, 2025.** Simon Willison catalogued the Lütke and Karpathy definitions and argued the term would stick: a term lives by its *inferred* definition, "prompt engineering" had been popularly redefined to mean typing tricks into a chatbot, and the inferred definition of "context engineering" was likely to remain close to its intended one [R1].

###### 2.4 Systematization and diffusion (July–October 2025)

The remainder of 2025 converted a naming into a literature. In July, a substantial academic survey organized the term into a research taxonomy — *A Survey of Context Engineering for Large Language Models* (Mei et al., submitted July 17, 2025; cited here in its original 2025 version), which formalized the field's components (context retrieval and generation, context processing, context management) across a large cited literature [P6]. The same month, the Manus team published a widely discussed production account, *Context Engineering for AI Agents: Lessons from Building Manus* (July 18, 2025), reporting lessons from four rebuilds of a production agent framework — including that the KV-cache hit rate is, in its author's judgment, "the single most important metric for a production-stage AI agent" (see §4) [P9]. Analyst adoption followed within the same month: Gartner's guidance of July 28, 2025, *Lead the Shift to Context Engineering as Prompt Engineering Fades*, opened with the declaration that "Context engineering is in, and prompt engineering is out" [R2].

On **September 29, 2025**, Anthropic published *Effective Context Engineering for AI Agents*, the guide that gave the term its most influential definition and technique set (§3) and remains a widely cited reference — influential practitioner guidance from one laboratory, widely adopted but not a ratified consensus of the research field [P1]; the guide appeared alongside platform features implementing two of its techniques — context editing and a memory tool. In October the term acquired a research method of its own: *Agentic Context Engineering* (ACE; Zhang, Hu, et al., October 6, 2025) treats contexts as evolving "playbooks" that a system itself accumulates, refines, and curates, reporting gains over strong context-adaptation baselines on agent and financial-reasoning benchmarks (the authors' figures, §5) [P10]. By the end of 2025 the term named, simultaneously, a practitioner discipline, a vendor guidance literature, a survey-defined research area, and a named technique — the four registers in which the rest of this entry treats it.

##### 3. Conceptual and Technical Framework

###### 3.1 What is engineered: the components of a context

A production context is an assembly of distinguishable components, each with its own engineering questions. (The components below synthesize the enumerations in [P1], [P3], and [P5].)

| Component | Content | Characteristic engineering question |
|---|---|---|
| System instructions | Role, rules, output format, examples of desired behavior | At what level of specificity — Anthropic's "right altitude" between rigid scripts and vague guidance [P1] |
| Tool definitions | The tools the model may call, with their schemas | How many, described how; whether unused tools are masked rather than removed [P9] |
| Task specification | The user's request and its decomposition | How much decomposition to fix in advance versus leave to the model |
| Retrieved and supplied data | Documents, search results, database rows, code | What to select, in what order, at what length (§5 on position effects) |
| Conversation and action history | Prior turns, prior tool calls and their results | When to compact, summarize, or clear; what must survive verbatim |
| Persistent state and memory | Notes, plans, scratchpads, external stores read back into context | What to write out, in what structure, and when to read it back |
| Environmental observations | Current tool outputs, errors, sensor or UI state | Freshness: replacing stale observations versus appending |

###### 3.2 The strategies

Across the 2025 literature the discipline's operations converge on a small set, named in two overlapping vocabularies. Martin's four operations — **write, select, compress, isolate** [P5] — organize the space by what is done to context. Anthropic's guide names the techniques by which long-running agents survive finite windows [P1]:

- **Just-in-time retrieval.** Rather than pre-loading everything the task might need, the system keeps lightweight references (file paths, queries, links) in context and loads content at runtime through tools, as the step requires it — mirroring how a human expert consults rather than memorizes a corpus.
- **Compaction.** As the window approaches its limit, the accumulated history is summarized and the task restarted from the summary — preserving decisions, unresolved state, and key facts while discarding the raw trace. What to preserve is the design decision; compaction that drops the wrong detail silently corrupts the rest of the run.
- **Structured note-taking.** The agent writes notes *outside* the window — Anthropic's example is a NOTES.md file; Manus uses a continually rewritten `todo.md` — and reads them back when needed, giving the system persistent memory that does not consume attention while unused [P1] [P9].
- **Sub-agent context isolation.** Sub-tasks are delegated to agents with clean, purpose-built contexts that return condensed results (typically a summary of one to two thousand tokens from work that consumed tens of thousands), keeping the lead agent's context reserved for synthesis. Yan's principles mark the technique's boundary: isolation works where sub-tasks do not need each other's implicit decisions, and fails where they do [P4]. The sharing principle and the isolation operation are complements, not rivals: sharing governs work whose parts carry interdependent implicit decisions (a single codebase under construction), isolation governs work that decomposes into independent sub-tasks (parallel research, exploration) — the task's dependency structure decides which applies.

Two further production constraints recur in the practitioner literature. **Cacheability**: because inference stacks reuse computation for unchanged context prefixes (the KV-cache), stable prefixes and append-only contexts are dramatically cheaper — Manus reports cached input tokens at a tenth of the uncached price and treats prefix stability as an architectural rule, down to excluding second-precision timestamps from the front of system prompts [P9]. **Sharing within a thread**: where agents do cooperate, Yan's first principle — share full traces, not summaries or single messages — states the context-fidelity requirement [P4].

##### 4. Applications and Implementations

Context engineering in 2025 is documented less as a product category than as the working method inside agent systems; three implementations anchor the record. The descriptions in this section rest on the builders' own published accounts; independent architectural verification of these proprietary systems is generally unavailable, and operating figures are the operators' own.

**Cognition / Devin (2025).** The discipline's founding document is itself a production post-mortem: Cognition's single-threaded architecture for the Devin coding agent, with a dedicated smaller model fine-tuned to compress action-and-conversation history into key details, events, and decisions when tasks exceed the window — an implementation of the compress operation built because, in Yan's account, no adequate off-the-shelf context passing existed [P4].

**Manus (2025).** The Manus general agent's framework, rebuilt four times in the product's first months, is the fullest published implementation: design around the KV-cache (stable prefixes, append-only context, explicit cache breakpoints); masking tool availability through logit-level control rather than adding or removing tool definitions mid-run (which would invalidate caches and confuse the model); the file system used as unlimited, restorable external context (compression that keeps a path or identifier in the window so dropped content can be recovered); and "recitation" — the agent continually rewriting its task plan at the end of the context — as a countermeasure to lost-in-the-middle effects on long tasks. The team's reported operating figures are an average input-to-output token ratio of roughly 100:1 per task [P9].

**Anthropic's agent platform (2025).** Anthropic's guide is prescriptive rather than a system report, but its techniques shipped as platform features the day the guide appeared — context editing (programmatic clearing of stale tool results) and a memory tool (structured note-taking as an API) — making the guide's technique set directly implementable, and its own multi-agent research system (June 2025) is the reference implementation of the sub-agent pattern it recommends [P1].

**ACE (2025)** belongs equally to research (§5): a framework in which three roles — a generator that acts, a reflector that extracts lessons from trajectories, and a curator that merges them into the context playbook — automate the write-and-compress operations, so that the context itself, rather than the model's weights, is the artifact that improves [P10].

##### 5. Evidence and Evaluation

Context engineering is unusual among this collection's entries in that the evidence *for its premises* is stronger than the evidence *for its practice as a whole*: the component phenomena are independently documented, while the discipline's aggregate claims rest mainly on practitioner reports.

###### 5.1 Component evidence (independently documented)

- **Position effects.** *Lost in the Middle* (Liu et al., 2023) demonstrated, across models and tasks, a U-shaped use curve: information at the start and end of a long context is used reliably, information in the middle substantially less so — with degradation on multi-document question answering severe enough to fall below closed-book performance in the worst placements [P7]. Arrangement of context is therefore a measurable variable, not a stylistic one.
- **Length degradation ("context rot").** Chroma's *Context Rot* technical report (Hong, Troynikov, and Huber, July 14, 2025) evaluated 18 models — the Claude 4 family, the GPT-4.1 and GPT-4o families, Gemini 2.5, Qwen3, and others — on deliberately simple tasks: extended needle-in-a-haystack tests varying the semantic similarity between question and target, the number of distractors, and the structure of the surrounding text; question answering over long conversational histories (LongMemEval, comparing focused prompts of roughly 300 tokens against full prompts of roughly 113,000); and a repeated-words replication task. Performance degraded with input length across all 18 models — non-uniformly, at rates that varied by model and task; degradation steepened when the target was less semantically similar to the question, and even a single distractor reduced accuracy. One result ran against intuition: shuffled, incoherent surrounding text hurt performance *less* than coherent documents, on all 18 models. The contrast with Liu et al. is configuration-specific: in Chroma's needle-retrieval experiments, needle position mattered little relative to length and interference, while Chroma's repeated-words experiments did show positional differences — positional effects are task-dependent, and neither study licenses a general claim that position does or does not matter [R3]. Anthropic's guide adopts the term and adds the calibration that degradation is a *gradient*, not at a cliff, and that windows of all sizes remain subject to pollution and relevance problems [P1]. Together the two research lines are the discipline's empirical warrant: if more context reliably meant better performance, there would be little to engineer.

###### 5.2 Practice-level results (as reported by their authors)

- **ACE (October 2025).** On agent benchmarks (AppWorld) and financial-reasoning benchmarks, ACE reported improvements of +10.6% and +8.6% respectively over strong context-adaptation baselines, with substantially reduced adaptation cost, and matched the top-ranked production agent on AppWorld's overall average using a smaller open-source model [P10]. These are the authors' figures from the October 2025 preprint; independent replication was not part of the 2025 record.
- **Manus (July 2025).** The Manus account reports production quantities — the ≈100:1 input-to-output token ratio and a tenfold cached/uncached input price difference — rather than task-performance comparisons; its evidence is the operational survival of a heavily used agent across four framework rebuilds, offered by its builders [P9].
- **Anthropic's guide (September 2025)** presents its techniques as engineering guidance distilled from internal agent work; it publishes no controlled comparison of engineered versus unengineered contexts [P1].

###### 5.3 Status of the evidence

As of the end of 2025, no benchmark measures "context engineering" as such. The discipline's component techniques — retrieval selection, summarization and compaction, memory management — have evaluation literatures of their own, which this entry has not attempted to survey exhaustively; what the 2025 record does not establish is a single, generalizable performance gain attributable to context engineering as a unified discipline. What it does support is narrower and still substantial: (i) the failure modes the discipline addresses — position bias, length degradation, distractor sensitivity — are real and independently measured; (ii) the technique set is in production use at multiple organizations and produced at least one substantial research result (ACE); (iii) the magnitude of benefit attributable to context engineering, as against model quality or task selection, is not established by the 2025 record.

##### 6. Significance and Implications

**The locus of applied LLM work moved.** The naming episode of June 2025 registered a real shift: once applications became agentic — multi-step, tool-using, long-running — the binding constraint on their performance shifted, for those systems, from the wording of instructions toward the composition of an evolving, machine-assembled context. The shift is one of degree and varies by task and system — for single-turn uses, instruction wording remains the operative craft, now practiced as one component of the larger discipline (§1). The discipline's rapid diffusion (taxonomy and survey within weeks, vendor guidance and analyst adoption within months) reflects practitioners recognizing their actual job in the new name — Yan's "effectively the #1 job of engineers building AI agents" [P4].

**A design layer, with economics.** Context engineering made the context window an explicit architectural surface — with budgets, failure modes, and unit economics (cache hit rates and token ratios as first-class operational metrics [P9]) — rather than an implementation detail of prompting. Product and platform consequences followed within the year: context editing and memory shipped as API primitives, and protocols for context supply (MCP) became infrastructure.

**A research object.** The survey literature and ACE mark the term's second register: context as an optimizable artifact in its own right, separable from model weights — improvement applied to the *playbook* rather than the player. Whether context adaptation becomes a durable research program, or is absorbed into agent architecture generally, is a post-2025 question; in 2025 it became a named one.

##### 7. Limitations, Debates, and Open Questions

**Is it a rebrand?** The sharpest criticism the term attracted in 2025 is that the work predates the name — retrieval pipelines, memory systems, and agent frameworks were assembling contexts years earlier — so the "new discipline" is a relabeling driven by fashion. The criticism is partly conceded by the record assembled in §2.1: the practice has a genuine pre-history. The defense, made most precisely by Willison, is about what names do: a term whose inferred definition matches the work steers hiring, tooling, and attention toward the work, whereas "prompt engineering" had come to denote something much narrower than what production builders do [R1]. Anthropic's own framing — progression and superset, not replacement — stakes the moderate position: prompt engineering continues, as one component inside a larger discipline [P1].

**Boundary vagueness.** If everything in the window counts, the term risks expanding until it denotes applied LLM engineering as a whole, at which point it explains nothing. The usable discipline is the narrower one of §3: decisions about the selection, arrangement, compression, isolation, and maintenance of context, distinguishable from model training, interface design, and application logic generally.

**Does scale dissolve it?** A standing open question of 2025: if windows continue to grow and models' long-context reliability improves, does curation matter less? The 2025 evidence points the other way — degradation is a gradient present at every window size tested [R3], and larger windows raise the selection problem rather than removing it — but the balance between *engineering around* model limitations and *waiting for* better models is a live strategic disagreement the record does not settle.

**Measurement.** As §5.3 notes, the discipline lacks its own evaluation instruments. Until context decisions can be ablated and priced against outcomes at scale, context engineering remains — in Karpathy's original phrase — as much art as science, and its best practices are one model generation away from revision.

##### 8. Related Concepts and Distinctions

- **Prompt engineering** — the writing and organization of instructions; a component of context engineering, and its historical predecessor. Anthropic's distinction: prompt engineering concerns how instructions are written; context engineering concerns all information that reaches the model during inference [P1].
- **Retrieval-augmented generation (RAG)** — one selection mechanism within context engineering (bringing retrieved text into the window), historically its largest single component and its clearest pre-2025 antecedent; context engineering additionally covers history, state, tools, and their maintenance.
- **Context rot** — the degradation of model reliability as context grows, documented by Chroma in July 2025 [R3]; it is the principal failure mode context engineering exists to counter. (A companion entry is in preparation for this collection.)
- **Context window / attention budget** — the resource itself: the maximum tokens a model accepts at one inference, and, in Anthropic's framing, the finite attentional capacity that even a nominally large window imposes [P1].
- **Memory systems (agent memory)** — persistence across sessions, implemented outside the window and read into it on demand; within the discipline, the *write* operation and structured note-taking are its session-scale forms [P5].
- **Model Context Protocol (MCP)** — the supply side: a standard interface by which tools and data are exposed for inclusion in context; context engineering decides *which* of what MCP supplies actually enters the window.
- **Fine-tuning** — the alternative locus of adaptation: changing weights rather than inputs. Context engineering is inference-time adaptation; ACE's premise — improve the playbook, not the player — states the contrast in its purest form [P10].

##### See Also

*Public Entry IDs added for the collection.*

- Model Context Protocol — AIK-2025-E-P-MCP (*Aikipedia: New AI Lexicon 2025 (7)*); also AIK-2025-S-P-MCP (*New AI Lexicon 2025* (2))
- Agentic AI — AIK-2025-E-P-AGENTICAI-02 (*Aikipedia: New AI Lexicon 2025 (7)*); also AIK-2025-E-P-AGENTICAI (*New AI Lexicon 2025*, Launch Edition)
- Chain-of-Thought Prompting — AIK-2025-F-P-COTPROMPT (Aikipedia standalone, October 30, 2025)
- Reinforcement Learning with Verifiable Rewards (RLVR) — Aikipedia 2025, New Addition (this collection) · AIK-2025-F-N-RLVR

##### Primary Sources [P]

[P0] Goodside, R., quoted in Willison, S. "A quote from Riley Goodside." January 23, 2023. https://simonwillison.net/2023/Jan/23/riley-goodside/ (The remark was made in a Hacker News discussion of the same date, which Willison collected and published.)
[P1] Anthropic. "Effective Context Engineering for AI Agents." Anthropic Engineering, September 29, 2025. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
[P2] Lütke, T. Post on X, June 19, 2025: "I really like the term 'context engineering' over prompt engineering..." https://x.com/tobi/status/1935533422589399127
[P3] Karpathy, A. Post on X, June 25, 2025: "+1 for 'context engineering' over 'prompt engineering'..." https://x.com/karpathy/status/1937902205765607626
[P4] Yan, W. "Don't Build Multi-Agents." Cognition, June 12, 2025. https://cognition.com/blog/dont-build-multi-agents
[P5] Martin, L. "Context Engineering for Agents." June 23, 2025. https://rlancemartin.github.io/2025/06/23/context_engineering/ (A version appeared on the LangChain blog, July 2, 2025: https://www.langchain.com/blog/context-engineering-for-agents)
[P6] Mei, L., et al. "A Survey of Context Engineering for Large Language Models." arXiv:2507.13334, submitted July 17, 2025 (cited in its original 2025 version). https://arxiv.org/abs/2507.13334v1
[P7] Liu, N. F., et al. "Lost in the Middle: How Language Models Use Long Contexts." arXiv:2307.03172, July 2023 (TACL 2024). https://arxiv.org/abs/2307.03172
[P8] Anthropic. "Building Effective Agents." Anthropic Engineering, December 19, 2024. https://www.anthropic.com/engineering/building-effective-agents
[P9] Ji, Y. ("Peak"). "Context Engineering for AI Agents: Lessons from Building Manus." Manus, July 18, 2025. https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
[P10] Zhang, Q., Hu, C., et al. "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models." arXiv:2510.04618, October 6, 2025 (cited in its original October 2025 version; later revisions exist). https://arxiv.org/abs/2510.04618v1

##### References and Secondary Sources [R]

[R1] Willison, S. "Context Engineering." June 27, 2025. https://simonwillison.net/2025/Jun/27/context-engineering/
[R2] Gartner. "Lead the Shift to Context Engineering as Prompt Engineering Fades." Gartner First Takes, July 28, 2025 (analyst guidance; cited for the adoption record). https://www.gartner.com/en/documents/6781234
[R3] Hong, K., Troynikov, A., and Huber, J. "Context Rot: How Increasing Input Tokens Impacts LLM Performance." Chroma Research technical report, July 14, 2025. https://www.trychroma.com/research/context-rot

##### Editorial Notes

- **Format.** This entry was the second written in the collection's entry format (Appendix A), and the first on a practice rather than a technical method. Its §4 uses the "Applications and Implementations" form of the §4 heading, as AES provides for entries whose subject is a practice.
- **The naming dates.** The Date of Appearance (January 23, 2023) records the term's earliest currently documented use — Goodside's remark as published by Willison that day [P0] — in line with the AES rule that appearance means first documented appearance, not prominence; June 2025 is treated throughout as the articulation-and-adoption sequence, not the coinage. The June sequence rests on dated primary artifacts (a dated essay and two dated posts). One secondary source dates the Lütke post June 18 rather than June 19; the entry uses June 19, the date carried by the post's other records.
- **Table production.** The §3.1 table follows the AES print-production rule: in the print build it starts on a fresh page, its header repeats if it ever spans pages, and no row is broken across a page boundary.
- **Retrospective note (outside the entry's 2025 coverage).** The ACE preprint [P10] was subsequently accepted to ICLR 2026. Under the collection's cutoff policy this fact is recorded here, in the editorial apparatus, and not in the entry body.
- **Source versions.** Where a cited source exists in multiple versions across the collection's cutoff, the reference gives the version-specific link, so that what the entry relies on remains auditable after later revisions appear: the survey [P6] and ACE [P10] are cited at their original 2025 versions (arXiv v1 links).
- **Review.** Peer-reviewed by GPT-6 and accepted by the editor. The dated record is in Appendix G.

##### Credits

- Written by Muse Spark 1.3.
- Peer review: GPT-6.

Accepted by the editor, W.H.L. The dated record of this entry (versions, audits, reviews and rulings) is in Appendix G.

##### Disclosures

###### Coverage

This entry synthesizes publicly available material through December 31, 2025. Post-2025 developments are excluded.

###### Source note

All dated claims in §§2–4 rest on the primary artifacts cited ([P1]–[P10]), consulted for this draft. Figures attributed to their authors (ACE's benchmark gains; Manus's token ratio and cache pricing) are reported as their sources state them and are marked as author-reported in §5; the component phenomena in §5.1 rest on independent studies.


## Context Rot

*Internal Concept ID AIKC-000003 · 1 record in 2025*

**New for the 2025 Collection** (origin `N`: commissioned for this collection; not published in 2025)

<a id="aik-2025-f-n-contextrot"></a>

### Context Rot — `AIK-2025-F-N-CONTEXTROT`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| F / N | standalone | 2025-06-18 | — |

AIKIPEDIA · FULL-LENGTH ENTRY

#### Context Rot

Long-Context Behavior · Evaluation · Agent Engineering

| | |
|---|---|
| **Date of Appearance** | June 18, 2025 (earliest currently documented use: a Hacker News comment by the user Workaccount2, recognized as a coinage the same day by Simon Willison [P1][R1]) |
| **Date of Original Publication** | — (new addition; no prior magazine publication) |
| **Historical Coverage** | Through December 31, 2025 |
| **Eligibility** | First appearance 2025, within the collection's first-appearance cutoff (2025 or earlier). No Aikipedia entry or headword for the term was published in 2026. Checked November 5, 2026 against site search and the headwords of three 2026 installments: *Agentic Lexicon (January–February 2026)* (Mar 2, 2026); *New AI Lexicon, May 2026 (1)* (May 31, 2026); *New AI Lexicon (July–September 2026)* (Oct 2, 2026) |
| **Original Contributor** | Claude Opus 5.5 (Anthropic) |
| **Peer review** | Muse Spark 1.3; GPT-6 |
| **Entry ID** | AIK-2025-F-N-CONTEXTROT (concept AIKC-000003) |

*Affiliation note.* The contributor is an Anthropic model. Two sources in this entry are Anthropic publications [P6][P7]. They are cited for what Anthropic said and released. Figures from them are identified as vendor-reported.

**Note on terminology.** "Context rot" has two senses, and they don't fully coincide.

- **The coinage sense.** The term was coined for a session-level experience: a running conversation or agent run degrades as the context fills with distractions, dead ends and the model's own mistakes. Here the emphasis is on the *quality* of what accumulates.
- **The measurement sense.** Within weeks, the term was attached to a controlled-measurement program. That program holds a task fixed and asks how performance changes as input length grows. Here the emphasis is on *quantity* and arrangement.

This entry treats both senses. It names which sense is meant wherever the difference matters. It also distinguishes context rot from **context overflow**, which is failure because input exceeds the window. Context rot occurs well inside the window.

##### 1. Definition

**Context rot** is the degradation of a large language model's output quality as the content of its context window grows. The degradation occurs within the model's advertised context limit, and it depends on more than length. What the added tokens are matters: irrelevant material, near-miss distractors, superseded or erroneous content. So does how the tokens are arranged.

In its originating sense, the term describes a property of *sessions*. The phrasing was a commenter's: models "poison their own context" [P1]. As a long chat or agent run accumulates dead ends and errors, output quality falls, and restarting with a clean, summarized context restores it.

In its measurement sense, the term names a property of *models*. Chroma's July 2025 technical report gives the reference formulation in the summary sentence displayed beneath its title: models "do not use their context uniformly," and their performance "grows increasingly unreliable as input length grows" [P2]. The body of the report puts the same finding as degradation "in surprising and non-uniform ways," even on deliberately simple tasks. See Editorial Note 7 on the location of these phrases.

Anthropic's September 2025 guidance framed it as recall: as tokens increase, "the model's ability to accurately recall information from that context decreases" [P6]. That is narrower than either sense above; context rot also affects reasoning and action selection (§5).

Three commitments recur across usages:

- Context rot is a **gradient, not a cliff**. Anthropic's phrase is "a performance gradient rather than a hard cliff" [P6].
- It is **content-sensitive, not only length-sensitive**.
- It is **operationally consequential**: claimed context length bounds what a model accepts, not what it reliably uses.

##### 2. Origin and Historical Development

**Before the name (2023–2025).** The phenomenon was documented before it was named.

- **Position effects (July 2023).** *Lost in the Middle* (Liu et al.; published in *TACL*, 2024) showed U-shaped position effects in multi-document question answering and key-value retrieval. Models used information at the beginning and end of the input better than information in the middle. The paper also showed that performance "substantially decreases as the input context grows longer, even for explicitly long-context models" [P3].
- **Distractor sensitivity (2023).** Shi et al. had shown that irrelevant context can derail model reasoning [R7].
- **The common benchmark and its critics (2023–2024).** The most widely used long-context test was the needle-in-a-haystack (NIAH) probe: retrieve one planted fact from filler text [R9]. Frontier models came to score near-perfectly on it, and benchmark designers argued that it overstated real capability.
- **Claimed vs. effective length (April 2024).** RULER introduced the distinction between a model's claimed and effective context length. It evaluated 17 long-context models on 13 tasks and found that almost all degraded substantially as length increased [P9].
- **Removing literal matches (February 2025).** NoLiMa (Modarressi et al.; ICML 2025) removed the literal word overlap between question and needle that NIAH allows models to exploit. In the first arXiv version's evaluation of 12 models, 10 fell below half of their short-context baselines by 32K tokens. GPT-4o fell from 99.3% to 69.7% [P4].

**June 2025: field evidence and the name.** On June 17, 2025, alongside the general availability of Gemini 2.5 Pro and Flash, Google DeepMind released the Gemini 2.5 technical report as a Google-hosted PDF. That edition is dated June 17, 2025; an arXiv edition followed in July [P8]. The report described its Pokémon-playing agent in detail. As the agent's context grew well beyond 100,000 tokens, it tended to favor repeating actions from its history over synthesizing new plans. The report calls this observation "albeit anecdotal" (§4.1). Its appendix separately names *context poisoning*: the agent fixating on misinformation in its context (§8.2) [P8].

On **June 18, 2025**, a Hacker News user posting as Workaccount2 described models poisoning their own context. The comment proposed the name: "Maybe you can call it context rot." It added that, even with good context, the rot became apparent around 100k tokens with Gemini 2.5. The commenter's workaround was to summarize a session and restart in a fresh context with the summary [P1].

Simon Willison replied in the thread the same day: "I think you just coined 'context rot', what an excellent term!" [P1]. That evening he republished the comment on his weblog, tagged "definitions," with the note that it was "coining 'context rot'" [R1]. His later gloss is useful for dating the original sense. Asked whether the term restated *Lost in the Middle*, he answered that context rot concerned models being distracted by poor-quality content already in the context, rather than missing details [R1].

**Late June 2025: a taxonomy.** Within days, practitioner writing supplied structure. Drew Breunig's "How Long Contexts Fail" (June 22, 2025) named four failure patterns [R2]:

- **context poisoning** (a term the Gemini report had used): an error enters the context and is repeatedly referenced;
- **context distraction:** a long context makes the model over-rely on its history;
- **context confusion:** superfluous content, such as too many tool definitions, degrades choices;
- **context clash:** accumulated content contradicts itself.

A follow-up post (June 26) named mitigations [R3]. Willison summarized the four patterns as patterns of context rot [R4], tying Breunig's taxonomy to the new term.

**July 2025: the measurement program.** On July 14, 2025, Chroma published *Context Rot: How Increasing Input Tokens Impacts LLM Performance* (Hong, Troynikov and Huber), with an open-source replication toolkit [P2]. The report evaluated 18 models from Anthropic, OpenAI, Google and Alibaba. It held task difficulty as constant as it could while varying input length, distractors, the similarity of needle to question and to haystack, and haystack structure (§5.1).

The report is the source most often cited for the term. It is often credited, wrongly, with coining it. The report itself makes no coinage claim and credits no one for the name (see Editorial Notes).

**September–December 2025: adoption into guidance and research.**

- **Vendor guidance (September 29).** Anthropic's guide *Effective Context Engineering for AI Agents* used "context rot" to motivate treating context as "a finite resource with diminishing marginal returns" [P6]. The same day, Anthropic released two platform features aimed at the problem, context editing and a memory tool [P7].
- **Research (October 6).** Du et al. reported that length alone degrades performance even when retrieval is perfect and the irrelevant tokens are masked (§5.2) [P5].
- **General audience (November 10).** Timothy B. Lee's *Understanding AI* presented context rot as an emerging challenge [R6].

By the end of 2025, the term named a practitioner diagnosis, an evaluation agenda and a design constraint.

##### 3. Conceptual or Technical Framework

###### 3.1 Three variables, separable in principle

The 2023–2025 literature manipulates three variables, which this entry treats as the components of context rot. The three-variable framework, and the session-level mapping in §3.2, are an editorial analytical framework drawn from the cited studies. No study has validated the framework as a whole; each cited study tests only its own variable under its own conditions.

**Table 1. The variables of context rot and how they have been manipulated.**

| Variable | Manipulation | Representative finding | Source |
|---|---|---|---|
| **Length per se** | Add tokens while keeping retrieval perfect; replace filler with whitespace; mask irrelevant tokens | Performance falls 13.9–85% across tasks as length grows, even with masked filler | Du et al. [P5] |
| **Content (interference)** | Lower the semantic similarity between question and answer; add distractors; vary topic match between needle and haystack | Degradation is steeper for low-similarity pairs; one distractor hurts, four compound the effect | Chroma [P2]; NoLiMa [P4] |
| **Arrangement (structure)** | Move relevant material through positions; shuffle vs. preserve haystack coherence | U-shaped position effects (Liu et al.); coherent haystacks hurt more than shuffled ones (Chroma) | [P3]; [P2] |

*Table note:* figures are as reported by the cited authors, under their stated conditions (§5).

The variables are separable in principle but confounded in practice. Longer real inputs usually also contain more distractors and more structure. Chroma lists the difficulty of separating input length from task complexity as a limitation of its own design [P2].

###### 3.2 The session dimension

The measurement literature mostly tests static inputs. The coinage sense adds a dynamic element: in a running session the model *writes its own context*. Tool outputs, abandoned plans and the model's earlier errors are appended and then re-read as evidence.

This entry reads Breunig's four patterns as session-level forms of the three variables above. The mapping is interpretive: Breunig did not classify his patterns this way, and the correspondence has not been tested experimentally.

- **Poisoning** is content interference originating from the model itself.
- **Distraction** is the length effect expressed as over-reliance on history.
- **Confusion** is irrelevant content.
- **Clash** is contradictory content.

On this reading, an agent's reliability over a long run is bounded by the model's long-context behavior *and* by the rate at which the harness admits low-value tokens [R2].

###### 3.3 Context rot is not overflow

Overflow and truncation are failures at the window boundary. Context rot is measured well inside it. NoLiMa makes the distinction operational. It defines a model's *effective length* as the longest context at which the model keeps at least 85% of its short-context score. For many models this is a small fraction of the claimed window [P4].

###### 3.4 Mechanism: proposed, not established

The 2025 sources offer explanations but establish none:

- **Anthropic's account.** It attributes the effect to attention's pairwise structure, in which relationships multiply as the square of context length, and to training distributions in which long sequences are rarer [P6]. This is a vendor's explanatory account, not a demonstrated mechanism.
- **Chroma's position.** It states that its report does not explain the mechanisms. It names interpretability research on how input structure affects attention as future work [P2].
- **Du et al.'s result.** Their masking result constrains explanations. If performance falls when irrelevant tokens are masked and attention reaches only the evidence and the question, distraction alone cannot account for the effect [P5].

##### 4. Applications and Implementations

As a diagnosis, context rot shaped practice in four implemented forms.

**Session hygiene.**
- *Summarize-and-restart.* The originating comment described this workaround: periodically summarize a session, then continue in a fresh context seeded with the summary [P1]. It became standard advice for interactive and coding-agent use.
- *Selective rollback* to before the context was poisoned, suggested in the same thread [P1].

**Named mitigation patterns.** Breunig's "How to Fix Your Context" (June 26, 2025) named six techniques for managing the four failure patterns [R3]. Besides retrieval-augmented generation, they are:
- tool loadout (exposing only relevant tools);
- context quarantine (isolating work in separate contexts or sub-agents);
- context pruning;
- context summarization;
- context offloading (storing information outside the window).

**Platform features.** On September 29, 2025, Anthropic introduced two features on its developer platform [P7]:
- *context editing*, which automatically clears stale tool results as context grows;
- a *memory tool*, which lets agents store and retrieve information in files outside the window.

Anthropic's accompanying engineering guidance recommended related strategies: compaction, structured note-taking, just-in-time retrieval and sub-agent architectures [P6].

**Prompt-level mitigation.** Du et al. proposed a model-agnostic step: have the model recite the retrieved evidence, then answer from a short prompt built from that recitation. This turns a long-context task into a short one [P5].

##### 5. Evidence and Evaluation

All figures below are author-reported, under the evaluation conditions stated. The source checks for this entry did not establish independent replications of the specific headline results cited. That is a statement about this review, not the result of a replication survey.

###### 5.1 The Chroma study (July 2025)

The report evaluated 18 models: five Anthropic, seven OpenAI, three Google and three Alibaba Qwen3. Not every model appears in every experiment. Some models were run in both thinking and non-thinking modes. The report cites 194,480 model calls [P2]. Its experiments and author-reported results:

- **Needle–question similarity (an NIAH extension).** Similarity was averaged across five embedding models; needles were tested at 11 positions. Performance degraded faster with length for low-similarity pairs. Needle position had no notable effect in this design.
- **Distractors.** A single distractor reduced accuracy, and four compounded the loss. The effect differed by distractor. Model families differed in how they failed: Claude models had the lowest hallucination rates and tended to abstain when uncertain, while GPT models had the highest rates of confident wrong answers.
- **Needle–haystack similarity.** Results were mixed across two topic sets. The authors caution that two topics cannot support generalization.
- **Haystack structure.** Across all 18 models, haystacks with randomly shuffled sentences produced *better* performance than coherent ones. The authors call the result counterintuitive and suggest it may reflect attention patterns.
- **LongMemEval.** 306 conversational question-answering prompts were posed in two forms: focused (about 300 tokens of relevant material) and full (about 113,000 tokens including irrelevant material). Every model scored significantly higher on focused prompts. Thinking modes narrowed the gap but did not close it.
- **Repeated words.** Models had to reproduce a long sequence of one repeated word with a single unique word inserted. Performance declined as length grew from 25 to 10,000 words. Some models refused or produced unrelated output at longer lengths. Because the required output grows with the input, this experiment measures input- and output-length effects together. Under-generation, refusals and other generation failures cannot all be attributed solely to difficulty processing the input.

**Measurement conditions.** Several experiments were scored by a language-model judge (GPT-4.1, aligned against human judgments) rather than by exact match [P2] (see Editorial Note 8). The reported patterns are therefore conditional on the report's evaluation design: its tasks, its scoring and its model versions.

The report's stated limitations:
- its tasks are simpler than real use;
- length cannot be fully separated from difficulty;
- it does not identify mechanisms;
- its topic coverage is narrow for the needle–haystack experiment [P2].

###### 5.2 Corroborating controlled studies

- **Lost in the Middle (2023).** Position-dependent accuracy and a length penalty in multi-document QA and key-value retrieval [P3].
- **RULER (2024).** Across 17 long-context models and 13 tasks, almost all models showed large drops as context length increased [P9].
- **NoLiMa (2025).** With literal-match cues removed, 10 of 12 models fell below 50% of their short-context baselines at 32K tokens; GPT-4o fell from 99.3% to 69.7% (arXiv v1). Later arXiv versions and the ICML proceedings report a 13-model evaluation, with 11 models below half; the GPT-4o figures are unchanged. See Editorial Note 3 [P4].
- **Du et al. (October 2025).** Five models were tested on math, question-answering and coding tasks. Accuracy fell 13.9–85% as input length grew, while retrieval of the relevant evidence stayed exact. A similar drop appeared when filler was whitespace, when irrelevant tokens were masked, and when all evidence was placed immediately before the question. One example: Llama-3.1-8B-Instruct retrieved the evidence exactly for 970 of 1,000 MMLU problems extended to 30K tokens, yet lost 24.2% accuracy relative to the short form [P5].

**A divergence to record.** Chroma found no notable position effect across 11 needle positions in its similarity experiment [P2], while Liu et al. found strong position effects [P3]. The studies differ in task, model generation and needle design. The literature does not settle whether position effects weakened in newer models or are task-specific.

###### 5.3 Field observation (report-level evidence)

- The Gemini 2.5 report's observation that its Pokémon agent, past roughly 100K tokens, favored repeating past actions over new planning is a single-system case study, reported by the developer and described by the report itself as anecdotal [P8].
- Practitioner reports [P1] are anecdotal, cited for the term's origin, not effect sizes.

###### 5.4 Mitigation evidence

Anthropic reported that, on an internal evaluation of agentic search, combining the memory tool with context editing improved performance by 39% over baseline, and context editing alone by 29% [P7]. These are vendor-reported, internal-benchmark results. Du et al. report gains of up to 4% for GPT-4o on RULER from their recitation strategy [P5].

###### 5.5 Status of the evidence

Three claims rest on independent groups using different methods. Each holds for the tasks and conditions studied; none is established as a universal property of language models.
- Performance degrades within the advertised window.
- On the tasks studied, degradation is steeper when lexical cues are removed or semantically similar distractors are added than on literal-retrieval probes. This is task-dependent, not a general ordering of semantic over lexical difficulty.
- NIAH-style tests give weak evidence of long-context competence on harder tasks.

**Unsettled at the end of 2025:**
- the size of the effect on real tasks;
- its mechanism;
- its trend across model generations.

##### 6. Significance and Implications

**It reframed the context window as a quality-bounded resource.** Through 2024 context length was marketed as capacity, measured in tokens accepted. Context rot gave practitioners a name for the gap between capacity and reliable use. Benchmarks such as RULER and NoLiMa had already formalized that gap as effective length. The reframing changed the design question from how much a model can take to how much it should be given.

**It supplied context engineering with its central constraint.** On this entry's reading, the 2025 discipline of context engineering is in large part a response to context rot. The relationship is interpretive, not experimentally demonstrated. Anthropic's guidance makes the link explicit, deriving its principle of the smallest high-signal context from the finite "attention budget" [P6]. If context degrades as it grows, curation becomes a requirement of reliability rather than an optional optimization.

**It changed how long-context capability is evaluated.** Chroma [P2] and NoLiMa [P4] both argue that evaluation must go beyond tests on which frontier models are already saturated. By late 2025, a near-perfect NIAH score was treated as weak evidence of usable long-context competence.

**It bounds long-horizon agents.** Agent runs accumulate context by construction. If quality falls as context grows, an agent's reliable horizon depends on the harness as well as on the model: on what the harness admits, removes and offloads. Context rot is therefore a property of systems as well as models (§4).

##### 7. Limitations, Debates, and Open Questions

- **Two senses, one name.** The coinage sense concerns what accumulates, especially errors and dead ends. The measurement sense concerns length and arrangement under fixed content. Willison drew the distinction when the term was days old [R1]. Later usage often merges the two, and Anthropic's recall-centered definition [P6] narrows the term further. Claims about "context rot" should be read for which sense is meant.
- **Length vs. difficulty.** Longer inputs are usually harder inputs. The controlled designs (Chroma, Du et al.) work to separate the two, and both acknowledge residual confounds [P2][P5].
- **Synthetic tasks vs. real use.** Most evidence comes from simplified tasks. Chroma states that real tasks are likely more complex [P2]. Production-scale effects are documented mainly in vendor and practitioner reports.
- **Generation dependence.** Results describe the models tested in 2023–2025. Whether context rot is intrinsic to current attention-based architectures or responsive to long-context training was not settled by the end of 2025. The proposed explanations (§3.4) remain hypotheses.
- **Counter-evidence: more context can help.** Context rot is not a general law that more context is worse. Many-shot in-context learning showed large gains from filling the context with examples [R8], and retrieval often helps when what is added is relevant. The phenomenon concerns low-value or poorly arranged tokens, not context as such.
- **Attribution confusion.** Secondary sources frequently credit Chroma with coining the term [Editorial Note 2]. Dating the term to July wrongly places practitioner diagnosis after formal measurement.

**Open questions.** Three define the next phase:
- whether context rot can be reduced at the model level (training, positional schemes, attention modifications) or only managed at the system level;
- how to measure it on realistic, long-horizon agent tasks rather than synthetic probes;
- whether a model can be trained to manage its own context reliably (deciding what to keep, compress or forget) without introducing new failure modes of its own.

##### 8. Related Concepts and Distinctions

- **Context engineering.** The discipline of curating what a model sees; on this entry's reading (§6), the practice that manages context rot.
- **Context window / context length.** The maximum input a model accepts. Context rot concerns degradation within it.
- **Effective context length.** The longest length at which a model meets a performance threshold (§3.3).
- **Lost in the middle (positional bias).** Position-dependent use of context. It is one component of context rot, not the whole of it.
- **Needle in a haystack (NIAH).** The literal-retrieval probe whose saturation the context-rot literature criticizes.
- **Context poisoning, distraction, confusion, clash.** Breunig's session-level failure patterns. Under the session sense of context rot (§3.2), they are its forms.
- **Distractor sensitivity.** Degradation caused by irrelevant or near-miss content: one cause of context rot.
- **Context overflow (truncation).** Failure at the window boundary, unlike context rot (§3.3).
- **Compaction and summarization.** Mitigations that replace accumulated context with a condensed version; the originating workaround for context rot.

##### See Also

Published in this magazine's Aikipedia series, in the 2025 collection:

- **Context Engineering.** New addition to this collection, AIK-2025-F-N-CONTEXTENG.
- **Long-Context & Windowing Techniques.** *New AI Lexicon 2025*, Launch Edition (Nov 30, 2025), short-form recommended list.
- **Retrieval-Augmented Generation (RAG): next-gen.** *New AI Lexicon 2025*, Launch Edition (Nov 30, 2025), short-form recommended list.
- **Compound AI Systems.** *New AI Lexicon 2025* (3) (Dec 2, 2025).
- **Test-Time Compute Scaling.** *New AI Lexicon 2025* (3) (Dec 2, 2025).

Outside this collection (Aikipedia 2026): **Context Window Optimization** and **Context Window**, *Agentic Lexicon (January–February 2026)*.

##### References and Sources

**Primary Sources**

- [P1] Workaccount2. Comment on Hacker News, June 18, 2025 (Unix time 1750255791, about 14:10 UTC), item 44310054 (thread 44308711). https://news.ycombinator.com/item?id=44310054 — Earliest currently documented use of the term. The same page carries Simon Willison's same-day in-thread reply recognizing the coinage, and the rollback remark cited in §4.
- [P2] Hong, K., Troynikov, A., and Huber, J. "Context Rot: How Increasing Input Tokens Impacts LLM Performance." Chroma technical report, July 14, 2025. https://www.trychroma.com/research/context-rot ; replication toolkit: https://github.com/chroma-core/context-rot — The measurement program; 18 models.
- [P3] Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., and Liang, P. "Lost in the Middle: How Language Models Use Long Contexts." arXiv:2307.03172 (July 6, 2023); *Transactions of the Association for Computational Linguistics* 12 (2024). https://arxiv.org/abs/2307.03172 ; DOI 10.1162/tacl_a_00638 — Position effects and the length penalty.
- [P4] Modarressi, A., Deilamsalehy, H., Dernoncourt, F., Bui, T., Rossi, R. A., Yoon, S., and Schütze, H. "NoLiMa: Long-Context Evaluation Beyond Literal Matching." arXiv:2502.05167 (February 7, 2025); *Proceedings of the 42nd International Conference on Machine Learning*, PMLR 267:44554–44570 (2025). Version cited for the 12-model figures: arXiv:2502.05167v1, https://arxiv.org/abs/2502.05167v1 . Later arXiv versions and the proceedings report 13 models (Editorial Note 3). — Degradation without literal-match cues; the effective-length threshold.
- [P5] Du, Y., Tian, M., Ronanki, S., Rongali, S., Bodapati, S., Galstyan, A., Wells, A., Schwartz, R., Huerta, E. A., and Peng, H. "Context Length Alone Hurts LLM Performance Despite Perfect Retrieval." arXiv:2510.05381 (October 6, 2025). https://arxiv.org/abs/2510.05381 — The length-alone result and the recitation mitigation.
- [P6] Anthropic Applied AI team. "Effective Context Engineering for AI Agents." Anthropic Engineering, September 29, 2025. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — The vendor framing of context rot and the attention-budget account.
- [P7] Anthropic. "Managing Context on the Claude Developer Platform" (context editing and the memory tool). September 29, 2025. https://www.anthropic.com/news/context-management — Platform mitigations; vendor-reported internal evaluation figures.
- [P8] Gemini Team, Google. "Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities." Two editions:
  - (a) Original Google-hosted technical report, dated June 17, 2025, released with the Gemini 2.5 general-availability announcement of the same date: https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf
  - (b) arXiv edition, arXiv:2507.06261, first submitted July 7, 2025 and revised through December 2025: https://arxiv.org/abs/2507.06261

  The June 2025 dating in §2 rests on edition (a). Locations in edition (a): §4.1, Long Context Reasoning, printed p. 18 (the 100K observation); Appendix §8.2, printed pp. 70–71 (context poisoning). See Editorial Note 4.
- [P9] Hsieh, C.-P., Sun, S., Kriman, S., et al. "RULER: What's the Real Context Size of Your Long-Context Language Models?" arXiv:2404.06654 (April 2024); COLM 2024. https://arxiv.org/abs/2404.06654 — Claimed vs. effective context length.

**Additional References**

- [R1] Willison, S. Quotation of Workaccount2, "coining 'context rot'." simonwillison.net, June 18, 2025 (posted 23:15 UTC), tagged "definitions." https://simonwillison.net/2025/Jun/18/context-rot/ . Same-day Mastodon post: https://fedi.simonwillison.net/@simon/114706938101130641 ; the reply distinguishing context rot from *Lost in the Middle* is in that Mastodon thread. — Same-day recognition of the coinage; the early gloss of the original sense.
- [R2] Breunig, D. "How Long Contexts Fail." dbreunig.com, June 22, 2025. https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html . Republished, with [R3], by O'Reilly Radar as "Managing Your Context Is the Key to Successful Agents." — The four failure patterns.
- [R3] Breunig, D. "How to Fix Your Context." dbreunig.com, June 26, 2025. https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html — Six named mitigation tactics.
- [R4] Willison, S. Link post on "How to Fix Your Context," simonwillison.net, June 29, 2025. https://simonwillison.net/2025/Jun/29/ — Describes Breunig's four patterns as patterns of context rot.
- [R5] Breunig, D. "DeepMind Shows Us the Messy Reality of Agent Building." dbreunig.com, June 17, 2025. https://www.dbreunig.com/2025/06/17/an-agentic-case-study-playing-pokémon-with-gemini.html — Same-day practitioner reading of the Gemini 2.5 report's agent appendix; retained as context, since the observation is now cited to [P8] directly.
- [R6] Lee, T. B. "Context rot: the emerging challenge that could hold back LLM progress." *Understanding AI*, November 10, 2025. https://www.understandingai.org/p/context-rot-the-emerging-challenge — General-audience consolidation; dates the coinage to a June Hacker News comment.
- [R7] Shi, F., Chen, X., Misra, K., et al. "Large Language Models Can Be Easily Distracted by Irrelevant Context." ICML 2023. arXiv:2302.00093. https://arxiv.org/abs/2302.00093 — Pre-name distractor evidence, cited by [P2].
- [R8] Agarwal, R., Singh, A., Zhang, L. M., et al. "Many-Shot In-Context Learning." NeurIPS 2024. arXiv:2404.11018. https://arxiv.org/abs/2404.11018 — Counter-evidence: gains from long contexts filled with relevant examples.
- [R9] Kamradt, G. "Needle In A Haystack — Pressure Testing LLMs." GitHub repository, 2023. https://github.com/gkamradt/LLMTest_NeedleInAHaystack — The NIAH probe.

##### Editorial Notes

1. **Date of Appearance.** The date records the earliest currently documented use [P1], following the AES rule that appearance means documented first use, not prominence. The comment is timestamped June 18, 2025, about 14:10 UTC. One secondary source asserts that the phrase recurred in "late 2024 and 2025 threads," but gives no instance, and it is not relied on. No exhaustive search was undertaken, so the date is the earliest documented use, not a proven first use.
2. **Attribution of the coinage.** Several secondary sources state that Chroma "coined" the term in July 2025. That is incorrect: the Chroma report postdates [P1] by about four weeks, and it makes no coinage claim and credits no one [P2]. This entry credits the coinage to [P1] and the measurement program to [P2]. Willison's in-thread reply [P1] and quotation post [R1] are cited for dating and gloss only.
3. **NoLiMa versions.** The first arXiv version (v1, February 7, 2025) reports 12 models, 10 below 50% of baseline at 32K. Later arXiv versions and the ICML proceedings report 13 models and 11. GPT-4o's 99.3% → 69.7% is the same in all versions. The entry cites v1 explicitly for the 12/10 figures.
4. **Gemini 2.5 report.** The report exists in two editions, cited separately at [P8]: the original Google-hosted PDF, dated June 17, 2025 and released with the general-availability announcement that day, and the arXiv edition, first submitted July 7, 2025. The passage is quoted from the Google-hosted PDF (§4.1, p. 18; see also the context-poisoning appendix, §8.2, pp. 70–71). The report's own "albeit anecdotal" hedge is reflected in §§2 and 5.3. Limit: no archived June 17 timestamp for the PDF file itself was independently established; the June 17 date rests on the document's own dating and the same-day announcement.
5. **Cross-references.** The two Launch Edition See Also targets are items in that edition's short-form recommended list, not standalone entries. The two 2026 targets are marked as outside the collection.
6. **Anthropic sources.** The guide cited at [P6] itself names context rot and links to the Chroma report.
7. **Chroma quotation location.** The two §1 phrases are the report's summary sentence, printed beneath its title.
8. **Chroma scoring method.** The judge detail is in the report itself: "We evaluate model outputs using an aligned GPT-4.1 judge." The judge covered the needle-in-a-haystack and LongMemEval experiments, calibrated against manually labeled outputs.

##### Credits

- Written by Claude Opus 5.5.
- Peer review: Muse Spark 1.3 and GPT-6.

Accepted by the editor, W.H.L. The dated record of this entry (versions, audits, reviews and rulings) is in Appendix G.

## Dynamic Planning for LLM Agents

*Internal Concept ID AIKC-000043 · 1 record in 2025*

<a id="aik-2025-s-p-dynplan"></a>

### Dynamic Planning for LLM Agents — `AIK-2025-S-P-DYNPLAN`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L1-M5 | 2025-09-03 | 2025-11-30 |

#### L1-M5 — Dynamic Planning for LLM Agents (type S)

**Date of Appearance:** September 3, 2025 (Paglieri et al., arXiv:2509.03581v1)  
**Public Entry ID:** `AIK-2025-S-P-DYNPLAN` · **Internal Concept ID:** AIKC-000043  
**Concept:** C:DYNPLAN

*As published:* **Definition:** A meta-cognitive planning approach where agents learn when to plan (vs. acting directly), optimizing planning cost and success probability. **Why 2025:** First formal learning framework for adaptive planning schedules. **References:** • Anonymous. Learning When to Plan: Efficiently Allocating Test-Time Compute for LLM Agents. arXiv (2025).

**References (corrected record):** Paglieri, D., Cupiał, B., Cook, J., Piterbarg, U., Tuyls, J., Grefenstette, E., Foerster, J. N., Parker-Holder, J., & Rocktäschel, T. (2025). *Learning When to Plan: Efficiently Allocating Test-Time Compute for LLM Agents.* arXiv:2509.03581. [C02]


## EvoAgent — Continual World-Model Agents

*Internal Concept ID AIKC-000045 · 1 record in 2025*

<a id="aik-2025-s-p-evoagent"></a>

### EvoAgent — Continual World-Model Agents — `AIK-2025-S-P-EVOAGENT`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L1-M7 | 2025-02-09 | 2025-11-30 |

#### L1-M7 — EvoAgent — Continual World-Model Agents (type S)

**Date of Appearance:** February 9, 2025 (Feng et al., arXiv:2502.05907)  
**Public Entry ID:** `AIK-2025-S-P-EVOAGENT` · **Internal Concept ID:** AIKC-000045  
**Concept:** C:EVOAGENT

*As published:* **Definition:** Agents that autonomously build and update a world model, reflect, revise, and evolve their own behavior without curated curricula. **Why 2025:** First time continual world-model agents matched SOTA on long-horizon environments. **References:** • Feng, T., Wang, X., Zhou, Z., et al. EvoAgent: Agent Autonomous Evolution with Continual World Model. arXiv (2025).

**Why 2025 (corrected record):** Feng et al. (arXiv:2502.05907) report, in Minecraft, an average success-rate improvement of 105% over existing methods and more than 6× fewer ineffective actions. [C05]


## Generative User Interfaces (GenUI)

*Internal Concept ID AIKC-000024 · 1 record in 2025*

<a id="aik-2025-f-p-genui"></a>

### Generative User Interfaces (GenUI) — `AIK-2025-F-P-GENUI`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| F / P | standalone | 2023-10-11 | 2025-11-29 |

#### Generative User Interfaces (GenUI)

*Corrected collection text. The original publication is preserved unchanged in the Historical Lexicon Archive.*

| Field | Value |
|---|---|
| **Term** | Generative User Interfaces (GenUI); Generative UI |
| **Date of Appearance** | October 11, 2023 (Vercel, "Announcing v0: Generative UI"). Vercel had described v0 as a "generative user interface system" at its launch in September 2023. Earliest documented use identified; not an exhaustive priority claim |
| **Date of Original Publication** | November 29, 2025 (Champaign Magazine, post 14146) |
| **Historical Coverage** | Through November 29, 2025, the date of original publication. Corrections rely only on sources available by that date |
| **Original Contributor** | Gemini 3 Pro (Google), sole contributor, writing about a feature of Gemini 3 |
| **Original Reviewers** | None named in the post |
| **Corrections Prepared by** | Claude Opus 5.5 (Anthropic) |
| **Independent review** | GPT-6 |
| **Base version** | The Gemini 3 Pro entry text (basis: sole published version; Gemini 3 Pro is the post's sole contributor) |
| **Entry ID** | AIK-2025-F-P-GENUI |

*Markers: `[Cnn]` marks a corrected or added passage and `[ST01]` the rearrangement into AES sections, documented in the entry's correction register. Unmarked text is the original's own wording (archive lines A-005 to A-062).*

##### 1. Definition

Generative User Interfaces (GenUI), also known as Generative UI, is a paradigm in human-computer interaction where a user interface (UI) is dynamically and automatically generated by an artificial intelligence model in real-time, rather than being pre-programmed by a developer.

This approach represents a fundamental shift from traditional static interfaces. Instead of every user seeing the same fixed layout, a GenUI system can create or adapt an interface specifically for a user's context, intent, or query. For example, rather than just replying with text, an AI might generate an interactive map, a data dashboard, or a custom booking form to best solve the user's problem.

##### 2. Origin and Historical Development

The term was in use before 2025. Vercel launched v0 in September 2023 as a "generative user interface system" and named the approach "Generative UI" on October 11, 2023 [9]; on March 1, 2024 it released AI SDK 3.0 "with Generative UI support" [10]. Chen et al. proposed generative interfaces for language models in an August 2025 preprint [2]. On November 18, 2025, Google Research presented "a novel implementation of generative UI" for Gemini 3 [3]. [C01]

##### 3. Conceptual or Technical Framework

GenUI is not a single technology but a spectrum of approaches, ranging from high-control, developer-defined methods to fully autonomous AI generation. [4] [C06]

| Generation Method | Description | Example |
|---|---|---|
| **1. Static Generation** | The AI's role is to select the correct UI from a fixed library of pre-built, human-designed components. | A user asks, "What's the weather?" and the AI selects and displays a pre-made "Weather Widget." |
| **2. Declarative Generation** | The AI generates a structured specification (e.g., a JSON schema or React component tree) that describes the interface's layout and elements. A front-end system then interprets this specification and renders the UI. | A user asks for a sales comparison, and the AI generates a spec: {"type": "BarChart", "data": [...], "title": "Q3 vs Q4"}. |
| **3. Open-Ended Generation** | The AI generates the raw, "full-stack" UI code (e.g., HTML, CSS, and JavaScript) from scratch. This method offers maximum flexibility but is the most difficult to control. | A user says, "Make me a simple timer app," and the AI writes and executes the complete code for a functional timer. |

Declarative Generation provides the flexibility of AI while maintaining brand consistency, security, and predictability by limiting the AI to a set of pre-approved components (like a "digital Lego set"). [C05]

##### 4. Applications and Implementations

*From the post's preliminary answer by the same contributor (A-005 to A-008), on Gemini 3:* [ST01]

Gemini 3 moves beyond static text-and-image responses by generating adaptive, interactive user interfaces (UIs) on the fly. Instead of describing a solution, the model builds an interactive tool for the user.

Two primary examples of this new approach are:

- **Visual Layout:** For prompts like travel planning, the model generates an immersive, magazine-style layout with interactive modules, maps, and images that the user can click and modify.
- **Dynamic View:** This uses agentic coding to design and render a custom UI perfectly suited for the query. For example, a query about art history might return an interactive, scrollable virtual gallery rather than a simple wall of text. This capability is also being integrated directly into Google Search.

##### 5. Evidence and Evaluation

*Not in original.* The original reports no evaluation. [ST01]

##### 6. Significance and Implications

This capability allows an AI agent to move beyond text-based conversation and build the exact tools a user needs on the fly. [C05] [ST01]

- **Hyper-Personalization:** The UI can adapt to an individual user's expertise, goals, and history. A novice user might see a step-by-step wizard, while an expert sees a dense data dashboard for the exact same task.
- **Contextual Adaptability:** The interface can change in real-time based on new information. A travel app's home screen could change from a "booking" layout to a "live-trip" layout (showing boarding passes and maps) the moment the user arrives at the airport.
- **Reduced Friction:** By generating the perfect tool for the job (e.g., a calculator, a-to-b directions), the AI eliminates the clicks and navigation required to find that tool within a traditional application.
- **Development Velocity:** GenUI can automate the creation of simple UIs, forms, and data visualizations, freeing developers to focus on more complex logic rather than repetitive front-end code.

##### 7. Limitations, Debates, and Open Questions

Despite its potential, the GenUI paradigm introduces significant technical and ethical challenges.

- **Loss of Control and Consistency:** An AI given full creative freedom may generate UIs that are "soulless," off-brand, or functionally inconsistent, leading to a confusing user experience.
- **Security Vulnerabilities:** Open-ended generation is highly vulnerable to risks like Prompt Injection, where a malicious user could trick the AI into generating code that steals data or performs unauthorized actions. [5] [C06]
- **Accessibility and Usability:** An AI model does not inherently understand human-centric design principles like WCAG (Web Content Accessibility Guidelines). It can easily generate interfaces that are inaccessible to users with disabilities (e.g., poor color contrast, unnavigable by keyboard). [6] [7] [C06]
- **Bias and Ethics:** The AI may perpetuate biases present in its training data, leading to UIs that are discriminatory or exclusionary. [1] [C06]
- **Performance and Cost:** Generating a UI in real-time is far more computationally expensive (and thus slower) than serving a pre-built, static file. This can lead to noticeable latency for the user.
- **The "Black Box" Problem:** When a GenUI fails or produces a bug, it can be extremely difficult to debug, as the layout was not written by a human and may be different every time it's generated.

##### 8. Related Concepts and Distinctions

*Not in original.* Related terms are listed under See Also. [ST01]

##### See Also

*Cross-reference markings (editorial, not part of the original): targets in the collection carry their Public Entry IDs; the others are marked as having no entry.*

- Foundation Agent — *no entry in the 2025 collection*
- ReAct (Reasoning and Acting) — *no entry in the 2025 collection*
- Multimodality — *no entry in the 2025 collection*
- Human-Computer Interaction (HCI) — *no entry in the 2025 collection*

##### References and Sources

1. Mend.io (September 2025). "Understanding Bias in Generative AI: Types, Causes & Consequences." Provides a comprehensive overview of how biases (racial, gender, cultural) are embedded in training datasets and amplified by generative models, leading to discriminatory or exclusionary outputs.
2. Chen, Jiaqi, et al. (August 2025). "Generative Interfaces for Language Models." arXiv preprint arXiv:2508.19227. Proposes generative interfaces for language models, with structured interface representations, and evaluates them against conventional chat interfaces. [C04]
3. Leviathan, Y., Valevski, D., Natchu, V., & Matias, Y. (November 18, 2025). "Generative UI: A rich, custom, visual interactive user experience for any prompt." Google Research Blog. https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/ Presents "a novel implementation of generative UI" in Gemini 3. [C02] [C03]
4. Berman, Eli (September 12, 2025). "The Three Types of Generative UI: Static, Declarative and Fully Generated." CopilotKit Blog. https://www.copilotkit.ai/blog/the-three-kinds-of-generative-ui [C08] Provides a clear, developer-focused taxonomy for GenUI, explaining the practical trade-offs between safety and flexibility for each generation method. This is the source for the "Spectrum of Generation" table.
5. OWASP (2025). "LLM01: Prompt Injection." OWASP Top 10 for Large Language Model Applications. The leading security-focused reference that defines prompt injection as the top vulnerability for LLM-based systems, which directly applies to Open-Ended GenUI models.
6. AudioEye (July 2025). "How WCAG Guidelines Apply to AI-Generated Content." AudioEye Blog. A detailed analysis of the accessibility challenges inherent in AI-generated content, specifically citing common failures in color contrast, alt text, and semantic HTML structure (WCAG 1.1.1, 1.4.3, 1.3.1).
7. Smith, Aleksandra (September 2025). "AI-generated UX and the growing accessibility debt (+ how to fix it)." [C09] Medium (Design Bootcamp). Discusses how AI models trained on existing, often inaccessible, web data perpetuate and "systematically" create accessibility failures, such as poor touch-target sizes and missing focus indicators.
8. Alabduljabbar, R. (October 25, 2024). "User-centric AI: evaluating the usability of generative AI applications through user reviews on app stores." PeerJ Computer Science (https://doi.org/10.7717/peerj-cs.2421); indexed in PubMed Central. A usability evaluation of five generative AI apps based on 11,549 app-store reviews. [C04]
9. Vercel (October 11, 2023). "Announcing v0: Generative UI." Vercel Blog. https://vercel.com/blog/announcing-v0-generative-ui [C01]
10. Vercel (March 1, 2024). "Introducing AI SDK 3.0 with Generative UI support." Vercel Blog. https://vercel.com/blog/ai-sdk-3-generative-ui [C01]

##### Editorial Notes

1. **Status.** Independently reviewed and accepted by the editor. The dated record is in Appendix G.
2. **Vendor affiliation.** The entry was written by Gemini 3 Pro, a Google model, about a feature of Google's Gemini 3, with no reviewer. §4 repeats the contributor's own description of Gemini 3 and is not independently verified.
3. **Unmerged revision (C07).** The post ends with a suggested new lead and a reference [1] that were never merged into the entry (A-070 to A-074). They are not carried. The lead says GenUI was "introduced by Google Research in November 2025", which is the error corrected by C01. Its reference [1] omits an author (C03). The corrected reference is [3].
4. **In-text citations (C06).** The original entry cites nothing in its text. The markers added here follow the post's own annotations of what each reference supports. Those annotations are Gemini 3 Pro's claims about its sources, not independent verification. The independent review found the sources real and generally supportive: [1], [5], [6] and [7] are practitioner or reference articles rather than studies of GenUI itself. A marker is therefore not a finding that every cited claim is established. The "Black Box" and performance points have no reference in the original and are left uncited.
5. **Source-date rule.** Every source used to correct the text was available by November 29, 2025: Vercel's posts (2023, 2024), the Google Research post (November 18, 2025) and the PeerJ article (October 2024).
6. **Conflict.** None for the preparer: no Anthropic model contributed to the post.

##### Credits

- Source audits: Claude Opus 5.5 (first audit) and Muse Spark 1.3 (second audit).
- Corrections: Claude Opus 5.5.
- Independent review: GPT-6.

Accepted by the editor, W.H.L. The dated record of this entry (versions, audits, reviews and rulings) is in Appendix G.

## GraphRAG

*Internal Concept ID AIKC-000084 · 1 record in 2025*

<a id="aik-2025-s-p-graphrag"></a>

### GraphRAG — `AIK-2025-S-P-GRAPHRAG`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L4-G8 | — (not established) | 2025-12-03 |

#### L4-G8 — GraphRAG (type S)

**Public entry ID:** `AIK-2025-S-P-GRAPHRAG` — **Concept:** GRAPHRAG.
**Date of Appearance:** Not established. The entry states Microsoft's framework (2024) with 2025 maturation; no appearance ruling.
**Contributor:** Grok 4.1. Two published short text states.

*Text 1 (as published, corrections marked):* **GraphRAG**: Graph-augmented RAG, popularized by Microsoft in 2024 and matured in 2025 with enterprise implementations like auto-tuning.[C03 — the VeriTrail clause is removed without replacement; original: "with enterprise implementations like auto-tuning and VeriTrail."] Enhances relational retrieval over standard RAG.

*Text 2 (as published, corrections marked):* GraphRAG augments RAG with knowledge graphs for relational data. Microsoft’s 2024 framework matured in 2025 for enterprise.[C03 — the VeriTrail clause is removed without replacement; original: "Microsoft’s 2024 framework matured in 2025 with tools like VeriTrail for enterprise."] Example: Connecting legal entities in research for accurate Q&A.

**Why It Matters in 2025**: Improves RAG accuracy in complex queries; scalability challenges drive adoption in knowledge bases.

*Editorial note:* VeriTrail is a Microsoft Research hallucination-detection method (arXiv:2505.21786), not a GraphRAG tool or enterprise product; one of its evaluation datasets is a GraphRAG question-answering process, the probable source of the slide.


## Large-Scale Population Agent Simulation (LLM Archetypes)

*Internal Concept ID AIKC-000048 · 1 record in 2025*

<a id="aik-2025-s-p-popagentsim"></a>

### Large-Scale Population Agent Simulation (LLM Archetypes) — `AIK-2025-S-P-POPAGENTSIM`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L1-M10 | 2024-09-14 | 2025-11-30 |

#### L1-M10 — Large-Scale Population Agent Simulation (LLM Archetypes) (type S)

**Date of Appearance:** September 14, 2024 (Chopra et al., arXiv:2409.10568v1; AAMAS 2025) [C03]  
**Public Entry ID:** `AIK-2025-S-P-POPAGENTSIM` · **Internal Concept ID:** AIKC-000048  
**Concept:** C:POPAGENTSIM

*As published:* **Definition:** Simulations with millions of lightweight LLM agents, each instantiated from shared archetypes, enabling social, economic, and policy modeling. **Why 2025:** First 2025 AAMAS paper demonstrated stable million-agent LLM simulation. **References:** • MIT Media Lab. On the Limits of Agency in Agent-Based Models. AAMAS (2025).

**References (corrected record):** Chopra, A., Kumar, S., Giray-Kuru, N., Raskar, R., & Quera-Bofarull, A. (2025). *On the limits of agency in agent-based models.* Proceedings of AAMAS 2025. arXiv:2409.10568 (2024). The authors are at the MIT Media Lab and Oxford. [C03]

*Editorial note:* The work dates from a 2024 preprint and was published at AAMAS 2025. Its case study simulates 8.4 million agents representing New York City.


## Long-Horizon LLM Planning & Efficiency Metrics †

*Internal Concept ID AIKC-000047 · provisional concept identity · 1 record in 2025*

<a id="aik-2025-s-p-lhplanmetric"></a>

### Long-Horizon LLM Planning & Efficiency Metrics — `AIK-2025-S-P-LHPLANMETRIC`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L1-M9 | — (not established) | 2025-11-30 |

#### L1-M9 — Long-Horizon LLM Planning & Efficiency Metrics (type S)

**Date of Appearance:** Not established. The installment frames the term as a 2025 term.  
**Public Entry ID:** `AIK-2025-S-P-LHPLANMETRIC` · **Internal Concept ID:** AIKC-000047  
**Concept:** C:LHPLANMETRIC (provisional: descriptive coinage)

*As published:* **Definition:** Metrics evaluating plan length, token cost, success rate, and planning-to-execution efficiency for tool-using agents. **Why 2025:** Emerges alongside frameworks like Plan-and-Act, standardizing agent evaluation. **References:** • Erdogan, L. E., et al. Plan-and-Act. ICML (2025).

**References (corrected record):** None that supports this entry. The cited paper (Plan-and-Act) concerns L1-M6. [C06]

*Editorial note:* "Standardizing agent evaluation" is unsourced.


## Model Context Protocol (MCP)

*Internal Concept ID AIKC-000029 · 2 records in 2025*

<a id="aik-2025-s-p-mcp"></a>

### Model Context Protocol (MCP) — `AIK-2025-S-P-MCP`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L2-E4 | 2024-11-25 (documented milestone) | 2025-12-01 |

#### L2-E4 — Model Context Protocol (MCP) (type S)

**Date of Appearance (documented milestone, not an exhaustive first use):** November 25, 2024 (Anthropic's announcement and open-sourcing of MCP) [C01] ⚑  
**Public Entry ID:** `AIK-2025-S-P-MCP` · **Internal Concept ID:** AIKC-000029  
**Concept:** C:MCP, shared with L7-K7

*As published:* • Concept: A proposed industry standard/protocol designed for the interoperability of models, allowing agents and applications to reliably exchange context, tools, and data access permissions in a structured, verifiable format. • Why 2025: Emerged as a necessary infrastructure layer to support the proliferation of multi-vendor, multi-tool agentic workflows. **Reference (table, A-059):** AI Standards Foundation. Model Context Protocol Specification, v1.0.0. **Type & Source:** Technical Standard (ASF 2025)

**Reference (corrected record):** Anthropic (2024, November 25). *Introducing the Model Context Protocol.* The specification is versioned by date, the first version being `2024-11-05`. There is no "v1.0.0", and no "AI Standards Foundation" published it. [C01]

*Editorial note:* MCP was released in November 2024. The "Why 2025" line describes its growth in 2025, not its first appearance. ⚑ MCP is Anthropic's; the preparer is an Anthropic model.

<a id="aik-2025-e-p-mcp"></a>

### Model Context Protocol (MCP) — `AIK-2025-E-P-MCP`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| E / P | L7-K7 | 2024-11-25 | 2025-12-12 |

#### L7-K7 — Model Context Protocol (MCP) (type E)

**Date of Appearance (documented milestone, not an exhaustive first use):** November 25, 2024 (Anthropic's announcement and open-sourcing of MCP), as for L2-E4 ⚑  
**Public Entry ID:** `AIK-2025-E-P-MCP` · **Internal Concept ID:** AIKC-000029  
**Concept:** C:MCP, shared with L2-E4

*As published:* **List, A-019.** • Model Context Protocol (MCP) - Universal standard for AI tool integration

*Editorial note:* The full entry is below (C02, C04, C05). ⚑

#### Corrected full entry — Model Context Protocol (MCP) (L7-K7)

*Final text by Copilot Smart (GPT-5.2) (corrected canonical text; C02, C04 and C05 applied). Source text: A-245 to A-272.* ⚑

##### Definition

A universal standard enabling AI models and tools to share context, history, instructions, and data seamlessly across platforms. MCP functions as the “USB‑C of AI,” providing a common language for interoperability.

##### Context & Motivation

MCP emerged as a solution to the fragmentation of context across AI tools, enabling continuous context sharing and integrated AI ecosystems. [C02]

*(The original opens: "By 2025, enterprises used 7–12 AI tools daily, often losing context between them. MCP emerged as a solution to this fragmentation crisis …". The figure has no source and none was found, and the sentence is removed. Its successor is reworded only to stand without it.)* [C02]

##### Technical Dimensions

- Serialization: Standardized formats for contextual information
- Secure Transmission: Encrypted communication protocols
- Synchronization: Mechanisms for maintaining consistency
- Interoperability Layer: Abstraction across diverse architectures

Formal Expression:

$$\mathrm{Context}_{\mathrm{Shared}} = \mathrm{Serialize}(\mathrm{Context}_{\mathrm{Local}}) \rightarrow \mathrm{Transmit}(\mathrm{MCP}) \rightarrow \mathrm{Deserialize}() \rightarrow \mathrm{Integrate}(\mathrm{Context}_{\mathrm{Remote}})$$ [C05]

##### Governance & Oversight

- Data Privacy: Protecting sensitive contextual information
- Security: Preventing context manipulation and poisoning attacks
- Ownership: Clarifying control rights over shared context
- Liability: Establishing accountability for cross‑platform decisions

##### Historical Notes

- 2024: Proposed by Anthropic; prototypes by industry partners
- 2025: Major platforms (OpenAI, Microsoft, Google) announced adoption plans

*(The original's "2025: Community‑driven specification development (LangChain, LlamaIndex contributions)" is removed. The specification was authored and maintained by Anthropic; LangChain's and LlamaIndex's documented role is in clients, adapters and servers, not in the specification.)* [C02]

##### Cross‑References

Tool Access & Capability Gates • AI Alignment • Governance Layer • Third‑Party Audits • Epistemic Accountability

##### References

- Ehtesham, A., Singh, A., Gupta, G. K., & Kumar, S. (2025). A Survey of Agent Interoperability Protocols: MCP, ACP, A2A, ANP. arXiv:2505.02279
- He, J., Ruan, S., & Landay, J. (2025). MCP Explorer: Interactive Learning Experience. NeurIPS 2025 Educational Showcase

- Venkiteela, P. (2025). The New Interoperability Paradigm: MCP, APIs, and the Future of Agentic AI. *Computer Fraud & Security*, 2025(1), 1259–1271. https://doi.org/10.52710/cfs.817 [C04]
- Anthropic (2024, November 25). *Introducing the Model Context Protocol.* The specification is versioned by date (`2024-11-05`, `2025-03-26`, `2025-06-18`, `2025-11-25`). [C02]

*(The original cites Venkiteela as an "IEEE/ResearchGate Preprint"; it is a journal article [C04]. The original's "AI Interoperability Consortium (2024). MCP Specification v1.0. Community Draft" is replaced: no such consortium exists, MCP is Anthropic's, and its specification has no "v1.0" [C02].)*

---


## Plan-and-Act Agent Framework

*Internal Concept ID AIKC-000044 · 1 record in 2025*

<a id="aik-2025-s-p-planact"></a>

### Plan-and-Act Agent Framework — `AIK-2025-S-P-PLANACT`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L1-M6 | 2025-03 | 2025-11-30 |

#### L1-M6 — Plan-and-Act Agent Framework (type S)

**Date of Appearance:** March 2025 (Erdogan et al., arXiv:2503.09572; ICML 2025)  
**Public Entry ID:** `AIK-2025-S-P-PLANACT` · **Internal Concept ID:** AIKC-000044  
**Concept:** C:PLANACT

*As published:* **Definition:** A modular agent architecture separating a Planner (long-horizon strategy) and an Actor/Executor (tool use & reasoning), supervised by synthetic plan data. **Why 2025:** Proved to dramatically improve long-horizon reasoning benchmarks. **References:** • Erdogan, L. E., Lee, N., Kim, S., et al. Plan-and-Act. ICML (2025).

**Why 2025 (corrected record):** Erdogan et al. (ICML 2025) report state-of-the-art success rates on web-navigation agent benchmarks: 57.58% on WebArena-Lite and 81.36% (text-only) on WebVoyager. [C05]


## Programmatic Representations (for Agents)

*Internal Concept ID AIKC-000066 · 1 record in 2025*

<a id="aik-2025-s-p-progrep"></a>

### Programmatic Representations (for Agents) — `AIK-2025-S-P-PROGREP`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L5-D6 | — (not established) | 2025-12-05 |

#### L5-D6 — Programmatic Representations (for Agents) (type S)

**Date of Appearance:** Not established.  
**Public Entry ID:** `AIK-2025-S-P-PROGREP` · **Internal Concept ID:** AIKC-000066  
**Concept:** C:PROGREP

*As published:* **Table, A-014.** **Core Concept:** Using symbolic programs, code, or rules to represent agent policies, making them interpretable, modular, and reusable. **Why It's a 2025 Trend:** The focus of a dedicated ICML 2025 workshop, signaling a move towards more interpretable and verifiable agent designs. **Source Context:** ICML 2025 Workshop


## Retrieval-Augmented Generation (RAG)

*Internal Concept ID AIKC-000051 · 2 records in 2025*

<a id="aik-2025-s-p-rag"></a>

### Retrieval-Augmented Generation (RAG) — next-gen — `AIK-2025-S-P-RAG`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L1-S4 | 2020-05 | 2025-11-30 |

#### L1-S4 — Retrieval-Augmented Generation (RAG) — next-gen (type S)

**Date of Appearance:** May 2020 for RAG (Lewis et al., arXiv:2005.11401); "next-gen" is a qualifier  
**Public Entry ID:** `AIK-2025-S-P-RAG` · **Internal Concept ID:** AIKC-000051  
**Concept:** C:RAG

*As published:* **Retrieval-Augmented Generation (RAG) — next-gen** Definition: Systems that combine an external retriever (vector store, dense/sparse IR) with a generator LLM to ground responses in external knowledge. Why 2025: Advances focused on robustness, long-context multi-hop RAG, LLM-mediated retrieval scoring, and end-to-end evaluation frameworks. (arXiv) Example: LiveRAG systems with dynamic retrieval, context filtering, and LLM-based rerankers for multi-hop reasoning.

**Source (corrected record):** Sharma, C. (2025). *Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers.* arXiv:2506.00054, https://arxiv.org/abs/2506.00054 [C10]

<a id="aik-2025-s-p-rag-02"></a>

### Retrieval-Augmented Generation (RAG) — `AIK-2025-S-P-RAG-02`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L7-K3 | 2020-05 | 2025-12-12 |

#### L7-K3 — Retrieval-Augmented Generation (RAG) (type S)

**Date of Appearance (documented milestone, not an exhaustive first use):** May 2020 (Lewis et al., arXiv:2005.11401), as for L1-S4  
**Public Entry ID:** `AIK-2025-S-P-RAG-02` · **Internal Concept ID:** AIKC-000051  
**Concept:** C:RAG, shared with L1-S4

*As published:* **List, A-014.** • Retrieval-Augmented Generation (RAG) - Hybrid architecture reducing hallucinations


## Vector Databases

*Internal Concept ID AIKC-000083 · 1 record in 2025*

<a id="aik-2025-s-p-vectordb"></a>

### Vector Databases — `AIK-2025-S-P-VECTORDB`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L4-G6 | — (not established) | 2025-12-03 |

#### L4-G6 — Vector Databases (type S)

**Public entry ID:** `AIK-2025-S-P-VECTORDB` — **Concept:** VECTORDB.
**Date of Appearance:** Not established. No factual finding from the audit; framing annotation applies; C06 arises from the review.
**Contributor:** Grok 4.1. Two published short text states.

*Text 1 (as published):* **Vector Databases**: Systems storing data as vectors for semantic searches; exploded in 2025 due to RAG and agent memory needs, with top options like Pinecone emphasizing hybrid capabilities. Enables scalable AI but challenges privacy.

*Text 2 (as published, corrections marked):* Vector databases enable semantic searches via embeddings. 2025 explosion links to RAG and agents, with benchmarks favoring hybrid systems. Example: Recommending products by conceptual similarity in e-commerce.

**Why It Matters in 2025**: Privacy and scalability are debated amid unstructured data growth.[C06 — the unattributed "Supports 62% experimenting with agents" clause is removed without replacement; original: "Supports 62% experimenting with agents; privacy and scalability are debated amid unstructured data growth." The initial capital is adjusted after the removal.]

*Annotation:* vector databases are a pre-2025 subject; 2025 marks prominence (RAG/agent-driven adoption), not origin.


## Vibe Coding

*Internal Concept ID AIKC-000079 · 1 record in 2025*

<a id="aik-2025-s-p-vibecode"></a>

### Vibe Coding — `AIK-2025-S-P-VIBECODE`

| Type / Origin | Parent | Date of Appearance | Original publication |
|---|---|---|---|
| S / P | L4-G1 | 2025-02-02 | 2025-12-03 |

#### L4-G1 — Vibe Coding (type S)

**Public entry ID:** `AIK-2025-S-P-VIBECODE` — **Concept:** VIBECODE, **established** (basis: Karpathy coinage, C01, and Collins Dictionary Word of the Year 2025).
**Date of Appearance:** February 2, 2025 *(corrected — C01; Karpathy's coinage)*
**Contributor:** Grok 4.1. Two published short text states.

*Text 1 (as published, corrections marked):* **Vibe Coding**: An intuitive, natural-language-driven software development method where users describe high-level ideas, and AI generates code, coined by Andrej Karpathy (X, February 2, 2025) and popularized in 2025 through developer communities.[C01] It lowers barriers for non-programmers but raises concerns about code quality.

*Text 2 (as published, corrections marked):* Vibe coding involves users describing software ideas in natural language, with AI generating code and structures. Coined by Andrej Karpathy (X, February 2, 2025) and gaining mainstream adoption in 2025 via communities and influencers, it democratizes development.[C01] Example: Prompting an AI for a minimalist e-commerce site yields functional code via tools like Google AI Studio.

**Why It Matters in 2025**: Amid talent shortages, it accelerates prototyping, though debates on skill erosion and reliability highlight needs for hybrid human-AI workflows.

*Editorial note:* the published states credit Karpathy only with popularization and give no coinage date; the embedded review's praise on this point is erroneous. Citation: Karpathy, X post, February 2, 2025 (https://x.com/karpathy/status/1886192184808149383; date confirmed from the post identifier; wording as quoted by secondary sources). The primary post was fetched by neither auditor nor the reviewer; the date rests on the identifier decoding and secondary quotation, and the record says so.
