# Shared methods and provenance

This portfolio groups work by project, target and computational stage. It does not merge distinct inputs, candidate numbering schemes or control outcomes just because they share a method name.

## Minimum record for a computational stage

- Target, construct, chain and sequence provenance, with source identifiers where retained.
- Input files and their SHA-256 values, plus any transformations that are documented.
- Tool and model version, environment, device, command and configuration when present in the source record.
- Dataset partition, controls and screening thresholds; identify whether they were fixed before or after inspecting outputs.
- Output inventory and status, including failed runs, incomplete downloads, recovery attempts and corrections.
- Interpretation bounded to the evidence. Predicted confidence is not measured affinity, activity or experimental validation.

## Archive format

Git tracks source code, explanatory documents, small summary tables and selected inputs/results. Large source trees are attached to versioned Releases in chunks below 512 MiB. Each archive carries a manifest recording source path, archive path, bytes and SHA-256. A restore check downloads each asset into a clean directory, extracts it and compares every listed file. The corresponding project report records the result and any exceptions.

## Third-party materials

Upstream software, model weights, reference structures, papers and datasets are not relicensed by this portfolio. Their attribution, version, source URL, license status and whether locally modified must be recorded at item level before redistribution. If the right to redistribute is uncertain, retain the item locally and publish only a citation and retrieval instructions.

## Limitations

The current archive check validates byte identity for released source files; it does not rerun the scientific workflows, validate biological hypotheses, reproduce external services, or establish experimental performance. A clean restore is an archive integrity check, not a scientific replication.
