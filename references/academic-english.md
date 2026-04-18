# English Academic Papers · Expert Panel Reference

## When to apply

Manuscripts targeting international journals (Nature/Science family, top field journals, IEEE transactions, ACL/CVPR-tier conferences, general SCI/SSCI), PhD thesis chapters in English, grant proposals (NSF/NIH/ERC), workshop submissions.

## Panel roster (pick 5–8)

### 1. Methodology Reviewer (Prof. M)

Focus: construct validity, internal/external validity, experimental/observational design rigor, sampling adequacy, statistical power, pre-registration status, replicability risk.

Sample probes: What is the pre-registered hypothesis? Is the sample size justified a priori? Could any of the threats to validity (Campbell & Stanley) meaningfully alter your conclusion?

### 2. Domain Expert (Dr. D)

Focus: positioning relative to prior art of the past 2–3 years, completeness of literature coverage (including in-progress arXiv preprints where relevant), whether the "novelty" claim is actually novel, community conventions of the subfield.

Sample probes: This claim was made by [X et al., 2024] — are you aware? How does your contribution differ from the closest prior work cited in §2.3?

### 3. Statistics & Experimental Analyst (Analyst S)

Focus: test selection, correction for multiple comparisons, effect size reporting, confidence intervals, the p-value vs. practical significance distinction, assumptions behind each test, robustness checks, overfitting risk in ML papers.

Sample probes: Are assumptions of the test (normality, independence, homoscedasticity) satisfied? Did you report effect sizes and CIs, not just p-values? What's the probability of this result under the null given your sample size?

### 4. Writing & Argument Reviewer (Editor W)

Focus: whether abstract faithfully represents the paper, whether the intro's "gap → contribution → approach" triangle is crisp, signposting, topic sentences, whether figures carry their own weight, consistency of notation and terminology.

Sample probes: The abstract promises X; where exactly in §4–5 is X demonstrated? Does every figure have a takeaway a reader can state in one sentence?

### 5. Reproducibility & Open Science Auditor (Auditor R)

Focus: code/data availability, computational environment, random seeds, hyperparameters, evaluation protocol, leakage between train/test, whether claimed results can be reproduced by a reader with access only to the paper + supplement.

Sample probes: Where is the code? Are hyperparameters reported? Could a reader reproduce Table 3 from what's provided? Is there any train/test leakage in the pipeline?

### 6. Peer Reviewer Simulation (Blind-Reviewer B)

Focus: simulates a top-journal or top-conference reviewer operating under time pressure. Applies the actual acceptance criteria of the target venue (novelty + rigor + significance + clarity). Delivers the kind of blunt, specific feedback one gets from R2.

Sample probes: I am reviewer 2. In the first 10 minutes of reading I cannot tell what is new. Strengthen the "what is new" statement in the intro or I vote reject.

### 7. Ethics & Integrity Reviewer (Auditor E)

Focus: IRB / ethics approval statement, consent, data privacy, conflict of interest disclosure, authorship conventions, citation hygiene (no phantom citations, no excessive self-cite), AI-use disclosure per current venue policy.

Sample probes: Was IRB approval obtained and disclosed? Are conflicts of interest listed? Is the AI-use statement consistent with the venue's current policy?

### 8. Thesis Supervisor / Committee Member (Advisor A)

Focus: coherence of the overall thesis narrative, whether the chapters hang together as a unified contribution, the quality of the research question → methods → findings → discussion chain, how the work will fare in a defense setting (not just on paper), and whether the candidate's independent intellectual contribution is visible.

Sample probes: Can you state your thesis's central argument in one sentence? When the committee asks "how does your work differ fundamentally from [closest prior work]," what's your answer? Does Chapter 4's evidence actually support Chapter 5's claims, or is there a gap? Which parts of this work could you confidently defend at a viva, and which parts are you hoping won't come up?

### 9. PhD External Examiner (External E)

Focus: simulates a senior external examiner at a PhD viva / thesis defense. Applies the bar of "originality + sufficient scope for a doctorate + candidate can defend against expert scrutiny." Especially attentive to whether the contribution is genuinely novel at the PhD level (not just "another paper's worth of work") and whether the thesis would hold up to hostile questioning.

Sample probes: Is this work sufficient for a PhD at a top university, or is it three papers stapled together? If I challenge the core claim with [plausible counterargument], can the candidate respond? Is there a genuinely original theoretical / methodological / empirical contribution, or is this competent-but-derivative work?

### 10. Devil's Advocate

Focus: challenge every consensus point. Especially targets "everyone agrees the method is sound" or "the writing is clear" — pressure tests these until they either hold or break. See `references/anti-groupthink.md` for the DA hard rules (must cite original text / must give a concrete testable counterexample).

## Common fatal flaws (P0 candidates)

- **Novelty inflation**: the "contribution" is a well-known technique applied to a marginally different dataset.
- **Baseline cherry-picking**: only weak/outdated baselines are compared against.
- **Leakage**: test set information bleeds into training or model selection.
- **Overclaim in abstract**: abstract asserts generalizability or causality far beyond what the data supports.
- **Statistical hygiene failures**: uncorrected multiple comparisons, missing effect sizes, no CIs.
- **Unreproducible results**: code not available, critical hyperparameters unreported, random seeds unfixed.
- **Figure-text mismatch**: a figure visually implies trend X but the text claims trend Y.
- **Unacknowledged prior work**: a paper published in the last 18 months in the same venue did essentially the same thing.

## Calibration by venue

- **Nature/Science/top CS conferences (NeurIPS/ICML/ACL)**: any P0 → reject; ≥2 P1 → major revision at best.
- **Top field journals / A* conferences**: any P0 → major revision; P1s must be addressed.
- **General SCI/SSCI**: P0 must be fixed; P1 should be addressed in revision.
- **Workshop / minor venues**: P0 still required to fix; P1 flexible.
- **Grant proposals**: emphasis shifts to "novelty + impact + feasibility"; methodological P0 flaws are fatal.

## Calibration by thesis level (if the work is a dissertation chapter or full thesis)

- **PhD thesis (top-tier university)**: novelty bar is high — must be genuinely original; methodological rigor non-negotiable; external examiner will look for "could this candidate defend this against a hostile expert?" P0s = fatal; ≥3 P1s suggest the thesis is not yet defensible.
- **PhD thesis (general)**: coherence across chapters and sufficiency of contribution matter more than originality-at-top-conference level. P0s still fatal; P1s need committee-level discussion.
- **Master's thesis**: bar is "competent application of methods to a well-scoped question." Novelty is welcome but not required. P0s (e.g., methodological incoherence) fatal; P1s negotiable depending on committee culture.
- **Proposal / qualifying paper**: emphasis on research question + feasibility + preliminary results rather than full empirical completion.
