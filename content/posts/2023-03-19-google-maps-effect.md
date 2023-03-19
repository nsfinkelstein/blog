+++
title = "The Google maps effect: A reason to be cautious about using AI coding assistants"
+++

There are plenty of upsides to using Google maps. The first few times you go somewhere new, it's
easier to get there. You don't have to look up directions, you're not going to miss a turn. The
route you take may have less traffic on it. You might even get advance warning about a speed trap.

But there are downsides too. By handing over control of your route to the machine, you become a sort
of direction-following machine yourself. You don't have to look for landmarks along the way, or even
to register which streets you're driving on. As long as you _turn left at the light_ when told,
you'll get where you're going.

As a result, a common phenomenon is that people who are regular users of things like Google maps
never develop a familiarity with there physical landscapes. They don't understand the infrastructure
well enough to reason about how to adjust their trip if necessary, or about why their might be
traffic on certain roads at specific times. It's not uncommon for people to use Google maps on trips
they've taken dozens of times.

I think of this as the Google maps effect. We get enticed into handing off responsibility to a
machine by short term, substantial benefits. But as a result we become reliant on the machine. We
become strangers on our own roads. Worse still, we can lose access to a certain kind of spatial /
transportational reasoning capacity that was genuinely valuable, and genuinely rewarding to use. We
can lose the _sensation_ of where we are, in the context of where we've been and where we're going.

It's easy to imagine that using AI coding assistants will lead to a similar result, albeit in
developing software rather than in navigating the physical world. The most recent models are able to
load entire repositories as context for answering specific questions, or generating code for
specific tasks. A developer using these AI tools doesn't need nearly as strong of mental model for
how the code is structured. And because the AI tools can "write" code snippets, the developer
doesn't need nearly as strong of an understanding of the conceptual layout of the libraries they're
using either. Over time, I suspect developers using these tools will get more and more out of touch
with their own code bases, with the libraries they're using to develop, and eventually, with the
code they write themselves (with the help of the AI). As with Google maps, we'll lose an important
dimension to our reasoning.

There's a lot of excitement right now about what an AI code assistant can do. People ask it to
generate code for certain tasks, in non-trivial contexts, and it can provide answers that are either
correct or nearly correct. It looks like it can save it quite a lot of effort. We don't have to
learn all about some relevant libraries, we don't have to invest a lot of time into understanding
how all the pieces of the code we're dealing with fit together, and so on. But the side effect of
investing all that time is that we learn, and the things that we learn provide context for us to
create better and better solutions over time. What happens when all that time investment &mdash; and
all that learning &mdash; become optional?

I think the current wave of excitement is similar to what we saw when Google maps first came out,
and it became possible to take complex journeys without getting detailed directions or pouring over
maps. But it's important to think about the long-term. The tools we use change the work we do, and
over time, they change us too. We have to think carefully about just how they're changing us, and
make sure it's in a way we're comfortable with. Ideally, it'll be in a way that's not just improving
short-term efficiency, but improving us as well.

Even if we only care about productivity, and not about the effect on ourselves as reasoning
entities, it's not totally clear that AI code assistants as they currently stand will help with
long-term efficiency. A trip with Google maps is fleeting. Code isn't. My suspicion is that as we
produce more code that we don't understand well enough to have written ourselves, it will get harder
for us to reason about the code and add to it productively.

There are plenty of other reasons to be wary of AI assistants. They can produce plausible seeming
results that have subtle bugs, which means we _should_ regard all their output very critically.
Debugging is harder than writing code. If we're properly evaluating and testing the outputs of these
models for bugs, have we saved ourselves any time? And if we're not, what kinds of problems might we
be causing ourselves and the users of our code? And so on.

We may eventually get to a set of AI tools that make us more efficient, both short term and long
term, without hurting our own abilities. Proper coding assistants will take time, effort and thought
to develop. I suspect that using the current generation of models &mdash; trained on a different
task, without consideration of this use &mdash; will hurt our relationship to our work, in the same
way Google maps has shallowed our relationship to navigating and understanding our surroundings.
Until these tools get better, it's worth being cautious.
