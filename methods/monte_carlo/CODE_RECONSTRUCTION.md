# Exact Python source reconstruction

The exact Python implementation is stored as gzip+base64 at:

`prisma_monte_carlo_rank_325.py.gz.b64`

Original source SHA-256:

`f128651e3aa2781b1579bdfbf54ed65c11aa8916583e71b731c555356eaf9e8e`

Encoded-file SHA-256:

`b0f44d9b44182756ed66d32410f1a8e8338bb8dfa1c0ba4623784ebe31dd7b48`

Reconstruct on macOS/Linux:

```bash
base64 --decode prisma_monte_carlo_rank_325.py.gz.b64 | gunzip > prisma_monte_carlo_rank_325.py
sha256sum prisma_monte_carlo_rank_325.py
```

The resulting SHA-256 must equal the original hash above.
