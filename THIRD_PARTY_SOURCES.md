# Third-party software, model and data provenance

Checked on 2026-10-31. This register records tools found in the scoped workspaces. A code license does not automatically establish redistribution rights for checkpoints, training data, structures, or generated artifacts; each is considered separately. The per-file local inventory retains exact paths and hashes without publishing the full local filesystem listing.

| Component | Recorded use in these projects | Upstream/source | License and handling |
|---|---|---|---|
| RFdiffusion | Backbone generation and smoke examples | [RosettaCommons/RFdiffusion](https://github.com/RosettaCommons/RFdiffusion) | Upstream states BSD license. Attribute source; user-specific runs and modifications remain separate. We did not copy upstream source into these repositories. |
| ProteinMPNN | Inverse folding and sequence generation | [dauparas/ProteinMPNN](https://github.com/dauparas/ProteinMPNN) | Upstream LICENSE is MIT. Attribute source; project outputs remain distinct. |
| ColabFold | Structure prediction and historical GLP1R/EGFR workflows | [sokrypton/ColabFold](https://github.com/sokrypton/ColabFold) | Source repository is MIT; AlphaFold/ColabFold model parameters and remote-service datasets retain their own terms. No weights are redistributed by this registry. |
| Boltz / Boltz-2 | Structural prediction and analysis | [jwohlwend/boltz](https://github.com/jwohlwend/boltz) | Upstream says code and weights are MIT. Project input/reference files still retain their own provenance. |
| BoltzGen | KRAS G12D design and inverse-folding run (local environment recorded as 0.3.2) | [HannesStark/boltzgen](https://github.com/HannesStark/boltzgen) | Upstream code is MIT. Local checkpoint/cache items are held locally and excluded from release pending asset-level provenance and license review. |
| ESM | PCANN dependency/model cache | [facebookresearch/esm](https://github.com/facebookresearch/esm) | Source code LICENSE is MIT. The local 2.60 GB ESM-2 checkpoint is retained locally; checkpoint/data terms were not independently established for this exact downloaded artifact, so it is not redistributed. |
| GPD | Local sequence-design source clone | [decodermu/GPD](https://github.com/decodermu/GPD) | GitHub repository metadata reports no license and the repository tree has no top-level LICENSE. The local clone has modified requirements and example FASTA plus untracked artifacts. Do not redistribute this source or its user modifications until rights are established. |
| PCANN | Local predictor source and pretrained outputs | [bionmr-spbu-projects/PCANN](https://github.com/bionmr-spbu-projects/PCANN) and the source URL embedded in its `setup.py`, [OOLebedenko/PCANN](https://github.com/OOLebedenko/PCANN) | Both candidate repositories report no license through GitHub metadata and have no top-level LICENSE. The local source tree and weights remain local; the ESM subdirectory's MIT code license does not license the PCANN package or its weights. |

## Policy

- Record the exact upstream URL and version/commit when present in local logs; if no pin survives, mark it unknown.
- Keep third-party checkpoints, downloaded reference data, and caches out of these public repositories unless their specific redistribution terms are confirmed.
- Do not silently remove local modifications to an upstream clone. Keep the clone local and document the dirty files.
- Public project results identify the tool/model version and do not imply endorsement by the tool authors.

## 中文说明

本表记录截至 2026-10-31 在纳入范围内发现的第三方软件、模型和数据来源。代码许可并不自动覆盖权重、训练数据、结构文件或生成结果；这些材料分别审查。逐文件本地清单保留精确路径和哈希，没有公开完整本机文件目录。

| 工具 | 项目中的记录用途 | 上游来源 | 许可与处理 |
|---|---|---|---|
| RFdiffusion | 骨架生成和 smoke 示例 | [RosettaCommons/RFdiffusion](https://github.com/RosettaCommons/RFdiffusion) | 上游声明 BSD 许可。保留来源归属；用户运行结果和修改分开存放，本次没有复制上游源码。 |
| ProteinMPNN | 逆折叠和序列生成 | [dauparas/ProteinMPNN](https://github.com/dauparas/ProteinMPNN) | 上游 LICENSE 为 MIT。保留归属；项目运行结果独立记录。 |
| ColabFold | 结构预测及 GLP1R/EGFR 历史流程 | [sokrypton/ColabFold](https://github.com/sokrypton/ColabFold) | 源码仓库为 MIT；AlphaFold/ColabFold 权重及远程服务数据另有各自条款。本表不分发权重。 |
| Boltz / Boltz-2 | 结构预测和分析 | [jwohlwohlwend/boltz](https://github.com/jwohlwend/boltz) | 上游声明代码和权重为 MIT。项目输入与引用文件仍按其来源另行处理。 |
| BoltzGen | KRAS G12D 设计与逆折叠运行；本地环境记录版本 0.3.2 | [HannesStark/boltzgen](https://github.com/HannesStark/boltzgen) | 上游源码为 MIT。本地检查点/缓存继续留存；待逐项确认文件来源与许可前不上传。 |
| ESM | PCANN 依赖和本地模型缓存 | [facebookresearch/esm](https://github.com/facebookresearch/esm) | 上游源码 LICENSE 为 MIT。本地 2.60 GB ESM-2 权重留在本地；尚未对该下载文件本身的条款完成独立确认，因此不再分发。 |
| GPD | 本地序列设计源码克隆 | [decodermu/GPD](https://github.com/decodermu/GPD) | GitHub 元数据未声明许可，仓库顶层也无 LICENSE。本地克隆修改了 requirements 和示例 FASTA，并包含未跟踪产物。权利确认前不分发源码或个人修改。 |
| PCANN | 本地预测源码和预训练结果 | [bionmr-spbu-projects/PCANN](https://github.com/bionmr-spbu-projects/PCANN) 及其 `setup.py` 指向的 [OOLebedenko/PCANN](https://github.com/OOLebedenko/PCANN) | 两个候选仓库的 GitHub 元数据都未声明许可，顶层没有 LICENSE。本地源码和权重留存；ESM 子目录中源码的 MIT 许可不覆盖 PCANN 包或其权重。 |

第三方检查点、下载参考数据和缓存默认不进入公开仓库，除非其特定再分发条款已确认。上游克隆中的本地改动不会被覆盖或静默删除；未记录版本时明确标为未知。
