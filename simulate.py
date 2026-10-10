from datetime import datetime

class Agent:
    def __init__(self, name, initial_score=0):
        self.name = name
        self.reputation = initial_score
        self.daily_spent = 0
        self.last_reset = datetime.now().date()
        self.update_caps()

    def update_caps(self):
        if self.reputation >= 800:
            self.tier, mult = "Elite", 8
        elif self.reputation >= 600:
            self.tier, mult = "Expert", 5
        elif self.reputation >= 300:
            self.tier, mult = "Trusted", 3
        else:
            self.tier, mult = "Newbie", 1
        self.max_single = round(2 * mult, 2)
        self.daily_budget = round(10 * mult * 2.5, 2)

    def reset_if_new_day(self):
        today = datetime.now().date()
        if self.last_reset != today:
            self.daily_spent = 0
            self.last_reset = today

    def try_spend(self, amount):
        self.reset_if_new_day()
        if amount > self.max_single:
            return False, f"Exceeds single cap (${self.max_single})"
        if self.daily_spent + amount > self.daily_budget:
            return False, f"Exceeds daily budget (${self.daily_budget})"
        self.daily_spent += amount
        return True, f"Spent ${amount} | Remaining: ${self.daily_budget - self.daily_spent:.2f}"

    def apply_job_result(self, success=True, points=50):
        if success:
            self.reputation = min(1000, self.reputation + points)
            result = f"+{points} score"
        else:
            penalty = int(self.reputation * 0.15)
            self.reputation = max(0, self.reputation - penalty)
            result = f"-{penalty} score (penalty)"
        self.update_caps()
        return result

# ========== Advanced Demo ==========
agents = [
    Agent("NewAgent", 50),
    Agent("GrowingAgent", 320),
    Agent("ProAgent", 750),
    Agent("EliteAgent", 920)
]

print("=== Current Status ===")
for a in agents:
    print(f"{a.name}: Score {a.reputation} | {a.tier} | Single ${a.max_single} | Daily ${a.daily_budget}")

print("\n=== Spending Tests ===")
tests = [
    ("NewAgent", 3),
    ("GrowingAgent", 8),
    ("ProAgent", 20),
    ("EliteAgent", 30)
]
for name, amt in tests:
    agent = next(a for a in agents if a.name == name)
    ok, msg = agent.try_spend(amt)
    print(f"{'✅' if ok else '❌'} {name} tried ${amt} → {msg}")

print("\n=== After Jobs ===")
print("NewAgent successful job:", agents[0].apply_job_result(True, 180))
print("ProAgent failed job:", agents[2].apply_job_result(False))
