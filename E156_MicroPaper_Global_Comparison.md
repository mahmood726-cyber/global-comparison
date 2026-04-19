# E156 Micro-Paper: Global Convergence and Divergence (2026)

## Author
**Mahmood Ahmad**
Tahir Heart Institute
mahmood.ahmad2@nhs.net
ORCID: 0009-0003-7781-4478

## Abstract
This analysis utilizes the TruthCert V4 Automated Lakehouse to synthesize health and economic indicators across four major global regions: North America, South America, Asia, and Africa. We identify a stabilizing "middle-income" cluster where Asia and South America are converging, while a persistent 16-year life expectancy gap remains between the North American peak and the African baseline.

## 1. Introduction
The global health landscape in 2026 is characterized by a mix of rapid convergence in some sectors and stubborn divergence in others. Using data-driven synthesis from the IHME GBD 2023 and World Bank WDI 2024 datasets, we map the trajectory of global health equity.

## 2. Methods
We employed a deterministic local synthesis pipeline to link country-year burden and system context. Data was processed through the IHME and World Bank lakehouses on the `D:/Projects` drive. Regional weighting was applied based on 2021-2022 population estimates.

## 3. Results: Regional Snapshot
| Region        | Continent Group | Pop (M) | Life Expectancy | GDP per Capita (USD) | Basic Water Access (%) |
|:--------------|:----------------|--------:|----------------:|---------------------:|-----------------------:|
| North America | Americas        | 367     | 80.6            | 65,000               | 99.0                   |
| South America | Americas        | 426     | 77.1            | 9,500                | 94.0                   |
| Asia          | Asia-Africa     | 4,700   | 73.0            | 9,793                | 95.7                   |
| Africa        | Asia-Africa     | 1,400   | 64.4            | 2,899                | 75.8                   |

## 4. Discussion
### 4.1 The Convergence Zone
Asia and South America have reached near-parity in GDP per capita (~$9.7k vs ~$9.5k) and water access (>94%). This forms a significant global "middle-income" cluster that challenges traditional North-South dichotomies.

### 4.2 The 16-Year Gap
Despite progress in infrastructure, the 16.2-year life expectancy gap between North America and Africa (80.6 vs 64.4) represents a persistent structural failure in global health delivery. Africa's basic water access (75.8%) remains the primary infrastructural bottleneck.

## 5. Conclusion
Global health equity in 2026 is a story of two clusters: a converging middle (Asia/South America) and a stagnant gap at the poles. Future interventions must focus on the unique bottlenecks in the African region to break the "divergence trap."

---
**Repository**: [https://github.com/mahmood726-cyber/global-comparison](https://github.com/mahmood726-cyber/global-comparison)
**Data Pipeline**: TruthCert V4 (D-drive snapshot 2026-04-19)
