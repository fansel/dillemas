# Who may read our messages? — speaker notes

Facts as of 27 October 2026. Page numbers match the PDF.

## Part 1 · The dilemma (pages 1–4)

**1 · Cover.** Our topic is the conflict between privacy and state surveillance of communication. We use Chat Control as a case study.

**2 · The question.** Who should be able to read your messages? Most people would say: me, the person I write to, and in some cases the police with a court order. Politicians, courts and engineers have argued about where that line goes for more than 30 years.

**3 · Two legitimate goals.** On one side, the state has a duty to protect people from serious crime, for example children from sexual abuse. On the other side, the EU Charter protects private life and personal data (Articles 7 and 8). More access for the state means less confidentiality, and the other way round. Every option gives something up, which is why we treat this as a dilemma.

**4 · Who faces the dilemma?** A dilemma needs someone who has to decide or act and gives up something legitimate either way. The course asks us to explain why it is a dilemma and for whom.
- **The EU and its member states (Commission, Parliament, Council) decide.** Protect children, or protect private communication? Say aloud: each choice gives up a goal that deserves protection. This is the main case.
- **Providers (Signal, WhatsApp, Meta and others) must act.** Scan messages and weaken trust in encryption, or refuse and risk leaving the EU. Signal has said it would rather leave the EU (slide 18).
- **Users carry the consequences.** Parents in particular want children protected and their chats private. They do not decide, but they live with the result (say this aloud).
- **Children** are the people the law wants to protect, and they have no say in the decision (say this aloud).
If asked: investigators have their own tension, they want access but also need methods that hold up in court and systems that are secure. We left them out to keep the slide short.

## Part 2 · Why privacy matters (pages 5–9)

**6 · "I've got nothing to hide".** This is the most common argument for surveillance. Daniel Solove (2007) and Bruce Schneier (2006) show three problems with it:
- Small, harmless facts combined reveal health, beliefs and relationships. Schneier cites Cardinal Richelieu: give me six lines written by the most honest man and I will find enough to hang him.
- Privacy is not secrecy. We put blinds on windows and a door on the bathroom without being criminals. Snowden: saying you have nothing to hide is like saying you do not care about free speech because you have nothing to say.
- Rules change, so data that is harmless today can be used differently by a future government or in another country.

If asked: Adam Moore (2011) adds that surveillance hits some groups harder, based on appearance, ethnicity, sexuality and religion. This links to Justice on slide 22.

**7 · Chilling effect.** Jon Penney (2016) measured monthly views of 48 Wikipedia articles on terrorism-related topics. After the Snowden revelations in June 2013, views dropped by about 20 percent and kept falling. People avoided reading legal information because they felt watched. Surveillance changes the behaviour of people who have done nothing wrong.

**8 · Access can be used by others.**
- **Athens Affair (2004–05):** unknown attackers used the legal wiretap function in Vodafone Greece's network to listen to about 100 phones, including the Prime Minister's.
- **Salt Typhoon (2024–25):** Chinese state hackers got into US telecom networks, including the systems for court-ordered wiretaps. In 2025, 13 countries reported more than 200 affected US organisations. In December 2024 the FBI and CISA advised Americans to use encrypted messengers.

The 2015 paper "Keys under doormats" by leading security researchers concludes that a way in that works only for authorities cannot be built.

**9 · Function creep.** Spyware is sold to fight terrorism and serious crime, but journalists, activists and politicians keep appearing among the targets:
- **Pegasus Project (2021):** a leaked list of about 50,000 phone numbers of possible targets.
- **Germany (2025):** the Federal Constitutional Court ruled that state trojans may not be used for minor offences.

## Part 3 · Why the state wants access (pages 10–12)

**11 · Encryption also hides crime.** To be fair to the other side. Most platforms report child abuse material to NCMEC, a US organisation, because Europe has no central body of its own. In 2023 NCMEC received 36.2 million reports, in 2024 20.5 million: 43 percent fewer. Two things explain the drop:
- **Bundling:** one viral video shared thousands of times now counts as one report. Counted as incidents, the 2024 figure is 29.2 million, so about 7 million fewer than in 2023.
- **Messenger's end-to-end encryption:** NCMEC calls this the most probable factor. Facebook reported about 6.9 million fewer reports after adjusting for bundling. This is NCMEC's own analysis, not an independent audit.

Google, X, Discord and Microsoft also reported at least 20 percent less, which NCMEC cannot explain by encryption. The REPORT Act (2024) was meant to increase reporting, because it added child trafficking and online enticement to the offences platforms must report. Yet reports fell. The system is also fragile: US law requires platforms to report what they find, not to look for it, so scanning is voluntary.

**12 · Targeted operations work.**
- **EncroChat:** police hacked the network, which led to 6,558 arrests in Europe and about 900 million euros seized.
- **ANOM:** the FBI secretly ran an encrypted app used by criminals, which led to more than 800 arrests in 16 countries.
- **Sky ECC:** in Germany alone, 585 arrest warrants followed.

These cases show that investigators can reach encrypted communication without scanning everyone. They are still controversial: courts, including the EU Court of Justice in 2024, have ruled on how such evidence may be used.

## Part 4 · Case study: Chat Control (pages 13–19)

**14 · Encryption moved the access point.** Before end-to-end encryption, the provider could read messages, so police could ask the provider. With end-to-end encryption the provider only sees scrambled data, and investigators call this "going dark". The state now has three options, all on the device itself: hack the phone, scan on the phone, or force companies to weaken encryption.

**15 · Chat Control 1.0 and 2.0.** Chat Control started after the EU extended the ePrivacy Directive to messaging apps, which made the voluntary scanning that companies were already doing illegal.
- **1.0 (2021):** a temporary EU exception lets tech companies, such as Google, Meta and Microsoft, scan messages voluntarily. It expired in April 2026, which left several months without a legal basis, and was renewed in July 2026 until 2028, now excluding encrypted chats. Say the last part out loud, because it is not on the slide.
- **2.0 (2022):** a permanent law. Authorities could order a service to scan all its users' messages, including encrypted ones. A new EU Centre would handle reports in Europe instead of sending them to NCMEC in the US. Version 2.0 is only a proposal; it has not been adopted.

**16 · Client-side scanning.** To scan encrypted chats, the check has to happen on the user's own device, before the message is encrypted. That is why it is called client-side scanning. Known images are compared with a list of fingerprints (perceptual hashes), and new material is assessed by AI, which makes more errors. If something is flagged, a report goes to the EU Centre and then to the police. The encryption stays technically intact, but its promise that no third party sees your message is gone. That is why researchers treat client-side scanning like a backdoor (Abelson et al., 2024).

This has been tried. In 2021 Apple announced NeuralHash: photos were compared on the iPhone with a list of known abuse images before upload to iCloud. Apple cancelled the project in 2022 and later explained that it would create new attack paths for data thieves. The lesson is about the architecture, not only about hacking: private encryption and scanning on the device exclude each other. Note that NeuralHash scanned photos, not chats.

For your own knowledge: a perceptual hash is a fingerprint of how an image looks, not of its bytes, so resizing or compressing gives the same or a very similar hash, while a normal cryptographic hash changes completely. It can fail in both directions: different images can collide, and small deliberate edits can fool the detector.

**17 · Status.**
- **May 2022:** the Commission proposed mandatory scanning.
- **Nov 2023:** Parliament said only suspects, and only with a judge's order.
- **Nov 2025:** member states agreed on voluntary scanning instead of an obligation.
- **Sep 2026:** after six negotiation rounds there is still no deal on private chats.
- **Next round:** reported for December, but not officially confirmed.

Already agreed: risk assessment for platforms, removal and blocking orders, and the EU Centre. Still open: scanning of private chats, encrypted services, and age verification.

**18 · Who stands where.**
- **Commission:** started at "scan all chats".
- **Member states:** want voluntary scanning by companies.
- **Parliament:** wants only targeted orders against suspects.
- **Signal and about 500 researchers:** reject scanning of private chats; Signal said it would rather leave the EU.

**19 · False alarms.** Even if the technology worked, there is the problem of scale. A system that is 99.9 percent accurate, scanning a billion messages a day, still produces a million false alarms every day. The bar chart shows the share of reports to police that did not lead to a case. The measures differ slightly, so say so:
- **Ireland (2020):** 471 of the reports from NCMEC, more than 11 percent, were not abuse material (ICCL figure confirmed by the Gardaí, via RTÉ).
- **Germany (2023):** 89,336 of 180,287 reports were criminally relevant, so about half were not.
- **Norway (2023):** 4,500 of 13,211 tips were taken on; the rest were rejected, mostly because the act is not a crime in Norway or is below the police threshold.
- **Switzerland (2019):** fedpol said only about one tenth of the reports were criminally relevant. This is a single sentence quoted by Beobachter; the 90 percent is our calculation.
- **Czechia (2024, light bar):** 888 of 22,553 reports were passed on for investigation. This is a different measure: not passed on is not the same as false.

Sources: RTÉ and Irish Times (2022), netzpolitik.org (2024), Kripos (2024), Beobachter (2022), Czech Police.

## Part 5 · Is Chat Control ethical? (pages 20–25)

**21 · Framework.** We use the principlist framework for cybersecurity ethics by Formosa, Wilson and Richards (2021) from Lecture 2. The authors argue that applying the big ethical theories directly leads to conflicting results, because no theory has overwhelming authority. So they propose five mid-level principles for cybersecurity. Their definitions, in short:
- **Beneficence:** technology should benefit people, promote well-being and make our lives better overall.
- **Non-maleficence:** technology should not be used to intentionally harm people or to make our lives worse overall.
- **Autonomy:** people should be able to make informed decisions for themselves about how technology is used in their lives.
- **Justice:** technology should promote fairness, equality and impartiality, and should not unfairly discriminate, undermine solidarity or prevent equal access.
- **Explicability:** technology should be intelligible, transparent and comprehensible, and it should be clear who is accountable.

Important: these principles can conflict with one another and need to be balanced in a context-sensitive manner, which can result in a range of ethical trade-offs (Formosa et al., p. 1). The framework does not rank them. We apply them to one case: Chat Control 2.0, the proposal to order services to scan private chats, including encrypted ones.

Our own method, not from the paper: for each principle we list what speaks for and against Chat Control, and our verdicts (open, not met) are our own scale. The principles overlap, so the same fact can matter under more than one of them. We try to use it under the principle where it fits best.

**22 · Chat Control 2.0 through the five principles.** This is our group's assessment. Walk through the table row by row, first what speaks for the proposal, then what speaks against it:
- **Beneficence (open):** it could find abuse material and offenders in encrypted chats, where reports have fallen. But the benefit is unproven: more reports do not show that more children are protected, and offenders can switch to channels that are not scanned (plausible, but we have no data on how many do). Targeted operations (EncroChat and others) are not an argument here: they concern organised crime, not child abuse, so they show that alternatives exist in principle, not that they work for child abuse. We raise that as a question of milder means in the footer and on the next slide.
- **Non-maleficence (open, debatable):** this is the principle where the definition itself is debatable. It says technology should not be used "to intentionally harm humans or to make our lives worse overall". Intentional harm: no, the aim is child protection. But "worse overall" is a net judgement, and the benefit is still open under Beneficence, so we cannot claim a net harm for sure. In favour: stopping the spread of abuse images could prevent further harm to victims. Against: four places where harm could arise, from most to least certain (costs without benefit, if offenders switch channels, belongs to Beneficence, not here):
  1. **Weaker security for all:** a new component on every device reads messages before encryption. It can be hacked or abused, and an end-to-end encrypted messenger no longer promises that only the two of you can read. Experts share this concern (Abelson et al., 2024). Analogies: Athens Affair, Salt Typhoon.
  2. **Wrongly flagged users:** their account, contacts and data can be lost and the police may get involved. How many are affected is unclear, the harm for them is high. False alarms also tie up investigators who are then missing for real cases.
  3. **Fewer confidential spaces:** people write differently when they know they are scanned (Penney: about 20 % fewer views after Snowden). This hits journalists and sources, doctors, lawyers and people seeking help. Plausible, but not measured for Chat Control.
  4. **Later misuse:** the infrastructure stays and a future government could use it for other purposes (analogy: Pegasus). This is a fear, not a finding.
  Honest summary: for most people nothing changes in daily life. The harm is spread out, probable and long-term, and it hits a few people hard. "Make our lives worse overall" means adding everything up and weighing it against the benefit, which is still open. So we call it debatable, not "not met". Back-up if asked:
  - **Security:** Apple dropped its own iCloud photo scanning plan in December 2022 and explained in September 2023 that it would create new threat vectors for data thieves. That was iCloud photos, not Chat Control, so it is an analogy. The EDPB and EDPS (joint opinion, July 2022) warned of generalised and indiscriminate scanning and pointed to error rates. The Council Legal Service (opinion 8787/23, April 2023) called detection orders a particularly serious limitation of the rights to privacy and data protection; the Commission services disagreed.
  - **Error rates are disputed.** The Commission report on the interim regulation (COM(2023) 797) shows low reversal rates after appeals: Meta 2022 reinstated 3.7k of 6.6 million actioned items (0.06 %), X about 500 of 501k suspended accounts (0.10 %). But providers did not report false positives per technology, reversal rates are not the statistical definition, and few users appeal. The German police figure (about half of 89,336 + 90,951 reports not criminally relevant in 2023) measures something else: what police sort out later. All of this concerns today's voluntary scanning, not Chat Control 2.0.
  - **Harm to innocent users:** the 2022 New York Times case of a father whose account was disabled after sending photos of his sick son to a doctor; police cleared him, Google rejected the appeal. It concerns Google's own scanning, not Chat Control.
  - Athens Affair, Salt Typhoon and Pegasus are analogies for misuse of surveillance functions, not proof for Chat Control. Hash matching produces fewer false alarms than AI classifiers (our assumption from the debate, not a source). Lists that could be widened later are covered under Explicability.
- **Autonomy (not met):** victims have a real interest in privacy and dignity, because images of their abuse spread without their consent. But privacy is invaded without a real choice: every message is scanned on your own phone before end-to-end encryption can protect it, and refusing means not communicating. We put the invasion itself under Autonomy, because it is wrong even if nothing is found (the answer to "nothing to hide"). The consequences, such as security loss or wrongly flagged users, go under Non-maleficence. The framework has no separate principle for privacy, so this placement is our interpretation. The chilling effect can be named under both: loss of freedom (autonomy) and harm to people who need confidential spaces (non-maleficence). The encryption stays technically intact, but it is bypassed. Your device is normally the place where nobody reads along.
- **Justice (not met):** the question is whether benefits and burdens are distributed fairly. In favour: solidarity with victims, which the definition names explicitly, and the same rules apply formally to all users. Against: the benefit goes to a few, but the burden falls on all users, who are treated as suspects without cause.
- **Explicability (not met):** in favour: one central EU Centre receives all reports, so there is a defined point of accountability. Against: hash lists and AI cannot be checked and the lists are secret, so the purpose could be widened unnoticed. Responsibility is split between providers, EU Centre and police, so it is not clear who is accountable.

How we sorted the arguments (ask if someone wonders): the scan itself goes under Autonomy, because reading every message is intended and is a loss of control that stays wrong even if nothing is found (answer to "nothing to hide"). Loss of privacy can also be seen as harm, a loss of a protected space, so it counts under both Autonomy and Non-maleficence. What follows from the scan goes under Non-maleficence: it is not the aim but foreseeable, because the EDPB, EDPS and the Council Legal Service warned beforehand. The definition says "intentionally", so be ready for "not intended, so no violation". Our answer: the definition also says "make our lives worse overall", and foreseen harm that is accepted should count. The framework has no principle for privacy, so the placement is our interpretation and a simplification: the same fact can matter under more than one principle. Milder means (targeted measures) are not a principle either, so we ask about them on the next slide.

Footnote that was on the slide, say it aloud if asked: benefit unclear, error rates disputed, milder means untested for child abuse. This is our group's judgement, and hash matching and AI detection have different error rates.

Result: three principles are not met by the design itself (autonomy, justice, explicability). Benefit and harm depend on how it works in practice, so we call them open and debatable. A milder means has not been ruled out for child abuse. It is a judgement, not a calculation.

Honest gap: our evidence for targeted measures (EncroChat, ANOM, Sky ECC) concerns organised crime, not child abuse. Be ready for that question. Also, the NCMEC reports come from platforms scanning unencrypted content, so the German figure does not say what scanning encrypted chats would find.

**23 · Check everyone, or only suspects?** This is the step from our assessment of Chat Control to the alternative. Left: the European Commission's proposal, scan everyone, all chats, also encrypted. Right: the European Parliament's position (November 2023), only suspects, with a judge's order. This is not our own solution. Julia already showed both positions on slides 17 and 18, so do not explain them again. Say: "The Parliament says this is the better alternative. We test that claim with the same five principles."

Two separate questions, keep them apart if someone asks:
- **Who is checked?** Everyone or only suspects. That is what the grids show.
- **How do investigators get at the content?** A scanner on every phone, or access to one device. "Targeted" does not mean state trojan. For an end-to-end encrypted chat of a suspect, the content can only be reached on the device or inside the group: spyware or a state trojan, reading a seized device, or undercover work in the chat. Outside the encryption there are metadata, unencrypted backups and tips from users or hotlines. The Parliament does not prescribe a trojan. As far as we know, its position excludes scanning of encrypted chats and limits orders to suspects, and national law decides how investigators reach encrypted content (in Germany, for example, the rules on source telecommunications surveillance). Check this against the Parliament's text before you present.

**24 · The alternative.** The slide shows one sentence per principle compared with Chat Control 2.0. Say the comparison aloud (unclear, mixed, better, better, better). Walk through it:
- **Beneficence (unclear):** finds known suspects and can shut down whole networks. But it only finds people who are already suspected, and our evidence (EncroChat, ANOM, Sky ECC) concerns organised crime, not child abuse. We do not claim that targeted measures work equally well for child abuse.
- **Non-maleficence (mixed):** far fewer people are affected. But spyware needs security holes (if the state keeps them secret, they stay open for everyone, which is our own background knowledge, not from a source), the tool can be misused (Pegasus), and the German Federal Constitutional Court limited state trojans in 2025 to serious crimes.
- **Autonomy (better):** only suspects are affected and a judge decides. Suspects still lose their privacy.
- **Justice (better):** the burden falls on people with a concrete suspicion. The price: less protection for victims of offenders nobody suspects.
- **Explicability (better):** a judge's order is documented and can be challenged. Hacking tools work in secret by nature.
Message: it is not a perfect solution, it is a different trade-off. Be ready for "does it work for child abuse?" and answer honestly that we do not know.

**25 · Conclusion.** Two parts: the dilemma, then our position.

**The dilemma**
1. **Every option gives something up.** Protecting children and protecting private communication are both legitimate goals. This is a dilemma for the EU and its member states who decide, for providers who must act, and for users who live with the result. The dilemma does not go away, whatever is decided. (The conflict is also old: from the Clipper Chip to Chat Control each new technology has raised it again. Say that aloud if you want.)

**Our position** (say: "If we have to weigh it for Chat Control, this is where we land.")
2. **Chat Control 2.0 conflicts with freedom, fairness and transparency.** Three principles are not met. Harm and benefit remain open: harm is debatable (intentional or not, worse overall or not) and the benefit is unproven.
3. **The Parliament's targeted model does better on those three,** but it only finds people who are already suspected. Our evidence for targeted work concerns organised crime, not child abuse.
4. **Our weighing.** Certain, widespread costs weigh more than an unproven benefit. The costs are built into the design: every message is read, everyone is a suspect, nobody can check the lists. The benefit depends on how it works in practice, and nobody has shown it. Say aloud: independent evidence of a large benefit would change our weighing. That means we treat autonomy as a heavy weight, not as an absolute limit. If someone asks why you do not call it a ban: the principles can conflict and have to be balanced in context, and this is our balance, not a calculation.

**Our answer to the opening question (slide 2):** Who may read our messages? Not everyone, all the time. A judge, and a concrete suspicion.

Closing line, say it aloud (Schneier, 2006): the choice is not security versus privacy, but liberty versus control.

Left out of the slide: encryption moved the point of access onto our devices (slide 14), and what is built for surveillance stays available to future governments and to attackers (slides 8 and 9). The infrastructure argument is a risk, not a finding.

**26 · References.** **27 · Thank you.**
