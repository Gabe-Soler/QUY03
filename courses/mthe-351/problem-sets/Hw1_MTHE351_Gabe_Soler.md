MTHE 351
Homework 1
Gabe Soler - 20443392
Sep 21st, 2026

#### 1. 
- (a) sample space

Answer: S = M $\cup$ N

M = Sample space of events that are length 2
N = Sample space of events that are length 3 

M = {[1,4], [4,1], [2,3], [3,2], [4,2], [2,4], [4,3], [3,4]}
N = {[1,2,3], [1,3,2], [3,1,2], [2,1,3], [1,2,4], [2,1,4], [1,3,4], [3,1,4]}

thus, $$\begin{gathered} S = M + N \\ S = \{[1,4], [4,1], [2,3], [3,2], [4,2], [2,4], [4,3], \\ [3,4], [1,2,3], [1,3,2],   [3,1,2], [2,1,3], [1,2,4], [2,1,4], [1,3,4], [3,1,4]\}\\ |S| = 16 \end{gathered}$$

- (b) 

E = the event that "one of the balls drawn is 1"
F = the event that "the final sum of the balls drawn is even"

(i) "both E and F occur"
    this corresponds to: $$E \cap F$$
    *Answer:*
    $E \cap F$ = {[2,1,3], [3,1,2], [1,2,3], [1,3,2], [1,3,4], [3,1,4]}
    $|E \cap F |$ = 6


(ii) "Neither E nor F occur"
this corresponds to: $$(E \cup F)^c$$

*Answer:*
$(E \cup F)^c$ = {[3,2], [2,3], [3,4], [4,3]}
$|(E \cup F)^c|$ = 4

(iii) "Exactly one of the events occur"
this corresponds to: 
$$E \cup F - E \cap F$$
by an earlier result,

$$|E \cap F| = 6$$ 
$$|E \cup F|^c = 4$$ 
thus, 
$$|E \cup F| = 12$$
now we have that, 
$$|E \cup F - E \cap F| = 6$$
 And we get the *answer:*
$E \cup F - E \cap F = \{[1,4], [4,1], [4,2], [2,4], [1,2,4], [2,1,4]\}$

2. 

let E, F, G be three events

(a) "at least two of the three exist"

- this wording suggests that at least 2 events must occur, implying 3 can occur

let this event be $X_1$

$$X_1 = (E \cup F) + (F \cup G) + (E \cup G) +  (E \cup F \cup G)$$

(b) "at most two of the three events occur"

- this wording suggests that either 1 or 2 events occur

let this event be $X_2$

$$X_2 =( E + F + G) + (E \cup F - ((E \cup F) \cap G)$$