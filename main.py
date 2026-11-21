"""Urban Retail Analytics System - Python Module End Assessment 1."""

# ============================================================
# Section 1: Basic Syntax
# ============================================================
print("=== Section 1.1: Order Tax Calculator ===")
base_price = float(input("Enter item base price: "))
# Add the standard 10% sales tax to the base price to get the total price
total_price = base_price * 1.10
print(f"Final price with tax: ${total_price:.2f}.")

print("\n=== Section 1.2: Order Size Classifier ===")
quantity = int(input("Enter order quantity: "))
if quantity >= 10:
    print("Bulk Wholesale Order")
elif 3 <= quantity <= 9:
    print("Standard Customer Order")
else:
    print("Single Item Purchase")

# ============================================================
# Section 2: Iteration, Logic & Reusable Functions
# ============================================================
print("\n=== Section 2.1: Daily Sales Auditor ===")
transactions = [45.0, 0.0, 120.5, -10.0, 300.0, 85.0]
for amount in transactions:
    if amount <= 0:
        continue  # skip non-positive amounts
    if amount > 250.0:
        print(f"Order of ${amount} exceeds $250.0 - high-value security review required. Stopping.")
        break
    print(f"Valid transaction: ${amount}")

print("\n=== Section 2.2: Discount & Reward Functions ===")


def calculate_discount(bill_amount, vip_member=False):
    if vip_member:
        return bill_amount * 0.85  # 15% VIP discount
    return bill_amount * 0.95      # 5% standard discount


points_earned = lambda amount: amount // 10


def tier_bonus(level):
    if level == 1:
        return 50
    return 50 + tier_bonus(level - 1)


print("Discount (100, VIP):", calculate_discount(100, vip_member=True))
print("Discount (100, regular):", calculate_discount(100))
print("Points earned for $85:", points_earned(85))
print("tier_bonus(3):", tier_bonus(3))

# ============================================================
# Section 3: Data Structures & File Handling
# ============================================================
print("\n=== Section 3.1: Customer Profile & Menu Systems ===")
hq_coords = (40.7128, -74.0060)
print("HQ coordinates:", hq_coords)

guest_emails = ["a@store.com", "b@store.com", "a@store.com", "c@store.com"]
unique_emails = set(guest_emails)
print("Unique emails:", unique_emails)

item_stock = {"Shirt": 50, "Pants": 30, "Hat": 15}
item_stock["Hat"] = 20
print("Updated stock:", item_stock)

prices = [15.0, 25.0, 40.0, 10.0]
discounted_prices = [p * 0.90 for p in prices]
print("Discounted prices:", discounted_prices)

print("\n=== Section 3.2: Audit Logging & Error Handling ===")
with open("audit_log.txt", "a") as log_file:
    log_file.write("Daily audit complete.\n")
print("Audit log written to audit_log.txt")

try:
    store_id = int(input("Enter Store ID Number: "))
except ValueError:
    print("Error: Store ID must be an integer.")
else:
    print("Store ID recorded successfully.")
finally:
    print("Session closed.")

# ============================================================
# Section 4: Standard Modules & Custom Utility Package
# ============================================================
print("\n=== Section 4.1: Built-in Modules ===")
import random
import datetime

print("Today's date:", datetime.date.today())
print("Order tracking number:", random.randint(1000, 9999))

print("\n=== Section 4.2: Custom Module ===")
from inventory_utils import check_stock

print("check_stock(5):", check_stock(5))

# ============================================================
# Section 5: Object-Oriented Programming
# ============================================================
print("\n=== Section 5: Store Branch Class Hierarchy ===")


class StoreBranch:
    company_name = "Urban Retail"

    def __init__(self, branch_id, daily_revenue):
        self.branch_id = branch_id
        self.__daily_revenue = daily_revenue  # private (encapsulated)

    def get_revenue(self):
        return self.__daily_revenue


class FlagshipStore(StoreBranch):
    def __init__(self, branch_id, daily_revenue, vip_lounge_access):
        super().__init__(branch_id, daily_revenue)
        self.vip_lounge_access = vip_lounge_access

    def get_revenue(self):  # method overriding (polymorphism)
        return super().get_revenue() + 500.0


flagship = FlagshipStore(101, 2000.0, True)
print(f"{flagship.company_name} - Branch {flagship.branch_id} final revenue: ${flagship.get_revenue()}")
