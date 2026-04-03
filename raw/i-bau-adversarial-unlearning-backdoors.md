# Adversarial Unlearning of Backdoors via Implicit Hypergradient (I-BAU)

## Authors
Yi Zeng, Si Chen, Won Park, Z. Morley Mao, Ming Jin, Ruoxi Jia

## Venue
ICLR 2022

## Year
2022

## URL
https://arxiv.org/abs/2110.03735

## Abstract Summary
I-BAU (Implicit Backdoor Adversarial Unlearning) proposes a minimax optimization framework for removing backdoors from trained models. The method jointly optimizes a trigger estimator and model parameters: the inner maximization finds the worst-case trigger that the model is sensitive to, while the outer minimization makes the model invariant to this estimated trigger. The key innovation is using implicit hypergradient computation to efficiently solve this bilevel optimization, avoiding the computational cost of unrolling the inner optimization.

## Key Contributions

1. **Minimax formulation for backdoor unlearning**: Formulated backdoor removal as a bilevel optimization problem where the inner loop discovers the worst-case trigger and the outer loop unlearns it.

2. **Implicit hypergradient computation**: Proposed using implicit differentiation to compute the gradient of the outer objective with respect to model parameters, avoiding expensive inner-loop unrolling and making the optimization tractable.

3. **Universal trigger estimation**: The inner optimization finds a universal perturbation (proxy trigger) that maximally activates the backdoor behavior, providing a better approximation of the actual trigger than heuristic methods.

4. **Efficient and effective defense**: Achieved state-of-the-art backdoor removal with minimal computational overhead and requiring only a small clean dataset.

## Method Details
I-BAU formulates the defense as a bilevel optimization:

**Bilevel Formulation**:
- **Outer problem** (model unlearning): min_theta L_clean(theta) + lambda * L_unlearn(theta, delta*(theta))
- **Inner problem** (trigger estimation): delta*(theta) = argmax_delta L_attack(theta, delta)

Where:
- theta are model parameters
- delta is the estimated trigger perturbation
- L_clean ensures clean accuracy is maintained
- L_unlearn makes the model invariant to the estimated trigger
- L_attack measures how much the trigger changes model outputs

**Implicit Hypergradient**: Rather than unrolling the inner optimization (which requires storing and backpropagating through many optimization steps), I-BAU uses the implicit function theorem:
1. At the optimal inner solution delta*, the gradient of L_attack with respect to delta is zero.
2. By implicit differentiation, the gradient of the outer objective with respect to theta can be computed using only the Hessian of L_attack at the optimal point.
3. The Hessian-vector product is approximated efficiently using finite differences.

**Algorithm**:
1. Initialize with the backdoored model parameters theta.
2. For each iteration:
   a. Solve the inner problem: find delta* that maximizes attack success (using PGD for a few steps).
   b. Compute the implicit hypergradient of the outer objective.
   c. Update theta to minimize the outer loss (reducing sensitivity to the estimated trigger while maintaining clean accuracy).
3. Repeat until convergence.

**Unlearning Loss**: L_unlearn = KL(f(x + delta*; theta) || f(x; theta)), which encourages the model to produce the same output regardless of whether the trigger is present.

## Key Results
- Reduces attack success rate to below 2% across 8 different attacks on CIFAR-10 and GTSRB, outperforming Neural Cleanse, Fine-Pruning, and NAD.
- Clean accuracy degradation is less than 1%.
- The implicit hypergradient computation reduces the computational cost by 5-10x compared to unrolled bilevel optimization.
- The estimated trigger pattern closely resembles the actual trigger, demonstrating the inner optimization's effectiveness.
- Convergence is achieved within 10-20 outer iterations, taking only a few minutes on standard hardware.
- Requires only 5% of training data as the clean set.
- Robust to different trigger sizes, types, and poisoning rates.
