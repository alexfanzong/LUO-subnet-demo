# LUO Architecture Overview

LUO is designed as legal uncertainty infrastructure: a system for retrieving legal evidence, preserving jurisdictional disagreement, and validating whether a miner's answer is grounded in real citations.

This document is intentionally public-safe. It explains the architecture without publishing the full private corpus, synthetic trap set, or validator implementation details.

## Core Loop

```text
User question
  -> miner retrieves jurisdiction-aware evidence
  -> miner produces a cited legal uncertainty map
  -> validator audits citations, trap exposure, and reasoning coherence
  -> consensus rewards faithful uncertainty mapping
```

## Components

### 1. Evidence Corpus

The MVP uses a curated Tornado Cash legal corpus covering four target jurisdictions:

- United States
- Netherlands
- Switzerland
- Hong Kong

The corpus is built to distinguish:

- explicit enforcement positions,
- judicial reversals,
- criminal prosecution theories,
- regulatory silence,
- framework-only materials,
- cross-jurisdiction comparison.

The public demo can describe this corpus at a high level. The full corpus and trap list remain private unless separately reviewed for release.

### 2. Miner Retrieval

Miners are expected to retrieve relevant legal evidence before answering. The MVP uses local retrieval for reliability:

- local embeddings,
- vector search,
- source IDs,
- jurisdiction labels,
- legal-position labels.

The important rule is simple: a miner must show its evidence before it claims certainty.

### 3. Synthetic Traps

The MVP includes synthetic trap citations. These are deliberately plausible-looking but fabricated authorities. They test whether a miner can preserve uncertainty instead of manufacturing a confident answer from fake sources.

Synthetic traps are a mechanism-design tool. They make fabricated certainty economically visible.

### 4. Validator Audit

Validators evaluate miner outputs across three broad dimensions:

- whether cited source IDs exist,
- whether the miner cites synthetic traps,
- whether the reasoning preserves the actual structure of legal divergence.

The MVP keeps validator scoring reproducible for demo purposes. Later versions can add LLM-as-Judge review and multi-validator consensus.

### 5. Public Demo Surface

The public demo is a static HTML experience that explains the mechanism:

- Opening: why fabricated certainty is dangerous.
- Search: how miner retrieval exposes citations.
- Audit: how validator scoring separates faithful answers from fabricated ones.
- Atlas: how one protocol can have four legal treatments.
- Close: why the subnet rewards uncertainty mapping instead of single-answer generation.

## Public / Private Boundary

Public-safe:

- static demo UI,
- high-level architecture,
- product positioning,
- roadmap,
- dependency list.

Private by default:

- full corpus,
- synthetic trap list,
- validator implementation,
- generated miner A/B/C outputs,
- prompt drafts and local notes,
- screenshots that may include private desktop context.

## Roadmap

### Phase 1 - Evidence and Trap MVP

Completed: static demo, curated corpus, local retrieval, preset miner outputs, validator scoring, optional LLM backend.

### Phase 2 - Staked Challenge Layer

Participants can stake to challenge validator scores. This turns review into an appeal-like mechanism and rewards validators who anticipate durable consensus.

### Phase 3 - RWA Vertical Market

Extend LUO from Tornado Cash to tokenized real-world assets, stablecoins, custody, sanctions, securities, commodities, tax, and cross-border distribution.

### Phase 4 - Production Subnet Candidate

Define miner/validator task specs, publish benchmark subsets, add multi-validator aggregation, and harden the citation audit pipeline.
