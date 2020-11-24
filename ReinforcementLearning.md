---
layout: default
title: Reinforcement Learning
permalink: /Reinforcement Learning/
---

# Reinforcement Learning

Reinforcement Learning is a type of Machine learning where the autonomous agent learns from trial and error by attempting to maximize cumulative rewards over time. In the RL paradigm, the agent learns to improve its performance at an assigned task by interacting with its environment. In this technique, state-action pairs can be recovered from interaction with the environment while modelling dynamics of the vehicle state, environment as well as the stochasticity in the movement and actions of the environment and agent respectively.

We tested our agent on a number of different reward functions, such as a coordinate based reward to ensure the car drives on the road, a polar coordinate reward to test the car's performance around a roundabout road and computer vision based rewards to prevent the car from crashing into obstacles.

For example, below is the path taken by the car during training of the DQN Roundabout objective, it shows the agent going further as the number of episodes increases.

<iframe width="700" height="400" src="https://drive.google.com/file/d/12NUFDWdM5Hf_AiRWUpoGHWNDT-jdlwix/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



Here is a video compilation of our agent's performance based on different rewards and environments.


<iframe width="700" height="400" src="https://drive.google.com/file/d/1tbRvZnJCk1rearyCT5bVf04Apvfsmj_9/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
