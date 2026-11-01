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
| KRAS follow-on screen (batch2) | 516 | PASS; 467 byte-identical, 49 privacy-transformed |
| KRAS Asp6 follow-on (batch3) | 1,119 | PASS; 1,079 byte-identical, 40 privacy-transformed |

The KRAS follow-on ZIP was downloaded from [Release archive-2026-10-31-batch2](https://github.com/ziguimu/KRAS-G12D-pMHC-design/releases/tag/archive-2026-10-31-batch2). SHA-256: `df0ca6f1dd4da25243a0b4421140f18a8817c30f0cfd3f6c9076d47c571ed7b8`; ZIP CRC, file counts, sizes, and published hashes passed. Manifest-list contains 516 source records; the ZIP also contains its MANIFEST.json.

The five archive counts sum to 36,882 validated source file paths. GLP1R's 4,055 count is unique paths across its multiple archives, not the sum of per-asset memberships.

## KRAS result status

The automatically triggered follow-on screen completed before archival. It screened 32 additional unique designs; one passed the mutant-only gate and entered confirmation at seeds 15, 16, and 17. All confirmation gates failed the mutant-minus-WT binder and peptide interface thresholds. No candidate qualified. The cumulative project checkpoint is 896 unique computational designs screened and zero qualified. No experimental binding evidence is reported. These are archived historical outputs, not a newly rerun scientific validation.

The later automatic Asp6 run generated 32 candidates and its designated mutant seed-15 screen completed 32/32 with zero prediction or audit failures. The frozen mutant gate passed 0/32, so no confirmation panel was started. Sequence-hash reconciliation found all 32 sequences in the historical record: this batch added 0 unique sequences and the cumulative count remains 896. The 589 partial files from a separately interrupted duplicate invocation are archived but excluded from metrics. [The Asp6 Release](https://github.com/ziguimu/KRAS-G12D-pMHC-design/releases/tag/archive-2026-10-31-batch3) restored 1,119/1,119 files, with 1,079 source-byte-identical and 40 privacy-transformed files; SHA-256, size, CRC, path safety, and member checks passed. The design stage exit code was not captured.

## KRAS Asp6 最新结果（中文补充）

随后自动运行的 Asp6 批次生成 32 条候选；既定 mutant seed-15 筛选完成 32/32，预测失败和审计错误均为 0。冻结 mutant 门槛通过 0/32，因此没有启动确认面板。序列哈希核对发现 32 条均为历史重复，本批新增独特序列为 0，累计仍为 896。另一次误启动后中断的重复调用产生 589 个部分文件，虽已归档但不纳入指标。[Asp6 Release](https://github.com/ziguimu/KRAS-G12D-pMHC-design/releases/tag/archive-2026-10-31-batch3) 恢复核对 1,119/1,119 个文件通过，其中 1,079 个源字节相同、40 个为隐私转换文本；SHA-256、大小、CRC、路径安全和成员清单均通过。设计阶段进程退出码未捕获。

## Cleanup and local exceptions

The non-KRAS exact-file cleanup removed 10,258 files after source-hash checks and Release restore verification; measured free space increased by 5,293,375,488 bytes (about 4.93 GiB). Prior cleanup batches have separate logs and are not included in that measured delta. The KRAS source research tree remains locally available. The complete ChatGPT account ZIP and privacy-transformed source text remain local. The final KRAS temporary-copy cleanup is recorded separately in the local deletion log.

## Conversation coverage and limitations

Published conversation records are de-identified and are only as complete as their available source/export coverage; project archives state attachment or transcript limitations. The full ChatGPT account ZIP is not public. Archive integrity checks do not establish scientific validity, and structure/model scores do not establish binding affinity.

## KRAS batch4 restore validation 鈥?2026-11-01

Release [archive-2026-11-01-batch4](https://github.com/ziguimu/KRAS-G12D-pMHC-design/releases/tag/archive-2026-11-01-batch4) was downloaded afresh and verified with `tools/verify_release_restore.py`. Result: PASS, 1,004/1,004 source records; 920 byte-identical and 84 privacy-transformed. Missing members, size mismatches, published SHA-256 mismatches, unsafe paths, unexpected members, and ZIP CRC errors: 0. ZIP SHA-256: `3a0b54786a2614de8c5fb4d59cbd540a47f2124e6e171cdd0c48323b6e8fa506`.

The seven archive coverage groups together contain 37,886 source-path records across validated packages. This is a package-membership total, not a deduplicated filesystem-file count. The latest KRAS screen comprised 64 sequences unique relative to the 367 historical sequence records scanned; 2 passed the initial mutant gate, but both failed all three-seed confirmations (6/6 comparisons failed). No candidate qualified. Seed 16 process exit status is unknown despite complete logs and parsed outputs. See the [KRAS run record](https://github.com/ziguimu/KRAS-G12D-pMHC-design/blob/main/docs/RUN_STATUS_20261101_Asp6_cand01.md).
