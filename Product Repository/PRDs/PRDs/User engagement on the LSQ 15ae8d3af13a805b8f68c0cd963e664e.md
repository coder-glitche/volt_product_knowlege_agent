# User engagement on the LSQ

: Naman Agarwal
Created time: December 12, 2024 12:02 PM
Status: Not started
Last edited: December 12, 2024 5:55 PM

Currently issues 

# Ticketing System Requirements & Workflow

Chief Product Officer Document | December 2024

## Executive Summary

Our current ticketing infrastructure needs a significant overhaul to address critical gaps in issue tracking, resolution monitoring, and customer service delivery across multiple channels. This document outlines the requirements for a new unified ticketing system that will serve our diverse user base and improve operational efficiency.

## Current Pain Points Analysis

1. Issue Resolution Tracking
    - No unified system to track resolution progress
    - Limited visibility into resolution time frames
    - Inability to measure team performance effectively
2. Organizational Context
    - Disconnected systems leading to fragmented customer context
    - Multiple tools (Exotel, RUNO, Retool, LSQ CRM, Zendesk) creating data silos
    - Limited cross-functional visibility
3. Support Coverage
    - Backup handling inefficiencies
    - Lack of structured handover processes
    - No clear escalation matrices
4. Performance Metrics
    - Missing TAT (Turn Around Time) tracking at issue level
    - No trend analysis capabilities
    - Unable to identify recurring issues and root causes

## Core Requirements

### Ticket Creation & Management

1. Mandatory Ticket Creation
    - 100% ticket creation for all customer interactions
    - Channels: Phone calls, WhatsApp, Email
    - Required fields: Partner ID, Issue Category, Description
    - Clear resolution confirmation before ticket closure
2. Channel-Specific Workflows
    - MFD Channel specific routing rules
    - Direct customer support workflow
    - B2B partner interface requirements
3. SLA Management
    - Channel-specific SLA definitions
    - Real-time SLA tracking
    - Escalation workflows
    - Performance dashboards

### User Management & Access Control

1. Internal Users
    - MFD Channel Team (5 RMs, 2 backup RMs, 2 Chat support)
    - Support Channel Team (10 agents)
    - Sales Team (7 members)
    - Ops and Tech on-call teams
    - Admin users
2. External Users
    - Direct MFDs
    - Platform MFDs
    - B2C customers
    - B2B platform partners

### Integration Requirements

1. Communication Systems
    - Exotel for call routing
    - RUNO for call visibility
    - Periskope and WATI for WhatsApp
    - Email integration
2. Internal Systems
    - Retool for DB state visibility
    - LSQ CRM
    - Slack for internal communications

## Key Features

1. Unified Dashboard
    - Single view of customer interactions
    - Real-time status tracking
    - SLA monitoring
    - Team performance metrics
2. Analytics & Reporting
    - Issue frequency analysis
    - Resolution time tracking
    - Team performance metrics
    - Channel-wise analysis
    - Custom report generation
3. Workflow Automation
    - Automatic ticket routing based on channel and issue type
    - SLA-based escalation
    - Auto-assignment for backup handling
    - Status update notifications

## Success Metrics

1. Operational Metrics
    - 100% ticket creation compliance
    - SLA adherence rate
    - Average resolution time
    - First call resolution rate
2. Quality Metrics
    - Customer satisfaction scores
    - Issue recurrence rate
    - Escalation frequency
    - Team performance scores

## Implementation Considerations

1. Data Migration
    - Historical ticket data
    - Customer interaction history
    - Knowledge base articles
2. Training Requirements
    - Role-based training modules
    - Standard operating procedures
    - Knowledge transfer sessions
3. Rollout Strategy
    - Phased implementation approach
    - Pilot with MFD channel
    - Gradual extension to other channels

## Open Questions & Challenges

1. Technical Integration
    - How to ensure seamless integration with existing tools?
    - What is the backup plan for system downtime?
    - How to handle data synchronization across platforms?
2. Business Process
    - How to maintain MFD privacy requirements while ensuring effective support?
    - What is the escalation matrix for different types of issues?
    - How to handle peak load scenarios?
3. Change Management
    - How to ensure adoption across different teams?
    - What metrics will define success?
    - How to handle resistance to change?