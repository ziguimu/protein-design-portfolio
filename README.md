# Protein Design Portfolio

A portfolio of computational protein-design projects, structural evaluations, reproduction attempts, and evidence audits. All results are computational unless an experiment is explicitly described. Model confidence and interface scores do not demonstrate binding affinity or biological activity.

[中文说明](#中文说明)

## Research map

| Project | Research question and materials | Current status |
|---|---|---|
| [AI-BinderDesign](https://github.com/ziguimu/AI-BinderDesign) | EGFR binder design and EGFR/TNF control-based structural evaluation; includes the original 28-slide report | EGFR and TNF source archives published; 1,588 files restored and SHA-256 checked |
| [GLP1R-reproduction](https://github.com/ziguimu/GLP1R-reproduction) | GLP-1R paper reproduction across sequence design, ColabFold, Boltz-2, PCANN and recovery stages | Seven source archives published; 4,055 unique archive paths restored and checked; reproduction deviations are recorded |
| [TfR1-binder-design](https://github.com/ziguimu/TfR1-binder-design) | Three rounds of TfR1 candidate design, source results, failure analysis and corrected claims | Source archive published; 4,338 files restored and checked; five computational candidates remain unvalidated |
| [KRAS-G12D-pMHC-design](https://github.com/ziguimu/KRAS-G12D-pMHC-design) | Mutant/WT/apo control-based KRAS G12D pMHC binder design and screening | Four Releases cover the original archive and three follow-on rounds; the latest screened 64 Asp6 designs, with 0/2 initial-gate passers qualifying after three-seed confirmation. prior documented cumulative count remains 896 for its stated scope; the 64-sequence comparison covers 367 historical records only, so a global total is not recomputed; computational only |
| [ai-protein-design](https://github.com/ziguimu/ai-protein-design) | Reusable design workflow, templates, audit utilities and bounded case evidence | Source, templates, a bounded validation report, and selected de-identified cases published; additional records remain under privacy and rights review |

## Shared workflow and evidence standards

Projects preserve their actual stages and source organization. Shared practice includes recording target and construct identity, input provenance, software/environment details where available, historical commands, screening criteria, positive and negative controls, source hashes, and the difference between predicted structure and experimental evidence. Missing history is labeled rather than reconstructed from assumptions. See [methods and provenance](METHODS.md), [third-party sources and license status](THIRD_PARTY_SOURCES.md), and [project status](PROJECTS_STATUS.md).

Third-party tools and weights (including RFdiffusion, ProteinMPNN, GPD, PCANN, ESM and structure-prediction packages) remain attributed to their owners and retain their own licenses. Project-specific modifications and outputs are kept distinct from upstream source. See each repository's `LICENSE-DATA.md` and provenance records.

## Contribution and authorship

The project records document user-directed research questions, choices, interpretation and review, alongside computational work performed with AI assistance. This portfolio makes no claim of experimental validation or authorship beyond the records included in each project. Contributions and missing provenance are described at project level where the source supports them.

## Restore and verify

Large source trees are distributed as versioned GitHub Release assets rather than ordinary Git history. Each archive includes a file-level manifest with project-relative source path, archive path, byte count and SHA-256. Absolute workstation paths are omitted. For transformed text files, the manifest records source and published hashes separately and reports the redaction count; source copies of transformed text remain local. Restoration reports record checked file counts. Current validated releases:

- [AI-BinderDesign archive](https://github.com/ziguimu/AI-BinderDesign/releases/tag/archive-2026-10-31)
- [GLP1R reproduction archives](https://github.com/ziguimu/GLP1R-reproduction/releases/tag/archive-2026-10-31)
- [TfR1 source archive](https://github.com/ziguimu/TfR1-binder-design/releases/tag/archive-2026-10-31)
- [KRAS original archive](https://github.com/ziguimu/KRAS-G12D-pMHC-design/releases/tag/archive-2026-10-31)
- [KRAS follow-on screen archive](https://github.com/ziguimu/KRAS-G12D-pMHC-design/releases/tag/archive-2026-10-31-batch2)
- [KRAS Asp6 follow-on archive](https://github.com/ziguimu/KRAS-G12D-pMHC-design/releases/tag/archive-2026-10-31-batch3)
- [KRAS Asp6 candidate 01 screen and confirmation archive](https://github.com/ziguimu/KRAS-G12D-pMHC-design/releases/tag/archive-2026-11-01-batch4)
- [Final archive and cleanup audit](ARCHIVE_AUDIT_2026-11-01.md)

The original KRAS archive restored 25,266 files; the first follow-on package restored 516 manifest-listed files (467 byte-identical source files and 49 privacy-transformed text files); the Asp6 package restored 1,119 files (1,079 byte-identical and 40 privacy-transformed). The complete ChatGPT account export remains local and is not included.

## Licenses

Original code is MIT licensed where rights are established. Original documentation and data are CC BY 4.0 where rights are established. Third-party code, weights, papers and datasets retain their original terms. See [LICENSE-DATA.md](LICENSE-DATA.md).

## 中文说明

本项目组合整理计算蛋白质设计、结构评价、论文复现尝试和证据审计。除非明确记录实验，所有结果均为计算结果。模型置信度和界面评分不能证明结合亲和力或生物活性。

### 研究项目与进度

| 项目 | 研究内容 | 当前状态 |
|---|---|---|
| [AI-BinderDesign](https://github.com/ziguimu/AI-BinderDesign) | EGFR 结合剂设计、EGFR/TNF 对照结构评价及原始 28 页报告 | EGFR 与 TNF 归档已发布；1,588 个文件下载恢复并通过 SHA-256 校验 |
| [GLP1R-reproduction](https://github.com/ziguimu/GLP1R-reproduction) | GLP-1R 论文复现中的序列设计、ColabFold、Boltz-2、PCANN 与恢复阶段 | 七个归档已发布；4,055 个唯一归档路径校验通过；复现偏差有记录 |
| [TfR1-binder-design](https://github.com/ziguimu/TfR1-binder-design) | 三轮候选设计、原始结果、失败分析和结论更正 | 归档已发布；4,338 个文件校验通过；五个计算候选尚未实验验证 |
| [KRAS-G12D-pMHC-design](https://github.com/ziguimu/KRAS-G12D-pMHC-design) | Mutant/WT/apo control-based KRAS G12D pMHC binder design and screening | Four Releases cover the original archive and three follow-on rounds; the latest screened 64 Asp6 designs, with 0/2 initial-gate passers qualifying after three-seed confirmation. prior documented cumulative count remains 896 for its stated scope; the 64-sequence comparison covers 367 historical records only, so a global total is not recomputed; computational only |
| [ai-protein-design](https://github.com/ziguimu/ai-protein-design) | 可复用工作流、模板、审计工具和有边界的案例证据 | 技能源码、模板、有限范围的验证报告和精选脱敏案例已发布；其他记录仍在进行隐私和权利审查 |

### 共用流程与证据边界

项目保留各自真实阶段与来源结构。共用方法包括记录靶标及构建体、输入来源、软件环境、历史命令、筛选标准、正负对照、文件哈希，并区分预测结构与实验依据。历史信息缺失时会明确标注，不凭推测补写。详见[方法与来源](METHODS.md)、[第三方来源与许可状态](THIRD_PARTY_SOURCES.md)及[项目状态](PROJECTS_STATUS.md)。

RFdiffusion、ProteinMPNN、GPD、PCANN、ESM 和结构预测软件等第三方工具与权重仍归原权利人，并沿用各自许可。项目修改与运行结果同上游源码分开记录。

### 贡献与作者身份

项目记录反映用户提出和指导研究问题、作出选择并审阅解释；部分计算工作由 AI 辅助完成。本组合不超出各项目已有记录宣称实验验证或作者身份。各项目仅在来源证据支持时描述贡献；来源缺失会单独说明。

### 恢复与校验

大型原始目录作为带版本的 GitHub Release 附件发布。每个归档含项目相对来源路径、归档路径、字节数和 SHA-256 的逐文件清单，不公开本机绝对路径。脱敏改写的文本文件分别记录源件与发布件哈希及替换次数；相应源文本留在本地。恢复报告记录核验数量。目前已完成恢复核验的项目归档为：AI-BinderDesign、GLP1R-reproduction、TfR1-binder-design 和 KRAS-G12D-pMHC-design。KRAS 原始归档恢复 25,266 个文件；后续筛选包恢复 516 个清单文件（467 个字节与来源相同，49 个为隐私转换文本）。完整 ChatGPT 账户导出按用户要求留在本地，不在此公开。

原创代码在权利明确时采用 MIT；原创文档和数据在权利明确时采用 CC BY 4.0。第三方材料保留原许可，详见 [LICENSE-DATA.md](LICENSE-DATA.md)。


## Integrity and cleanup tools

- `tools/verify_release_restore.py` checks ZIP CRCs, manifest membership, traversal/symlink safety, file sizes and SHA-256; it can restore into a new empty directory. It reports whether each published file is byte-identical to its source hash or is a privacy-transformed copy.
- `tools/guarded_cleanup.py` is dry-run by default. It accepts only explicit per-file path/hash entries, constrains them to a chosen root, and skips unauthorized, changed, missing, symlinked, outside-root, and active paths/PIDs. Use `--apply` only after a release restore has passed.

These tools check archive integrity and cleanup preconditions; they do not validate scientific results.

## Conversation provenance

The project READMEs link to the available redacted scientific conversation records and their coverage notes. The full ChatGPT account export remains local; records with unresolved attachment or source coverage say so explicitly.

### 对话来源

各项目 README 链接到可访问的脱敏科研对话及其覆盖说明。完整 ChatGPT 账户导出仍保留在本地；附件或来源覆盖未确认的记录会明确说明。

