# snake_ai
## Project overview
- I am laughably bad at snake so much so it is at the point where it would be easier for me to code the game from scratch and train and AI to do it better than to actually get better


## TODOLIST
### **2. Core Game Logic**
- [ ] Implement the basic Snake game using PyGame.
  - [ ] Create the game board and Snake entity.
  - [ ] Add food generation logic.
  - [ ] Handle Snake movement and collisions.
- [ ] Test the game for basic functionality.

---

### **3. Reinforcement Learning Environment**
- [ ] Create a custom environment for Snake (compatible with OpenAI Gym style).
  - [ ] Define the state representation (e.g., Snake's position, direction, food location).
  - [ ] Implement valid actions (e.g., move forward, turn left, turn right).
  - [ ] Set up the reward system:
    - [ ] +1 for eating food.
    - [ ] -1 for collisions.
    - [ ] 0 for standard moves.
  - [ ] Implement a `reset` and `step` method for the environment.

---

### **4. Q-Learning Implementation**
- [ ] Implement a basic Q-learning agent.
  - [ ] Create a Q-table to map states to actions.
  - [ ] Implement the exploration vs. exploitation strategy.
  - [ ] Update the Q-table using the Q-learning algorithm.
- [ ] Train the Q-learning agent on the Snake environment.
- [ ] Visualize the training progress (e.g., rewards over episodes).

---

### **5. Deep Q-Learning (DQN)**
- [ ] Implement a DQN agent using a neural network.
  - [ ] Design the neural network architecture for state-action predictions.
  - [ ] Use a replay buffer for storing experiences.
  - [ ] Implement target network updates for stability.
- [ ] Train the DQN agent on the Snake environment.
- [ ] Save the trained model.

---

### **6. Testing and Evaluation**
- [ ] Test the trained agents in the game.
- [ ] Compare the performance of Q-learning and DQN agents.
- [ ] Record and visualize metrics like average score and training time.

---

### **7. Final Touches**
- [ ] Add comments and clean up code.
- [ ] Write unit tests for critical components (e.g., environment, agents).
- [ ] Document usage instructions in the README.
- [ ] Add a demo (e.g., GIF or video of the Snake AI in action).

---

### **8. Optional Features**
- [ ] Add different difficulty levels.
- [ ] Implement multi-agent support (e.g., competing Snakes).
- [ ] Experiment with advanced RL algorithms (e.g., PPO, A3C).
- [ ] Add a leaderboard for high scores.
