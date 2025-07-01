# Password Security Analysis Report

## 1. Password Samples

| Password                      | Length | Complexity   | cracklib-check | Dictionary Test       | Estimated Crack Time |
|------------------------------|--------|--------------|----------------|------------------------|----------------------|
| `weak123`                    | 7      | Low          | too short      | Found in rockyou.txt   | Instant              |
| `P@ssword1`                  | 9      | Medium       | OK             | Variation found        | 2 hours              |
| `Tr0ub4d0ur&3`               | 11     | High         | OK             | Not found              | 3 years              |
| `xK8#qP$2mL!9zR*5`           | 16     | Very High    | OK             | Not found              | Millions of years    |

## 2. Tools Used

- **cracklib-check**: Checks basic strength and policy adherence
- **grep + rockyou.txt**: Simulates dictionary-based cracking
- **Python scripts**: Evaluate structure, entropy, and uniqueness
- **hashcat**: Simulates brute force and GPU-based cracking

## 3. Key Observations

- **Longer passwords outperform complex short ones**
  - e.g., `CorrectHorseBatteryStaple!` > `P@ssw0rd!`
- **Random characters defeat dictionary attacks**
- **Password reuse is the biggest vulnerability**
  - 60% of users reuse passwords (Verizon DBIR 2023)

## 4. Attack Vectors & Prevention

| Attack Type        | Description                             | Protection                      |
|--------------------|-----------------------------------------|----------------------------------|
| Brute Force        | Tries all combinations                  | Use long, complex passwords      |
| Dictionary         | Uses common words and patterns          | Avoid predictable sequences      |
| Phishing           | Tricks users into sharing credentials   | Verify websites, use 2FA         |
| Credential Stuffing| Uses leaked credentials across sites    | Use unique passwords per site    |

## 5. Complexity vs. Security

| Password Type           | Crack Time       | Security Level |
|-------------------------|------------------|----------------|
| 6 lowercase letters     | Instant          | Very Weak      |
| 8 mixed-case characters | 2 days           | Weak           |
| 12 characters + symbols | 34 years         | Strong         |
| 16+ random characters   | Millions of years| Very Strong    |

## 6. Best Practices

- Minimum **12 characters**, ideally more
- Mix **uppercase**, **lowercase**, **numbers**, and **symbols**
- Prefer **passphrases** (e.g., `PurpleElephant$RunsFast!`)
- Never reuse passwords
- Use tools like **KeePassXC** or **Bitwarden**
- Enable **2FA** wherever possible

---

*Report created in Kali Linux virtual environment on February 20, 2024.*
