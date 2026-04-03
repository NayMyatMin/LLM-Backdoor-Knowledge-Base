# Neurotoxin: Durable Backdoors in Federated Learning

## Authors
Zhengming Zhang, Ashwinee Panda, Linyue Song, Yaoqing Yang, Michael W. Mahoney, Joseph E. Gonzalez, Kannan Ramchandran, Prateek Mittal

## Venue
ICML 2022

## Year
2022

## URL
https://arxiv.org/abs/2206.10341

## Abstract Summary
Neurotoxin addresses a key limitation of backdoor attacks in federated learning: the backdoor tends to be forgotten quickly after the attacker stops participating in training. The paper proposes a method to make backdoors more durable by injecting the backdoor into parameters that are unlikely to be updated by subsequent honest participants. Specifically, Neurotoxin targets parameters with the smallest gradient magnitudes during clean training, ensuring the backdoor resides in "rarely-used" parameters that honest updates do not overwrite.

## Key Contributions

1. **Durable backdoor design for FL**: Identified and exploited the insight that backdoor durability depends on which parameters encode the backdoor, proposing to target low-gradient parameters that are rarely updated during clean training.

2. **Gradient-based parameter selection**: Developed a method to identify parameters whose gradients are consistently small across honest participants' clean data, indicating these parameters are "safe" for backdoor injection.

3. **Persistence analysis**: Provided both theoretical and empirical analysis of why backdoors in low-gradient parameters persist longer than those in frequently-updated parameters.

4. **Improved attack under defenses**: Showed that the durable backdoor design also improves attack success against FL defenses like norm clipping and robust aggregation.

## Method Details
Neurotoxin modifies the standard FL backdoor attack to improve persistence:

**Parameter Selection**:
1. The attacker first estimates which model parameters have the smallest gradients during clean training. This can be done by:
   - Training on the attacker's own clean data and measuring average gradient magnitudes.
   - Observing gradient information from the global model updates across rounds (if accessible).
2. Parameters are ranked by their average gradient magnitude, and the bottom-k% are selected as "durable" parameters.

**Targeted Backdoor Injection**:
1. The attacker trains the backdoor using standard poisoning on their local data.
2. A projection step restricts the backdoor-related weight changes to primarily affect the selected low-gradient parameters.
3. Formally: delta_backdoor is projected onto the subspace spanned by the low-gradient parameters: delta_projected = P_low * delta_backdoor, where P_low is the projection matrix for the selected parameter indices.

**Attack Integration**: The projected update is then submitted to the FL server using the standard model replacement technique (scaled to counteract aggregation dilution).

**Why It Works**: In subsequent rounds of honest training, the gradient updates from honest participants primarily affect high-gradient parameters (those important for the clean task). The backdoor, residing in low-gradient parameters, receives minimal updates and thus persists for many more rounds than a standard backdoor.

**Coordinate-wise Analysis**: The paper provides a coordinate-wise analysis of gradient magnitudes, showing that the clean task and backdoor task can be decomposed into largely disjoint parameter subsets, enabling this targeted injection.

## Key Results
- Backdoor persistence increases from ~10 rounds (standard attack) to 100+ rounds after the attacker stops participating.
- Attack success rate remains above 80% for 5-10x longer than baseline FL backdoor attacks.
- Effective against norm clipping defense: the projected updates have smaller norms in the frequently-inspected directions.
- Works across multiple FL settings: cross-silo (10-100 clients) and cross-device (1000+ clients) scenarios.
- Tested on CIFAR-10, EMNIST, and Reddit next-word prediction tasks.
- The parameter selection strategy is transferable: parameters identified on one round's data remain low-gradient in subsequent rounds.
- Minimal impact on clean accuracy (< 0.5% degradation compared to no-attack baseline).
