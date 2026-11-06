# Chapter 2: The Canaries

Nineteen percent.

Hold that number for a moment, because the rest of this chapter is the story of where it came from, what it does and does not mean, and why three economists at Stanford spent a year stress-testing it before they would say it out loud.

In the spring of 2025, the *Wall Street Journal* told its readers that young graduates were facing an employment crisis.¹ The Federal Reserve Bank of New York, which tracks the fortunes of recent college graduates the way a cardiologist tracks a worrying rhythm, was publishing numbers that said much the same thing: the people who had done everything right (the degree, the internships, the GPA) were waiting longer, applying more, and hearing back less.² Anyone with a niece or a nephew graduating that year already knew this. The group chats knew it. The career-center waiting rooms knew it.

What nobody knew was why. A bad year for graduates has plenty of ordinary suspects. Interest rates had climbed faster than at any point in four decades, and companies that borrow less, hire less. The technology sector was still digesting its pandemic hiring binge. Remote work had scrambled the geography of entry-level jobs. And somewhere in the lineup, looking exactly as guilty or as innocent as the others, stood generative AI. Two and a half years old as a mass-market product, already writing code, answering support tickets, and summarizing documents, which happens to be a fair description of what a 23-year-old office worker is hired to do.

Opinion split along the usual lines. The doomers said the machines had arrived. The boosters said the kids should learn to prompt. What neither side had was evidence that could separate AI from the interest rates, the tech hangover, and the rest of the lineup.

The evidence, as it turned out, was sitting in the payroll system.

Every month, a company called ADP runs payroll for firms that collectively employ more than 26 million American workers.³ Payroll data has a property that surveys, job postings, and LinkedIn profiles do not: it is administratively true. Nobody rounds up their headcount to impress a processor. A paycheck either went out or it didn't. If you want to know who is actually employed, at what age, in what occupation, month by month, close to real time, there are few better places on earth to look.

In 2025, three researchers at Stanford's Digital Economy Lab got that look: Erik Brynjolfsson, Bharat Chandar, and Ruyu Chen. Brynjolfsson had spent three decades studying how technology moves through economies, long enough to have seen two previous rounds of "the machines are coming" come and mostly go. The team assembled a balanced panel from the ADP records: the same firms, tracked every month, between 3.5 and 5 million full-time workers at a time, each one tagged with an occupation code that could be matched to measures of how exposed that occupation's tasks are to AI.³ Then they asked a question that sounds simple and had never been properly answered. Since ChatGPT arrived, who, exactly, has stopped getting hired?

Not "which jobs feel threatened." Not "which CEOs predict layoffs." Who, in the administrative record, with an occupation code and a birth year, is missing?

The answer had a shape nobody's talking points had predicted. It wasn't an occupation. It wasn't an industry. It was an age.

## No apocalypse, one exception

Start with what the payroll data does *not* show, because it is the part both camps get wrong.

It does not show an AI jobs apocalypse. Between November 2022, the month ChatGPT launched, and June 2026, employment across the whole ADP sample rose about 6 percent. Even in the occupations most exposed to AI, the quintile whose task lists overlap most with what a language model can do, employment *grew* about 4 percent.⁴ Growth, not collapse. Anyone telling you that AI has already hollowed out the American workforce is describing a dataset that does not exist. The researchers wrote it as their first fact, in plain language: no evidence of widespread, economy-wide job displacement.⁴

Then they split the workers by age, and the picture cracked.

For workers aged 26 and up, more-exposed and less-exposed occupations tracked each other the way they always had. Whatever was happening to bookkeepers was happening to 45-year-old bookkeepers and 28-year-old bookkeepers in roughly equal measure. The lines moved together.

For workers aged 22 to 25, the lines tore apart.

In the occupations least exposed to AI (the bottom three quintiles of exposure, the jobs built on hands, presence, and persuasion), employment of 22-to-25-year-olds grew about 10 percent over those three and a half years. Perfectly healthy. In the two most exposed quintiles (software development, customer service, the clerical core of the office), employment of the same age group *fell* about 11 percent.⁵

Run the comparison the way the researchers did and you get the number this chapter opened with. Had young workers in AI-exposed occupations simply kept pace with their less-exposed peers, not boomed, just kept pace, there would be roughly 19 percent more of them employed in those occupations than there actually were in June 2026.⁵ One in five, relative to the path not taken. Their older colleagues, in the same occupations, often at the same firms, show no comparable gap at all.⁶

**[FIGURE 2.1 — "Junior hiring fell first"]**

The young workers were not spread across the economy evenly enough for the damage to show up in headlines. The most exposed occupations held 57 percent of this age group's employment when ChatGPT launched, so an 11 percent decline there dragged the whole cohort's employment roughly flat, down 1.9 percent, across a period when every older age band grew, some by as much as 11 percent.⁷ Flat is the kind of number that hides. Nobody writes a front-page story about flat. You only see the hole when you know which slice of the workforce to cut.

And here is the detail that should bother you most. This was not one bad reading. The Stanford team published first in August 2025, with data through July of that year, and their headline estimate (young workers in exposed occupations, adjusted for shocks hitting their firms) was a 13 percent relative decline. They updated with data through September 2025: 16 percent. By the time the data ran through June 2026, the simpler kept-pace measure stood at 19 percent, up from 15 percent at the previous vintage.⁸ Each time the economists went back to the payroll records, the gap had grown. A one-off reading can be noise. A reading that widens every time you take it is a trend, and trends have causes.

**[FIGURE 2.2 — "The gap is an age gradient"]**

## The door narrows

If your mental image of all this is a wave of 24-year-olds carrying boxes out of office buildings, replace it. That is not what the data shows, and the difference matters for everything you'll decide after reading this book.

The payroll records let the researchers separate two ways an occupation shrinks: people being pushed out, and people not being let in. These are different events with different victims. A separation is a person losing the job they had. A hiring slowdown is a person never getting the job at all. A quieter injury, with no severance letter and no statistic attached to their name.

The young-worker gap is almost entirely the second kind. Separation rates for young workers in exposed occupations did not spike. They fell, and fell at least as much as in the least exposed occupations, the opposite of what a layoff wave would look like.⁹ What changed was the front door. After 2022, the gap between how often exposed and non-exposed employers hired young people opened up and kept opening. Firms were not firing their junior staff. They had stopped replacing them.

This happened inside a labor market that economists at the St. Louis Fed took to calling "low-hire, low-fire": sluggish churn everywhere, for everyone.⁹ But a low-hire market punishes one group above all others, the people whose entire access to employment runs through being hired. A 45-year-old in a slow market keeps her job. A 23-year-old in a slow market never gets one.

So the next question was obvious. Hiring of young people slowed, but was AI the reason, or just a bystander? The researchers had a way to get closer to an answer, and it came from an unexpected source: the AI companies' own logs.

Anthropic, the maker of the Claude models, publishes an index of what people actually use its AI for, mapped to the government's catalogue of occupational tasks, and classified by *how* the AI is used, which is the useful part. Some conversations look like delegation: here is the task, do it, give me the output. The index calls that automation. Others look like collaboration, with drafts going back and forth, questions, refinements. It calls that augmentation.¹⁰ Chapter 4 lives inside this data; for now you need one result.

When the Stanford team sorted occupations by how much AI usage in them is *automation*, the young-worker decline snapped into focus. In an occupation one standard deviation higher on automation-style usage, employment of 22-to-25-year-olds fell about 9.8 percent more. A strong, statistically solid relationship that weakens with every step up the age ladder until, for workers over 40, it disappears.¹¹ Sort the same occupations by *augmentation*-style usage instead and the pattern inverts: no decline for the young, and for workers aged 41 to 49, employment actually rose with complementary usage, by about 2.4 percent per standard deviation.¹¹

Those two sentences, together, are the clearest mechanism signal anywhere in this book. Where people use AI to *do* the work, the youngest workers are disappearing from payrolls. Where people use AI to *help with* the work, experienced workers are gaining. The machine is not eating jobs. It is eating a particular kind of work, and that kind happens to be concentrated at the bottom of the ladder.

Why the bottom? The researchers' suggestion is uncomfortable for anyone who has recently paid tuition. What a new graduate sells is codified knowledge: the documented, teachable, textbook kind, exactly what a large language model is made of. What a veteran sells is tacit knowledge: the tricks, judgment, and client scar tissue that never got written down, and that a model trained on written things therefore never learned. In the data, occupations heavy on codified knowledge show the slowest growth in young hiring, while occupations heavy on tacit knowledge show the fastest growth for experienced workers.¹² A model, in other words, substitutes for school and complements experience. The entry-level job was where school got converted into experience. That conversion point is what is narrowing.

One more fact completes the picture, and it answers the question every economist asks first: what about wages? If AI were making junior labor less valuable, you might expect junior pay to sag. It hasn't, much. Base salaries for young workers in exposed occupations have tracked their peers' with little divergence; adjustment is happening in headcount, not in pay stubs.¹³ Firms, faced with a cheaper machine substitute, are not renegotiating with the 23-year-old. They are simply not calling her back. Wages are sticky; job offers are not. Which is why this chapter is not called "The Pay Cut." The adjustment chose a different margin, the one that never shows up on anyone's payslip because the payslip never gets printed.

## The cross-examination

A number like 19 percent deserves hostile questioning, and to their credit, the people who produced it did much of the interrogating themselves. Here is the honest version: the objections, and how far each one goes. If you only ever repeat this chapter's headline at a dinner party, repeat this section with it.

*Objection one: the trend started before ChatGPT.* Partly true. AI-exposed occupations boomed during the pandemic (they were the work-from-home jobs), and some of the decline since is that boom unwinding. The researchers quantified it. The exposed occupations' relative position climbed about 13 percentage points from its 2018–19 baseline to a mid-2020 peak, and by November 2022 had fallen right back to baseline. Everything since is new territory: the gap has dropped roughly 17 further points *below* where it stood before anyone had heard of COVID, and it kept falling for more than three years, through the period when interest rates peaked, flattened, and declined.¹⁴ A hangover ends when you're back to normal. This didn't.

*Objection two: it's just education.* The sharpest statistical challenge. AI-exposed occupations are college occupations, and when the researchers control for the share of workers with degrees, their estimate for young workers shrinks from about 18 percentage points to about 9. Still negative, barely significant.¹⁵ But think about what that control does. Generative AI is precisely a machine for reproducing what college teaches. Stripping out "educated occupations" from an analysis of AI may be stripping out the mechanism itself, like controlling for smoke in a study of fires. The honest statement is a range: somewhere between 9 and 18 points, depending on what you believe education is doing in the equation.¹⁵

*Objection three: ADP isn't America.* Correct, and the researchers say so. Their sample tilts toward larger firms and overrepresents exposed occupations. In Census survey data, the same comparison over 2022–24 shows a gap of about 2 percentage points, against 13 in ADP over the same window. Same direction, much smaller.¹⁶ The two sources agree closely where it matters most, in professional, financial, and information services (a gap of about 21 points in the survey, 23 in ADP), and diverge in education, health, and government, where survey reweighting problems muddy the comparison.¹⁶ A separate Census Bureau study of government administrative records found the same age-and-exposure pattern in direction.¹⁷ Treat the 19 as a reading from one large, tilted, unusually sharp instrument: directionally corroborated, magnitude still under review.

*Objection four: other researchers disagree.* Some do, and the strongest dissent deserves naming. In Denmark, economists studying eleven heavily exposed occupations with national data found precisely estimated effects of roughly nothing.¹⁸ Denmark is not America (different labor law, different firm sizes, different adoption), but a null is a null, and it should keep your confidence interval wide. On the other side of the ledger sits a Harvard study built from an entirely different instrument: the résumés of some 62 million U.S. workers across 285,000 firms. It compared companies that visibly adopted generative AI, which you can see in their job postings, against those that hadn't. From the first quarter of 2023, junior employment at the adopters fell sharply, roughly 9 to 10 percent relative to non-adopters, while senior employment held. The decline was concentrated in exposed roles and ran, once again, through slower hiring.¹⁹ Different data, different method, same shape: young, exposed, unhired.

So where does the cross-examination leave us? The Stanford authors chose their title with care. Canaries were not deployed in coal mines to prove the presence of gas. They were deployed to give an early, imperfect, directionally reliable signal. One you would be a fool to ignore and a different kind of fool to treat as a verdict. These are descriptive facts, not causal estimates; the authors say so on page one.²⁰ Something real is happening to the youngest workers in the most exposed occupations. It is happening through hiring. It tracks automation-style AI use specifically. It has been corroborated in direction by three independent data sources and challenged in magnitude by two. That is the state of the evidence, and it is more evidence than any opinion you heard this week.

## What the canary knows

Step back from the regressions and look at what the payroll records are actually describing. Millions of times a month, somewhere in America, a hiring decision quietly resolves. A manager has a gap, a budget, and now a third option that didn't exist in 2021. The data says those managers have not been firing the young people they already trained. They have been deciding, one requisition at a time, not to train the next one. No memo announces this. It is visible only in aggregate, as a 19 percent hole where a cohort should be. A hole that was 15 percent one data release earlier.⁸

Every previous chapter of automation anxiety asked, "Will the machines take the jobs?" The payroll data suggests that was the wrong question, with the wrong tense. The better question is the one this book keeps asking: *which tasks, done by whom, at which rung?* As of June 2026, the answer written in the ADP records is: codified office tasks, done by 22-to-25-year-olds, at the bottom rung. And the mechanism is a door closing, not a trapdoor opening.

But payroll is a lagging truth. It tells you who got hired months after someone decided to hire them. The deciding happens earlier, in a document every company writes and most workers never read closely: the job posting. If the entry-level door is narrowing, the postings should show the frame shrinking before the payroll shows fewer people walking through. They do, and that trail of evidence, from what employers ask for to what they quietly stopped asking for, is the next chapter.

## Notes

1. Lahart, J. & Chen, T., "Young Graduates Are Facing an Employment Crisis," *Wall Street Journal*, 2025.
2. Federal Reserve Bank of New York, "The Labor Market for Recent College Graduates," 2025.
3. Brynjolfsson, E., Chandar, B., & Chen, R., "Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence," Stanford Digital Economy Lab, Aug 2026 revision, Section 1 (ADP balanced panel, Jan 2021–Jun 2026; 3.5–5M workers/month). https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf
4. Ibid., Fact 1 and Fig. 1 (+~6% overall; +~4% most-exposed quintile).
5. Ibid., Fact 2 (−~11% vs +~10%; 21 pp divergence; 19% kept-pace shortfall).
6. Ibid., Abstract and Fact 2 (no comparable gap for experienced workers).
7. Ibid., Fact 2 and Fig. 2 (57% share; −1.9% cohort total; up to +11% for ages 35–40).
8. Ibid., Introduction (13% at Jul 2025 vintage; 16% at Sep 2025; kept-pace 15% → 19% by Jun 2026).
9. Ibid., Fact 4 (hiring vs separations; Online Appendix Fig. B.7); Rodgers, W. & Kassens, A., Federal Reserve Bank of St. Louis, 2026 ("low-hire, low-fire").
10. Handa, K., et al., Anthropic Economic Index, 2025 (automation vs augmentation classification).
11. Brynjolfsson, Chandar & Chen (2026), Table 3 Panel A (−0.098 per SD automation, ages 22–25; +0.024 complementarity, ages 41–49).
12. Ibid., mechanism section and Online Appendix J (codified vs tacit knowledge gradients).
13. Ibid., Fact 6 (compensation; stayers and new hires; Online Appendix G).
14. Ibid., Section 4.2 (+13 pp pandemic boom to mid-2020; back to baseline by Nov 2022; ~17 pp below baseline since; continued after rates peaked).
15. Ibid., Table 1 Panels A and C (−0.179 → −0.091 with college-share control) and Section 4.1.
16. Ibid., Section 5, Tables H.1–H.2 (ACS −0.022 [−0.055, +0.011] vs ADP −0.132, 2022–24; professional/info/financial −0.213 vs −0.231).
17. Tucker, L., "You're (not) Hired," U.S. Census Bureau CES Working Paper 26-27, 2026.
18. Humlum, A. & Vestergaard, E., "Large Language Models, Small Labor Market Effects," NBER Working Paper, 2025 (Denmark; 11 exposed occupations; precise nulls).
19. Hosseini, S. & Lichtinger, G., "Generative AI as Seniority-Biased Technological Change," SSRN 5425555, 2025 (≈62M résumés, 285,000 firms; ~9–10% junior decline at adopting firms from 2023Q1; slower hiring).
20. Brynjolfsson, Chandar & Chen (2026), Abstract ("early, descriptive indicators… rather than causal estimates").
