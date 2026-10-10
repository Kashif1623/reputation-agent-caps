// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ReputationSpendingCap {
    address public owner;
    enum Tier { Newbie, Trusted, Expert, Elite }

    struct AgentData {
        uint256 score;
        uint256 maxSingle;
        uint256 dailyBudget;
        uint256 dailySpent;
        uint256 lastDay;
        Tier tier;
    }

    mapping(address => AgentData) public agents;

    event ScoreUpdated(address indexed agent, uint256 score, Tier tier);
    event SpendChecked(address indexed agent, uint256 amount, bool allowed);

    constructor() { owner = msg.sender; }
    modifier onlyOwner() { require(msg.sender == owner); _; }

    function updateScore(address agent, uint256 newScore) external onlyOwner {
        require(newScore <= 1000);
        agents[agent].score = newScore;
        _recalc(agent);
        emit ScoreUpdated(agent, newScore, agents[agent].tier);
    }

    function trySpend(address agent, uint256 amount) external returns (bool) {
        _resetDaily(agent);
        AgentData storage a = agents[agent];
        bool ok = amount <= a.maxSingle && a.dailySpent + amount <= a.dailyBudget;
        if (ok) a.dailySpent += amount;
        emit SpendChecked(agent, amount, ok);
        return ok;
    }

    function _recalc(address agent) internal {
        AgentData storage a = agents[agent];
        if (a.score >= 800) { a.tier = Tier.Elite; a.maxSingle = 16e6; a.dailyBudget = 200e6; }
        else if (a.score >= 600) { a.tier = Tier.Expert; a.maxSingle = 10e6; a.dailyBudget = 125e6; }
        else if (a.score >= 300) { a.tier = Tier.Trusted; a.maxSingle = 6e6; a.dailyBudget = 75e6; }
        else { a.tier = Tier.Newbie; a.maxSingle = 2e6; a.dailyBudget = 25e6; }
    }

    function _resetDaily(address agent) internal {
        uint256 today = block.timestamp / 1 days;
        if (agents[agent].lastDay != today) {
            agents[agent].dailySpent = 0;
            agents[agent].lastDay = today;
        }
    }
}
