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

**13 · Encryption also hides crime.** To be fair to the other side: reports of child sexual abuse material to NCMEC, the US hotline most platforms report to, fell by 43 percent from 2023 to 2024. A large part of the drop followed Facebook Messenger's switch to end-to-end encryption. Investigators say they cannot act on crimes they cannot see.

**14 · Targeted operations work.**
- **EncroChat:** police hacked the network, which led to 6,558 arrests in Europe and about 900 million euros seized.
- **ANOM:** the FBI secretly ran an encrypted app used by criminals, which led to more than 800 arrests in 16 countries.
- **Sky ECC:** in Germany alone, 585 arrest warrants followed.

These cases show that investigators can reach encrypted communication without scanning everyone. They are still controversial: courts, including the EU Court of Justice in 2024, have ruled on how such evidence may be used.

## Part 4 · Case study: Chat Control (pages 15–20)

**16 · Chat Control 1.0 and 2.0.**
- **1.0:** since 2021, a temporary EU exception has allowed companies like Meta and Google to scan messages voluntarily. It expired in April 2026 and was renewed in July 2026 until 2028; encrypted chats are now excluded.
- **2.0:** the permanent law proposed in 2022. Authorities could order a service to scan all users' messages, including encrypted ones, and a new EU Centre would forward reports to the police.

In our matrix, version 2.0 belongs in the field "mass surveillance of content".

**17 · How it works.** Messages are checked on the phone before encryption. Known images are compared with a list of digital fingerprints, and new images and chats are assessed by AI, which makes more errors. If something is flagged, a report goes to the EU Centre and then to the police. The encryption itself is not broken, but the content has already been read. That is why researchers treat client-side scanning like a backdoor.

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

**20 · False alarms.** In Germany about half of the roughly 180,000 reports in 2023 were not criminally relevant, often teenagers' own photos or memes. In Ireland, one in nine reports from 2020 was not abuse material, and the police kept the data anyway.

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
