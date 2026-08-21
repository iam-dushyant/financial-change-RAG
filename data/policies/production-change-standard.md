# Production Change Standard

## Purpose

This standard defines the minimum controls required for changes to production technology services. It applies to application, infrastructure, database, configuration, network, and platform changes that may affect production service behaviour.

## Change Ownership

Every production change must have a named change owner.

The change owner is accountable for:

- defining the purpose and scope of the change;
- confirming that implementation steps are complete and technically reviewed;
- confirming that validation steps are defined before implementation;
- ensuring that a rollback or recovery approach exists;
- coordinating execution during the approved change window;
- confirming the final outcome after implementation.

Ownership may not be assigned to a shared mailbox, team name, or automated account.

## Pre-Implementation Validation

Before implementation, the change owner must confirm that:

- the requested change has been reviewed by an appropriate peer or technical approver;
- required testing has completed successfully in a suitable lower environment where practical;
- implementation commands, scripts, or deployment artefacts have been reviewed;
- dependencies and downstream impacts have been considered;
- monitoring is available to determine whether the change has succeeded;
- the rollback criteria are understood.

A production change must not begin if the validation method is undefined.

## Change Windows

Production changes must be executed within an approved change window unless the change is being performed under an emergency-change process.

The selected change window should take account of:

- expected customer impact;
- service criticality;
- support-team availability;
- dependency availability;
- business processing cycles;
- batch, settlement, or reconciliation windows.

A change must not deliberately overlap with a known high-risk processing period unless the risk has been explicitly accepted through the appropriate change-governance process.

## Implementation

The change owner must follow the documented implementation plan.

Material deviations from the approved implementation plan must be assessed before continuing.

If the actual implementation differs significantly from the approved plan, the change should be paused unless continuing is necessary to protect service stability.

## Validation After Change

Post-change validation must confirm that the intended outcome has been achieved.

Validation should include, where relevant:

- service health checks;
- application logs;
- infrastructure metrics;
- functional smoke tests;
- dependent-service checks;
- customer-impact indicators;
- error-rate or latency monitoring.

The absence of alerts alone is not sufficient evidence that a change was successful.

## Rollback

Every change that can reasonably be reversed must include a documented rollback plan.

The rollback plan should identify:

- the condition that triggers rollback;
- the person responsible for making the rollback decision;
- the rollback steps;
- any data-restoration requirements;
- expected rollback duration;
- validation steps after rollback.

If rollback is not technically possible, the change record must describe the alternative recovery approach.

A change owner must not claim that rollback has been approved unless that approval is explicitly recorded in the relevant change record.

## Completion

A production change may be marked successful only after required validation has completed.

If unexpected degradation remains after implementation, the change must not be closed as successful solely because deployment commands completed without error.

## Exceptions

Exceptions to this standard require documented approval through the appropriate change-governance process.

This document does not itself grant approval for any individual production change.
