# Incident Severity Guide

## Purpose

This guide provides a common framework for classifying technology incidents as SEV1, SEV2, or SEV3 based on business impact, service disruption, customer impact, and urgency.

Severity is determined by impact, not by the number of engineers involved or the perceived technical complexity of the fault.

## SEV1 - Critical

A SEV1 incident represents critical impact.

Examples may include:

- widespread inability for customers to access a critical service;
- widespread payment-processing failure;
- confirmed material data corruption affecting a critical service;
- major security compromise with active impact;
- prolonged outage of a system supporting time-critical financial processing.

Expected response:

- immediate incident coordination;
- dedicated incident leadership;
- rapid mobilisation of required technical teams;
- frequent stakeholder communication;
- active tracking of customer and business impact;
- explicit recovery and validation activities.

Communication should begin as soon as a credible critical impact is identified. Teams should not wait for full root-cause confirmation before communicating material impact.

## SEV2 - Major

A SEV2 incident represents significant but not critical impact.

Examples may include:

- partial degradation of an important service;
- failure affecting a significant subset of customers;
- substantial performance degradation;
- repeated transaction failures with an available workaround;
- loss of redundancy that creates elevated operational risk;
- material downstream processing delay without complete service outage.

Expected response:

- prompt incident ownership;
- coordinated technical investigation;
- regular stakeholder updates;
- monitoring of whether impact is increasing or decreasing;
- defined recovery actions.

If impact expands materially, the incident should be reassessed and may be raised to SEV1.

## SEV3 - Moderate

A SEV3 incident represents limited or moderate impact.

Examples may include:

- a localised defect affecting a small number of users;
- degradation of a non-critical feature;
- an operational issue with a reliable workaround;
- a non-urgent processing delay with no material financial impact;
- a fault detected internally before significant customer impact occurs.

Expected response:

- assigned ownership;
- normal engineering investigation;
- communication appropriate to the affected teams;
- tracking through to resolution.

A SEV3 should be escalated if the impact becomes broader or more severe.

## Severity Assessment

Incident severity should consider:

- number of customers affected;
- criticality of the affected service;
- transaction or financial impact;
- duration;
- availability of a workaround;
- data-integrity impact;
- security impact;
- regulatory or operational deadlines.

No single metric automatically determines severity in every situation.

## Communication

Incident communications should distinguish known facts from hypotheses.

Updates should include, where known:

- current impact;
- affected services;
- actions in progress;
- recovery status;
- next update time.

Unconfirmed root causes should not be presented as established facts.

## Recovery and Closure

An incident should not be considered resolved solely because a service has restarted.

Recovery validation should confirm that:

- service health has stabilised;
- transaction processing is functioning as expected;
- critical backlogs are being processed;
- customer impact has ended or materially reduced;
- relevant monitoring remains healthy.

Severity classification may be revised as new evidence becomes available.
