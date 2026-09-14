# Badge Readers & Badge Cloning

## Overview

If you've worked in IT, cybersecurity, or physical security, you've probably seen employees use a badge to unlock a door and assumed that the badge itself is secure.

That assumption depends heavily on **what technology the badge and reader use**.

Older access control systems, especially those using **125 kHz proximity cards**, can have significant security weaknesses. In some cases, an attacker with inexpensive hardware can read a badge and create a duplicate credential.

This does **not** mean every badge system is insecure. It means organizations need to understand **what technology they are actually using** and whether it still meets modern security requirements.

---

# What Is a Badge Reader?

A **badge reader** is a device that communicates with an access-control credential and determines whether the credential should be granted access.

Depending on the system, the credential may be:

- Proximity card
- Smart card
- RFID card
- Key fob
- Mobile device
- NFC credential
- Biometric identifier

The reader communicates with an access-control system, which determines whether the credential is authorized.

### Access Flow

```text
Employee Badge
      ↓
Badge Reader
      ↓
Access Control System
      ↓
Allow / Deny Access
```

The security of this process depends on **how the credential identifies and authenticates itself**.

---

# The Problem With Older 125 kHz Badges

One of the most common legacy technologies is **125 kHz low-frequency (LF) RFID**.

These systems are popular because they are:

- Inexpensive
- Simple to deploy
- Reliable
- Easy to maintain
- Compatible with older infrastructure

However, many legacy 125 kHz credentials were designed primarily around **identification**, rather than strong cryptographic authentication.

Some systems effectively communicate a static identifier to the reader.

Example:

```text
Badge → "12345678"
```

The reader checks whether `12345678` is authorized.

The problem is that if the credential's identifier can be read and reproduced, an attacker may be able to create a credential that the system accepts as legitimate.

---

# What Is Badge Cloning?

**Badge cloning** is the process of creating a credential that reproduces the identifying information of another badge.

The goal is not necessarily to compromise the access-control server.

Instead, the attacker attempts to make a duplicate credential appear legitimate to the reader.

### Conceptual Example

```text
Legitimate Badge
      ↓
Credential Information
      ↓
Duplicate Credential
      ↓
Badge Reader
      ↓
Access Granted
```

This differs from stealing a physical badge:

- A stolen badge can be deactivated.
- A cloned badge may continue working until the credential is changed or invalidated.

---

# Why Flipper Zero Gets Attention

Devices such as the **Flipper Zero** have made RFID and NFC experimentation significantly more accessible.

With compatible legacy credentials, these devices can demonstrate how easily certain older access-control technologies can be read or emulated.

The important distinction is:

> **The device isn't necessarily the vulnerability. The underlying credential technology is.**

If a badge uses strong cryptographic authentication, simply reading the card does not provide everything necessary to create a valid duplicate.

---

# Identification vs Authentication

This is one of the most important concepts when evaluating an access-control system.

## Identification

The credential essentially says:

```text
"I am credential 123456."
```

The system checks whether credential `123456` is authorized.

## Authentication

The credential proves that it is legitimate.

Example:

```text
Reader → Challenge
       ↓
Credential → Cryptographic Response
       ↓
Reader → Validate Response
       ↓
Access Granted
```

### Key Difference

- **Identification:** Copying the identifier may be enough.
- **Authentication:** Knowing the identifier alone should not allow an attacker to reproduce the credential.

---

# Why Modern Credentials Are More Secure

Modern access-control technologies can use **cryptographic authentication** rather than relying solely on a static identifier.

Examples include:

- AES encryption
- Secure key storage
- Challenge-response authentication
- Diversified keys
- Mutual authentication
- Secure messaging

A modern credential may contain secret cryptographic material that is never directly exposed.

An attacker might be able to see:

```text
Card ID: 12345678
```

But that does **not** necessarily provide the secret key required to authenticate as the card.

---

# Legacy vs Modern Access Control

| Feature | Legacy 125 kHz | Modern Smart Credential |
|----------|----------|----------|
| Frequency | 125 kHz | Often 13.56 MHz |
| Static identifiers | Common | Possible, but stronger systems 
