"""Write the winning plan to /output/entry.txt.

Deterministic, stdlib only, no network, no randomness.
"""

import os

ENTRY = (
    "Find 40 firms on Indeed paying $500+/mo for manual data entry. "
    "Email each hiring manager: a $199 one-time automation that does the job, "
    "built in a day. They already budget for it, so 2-4 sales = $400-800. "
    "Paid by Stripe; reinvest profits in outreach. "
    "Day one: list the 40 ads."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
