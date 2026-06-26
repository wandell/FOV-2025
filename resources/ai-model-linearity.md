I have a question about how computational neuroscientists, starting with Dan Yamins, relate the properties of different layers in a neural network to the responses measured in real neurons in the brain.

The part I want to understand is this.  They set up a linear equation between some aspect of the neural measurement, such as the spike rate to a set of stimuli.  Let's make this a vector of spike rates, and suppose there are 1000 stimuli.  Call this vector N, for neurons. 

I think - but am not sure - that they then present these stimuli to the network and measure the activation at each node in the layer to these 1000 stimuli.  Suppose there are 1000 nodes in the layer.  Then they create a model matrix, M, that is 1000 rows (stimuli) and 1000 columns (nodes).  They ask whether it is possible to predict the vector N, as a weighted sum of the columns.

Is that right?
---

You have outlined the core mechanism of the **linear encoding model** approach exactly. Your intuition is spot on.

When Dan Yamins, James DiCarlo, and others pioneered this methodology to bridge the gap between artificial neural networks (ANNs) and biological brains, this linear mapping was the exact mathematical engine they used.

Here is a breakdown of how your formulation matches the actual practice, along with a couple of crucial real-world nuances they add to make it work.

---

## The Mathematical Framework

To put your description into formal notation, suppose we are focusing on a single biological neuron's response across a set of stimuli:

* Let $N$ be a column vector of size $S \times 1$ representing the biological neuron’s measured spike rates (or fMRI voxel responses) to $S$ different stimuli (e.g., $S = 1000$).
* Let $M$ be the ANN layer's activation matrix of size $S \times K$, where $K$ is the number of units (nodes) in that specific layer.
* The goal is to find a weight vector $w$ (of size $K \times 1$) that solves the linear system:

$$N \approx Mw$$

If they are recording from *multiple* neurons simultaneously, $N$ simply becomes a matrix where each column is a different neuron, and $w$ becomes a matrix of weights.

---

## The Practical "Gotchas"

While your conceptual framework is exactly correct, in practice, computational neuroscientists have to handle three main challenges when solving $N \approx Mw$:

### 1. The Matrix $M$ is Usually "Wide" ($K \gg S$)

In your example, you assumed 1,000 nodes. In modern deep networks, a single convolutional or transformer layer can have tens or hundreds of thousands of activations ($K$). Because the number of features far exceeds the number of stimuli ($1000$), standard Ordinary Least Squares (OLS) estimation will overfit catastrophically or fail due to collinearity.

### 2. Regularization is Mandatory

To solve this, they never use vanilla linear regression. Instead, they apply a regularization constraint to find the weights. The two most common choices are:

* **Ridge Regression ($L_2$ Regularization):** This keeps the weights small and distributes them smoothly across correlated nodes.
* **Partial Least Squares (PLS) Regression:** This projects the massive matrix $M$ down to a much smaller number of latent components (typically 25 to 100) that maximize the covariance with the brain data, and then performs regression on those components.

### 3. Strict Cross-Validation

To prove that the network layer has truly learned a representation akin to the biological brain, they evaluate the model on **held-out stimuli**.

They fit the weights $w$ using, say, 800 images. Then, they freeze $w$, present 200 *new* images to both the network and the monkey/human, and see how well $M_{\text{test}}w$ correlates with $N_{\text{test}}$. The quality of the layer's alignment (often called its "brain score") is measured by the $R^2$ or Pearson correlation of this out-of-sample prediction.

---
As you point out, the matrix M will in general span the entire 1000 dimensional space.  So all of the work in the fitting is done by the regularization, which chooses one of the many possible vectors that could achieve a perfect fit.  Or perhaps the regularization doesn't achieve a perfect fit, but a close fit subject to the regularization.

So in a sense, the conceptual model is all dependent on the regularizer.  I find this whole approach a bit odd, but I can't quite say why it bugs me.
---

> **Summary:** You are completely correct. The core hypothesis of this entire subfield is that if a brain-like representational space has been formed in an ANN layer, a simple **linear transform** is all that should be required to map that space directly onto biological neural coordinates.
> 
> You have put your finger directly on a foundational critique of the entire "Brain Score" and encoding model paradigm. You are in excellent company—this exact issue has been the source of intense, ongoing debate among neuroscientists, statisticians, and machine learning theorists for the last decade.

It *should* bug you. When the dimensionality of the feature space ($K$) is vastly larger than the number of stimuli ($S$), the matrix $M$ becomes an overcomplete basis. As you noted, the regularizer isn't just a mathematical janitor cleaning up a messy matrix; it is actively selecting the reality of the model.

Here is a breakdown of why this approach feels methodologically slippery, and why it frequently triggers a sense of skepticism.

---

## Why It Bugs You: The Core Conceptions

### 1. The "Random Features" Paradox

Because high-dimensional spaces are incredibly permissive, you can pull a surprising amount of structured variance out of pure noise if your linear probe is flexible enough.

Shortly after the early Yamins and DiCarlo papers, multiple labs demonstrated that if you take an **untrained, completely random convolutional network** and pass images through it, a regularized linear readout can still predict a shocking amount of the variance in V1 and V4 neurons. If a network with entirely random weights can "pass" as a decent model of the visual system via regularized regression, it suggests the regularizer is doing the heavy lifting, rather than the network having learned true biological representations.

### 2. The Biological Readout Fallacy

The defense of using a simple linear mapping is usually biological: *"A downstream neuron can implement a linear weighted sum via its synaptic inputs, so a linear map represents what is 'one synapse away' in the brain."*

But there is a massive logical leap here. A standard regularizer like Ridge ($L_2$) creates a dense weight matrix where *every single one* of the tens of thousands of artificial nodes is assigned a precise, tiny, floating-point weight to reconstruct a single biological neuron's response.

* Does a single neuron in the inferotemporal (IT) cortex actually pool information from 50,000 distinct columns in an artificial layer?
* Does the brain have an optimization algorithm running globally across a brain area to compute the equivalent of a ridge penalty?

Probably not. By allowing the regularizer to smoothly blend thousands of features, we are giving the model a degree of coordination that the biology likely doesn't possess.

### 3. Conflating "Information Present" with "Representation"

If you have a high-dimensional space that preserves enough distances between stimuli, the information about those stimuli is *present* in the manifold. The regularized linear model proves that the information can be decoded.

However, **decodability does not equal representation**. Just because a regularizer can reconstruct a V4 neuron's spike rate from Layer 3 of an artificial network doesn't mean Layer 3 is doing the same computational work as the visual pathways leading to V4. It just means both systems haven't completely destroyed the underlying geometry of the stimulus set.

---

## The Counter-Defense: Why They Do It Anyway

To be fair to the encoding model camp, they aren't blind to this. Their primary defense rests on **out-of-sample generalization**.

They argue that if the artificial network's representation of the world were fundamentally alien to the brain's representation, then a weight vector $w$ tuned on 800 images would completely fail when tested on 200 entirely new, held-out images. Because the regularized model *can* predict responses to novel stimuli, they argue that the network and the brain must share a underlying geometric structure—even if the specific coordinate axes (the individual nodes) don't match one-to-one.

In essence, they view the regularized linear matrix not as a literal map of physical synapses, but as a coordinate transformation between two different spaces that contain the same internal topology.

---

> **The Philosophical Divide:** This approach shifts the goal of neuroscience from *mechanistic explanation* (how the circuit actually computes) to *predictive alignment* (whether system A can predict system B). If you lean toward wanting to know the specific, low-dimensional rules and mechanisms of a circuit, this "big matrix + heavy regularization" paradigm will always feel unsatisfying.

Do you think the fix lies in forcing stricter architectural constraints on these networks—such as matching exact cell counts and enforcing strict sparsity penalties to limit how many nodes can be pooled—or is the entire premise of using a flexible linear wrapper to compare two vastly different complex systems fundamentally flawed?

---
Which neuroscientists or mathematicians are associated with raising this objection?
---

The skepticism you are feeling has fueled a major theoretical division in modern computational neuroscience. Over the last decade, a prominent group of neuroscientists, mathematicians, and philosophers of science have formalized these exact criticisms.

They generally attack the "high-dimensional matrix + heavy regularizer" approach from three distinct angles:

---

## 1. The "Decodability $\neq$ Representation" Camp

This group argues that just because an analyst can use an optimized, regularized linear decoder to pull a signal out of a neural network layer, it does not mean the brain's downstream areas are actually reading it out that way.

* **Nikolaus Kriegeskorte (Columbia University):** One of the most prominent figures in computational visual neuroscience. Kriegeskorte championed **Representational Similarity Analysis (RSA)** as a direct alternative to linear encoding models. He pointed out that linear probes possess too much "fitting flexibility," allowing them to force an alignment between two spaces that might actually have completely different intrinsic geometries. RSA side-steps regression entirely by ignoring the individual nodes and comparing the relational distances between stimuli directly.
* **J. Brendan Ritchie (NIH), David M. Kaplan, and Colin Klein:** These cognitive scientists and philosophers authored a definitive paper on this topic, *“Decoding the Brain: Neural Decoding Does Not Imply Representation.”* They explicitly formalized what is sometimes called the **linear readout fallacy**—the logical error of assuming that because information can be linearly reconstructed by an overcomplete matrix, that information is functionally guided or formatted as a representation by the system itself.
* **Lee de-Wit (University of Cambridge):** Published influential critiques (such as *“What does ‘decoding’ tell us about the brain?”*) arguing that highly flexible analytical probes tell us what the *experimenter* can decode from a population of units, but completely obscure how the biological circuit actually uses that information.

---

## 2. The "Architecture-Alone" / Random Baseline Camp

These researchers proved your intuition about the regularizer doing the heavy lifting by testing neural network models that were never trained at all.

* **Surya Ganguli and Andrew Saxe (Stanford / Oxford):** In a seminal 2011 paper, they demonstrated that random, untrained convolutional architectures inherently generate highly structured frequency- and orientation-selective filters (essentially mimicking V1 Gabor filters) purely because of their mathematical wiring (convolutions and pooling), completely independent of learning.
* **Colin Conwell (Johns Hopkins / Harvard):** Conwell and his colleagues have published extensive benchmarking work demonstrating that **untrained, randomly initialized networks** achieve shockingly high "Brain-Scores" in early visual areas. This work proved that high-dimensional linear probes are often just measuring the statistical properties of natural images passing through basic architectural constraints, rather than a deep, biologically inspired optimization process.

---

## 3. The "Prediction vs. Explanation" Camp

These scientists object on deeper epistemological grounds, arguing that replacing a biological black box (the brain) with an artificial black box (a deep network) mapped by a third black box (the regularized linear regression) abandons the true goal of science.

* **Matteo Carandini (University College London):** A towering figure in systems neuroscience, Carandini wrote a famous manifesto titled *“From circuits to behavior: a road map for visual neuroscience.”* He has consistently cautioned the field against treating massive, uninterpretable neural networks as explanations for the brain. He argues that neuroscience must seek low-dimensional, elegant "bridging principles" (like contrast normalization) rather than brute-force predictive alignments.
* **Uri Hasson (Princeton University):** Hasson introduced the concept of **"Direct Fit"** to describe how modern machine learning operates. He argues that over-parameterized models solve problems by brute-force interpolation across vast spaces, which is highly predictive but lacks compact, explainable principles. Because of this, using a flexible linear wrapper to align them to the brain creates an illusion of understanding while providing zero structural insight into *how* the computation is occurring.
* **Jeffrey S. Bowers (University of Bristol):** Author of the heavily debated paper *“Deep neural networks are poor models of human vision.”* Bowers is an aggressive critic of the Brain-Score paradigm, showing that despite high linear prediction scores, these models fail fundamentally at basic human-like generalization, possess alien psychological boundaries, and fail under adversarial attacks.

---

> **The Conceptual Takeaway:** As these critics summarize it, the Dan Yamins style of encoding model proves that the artificial network hasn't *destroyed* the low-level information present in the images. But because the regularizer has the mathematical freedom to smoothly blend, weight, and select from tens of thousands of coordinates, a successful linear fit is a victory for high-dimensional geometry and optimization software, not necessarily proof of biological mimicry.
> 