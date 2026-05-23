# LUO - Legal Uncertainty Oracle

> On Bittensor, LUO lets permissionless miners produce cross-jurisdictional legal risk topology maps through evidence-constrained claim verification.

**LUO (Legal Uncertainty Oracle)** is legal uncertainty infrastructure for mapping, retrieving, and validating cross-jurisdiction legal divergence.

LUO does not try to force one legal answer. It preserves disagreement, anchors claims to evidence, and exposes fabricated certainty.

## Project Positioning

Modern legal and compliance work is increasingly cross-border, but legal answers are still usually delivered one jurisdiction at a time. LUO treats the structure of legal disagreement itself as the product.

The long-term goal is to build infrastructure where:

- miners retrieve jurisdiction-aware legal evidence,
- validators audit citations and claim-evidence closure,
- synthetic traps expose fabricated authority,
- economic incentives reward faithful uncertainty mapping,
- users receive a topology of legal divergence rather than a false universal answer.

In short: **Legal Uncertainty Infrastructure**, not a legal chatbot.

## Current Status - MVP v1.0

MVP v1.0 demonstrates the core mechanism end-to-end:

- Static pitch/demo UI for explaining the subnet mechanism.
- Tornado Cash legal-divergence case study.
- 46 real source entries + 5 synthetic traps in the private evaluation corpus.
- 4 target jurisdictions: United States, Netherlands, Switzerland, and Hong Kong, plus a cross-jurisdiction comparison layer.
- Three miner quality tiers used to demonstrate citation auditing and fabricated-reference detection.
- Public-safe architecture overview for the miner / validator / challenge flow.

The public demo surface is designed to work without paid APIs, without live model availability, and without exposing the private benchmark corpus.

## Demo Thesis

The most dangerous legal failure in an AI workflow is not uncertainty. It is certainty backed by citations that do not exist.

The current MVP uses Tornado Cash as the test case:

- **United States:** internal split between OFAC sanctions, Fifth Circuit reversal, and DOJ prosecution.
- **Netherlands:** criminal conviction path against Alexey Pertsev.
- **Switzerland:** framework-only evidence; no Tornado Cash-specific FINMA position.
- **Hong Kong:** soft-follow risk signaling; no independent Tornado Cash-specific mandate.

## Repository Structure

This public demo repository contains only the public-facing demo surface and architecture overview.

```text
.
├── index.html                  # Optional GitHub Pages entrypoint
├── pitch_demo_terminal/
│   ├── index.html              # Static pitch/demo UI
│   └── preview.py              # Streamlit wrapper for local preview
├── docs/
│   ├── ARCHITECTURE.md         # Architecture overview
│   └── IDEATHON_SUBMISSION.md  # Submission proposal draft
├── submission_assets/
│   ├── figure1_evidence_bound_risk_map.png
│   └── screenshots/            # Demo screenshots for proposal / README use
├── requirements.txt            # Python preview dependencies
└── README.md                   # Public project overview
```

## Submission Links

- **Full proposal:** [docs/IDEATHON_SUBMISSION.md](docs/IDEATHON_SUBMISSION.md)
- **Pitch demo:** [Live GitHub Pages demo](https://alexfanzong.github.io/LUO-subnet-demo/) / [source HTML](pitch_demo_terminal/index.html)

## Static Demo UI

The static UI lives at:

```text
pitch_demo_terminal/index.html
```

For local browser preview, open the HTML file directly.

For Streamlit preview:

```bash
streamlit run pitch_demo_terminal/preview.py
```

## Architecture

The MVP is organized around four roles:

- **User:** asks a cross-jurisdiction legal question.
- **Miner:** retrieves evidence and produces jurisdiction-aware claims.
- **Validator:** checks citation existence, fabricated-reference traps, and claim-evidence closure.
- **Challenge layer:** future staking mechanism for appealing or disputing validator scores.

The design goal is not to replace lawyers or sovereign legal interpretation. LUO maps where legal authority diverges, where evidence is silent, and where a model has forged certainty out of that silence.

## Roadmap

### Phase 1 - Evidence and Trap MVP: Complete

- Tornado Cash cross-jurisdiction case study.
- Synthetic trap set for fabricated citation detection.
- Miner output tiers and validator scoring concept.
- Static demo UI and presentation flow.

### Phase 2 - Staked Challenge Layer

- Let participants challenge validator scores by staking.
- Treat challenges as an appeal mechanism for legal reasoning.
- Track whether challenged scores converge or diverge under review.
- Reward validators that anticipate durable consensus, not just immediate majority opinion.

### Phase 3 - RWA Vertical Market

- Extend from Tornado Cash to tokenized real-world assets.
- Map divergence across securities, commodities, banking, sanctions, tax, custody, and cross-border distribution rules.
- Package jurisdictional divergence maps as an intelligence product for lawyers, compliance teams, issuers, custodians, and investors.

### Phase 4 - Production Subnet Candidate

- Miner/validator task specification.
- Public benchmark methodology.
- Multi-validator scoring aggregation.
- Production-grade citation audit pipeline.
- RWA-focused legal divergence datasets.

## Origins

LUO's first public prototype was prepared for the **Bittensor AI Subnet Ideathon in Shanghai on 2026-05-23**. The event is the launch context, not the project boundary.

## Contact

Alex Fan  
Cornell Law School  
Programmable Compliance Architect  
X: `@itsAlexFan`
