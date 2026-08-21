# Payments Release Policy

## Purpose

This policy defines minimum engineering controls for releases affecting payment-processing services, payment messages, transaction data, reconciliation flows, and related interfaces.

## Scope

The policy applies to production releases that may affect:

- payment initiation;
- payment routing;
- transaction authorisation;
- settlement processing;
- payment-state transitions;
- payment message schemas;
- reconciliation data;
- downstream financial reporting interfaces.

## Release Ownership

Every payment release must have a named release owner.

The release owner is responsible for coordinating:

- implementation readiness;
- dependency checks;
- release timing;
- validation;
- rollback planning;
- reconciliation checks where applicable.

## Backward-Compatible Schema Changes

Changes to payment-related schemas should be backward compatible wherever practical.

Preferred patterns include:

- adding optional fields rather than changing the meaning of existing fields;
- allowing old and new message consumers to operate during migration;
- introducing new schema versions without immediately removing previous versions;
- deploying consumers before producers when introducing new optional data;
- preserving existing field semantics during phased rollouts.

Breaking schema changes require explicit migration planning and must identify all affected producers and consumers.

A schema change must not assume that all dependent systems will be upgraded simultaneously unless this dependency has been verified.

## Payment Release Validation

Before release, teams should validate:

- message parsing;
- transaction-state handling;
- duplicate-message behaviour;
- retry behaviour;
- failure paths;
- downstream compatibility;
- logging and traceability;
- reconciliation outputs.

Testing should include representative payment states rather than only successful payment flows.

## Reconciliation

Reconciliation is required where a release can affect transaction balances, payment states, settlement records, or downstream financial reporting.

The release plan should define:

- which systems or datasets will be reconciled;
- expected record counts or value totals;
- acceptable tolerance, if any;
- who reviews the reconciliation result;
- what action is taken if a mismatch is found.

A technically successful deployment is not sufficient evidence of a successful payment release if reconciliation identifies unexplained discrepancies.

## Release Windows

Payment releases should avoid known settlement, reconciliation, end-of-day, or other critical financial-processing windows unless the release has been specifically assessed for those periods.

The release owner should confirm that relevant operational and engineering support is available for the planned window.

## Rollback and Recovery

A release affecting payment processing must include a rollback or recovery strategy.

The strategy should account for the possibility that:

- application binaries can be rolled back but data cannot;
- messages may already have been emitted;
- schema changes may already have been consumed downstream;
- transaction state may require manual reconciliation.

Rollback must not be described as "safe" solely because a previous application version can be redeployed.

## Post-Release Monitoring

Post-release monitoring should include relevant indicators such as:

- payment success and failure rates;
- processing latency;
- duplicate or retry rates;
- queue depth;
- failed downstream deliveries;
- reconciliation mismatches.

Monitoring duration should be appropriate to the processing cycle affected by the release.

## Governance

This policy defines engineering expectations. It does not provide regulatory approval, risk acceptance, or business authorisation for any specific release.
