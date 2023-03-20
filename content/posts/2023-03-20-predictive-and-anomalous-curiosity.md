+++
title = "Types of curiosity: predictive and anomalous"
+++

A couple days ago I wrote about an idea for [curiosity in reinforcement
learning](@/posts/2023-03-18-intrinsic-reinforcement-learning.md). Since then I was reminded that
there's already a class of methods in reinforcement learning that go by the same name, summarized in
[this paper](https://arxiv.org/pdf/1808.04355.pdf).

These methods use a different idea to generate "curiosity." They allow an agent to make predictions
about the effects of its actions. The more incorrect the agent is about its predictions, the more
it's penalized. It has an incentive to learn more about the kinds of situations that leave it least
about to predict the future.

The kind of curiosity I was writing about is different. The idea there would be to simulate the
agent's "mental model" of the world by using a model trained by an unsupervised approach. The agent
might contain, in part, an auto-encoder element that encodes the full state of the environment or
distinct objects in the environment. When the agent comes across input that the auto-encoder encodes
poorly, it gets a poor reward, indicating that input is _anomalous_ in what the agent has seen so
far.

I think human curiosity involves elements of both of these paradigms (and probably many others).
It's true that we're constantly making predictions about what we think will happen as a result of
our actions, and that when those predictions are wrong, that's an opportunity for learning. We can
get curious about why we were wrong, and try to figure out how to be less wrong in the future.

But curiosity doesn't require this kind of prediction. When we encounter something that's totally
new to us &mdash; something we don't quite know how to make sense of &mdash; we can get curious
about it, even without making predictions. This kind of curiosity is better simulated by an
unsupervised loss, which is evaluated on how well its "mental model" accords with reality. Just as
we're driven to find out more about _anomalies_ in our lives, the agent would be driven to refine
its "mental model" to account for the input that strikes it as strange. I think of this as a more
_reflective_ kind of curiosity. As we try to synthesize and assimilate information about the world,
we notice and wonder about pieces that don't quite fit.

What would happen if we created an agent with both predictive and anomalous curiosity? I wonder.
