# iPad / iOS Deployment

This post is more of a personal reflection than a traditional guide. At my current job, I help support field workers: crews working on bridges, milling operations, and general roadway construction. Foremen and superintendents are issued iPads to track progress, document work, and manage their teams’ hours.

## Cisco Meraki MDM

Before an iPad is sent into the field, it must be enrolled in our Mobile Device Management (MDM) system—Cisco Meraki. Meraki provides powerful tools for deploying, securing, and managing iOS devices remotely.

### Key Cisco Meraki Features

- **Location Tracking**: See approximate device location.
- **Device Details**: Model, serial number, charge level, and assigned owner.
- **Operating System Info**: Keep track of OS version for compliance.
- **Security Settings**: Ensure encryption and passcode policies are in place.
- **Storage Monitoring**: View available vs. used storage.
- **Network Details**: Wi-Fi and IP address visibility.
- **Cellular Info**: Monitor SIM status and data usage.
- **Remote Commands**: Erase device, install or remove apps, lock screen, etc.
- **Event Logs**: Full history of actions and changes.

Each iPad is assigned a **tag** in Meraki, which acts as a profile that installs pre-approved settings and apps automatically once the device is enrolled.

## iPad Setup Process

Once the iPad is enrolled and configured with the user’s Apple ID and Microsoft credentials, the goal is to set it up completely so it requires minimal troubleshooting in the field.

### Core Applications We Install

- **Email (Outlook)** – Configured for company communication.
- **Authenticator (Microsoft Authenticator)** – Required for MFA across systems.
- **Ticketing App** – Used for reporting device or system issues.
- **Copilot** – For AI-assisted productivity.
- **OneDrive** – Cloud storage and file sharing.

The goal is to have everything ready from day one, so the user can start working with as few roadblocks as possible. Proper setup upfront minimizes downtime and support requests

