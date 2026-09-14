---
course: cmpe-365
type: reference
date: 2026-09-13
tags: [algorithms, asymptotics, recurrences, dynamic-programming, graph-algorithms, np-completeness]
source: clrs-4e.pdf
part: "Introduction"
---

# Introduction

> **Math fidelity.** This PDF sets its symbols in Type3 subset fonts whose private-use codepoints are assigned per subset, so the same code means different things in different chapters and cannot be decoded from the font alone. Letters, digits, brackets, fractions, superscripts and the named operators were repaired and are reliable. Every symbol that could not be identified is shown as `{?}` rather than guessed at - look it up in `clrs-4e.pdf` at the page given above. Unresolved here: `1` x11412, `{?}` x612, `˚` x124, `"` x73, `(` x47, `#` x22.

*Source pages 1161-1161 of `clrs-4e.pdf`.*

Introduction When you analyze algorithms, you often need to draw upon a body of mathematical tools. Some of these tools are as simple as high-school algebra, but others may be new to you. In Part I, we saw how to manipulate asy mptotic notations and solve recurrences. This appendix comprises a compendium of several other concepts and methods used in analyzing algorithms. As noted in t he introduction to Part I, you may have seen much of the material in this appendix before having read this book, although some of the specific notational conventions appearing here might differ from those you have seen elsewhere. Hence, you shou ld treat this appendix as reference material. As in the rest of this book, however, we have included exercises and problems, in order for you to improve your skills in these areas. Appendix A offers methods for evaluating and boundi ng summations, which occur frequently in the analysis of algorithms. Man y of the formulas here appear in any calculus text, but you will find it convenient to have these methods compiled in one place. Appendix B contains basic definitions and notations for sets, relations, functions, graphs, and trees. It also gives some basic properties of these mathematical objects. Appendix C begins with elementary principles of counting: permutations, com- binations, and the like. The remainder contains definitions and properties of basic probability. Most of the algorithms in this book re quire no probability for their analysis, and thus you can easily omit the latter s ections of the chapter on a first reading, even without skimming them. Later, when yo u encounter a probabilistic analysis that you want to understand better, you will find Appendix C well orga- nized for reference purposes. Appendix D defines matrices, their operations, and some of their basic prop- erties. You have probably seen most of this materia l already if you have taken a course in linear algebra. But you might find it helpful to have one place to look for notations and definitions.
