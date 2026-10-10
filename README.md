# Reputation-Scaled Spending Caps for Agents

Advanced prototype for the Arc / ERC-8004 + ERC-8183 ecosystem.

## What it does
Agents start with low spending limits. Limits automatically increase based on reputation score from completed jobs and feedback. Failed or disputed jobs temporarily lower the caps.

## Files
- `simulate.py` — Full multi-agent Python simulation
- `dashboard.html` — Interactive browser dashboard
- `agent-prompt.md` — System prompt for AI agents
- `ReputationSpendingCap.sol` — Reference Solidity contract

## How to run
1. Install Python (if not already installed)
2. Download the repository (Code → Download ZIP)
3. Open a terminal in the folder and run:
   ```bash
   python simulate.py
