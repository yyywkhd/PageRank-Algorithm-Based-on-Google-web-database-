# Web-page-algorithm
### Introduction of the PageRank algorithm
<p>PageRank is a technique for ranking web pages based on the hyperlinks between them. It is used by Google to reflect the relevance and importance of a web page and is one of the most effective indicators for assessing the optimization of a web page in search Engine Optimization operations.</p>

### The algorithm is implemented in four main steps.
1. Basic PageRank Model

2. Termination Point Problem

3. The Trap Problem

4. Solving the Termination Point Problem and the Trap Problem

### For basic page rank model, we suppose there has four pages, which are A, B, C, D.

* A ->B, A->C, A->D

* B->A, B->D

* C->A

* D->A, D->B, D->C

<p>This example only contains 4 pages. web user have 1/3 possiblity link to B,C,D if they currently stay in page A. By analogy, we will get a transition matrix.</p>

#### The termination point problem
<p>The behavior of the above Internet user is an example of a Markov process, and to satisfy convergence, one condition is required: the graph is strongly connected, i.e., it is possible to reach any other web page from any web page.
At the same time, there are pages on the Internet that do not satisfy the strong connectivity property, because some pages do not point to any pages. If the above calculation is followed, the Internet user reaches such a page and is left in limbo, resulting in the cumulative transfer probability obtained earlier being zeroed out.</p>

#### Solving the Termination Point Problem and the Trap Problem
<p> In the above process, we have missed the point that the web surfer is a laid back web surfer, not a stupid web surfer. This address may of course be the original web page again, but here it gives him a chance to escape from this abyss. Simulating a clever and laid-back web surfer, the algorithm is improved so that at each step, the web surfer may not want to look at the current web page, and instead of looking at the current web page, he will not click on the above link, but instead quietly type another address into the address bar, and the probability of jumping to each web page by typing in the address bar is . Assuming that the probability that the Internet user views the current web page at each step is , then the probability that he jumps from the browser address bar is , so the original iterative formula is transformed into: </p>

$$ V'\, =\, αMV\, +\, (1-α)e $$




#### If this code is used for cheating and other breaches of academic integrity, you will be responsible for the consequences.
