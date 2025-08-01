# Multi Factor Authentication (MFA)

Almost every company out there now uses some form of MFA, to protect their users, systems and data. For those of you who do not know, MFA is a security process that requires a user to verify their identitfy using a MINNIMIUM of two or more **DIFFIERENT** tpye of crednetials before they can gain access to a system account, or other senstitive data. 

## How to Authenticate Users

There are three categories of crednetials when it comes to Authorizing Users in MFA/2FA

- Something you know: A password or pin
- Something you know: A smartphone, badge, token
- Something you are: Facial recognition, or any other biometrics

One thing to remember from this, is that if you have two Something you know, such as a Pin and then your birthday, that is not MFA, both of these are something you know and are knowledge based. To have a true MFA system you need to have 2 different categories.

Examples:
- Password + code from phone (Know + Have)
- Password + Fingerprint (Know + are)
- Badge + Facial Scan (Have + Are)

## Why we Authenticate users

If we do not authenticate users, how will we truly know who is accessing systems and senstitive information. MFA adds an extra layer of protection beyond jsut a username and password.

1. Passwords are weak
   - Passwords can be brute forced, stolen, or leaked
   - People use the same password across multiple accounts
2. MFA uses multiple proofs of Identity
   - Even if a hacker gets one, they can't get all the way in without the other
   - Uses combinations of the above categories
3. Prevents unauthroized access
   - Makes it harder to access your accounts
4. Reduces risk of phishing and credential theft
   - Many phsihing attacks target login credentials like passwords on dirty sites.
5. Protects senstitive data and Systems
6. Compliance and Regulations
   - Some industries REQUIRE it due to laws such as HIPAA or GDPR

## 2FA vs MFA

When it comes to MFA, a lot of people just use the term 2FA (Two-factor authentication), without knowing the difference. 2FA is actually a subset of MFA.

Multi-Factor Authentication (MFA) is a method of verifying a user's identity by requiring **two or more** verification factors. Two-Factor Authentication (2FA) is a specific type of MFA that uses **exactly** two factors.

## Definitions

| Term    | Number of Factors | Example                           |
| ------- | ----------------- | --------------------------------- |
| **2FA** | Exactly 2         | Password + SMS code               |
| **MFA** | 2 or more         | Password + SMS code + fingerprint |

- **2FA (Two-Factor Authentication):** Uses exactly two different types of authentication factors.
- **MFA (Multi-Factor Authentication):** Uses two or more different types of authentication factors, including 2FA and beyond.


