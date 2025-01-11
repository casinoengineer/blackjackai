# Blackjack AI

This is a simple Python project where an AI plays the classic card game **Blackjack** against a dealer. The AI uses a basic strategy to decide whether to "hit" or "stand" based on its current hand and the dealer's visible card.

## Features
- Simulated deck of cards with proper shuffling.
- AI decision-making based on basic Blackjack strategy.
- Handles busts, ties, and wins for both the player and the dealer.
- Simplified rules for easy understanding and gameplay.

## How to Run
1. **Install Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Clone or Download the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

3. **Run the Game**:
   Execute the Python script in your terminal:
   ```bash
   python blackjack_ai.py
   ```

4. **Enjoy the Game**:
   Follow the prompts in the terminal to see how the AI plays Blackjack against the dealer.

## Rules of the Game
- The goal is to get as close to 21 as possible without exceeding it.
- The AI plays first, deciding to "hit" (take another card) or "stand" (keep its current hand).
- The dealer must draw cards until their score is at least 17.
- The winner is determined by comparing the scores:
  - If the AI's score exceeds 21, it busts, and the dealer wins.
  - If the dealer's score exceeds 21, the AI wins.
  - If both scores are equal, it's a tie.

## Example Gameplay
```text
Your hand: ['A', '7'], Score: 18
Dealer's visible card: 9
AI stands with: ['A', '7'], Score: 18
Dealer's hand: ['9', '7', '5'], Score: 21
Dealer wins!
```

## Customization
Feel free to modify the following features:
- **AI Strategy**: Enhance the AI's decision-making logic.
- **Game Rules**: Add features like splitting, doubling down, or betting.
- **Multiplayer Support**: Allow multiple AI or human players.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Suggestions and improvements are always welcome!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Inspired by the classic card game Blackjack.
- Developed for educational purposes to demonstrate basic AI decision-making in Python.

---

Happy coding and enjoy playing Blackjack with AI!
