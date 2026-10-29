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

**8 · "I've got nothing to hide".** This is the most common argument for surveillance. The legal scholar Daniel Solove (2007) shows three problems with it:
- Small, harmless facts combined reveal health, beliefs and relationships.
- Privacy is about who holds power over information, not only about hiding wrongdoing.
- Rules change, so data that is harmless today can be used differently by a future government or in another country.

**9 · Chilling effect.** Jon Penney (2016) measured monthly views of 48 Wikipedia articles on terrorism-related topics. After the Snowden revelations in June 2013, views dropped by about 20 percent and kept falling. People avoided reading legal information because they felt watched. Surveillance changes the behaviour of people who have done nothing wrong.

**10 · Access can be used by others.**
- **Athens Affair (2004–05):** unknown attackers used the legal wiretap function in Vodafone Greece's network to listen to about 100 phones, including the Prime Minister's.
- **Salt Typhoon (2024–25):** Chinese state hackers got into US telecom networks, including the systems for court-ordered wiretaps. In 2025, 13 countries reported more than 200 affected US organisations and targets in over 80 countries. In December 2024 the FBI and CISA advised Americans to use encrypted messengers.

The 2015 paper "Keys under doormats" by leading security researchers concludes that a way in that works only for authorities cannot be built.

**11 · Function creep.** Spyware is sold to fight terrorism and serious crime, but journalists, activists and politicians keep appearing among the targets:
- **Pegasus Project (2021):** a leaked list of about 50,000 phone numbers of possible targets.
- **Paragon (2025):** WhatsApp warned about 90 users, including journalists in Italy.
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

**22 · Framework.** We use the principlist framework by Formosa, Wilson and Richards (2021) from Lecture 2. Each principle becomes a question:
- Does it do good?
- Does it cause harm?
- Does it respect freedom?
- Is it fair?
- Is it transparent?

We apply the five questions to two approaches: scanning everyone, and targeted measures against suspects.

**23 · Mass vs. targeted.** This is our group's assessment.
- **Beneficence:** both approaches find offenders. Mass scanning probably finds more, so it is slightly ahead here.
- **Non-maleficence:** mass scanning weakens security for everyone and flags innocent people.
- **Autonomy:** mass scanning watches everyone and produces chilling effects.
- **Justice:** mass scanning treats every user as a suspect.
- **Explicability:** targeted measures do better, because a judge's order is required and documented.

**24 · Check everyone, or only suspects?** The left grid shows mass scanning, where everyone is checked. The right grid shows the targeted model, where only a few suspects are checked with a court order. The European Parliament supports the targeted model, while most member states want wider options. The negotiations have not settled this yet.

**25 · Conclusion.**
1. The conflict is old; from the Clipper Chip to Chat Control, each new technology has raised the same question.
2. Encryption moved the conflict onto our own devices.
3. Measured with the five principles, targeted measures do better than scanning everyone, and the examples show they still catch criminals.
4. Infrastructure built for surveillance stays available to future governments and to attackers.

**26 · References.** **27 · Thank you.**
