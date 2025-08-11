# Quarterly Earnings Report — Q2 2025
**Technical Consultant**  
24f2006003@ds.study.iitm.ac.in

<aside class="notes">
- Greet stakeholders.
- State purpose: concise review of results, drivers, and next steps.
- Timebox: 10 minutes + Q&A.
</aside>

---

## Agenda
- Highlights and top-line metrics.  
  <!-- .element: class="fragment" -->
- Segment performance and drivers.  
  <!-- .element: class="fragment" -->
- Key formulas and example calculations.  
  <!-- .element: class="fragment" -->
- Risks, actions, appendix.  
  <!-- .element: class="fragment" -->

<aside class="notes">
- Transition: say each agenda item will take ~2 minutes.
</aside>

---

## Top-line Highlights
- **Revenue**: **+12%** quarter-over-quarter.  
  <!-- .element: class="fragment" -->
- **Net income**: **+8%** quarter-over-quarter.  
  <!-- .element: class="fragment" -->
- **Operating margin**: **15%**.  
  <!-- .element: class="fragment" -->

<aside class="notes">
- Emphasize drivers: volume, price mix, cost controls.
- Call out any one-off items here.
</aside>

---

## Revenue by segment
- **Retail**: 45% of revenue — growth +9%.  
  <!-- .element: class="fragment" -->
- **Enterprise**: 35% of revenue — growth +15%.  
  <!-- .element: class="fragment" -->
- **Other**: 20% — stable.  
  <!-- .element: class="fragment" -->

<aside class="notes">
- Mention top 2 deals that moved Enterprise.
- Note any churn or large renewals.
</aside>

---

## Profitability metrics (formulas)
- Return on Equity (ROE)  
  Inline: $ROE = \dfrac{\text{Net Income}}{\text{Shareholders' Equity}} \times 100\%$.  
  <!-- .element: class="fragment" -->

- EBITDA Margin  
  Block:
  $$
  \text{EBITDA Margin} = \frac{\text{EBITDA}}{\text{Revenue}} \times 100\%.
  $$
  <!-- .element: class="fragment" -->

<aside class="notes">
- Define each numerator and denominator briefly.
</aside>

---

## Model target (symbolic)
We use the target metric:

$$
T = 0.15\cdot \text{GAA} + 0.2\cdot \text{ROE1} + 0.2\cdot P_1 + 0.2\cdot P_2 + 0.25\cdot F
$$

<aside class="notes">
- Explain each variable: GAA (growth-adjusted assets), ROE1 (recent ROE), P1/P2 (policy factors), F (forecast adjustment).
</aside>

---

## Model example (numeric)
Given:
- GAA = 100  
  <!-- .element: class="fragment" -->
- ROE1 = 30  
  <!-- .element: class="fragment" -->
- P1 = 10  
  <!-- .element: class="fragment" -->
- P2 = 5  
  <!-- .element: class="fragment" -->
- F = 50  
  <!-- .element: class="fragment" -->

Compute step-by-step:
1. $0.15 \times 100 = 15$.  
2. $0.2 \times 30 = 6$.  
3. $0.2 \times 10 = 2$.  
4. $0.2 \times 5 = 1$.  
5. $0.25 \times 50 = 12.5$.  
Sum: $T = 15 + 6 + 2 + 1 + 12.5 = 36.5$.

<aside class="notes">
- Walk through arithmetic slowly on-screen; show each term as it's added.
</aside>

---

## Example code: ROI (JS) and simple metrics (Python)
JavaScript (ROI):
```javascript
// ROI as percent
function roi(gain, cost) {
  return ((gain - cost) / cost) * 100;
}
console.log( roi(120, 100) ); // 20
