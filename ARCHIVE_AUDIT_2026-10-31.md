# Archive audit — 2026-10-31

## Scope and method

This report summarizes the six-repository portfolio archival. Project sources and results were organized into Git content and versioned GitHub Release assets. Raw-release validation downloaded assets from GitHub into fresh directories, checked archive CRC, manifest membership, safe paths, expected sizes, and published SHA-256 values. Privacy-transformed text is identified separately from byte-identical source content. Archiving does not repeat or independently validate scientific calculations.

## Repositories

- Portfolio: https://github.com/ziguimu/protein-design-portfolio
- EGFR/TNF: https://github.com/ziguimu/AI-BinderDesign
- GLP1R reproduction: https://github.com/ziguimu/GLP1R-reproduction
- TfR1: https://github.com/ziguimu/TfR1-binder-design
- KRAS: https://github.com/ziguimu/KRAS-G12D-pMHC-design
- Skill: https://github.com/ziguimu/ai-protein-design

## Remote restore results

| Project archive | Restored file paths | Result |
|---|---:|---|
| AI-BinderDesign | 1,588 | PASS |
| GLP1R-reproduction | 4,055 unique paths | PASS |
| TfR1-binder-design | 4,338 | PASS |
| KRAS original archive | 25,266 | PASS |
| KRAS follow-on screen | 516 | PASS; 467 byte-identical, 49 privacy-transformed |

The KRAS follow-on ZIP was downloaded from [Release archive-2026-10-31-batch2](https://github.com/ziguimu/KRAS-G12D-pMHC-design/releases/tag/archive-2026-10-31-batch2). SHA-256: `df0ca6f1dd4da25243a0b4421140f18a8817c30f0cfd3f6c9076d47c571ed7b8`; ZIP CRC, file counts, sizes, and published hashes passed. Manifest-list contains 516 source records; the ZIP also contains its MANIFEST.json.

The five archive counts sum to 35,763 validated source file paths. GLP1R's 4,055 count is unique paths across its multiple archives, not the sum of per-asset memberships.

## KRAS result status

The automatically triggered follow-on screen completed before archival. It screened 32 additional unique designs; one passed the mutant-only gate and entered confirmation at seeds 15, 16, and 17. All confirmation gates failed the mutant-minus-WT binder and peptide interface thresholds. No candidate qualified. The cumulative project checkpoint is 896 unique computational designs screened and zero qualified. No experimental binding evidence is reported. These are archived historical outputs, not a newly rerun scientific validation.

## Cleanup and local exceptions

The non-KRAS exact-file cleanup removed 10,258 files after source-hash checks and Release restore verification; measured free space increased by 5,293,375,488 bytes (about 4.93 GiB). Prior cleanup batches have separate logs and are not included in that measured delta. The KRAS source research tree remains locally available. The complete ChatGPT account ZIP and privacy-transformed source text remain local. The final KRAS temporary-copy cleanup is recorded separately in the local deletion log.

## Conversation coverage and limitations

Published conversation records are de-identified and are only as complete as their available source/export coverage; project archives state attachment or transcript limitations. The full ChatGPT account ZIP is not public. Archive integrity checks do not establish scientific validity, and structure/model scores do not establish binding affinity.
