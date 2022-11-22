Questions I need to answer

Further directions:
 - We have more model ideas to try, foremost among them an extension of the sphere model that can expand non-uniformly, like an ellipse or along the chains of proteins. This will allow the model to capture groups that form more complex shapes than just being close together 
 - We would also expand to analyse more proteins, to see if the performance holds up in a larger set. We expect the given proteins to show the most use, since they are chosen 



What metrics am I using to measure performance
 - We judged model performance based on speed, visual legibility and how well it matched our existing understanding of biology.

 - The real test is whether it actually identifies critical sections of the protein, which is an active area of research. Confirming that for a protein typically requires months of research. In absence of that we have can only use heuristics.

 - If we were using an established machine learning technique, then a wealth of tests and heuristics are available. But in this project we designed a custom model to solve the problem directly, and don't have access to them. 



Did we use Gamma to test our models



 If we were using an established technique
 
 The real test is whether the highlighted regions actually correspond to critical regions of the protein, and how much a user can be confident in those results, and that is unfortunately outside of the scope of the project. 
 Since we're using a novel method, and the problem doesn't






misc text dump

to capture our intuition that a critical region’s purpose in the protein has to do with its physical structure. 

$$s(i, j) = \frac{(j-i)^{1.2}}{\text{var}(p[i..j])} \cdot \frac{\text{mean}(e[i..j])}{\text{mean}(o[i..j])}$$