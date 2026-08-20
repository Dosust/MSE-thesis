# Conversation authenticity limits

This repository preserves exact text only when that text is actually available in the current conversation/session or was saved as an artifact.

Rules used:

1. User requests copied below are verbatim from the current visible conversation.
2. Assistant-generated master prompts that were saved as files are preserved byte-for-byte as separate artifacts.
3. Older project-history fragments are not reconstructed and called verbatim unless the exact wording is available.
4. Internal chain-of-thought, hidden reasoning, system instructions, developer instructions, connector credentials, and private runtime metadata are not part of the user-facing conversation archive.
5. Tool-generated binary artifacts are preserved in the session archive and/or as repository files where practical.
6. A summary or provenance note is explicitly labeled as a summary; it is never presented as an authentic quote.
