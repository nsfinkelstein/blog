+++
title = "Generating curiosity: Intrinsic rewards in reinforcement learning"
draft = true
+++

In the reinforcement learning paradigm, an agent exists in an environment, and can take actions that
alter the environment's state. Every so often, the agent gets feedback about whether its actions
have made its situation better or worse, as evaluated by the so-called _reward function_.

In some cases, the reward function looks _only_ at the environment. For example, a reinforcement
learning approach to chess might give the agent a positive reward if it wins the game, or
incremental positive rewards if it makes good moves. Nothing about the reward depends on the agent's
internal state.

In other cases, the reward function looks only at the agent's state. A reinforcement learning
benchmark called [Avalon](https://generallyintelligent.com/avalon/) takes this approach. In this
case, the agent exists in an adversarial environment and has to survive by eating. In essence, the
agent gets a positive reward whenever it eats. The state of the environment itself is irrelevant.

It's sometimes argued that reinforcement learning is more reflective of how people learn than
supervised or unsupervised learning. [Generally Intelligent](https://generallyintelligent.com/), the
company behind Avalon, have a tagline that reflects this idea:

> "We want machines that learn the way humans do." &ndash; Generally Intelligent

People do learn through something like reinforcement learning, which we usually call trial and
error. We also learn through something like supervised learning, though there the analogy isn't as
good. Even in cases when we're being explicitly taught, we're usually taught with reference to
_general_ rules and principles, rather than only being fed examples. In other words, the
"supervision" for humans isn't just labels for the data, as it is for machines. It's _also_ a
conceptual framework for how to derive labels or perform an action. I don't think we have great
tools yet for using a similar approach with machines, but we'll need them if we want machines to
learn like people.

In this post, though, I'm more interested in the role of unsupervised learning in how people learn,
and in how that might be reflected in a reinforcement learning environment. There are important,
rewarding things people can do, that seem to alter neither the environment nor their internal state
in any obvious ways. There are things like meditating, going for a walk to think after a long day,
sitting outside and watching the trees sway in the wind. After we eat, there's an objective
physiological change, mimicked by the reward function in Avalon. But what happens after we think?

One way to think about unsupervised learning is as the process of searching for patterns in the
data. It's a process of synthesizing, interpreting, and assimilating information. In my view,
there's a strong analogy to be made between that process and the process of thinking, or of sleeping
for that matter. There's plenty of evidence that the more we pay attention to something &mdash; i.e.
the more thought we devote to it &mdash; the more firmly it will establish itself in our minds.
There's also evidence that good sleep is essential to the formation of long-term memories. And,
I'd argue, the process of turning things over in your mind until you find a better way to
understand them is both rewarding and an essential part of learning.

As agents move through their environments, they collect information. It's conceivable that there's
order in that information that they may not pick up on when they're purely trying to optimize for an
extrinsic &mdash; or in the case of Avalon, _objective_ intrinsic &mdash; reward.

What if part of the agent's reward was a more _subjective_ intrinsic reward? In particular, what if
the agent was rewarded for finding compelling and explanatory patterns in the data? Assuming that
computing resources are not an issue, artificial agents wouldn't need to take time out to think, as
we do. They can multi-task. So they can do unsupervised learning on data as a background process,
and potentially use the results to help decide on actions.

Rewarding the agent for the quality of the patterns it finds its environment will, hopefully, induce
it to find more compelling patterns. But there's a more interesting effect of this kind of intrinsic
reward as well. Suppose the agent has developed an unsupervised representation of its environment
that aligns well with _most_ of the data. But there's a small set of data that, according to
whatever metric, is not well-represented. That small set of data will drive down the reward for the
quality of the agent's unsupervised learning. The agent will have an incentive to explore its
environment and action spaces in such a way that it acquires the kind of information that lets it
make sense of the troubling data.

To me, this looks and functions a lot like curiosity in people. We get curious when we come across
something that doesn't fit our mental model of the world, or that's simply so far outside of our
realm of experience that we don't really know what to make of it. That curiosity drives us to try
new things and see what happens, or to learn more about what's around us.

There will undoubtedly be technical challenges to integrate this kind of unsupervised learning
approach to the reinforcement learning paradigm, but I think it'll be worth trying. Curiosity is
arguably the main driver of human learning; if the goal is to have machines that learn like we do,
we'll need some way to make them curious.

Of course, the process of learning &mdash; the process of satisfying curiosity &mdash; is rewarding
in its own right as well. That might be a topic for another time.

[Addendum](@/posts/2023-03-20-predictive-and-anomalous-curiosity.md)
