Advanced prototype for Arc / ERC-8004 + ERC-8183 ecosystem.

## What it does
Agents start with low spending limits. Limits automatically rise with reputation score from completed jobs and feedback. Failed jobs temporarily lower caps.

## Files
- `simulate.py` — Full multi-agent Python simulation
- `dashboard.html` — Interactive browser dashboard
- `agent-prompt.md` — System prompt for AI agents
- `ReputationSpendingCap.sol` — Reference Solidity contract

## How to run
1. Python install karo (agar nahi hai)
2. Repo download karo (Code → Download ZIP)
3. Terminal mein folder open karke chalao:
   ```bash
   python simulate.py
