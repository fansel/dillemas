# Who may read our messages? — speaker notes

Facts as of 27 October 2026. Page numbers match the PDF.

## Part 1 · The dilemma (pages 1–6)

**1 · Cover.** Our topic is the conflict between privacy and state surveillance of communication. We use Chat Control as a case study.

**2 · The question.** Who should be able to read your messages? Most people would say: me, the person I write to, and in some cases the police with a court order. Politicians, courts and engineers have argued about where that line goes for more than 30 years.

**3 · Two legitimate goals.** On one side, the state has a duty to protect people from serious crime, for example children from sexual abuse. On the other side, the EU Charter protects private life and personal data (Articles 7 and 8). More access for the state means less confidentiality, and the other way round. Every option gives something up, which is why we treat this as a dilemma.

**4 · History.** The same debate has come back several times:
- **1993:** the US government wanted the Clipper Chip, an encryption chip whose keys would be held by the state. Researchers found a flaw in 1994, and the plan was effectively abandoned by 1996.
- **2006:** the EU required telecom companies to store everyone's call data.
- **2013:** Edward Snowden revealed NSA mass surveillance.
- **2014:** the EU Court of Justice struck down the data retention directive as disproportionate.
- **2016:** Apple refused to help the FBI unlock the iPhone of the San Bernardino attacker.
- **2020:** police in France and the Netherlands hacked EncroChat, an encrypted phone network used by criminals.
- **2022:** the EU Commission proposed Chat Control 2.0.
- **2025:** a secret UK order led Apple to stop offering encrypted iCloud backups to new UK users.

**5 · Four ways the state can listen.** We sort surveillance along two questions: is it aimed at one suspect or at everyone, and does it collect the content or only the metadata (who, when, where)?
- **Targeted content:** classic wiretaps, state trojans and spyware. Germany issued 16,868 wiretap orders in 2024, and each needs a judge.
- **Targeted metadata:** the call records of one suspect.
- **Mass metadata:** data retention. The EU version was struck down in 2014, and Germany is currently debating storing IP addresses for three months; that bill has not passed yet.
- **Mass content:** bulk interception, as in the NSA programmes, and Chat Control 2.0. This is where the legal and ethical problems are largest.

**6 · Encryption moved the access point.** Before end-to-end encryption, the provider could read messages, so police could ask the provider. With end-to-end encryption the provider only sees scrambled data, and investigators call this "going dark". The state now has three options, all on the device itself: hack the phone, scan on the phone, or force companies to weaken encryption.

## Part 2 · Why privacy matters (pages 7–11)

**8 · "I've got nothing to hide".** This is the most common argument for surveillance. Daniel Solove (2007) and Bruce Schneier (2006) show three problems with it:
- Small, harmless facts combined reveal health, beliefs and relationships. Schneier cites Cardinal Richelieu: give me six lines written by the most honest man and I will find enough to hang him.
- Privacy is not secrecy. We put blinds on windows and a door on the bathroom without being criminals. Snowden: saying you have nothing to hide is like saying you do not care about free speech because you have nothing to say.
- Rules change, so data that is harmless today can be used differently by a future government or in another country.

If asked: Adam Moore (2011) adds that surveillance hits some groups harder, based on appearance, ethnicity, sexuality and religion. This links to Justice on slide 23.

**9 · Chilling effect.** Jon Penney (2016) measured monthly views of 48 Wikipedia articles on terrorism-related topics. After the Snowden revelations in June 2013, views dropped by about 20 percent and kept falling. People avoided reading legal information because they felt watched. Surveillance changes the behaviour of people who have done nothing wrong.

**10 · Access can be used by others.**
- **Athens Affair (2004–05):** unknown attackers used the legal wiretap function in Vodafone Greece's network to listen to about 100 phones, including the Prime Minister's.
- **Salt Typhoon (2024–25):** Chinese state hackers got into US telecom networks, including the systems for court-ordered wiretaps. In 2025, 13 countries reported more than 200 affected US organisations. In December 2024 the FBI and CISA advised Americans to use encrypted messengers.

The 2015 paper "Keys under doormats" by leading security researchers concludes that a way in that works only for authorities cannot be built.

**11 · Function creep.** Spyware is sold to fight terrorism and serious crime, but journalists, activists and politicians keep appearing among the targets:
- **Pegasus Project (2021):** a leaked list of about 50,000 phone numbers of possible targets.
- **Germany (2025):** the Federal Constitutional Court ruled that state trojans may not be used for minor offences.

## Part 3 · Why the state wants access (pages 12–14)

**13 · Encryption also hides crime.** To be fair to the other side. Most platforms report child abuse material to NCMEC, a US organisation, because Europe has no central body of its own. In 2023 NCMEC received 36.2 million reports, in 2024 20.5 million: 43 percent fewer. Two things explain the drop:
- **Bundling:** one viral video shared thousands of times now counts as one report. Counted as incidents, the 2024 figure is 29.2 million, so about 7 million fewer than in 2023.
- **Messenger's end-to-end encryption:** NCMEC calls this the most probable factor. Facebook reported about 6.9 million fewer reports after adjusting for bundling. This is NCMEC's own analysis, not an independent audit.

Google, X, Discord and Microsoft also reported at least 20 percent less, which NCMEC cannot explain by encryption. The REPORT Act (2024) was meant to increase reporting, because it added child trafficking and online enticement to the offences platforms must report. Yet reports fell. The system is also fragile: US law requires platforms to report what they find, not to look for it, so scanning is voluntary.

**14 · Targeted operations work.**
- **EncroChat:** police hacked the network, which led to 6,558 arrests in Europe and about 900 million euros seized.
- **ANOM:** the FBI secretly ran an encrypted app used by criminals, which led to more than 800 arrests in 16 countries.
- **Sky ECC:** in Germany alone, 585 arrest warrants followed.

These cases show that investigators can reach encrypted communication without scanning everyone. They are still controversial: courts, including the EU Court of Justice in 2024, have ruled on how such evidence may be used.

## Part 4 · Case study: Chat Control (pages 15–20)

**16 · Chat Control 1.0 and 2.0.** Chat Control started after the EU extended the ePrivacy Directive to messaging apps, which made the voluntary scanning that companies were already doing illegal.
- **1.0 (2021):** a temporary EU exception lets tech companies, such as Google, Meta and Microsoft, scan messages voluntarily. It expired in April 2026, which left several months without a legal basis, and was renewed in July 2026 until 2028, now excluding encrypted chats. Say the last part out loud, because it is not on the slide.
- **2.0 (2022):** a permanent law. Authorities could order a service to scan all its users' messages, including encrypted ones. A new EU Centre would handle reports in Europe instead of sending them to NCMEC in the US. Version 2.0 is only a proposal; it has not been adopted.

**17 · Client-side scanning.** To scan encrypted chats, the check has to happen on the user's own device, before the message is encrypted. That is why it is called client-side scanning. Known images are compared with a list of fingerprints (perceptual hashes), and new material is assessed by AI, which makes more errors. If something is flagged, a report goes to the EU Centre and then to the police. The encryption stays technically intact, but its promise that no third party sees your message is gone. That is why researchers treat client-side scanning like a backdoor (Abelson et al., 2024).

This has been tried. In 2021 Apple announced NeuralHash: photos were compared on the iPhone with a list of known abuse images before upload to iCloud. Apple cancelled the project in 2022 and later explained that it would create new attack paths for data thieves. The lesson is about the architecture, not only about hacking: private encryption and scanning on the device exclude each other. Note that NeuralHash scanned photos, not chats.

For your own knowledge: a perceptual hash is a fingerprint of how an image looks, not of its bytes, so resizing or compressing gives the same or a very similar hash, while a normal cryptographic hash changes completely. It can fail in both directions: different images can collide, and small deliberate edits can fool the detector.

**18 · Status.**
- **May 2022:** the Commission proposed mandatory scanning.
- **Nov 2023:** Parliament said only suspects, and only with a judge's order.
- **Nov 2025:** member states agreed on voluntary scanning instead of an obligation.
- **Sep 2026:** after six negotiation rounds there is still no deal on private chats.
- **Next round:** reported for December, but not officially confirmed.

Already agreed: risk assessment for platforms, removal and blocking orders, and the EU Centre. Still open: scanning of private chats, encrypted services, and age verification.

**19 · Who stands where.**
- **Commission:** started at "scan all chats".
- **Member states:** want voluntary scanning by companies.
- **Parliament:** wants only targeted orders against suspects.
- **Signal and about 500 researchers:** reject scanning of private chats; Signal said it would rather leave the EU.

**20 · False alarms.** Even if the technology worked, there is the problem of scale. A system that is 99.9 percent accurate, scanning a billion messages a day, still produces a million false alarms every day. The bar chart shows the share of reports to police that did not lead to a case. The measures differ slightly, so say so:
- **Ireland (2020):** 471 of the reports from NCMEC, more than 11 percent, were not abuse material (ICCL figure confirmed by the Gardaí, via RTÉ).
- **Germany (2023):** 89,336 of 180,287 reports were criminally relevant, so about half were not.
- **Norway (2023):** 4,500 of 13,211 tips were taken on; the rest were rejected, mostly because the act is not a crime in Norway or is below the police threshold.
- **Switzerland (2019):** fedpol said only about one tenth of the reports were criminally relevant. This is a single sentence quoted by Beobachter; the 90 percent is our calculation.
- **Czechia (2024, light bar):** 888 of 22,553 reports were passed on for investigation. This is a different measure: not passed on is not the same as false.

Sources: RTÉ and Irish Times (2022), netzpolitik.org (2024), Kripos (2024), Beobachter (2022), Czech Police.

## Part 5 · Weighing the dilemma (pages 21–25)

**22 · Framework.** We use the principlist framework for cybersecurity ethics by Formosa, Wilson and Richards (2021) from Lecture 2. The authors argue that applying the big ethical theories directly leads to conflicting results, because no theory has overwhelming authority. So they propose five mid-level principles for cybersecurity. Their definitions, in short:
- **Beneficence:** technology should benefit people, promote well-being and make our lives better overall.
- **Non-maleficence:** technology should not be used to intentionally harm people or to make our lives worse overall.
- **Autonomy:** people should be able to make informed decisions for themselves about how technology is used in their lives.
- **Justice:** technology should promote fairness, equality and impartiality, and should not unfairly discriminate, undermine solidarity or prevent equal access.
- **Explicability:** technology should be intelligible, transparent and comprehensible, and it should be clear who is accountable.

Important: these principles can conflict with one another and need to be balanced in a context-sensitive manner, which can result in a range of ethical trade-offs (Formosa et al., p. 1). The framework does not rank them. We apply them to one case: Chat Control 2.0, the proposal to order services to scan private chats, including encrypted ones.

Our own method, not from the paper: for each principle we list what speaks for and against Chat Control, and our verdicts (open, not met) are our own scale. The principles overlap, so the same fact can matter under more than one of them. We try to use it under the principle where it fits best.

**23 · Chat Control 2.0 through the five principles.** This is our group's assessment. Walk through the table row by row, first what speaks for the proposal, then what speaks against it:
- **Beneficence (open):** it could find abuse material and offenders in encrypted chats, where reports have fallen. But the benefit is unproven: more reports do not show that more children are protected. Targeted operations catch offenders in other crime areas (organised crime, not child abuse).
- **Non-maleficence (not met):** in favour: stopping the spread of abuse images could prevent further harm to victims. Against, documented: many false alarms, about half of German reports in 2023 were not criminally relevant. Careful: this figure comes from today's voluntary scanning, not from Chat Control 2.0. It shows how high the error rate is today, not how high it would be under Chat Control. Against, risk by analogy: a scanner on every phone is a new attack surface (analogies: Athens Affair, Salt Typhoon), and lists could be widened later (analogy: Pegasus). These are analogies for the misuse of surveillance functions, not proof for Chat Control. Hash matching produces fewer false alarms than AI classifiers (our assumption from the debate, not a source). Note on the definition: it says "intentionally", and the harm here is a side effect, not the aim, but the definition also says "make our lives worse overall".
- **Autonomy (not met):** victims have a real interest in privacy and dignity, because images of their abuse spread without their consent. But there is no real choice: every message is scanned on your own phone before end-to-end encryption can protect it, and refusing means not communicating. The encryption stays technically intact, but it is bypassed. Your device is normally the place where nobody reads along.
- **Justice (not met):** the question is whether benefits and burdens are distributed fairly. In favour: solidarity with victims, which the definition names explicitly, and the same rules apply formally to all users. Against: the benefit goes to a few, but the burden falls on all users, who are treated as suspects without cause.
- **Explicability (not met):** in favour: one central EU Centre receives all reports, so there is a defined point of accountability. Against: hash lists and AI cannot be checked and the lists are secret, so the purpose could be widened unnoticed. Responsibility is split between providers, EU Centre and police, so it is not clear who is accountable.

Result: the benefit is unclear, the false alarms are documented, and a milder means has not been ruled out for child abuse. It is a judgement, not a calculation.

Honest gap: our evidence for targeted measures (EncroChat, ANOM, Sky ECC) concerns organised crime, not child abuse. Be ready for that question. Also, the NCMEC reports come from platforms scanning unencrypted content, so the German figure does not say what scanning encrypted chats would find.

**24 · Check everyone, or only suspects?** The left grid shows mass scanning, where everyone is checked. The right grid shows the targeted model, where only a few suspects are checked with a court order. The European Parliament supports the targeted model, while most member states want wider options. The negotiations have not settled this yet.

**25 · Conclusion.**
1. The conflict is old; from the Clipper Chip to Chat Control, each new technology has raised the same question.
2. Encryption moved the conflict onto our own devices.
3. Measured with the five principles, Chat Control 2.0 fails on harm, freedom, fairness and transparency, and its benefit is unproven. Targeted measures are the alternative, and the examples show they still catch criminals.
4. Infrastructure built for surveillance stays available to future governments and to attackers.

Closing line (Schneier): the choice is not security versus privacy, but liberty versus control.

**26 · References.** **27 · Thank you.**
