# Ether on a Stick

Max Fang and Philip Hayes. Recipient of $1000 prize at Treehacks Spring 2016

## What it does

Ether on a Stick is a platform that allows participants to contribute economic incentives for the completion of arbitrary tasks. More specifically, it allows participants to pool their money into a smart contract that will pay out to a specified target if and only if a threshold percentage of contributors to the pool, weighted by contribution amount, votes that the specified target has indeed carried out an action by a specified due date.

Example: A company pollutes a river, negatively affecting everyone nearby. Residents would like the river to be cleaned up, and are willing to pay for it, but only if the river is cleaned up. Solution: Residents use Ether on a Stick to pool their funds together that will pay out to the company if and only if a specified proportion of contributors to the pool vote that the company has indeed cleaned up the river.

## How we built it

Ether on a Stick implements with code a game theoretical mechanism called a Dominant Assurance Contract that coordinates the voluntary creation of public goods in the face of the free rider problem. It is a decentralized app (or "dapp") built on the Ethereum network, implementing a "smart contract" in Serpent, Ethereum's Python-like contract language. Its decentralized and trustless nature enables the creation of agreements without a 3rd party escrow who can be influenced or corrupted to determine the wrong user.

## Challenges

The first 20 hours of the hackathon were mostly spent setting up and learning how to use the Ethereum client and interact with the network. A significant portion was also spent planning the exact specifications of the contract and deciding what mechanisms would make the network most resistant to attack. Despite the lack of any kind of API reference, writing the contract itself was easier, but deploying it to Ethereum testnet was another challenge, as large swaths of the underlying technology hasn't been built yet.

## What's next for Ether on a Stick

We'd like to take a step much closer to a game-theoretically sound system (don't quote us, we haven't written a paper on it) by implementing a sort of token-based reputation system, similar to that of Augur. In this system, a small portion of pooled funds are set aside to be rewarded to reputation token bearing oracles that correctly vote on outcomes of events. "Correctly voting" means voting with the majority of the other randomly selected oracles for a given event. We would also have to restrict events to only those which are easily and publically verifiable; however, by decoupling voting from contribution, this bypasses a Sybil attack wherein malicious actors (or the contract-specified target of the funds) can use a large amount of financial capital to sway the vote in their favor.
