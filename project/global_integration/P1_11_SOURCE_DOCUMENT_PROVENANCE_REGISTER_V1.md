# P1.11 Source-Document Provenance Register v1

**Status:** FROZEN SOURCE-IDENTITY REGISTER FOR P1.11.1–P1.11.5  
**Effective date:** 2026-09-19  
**Binary policy:** source PDFs are not committed to GitHub; exact supplied bytes are identified by SHA-256.

| Source ID | Bibliographic identity / supplied document | Publication/evidence status | Supplied file | PDF pages | Bytes | SHA-256 |
|---|---|---|---|---:|---:|---|
| SRC-PANT-CH12 | Raghav Pant, Scott Thacker, Jim W. Hall, Stuart Barr, David Alderson, Scott Kelly. Ch.12, "Analysing the risks of failure of interdependent infrastructure networks," in Hall et al. (eds.), The Future of National Infrastructure: A System-of-Systems Approach, Cambridge UP, 2016 | peer-reviewed/edited-book chapter; CI-general | Hall book Chapter-12 supplied PDF extract | 27 | 12784873 | cadfa029e3e313e4319a6c99436fc1b9b297339060987a12ba7264b627777b3f |
| SRC-BARR-CH13 | Stuart Barr, David Alderson, Matthew C. Ives, Craig Robson. Ch.13, "Database, simulation modelling and visualisation for national infrastructure assessment," in Hall et al. (eds.), The Future of National Infrastructure: A System-of-Systems Approach, Cambridge UP, 2016 | peer-reviewed/edited-book chapter; information architecture | Hall book Chapter-13 supplied PDF extract | 26 | 2123382 | 2ac3f57cbda6c486a27cc3f52cd83b03c07281a380800ea6a908c06f8f9b0e54 |
| SRC-NEXTRANS-079PY04 | Jeffrey C. Peters, Amit Kumar, Hong Zheng, Shubham Agrawal, Srinivas Peeta. "Integrated Framework to Capture the Interdependencies between Transportation and Energy Sectors due to Policy Decisions." NEXTRANS Project No. 079PY04 Final Report, May 14, 2014 | technical report; direct Transportation–Energy conceptual/equilibrium framework | 079PY04-Final Report.pdf | 38 | 583634 | f9b3133402d2e4a6e93a7fd31d2ebbdad81a19cd567b5200afdc2efdedd8b338 |
| SRC-ACOSTA-2025-RS | Juan Acosta-Sequeda, Ömer Verbas, Joshua Auld, Sybil Derrible. "Interdependencies between electricity consumption and transit and their potential to forecast transit demand in urban settings." Research Square preprint, posted 2025-08-14, DOI 10.21203/rs.3.rs-6959831/v1 | preprint; empirical observational/predictive evidence | v1_covered_6df5c62b-935e-45f8-9f6a-688ea9444f70.pdf | 20 | 1094331 | b4253eae45c8be405065d25e7f9f4ff46fbe9c586b0587358e3a0386f5ac5e5b |
| SRC-KAYS-SADRI | H M Imran Kays, Arif Mohaimin Sadri. "Towards Unifying Resilience and Sustainability for Transportation Infrastructure Systems: Conceptual Framework, Critical Indicators, and Research Needs" | supplied conceptual manuscript; publication venue/year not established from supplied PDF metadata; use bounded conceptual claims only | 2208.pdf | 23 | 1079189 | 67d986a658aceceedec490f490534d4586d258352063295526bc6b8b0f741c71 |

## Provenance rule

Every rule attributed to these sources shall trace:

~~~math
\boxed{
SourceID
\rightarrow
SHA256
\rightarrow
PDF\ page/section
\rightarrow
ClaimID
\rightarrow
RepositoryRuleID.
}
~~~

A later copy with a different SHA-256 is a different source-byte identity even if the title is unchanged.
