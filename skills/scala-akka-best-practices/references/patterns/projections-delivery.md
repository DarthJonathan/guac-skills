# Readside freshness, replay, delivery, and partial writes

426 source-specific cases. Statements retain their historical scope and source stance. Read related PR cases for corrections or alternatives.

## Cases

- A1-0011 — Remove code in CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4
- A1-0012 — Expiry events accept optional lastUpdatedTS and use latest only if absent
- A1-0013 — CRA snapshot handler updates target row idempotently
- A1-0014 — Assessment history PK is customerId and lastUpdatedTS
- A1-0015 — Complex product acknowledgement strictly follows assessment
- A1-0016 — CRA snapshot stores queryable derived columns while history updates only advisoryProfile
- A1-0017 — Patch function is already checked not to change profile lastUpdatedTS
- A1-0018 — CRA history does not update by lastUpdatedTS alone
- A1-0019 — CRA snapshot updates explicit columns to exclude complex product acknowledgement
- A1-0020 — Alert on possible CRA history corruption without blocking projection
- A1-0022 — Snapshot projection V2 never persists complexProductKnowledgeAttestationDate (identified in hunk)
- A1-0023 — Profile JDBC projection V2 never persists complexProductKnowledgeAttestationDate (identified in hunk)
- A1-0024 — Review-pattern comparison on first commit before and after update
- A1-0097 — Corrupt MV projection could suppress comms for actual breach-suggested event
- A1-0559 — Auto-rebalance communication buffer may fail under projection lag
- A1-0560 — Use generic communication-ID helpers with explicit event and recipient seed
- A1-0562 — Different tags allow first-goal notification to miss both A and B
- A1-0563 — Choose first-goal notification by createdAt minimum instead of buffer
- A1-0565 — Share pending-trades-stopped rebalance communication condition in base
- A1-0633 — Restore deprecated SMART_BETA for persisted event replay
- A1-0636 — Missing customer in historical CKA projection logs and skips
- A1-0645 — Update marketdata InstrumentTopicSubscriber condition for InstrumentDetailsUpdatedMsg
- A1-0724 — Trigger monthly-data refresh only on changed stitch config
- A1-0771 — Apply change to recentEntityChanges and recentEntityChangesData
- A1-0777 — Unsorted plan-keyed recentEntityChangesData has undefined context selection
- A1-0782 — Append only recently created plans when faking initial investment
- A1-0784 — Enable RRT by config and merge upstream in queryCustomerTransactions
- A1-0785 — Patch/base merge may replace cancelling or orders-generated upstream with pending transaction
- A1-0789 — Resolve goal RRT plans before entityIds filter to avoid overfetch
- A1-0790 — Use InvestmentRrtCommandContext with rrtContext None instead of SystemTriggeredCommand
- A1-0793 — Use recentEntityChanges rrtContextFilter; returned contexts guide fetching
- A1-0794 — Filter expected contexts with Option forall and empty-list wildcard
- A1-0844 — Redeemable-value readside call may need consistency review
- A1-0845 — Use non-RRT getPlanRedeemableValue
- A1-0846 — Readside getPlan mixed with RRT redemption call needs consistent choice
- A1-0847 — Trading projection may not need RRT change
- A1-0959 — SgCustomerServiceTopics.CustomerServiceComplianceTopic already enriched with tenant context
- A1-0970 — Use updatedAt from message payload
- A1-0973 — Messages can share timestamp; communication identity needs message type or context
- A1-0996 — Readside SIP schedule lookup has rare creation-then-TAA-modify race
- A1-1092 — Always return at least readSideResults; only RRT should time out
- A1-1095 — RRT merge must handle hard and soft deletions
- A1-1099 — RRT helper distinguishes fetch failure empty/deleted and fetched data
- A1-1103 — Refresh readSideLoader on timeout
- A1-1104 — Use data-to-entity-ID extractor to remove readside tombstones before topping up entity data
- A1-1105 — Keep readsideData entityData and entityTombstones separate
- A1-1106 — Investment RRT groups requests by PlanId then tombstone-filters and replaces whole groups
- A1-1107 — Goal RRT groups by GoalId then tombstone-filters and replaces one-element groups
- A1-1111 — Document A deleted or filtered in entity loader
- A1-1112 — RRT example retains inactive status until caller postmerge filter
- A1-1121 — By-entity merge replaces every readside entry for same entityId
- A1-1122 — By-key merge overrides matching key but missing data does not delete
- A1-1142 — AccreditedInvestorEntity readside depends on customer Kafka; API race accepted
- A1-1231 — Use existing voucher JDBC projection if historical events irrelevant
- A1-1311 — New RPC projection not started in HK
- A1-1312 — Existing RPC B2C comms projection must skip B2B workflow communications
- A1-1330 — Skip B2B in existing comms projection in this PR before independent comms change
- A1-1427 — Warn and rethrow trade-cancel command so projection retries
- A1-1429 — Redemption may wait for cancelled-trade event propagation
- A1-1434 — Log error and move on rather than stall whole projection tag
- A1-1449 — Decide throw versus retry-and-give-up to avoid projection block
- A1-1461 — Remove live full-redemption recheck from invalid-order replay handling
- A1-1504 — Handle new advised payloads in goal projections including GoalSupportingDataProjection
- A1-1702 — Daily-price deletion requires InstrumentMarketDataMsg for timeseries propagation
- A1-1704 — Repeated row delete on projection offset replay is idempotent
- A1-1716 — Use readside updatedAt rather than createdAt LocalDate for schedule removal
- A1-1717 — Rare schedule-update/full-redemption race within7s plus projection lag accepted
- A1-1720 — Do not send expired comms merely after successful remove command
- A1-1851 — Error-log and move on instead of Kafka stall
- A1-1882 — Stop publishing deprecated portfolio events
- A1-1967 — Do not replay new goal projection into same live plan table
- A1-1968 — No simultaneous V4/V5 writes to planV4
- A1-2004 — Add goal-service consistency endpoint pair; mismatch sync via command
- A1-2005 — Check goal/rebalance plan readside consistency instead of unnecessary endpoint
- A1-2040 — Fee command duplicate initiatingFullRedemptionRequestId check makes topic handling idempotent
- A1-2141 — PLAN_ONE_TIME_INVESTMENT_APPROVED needs investment-service trigger
- A1-2149 — At-least-once workflow approval uses stable requestIdSeed to dedupe investment
- A1-2151 — Use goal supporting-data table populated via investment projection/internal endpoint
- A1-2165 — Investment projection+goal internal upload versus Kafka approved event+subscriber
- A1-2281 — Consider recipientId for reassigned task; insertion target unspecified
- A1-2370 — Normal instruments enter readside via price updates; benchmarks lack those
- A1-2427 — Combine two completion mails for same customer internal plan transfer
- A1-2428 — Send only after both sides submitted/completed with identical data
- A1-2437 — Invalid persisted event log and skip; replay cannot fix it
- A1-2440 — Invalid reference data should throw because fixable then retry
- A1-2442 — Do not block projection on permanently invalid persisted event
- A1-2445 — Communication identity uses planId instead of customerId
- A2-0026 — BackfillPlanProfileTenantIdCmdHandler: Let’s also return without events if same tenantId already exists. Then we won’t have duplicated events, as the subscriber might process a ...
- A2-0027 — BackfillPlanProfileTenantIdTaskTopicSubscriber: We shouldn’t need planId as part of the cmd since it’s already entityId
- A2-0028 — PlanProfileJdbcProjectionV3: Since we have the full PlanProfile in the `PlanProfileTenantIdBackFilledEvt`, let’s use it directly instead of fetching from entity again.
- A2-0029 — FeeChargeRequestJdbcProjectionV6: I think we can let DB take care of both the query and update. Something like `UPDATE feeChargeRequests SET tenantId WHERE customerId, planId`
- A2-0030 — FeeChargeRequestJdbcProjectionV6: There’s no need to query this anymore. The `updateTenantId` takes care of all requests with matching customerId/planId
- A2-0031 — BackfillPlanProfileTenantIdTaskTopicSubscriber: I realize we could have made the task keyed by customerId instead, then in this subscriber, we query planProfiles by customerId a...
- A2-0036 — BaseRedemptionCommunicationV2Projection: Here we change the formula to generate communication id. During deployment, depending on timing, this might cause the email to trigger t...
- A2-0037 — SgRedemptionCommunicationV2Projection: Can save tenant lookup call if returned context is empty
- A2-0039 — BaseRedemptionCommunicationV2Projection: Naming can be a little confusing now
- A2-0105 — GoalSupportingDataProjection: `ele.event.taskApprovalDetails` should compile so no need to check this
- A2-0106 — GoalSupportingDataProjection: This block probably can refactor to avoid repeating the code vs `handleGoalCreationApprovedHandler`
- A2-0121 — InvestmentSupportingDataProjection: Now we know these projections can cost us decent chunk of money, since it’s not used in prod, maybe good chance to reuse existing projection ...
- A2-0128 — InvestmentSupportingDataProjection: reuse $context and actionContext
- A2-0135 — GoalSupportingDataProjection: Maybe just call `upsertGoalSupportingData` directly?
- A2-0144 — InvestmentSupportingDataProjection: Last chance to change with relatively little cost, before committing this to prod. Is there strong reason for this to be standalone projectio...
- A2-0151 — InvestmentPlanEventProcessor: We now wire sg class in common projection used in hk. It should be split…
- A2-0182 — SgWorkflowEngineE4s: WorkflowEngineE4s
- A2-0200 — InitiateCancellationFlowCmdHandler: This `INVALID_CANCEL_ATTEMPT` is mapped to NotFound right now. It seems not used, so maybe change it to BadRequest instead?
- A2-0208 — BffServiceE4s: This should work, but would be better to follow Option 2 explained in [<url> data-inline-card='' } 
- A2-0213 — CostOfInvestmentDetailsJdbcProjectionV7: Remove this call since we are looking up whole txn below?
- A2-0283 — PlanFeeInstructionEntity: Just thinking out loud, I’m not sure about capturing this effectiveEndDate in the event
- A2-0291 — common: Removed since wrong existing config. `projection` doesn’t have any entity anymore
- A2-0301 — BaseServiceLogicImpl: The cmd is idempotent anyway, so maybe we just trigger from goal level instead? No need to double lookup
- A2-0313 — RecurringInvestmentScheduleHistoryDataEventProcessorV3: `PlanRecurringInvestmentScheduleHistoryTableV3` stores the history audit entries, so we can’t rely on this backfill evt t...
- A2-0319 — InstrumentMonthlyChangesTaskSubscriber: Should be `upload` not `calculate`
- A2-0346 — GoalEventProcessor: We split new projection, inject `WorkflowEngineServiceSg` and wire it only for SG
- A2-0347 — GoalSupportingDataTableV1: `GoalActionContext` covers `CREATION_APPROVED, MODIFICATION_APPROVED` which is initiated from goal svc
- A2-0435 — Review: How to persist documentIds for goal? One approach could be below \(we can review again later\)
- A2-0483 — Review: ## SG
- A2-0484 — PortfolioStatsJdbcTable: I don’t create these index in V2:
- A2-0520 — HkFeeManagerProjection: There is no tax in HK at all, so maybe simpler solution would be to have `HkFeeManagerProjection` only handle `FeeChargeDiscountAppliedEvt` which would t...
- A2-0523 — HkFeeManagerProjection: HK simply doesnt have any tax for investment. And as you can see, it’s very simple to add when the gov changes this, if ever. If they actually do that, w...
- A2-0527 — HkChargeCommunicationEventProcessor: Can we name this `HkChargeCommunicationProjection` instead? Previously these were named `*EventProcessor` because of Lagom pattern
- A2-0530 — HkFeeManagerProjection: No need for-comprehend block here
- A2-0541 — HkChargeCommunicationProjection: These don’t need to be val
- A2-0544 — HkChargeCommunicationProjection: This logic actually exists in `InitiateFeeRedemptionCmdHandler`, it’s best we rely on sequence of events, rather than duplicating it again.
- A2-0548 — HkChargeCommunicationProjection: Can we put meaningful message here? Maybe sth along the line of `Skipping communication for FeeChargeCompletedEvt of planId $planId, feeChargeRe...
- A2-0552 — SgGoalCreateInvestmentSummaryBehaviour: [person] [person] Looks like we look up `portfolio` here, but only use id and effectiveDate from it - these are already available in `pro...
- A2-0597 — ModelPortfolioEntity: So there are 2 events:
- A2-0608 — PortfolioTopicSubscriber: This can move outside right? We don’t need to do this for every ccy
- A2-0610 — ServiceLogicImpl: I mean move this outside too. No need to bulkUpsert this for every ccy cuz this table doesn’t care about marketCcy
- A2-0651 — package: We need projection too?
- A2-0662 — package: Should be required projection
- A2-0678 — GoalTopicSubscriber: Nit: let’s assign `val portfolioId = plan.targetAssetAllocation.modelPortfolioId` then we can use it below as well
- A2-0697 — InstrumentPortfolioSubscribersDataRepository: Let’s do Source because this List will grow for popular instrument
- A2-0711 — PortfolioMarketDataEventProcessor: Let’s move this to PortfolioTopicSubscriber. Eventually we should also handle `ModelPortfolioDeactivatedMsg` and delete from repo
- A2-0713 — PortfolioMonthlyChangesHelper: Let’s make this method handing the subscriber lookup \+ streaming the task \(in next task\), and keep the instrument projection simple.
- A2-0715 — PortfolioTopicSubscriber: Let’s add an if here to calculate only if not DIY
- A2-0718 — PortfolioMonthlyChangesHelper: I think there are 2 types of race conditions we might see here:
- A2-0753 — SplitCashReservationsForFullRedemptionFeeChargeCmdHandler: It starts from None, and then capture the fee charge amount so far for the full redemption. It might have 2 fee charge...
- A2-0788 — InstrumentPortfolioSubscribersDataRepository: Let’s not put repository yet in this PR. Do join between this and mc table so we can dedupe in DB
- A2-0792 — InstrumentPortfolioSubscribersDataJdbcHandler: Take VO instead of individual fields. Set updatedAt outside
- A2-0793 — InstrumentMarketDataJdbcProjection: Consider skipping old events, and sync to db separately to save cost processing old events we don’t care
- A2-0796 — InstrumentPortfolioSubscribersDataRepository: Just `streamInstrumentPortfolioSubscribers` ?
- A2-0800 — InstrumentMarketDataJdbcProjection: Since we are skipping old events, just don’t handle this event anymore? Can just put a comment
- A2-0802 — PortfolioTopicSubscriber: Yea definitely bulkUpsert here
- A2-0806 — TopicSubscriber: We should also bake in the Kamon Context propagation in this processing flow \(with option to opt out maybe if needed\)
- A2-0811 — TopicSubscriber: We should use `topicSubscriberSettings.parallelism` here?
- A2-0812 — TopicSubscriber: I realize the `ScaladslKafkaSubscriber` additionally set the below
- A2-0813 — BrokerOrderTopicSubscriber: Lagom is using below by default
- A2-0814 — TopicSubscriber: In the TaskTopicSubscribers, these are used to retry processing individual message \(before dropping them\). Here you’re using as config to restart the subscrip...
- A2-0816 — TopicSubscriber: [person] As discussed, it’s actually not safe to blindly increase `parallelism` here when consuming messages from same partition \(only safe for the task topic\).
- A2-0817 — ServiceClientConfig: typesafe config would already throw `ConfigException.Missing` if not set
- A2-0850 — AdvisedGoalCreateHelper: This should be Option. For those request that still have the `initialInvestmentAmount` sent from FE, they can resolve from there. For CoreEnhanced/Flags...
- A2-0855 — ProjectionServiceE4s: Use config instead so that we can switch by just updating manifest, instead of having to build image for projection or releasing caller services
- A2-0856 — ServiceLogicImpl: Move this as private val in `ServiceLogicImpl`
- A2-0880 — ServiceLogicImpl: Should we add to FutureUtils… sth like `withTimer(timer: Timer, => T: Future[T])` and take care of proper start stop there? I suppose we don’t need to capture ...
- A2-0881 — ServiceLogicImpl: A bit late to call with withTimer here cuz the future already started when you define above
- A2-0882 — EmailProviderData: All of these, in theory, would need to be optional. Cuz there might be existing message in the kafka topic without the fields, and communication svc starts ex...
- A2-0888 — Semi-annual report rollout: include communication in services.list
- A2-0932 — InitiateFeeChargeCmdHandler: Maybe we can rearrange this logic a little
- A2-0933 — Review: We also need to emit kafka msg for skipped fee charge and handle it on redemption svc side to complete the full redemption request
- A2-0944 — FeeChargeRequestJdbcRepository: We also need to handle the skipped event in `FeeChargeRequestJdbcProjectionV6`
- A2-0952 — BaseRedemptionCommunicationV2Projection: Can import `TraversableOnceUtils` and use it like this
- A2-0981 — InvestmentTransferCommunicationV2ProjectionSg: Looks like we just need to return a result struct that contains the type of violation, then check if cka violation then send comms...
- A2-0996 — package: Rename to `NotifyRebalanceTradeSettlementDetailsAmendedCmd`… do the same for event and kafka msg
- A2-0997 — NotifyRebalanceTradeSettlementAmendedCmdHandler: This is very dangerous and potentially lead to wonky data state if not done properly by POps. In fact, if you check the entrypoi...
- A2-0998 — TradeTopicSubscriber: Should we add similar check for settlementConfirmed\* fields, similar to `TradeSettlementConfirmedMsg`?
- A2-1006 — RedemptionRequestTopicSubscriberV3: Not sure if we need all these validation in transaction svc. Maybe just dump directly with status = `SETTLEMENT_CONFIRMED`.
- A2-1007 — package: Maybe following naming pattern of investment svc, e.g. `RedemptionRequestSettlementDetailsAmendedEvt`… update for Kafka msg too
- A2-1012 — RedemptionRequestTopicSubscriberV3: Do we need forceUpdate = true since it’s already completed?
- A2-1073 — PushNotificationProviderData: In theory these should be optional \(otherwise we might break serdes of there are lagged messages in the kafka topic\), but I guess this one is ok ...
- A2-1081 — ReportApplication: Just some notes here, yall are right about the trade-offs but manual start is not that bad, depending on use cases.
- A2-1097 — InstrumentJdbcEventProcessor: Let’s use Cassandra projection manager?
- A2-1104 — ProjectionHelper: This doesn’t look right. We already match in `getIndicativeAmount`, we shouldn’t need to match again
- A2-1105 — ProjectionHelper: Use `resolvedRecurringAmountInPlanCcy`?
- A2-1136 — CassandraProjectionManager: Due to this issue, currently all of these spans completes almost instantly \(~0.005s as per current metrics in both prod and staging env\)
- A2-1150 — HkRebalancePlanCommunicationV2Projection: Why is it a warn? Just info right? Same for sg
- A2-1166 — TradingRestrictionLogic: No need to duplicate this whole comment right? Just put both threshold breach \+ portfolio version update into same line?
- A2-1171 — Review: Tested in SG staging with `charge` svc
- A2-1172 — TaskTopicManagementPubSub: This is only published to whoever subscribes to this akka Topic, i.e. the service instances only
- A2-1174 — TaskTopicManagementPubSub: No issue if wrong task. I added error log for this in TaskTopicManager too.
- A2-1176 — Review: That would be next step. Need to check w PM regarding where to store, and the query requirement for it. Likely we just need to stamp in productLineAndIntent… and build h...
- A2-1223 — HkRebalancePlanCommunicationV2Projection: Should we change this to use `RebalanceCompletedThresholdBreachCommunicator`?
- A2-1234 — InvestmentRequestTopicSubscriberV3: Should we also use `UpdateFundingInstructionsCmd` here?
- A2-1235 — InvestmentRequestTopicSubscriberV3: There can be eventual consistency delay here no? So might end up with stale version of transaction in the repository
- A2-1236 — InvestmentRequestTopicSubscriberV3: Looks like we need separate cmd to update fxConversionRequestId / deposit transactionId without changing status?
- A2-1237 — InvestmentRequestTopicSubscriberV3: Are we missing a change for `InvestmentRequestHelper` to top up deposit transaction id?
- A2-1244 — BrokerCashTransactionTopicSubscriberV3: What will happen to normal deposit? They will flow straight from broker → transaction, without any records in TradingAccountEntity right?...
- A2-1245 — BrokerCashTransactionTopicSubscriberV3: Do we need handle the same for deleted/rejected? I suppose we don’t want to wipe out TradeDetails even for those statuses?
- A2-1308 — Review: In Invest, for new tables \+ projection, we typically include version in the name of the classes, so that there are clean code changes in the PR: 1st PR to add new versi...
- A2-1310 — D56 abort rejected withdrawal dividend: 187.44 switches to cash balance; 12.56 reinvestment remains unchanged
- A2-1311 — DividendTopicSubscriberV3: Added comment for the AbortCmd… from transaction pov, it doesnt need to know about the possible cases of pref here. In future, we might support for ca...
- A2-1352 — RebalancerConfigJdbcProjection: Should we make this column required, and default to event timestamp if missing from evt?
- A2-1395 — GoalModificationWithPortfolioSimulationRestrictionDpmSpec: Feels like lots of duplicated tests in here, while missing some other cases specific to DPM
- A2-1408 — AdvisoryApplication: We should be able to move both this and `productPortfolioJdbcRepository` to base `ServiceComponents`. Can use wire instead of new keyword.
- A2-1412 — AdvisoryApplication: I haven’t checked fully, but I think the pattern I’ve seen so far, the kafka subscribers are wired and started last. So we keep `setupBaseSubscribers` as la...
- A2-1414 — SubscriberHelpers: Avoid Option.get in general. I guess here you can write it as
- A2-1415 — SubscriberHelpers: Maybe return None here
- A2-1447 — package: goal-api `OneTimeInvestmentRequestV2(fundingInstructions, Option[indicativeAmount])`
- A2-1454 — Review: Can we also delete the cassandra readside \+ projection too :pray:
- A2-1473 — GoalCreationFromPortfolioSimulationRestrictionSpec: I’m thinking this test is quite big. Should we consider split into 2 files?
- A2-1487 — Review: Existing naming in `transaction` svc is a bit confusing \(introduced by the multiple versions of entity migration\)
- A2-1488 — TransactionV3JdbcProjectionV2: It’s version numbers for 2 different things. Can let them be independent
- A2-1489 — PlanTopicSubscriber: Rare but let’s change this to 1
- A2-1490 — RedemptionRequestTopicSubscriber: Same here
- A2-1491 — TradeTopicSubscriber: Hmm I’m surprised we have so many `parallelism` = 2 in investment svc without the safeMapAsync… [person] speed should be fine here, we should just change t...
- A2-1493 — FlowUtils: ```
- A2-1494 — PlanTimeSeriesTopicSubscriber: Do we really need the context for the payload \+ identifier mapping?
- A2-1565 — RebalanceTopicSubscriberV3: Why name this as `isForceDeleted` while its logic is just `isDeleted`?
- A2-1566 — TransactionJdbcProjectionV2: Let’s not mix the naming, it can be confusing for future readers:
- A2-1568 — TransactionJdbcProjectionV1_3: Do we want similar cutOff for the V2 projection? Or it’s ok cuz there’s not much data in HK?
- A2-1569 — JdbcSchema: You still need to create V2 and V1\_3 until we completely remove the 2 projections right? Otherwise this will scream if we deploy to new dynamic env \(or if it’s res...
- A2-1572 — RebalanceTopicSubscriberV3: I mean this method derive the deleted status \(or not\) from txn data, nothing about force or not.
- A2-1580 — RebateDistributionRequestJdbcRepositoryTest: Is it duplicate test? It’s not mockDb btw, it’s real embedded pg
- A2-1585 — TransactionTypes: We can let the old `FxConversionDetails` having optional accounts, as we are migrating away from this v1 model.
- A2-1587 — FxConversionRequestTopicSubscriberV2: Let’s use `BrokerAccountId.fromFxWalletBrokerAccountDto`
- A2-1601 — RebateDistributionJdbcEventProcessor: Should we use timestamp from the evt, and if not available use evt timestamp offset instead?
- A2-1602 — RebateDistributionJdbcEventProcessor: Consider log full event and its offset maybe. That will help us identifying problematic event faster when this error happens.
- A2-1630 — Review: * advisory.corporate\_customer\_v2
- A2-1631 — PlanTimeSeriesTopicSubscriber: Maybe 4 as well?
- A2-1632 — PlanTimeSeriesTopicSubscriber: I think planId is available in trait `PlanMarketValueMsg`
- A2-1635 — RegionalCustomerTopicCustomer: Not sure if we should check holdings or ongoing transactions…. I think it’s manual check today by POps, but if they somehow miss it, it would be p...
- A2-1636 — RegionalCustomerTopicCustomer: Not possible as of now I think. I mean if any chance of mistake, at least on our side, we only touch the schedules, which are easy to reinstate. A...
- A2-1637 — RegionalCustomerTopicCustomer: Update logging msg
- A2-1638 — RegionalCustomerTopicCustomer: Entity is keyed by goalId so would it be better to increase parallelism for goals to 4, keeping parallelism for plans at 1?
- A2-1639 — RegionalCustomerTopicCustomer: Btw should we use jdbc readside instead? Eventually we want to get rid of these cassandra readside for general query needs
- A2-1649 — PreferredLocalLookupHelper: Can we add a base trait `PreferredLocalLookupHelper` too?
- A2-1651 — Review: I mean we still have to write this same method in every communication projection x every service.
- A2-1679 — RedemptionRequestTopicSubscriberV3: Let’s make this specific to fee redemption only, and move the `request.feeChargeDetails.isDefined` to require clause
- A2-1680 — RedemptionRequestTopicSubscriberV3: Hmm I don’t remember seeing this in prev version? I thought we said we only calculate the chargedByCash and chargedBySell amount without touc...
- A2-1681 — RedemptionRequestTopicSubscriberV3: Isn’t your 1st screenshot showing 20.91 in L1?
- A2-1682 — RedemptionRequestTopicSubscriberV3: Right, sorry I missed that… somehow I thought we only call only for fee \(and hence even suggest making it specific with require clause :see_...
- A2-1697 — BaseRedemptionCommunicationV2Projection: [person] can you check with [person] on how this TAA field is used? Feels very wasteful to lookup portfolio service here, while `planDto...
- A2-1698 — BaseRedemptionCommunicationV2Projection: Is it ok for us to change for this email too?
- A2-1699 — BaseRedemptionCommunicationV2Projection: We should just log error and move on instead of throwing and potentially block the projection here
- A2-1700 — BaseRedemptionCommunicationV2Projection: Can we confirm that it’s correct to use confirmedAt as trade date here? My understanding is Alts redemption settlement is extra long, so...
- A2-1701 — BaseRedemptionCommunicationV2Projection: Ah we already filter for this in the main handle method
- A2-1702 — BaseRedemptionCommunicationV2Projection: Not sure how this metrics field is used. Can you also confirm if we need new name for Alts?
- A2-1704 — BaseRedemptionCommunicationV2Projection: It’s the same thing but we have some utils in OptionUtils to make this a bit more fluent \(I think\)
- A2-1709 — CustomerAdvisoryProfileDataV2: Identical to `CustomerAdvisoryProfileData` with extra 3 fields `annualIncome` / `liquidNetWorth` / `craQuestionnaire`. Same for the V2 tables.
- A2-1711 — CustomerAdvisoryProfileJdbcEventProjectionV2: Yea this should give us zero impact for now, cuz we don’t expect `ExpiryDateOverriddenEvt` or `CraExpiredEvt` in prod yet. And data...
- A2-1776 — AltsLcoCalculationMatrix: Feels like this and the scoreCalculator can be refactor a bit more to remove duplicate code, but ok we can iterate on this later
- A3-0006 — InstrumentMStarAddMarketDataTable.scala: Miscomm then lol. I guess because you wanted to update annual yield via processor?
- A3-0015 — ServiceLogicImpl.scala: will need your help to change this to use readside after yours are in
- A3-0016 — RecurringInvestmentScheduleHistoryDataEventProcessor.scala: Let’s also remove the existing `ReadSideId`?
- A3-0024 — InstrumentJdbcEventProcessorV2.scala: use CassandraProjectionManager
- A3-0025 — InstrumentJdbcEventProcessorV2.scala: follow the pattern we have in other services with JdbcSchema
- A3-0026 — InstrumentV2JdbcDbHandler.scala: We don’t really need transaction for readside so we can inject db here, and return Future… it’s easier to use and mock in test if needed
- A3-0027 — InstrumentJdbcEventProcessorV2.scala: It’s just a bit cleaner to group them together, both those with event processor and those pure CRUD
- A3-0028 — InstrumentDbEventProcessorNew.scala: we can remove already. BQ is currently using pg instruments\_v4
- A3-0033 — DailyMvPersistenceHelper.scala: Extract this logic out of `PlanTimeSeriesTopicSubscriber` and let it handle updating both dailyMV and dailyMVAuditEntry tables
- A3-0056 — BrokerCashTransactionTopicSubscriberV3.scala: transactionV3 is good enough I think… no need to repeat the topic in group name
- A3-0057 — BrokerCashTransactionTopicSubscriberV3.scala: Can we add some log here, info is good enough I think, saying that we are skipping because txn is already deleted
- A3-0086 — TransactionV2AccountSerializerRegistry.scala: I suppose we don’t migrate state because we only need events to move to V3?
- A3-0089 — Staging skips are temporary unblockers; remove default skips and observe issues
- A3-0095 — UpdateCurrentAssetAllocationCmdHandler.scala: For RPC, goal svc will send a TAA updated msg which will trigger this cmd. However, we will skip it, cuz we change the flow to trigger both RPC/Breach
- A3-0108 — Estimated fee resend: forceResend plus customer include/exclude sets, not amount-derived comm ID
- A3-0116 — RPC endpoints intentionally differ: customer readside versus goal entity consistency
- A3-0145 — FeeManager.scala: We call per request here, so decide to consolidate tax details in the event processor instead by calling TaxHelper
- A3-0148 — MV-before-plan-topic race creates planProfile with wrong planCcy; remove early creation
- A3-0183 — CustomerTransactionMigrationEventProcessor.scala: Hmm I guess it’s ok, but we will lose the requestedBy and reason in these events
- A3-0228 — DetectExpiringRecurringInvestmentCmdHandler.scala: Why don’t we just send the communication directly from the scheduler? I’m thinking this is really not an event for GoalEntity - no logic in cmd handle
- A3-0229 — ExpiringRecurringInvestmentScheduleProcessor.scala: I suppose we can extract the communication bits to another class - which has Base containing the methods to send out various notification types, and S
- A3-0243 — PlanCommunicationV2EventProcessor.scala: Can we extract this communication sending to separate method so it’s easier to follow? ``` event.removalReason match { case Some(RecurringInvestmentSc
- A3-0256 — Schedule history without key duplicates on event retry
- A3-0257 — RecurringInvestmentScheduleJdbcEventProcessor.scala: `upsertPlanRecurringInvestmentSchedule` will skip if schedule is None? don’t we need another method to delete in dbHandler?
- A3-0259 — : Can we add tests too please, for both processor and repository
- A3-0263 — Schedule deactivation domain events belong in command/PlanProjection; JDBC writes only
- A3-0264 — Mutable endingOnDate/toBeExpiredOn indices: catch up projection before adding indices
- A3-0265 — UpdatedEvt old/new inserts and offset-commit failures: duplicate windows and PK alternatives
- A3-0267 — RecurringInvestmentScheduleJdbcEventProcessor.scala: In theory again, since we don’t actually care about this table from application side, we should just add another topic producer that re-publish all me
- A3-0268 — BaseInvestmentCommunicationEventProcessor.scala: Since we are already handling cancelled evt here, I think no need to go back to common method `getBrazeCampaignIdByRegion` to handle all event types a
- A3-0292 — Producer persistence offset versus consumer message timestamp metric naming
- A3-0293 — Kafka CreatedTime lag includes Akka persistence delay and poll interval
- A3-0309 — PlanCommunicationV2EventProcessor.scala: Fallback to event timestamp instead of now?
- A3-0310 — PlanCommunicationV2EventProcessor.scala: So we’re ok to fire and forget here?
- A3-0313 — Old replayed events missing createdAt should use event timestamp to avoid fresh communication
- A3-0314 — PlanCommunicationV2EventProcessor.scala: Same here, let’s also fallback to event timestamp
- A3-0316 — RecurringInvestmentScheduleHistoryJdbcEventProcessor.scala: Can we just use data from event itself?
- A3-0319 — Schedule history created/stopped rows have no link ID: data-team join expectations
- A3-0321 — BrokerMccyAccountCreatorProcessor.scala: using projection makes sense, cuz it’s all internal to broker svc. No need extra hop to Kafka. Other events would be filtered out anyway so it should 
- A3-0323 — Three-MCCY-broker creation: partial success, retry and stale active-account readside
- A3-0324 — ServiceLogicImpl.scala: If topic producer also misses then we need to either republish the event, or also sync trading with rebalance. In the case I need right now, only read
- A3-0325 — TAA has four entities/two BQ copies; remove rebalance TAA entity and janitor remaining three
- A3-0344 — Upstream optional fee fields remain optional for V1-to-V2 migration
- A3-0362 — WithdrawalTopicSubscriberV2.scala: Log error and skip? There’s nothing you can do if data is wrong?
- A3-0364 — RebateDistributionTopicSubscriberV2.scala: just log error and move on right? why hard block here and get stuck on a poison msg?
- A3-0381 — Future schedule startingDate PK collision across01Aug/05Aug/15Aug updates tolerated for CKAE
- A3-0388 — New updatedAt missing on old events: ele.timestamp rather than replay-now
- A3-0389 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Should we also handle `InvestmentPlanDeactivatedEvt`?
- A3-0390 — InvestmentScheduleActivePeriod.scala: Just a note, missing here might be caused by different issues, not just missing ack on CKAE
- A3-0391 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Here we use latest data of investmentPlan, so you may see a schedule created here with an already deactivated plan. Not sure but now I’m thinking if w
- A3-0392 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Better to check if `recurringInvestmentSchedule` exists then upsert, then recurringAmount/Interval won’t be optional
- A3-0393 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Same for customerId/tradingAccountType/ccy. If we can remove them and join on planId instead, then we can make this projection much faster as it doesn
- A3-0395 — InvestmentScheduleActivePeriodJdbcRepository.scala: I see that `deActivatedAt` is at plan level, but `markDeletionByPlanId` is called when schedule is removed, nothing to do with plan deactivation
- A3-0396 — InvestmentScheduleActivePeriodTable.scala: \(3\) will override \(1\) because they have same pk - but ok, we establish it’s ok in context of CKAE
- A3-0398 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Actually, here you should use the `recurringInvestmentSchedule` inside the investmentPlan of the event, instead of fetching latest from entity Also, i
- A3-0400 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Use `event.updatedAt` if available
- A3-0401 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: the better syntax would be ``` _ <- investmentPlan.recurringInvestmentSchedule match { case Some(schedule) => repository.upsert(...) case None => Futu
- A3-0431 — : WIP: * tested the backfill endpoint itself → works * pending: * wait for new version of readside → update query to filter * in prod it’s huge amount o
- A3-0437 — ThresholdBreachJdbcEventProcessor.scala: Use cassandra projection
- A3-0438 — RebalancingProcessor.scala: This is used in two more places it seems… `ThresholdBreachReportGenerator` and `RebalancePlanProjection`. Why don’t we switch for them too?
- A3-0447 — Empty generated orders before/after Lagom removal: log+Done with no event preserves outcome
- A3-0453 — UpdateTradeWithManualOrdersCmdHandler.scala: I’m not changing the `UpdateMarketDataCmdHandler` side as it seems to “expect” it to happen in its info logging ``` (perhaps the events got replayed b
- A3-0458 — WithdrawalTopicSubscriber.scala: Should we go to entity if not found in readside?
- A3-0479 — package.scala: It’s called in projection… tmr we might go to a region that does not require tax for example.. it’s up to projection to decide…
- A3-0507 — ChargeApplication.scala: Can we follow the naming convention to call it Projection?
- A3-0509 — FeeChargeRequestJdbcEventProcessorV5.scala: Hmm so we also update these planProfile too. I guess it’s fine cuz this will look up latest planProfile, but still feel very expensive :sweat_smile:
- A3-0516 — Readside TAA retry proposal5s-to10s/3 retries assumes no repeated TAA-updated event
- A3-0529 — Idempotent fee projection handlers with noop-catch-up then new-flow second release
- A3-0530 — FeeManager.scala: integrate with your exemption logic here, and full redemption charge below
- A3-0531 — Tax calculation for lag spanning GST boundary: date-aware proposal explicitly deferred
- A3-0532 — commands.scala: Just to make sure we don’t wrongly override existing data in case the cmd is called twice, unless the force flag is set \(cuz it will be called via pr
- A3-0534 — InvestmentTransferEventProcessor.scala: We need to return Future to chain it here. Otherwise, event processor won’t wait for investOnce and `NotifyInvestmentProcessInitiatedCmd` to complete 
- A3-0571 — Only transient errors should throw in EventProcessor/TopicSubscriber to avoid stuck data errors
- A3-0592 — Investment owns pending-investment communication after broker virtual-account update
- A3-0597 — BrokerAccountTopicSubscriberHandlers.scala: 12 or 1? Also do you think it’s better to filter timestamp in the subscriber?
- A3-0603 — FeeChargeRequestProjection.scala: If cash reservation fails, we will log this error and delete the fee charge request. We would have separate dashboard/admin screen to keep track of wh
- A3-0604 — Alts cash-reservation remote call in projection; Kafka request/result ideal lacks trading events
- A3-0617 — HkRedemptionCommunicationV2Projection.scala: This seems almost identical to SG, except for the templateId - which both can be set in same `localeToTemplateId` map as well. I guess we keep them du
- A3-0622 — PlanTimeSeriesTopicSubscriber.scala: I can drop the cache For accountingCcy, making this subscriber aware of which ccy is a bit leaky I feel… basically, when we receive MV update from a p
- A3-0624 — PlanTimeSeriesTopicSubscriber.scala: Oh this cache is just to store the goalType by goalId - so that we avoid constantly looking up from DB or entity when we have MV updates. I think it’s
- A3-0639 — JdbcSchema.scala: We can’t drop until data team has moved
- A3-0654 — ContractNoteNotificationManagerHK.scala: Ok this doesn’t look right. Contract note notification should be per order. So one `RebalanceRequestOrderSettlementAssumedMsg` should yield exactly 1 
- A3-0655 — ContractNoteNotificationManagerHK.scala: And if we just need 1 order, I think we can drop the instrument cache and just query instrumentSvc directly
- A3-0656 — ContractNoteNotificationManagerHK.scala: If we throw on this corrupted msg, the subscriber will be stuck
- A3-0706 — Missing PlanSubscriber: inactive fine, active requires manual investigation/add-back
- A3-0712 — PlanTimeseriesTopicSubscriber.scala: How about ``` _ <- maybeLatestStoredMV match { case Some(latestStoredMV) if latestStoredMV.updatedAt.isAfter(msg.updatedAt) => logger.info("Skipping..
- A3-0715 — ServiceLogicImpl.scala: it is added as part of FHC. Once we rewrite the logic, I think we should separate the concerns: 1. update the MV projection always 2. afterwards, chec
- A3-0716 — PlanTimeseriesTopicSubscriber.scala: Yup, just normal upserting projection data
- A3-0717 — MV projection upserts every latest message before rebalance checks; same-group migration
- A3-0718 — ProjectionMarketValueData.scala: we normally name `XXXProjectionData`
- A3-0740 — Rebalance cash-release timing: pending-MV double-count window until buy export
- A3-0741 — HkRebalanceTopicSubscriber.scala: Contract note events if any should be at order level. We should not use the same message `RebalanceTradeSubmittedExternallyMsg` which is at whole trad
- A3-0742 — HkRebalanceTopicSubscriber.scala: We might update to assumed/confirmed amount if we want to. However, the difference won’t be too huge. I don’t implement it here yet because as of toda
- A3-0743 — HkRebalanceTopicSubscriber.scala: We “hope” timeseries would have increased the pending rebalance buy, not assumed MV
- A3-0744 — HkRebalanceTopicSubscriber.scala: the order level messages only applicable for contract notes change. For this CR flow, we care about the order level messages from timeseries. They are
- A3-0746 — New consumer group starts latest and may miss lagged messages during rollout
- A3-0764 — TransactionFxConverter.scala: Can we change the logging to be clearer that “no fx rate found for ccypair \+ date”. Asking marketdata svc is fine, but more important is we need to f
- A3-0767 — Auto FX sync tradeoff: stale fallback cached for a day versus repeated missing-rate sync
- A3-0781 — FxRateHelper.scala: Should we invalidate the cache after this sync so that we reload fresh rate?
- A3-0791 — StatementMetadataForUobkhGenerationScheduler.scala: So if it runs successfully then restarts due to whatever reason within the 3hr window, we will run again?
- A3-0819 — RedemptionCommunicationV2EventProcessor.scala: In investment svc, it seems we added Base event processor for anything common. And hk/sg for region specific communication
- A3-0820 — RedemptionCommunicationV2EventProcessor.scala: I suppose each region can has its own `*CommunicationV2Projection/EventProcessor`… so that the context is clear when one looks at the class. If there 
- A3-0822 — Recurring failure email: actual reason, event-domain coupling and direct-publish deferral
- A3-0836 — : I guess this one we will add a sync to update existing plans?
- A3-0863 — SgServiceLogicImpl.scala: Why don’t we read from entity here?
- A3-0864 — SgServiceLogicImpl.scala: Ah this is just to compare between charge entity and charge readside? I think we can skip this, cuz we will anyhow fetch from entity and write again -
- A3-0867 — SgServiceLogicImpl.scala: Ok I see same wrong logging in subscriber too :grimacing:
- A3-0882 — FxRatesTopicSubscriberV2.scala: We are writing to DB only, so I think we can just dump as in \(stay true to projection\). I think we have this logic last time because it was via enti
- A3-0883 — FxRatesTopicSubscriberV2.scala: This the upsert call fails, the whole future will still error, and the subscriber will retry. The `.map(_ => Done)` purely means “we are ignoring the 
- A3-0886 — AdvisoryApplication.scala: Don’t we need subscriber to customer/onboarding topic to populate the `customerProjectionDataJdbcRepository`?
- A3-0891 — Macwire inside Future sometimes misses subscribers; possible SlickReadside relation unproven
- A3-0892 — Customer onboarding/projection assumptions behind expected advisory-profile existence
- A3-0893 — Near-cutoff onboarding CRA without completion may cross VC age outside customer projection
- A3-0894 — CustomerProjectionDataJdbcRepository.scala: If this gets expensive, we should consider adding another readside table for advisory profile containing only the latest entry
- A3-0895 — CustomerAdvisoryProfileJdbcRepository.scala: Hmm alright, maybe another readside table containing only latest is worth it :grimacing:
- A3-0896 — CustomerAdvisoryProfileJdbcRepository.scala: And in that new table, we can consider extract this field as an optional column, to make query simpler
- A3-0902 — CustomerProjectionDataJdbcRepository.scala: Also do we want to return to Optional advisory profile? NonVc suggests profile is there
- A3-0905 — CustomerPersonalDetailsTopicSubscriber.scala: Can we keep this TODO, maybe adjust it a little - since we still want to trigger recalculation if DOB changes… As of now, it always triggers
- A3-0909 — CraManager.scala: Ok customer projection table will have data from onboarding entity, just no sync endpoint… So the sync needs to check customer status somehow
- A3-0911 — CustomerProjectionDataJdbcRepository.scala: Keep Optional because readside might lag
- A3-0915 — Missing profile readside: warn and force inclusion, while expired stays until retake
- A3-0919 — CraManager.scala: Hmm this will emit `ExpiryDateOverriddenEvt` which is not what happening here… I think we will need another pair of cmd/event
- A3-0920 — Stale onboarding DOB can overwrite newer customer DOB: version/timestamp TODO
- A3-0928 — CRA expiry override versus check: date-update event separate from expired-flag event
- A3-0936 — SgDividendService.scala: I’m not really sure. But trading subscribes to it for old flow..
- A3-0938 — DividendApplication.scala: The lags are tracked based on offsets only. So if offset table is not created, nothing will work…
- A3-0940 — EmailProviderData.scala: I’m a little confused on this. Do we want to serialize `RecurringInvestmentModifiedData` directly, or via its sealed trait `SendgridTemplateData` ?
- A3-0982 — SgOnlyInvestmentCommunicationV2EventProcessor.scala: If we wire this for SG, then we will start sending email for 2 days worth of confirmed investment requests…
- A3-0983 — Missing broker virtual-account data blocks tag and may age communication past2days
- A3-0995 — SG/HK investment communication trigger ownership and deferred SG migration
- A3-1000 — CustomerAdvisoryProfileTopicSubscriber.scala: we can remove this groupId now, since we will use only 1 group. Otherwise maybe rename it
- A3-1001 — HkCustomerTopicSubscriber.scala: If you want to name the group, at least put `compliance` in there so we can tell easily which service is the subscriber
- A3-1031 — HkInvestmentTopicSubscriber.scala: We don’t have any timestamp field from `InvestmentRequestDto` ? what if this subscriber lags and we will use wrong timestamp?
- A3-1034 — Investment projection timestamps differ by OrdersGenerated/Cancellation/ExternalSubmitted message
- A3-1036 — HkInvestmentTopicSubscriber.scala: Use max order’s createdAt?
- A3-1037 — HkInvestmentTopicSubscriber.scala: Use max order’s createdAt?
- A3-1040 — CustomerCraUpdatedLogic.scala: Ah I should have added the timestamp in the event :see_no_evil:
- A3-1089 — : I understand we can potentially reuse existing event processor because: * in HK, it’s brand new so we start from scratch * in SG, we don’t process old
- A3-1090 — Projection transient retryWARN versus persistent lag threshold1hr and Sentry flooding
- A3-1091 — DividendCommunicationV2EventProcessor.scala: It’s legit to distribute dividend with infoDate in the distant past. Why don’t we filter using createdAt field instead? Also, just to confirm, we want
- A3-1093 — AutoSellDownDividendCommunicationV2EventProcessor.scala: AutoSellDown is a different requirement \(automatically redeem the dividend, due to plan already empty for example\) Can we name this `BrokerAccountDi
- A3-1094 — DividendCommunicationV2EventProcessor.scala: Meaning if somehow this event processor lags long enough, we don’t need to inform customer? Also do we have requirement to use infoDate too? Why can’t
- A3-1101 — PlanCommunicationV2EventProcessor.scala: If we throw here, the event processor will get stuck. And given we can’t practically modify event, should we just log error and move on?
- A3-1120 — Ack compensation/recon alternative tolerates eventual correction unlike CR earmark
- A3-1149 — EdgeQueryTradingRestrictionLogic.scala: This one is good example to check because we use data returned from timeseries
- A3-1156 — : Will do the following in separate PR: * scheduling to trigger recon endpoint * Slack integration * add timestamp to BuyEarmark to help reduce prematur
- A3-1161 — DocumentTopicSubscriber.scala: So the only thing we need from document service is this documentId? Should report service just publish to communicate in `StatementDataGenerator#creat
- A3-1162 — StatementDataGenerator has documentId+statement after PDF; avoid topic relookup for comm
- A3-1176 — RedemptionRequestTopicSubscriberV2.scala: Hmm if this validation fails, the kafka subscriber will forever stuck..
- A3-1270 — BrokerCashTransactionTopicSubscriberV2.scala: I guess it doesn’t happen at all, hence we never run into this stuck issue. Let’s log error and move on - since there’s nothing `transaction` service 
- A3-1284 — ChargeApplication.scala: This one looks strange. How is it possible that this one is lazy val in SG today :open_mouth: I guess because it’s wired in `ServiceLogicImpl` ? Seem 
- A3-1332 — Measure goal-readside lookups before adding local eventually-consistent projections
- A3-1355 — transactionTypes.scala: on point \(3\), it’s not about losing data. Old data is still there in events, we just want latest snapshot in State \(ideally\). From readside point 
- A3-1366 — ReadSidePersistenceComponentsWithKamon already wraps CassandraReadSide
- A3-1373 — RecommendedPortfolioChangePageLoader.scala: When would this be not found? If there are legit cases, then we need to determine how to handle them instead of throwing exception…
- A3-1376 — InstrumentMarketDataEventProcessor.scala: Just thinking out loud… if we plan to migrate to use Kafka for all events in this processor, do we maybe want to use TopicProducer instead?
- A3-1417 — CraManager.scala: I’ll add the Jdbc event processor \+ repository to query for this bit separately… PR is getting too fat now
- R-3314 — Exclude the latest CRA submission from past results while readside may still lag
- R-3336 — PlanTimeSeriesSubscriber: proposed mapAsync(1) without throttle before finding the unawaited simulation
- R-3337 — safeRenewProjectionForCustomer is started with a value binding and not awaited
- R-3338 — Decouple MV draining from simulation with a separate retry/throttle/conflate topic proposal
- R-3376 — At some point, I guess we should split PlanProfile out of Entity. Local cache built from Kafka should just be updated directly, no need to maintain event t
- R-3402 — PlanEventProcessor ServiceClient dependency moves wiring from Components to Application
- R-3403 — Why did we add this error logging only for `PlanRecurringTransferScheduleCreatedEvt`? This should be blocked by the changes in GoalServiceImpl already righ
- R-3419 — Since `dailyFeeJdbcRepository` is deprecated, I’ll skip updating it here to keep the response of `FeeGenerator#generatePlanFeeForFullRedemption` simpler
- R-3420 — `FeeGenerator#generatePlanFeeForFullRedemption` is not “safe” and would propagate any exception. Unlike `FeeGenerator#safeGeneratePlansFeeForCustomer` whic
- R-3423 — Yep, `RedemptionRequestWaitingForFeeChargeMsg` only arrived after when `ConfirmSettlementCmdHandler` handled the order\(s\) confirm settlement
- R-3424 — Replayed fee must match the already charged period; conflicting extra fee needs investigation
- R-3445 — PDF upload sends email before documentId persistence; SFTP widens the duplicate window
- R-3455 — Maybe we don’t need parallelism = 2 here, since it’s always same entity
- R-3475 — Initial proposal keeps old Plan writes while a separate new Plan processor populates V1
- R-3477 — Identical to `GoalTable` except for version bump. We want to ensure consistency between Goal and Plan tables, hence update them together in same JdbcEventP
- R-3478 — Initial processor split is withdrawn so Goal and Plan update together for consistency
- R-3479 — Identical to `GoalJdbcEventProcessor` except using V1 DBHandler \+ V1 readsideId
- R-3480 — We also switch to use CassandraReadSide instead of SlickReadSide for the offsetstore for more reliability.
- R-3500 — Yup as long as readiness probe fails by then, pod won’t receive any more traffic. However, for event processor flow, I’m not sure if Lagom knows to re-assi
- R-3501 — Proposal to recover force-rebalance failure after successful TAA update because a later topic message can trigger rebalance
- R-3517 — Added `Deleted` to the cases in `deleteRelatedTransaction` I see `DeleteCmd` is already handled correctly by the entity if in `Deleted` state
- R-3527 — I mark this deprecated, and will remove after we verify everything is fixed in prod. For same reason, I will reuse existing `DividendReinvestedEvt` since t
- R-3528 — No we sync only Confirmed ones. Assumed dividends \(if any\) would eventually be confirmed, and get processed by new logic
- R-3555 — I think it’s better to let consumer\(s\) have to chance to decide what to do with missing data - rather than throwing
- R-3556 — If you prefer Exception instead, because say you expect caller to always call with valid ID… then code is little cleaner to read if we return Future.failed
- R-3557 — The method signature returns List of stats, so maybe it is semantically better to return empty list instead throw exception if not found?
- R-3558 — Portfolio stats exact-ID lookup and filter lookup both produce a List response
- R-3560 — Question… do we need to change the consumer group / reset current group’s offset so that we re-process the kafka messages again? Or is there a way to re-pu
- R-3578 — Hmm.. this `event` is used as `event.Tag.forEntityId(entityId).tag` which refer to this singleton ``` object CustomerTransactionManagerEvt { val NumShards 

## Full source cases

## A1-0011 — Remove code in CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> remove

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Target unspecified in comment; inspect hunk before applying removal.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:11 · comment 823005056 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:11 · comment 823005056 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4.scala`

**Explicit source context (hunk):**

> +                  r.maybeRiskProfileExpiryDate
> +                )
> +              }.update(
> +                updatedProfile,
> +                Some(updatedProfile.riskProfileStatus),
> +                Some(updatedProfile.expiryDate)
> +              )
> +            }
> +

## A1-0012 — Expiry events accept optional lastUpdatedTS and use latest only if absent

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Add optional lastUpdatedTS to Expiry events. If exist then match, else use latest

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:12 · comment 823006415 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:12 · comment 823006415 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala`

**Explicit source context (hunk):**

> +  ): Future[Unit] = {
> +    val latestAssessment = customerAdvisoryProfileAssessments
> +      .filter(_.customerId === customerId)
> +      .filterOpt(assessmentUpdatedTS)(_.lastUpdatedTS === _)
> +      .sortBy(_.lastUpdatedTS.desc)
> +      .take(1)
> +
> +    val updateAction = latestAssessment.result.headOption.flatMap {
> +      case Some(data) =>

## A1-0013 — CRA snapshot handler updates target row idempotently

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileSnapshotJdbcProjectionV4.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Yes the handler will update the targeted row idempotently

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:13 · comment 823073674 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileSnapshotJdbcProjectionV4.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:13 · comment 823073674 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileSnapshotJdbcProjectionV4.scala`

**Explicit source context (hunk):**

> +  private def handleCustomerAgeCapturedEvt(entityId: String, event: CustomerAgeCapturedEvt): Future[Unit] = {
> +    dbHandler.upsertAssessment(CustomerAdvisoryProfileAssessmentData.fromCustomerAgeCapturedEvt(UUID.fromString(entityId), event))
> +  }
> +
> +  private def handleExpiryDateOverriddenEvt(entityId: String, event: ExpiryDateOverriddenEvt): Future[Unit] = {
> +    dbHandler.updateExpiryDate(UUID.fromString(entityId), event.currentAssessmentUpdatedTS, event.riskProfileStatus, event.expiryDate)
> +  }
> +
> +  private def handleCraExpiredEvt(entityId: String, event: CraExpiredEvt): Future[Unit] = {

## A1-0014 — Assessment history PK is customerId and lastUpdatedTS

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcProjection.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Rows cannot share the same timestamp

**Source-preserving request, proposal, or question:**

> pk is `(customerId, lastUpdatedTS)` - they can’t share same TS

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:14 · comment 823078089 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcProjection.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:14 · comment 823078089 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcProjection.scala`

**Explicit source context (hunk):**

> +    dbHandler.upsert(CustomerAdvisoryProfileAssessmentData.fromCustomerAgeCapturedEvt(UUID.fromString(entityId), event))
> +  }
> +
> +  private def handleExpiryDateOverriddenEvt(entityId: String, event: ExpiryDateOverriddenEvt): Future[Unit] = {
> +    dbHandler.updateExpiryDateOfAssessment(UUID.fromString(entityId), event.currentAssessmentUpdatedTS, event.riskProfileStatus, event.expiryDate)
> +  }
> +
> +  private def handleCraExpiredEvt(entityId: String, event: CraExpiredEvt): Future[Unit] = {
> +    dbHandler.expireAssessment(UUID.fromString(entityId), event.currentAssessmentUpdatedTS)

## A1-0015 — Complex product acknowledgement strictly follows assessment

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Yes, complex product ack strictly comes after assessment

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:15 · comment 823084645 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:15 · comment 823084645 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4.scala`

**Explicit source context (hunk):**

> +          data.maybeRiskProfileExpiryDate,
> +        )
> +
> +      case None =>
> +        customerAdvisoryProfiles += data
> +    }
> +
> +    validateUpdatedRows("upsertAssessment", database.run(updateAction.transactionally))
> +  }

## A1-0016 — CRA snapshot stores queryable derived columns while history updates only advisoryProfile

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> The snapshot table has the derived columns since we need to query on them. The history table doesnt have those. Both update the whole advisoryProfile

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:16 · comment 823088064 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

## A1-0017 — Patch function is already checked not to change profile lastUpdatedTS

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Already validate above that patch func doesn’t change the profile’s `lastUpdatedTS`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:17 · comment 823068721 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:17 · comment 823068721 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala`

**Explicit source context (hunk):**

> +              customerAdvisoryProfileAssessments
> +                .filter(_.customerId === data.customerId)
> +                .filter(_.lastUpdatedTS === data.lastUpdatedTS)
> +                .map(_.advisoryProfile)
> +                .update(updatedProfile)
> +            }
> +
> +          case _: VulnerableCustomerProfile =>
> +            logger.error(s"""

## A1-0018 — CRA history does not update by lastUpdatedTS alone

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We don’t update by `lastUpdatedTS` alone

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:18 · comment 823075773 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:18 · comment 823075773 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala`

**Explicit source context (hunk):**

> +            val updatedProfile = patch(profile)
> +            if (updatedProfile.lastUpdatedTS != profile.lastUpdatedTS) {
> +              DBIO.failed(new Exception(s"Failed to $patchContext: Updating lastUpdatedTS is not allowed"))
> +            } else {
> +              customerAdvisoryProfileAssessments
> +                .filter(_.customerId === data.customerId)
> +                .filter(_.lastUpdatedTS === data.lastUpdatedTS)
> +                .map(_.advisoryProfile)
> +                .update(updatedProfile)

## A1-0019 — CRA snapshot updates explicit columns to exclude complex product acknowledgement

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Yes, need to update the columns explicitly since we want to leave the complex product ack column out

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:19 · comment 823074672 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

## A1-0020 — Alert on possible CRA history corruption without blocking projection

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Replay should be rare; commenter prefers alert noise

**Source-preserving request, proposal, or question:**

> Yea replay should be rare. I’m not blocking projection here, noise alert on these potential data corruption is better I think

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:20 · comment 823085434 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

## A1-0022 — Snapshot projection V2 never persists complexProductKnowledgeAttestationDate (identified in hunk)

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileSnapshotJdbcProjectionV2.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Yes, V2 never persists this field. Already added in the comment to explain it as well

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Field not named in comment; hunk needed to identify.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.
- V2 field identity comes only from the hunk comment.

**Evidence:** anon-1.jsonl:22 · comment 823071036 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileSnapshotJdbcProjectionV2.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:22 · comment 823071036 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileSnapshotJdbcProjectionV2.scala`

**Explicit source context (hunk):**

> private def handleCraSubmittedEvt(entityId: String, event: CraSubmittedEvt): Future[Unit] = {
> -    val data = CustomerAdvisoryProfileDataV2.fromCraSubmittedEvt(UUID.fromString(entityId), event)
> -    dbHandler.upsert(data)
> +    val data = CustomerAdvisoryProfileAssessmentData.fromCraSubmittedEvt(UUID.fromString(entityId), event)
> +    dbHandler.upsert(CustomerAdvisoryProfileAssessmentData.toAdvisoryProfileDataWithoutProductKnowledge(data)) // V2 do not persist complexProductKnowledgeAttestationDate
>    }
>  
>    private def handleVulnerableCustomerProfileResultOverriddenEvt(entityId: String, event: VulnerableCustomerProfileResultOverriddenEvt): Future[Unit] = {

**Evidence:** anon-1.jsonl:22 · comment 823071036 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileSnapshotJdbcProjectionV2.scala`

**Explicit source context (hunk):**

> complexProductKnowledgeAttestationDate

## A1-0023 — Profile JDBC projection V2 never persists complexProductKnowledgeAttestationDate (identified in hunk)

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileJdbcProjectionV2.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Yes, V2 never persists this field. Already added in the comment to explain it as well

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Field not named in comment; hunk needed to identify.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.
- V2 field identity comes only from the hunk comment.

**Evidence:** anon-1.jsonl:23 · comment 823071938 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileJdbcProjectionV2.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:23 · comment 823071938 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileJdbcProjectionV2.scala`

**Explicit source context (hunk):**

> private def handleCraSubmittedEvt(entityId: String, event: CraSubmittedEvt): Future[Unit] = {
> -    val data = CustomerAdvisoryProfileDataV2.fromCraSubmittedEvt(UUID.fromString(entityId), event)
> -    dbHandler.upsert(data)
> +    val data = CustomerAdvisoryProfileAssessmentData.fromCraSubmittedEvt(UUID.fromString(entityId), event)
> +    dbHandler.upsert(CustomerAdvisoryProfileAssessmentData.toAdvisoryProfileDataWithoutProductKnowledge(data)) // V2 do not persist complexProductKnowledgeAttestationDate
>    }
>  
>    private def handleVulnerableCustomerProfileResultOverriddenEvt(entityId: String, event: VulnerableCustomerProfileResultOverriddenEvt): Future[Unit] = {

**Evidence:** anon-1.jsonl:23 · comment 823071938 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileJdbcProjectionV2.scala`

**Explicit source context (hunk):**

> complexProductKnowledgeAttestationDate

## A1-0024 — Review-pattern comparison on first commit before and after update

**Source stance:** reported-verification

**Context:**

> component: None; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> When reviewing the 1st commit alone:
> 
> ‌
> 
> Before the updated review patterns:
> 
> * wrongly flag not-switch repositories
> * didn’t not flag the event replay risk for history projection
> […incidental material or intervening source omitted…]
> ‌
> 
> After the updated review patterns \(tested 2 times\):

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Before text reports wrongly flagged not-switch repositories and literal double-negative replay-risk wording; after tested twice shown only in unavailable screenshots, so no textual success outcome inferred.

**Evidence:** anon-1.jsonl:26 · comment 823348080 · PR 14228 · 2026-07-08

> When reviewing the 1st commit alone:
> 
> ‌
> 
> Before the updated review patterns:
> 
> * wrongly flag not-switch repositories
> * didn’t not flag the event replay risk for history projection

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:26 · comment 823348080 · PR 14228 · 2026-07-08

> ‌
> 
> After the updated review patterns \(tested 2 times\):

## A1-0097 — Corrupt MV projection could suppress comms for actual breach-suggested event

**Source stance:** open-question

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/commmunicationHandlers/thresholdBreach/RebalanceSuggestedThresholdBreachCommunicator.scala; operation: [INV-5638] feat(communication, rebalance): Comms changes for NWM portfolios; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> If MV projection is somehow corrupted, we will skip sending the comms for actual breach suggested evt?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:100 · comment 820353777 · PR 14065 · 2026-07-01

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/commmunicationHandlers/thresholdBreach/RebalanceSuggestedThresholdBreachCommunicator.scala`

**Explicit source context (pr_title):**

> [INV-5638] feat(communication, rebalance): Comms changes for NWM portfolios

## A1-0559 — Auto-rebalance communication buffer may fail under projection lag

**Source stance:** open-question

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalCommunicationV2EventProcessor.scala; operation: BB-3188 auto rebalncing toggle; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I think this buffer might not be safe enough if the projection somehow has lags

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:566 · comment 776013943 · PR 13477 · 2026-03-31

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalCommunicationV2EventProcessor.scala`

**Explicit source context (pr_title):**

> BB-3188 auto rebalncing toggle

**Evidence:** anon-1.jsonl:566 · comment 776013943 · PR 13477 · 2026-03-31

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +   *   (again at the same precision as `timestampOrdering`).
> +   */
> +  def shouldTriggerFirstGoalNotification(existingGoals: List[GoalDto], currentGoal: Goal): Boolean = {
> +    existingGoals.minByOption(_.createdAt)(timestampOrdering).map(_.createdAt).fold(true) { existingMinCreatedAt =>
> +      timestampOrdering.lteq(currentGoal.createdAt, existingMinCreatedAt)
> +    }
> +  }
> +
> +  def handleGoalCreatedEvt(ele: EventEnvelope[GoalCreatedEvt]): Future[Done] = {

## A1-0560 — Use generic communication-ID helpers with explicit event and recipient seed

**Source stance:** suggestion

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/sg/SgB2BNotificationManager.scala; operation: BB-3188 auto rebalncing toggle; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Existing method names neither protect recipientId nor describe template-specific behavior

**Source-preserving request, proposal, or question:**

> These method names are quite misleading, as there’s no protection on what `recipientId` being set
> 
> Also the name sounds very generic, but it actually very specific to this rebalance pref template only.
> 
> Consider
> 
> ```scala
> getCommunicationIdForPlanEvent(emailTemplate, planId, eventTimestamp, recipientId)
> getCommunicationIdForCustomerEvent(emailTemplate, customerId, recipientId)
> ```
> 
> Within `getCommunicationIdForCustomerEvent`, if recipient is customer themselves, it’s fine to repeat the same customerId as part of the seed to generate communicationId

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:567 · comment 776005450 · PR 13477 · 2026-03-31

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/sg/SgB2BNotificationManager.scala`

**Explicit source context (pr_title):**

> BB-3188 auto rebalncing toggle

## A1-0562 — Different tags allow first-goal notification to miss both A and B

**Source stance:** observed-defect

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalCommunicationV2EventProcessor.scala; operation: BB-3188 auto rebalncing toggle; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** B persisted first; A skipped at size 1 missing A; B skipped at size>1 past buffer

**Source-preserving request, proposal, or question:**

> Goal A and B are created >1min apart. A is before B, however their IDs are on different tag so projection ordering can mix up
> 
> The following sequence is, in theory, possible:
> 
> * readside projection persists B
> * communication projection processes A: goals.size is 1 but not containing A → skip
> * readside projection persists A
> * communication projection processes B: go into else clause \(size > 1\) but gap exceeds buffer → also skip
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:569 · comment 776039557 · PR 13477 · 2026-03-31

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalCommunicationV2EventProcessor.scala`

**Explicit source context (pr_title):**

> BB-3188 auto rebalncing toggle

## A1-0563 — Choose first-goal notification by createdAt minimum instead of buffer

**Source stance:** suggestion

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalCommunicationV2EventProcessor.scala; operation: BB-3188 auto rebalncing toggle; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ```
>   /**
>     * TODO: EXPLAIN ME (may over send but should not miss)
>     *
>     * readside projection X: A -> B or B -> A
>     * commnnnn projection Y: A -> B or B -> A
>     * validate combinations + interleaving scenarios
>     *
>     */
>   def shouldTriggerFirstGoalNotification(existingGoals: List[GoalDto], currentGoal: Goal): Boolean = {
>     existingGoals.minByOption(_.createdAt).map(_.createdAt).fold(true) { existingMinCreatedAt =>
>       !currentGoal.createdAt.isAfter(existingMinCreatedAt)
>     }
>   }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Source seeks interleaving validation and says may oversend but should not miss.

**Evidence:** anon-1.jsonl:570 · comment 776067740 · PR 13477 · 2026-03-31

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalCommunicationV2EventProcessor.scala`

**Explicit source context (pr_title):**

> BB-3188 auto rebalncing toggle

## A1-0565 — Share pending-trades-stopped rebalance communication condition in base

**Source stance:** suggestion

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/commmunicationHandlers/thresholdBreach/RebalanceThresholdBreachRemovedCommunicator.scala; operation: BB-3188 auto rebalncing toggle; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** HK sends B2C; SG selects B2C or B2B by tenant

**Source-preserving request, proposal, or question:**

> Base
> 
> ```
>   override def communicate: Future[Done] = {
>     if (event.thresholdBreachRemovedReason.contains(ThresholdBreachRemovedReason.PENDING_TRADES_EXIST)) {
>       sendRebalancingStoppedEmailNotification
>     } else Future.successful(Done)
> 
>   }
> 
>   protected def sendRebalancingStoppedEmailNotification: Future[Done]
> 
>   
> ```
> 
> ‌
> 
> HK implements sendRebalancingStoppedEmailNotification to call B2C
> 
> SG impletmens sendRebalancingStoppedEmailNotification to check tenant and calls B2C or B2B
> 
> ‌
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:572 · comment 776072466 · PR 13477 · 2026-03-31

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/commmunicationHandlers/thresholdBreach/RebalanceThresholdBreachRemovedCommunicator.scala`

**Explicit source context (pr_title):**

> BB-3188 auto rebalncing toggle

## A1-0633 — Restore deprecated SMART_BETA for persisted event replay

**Source stance:** requested-change

**Context:**

> component: None; operation: Fix/noise logs; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> advisory in SG Dev stuck on old events using SMART\_BETA
> 
> ```
> Restarting stream due to failure [2354]: java.util.NoSuchElementException: No value found for 'SMART_BETA'
> java.util.NoSuchElementException: No value found for 'SMART_BETA'
> 	at scala.Enumeration.$anonfun$withName$1(Enumeration.scala:159)
> 	at scala.collection.immutable.HashMap.getOrElse(HashMap.scala:717)
> 	at scala.Enumeration.withName(Enumeration.scala:159)
> 	at com.endowus.silver.advisory.impl.entities.portfolio.models.package$ProductPortfolio$.$anonfun$advisoryTagToMetaData$2(package.scala:83)
> ```
> 
> → To keep things clean, add back the enum value and mark it as deprecated
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Multiple independent fixes retained in exact source; obsolete enum stalls replay, scale 40 causes noise, nonexistent customer stalls dev projection.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.

**Evidence:** anon-1.jsonl:641 · comment 765990137 · PR 13531 · 2026-03-11

**Explicit source context (pr_title):**

> Fix/noise logs

## A1-0636 — Missing customer in historical CKA projection logs and skips

**Source stance:** requested-change

**Context:**

> component: None; operation: Fix/noise logs; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> compliance in SG Dev stuck on old events with non-existence customerId
> 
> ```
> [temp-customer-knowledge-assessment-jdbc-handler-tenantId-v2-com.endowus.silver.compliance.impl.cka.entities.ces.CustomerKnowledgeAssessmentEvents$CustomerKnowledgeAssessmentEvent1] First attempt to process envelope with offset [TimeBasedUUID(
> […incidental material or intervening source omitted…]
> )] failed. Will retry [10] time(s). Exception: com.endowus.silver.customer.api.exceptions.CustomerSvcException: Customer [
> […incidental material or intervening source omitted…]
> ] does not exist! (404/1008 Policy Violation/Not Found)
> ```
> 
> → Handle, log error and skip instead

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Multiple independent fixes retained in exact source; obsolete enum stalls replay, scale 40 causes noise, nonexistent customer stalls dev projection.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.

**Evidence:** anon-1.jsonl:641 · comment 765990137 · PR 13531 · 2026-03-11

> compliance in SG Dev stuck on old events with non-existence customerId
> 
> ```
> [temp-customer-knowledge-assessment-jdbc-handler-tenantId-v2-com.endowus.silver.compliance.impl.cka.entities.ces.CustomerKnowledgeAssessmentEvents$CustomerKnowledgeAssessmentEvent1] First attempt to process envelope with offset [TimeBasedUUID(

**Explicit source context (pr_title):**

> Fix/noise logs

**Evidence:** anon-1.jsonl:641 · comment 765990137 · PR 13531 · 2026-03-11

> )] failed. Will retry [10] time(s). Exception: com.endowus.silver.customer.api.exceptions.CustomerSvcException: Customer [

**Evidence:** anon-1.jsonl:641 · comment 765990137 · PR 13531 · 2026-03-11

> ] does not exist! (404/1008 Policy Violation/Not Found)
> ```
> 
> → Handle, log error and skip instead

## A1-0645 — Update marketdata InstrumentTopicSubscriber condition for InstrumentDetailsUpdatedMsg

**Source stance:** open-question

**Context:**

> component: None; operation: Feat/INV-5338 v2 benchmark model; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Don’t we also need to change the condition in `InstrumentTopicSubscriber` of marketdata svc when handling `InstrumentDetailsUpdatedMsg`?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:652 · comment 752062326 · PR 13358 · 2026-02-10

**Explicit source context (pr_title):**

> Feat/INV-5338 v2 benchmark model

## A1-0724 — Trigger monthly-data refresh only on changed stitch config

**Source stance:** suggestion

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/subscribers/InstrumentTopicSubscriber.scala; operation: Feat/INV-4918 stitch data fields; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Generic instrument updates are noisy with docs/projected returns

**Source-preserving request, proposal, or question:**

> This will be very noisy with the document sync / projected return updates etc. If we intend this to be called after stitch config update, ideally we want separate event for that.
> 
> However, in view of FIO project, and we don’t want to add events yet, maybe we can change on instrument svc side to check if stitch config was changed in the upsert/override request compared to existing data, and if so, instrument svc calls marketdata svc directly to refresh monthly changes.
> 
> IIRC, marketdata svc typically fetch instrument from entity again to confirm that indeed the instrument exists before performing any sync. So this would be safe.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Separate event ideal; FIO constraint suggests direct instrument-to-marketdata call, marketdata rechecks entity existence.

**Evidence:** anon-1.jsonl:735 · comment 736704260 · PR 12946 · 2026-01-12

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/subscribers/InstrumentTopicSubscriber.scala`

**Explicit source context (pr_title):**

> Feat/INV-4918 stitch data fields

## A1-0771 — Apply change to recentEntityChanges and recentEntityChangesData

**Source stance:** requested-change

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Should be used in both `recentEntityChanges` and `recentEntityChangesData`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:783 · comment 738470561 · PR 13145 · 2026-01-14

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

## A1-0777 — Unsorted plan-keyed recentEntityChangesData has undefined context selection

**Source stance:** observed-defect

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RRTHelper.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Breaks downstream merge logic

**Source-preserving request, proposal, or question:**

> `recentEntityChangesData` returns entries keyed by planId, without any guarantee of which context it returns since we don’t sort. This will mess up with merge logic below

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:789 · comment 738488440 · PR 13145 · 2026-01-14

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RRTHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

## A1-0782 — Append only recently created plans when faking initial investment

**Source stance:** requested-change

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RRTHelper.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Recent updates can be existing plans

**Source-preserving request, proposal, or question:**

> Because of this, we need to return only recently-created plans only, not recently-updated plans. Only then it’s safe to construct fake initial investment from plan.
> 
> ‌
> 
> Otherwise we would need to fetch from investment entity again for these `planIdsFromUpstreamToAppend` \(with `fetchInitialInvestment = true` and empty `investmentRequestIds`\)
> 
> * If returns empty, indeed it’s brand new plan that hasn’t reached investment entity
> * Else, it would be an old plan, which we don’t care about
> 
> But yea cleaner to change on goal svc side

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Alternative fetch investment entity with fetchInitialInvestment true and empty IDs, but goal-side change cleaner.

**Evidence:** anon-1.jsonl:794 · comment 743548512 · PR 13145 · 2026-01-23

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RRTHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

## A1-0784 — Enable RRT by config and merge upstream in queryCustomerTransactions

**Source stance:** requested-change

**Context:**

> component: transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** No new RRT endpoint; inner query already validates customerId, so avoid duplicate methods

**Source-preserving request, proposal, or question:**

> This inner `queryTransactions` already has customerId validation. So we shouldn’t need to duplicate all these methods, since we are not adding new RRT endpoints for transaction?
> 
> We just need add a config whether RRT is enabled or not. If enabled, then additional fetch and merge with upstream in `queryCustomerTransactions`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:796 · comment 743583120 · PR 13145 · 2026-01-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

## A1-0785 — Patch/base merge may replace cancelling or orders-generated upstream with pending transaction

**Source stance:** open-question

**Context:**

> component: transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionRRTQueryLogic.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Is this wrong? Patch will override Base so if transaction svc has pending, but investment svc has cancelling/order generated, we take pending?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:797 · comment 743582116 · PR 13145 · 2026-01-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionRRTQueryLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

## A1-0789 — Resolve goal RRT plans before entityIds filter to avoid overfetch

**Source stance:** suggestion

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RRTHelper.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Current small-RRT volume accepted as okay

**Source-preserving request, proposal, or question:**

> Seeing the goalId filter here still feels a bit off. I guess since this RRT only, we don’t expect much data so it should be ok. Otherwise, I think if goalId is specified, calling get-goal-with-rrt to check its planIds, merge with input planId, and use for entityIds filter is better \(cuz we won’t over fetch\)

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:801 · comment 744756784 · PR 13145 · 2026-01-27

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RRTHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

## A1-0790 — Use InvestmentRrtCommandContext with rrtContext None instead of SystemTriggeredCommand

**Source stance:** suggestion

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/PlanTopicSubscriber.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Customer acted so retain RRT entry, exclude from recently-updated-investment filter

**Source-preserving request, proposal, or question:**

> Doesnt feel right to use `SystemTriggeredCommand` here. Maybe `InvestmentRrtCommandContext` but with `rrtContext = None`?
> 
> This way we still have rrt entry for it \(because customer did sth\), but it won’t satisfy the filter condition of “recently updated investments”

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:802 · comment 744755283 · PR 13145 · 2026-01-27

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/PlanTopicSubscriber.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

## A1-0793 — Use recentEntityChanges rrtContextFilter; returned contexts guide fetching

**Source stance:** requested-change

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/RRTHelper.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Both works but ideally we should use the `rrtContextFilter` of `recentEntityChanges` instead.
> 
> The fetcher should use the returned contexts to decide on how to fetch \(i.e. the way we use in investment svc\) instead of using them as another filter

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:805 · comment 744752539 · PR 13145 · 2026-01-27

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/RRTHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

## A1-0794 — Filter expected contexts with Option forall and empty-list wildcard

**Source stance:** suggestion

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/RRTHelper.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ```scala
> maybeExpectedContexts: Option[List[GoalRrtContext]]
> 
> rrtContextFilter = ctx => maybeExpectedContexts.forall(expectedContexts => expectedContexts.isEmpty || ctx.exists(expectedContexts.contains))
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:806 · comment 744909813 · PR 13145 · 2026-01-27

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/RRTHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

## A1-0844 — Redeemable-value readside call may need consistency review

**Source stance:** open-question

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/BaseTradingServiceLogicImpl.scala; operation: Feat/INV-5232 refactor redeemable value; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we need to worry about this readside call?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:856 · comment 738907409 · PR 13193 · 2026-01-15

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/BaseTradingServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/INV-5232 refactor redeemable value

## A1-0845 — Use non-RRT getPlanRedeemableValue

**Source stance:** open-question

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/BaseTradingServiceLogicImpl.scala; operation: Feat/INV-5232 refactor redeemable value; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Then should we use the non-RRT version of `getPlanRedeemableValue`?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:857 · comment 738911498 · PR 13193 · 2026-01-15

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/BaseTradingServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/INV-5232 refactor redeemable value

## A1-0846 — Readside getPlan mixed with RRT redemption call needs consistent choice

**Source stance:** explanation

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/BaseTradingServiceLogicImpl.scala; operation: Feat/INV-5232 refactor redeemable value; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> It’s matter of consistency. Next person reading this method will ask the same question, why getPlan from readside and then use RRT-enabled call in redemption

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:858 · comment 738912958 · PR 13193 · 2026-01-15

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/BaseTradingServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/INV-5232 refactor redeemable value

## A1-0847 — Trading projection may not need RRT change

**Source stance:** open-question

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferEventProcessor.scala; operation: Feat/INV-5232 refactor redeemable value; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we need to change this to RRT? This is already in projection of trading svc

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:859 · comment 739780654 · PR 13193 · 2026-01-16

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferEventProcessor.scala`

**Explicit source context (pr_title):**

> Feat/INV-5232 refactor redeemable value

## A1-0959 — SgCustomerServiceTopics.CustomerServiceComplianceTopic already enriched with tenant context

**Source stance:** open-question

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/CustomerTopicSubscriber.scala; operation: [INV-5146] feat(compliance): Add test cases for EIP/SIP state change subscriber and use tenant service instead of tenant provider to support service endpoint web E2E tests; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Avoid second tenant-service fetch

**Source-preserving request, proposal, or question:**

> This is only used for `SgCustomerServiceTopics.CustomerServiceComplianceTopic` only - which should have tenant context enriched in `CustomerComplianceProjectionTopicProducer`. Do we still need to change to call tenant svc again?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:974 · comment 730824796 · PR 13124 · 2025-12-23

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/CustomerTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [INV-5146] feat(compliance): Add test cases for EIP/SIP state change subscriber and use tenant service instead of tenant provider to support service endpoint web E2E tests

## A1-0970 — Use updatedAt from message payload

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/CustomerTopicSubscriber.scala; operation: [INV-5045] feat(compliance): implement state changes for sip ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can we use the `updatedAt` from the msg payload instead

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:985 · comment 724813457 · PR 13004 · 2025-12-09

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/CustomerTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [INV-5045] feat(compliance): implement state changes for sip ack

**Evidence:** anon-1.jsonl:985 · comment 724813457 · PR 13004 · 2025-12-09

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/CustomerTopicSubscriber.scala`

**Explicit source context (hunk):**

> +      } else {
> +        getCustomerPlanRecurringDetails(customerId).flatMap { plans =>
> +          if (plans.planRecurringScheduleTypes.nonEmpty) {
> +            sendEmailForSipAck(customerId, plans, msg.updatedAt, "CkaDetailsUpdatedMsg")
> +          } else {
> +            Future.successful(Done)
> +          }
> +        }
> +      }

## A1-0973 — Messages can share timestamp; communication identity needs message type or context

**Source stance:** observed-defect

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/CustomerTopicSubscriber.scala; operation: [INV-5045] feat(compliance): implement state changes for sip ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> In theory, these msg can have same timestamp as well. We need more identifiers here, maybe some context string or the msg type?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:988 · comment 724814432 · PR 13004 · 2025-12-09

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/CustomerTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [INV-5045] feat(compliance): implement state changes for sip ack

## A1-0996 — Readside SIP schedule lookup has rare creation-then-TAA-modify race

**Source stance:** explanation

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala; operation: [INV-5045] feat(compliance): implement state changes for sip ack; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Accepted normal race; customer can acknowledge dashboard

**Source-preserving request, proposal, or question:**

> These calls are going to readside, we were with using them in FE display endpoints / comms but this request flow, there can be some tricky EC cases if customer create a schedule on non-SIP TAA then quickly modify into SIP TAA.
> 
> I think it should be rare enough to treat as normal race condition, and customer still can ack on dashboard.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1012 · comment 728911007 · PR 13004 · 2025-12-18

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5045] feat(compliance): implement state changes for sip ack

## A1-1092 — Always return at least readSideResults; only RRT should time out

**Source stance:** open-question

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We discussed that we would always return at least data from `readSideResults` right? Timeout handling is only if `rrtResults` takes too long?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1109 · comment 712510118 · PR 12767 · 2025-11-11

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1095 — RRT merge must handle hard and soft deletions

**Source stance:** observed-defect

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Hard delete removes keys; soft-delete active filter applies after merge

**Source-preserving request, proposal, or question:**

> This merge logic doesn’t handle deletion correctly right?
> 
> * if entity is hard delete, we need remove the keys from merged data
> * if entity is soft delete, we need to move the filter condition \(e.g. active goal status\) outside after merging
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1112 · comment 712781906 · PR 12767 · 2025-11-12

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1099 — RRT helper distinguishes fetch failure empty/deleted and fetched data

**Source stance:** requested-change

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Caller entityLoader remains Iterable; failures log and skip ID

**Source-preserving request, proposal, or question:**

> Caller shouldnt have to worry about fetch vs deleted data here. `entityLoader` should return `Iterable[Data]` as before.
> 
> And here, this rrt helper should take care of those logic:
> 
> * if fail → log warn/error and skip that id?
> * if return empty → deleted data
> * else → fetched data
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1116 · comment 713901066 · PR 12767 · 2025-11-14

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1103 — Refresh readSideLoader on timeout

**Source stance:** suggestion

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Consider refresh `readSideLoader` if we timeout?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1120 · comment 713924875 · PR 12767 · 2025-11-14

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

**Evidence:** anon-1.jsonl:1120 · comment 713924875 · PR 12767 · 2025-11-14

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (hunk):**

> +      }
> +
> +      Future.firstCompletedOf(Seq(fut, timeoutFut)).recoverWith {
> +        case _: RRTQueryTimeoutException => timeoutHandler
> +      }
> +    }
> +  }
> +
> +}

## A1-1104 — Use data-to-entity-ID extractor to remove readside tombstones before topping up entity data

**Source stance:** requested-change

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Need Data → EntityId extractor.
> 
> From readSideData, filter out those entries having `tombstoneDate.contains(entityIdExtractor(s))`
> 
> After that, we construct Map & top up entityFetchedData

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1121 · comment 713929090 · PR 12767 · 2025-11-14

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1105 — Keep readsideData entityData and entityTombstones separate

**Source stance:** requested-change

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Tombstones are EntityId rather than record Key

**Source-preserving request, proposal, or question:**

> That means we don’t need to put both fetched & tombstone data together
> 
> ```
> entityData: Iterable[EntityData[Key, Data]]
> ```
> 
> Just put in 2 fields
> 
> ```
> RRTDate(
>   readsideData: Iterable[Data],
>   entityData: Iterable[Data],
>   entityTombstones: Iterable[EntityId] // not Key
> )
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1122 · comment 713931646 · PR 12767 · 2025-11-14

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1106 — Investment RRT groups requests by PlanId then tombstone-filters and replaces whole groups

**Source stance:** explanation

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> readside: Iterable\[InvestmentRequestDto\]
> 
> entityData: Iterable\[\(PlanId, Iterable\[InvestmentRequestDto\]\)\] \(get cmd from PlanId\)
> 
> entityTombstones: Iterable\[PlanId\] // plans having no investment requests \(e.g. all hard deleted\)
> 
> --
> 
> from readSide
> 
> → groupBy entityIdExtractor = Iterable\[\(PlanId, Iterable\[InvestmentRequestDto\]\)\]
> 
> → filter against entityTombstones \(remove by PlanId\)
> 
> → replace with entityData
> 
> → values.flatten

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1123 · comment 713935985 · PR 12767 · 2025-11-14

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1107 — Goal RRT groups by GoalId then tombstone-filters and replaces one-element groups

**Source stance:** explanation

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> readside: Iterable\[GoalDto\]
> 
> entityData: Iterable\[\(GoalId, Iterable\[GoalDto\]\)\] \(get cmd from GoalId\) \(goalDto iterable has exactly 1 element\)
> 
> entityTombstones: Iterable\[GoalId\] // hard deleted goalIds
> 
> --
> 
> from readSide
> 
> → groupBy entityIdExtractor = Iterable\[\(GoalId, Iterable\[GoalDto\]\)\] \(goalDto iterable has exactly 1 element\)
> 
> → filter against entityTombstones \(remove by GoalId\)
> 
> → replace with entityData
> 
> → values.flatten

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1124 · comment 713936814 · PR 12767 · 2025-11-14

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1111 — Document A deleted or filtered in entity loader

**Source stance:** requested-change

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s add a note that A is deleted/filtered in entity loader

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1128 · comment 716200494 · PR 12767 · 2025-11-20

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1112 — RRT example retains inactive status until caller postmerge filter

**Source stance:** explanation

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Inactive records may be deleted or filtered by loader; preserve source example caveat

**Source-preserving request, proposal, or question:**

> Example of correct usage.
> 
> * RRT should have A → INACTIVE, B → PROCESSING \(inactive entries should be deleted from entity or filtered by loader logic\)
> * merged result would have correct data, containing all 3 entries with expected status \(caller can apply filter afterwards to remove INACTIVE\)
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1129 · comment 716198684 · PR 12767 · 2025-11-20

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1121 — By-entity merge replaces every readside entry for same entityId

**Source stance:** explanation

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Missing entity data means deletion, so loader filtering also deletes

**Source-preserving request, proposal, or question:**

> Data from entity will override data from readside of same entityId \(may have multiple entries\) completely.
> 
> If data from entity is missing, it’s treated as deletion. This means any filtering in loader will also be treated as deletion.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1138 · comment 716199626 · PR 12767 · 2025-11-20

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1122 — By-key merge overrides matching key but missing data does not delete

**Source stance:** explanation

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Loader must not implement deletions or filtering

**Source-preserving request, proposal, or question:**

> Data from entity will override data from readside of same key.
> 
> If data from entity is missing, it’s not treated as deletion. This means data loader should not have deletion or filtering logic.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1139 · comment 716197130 · PR 12767 · 2025-11-20

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1142 — AccreditedInvestorEntity readside depends on customer Kafka; API race accepted

**Source stance:** explanation

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala; operation: [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This repo is readside of AccreditedInvestorEntity in compliance svc which gets its update via kafka topic of customer svc. So there’s some room of race condition here, but should be ok in the scope of these APIs

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1159 · comment 724010310 · PR 13025 · 2025-12-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis

## A1-1231 — Use existing voucher JDBC projection if historical events irrelevant

**Source stance:** suggestion

**Context:**

> component: voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/entities/voucher/processors/jdbc/VoucherAltsFundDiscountConfigJdbcProjection.scala; operation: Feat/PG-1205 daily fee discount calculator; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Should we just add this to existing jdbc projection, since we don’t really care about historical events?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1245 · comment 719939423 · PR 12828 · 2025-12-01

Source path: `voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/entities/voucher/processors/jdbc/VoucherAltsFundDiscountConfigJdbcProjection.scala`

**Explicit source context (pr_title):**

> Feat/PG-1205 daily fee discount calculator

## A1-1311 — New RPC projection not started in HK

**Source stance:** open-question

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala; operation: [BB-3055] feat(rebalance): adding RPC approvals; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> But we are not starting the projection in HK right?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1326 · comment 703468304 · PR 12776 · 2025-10-23

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala`

**Explicit source context (pr_title):**

> [BB-3055] feat(rebalance): adding RPC approvals

## A1-1312 — Existing RPC B2C comms projection must skip B2B workflow communications

**Source stance:** open-question

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala; operation: [BB-3055] feat(rebalance): adding RPC approvals; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Workflow should trigger assignment/action comms like other approvals

**Source-preserving request, proposal, or question:**

> This one sends comms on RPC to B2C customers today, however I dont think it is tenant aware.
> 
> How are we planning to handle comms for B2B RPC? Since we are going via workflow, I suppose we should follow same pattern in which workflow triggers comms endpoint upon approver assignment / actions? If so, we also need to change this projection to skip for B2B?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1327 · comment 703470378 · PR 12776 · 2025-10-23

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala`

**Explicit source context (pr_title):**

> [BB-3055] feat(rebalance): adding RPC approvals

## A1-1330 — Skip B2B in existing comms projection in this PR before independent comms change

**Source stance:** requested-change

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala; operation: [BB-3055] feat(rebalance): adding RPC approvals; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Otherwise release immediately breaks communications; B2C preserved and B2B workflow can operate without comms

**Source-preserving request, proposal, or question:**

> I don’t know when your comms PR will be approved and merged, but within the scope of this PR, we can’t let this go out otherwise comms will immediately be broken.
> 
> Why don’t we just skip in the existing comms projection in this PR so that the change is complete, i.e. B2C flow is not affected, and B2B flow has the workflow creation working without comms?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1345 · comment 704288631 · PR 12776 · 2025-10-24

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala`

**Explicit source context (pr_title):**

> [BB-3055] feat(rebalance): adding RPC approvals

## A1-1427 — Warn and rethrow trade-cancel command so projection retries

**Source stance:** requested-change

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala; operation: [INV-4562] feat(charge, redemption, trading): Automate fee handling; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Other remote calls may retry then error-log and give up

**Source-preserving request, proposal, or question:**

> Yes agree to log warn \+ rethrow for this cmd, and let projection stuck and retry. Here we are cancelling a trade that supposed to stuck in order generation.
> 
> And for other remote calls, we can retry and give up with error logs :thumbsup:

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1443 · comment 684464774 · PR 12500 · 2025-09-16

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala`

**Explicit source context (pr_title):**

> [INV-4562] feat(charge, redemption, trading): Automate fee handling

## A1-1429 — Redemption may wait for cancelled-trade event propagation

**Source stance:** open-question

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala; operation: [INV-4562] feat(charge, redemption, trading): Automate fee handling; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I think redemption it’s ok to wait for the trade cancelled event to propagate?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1445 · comment 684465933 · PR 12500 · 2025-09-16

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala`

**Explicit source context (pr_title):**

> [INV-4562] feat(charge, redemption, trading): Automate fee handling

**Evidence:** anon-1.jsonl:1445 · comment 684465933 · PR 12500 · 2025-09-16

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala`

**Explicit source context (hunk):**

> +          )
> +        )
> +        .withRetry(shouldRetryOnException = AlwaysRetryOnException, settings = futureRetrySettings)
> +        .recover {
> +          case err =>
> +            logger.error(s"Failed to delete corresponding redemption request for trade id: $tradeId of plan id: $planId, please check", err)
> +        }
> +
> +      _ = logger.info(s"Replace existing fee charge request with cash-only-fee charge for plan id: $planId")

## A1-1434 — Log error and move on rather than stall whole projection tag

**Source stance:** suggestion

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala; operation: [INV-4562] feat(charge, redemption, trading): Automate fee handling; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Full-redemption trade remains stuck in order generation regardless

**Source-preserving request, proposal, or question:**

> This will cause the projection to stuck for all plans on the same tag. I think it’s ok to log error and move on so that we unblock the projection. The full redemption trade will basically stuck in order generation step, and it won’t be able to move on anyway?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1450 · comment 684466888 · PR 12500 · 2025-09-16

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala`

**Explicit source context (pr_title):**

> [INV-4562] feat(charge, redemption, trading): Automate fee handling

## A1-1449 — Decide throw versus retry-and-give-up to avoid projection block

**Source stance:** open-question

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala; operation: [INV-4562] feat(charge, redemption, trading): Automate fee handling; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we want to throw here? Or just give up after retry so that we don’t block projection

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1466 · comment 685509405 · PR 12500 · 2025-09-18

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala`

**Explicit source context (pr_title):**

> [INV-4562] feat(charge, redemption, trading): Automate fee handling

**Evidence:** anon-1.jsonl:1466 · comment 685509405 · PR 12500 · 2025-09-18

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala`

**Explicit source context (hunk):**

> +      trade <- refProvider.getPlanTraderEntityRef(planId).ask(GetTradeCmd(_, tradeId))
> +      _ <- refProvider
> +        .getPlanTraderEntityRef(planId)
> +        .ask(
> +          DeleteTradeRequestCmd(
> +            _,
> +            tradeId = tradeId,
> +            reason = reason,
> +            requestedBy = requestedBy,

## A1-1461 — Remove live full-redemption recheck from invalid-order replay handling

**Source stance:** requested-change

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala; operation: [INV-4562] feat(charge, redemption, trading): Automate fee handling; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Cmd already established no full redemption; later live request must not suppress processing or alerts and leave trade stuck

**Source-preserving request, proposal, or question:**

> If we want additional check, then we need to think about our future reader:
> 
> * One who follows the code would see that the cmdHandler already checks for ongoing full redemption, and that if `INVALID_ORDERS_GENERATED_BY_FEE_CHARGE` is thrown, that cmdHandler already validates there is no ongoing full redemption trade in the PlanTraderEntity
> * Now in projection, we again query again, but this time we check on redemption svc. This query is also live at the point of projection processing the event \(which can be replayed\), so it’s very possible that at this point, there is full redemption returned here
> * Then this code simply goes to do nothing and return
> 
> ‌
> 
> There would be 2 wrong things in such scenarios:
> 
> * The live full redemption request \(from redemption svc\) at this point should not have any effect on this processing logic
> * This fee redemption trade would be stuck due to invalid orders, and we do not have any alerts at all
> 
> ‌
> 
> I’d suggest to remove this check, unless we know there’s some corner cases that might happen
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1478 · comment 686138230 · PR 12500 · 2025-09-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala`

**Explicit source context (pr_title):**

> [INV-4562] feat(charge, redemption, trading): Automate fee handling

## A1-1504 — Handle new advised payloads in goal projections including GoalSupportingDataProjection

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertApprovalActionBehaviour.scala; operation: [BB-2923] feat(advisory)(bff): adding plan upsert flow; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we need to create another one advised? Also looks like we missed to handle these new payload type on goal svc side, e.g. `GoalSupportingDataProjection`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1521 · comment 691915709 · PR 12652 · 2025-10-01

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertApprovalActionBehaviour.scala`

**Explicit source context (pr_title):**

> [BB-2923] feat(advisory)(bff): adding plan upsert flow

## A1-1702 — Daily-price deletion requires InstrumentMarketDataMsg for timeseries propagation

**Source stance:** open-question

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/ces/events/package.scala; operation: [INV-4723] feat(marketdata): create delete api for daily prices; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Don’t we need corresponding `InstrumentMarketDataMsg` so that timeseries can subscribe?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1720 · comment 680255999 · PR 12527 · 2025-09-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/ces/events/package.scala`

**Explicit source context (pr_title):**

> [INV-4723] feat(marketdata): create delete api for daily prices

**Evidence:** anon-1.jsonl:1720 · comment 680255999 · PR 12527 · 2025-09-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/ces/events/package.scala`

**Explicit source context (hunk):**

> object InstrumentCcyUpdatedEvt {
>      implicit val format: Format[InstrumentCcyUpdatedEvt] = Json.format
>    }
> +
> +  case class InstrumentDailyPriceDeletedEvt(
> +    priceDate: LocalDate,
> +    instrumentCcy: CurrencyUnit,
> +  ) extends InstrumentMarketDataEvt
> +

## A1-1704 — Repeated row delete on projection offset replay is idempotent

**Source stance:** explanation

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/prices/InstrumentPricesJdbcHandler.scala; operation: [INV-4723] feat(marketdata): create delete api for daily prices; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This one is fine? Projection might replay offset so we might delete same row multiple times, as long as it’s deleted, we’re good

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1722 · comment 680254006 · PR 12527 · 2025-09-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/prices/InstrumentPricesJdbcHandler.scala`

**Explicit source context (pr_title):**

> [INV-4723] feat(marketdata): create delete api for daily prices

## A1-1716 — Use readside updatedAt rather than createdAt LocalDate for schedule removal

**Source stance:** open-question

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RedemptionRequestTopicSubscriber.scala; operation: Resolve INV-4304: Add logic to trigger comms for inter-goal transfers; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Redemption before schedule creation should not remove new schedule

**Source-preserving request, proposal, or question:**

> Using createdAt \(LocalDate\) feels dangerous here? If customer creates redemption and then create the schedule, then by right, we don’t want to remove right? How about we follow similar approach as transfer and fetch from readside \(which has updatedAt\) instead?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1734 · comment 675483486 · PR 12010 · 2025-08-27

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RedemptionRequestTopicSubscriber.scala`

**Explicit source context (pr_title):**

> Resolve INV-4304: Add logic to trigger comms for inter-goal transfers

## A1-1717 — Rare schedule-update/full-redemption race within7s plus projection lag accepted

**Source stance:** explanation

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RedemptionRequestTopicSubscriber.scala; operation: Resolve INV-4304: Add logic to trigger comms for inter-goal transfers; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Schedule may remain, later trigger fails redeemable validation and notifies customer

**Source-preserving request, proposal, or question:**

> Yea I think this one is ok. The race condition would be customer creates/updates the transfer schedule then immediately create full redemption within the EC delay window \(7s\) \+ lags buildup \(if any\). That is rare enough.
> 
> Even if it happens, we essentially will keep the schedule. When it’s triggered, trading svc side should already have all the redeemable amount validation, and eventually mark the transfer as failed \(which has comms to customer as well\)

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1735 · comment 675481796 · PR 12010 · 2025-08-27

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RedemptionRequestTopicSubscriber.scala`

**Explicit source context (pr_title):**

> Resolve INV-4304: Add logic to trigger comms for inter-goal transfers

## A1-1720 — Do not send expired comms merely after successful remove command

**Source stance:** observed-defect

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringTransferScheduleManager.scala; operation: Resolve INV-4304: Add logic to trigger comms for inter-goal transfers; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Stale invalid schedule command may acknowledge without removal

**Source-preserving request, proposal, or question:**

> This chained future is not safe right? If the trigger is stale with invalid schedule, `RemovePlanRecurringTransferScheduleCmd`  will return success and we would still proceed to trigger expired comms.
> 
> I think safest is still do 2 steps. Only trigger cmd here - which may or may not remove the schedule, as per its validation. But if removed, we send comms in projection.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Send only from removal-event projection.

**Evidence:** anon-1.jsonl:1738 · comment 675853462 · PR 12010 · 2025-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringTransferScheduleManager.scala`

**Explicit source context (pr_title):**

> Resolve INV-4304: Add logic to trigger comms for inter-goal transfers

## A1-1851 — Error-log and move on instead of Kafka stall

**Source stance:** suggestion

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/AcceptSellTradeRequestCmdHandler.scala; operation: TT-6669 Collect CPF/SRS fees in cash; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Review syncRedemptionRequests manual retrigger

**Source-preserving request, proposal, or question:**

> Hmm if we throw here, it means the kafka subscriber would get stuck. Maybe the above error is sufficient then we can move on right? We can review this existing `syncRedemptionRequests` so that we can trigger the cmd if needed

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1871 · comment 664266664 · PR 12320 · 2025-07-31

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/AcceptSellTradeRequestCmdHandler.scala`

**Explicit source context (pr_title):**

> TT-6669 Collect CPF/SRS fees in cash

## A1-1882 — Stop publishing deprecated portfolio events

**Source stance:** requested-change

**Context:**

> component: portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/producers/PortfolioTopicProducer.scala; operation: [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s stop publishing for these deprecated event as well?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1902 · comment 632759905 · PR 11812 · 2025-05-14

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/producers/PortfolioTopicProducer.scala`

**Explicit source context (pr_title):**

> [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio

**Evidence:** anon-1.jsonl:1902 · comment 632759905 · PR 11812 · 2025-05-14

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/producers/PortfolioTopicProducer.scala`

**Explicit source context (hunk):**

> -          updatedAllocationTable = AllocationTargetTable.toDto(evt.updatedAllocationTable),
> -        )
> -        Future.successful(msg)
> -
> -      case BasicEventEnvelope(entityId, evt: PortfolioProjectedReturnUpdatedEvt, offset) =>
> -        val portfolioId = UUID.fromString(entityId)
> -        val msg = PortfolioProjectedReturnUpdatedMsg(
> -          portfolioId = portfolioId,
> -          effectiveDate = evt.currentEffectiveDate,

## A1-1967 — Do not replay new goal projection into same live plan table

**Source stance:** suggestion

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessorV5.scala; operation: Feature/DATA-1522 new column to support product line with type view; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> It will definitely cost a bit to start a new projection, but otherwise load itself on Cassandra or PG should be ok.
> 
> Having said that, we need to be careful with this GoalJdbcProjection. It’s writing to both goal & plan readside tables, with some handlers take data from event while some other handlers fetch latest data from entity.
> 
> Here we only wish to upversion goal table, but not plan table. Running this V5 projection as is will cause a long window of inconsistent data in plan table, for extended period of time until the projection has caught up to latest offset.
> 
> We can consider a few options:
> 
> 1. Upversion both goal & plan tables, even if no changes to plan table’s schema
> 2. Upversion only goal, and perform double release to switch over:
> 
>     1. Release 1:
>     
>         1. projectionV4 writes to goalV4 \+ planV4
>         2. projectionV5 writes to goalV5
>         
>     2. Release 2 \(after projectionV5 has caught up\):
>     
>         1. projectionV4 writes to goalV4
>         2. projectionV5 writes to goalV5 \+ planV4
>         3. Ideally we switch when lag is zero, but even if there’s any, the window of inconsistent data is much smaller
>         
>     
> 3. Since new column is derived data \+ optional in schema, and we only care about latest value, we can consider using alter table add column approach. And add a sync endpoint \+ kafka tasks to populate it for all goals \(with some basic optimistic locking check\)
> 
> ‌
> 
> \(1\) is most straightforward but cost us the most. \(3\) requires somewhat more development effort, but will cost us the least. \(2\) is somewhat middle approach, tradeoff some PG writes \(still same cost of Cassandra reads\) with release logistics.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Alternatives version both tables, two-release switch after catchup, or ALTER optional derived column plus task backfill/optimistic lock; exact sequences/cost tradeoffs retained.

**Evidence:** anon-1.jsonl:1988 · comment 662890532 · PR 12333 · 2025-07-29

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessorV5.scala`

**Explicit source context (pr_title):**

> Feature/DATA-1522 new column to support product line with type view

## A1-1968 — No simultaneous V4/V5 writes to planV4

**Source stance:** requested-change

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessorV5.scala; operation: Feature/DATA-1522 new column to support product line with type view; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Old upsertPlanInEvent may remain until next entity-fetch handler, long inconsistent window

**Source-preserving request, proposal, or question:**

> Yes we definitely don’t want dual writes to planV4 from both projections. ProjectionV5 processes all events from beginning, if the gap between `upsertPlanInEvent` will set the old data into plan readside, and if the gap between that event and next `upsertPlanInGoalEntity` / `upsertPlansInGoalEntity` is long enough, we will have problem with inconsistent data.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1989 · comment 662925663 · PR 12333 · 2025-07-29

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessorV5.scala`

**Explicit source context (pr_title):**

> Feature/DATA-1522 new column to support product line with type view

## A1-2004 — Add goal-service consistency endpoint pair; mismatch sync via command

**Source stance:** requested-change

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; operation: [INV-1946] feat(rebalance): remove taa entity; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We need another favour of this endpoint pair to sync with goal svc. If mismatch found, we need to sync via cmd
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2023 · comment 652297936 · PR 12157 · 2025-07-02

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-1946] feat(rebalance): remove taa entity

## A1-2005 — Check goal/rebalance plan readside consistency instead of unnecessary endpoint

**Source stance:** requested-change

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/TargetAssetAllocationJdbcEventProcessorV1.scala; operation: [INV-1946] feat(rebalance): remove taa entity; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> No need this one. But we should check data consistency between goal svc readside vs rebalance plan readside

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2024 · comment 652297126 · PR 12157 · 2025-07-02

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/TargetAssetAllocationJdbcEventProcessorV1.scala`

**Explicit source context (pr_title):**

> [INV-1946] feat(rebalance): remove taa entity

## A1-2040 — Fee command duplicate initiatingFullRedemptionRequestId check makes topic handling idempotent

**Source stance:** explanation

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/RedemptionTopicSubscriber.scala; operation: [INV-4265] feat(charge): Full redemption charge fixes; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Yea, same as any other msg handler in TopicSubscriber. The cmd handler already has checks for duplicated `initiatingFullRedemptionRequestId`, so it should be idempotent as well

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2060 · comment 621188121 · PR 11639 · 2025-04-17

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/RedemptionTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [INV-4265] feat(charge): Full redemption charge fixes

## A1-2141 — PLAN_ONE_TIME_INVESTMENT_APPROVED needs investment-service trigger

**Source stance:** open-question

**Context:**

> component: goal-api/src/main/scala/com/endowus/silver/goal/api/enums/package.scala; operation: [INV-3426] feat(bff, workflowengine, advisory, goal, investment): Create subsequent investment for existing goal; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We would need another enum value for `PLAN_ONE_TIME_INVESTMENT_APPROVED` as well? Which would need different trigger mechanism, since source of event would be from `investment` svc

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2158 · comment 572113750 · PR 10480 · 2024-12-02

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/enums/package.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, workflowengine, advisory, goal, investment): Create subsequent investment for existing goal

## A1-2149 — At-least-once workflow approval uses stable requestIdSeed to dedupe investment

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/B2BProductHelpers.scala; operation: [INV-3426] feat(bff, workflowengine, advisory, goal, investment): Create subsequent investment for existing goal; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Full IdempotencyKey future; do not invest twice

**Source-preserving request, proposal, or question:**

> Idempotent means if same request is called twice \(or more\), we are able to de-dupe and execute it only once. Full fledge solution would involve properly implement `IdempotencyKey` , but for now, it should be sufficient if we rely on existing mechanism in `investment` svc to allow caller to set `investmentRequestId` via `requestIdSeed`
> 
> When a task is fully approved, workflow-engine will trigger this endpoint to perform the request \(sent in task payload\). The guarantee here is at-least-once. So we have to make sure we don’t invest multiple times if for whatever reason, it’s triggered multiple times by workflow-engine.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2166 · comment 573400069 · PR 10480 · 2024-12-04

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/B2BProductHelpers.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, workflowengine, advisory, goal, investment): Create subsequent investment for existing goal

## A1-2151 — Use goal supporting-data table populated via investment projection/internal endpoint

**Source stance:** suggestion

**Context:**

> component: goal-api/src/main/scala/com/endowus/silver/goal/api/enums/package.scala; operation: [INV-3426] feat(bff, workflowengine, advisory, goal, investment): Create subsequent investment for existing goal; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I’m thinking it would be easier if we use same table in goal svc
> 
> * add internal endpoint to populate the table
> * call that endpoint from a projection in investment svc
> 
> This way, we can have single table to query all action contexts for a goal
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2168 · comment 575879573 · PR 10480 · 2024-12-09

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/enums/package.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, workflowengine, advisory, goal, investment): Create subsequent investment for existing goal

## A1-2165 — Investment projection+goal internal upload versus Kafka approved event+subscriber

**Source stance:** suggestion

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentSupportingDataProjection.scala; operation: [INV-3426] feat(bff, workflowengine, advisory, goal, investment): Create subsequent investment for existing goal; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> There are 2 approaches:
> 
> 1. Projection in investment \(approved evt is internal to investment svc\) \+ internal endpoint of goal svc to upload supporting data
> 2. Publish approved evt as Kafka \+ subscriber on goal svc to upload supporting data \(no exposure of upload endpoint\)
> 
> ‌
> 
> Let’s think about pros & cons but \(1\) sounds easier to support cuz we have the endpoint ready for manual intervention if needed
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Internal endpoint alternative easier manual intervention; pros/cons unresolved.

**Evidence:** anon-1.jsonl:2182 · comment 585711505 · PR 10480 · 2025-01-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentSupportingDataProjection.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, workflowengine, advisory, goal, investment): Create subsequent investment for existing goal

## A1-2281 — Consider recipientId for reassigned task; insertion target unspecified

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/B2BNotificationManager.scala; operation: [INV-3765] feat(adviosry): create apis for b2b approval notifcations; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I’m thinking if we should just include recipientId here, in case if we ever need to re-assign a task \(e.g. changes to FA manager\)

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2298 · comment 595178780 · PR 11000 · 2025-02-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/B2BNotificationManager.scala`

**Explicit source context (pr_title):**

> [INV-3765] feat(adviosry): create apis for b2b approval notifcations

## A1-2370 — Normal instruments enter readside via price updates; benchmarks lack those

**Source stance:** explanation

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/subscribers/InstrumentTopicSubscriber.scala; operation: Resolve INV-3916: Fix to insert instrument for benchmark instrument onboarding.; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Ok so normal instruments are added to readside via the price updates - which benchmark instruments don’t have.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2385 · comment 595269269 · PR 11046 · 2025-02-11

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/subscribers/InstrumentTopicSubscriber.scala`

**Explicit source context (pr_title):**

> Resolve INV-3916: Fix to insert instrument for benchmark instrument onboarding.

## A1-2427 — Combine two completion mails for same customer internal plan transfer

**Source stance:** open-question

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/InstrumentTransferCommunicationV2Projection.scala; operation: [INV-3710] feat(inter plan transfer): handle comms for transfer instructions; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We will send 2 mails of completed instruction to same customer, if purely transferring between their plans. Is there a way to combine into 1?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2448 · comment 570098272 · PR 10435 · 2024-11-25

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/InstrumentTransferCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> [INV-3710] feat(inter plan transfer): handle comms for transfer instructions

## A1-2428 — Send only after both sides submitted/completed with identical data

**Source stance:** requested-change

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/InstrumentTransferCommunicationV2Projection.scala; operation: [INV-3710] feat(inter plan transfer): handle comms for transfer instructions; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Entity query acceptable

**Source-preserving request, proposal, or question:**

> We also need to make sure the data is identical between them, and only send out if both are submitted/completed. It should be ok to query entity here I think

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2449 · comment 570118866 · PR 10435 · 2024-11-25

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/InstrumentTransferCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> [INV-3710] feat(inter plan transfer): handle comms for transfer instructions

## A1-2437 — Invalid persisted event log and skip; replay cannot fix it

**Source stance:** requested-change

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/InstrumentTransferCommunicationV2Projection.scala; operation: [INV-3710] feat(inter plan transfer): handle comms for transfer instructions; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> If such event is emitted, there’s nothing this projectio can do so we should just log error and move on. Throwing and reprocessing it won’t change anything?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2458 · comment 578132263 · PR 10435 · 2024-12-16

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/InstrumentTransferCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> [INV-3710] feat(inter plan transfer): handle comms for transfer instructions

## A1-2440 — Invalid reference data should throw because fixable then retry

**Source stance:** explanation

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/InstrumentTransferCommunicationV2Projection.scala; operation: [INV-3710] feat(inter plan transfer): handle comms for transfer instructions; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This one is on the other hand better example that we should throw. It is invalid reference data, and can be fixed.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2461 · comment 579357753 · PR 10435 · 2024-12-18

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/InstrumentTransferCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> [INV-3710] feat(inter plan transfer): handle comms for transfer instructions

## A1-2442 — Do not block projection on permanently invalid persisted event

**Source stance:** requested-change

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/InstrumentTransferCommunicationV2Projection.scala; operation: [INV-3710] feat(inter plan transfer): handle comms for transfer instructions; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Same as older comments. We don’t want to throw here and block the projection. The invalid event has already been persisted, there’s nothing we can do about it.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2463 · comment 579357049 · PR 10435 · 2024-12-18

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/InstrumentTransferCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> [INV-3710] feat(inter plan transfer): handle comms for transfer instructions

## A1-2445 — Communication identity uses planId instead of customerId

**Source stance:** suggestion

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/InstrumentTransferCommunicationV2Projection.scala; operation: [INV-3710] feat(inter plan transfer): handle comms for transfer instructions; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** TransferInstructionId only plan-unique guaranteed, not customer/global

**Source-preserving request, proposal, or question:**

> We only ensure uniqueness of this `transferInstructionId` at plan level as of now.
> 
> By right, the id should be unique at customer level too \(or even globally\) since we are expecting it to be random UUID. But in theory, as long as the plans are different, a customer have duplicated `transferInstructionId`
> 
> ‌
> 
> Since we already check `shouldIgnoreTransferOutForSameBroker` above, maybe it’s safer to use planId instead of customerId here? Same for submitted evt

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Already ignores same-broker transfer out; applies submitted too.

**Evidence:** anon-1.jsonl:2466 · comment 579360326 · PR 10435 · 2024-12-18

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/InstrumentTransferCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> [INV-3710] feat(inter plan transfer): handle comms for transfer instructions

## A2-0026 — BackfillPlanProfileTenantIdCmdHandler: Let’s also return without events if same tenantId already exists. Then we won’t have duplicated events, as the subscriber might process a ...

**Source stance:** requested-change

**Context:**

> PR 11333 ([EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/BackfillPlanProfileTenantIdCmdHandler.scala; original row 26.

**Concern stated in the source:** A subscriber can process a task more than once and generate duplicate tenant-backfill events.

**Source-preserving request, proposal, or question:**

> Let’s also return without events if same tenantId already exists. Then we won’t have duplicated events, as the subscriber might process a task multiple times.

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:26 · comment 609026873 · PR 11333 · 2025-03-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/BackfillPlanProfileTenantIdCmdHandler.scala`

**Evidence:** anon-2.jsonl:26 · comment 609026873 · PR 11333 · 2025-03-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/BackfillPlanProfileTenantIdCmdHandler.scala`

**Explicit source context (pr_title):**

> [EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles

## A2-0027 — BackfillPlanProfileTenantIdTaskTopicSubscriber: We shouldn’t need planId as part of the cmd since it’s already entityId

**Source stance:** explanation

**Context:**

> PR 11333 ([EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/task/BackfillPlanProfileTenantIdTaskTopicSubscriber.scala; original row 27.

**Source-preserving request, proposal, or question:**

> We shouldn’t need planId as part of the cmd since it’s already entityId

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:27 · comment 609023439 · PR 11333 · 2025-03-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/task/BackfillPlanProfileTenantIdTaskTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:27 · comment 609023439 · PR 11333 · 2025-03-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/task/BackfillPlanProfileTenantIdTaskTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles

## A2-0028 — PlanProfileJdbcProjectionV3: Since we have the full PlanProfile in the `PlanProfileTenantIdBackFilledEvt`, let’s use it directly instead of fetching from entity again.

**Source stance:** explanation

**Context:**

> PR 11333 ([EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/PlanProfileJdbcProjectionV3.scala; original row 28.

**Concern stated in the source:** The event already contains the full PlanProfile; fetching entity state again is unnecessary for this event.

**Source-preserving request, proposal, or question:**

> Since we have the full PlanProfile in the `PlanProfileTenantIdBackFilledEvt`, let’s use it directly instead of fetching from entity again.
> 
> One day we need to for all these existing events as well, to have separate update query for them that doesn’t rely on fetching whole PlanProfile

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:28 · comment 609335815 · PR 11333 · 2025-03-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/PlanProfileJdbcProjectionV3.scala`

**Evidence:** anon-2.jsonl:28 · comment 609335815 · PR 11333 · 2025-03-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/PlanProfileJdbcProjectionV3.scala`

**Explicit source context (pr_title):**

> [EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles

## A2-0029 — FeeChargeRequestJdbcProjectionV6: I think we can let DB take care of both the query and update. Something like `UPDATE feeChargeRequests SET tenantId WHERE customerId, planId`

**Source stance:** suggestion

**Context:**

> PR 11333 ([EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcProjectionV6.scala; original row 29.

**Source-preserving request, proposal, or question:**

> I think we can let DB take care of both the query and update. Something like `UPDATE feeChargeRequests SET tenantId WHERE customerId, planId`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:29 · comment 609335884 · PR 11333 · 2025-03-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcProjectionV6.scala`

**Evidence:** anon-2.jsonl:29 · comment 609335884 · PR 11333 · 2025-03-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcProjectionV6.scala`

**Explicit source context (pr_title):**

> [EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles

## A2-0030 — FeeChargeRequestJdbcProjectionV6: There’s no need to query this anymore. The `updateTenantId` takes care of all requests with matching customerId/planId

**Source stance:** explanation

**Context:**

> PR 11333 ([EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcProjectionV6.scala; original row 30.

**Concern stated in the source:** updateTenantId already covers requests matching customerId/planId.

**Source-preserving request, proposal, or question:**

> There’s no need to query this anymore. The `updateTenantId` takes care of all requests with matching customerId/planId

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:30 · comment 609630992 · PR 11333 · 2025-03-17

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcProjectionV6.scala`

**Evidence:** anon-2.jsonl:30 · comment 609630992 · PR 11333 · 2025-03-17

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcProjectionV6.scala`

**Explicit source context (pr_title):**

> [EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles

## A2-0031 — BackfillPlanProfileTenantIdTaskTopicSubscriber: I realize we could have made the task keyed by customerId instead, then in this subscriber, we query planProfiles by customerId a...

**Source stance:** suggestion

**Context:**

> PR 11333 ([EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/task/BackfillPlanProfileTenantIdTaskTopicSubscriber.scala; original row 31.

**Source-preserving request, proposal, or question:**

> I realize we could have made the task keyed by customerId instead, then in this subscriber, we query planProfiles by customerId and invoke the cmd as usual. It’s one time exercise so this is ok too

**Conditions and limits:**

- The customerId-keyed alternative is explicitly considered optional because this is a one-time exercise.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:31 · comment 609631484 · PR 11333 · 2025-03-17

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/task/BackfillPlanProfileTenantIdTaskTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:31 · comment 609631484 · PR 11333 · 2025-03-17

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/task/BackfillPlanProfileTenantIdTaskTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles

## A2-0036 — BaseRedemptionCommunicationV2Projection: Here we change the formula to generate communication id. During deployment, depending on timing, this might cause the email to trigger t...

**Source stance:** observed-defect

**Context:**

> PR 11207 ([EN-4396] feat(redemption)(communication) Support B2B redemption emails and migrate to Communicator V2), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala; original row 36.

**Concern stated in the source:** Changing the communication-id formula can trigger the same email twice depending on deployment timing.

**Source-preserving request, proposal, or question:**

> Here we change the formula to generate communication id. During deployment, depending on timing, this might cause the email to trigger twice if we’re unlucky

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:36 · comment 610639292 · PR 11207 · 2025-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Evidence:** anon-2.jsonl:36 · comment 610639292 · PR 11207 · 2025-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> [EN-4396] feat(redemption)(communication) Support B2B redemption emails and migrate to Communicator V2

## A2-0037 — SgRedemptionCommunicationV2Projection: Can save tenant lookup call if returned context is empty

**Source stance:** suggestion

**Context:**

> PR 11207 ([EN-4396] feat(redemption)(communication) Support B2B redemption emails and migrate to Communicator V2), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/SgRedemptionCommunicationV2Projection.scala; original row 37.

**Concern stated in the source:** An empty returned context makes tenant lookup unnecessary.

**Source-preserving request, proposal, or question:**

> Can save tenant lookup call if returned context is empty

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:37 · comment 610647414 · PR 11207 · 2025-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/SgRedemptionCommunicationV2Projection.scala`

**Evidence:** anon-2.jsonl:37 · comment 610647414 · PR 11207 · 2025-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/SgRedemptionCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> [EN-4396] feat(redemption)(communication) Support B2B redemption emails and migrate to Communicator V2

## A2-0039 — BaseRedemptionCommunicationV2Projection: Naming can be a little confusing now

**Source stance:** suggestion

**Context:**

> PR 11207 ([EN-4396] feat(redemption)(communication) Support B2B redemption emails and migrate to Communicator V2), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala; original row 39.

**Concern stated in the source:** The actual HK projection inherits BaseRedemptionCommunicationV2Projection, the actual SG projection does not, and two new CommunicationManagers do.

**Source-preserving request, proposal, or question:**

> Naming can be a little confusing now
> 
> * HkRedemptionCommunicationV2Projection \(actual projection\) extends BaseRedemptionCommunicationV2Projection
> * but SgRedemptionCommunicationV2Projection \(actual projection\) does not, and yet the 2 new CommunicationManger extends BaseRedemptionCommunicationV2Projection
> 
> We can refactor later. This is just a note for now
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:39 · comment 610709720 · PR 11207 · 2025-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Evidence:** anon-2.jsonl:39 · comment 610709720 · PR 11207 · 2025-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> [EN-4396] feat(redemption)(communication) Support B2B redemption emails and migrate to Communicator V2

## A2-0105 — GoalSupportingDataProjection: `ele.event.taskApprovalDetails` should compile so no need to check this

**Source stance:** explanation

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalSupportingDataProjection.scala; original row 105.

**Source-preserving request, proposal, or question:**

> `ele.event.taskApprovalDetails` should compile so no need to check this

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:105 · comment 587734268 · PR 10896 · 2025-01-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalSupportingDataProjection.scala`

**Evidence:** anon-2.jsonl:105 · comment 587734268 · PR 10896 · 2025-01-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalSupportingDataProjection.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0106 — GoalSupportingDataProjection: This block probably can refactor to avoid repeating the code vs `handleGoalCreationApprovedHandler`

**Source stance:** suggestion

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalSupportingDataProjection.scala; original row 106.

**Source-preserving request, proposal, or question:**

> This block probably can refactor to avoid repeating the code vs `handleGoalCreationApprovedHandler`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:106 · comment 587734350 · PR 10896 · 2025-01-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalSupportingDataProjection.scala`

**Evidence:** anon-2.jsonl:106 · comment 587734350 · PR 10896 · 2025-01-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalSupportingDataProjection.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0121 — InvestmentSupportingDataProjection: Now we know these projections can cost us decent chunk of money, since it’s not used in prod, maybe good chance to reuse existing projection ...

**Source stance:** suggestion

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentSupportingDataProjection.scala; original row 121.

**Concern stated in the source:** Unused-in-prod projections have material cost; reuse is proposed.

**Source-preserving request, proposal, or question:**

> Now we know these projections can cost us decent chunk of money, since it’s not used in prod, maybe good chance to reuse existing projection instead of creating new ones \(same for goal svc [person] ?\)

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:121 · comment 587730830 · PR 10896 · 2025-01-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentSupportingDataProjection.scala`

> Now we know these projections can cost us decent chunk of money, since it’s not used in prod, maybe good chance to reuse existing projection instead of creating new ones \(same for goal svc

**Evidence:** anon-2.jsonl:121 · comment 587730830 · PR 10896 · 2025-01-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentSupportingDataProjection.scala`

> ?\)

**Evidence:** anon-2.jsonl:121 · comment 587730830 · PR 10896 · 2025-01-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentSupportingDataProjection.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0128 — InvestmentSupportingDataProjection: reuse $context and actionContext

**Source stance:** requested-change

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentSupportingDataProjection.scala; original row 128.

**Source-preserving request, proposal, or question:**

> Use the `$context`. Same for `actionContext` below

**Conditions and limits:**

- The comment explicitly names $context and actionContext, but supplies no old expression or replacement snippet beyond those names. Do not invent the surrounding interpolation or event logic.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:128 · comment 597526377 · PR 10896 · 2025-02-18

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentSupportingDataProjection.scala`

**Evidence:** anon-2.jsonl:128 · comment 597526377 · PR 10896 · 2025-02-18

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentSupportingDataProjection.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0135 — GoalSupportingDataProjection: Maybe just call `upsertGoalSupportingData` directly?

**Source stance:** suggestion

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalSupportingDataProjection.scala; original row 135.

**Source-preserving request, proposal, or question:**

> Maybe just call `upsertGoalSupportingData` directly?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:135 · comment 597530970 · PR 10896 · 2025-02-18

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalSupportingDataProjection.scala`

**Evidence:** anon-2.jsonl:135 · comment 597530970 · PR 10896 · 2025-02-18

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalSupportingDataProjection.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0144 — InvestmentSupportingDataProjection: Last chance to change with relatively little cost, before committing this to prod. Is there strong reason for this to be standalone projectio...

**Source stance:** suggestion

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentSupportingDataProjection.scala; original row 144.

**Concern stated in the source:** Before production, an extra standalone projection remains cheap to change; InvestmentPlanProjection could be made region-aware and reused.

**Source-preserving request, proposal, or question:**

> Last chance to change with relatively little cost, before committing this to prod. Is there strong reason for this to be standalone projection, or we can top up to existing `InvestmentPlanProjection` \(probably need to make it regional aware, but still easy to do\)

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:144 · comment 601750972 · PR 10896 · 2025-03-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentSupportingDataProjection.scala`

**Evidence:** anon-2.jsonl:144 · comment 601750972 · PR 10896 · 2025-03-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentSupportingDataProjection.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0151 — InvestmentPlanEventProcessor: We now wire sg class in common projection used in hk. It should be split…

**Source stance:** observed-defect

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentPlanEventProcessor.scala; original row 151.

**Concern stated in the source:** An SG workflow client is wired into a common projection used in HK.

**Source-preserving request, proposal, or question:**

> We now wire sg class in common projection used in hk. It should be split…

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:151 · comment 601799177 · PR 10896 · 2025-03-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentPlanEventProcessor.scala`

**Evidence:** anon-2.jsonl:151 · comment 601799177 · PR 10896 · 2025-03-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentPlanEventProcessor.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0182 — SgWorkflowEngineE4s: WorkflowEngineE4s

**Source stance:** explanation

**Context:**

> PR 10647 (Feat/AD-2007 b2b approvals bff), workflowengine-api/src/main/scala/com/endowus/silver/workflowengine/api/SgWorkflowEngineE4s.scala; original row 182.

**Concern stated in the source:** Current advisor/client portal split duplicates the pending-my-approval route until FE clients are unified.

**Source-preserving request, proposal, or question:**

> WorkflowEngineE4s
> 
> ```
> /pending-approvals/creator/:creatorId?assigneeRole
> /pending-approvals/assignee/:assigneeId
> ```
> 
> ‌
> 
> BFF
> 
> ```
> A. my-created-and-pending-manager-requests/taskType/:taskType
> - calls /pending-approvals/creator/<authenticated-employeeId>?assigneeRole=FA_MANAGER
> - RBAC: Create action for RBAC resource coresponding to taskType
> 
> B. my-created-and-pending-client-requests/taskType/:taskType
> - calls /pending-approvals/creator/<authenticated-employeeId>?assigneeRole=CLIENT
> - RBAC: Create action for RBAC resource coresponding to taskType
> 
> C. pending-my-approval/taskType/:taskType
> - calls /pending-approvals/assignee/<authenticated-employeeId/customerId>
> - RBAC: Approve action for RBAC resource coresponding to taskType
> ```
> 
> ‌
> 
> BFF currently splits advisor-portal \(AdvisorPortal\*\) and client-portal \(SilverFe\*\). This means \(C\) needs to be duplicated.
> 
> BFF will eventually unify the FE clients \(every endpoint need to support all user types, as long as they pass the RBAC and guards validation\)

**Conditions and limits:**

- Keep the three concrete route/RBAC mappings from the source; pending-my-approval is duplicated until client unification.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:182 · comment 580762582 · PR 10647 · 2024-12-23

Source path: `workflowengine-api/src/main/scala/com/endowus/silver/workflowengine/api/SgWorkflowEngineE4s.scala`

**Evidence:** anon-2.jsonl:182 · comment 580762582 · PR 10647 · 2024-12-23

Source path: `workflowengine-api/src/main/scala/com/endowus/silver/workflowengine/api/SgWorkflowEngineE4s.scala`

**Explicit source context (pr_title):**

> Feat/AD-2007 b2b approvals bff

## A2-0200 — InitiateCancellationFlowCmdHandler: This `INVALID_CANCEL_ATTEMPT` is mapped to NotFound right now. It seems not used, so maybe change it to BadRequest instead?

**Source stance:** suggestion

**Context:**

> PR 10714 ([INV-3798] feat(investment): Throw error on cancellation failed in investment service), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala; original row 200.

**Concern stated in the source:** INVALID_CANCEL_ATTEMPT currently maps to NotFound; throwing always can violate expected idempotent best-effort cancellation from projections/subscribers.

**Source-preserving request, proposal, or question:**

> This `INVALID_CANCEL_ATTEMPT` is mapped to NotFound right now. It seems not used, so maybe change it to BadRequest instead?
> 
> Generally, we want these cmd to be idempotent especially when they are used in projection / kafka subscriber. I think all these use cases that trigger investment cancellation from BE \(redemption / expiry / compliance\) understand that it is best effort basis. So it’s better to expose a flag to ignore this error instead of throwing always?

**Conditions and limits:**

- Best-effort cancellation is specifically discussed for backend redemption/expiry/compliance triggers; the source proposes an ignore-error flag.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:200 · comment 580810035 · PR 10714 · 2024-12-23

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Evidence:** anon-2.jsonl:200 · comment 580810035 · PR 10714 · 2024-12-23

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Explicit source context (pr_title):**

> [INV-3798] feat(investment): Throw error on cancellation failed in investment service

## A2-0208 — BffServiceE4s: This should work, but would be better to follow Option 2 explained in [<url> data-inline-card='' } 

**Source stance:** suggestion

**Context:**

> PR 10301 ([AD-2061] feat(advisory-portal,bff): Added BrokerAccountCashBalances endpoint), bff-api/src/main/scala/com/endowus/silver/bff/api/BffServiceE4s.scala; original row 208.

**Concern stated in the source:** The linked Option 2 is preferred to avoid duplicating BFF endpoint definitions; its details are unavailable in the comment.

**Source-preserving request, proposal, or question:**

> This should work, but would be better to follow Option 2 explained in [<url> data-inline-card='' } 
> 
> So that we don’t have to duplicate the endpoint definitions in BFF

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:208 · comment 562949308 · PR 10301 · 2024-11-08

Source path: `bff-api/src/main/scala/com/endowus/silver/bff/api/BffServiceE4s.scala`

**Evidence:** anon-2.jsonl:208 · comment 562949308 · PR 10301 · 2024-11-08

Source path: `bff-api/src/main/scala/com/endowus/silver/bff/api/BffServiceE4s.scala`

**Explicit source context (pr_title):**

> [AD-2061] feat(advisory-portal,bff): Added BrokerAccountCashBalances endpoint

## A2-0213 — CostOfInvestmentDetailsJdbcProjectionV7: Remove this call since we are looking up whole txn below?

**Source stance:** suggestion

**Context:**

> PR 10245 (Resolve INV-3514: Changes to include transaction fees as part of cost of investment calculation), broker-impl/src/main/scala/com/endowus/silver/broker/impl/entities/account/processors/CostOfInvestmentDetailsJdbcProjectionV7.scala; original row 213.

**Concern stated in the source:** The complete transaction is fetched below, making this earlier lookup unnecessary.

**Source-preserving request, proposal, or question:**

> Remove this call since we are looking up whole txn below?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:213 · comment 560704516 · PR 10245 · 2024-11-04

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/entities/account/processors/CostOfInvestmentDetailsJdbcProjectionV7.scala`

**Evidence:** anon-2.jsonl:213 · comment 560704516 · PR 10245 · 2024-11-04

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/entities/account/processors/CostOfInvestmentDetailsJdbcProjectionV7.scala`

**Explicit source context (pr_title):**

> Resolve INV-3514: Changes to include transaction fees as part of cost of investment calculation

## A2-0283 — PlanFeeInstructionEntity: Just thinking out loud, I’m not sure about capturing this effectiveEndDate in the event

**Source stance:** open-question

**Context:**

> PR 10030 ([EN-3952] (charge) Create new PlanFeeInstructionEntity), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala; original row 283.

**Concern stated in the source:** effectiveEndDate is derived, cannot be reconstructed at event-creation state by projection, and changing one instruction generally affects two instruction end dates.

**Source-preserving request, proposal, or question:**

> Just thinking out loud, I’m not sure about capturing this effectiveEndDate in the event
> 
> * It’s derived data, but I understand the concern that projection is not able to derive by itself since projection does not have access to the state at the point of event creation
> * It’s somewhat incomplete, because we would typically affect effectiveEndDate of 2 instructions, but we only emit for the one being upserted / deleted
> 
> If the intention is to provide ability for projection \(or even external topic subscriber\) to reconstruct the exact state, we can consider emit 2 events instead, one for the individual change, and one for the state \(pattern “Event-Carried State Transfer”\). This comes with its own pros & cons, but I think it’s cleaner and more flexible than stamping single effective end date here.
> 
> ‌
> 
> The field is logically optional right now. We can revisit this later if needed.

**Conditions and limits:**

- Two events (individual change plus state transfer) are an option with pros/cons; effectiveEndDate is currently logically optional and may be revisited.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:283 · comment 552730699 · PR 10030 · 2024-10-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Evidence:** anon-2.jsonl:283 · comment 552730699 · PR 10030 · 2024-10-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Explicit source context (pr_title):**

> [EN-3952] (charge) Create new PlanFeeInstructionEntity

## A2-0291 — common: Removed since wrong existing config. `projection` doesn’t have any entity anymore

**Source stance:** explanation

**Context:**

> PR 10485 ([INV-3738] feat(common): Make eventual-consistency-delay configurable), projection-impl/src/main/resources/common.conf; original row 291.

**Concern stated in the source:** projection has no entities and its old config was wrong.

**Source-preserving request, proposal, or question:**

> Removed since wrong existing config. `projection` doesn’t have any entity anymore

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:291 · comment 571846792 · PR 10485 · 2024-11-29

Source path: `projection-impl/src/main/resources/common.conf`

**Evidence:** anon-2.jsonl:291 · comment 571846792 · PR 10485 · 2024-11-29

Source path: `projection-impl/src/main/resources/common.conf`

**Explicit source context (pr_title):**

> [INV-3738] feat(common): Make eventual-consistency-delay configurable

## A2-0301 — BaseServiceLogicImpl: The cmd is idempotent anyway, so maybe we just trigger from goal level instead? No need to double lookup

**Source stance:** suggestion

**Context:**

> PR 10417 (Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.), goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; original row 301.

**Concern stated in the source:** The backfill command is already idempotent, making a double lookup unnecessary.

**Source-preserving request, proposal, or question:**

> The cmd is idempotent anyway, so maybe we just trigger from goal level instead? No need to double lookup

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:301 · comment 570115832 · PR 10417 · 2024-11-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:301 · comment 570115832 · PR 10417 · 2024-11-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.

## A2-0313 — RecurringInvestmentScheduleHistoryDataEventProcessorV3: `PlanRecurringInvestmentScheduleHistoryTableV3` stores the history audit entries, so we can’t rely on this backfill evt t...

**Source stance:** explanation

**Context:**

> PR 10417 (Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryDataEventProcessorV3.scala; original row 313.

**Concern stated in the source:** History audit entries cannot be repaired eventually by a new backfill event, unlike the current schedule table.

**Source-preserving request, proposal, or question:**

> `PlanRecurringInvestmentScheduleHistoryTableV3` stores the history audit entries, so we can’t rely on this backfill evt to correct the data eventually \(unlike `PlanRecurringInvestmentScheduleTableV3`\). The fallback logic must continue to stay even in newer table version \(or we add fallback logic to the db model `PlanRecurringInvestmentScheduleHistory` instead\)
> 
> But regardless, it seems we don’t need to handle backfill evt in the history projection

**Conditions and limits:**

- Keep investmentAmount→fundingInstructions fallback in newer history table versions, or move it to the PlanRecurringInvestmentScheduleHistory DB model. Do not infer backfill eventually fixes audit history.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:313 · comment 570860367 · PR 10417 · 2024-11-27

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryDataEventProcessorV3.scala`

**Evidence:** anon-2.jsonl:313 · comment 570860367 · PR 10417 · 2024-11-27

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryDataEventProcessorV3.scala`

**Explicit source context (pr_title):**

> Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.

## A2-0319 — InstrumentMonthlyChangesTaskSubscriber: Should be `upload` not `calculate`

**Source stance:** suggestion

**Context:**

> PR 10400 ([INV-3609] feat(marketdata, instrument): improve marketdata monthly changes reliability), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/task/InstrumentMonthlyChangesTaskSubscriber.scala; original row 319.

**Source-preserving request, proposal, or question:**

> Should be `upload` not `calculate`

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- The hunk identifies instrument-monthly-changes-upload-task and consumer-group naming; source requests upload rather than calculate.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:319 · comment 568223136 · PR 10400 · 2024-11-20

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/task/InstrumentMonthlyChangesTaskSubscriber.scala`

**Evidence:** anon-2.jsonl:319 · comment 568223136 · PR 10400 · 2024-11-20

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/task/InstrumentMonthlyChangesTaskSubscriber.scala`

**Explicit source context (hunk):**

> +  private val consumerGroupId = "marketDataSvc-instrumentMonthlyChangesUploadTask-group"
> +  private val taskConfigName = "instrument-monthly-changes-upload-task"
> +}

**Evidence:** anon-2.jsonl:319 · comment 568223136 · PR 10400 · 2024-11-20

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/task/InstrumentMonthlyChangesTaskSubscriber.scala`

**Explicit source context (pr_title):**

> [INV-3609] feat(marketdata, instrument): improve marketdata monthly changes reliability

## A2-0346 — GoalEventProcessor: We split new projection, inject `WorkflowEngineServiceSg` and wire it only for SG

**Source stance:** suggestion

**Context:**

> PR 10335 (Feat/INV-3508 goal create projections), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalEventProcessor.scala; original row 346.

**Concern stated in the source:** New SG workflow projections/tables should be wired only in SG until HK approval support exists.

**Source-preserving request, proposal, or question:**

> We split new projection, inject `WorkflowEngineServiceSg` and wire it only for SG
> 
> Tmr when we have approval in HK, change `WorkflowEngineServiceSg` to Base, wire in HK as well.. but further logic changes
> 
> ‌
> 
> Same for table, design is region agnostic, but we wire SG only

**Conditions and limits:**

- HK wiring is a future change requiring a base client and further logic changes; the schema itself is region agnostic.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:346 · comment 564025895 · PR 10335 · 2024-11-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalEventProcessor.scala`

**Evidence:** anon-2.jsonl:346 · comment 564025895 · PR 10335 · 2024-11-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalEventProcessor.scala`

**Explicit source context (pr_title):**

> Feat/INV-3508 goal create projections

## A2-0347 — GoalSupportingDataTableV1: `GoalActionContext` covers `CREATION_APPROVED, MODIFICATION_APPROVED` which is initiated from goal svc

**Source stance:** suggestion

**Context:**

> PR 10335 (Feat/INV-3508 goal create projections), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataTableV1.scala; original row 347.

**Source-preserving request, proposal, or question:**

> `GoalActionContext` covers `CREATION_APPROVED, MODIFICATION_APPROVED` which is initiated from goal svc
> 
> ‌
> 
> Then later for investment/redemption flow:
> 
> * add INVESTMENT\_APPROVED / REDEMPTION\_APPROVED to this enum
> * how to populate:
> 
>     * projection on investment/redemption will endpoint on goal svc to upsert this table
>     * OR emit kafka message from investment/redemption, and goal subscribe and upsert this table
>     
> 
> ‌
> 
> Then later, if ever, for adhoc documents upload to a goal:
> 
> * endpoint to persist event to goal, which go thru projection to upsert this table
> 
> ‌
> 
> How to upversion this table?
> 
> * table design is already as flexible as possible
> * if really to upversion, we just need new projection in goal & sync from investment/redemption
> 
> ‌

**Conditions and limits:**

- Investment/redemption may later upsert via goal endpoint or Kafka; both are alternatives, not a settled implementation. Adhoc upload can persist an event; table upversion can use a new goal projection and sync.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:347 · comment 564025013 · PR 10335 · 2024-11-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataTableV1.scala`

**Evidence:** anon-2.jsonl:347 · comment 564025013 · PR 10335 · 2024-11-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataTableV1.scala`

**Explicit source context (pr_title):**

> Feat/INV-3508 goal create projections

## A2-0435 — Review: How to persist documentIds for goal? One approach could be below \(we can review again later\)

**Source stance:** suggestion

**Context:**

> PR 10262 (Feat/INV-3637 bff endpoint upload document), no inline path; original row 435.

**Source-preserving request, proposal, or question:**

> How to persist documentIds for goal? One approach could be below \(we can review again later\)
> 
> * projection on `GoalCreationApprovedEvt`
> 
>     * take approved workflowId, calls workflow-engine to query associated request payload
>     * extract documentIds \(goal-impl depends on advisory-api \+ workflow-engine-api\) and persist to CRUD table for \(goalId \+ context\) → documentIds\[\]
>     
> * if we ever have adhoc docs upload per goal
> 
>     * if there is event, persist to CRUD table via projection
>     * if there is no event, persist to CRUD table directly
>     
> 
> ‌
> 
> If we ever have docs for other flow, e.g. investment/redemption/etc
> 
> * follow same approach as goal svc
> * `GET /api/v1/goal/:goalId/document` must compose from all underlying sources including goal \+ investment/redemption/etc
> 
> ‌

**Conditions and limits:**

- Document persistence via GoalCreationApprovedEvt projection is explicitly one possible design for later review; event/no-event adhoc paths are alternatives.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:435 · comment 559297294 · PR 10262 · 2024-10-30

**Evidence:** anon-2.jsonl:435 · comment 559297294 · PR 10262 · 2024-10-30

**Explicit source context (pr_title):**

> Feat/INV-3637 bff endpoint upload document

## A2-0483 — Review: ## SG

**Source stance:** explanation

**Context:**

> PR 10237 ([INV-3628] feat(advisory): Add eligibleForProjection flag to indicate to FE whether to display projection chart), no inline path; original row 483.

**Concern stated in the source:** ## SG

### Add goal

CoreEnhanced:

* portfolio-summary: add `eligibleForProjection` following projection condition

FundSmart:

* portfolio-summary: add `eligibleForProjection` following projection condition \+ multifund condition \(cannot check GWA vs CMA yet\)
* summary: add `eligibleForProjection` following projection condition \+ multifund-GWA condition

### Invest

CoreEnhanced:

* portfolio-summary: add `eligibleForProjection` following projection condition

FundSmart:

* summary: add `eligibleForProjection` following projection condition \+ multifund-GWA condition
* since there is no portfolio-summary here, FE will first call summary with fake amount to check `eligibleForProjection` before displaying the investment amount screen

### Modify goal

If return zeroed projection result, FE knows how to hide it, as it is separate steps

CoreEnhanced:

* summary: don’t calculate projection if empty goal

FundSmart:

* summary: don’t calculate projection if empty goal OR not multifund-GWA

---

## HK

### Add goal

FundSmart:

* portfolio-summary: add `eligibleForProjection` following projection condition \+ multifund condition \(cannot check GWA vs CMA yet\)

### Invest

FundSmart:

* portfolio-summary: add `eligibleForProjection` following projection condition \+ multifund-GWA condition

### Modify goal

If return zeroed projection result, FE knows how to hide it, as it is separate steps

FundSmart:

* summary: don’t calculate projection if empty goal OR not multifund-GWA

‌

**Source-preserving request, proposal, or question:**

> ## SG
> 
> ### Add goal
> 
> CoreEnhanced:
> 
> * portfolio-summary: add `eligibleForProjection` following projection condition
> 
> FundSmart:
> 
> * portfolio-summary: add `eligibleForProjection` following projection condition \+ multifund condition \(cannot check GWA vs CMA yet\)
> * summary: add `eligibleForProjection` following projection condition \+ multifund-GWA condition
> 
> ### Invest
> 
> CoreEnhanced:
> 
> * portfolio-summary: add `eligibleForProjection` following projection condition
> 
> FundSmart:
> 
> * summary: add `eligibleForProjection` following projection condition \+ multifund-GWA condition
> * since there is no portfolio-summary here, FE will first call summary with fake amount to check `eligibleForProjection` before displaying the investment amount screen
> 
> ### Modify goal
> 
> If return zeroed projection result, FE knows how to hide it, as it is separate steps
> 
> CoreEnhanced:
> 
> * summary: don’t calculate projection if empty goal
> 
> FundSmart:
> 
> * summary: don’t calculate projection if empty goal OR not multifund-GWA
> 
> ---
> 
> ## HK
> 
> ### Add goal
> 
> FundSmart:
> 
> * portfolio-summary: add `eligibleForProjection` following projection condition \+ multifund condition \(cannot check GWA vs CMA yet\)
> 
> ### Invest
> 
> FundSmart:
> 
> * portfolio-summary: add `eligibleForProjection` following projection condition \+ multifund-GWA condition
> 
> ### Modify goal
> 
> If return zeroed projection result, FE knows how to hide it, as it is separate steps
> 
> FundSmart:
> 
> * summary: don’t calculate projection if empty goal OR not multifund-GWA
> 
> ‌

**Conditions and limits:**

- The source is a per-region, per-product, per-flow matrix. Preserve all distinctions, including multifund-only before GWA/CMA is known, fake-amount SG invest-summary call, and zeroed modify-goal projections.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:483 · comment 557412639 · PR 10237 · 2024-10-25

**Evidence:** anon-2.jsonl:483 · comment 557412639 · PR 10237 · 2024-10-25

**Explicit source context (pr_title):**

> [INV-3628] feat(advisory): Add eligibleForProjection flag to indicate to FE whether to display projection chart

## A2-0484 — PortfolioStatsJdbcTable: I don’t create these index in V2:

**Source stance:** explanation

**Context:**

> PR 10219 ([INV-3618] feat(projection)(performance): Add validation for PortfolioStats to be older than 2007 before generating simulation result), projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/portfolioStats/PortfolioStatsJdbcTable.scala; original row 484.

**Concern stated in the source:** I don’t create these index in V2:

* portfolioId: 1st field in composite pk, no need additional index
* effectiveDate: not very useful field to query alone without portfolioId
* statsCcy: not very good field to index, as we only have a handful of ccy

‌

**Source-preserving request, proposal, or question:**

> I don’t create these index in V2:
> 
> * portfolioId: 1st field in composite pk, no need additional index
> * effectiveDate: not very useful field to query alone without portfolioId
> * statsCcy: not very good field to index, as we only have a handful of ccy
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:484 · comment 556612117 · PR 10219 · 2024-10-23

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/portfolioStats/PortfolioStatsJdbcTable.scala`

**Evidence:** anon-2.jsonl:484 · comment 556612117 · PR 10219 · 2024-10-23

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/portfolioStats/PortfolioStatsJdbcTable.scala`

**Explicit source context (pr_title):**

> [INV-3618] feat(projection)(performance): Add validation for PortfolioStats to be older than 2007 before generating simulation result

## A2-0520 — HkFeeManagerProjection: There is no tax in HK at all, so maybe simpler solution would be to have `HkFeeManagerProjection` only handle `FeeChargeDiscountAppliedEvt` which would t...

**Source stance:** suggestion

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkFeeManagerProjection.scala; original row 520.

**Concern stated in the source:** There is no tax in HK at all, so maybe simpler solution would be to have `HkFeeManagerProjection` only handle `FeeChargeDiscountAppliedEvt` which would trigger `InitiateFeeRedemptionCmd` always.

Original intention of making `FeeManagerProjection` region aware is that we can support different discount/tax flow \(not just basic injection of taxHelper\). E.g. South Korean would tax first and discount later

**Source-preserving request, proposal, or question:**

> There is no tax in HK at all, so maybe simpler solution would be to have `HkFeeManagerProjection` only handle `FeeChargeDiscountAppliedEvt` which would trigger `InitiateFeeRedemptionCmd` always.
> 
> Original intention of making `FeeManagerProjection` region aware is that we can support different discount/tax flow \(not just basic injection of taxHelper\). E.g. South Korean would tax first and discount later

**Conditions and limits:**

- HK no-tax handling and possible South Korean tax-before-discount are region-flow examples; future flows are not implemented facts.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:520 · comment 547220574 · PR 10103 · 2024-10-01

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkFeeManagerProjection.scala`

**Evidence:** anon-2.jsonl:520 · comment 547220574 · PR 10103 · 2024-10-01

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkFeeManagerProjection.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0523 — HkFeeManagerProjection: HK simply doesnt have any tax for investment. And as you can see, it’s very simple to add when the gov changes this, if ever. If they actually do that, w...

**Source stance:** suggestion

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkFeeManagerProjection.scala; original row 523.

**Concern stated in the source:** HK simply doesnt have any tax for investment. And as you can see, it’s very simple to add when the gov changes this, if ever. If they actually do that, we do not know if tax is applied before or after discount. There is no point adding all these code based on this assumption right now

**Source-preserving request, proposal, or question:**

> HK simply doesnt have any tax for investment. And as you can see, it’s very simple to add when the gov changes this, if ever. If they actually do that, we do not know if tax is applied before or after discount. There is no point adding all these code based on this assumption right now

**Conditions and limits:**

- Source describes HK tax at that historical point and rejects speculative ordering assumptions for hypothetical future tax.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:523 · comment 547871630 · PR 10103 · 2024-10-03

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkFeeManagerProjection.scala`

**Evidence:** anon-2.jsonl:523 · comment 547871630 · PR 10103 · 2024-10-03

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkFeeManagerProjection.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0527 — HkChargeCommunicationEventProcessor: Can we name this `HkChargeCommunicationProjection` instead? Previously these were named `*EventProcessor` because of Lagom pattern

**Source stance:** suggestion

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationEventProcessor.scala; original row 527.

**Concern stated in the source:** Can we name this `HkChargeCommunicationProjection` instead? Previously these were named `*EventProcessor` because of Lagom pattern

**Source-preserving request, proposal, or question:**

> Can we name this `HkChargeCommunicationProjection` instead? Previously these were named `*EventProcessor` because of Lagom pattern

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:527 · comment 549736511 · PR 10103 · 2024-10-07

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationEventProcessor.scala`

**Evidence:** anon-2.jsonl:527 · comment 549736511 · PR 10103 · 2024-10-07

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationEventProcessor.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0530 — HkFeeManagerProjection: No need for-comprehend block here

**Source stance:** suggestion

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkFeeManagerProjection.scala; original row 530.

**Source-preserving request, proposal, or question:**

> No need for-comprehend block here

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:530 · comment 549739387 · PR 10103 · 2024-10-07

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkFeeManagerProjection.scala`

**Evidence:** anon-2.jsonl:530 · comment 549739387 · PR 10103 · 2024-10-07

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkFeeManagerProjection.scala`

**Explicit source context (hunk):**

> +      .ask(
> +        InitiateFeeRedemptionCmd(
> +          _,
> +          feeChargeRequestId = feeChargeRequestId
> +        )
> +      )
> +  }

**Evidence:** anon-2.jsonl:530 · comment 549739387 · PR 10103 · 2024-10-07

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkFeeManagerProjection.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0541 — HkChargeCommunicationProjection: These don’t need to be val

**Source stance:** suggestion

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala; original row 541.

**Source-preserving request, proposal, or question:**

> These don’t need to be val

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:541 · comment 550147978 · PR 10103 · 2024-10-08

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala`

**Evidence:** anon-2.jsonl:541 · comment 550147978 · PR 10103 · 2024-10-08

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala`

**Explicit source context (hunk):**

> +class HkChargeCommunicationProjection(
> +  cassandraSession: CassandraSession,
> +  goalService: HkGoalService,
> +  platformNotificationTopicProducerDirect: PlatformNotificationTopicProducerDirect,
> +  dateTimeProvider: DateTimeProvider,
> +)(implicit val ec: ExecutionContext, system: ActorSystem)
> +    extends StrictLogging {

**Evidence:** anon-2.jsonl:541 · comment 550147978 · PR 10103 · 2024-10-08

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0544 — HkChargeCommunicationProjection: This logic actually exists in `InitiateFeeRedemptionCmdHandler`, it’s best we rely on sequence of events, rather than duplicating it again.

**Source stance:** suggestion

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala; original row 544.

**Concern stated in the source:** This logic actually exists in `InitiateFeeRedemptionCmdHandler`, it’s best we rely on sequence of events, rather than duplicating it again.

The communication logic in fact can be region agnostic as well \(the same way `InitiateFeeRedemptionCmdHandler` doesn’t care about sg or hk\). We can simply use the `redemptionDetails` \(instead of using amount from `discountDetails`, and having to assume that there is no tax involved\)

```
event.feeChargeRequest.redemptionDetails match {
  case Some(redemptionDetails) =>
    redemptionDetails.redeemedAmount match {
      case Some(chargeAmount) =>
        ...communication logic goes here...
      case None =>
        logger.error("... <unexpected-please-check> ... ")
        Future.successful(Done)
    }
  case None =>
    // waived without vouchers
    Future.successful(Done)
}
```

‌

**Source-preserving request, proposal, or question:**

> This logic actually exists in `InitiateFeeRedemptionCmdHandler`, it’s best we rely on sequence of events, rather than duplicating it again.
> 
> The communication logic in fact can be region agnostic as well \(the same way `InitiateFeeRedemptionCmdHandler` doesn’t care about sg or hk\). We can simply use the `redemptionDetails` \(instead of using amount from `discountDetails`, and having to assume that there is no tax involved\)
> 
> ```
> event.feeChargeRequest.redemptionDetails match {
>   case Some(redemptionDetails) =>
>     redemptionDetails.redeemedAmount match {
>       case Some(chargeAmount) =>
>         ...communication logic goes here...
>       case None =>
>         logger.error("... <unexpected-please-check> ... ")
>         Future.successful(Done)
>     }
>   case None =>
>     // waived without vouchers
>     Future.successful(Done)
> }
> ```
> 
> ‌

**Conditions and limits:**

- Communication follows FeeChargeCompletedEvt redemptionDetails: Some redeemedAmount sends; missing redeemedAmount logs unexpected and returns Done; None redemptionDetails is waived without vouchers and returns Done.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:544 · comment 550155826 · PR 10103 · 2024-10-08

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala`

**Evidence:** anon-2.jsonl:544 · comment 550155826 · PR 10103 · 2024-10-08

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0548 — HkChargeCommunicationProjection: Can we put meaningful message here? Maybe sth along the line of `Skipping communication for FeeChargeCompletedEvt of planId $planId, feeChargeRe...

**Source stance:** suggestion

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala; original row 548.

**Concern stated in the source:** Can we put meaningful message here? Maybe sth along the line of `Skipping communication for FeeChargeCompletedEvt of planId $planId, feeChargeRequest $feeChargeRequestId due to missing redeemedAmount in redemptionDetails`

**Source-preserving request, proposal, or question:**

> Can we put meaningful message here? Maybe sth along the line of `Skipping communication for FeeChargeCompletedEvt of planId $planId, feeChargeRequest $feeChargeRequestId due to missing redeemedAmount in redemptionDetails`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:548 · comment 550175721 · PR 10103 · 2024-10-08

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala`

**Evidence:** anon-2.jsonl:548 · comment 550175721 · PR 10103 · 2024-10-08

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0552 — SgGoalCreateInvestmentSummaryBehaviour: [person] [person] Looks like we look up `portfolio` here, but only use id and effectiveDate from it - these are already available in `pro...

**Source stance:** suggestion

**Context:**

> PR 10043 ([INV-3488] feat(advisory, charge): Enable portfolio (for advisory flow) and investment summaries (for execution only flow)), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateInvestmentSummaryBehaviour.scala; original row 552.

**Concern stated in the source:** [person] [person] Looks like we look up `portfolio` here, but only use id and effectiveDate from it - these are already available in `productPortfolio`. If indeed no need to lookup again, maybe we just split this into 2 methods, so that we can call them independently, instead of this `calculatePortfolioProjection`?

**Source-preserving request, proposal, or question:**

> [person] [person] Looks like we look up `portfolio` here, but only use id and effectiveDate from it - these are already available in `productPortfolio`. If indeed no need to lookup again, maybe we just split this into 2 methods, so that we can call them independently, instead of this `calculatePortfolioProjection`?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:552 · comment 550425625 · PR 10043 · 2024-10-09

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateInvestmentSummaryBehaviour.scala`

> Looks like we look up `portfolio` here, but only use id and effectiveDate from it - these are already available in `productPortfolio`. If indeed no need to lookup again, maybe we just split this into 2 methods, so that we can call them independently, instead of this `calculatePortfolioProjection`?

**Evidence:** anon-2.jsonl:552 · comment 550425625 · PR 10043 · 2024-10-09

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateInvestmentSummaryBehaviour.scala`

**Explicit source context (pr_title):**

> [INV-3488] feat(advisory, charge): Enable portfolio (for advisory flow) and investment summaries (for execution only flow)

## A2-0597 — ModelPortfolioEntity: So there are 2 events:

**Source stance:** suggestion

**Context:**

> PR 10034 (Resolve INV-3485: Changes to wait for response in subscriber, react to PortfolioAllocationTargetUpdatedMsg in rebalance.), portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/ModelPortfolioEntity.scala; original row 597.

**Concern stated in the source:** So there are 2 events:

* `PortfolioMovedToNewAllocationTargetEvt` is purely for TAA change. You can see `handleUpdateCurrentAllocationTargetCmd` \(the real cmd handler for emitting this evt\) only checks `effectiveDate` and `List[AllocationTarget]`
* `PortfolioAllocationTargetUpdatedEvt` is intended to update underlying instrument profile \(of the `AllocationTarget`\). We don’t really need this evt for the clone purpose. And even if needed, it should come via the instrument cloning instead.

‌

Advisory’s ProductPortfolio handles both PortfolioMovedToNewAllocationTargetMsg and PortfolioAllocationTargetUpdatedMsg. I don’t remember if we have migrated everything to refresh instrument data always, but this entity has a rework as we discussed in the past \(it just needs to store the tagging, and fetch fresh or projection portfolio/instrument data\). I think until then, let’s just leave it.

‌

**Source-preserving request, proposal, or question:**

> So there are 2 events:
> 
> * `PortfolioMovedToNewAllocationTargetEvt` is purely for TAA change. You can see `handleUpdateCurrentAllocationTargetCmd` \(the real cmd handler for emitting this evt\) only checks `effectiveDate` and `List[AllocationTarget]`
> * `PortfolioAllocationTargetUpdatedEvt` is intended to update underlying instrument profile \(of the `AllocationTarget`\). We don’t really need this evt for the clone purpose. And even if needed, it should come via the instrument cloning instead.
> 
> ‌
> 
> Advisory’s ProductPortfolio handles both PortfolioMovedToNewAllocationTargetMsg and PortfolioAllocationTargetUpdatedMsg. I don’t remember if we have migrated everything to refresh instrument data always, but this entity has a rework as we discussed in the past \(it just needs to store the tagging, and fetch fresh or projection portfolio/instrument data\). I think until then, let’s just leave it.
> 
> ‌

**Conditions and limits:**

- Keep TAA/effectiveDate change events separate from instrument-profile update events. ProductPortfolio still handles both, with broader redesign deferred.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:597 · comment 545564269 · PR 10034 · 2024-09-25

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/ModelPortfolioEntity.scala`

**Evidence:** anon-2.jsonl:597 · comment 545564269 · PR 10034 · 2024-09-25

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/ModelPortfolioEntity.scala`

**Explicit source context (pr_title):**

> Resolve INV-3485: Changes to wait for response in subscriber, react to PortfolioAllocationTargetUpdatedMsg in rebalance.

## A2-0608 — PortfolioTopicSubscriber: This can move outside right? We don’t need to do this for every ccy

**Source stance:** suggestion

**Context:**

> PR 9911 (Feat/INV-3336 marketdata cleanup phase 3), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/subscribers/PortfolioTopicSubscriber.scala; original row 608.

**Concern stated in the source:** This can move outside right? We don’t need to do this for every ccy

Same for 2 sync methods in ServiceLogicImpl

**Source-preserving request, proposal, or question:**

> This can move outside right? We don’t need to do this for every ccy
> 
> Same for 2 sync methods in ServiceLogicImpl

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:608 · comment 537966153 · PR 9911 · 2024-09-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/subscribers/PortfolioTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:608 · comment 537966153 · PR 9911 · 2024-09-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/subscribers/PortfolioTopicSubscriber.scala`

**Explicit source context (pr_title):**

> Feat/INV-3336 marketdata cleanup phase 3

## A2-0610 — ServiceLogicImpl: I mean move this outside too. No need to bulkUpsert this for every ccy cuz this table doesn’t care about marketCcy

**Source stance:** suggestion

**Context:**

> PR 9911 (Feat/INV-3336 marketdata cleanup phase 3), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; original row 610.

**Concern stated in the source:** I mean move this outside too. No need to bulkUpsert this for every ccy cuz this table doesn’t care about marketCcy

Same for below method and the subscriber

**Source-preserving request, proposal, or question:**

> I mean move this outside too. No need to bulkUpsert this for every ccy cuz this table doesn’t care about marketCcy
> 
> Same for below method and the subscriber

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:610 · comment 538049671 · PR 9911 · 2024-09-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:610 · comment 538049671 · PR 9911 · 2024-09-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/INV-3336 marketdata cleanup phase 3

## A2-0651 — package: We need projection too?

**Source stance:** open-question

**Context:**

> PR 9715 ([INV-3238] feat(advisory): create apis for goal modify flow), advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/goalmodify/package.scala; original row 651.

**Source-preserving request, proposal, or question:**

> We need projection too?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:651 · comment 531574112 · PR 9715 · 2024-08-16

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/goalmodify/package.scala`

**Evidence:** anon-2.jsonl:651 · comment 531574112 · PR 9715 · 2024-08-16

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/goalmodify/package.scala`

**Explicit source context (pr_title):**

> [INV-3238] feat(advisory): create apis for goal modify flow

## A2-0662 — package: Should be required projection

**Source stance:** requested-change

**Context:**

> PR 9715 ([INV-3238] feat(advisory): create apis for goal modify flow), advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/goalmodify/package.scala; original row 662.

**Source-preserving request, proposal, or question:**

> Should be required projection

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:662 · comment 532700573 · PR 9715 · 2024-08-20

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/goalmodify/package.scala`

**Evidence:** anon-2.jsonl:662 · comment 532700573 · PR 9715 · 2024-08-20

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/goalmodify/package.scala`

**Explicit source context (pr_title):**

> [INV-3238] feat(advisory): create apis for goal modify flow

## A2-0678 — GoalTopicSubscriber: Nit: let’s assign `val portfolioId = plan.targetAssetAllocation.modelPortfolioId` then we can use it below as well

**Source stance:** suggestion

**Context:**

> PR 9818 ([INV-3409] feat: Handle DIY portfolio deletion on goal deletion), portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/subscribers/GoalTopicSubscriber.scala; original row 678.

**Concern stated in the source:** Nit: let’s assign `val portfolioId = plan.targetAssetAllocation.modelPortfolioId` then we can use it below as well

Also let’s add portfolioId to the error logging

**Source-preserving request, proposal, or question:**

> Nit: let’s assign `val portfolioId = plan.targetAssetAllocation.modelPortfolioId` then we can use it below as well
> 
> Also let’s add portfolioId to the error logging

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:678 · comment 534411582 · PR 9818 · 2024-08-23

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/subscribers/GoalTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:678 · comment 534411582 · PR 9818 · 2024-08-23

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/subscribers/GoalTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [INV-3409] feat: Handle DIY portfolio deletion on goal deletion

## A2-0697 — InstrumentPortfolioSubscribersDataRepository: Let’s do Source because this List will grow for popular instrument

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala; original row 697.

**Concern stated in the source:** Let’s do Source because this List will grow for popular instrument

**Source-preserving request, proposal, or question:**

> Let’s do Source because this List will grow for popular instrument

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:697 · comment 524603079 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala`

**Evidence:** anon-2.jsonl:697 · comment 524603079 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0711 — PortfolioMarketDataEventProcessor: Let’s move this to PortfolioTopicSubscriber. Eventually we should also handle `ModelPortfolioDeactivatedMsg` and delete from repo

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/portfolio/processors/PortfolioMarketDataEventProcessor.scala; original row 711.

**Concern stated in the source:** Let’s move this to PortfolioTopicSubscriber. Eventually we should also handle `ModelPortfolioDeactivatedMsg` and delete from repo

**Source-preserving request, proposal, or question:**

> Let’s move this to PortfolioTopicSubscriber. Eventually we should also handle `ModelPortfolioDeactivatedMsg` and delete from repo

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:711 · comment 524607269 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/portfolio/processors/PortfolioMarketDataEventProcessor.scala`

**Evidence:** anon-2.jsonl:711 · comment 524607269 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/portfolio/processors/PortfolioMarketDataEventProcessor.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0713 — PortfolioMonthlyChangesHelper: Let’s make this method handing the subscriber lookup \+ streaming the task \(in next task\), and keep the instrument projection simple.

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala; original row 713.

**Concern stated in the source:** Let’s make this method handing the subscriber lookup \+ streaming the task \(in next task\), and keep the instrument projection simple.

And just pass portfolioId \+ effectiveDate, no need `Subscriber`

**Source-preserving request, proposal, or question:**

> Let’s make this method handing the subscriber lookup \+ streaming the task \(in next task\), and keep the instrument projection simple.
> 
> And just pass portfolioId \+ effectiveDate, no need `Subscriber`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:713 · comment 524624318 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Evidence:** anon-2.jsonl:713 · comment 524624318 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0715 — PortfolioTopicSubscriber: Let’s add an if here to calculate only if not DIY

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/subscribers/PortfolioTopicSubscriber.scala; original row 715.

**Concern stated in the source:** Let’s add an if here to calculate only if not DIY

**Source-preserving request, proposal, or question:**

> Let’s add an if here to calculate only if not DIY

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:715 · comment 524629905 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/subscribers/PortfolioTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:715 · comment 524629905 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/subscribers/PortfolioTopicSubscriber.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0718 — PortfolioMonthlyChangesHelper: I think there are 2 types of race conditions we might see here:

**Source stance:** observed-defect

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala; original row 718.

**Concern stated in the source:** I think there are 2 types of race conditions we might see here:

1. We get event that instrument mc is updated, and we trigger this method which will query instrument mc from readside - that might not have latest data yet… cuz they are 2 independent projections

    * We override the data for the instrument being updated, but it’s not bullet proof, e.g. db projection is super lagged for some reason
    
        * event of instrumentA, its data A2 is overridden on top of existing readside A1 & B1
        * then event of instrumentB, its data B2 is overridden on top of stale A1 & B1
        
    
2. Multiple instruments might be updated at once, each of them triggering this method… their upsert might override each other

    * This was protected with Portfolio entity last time. So we might need some impl of optimistic locking here
    

‌

**Source-preserving request, proposal, or question:**

> I think there are 2 types of race conditions we might see here:
> 
> 1. We get event that instrument mc is updated, and we trigger this method which will query instrument mc from readside - that might not have latest data yet… cuz they are 2 independent projections
> 
>     * We override the data for the instrument being updated, but it’s not bullet proof, e.g. db projection is super lagged for some reason
>     
>         * event of instrumentA, its data A2 is overridden on top of existing readside A1 & B1
>         * then event of instrumentB, its data B2 is overridden on top of stale A1 & B1
>         
>     
> 2. Multiple instruments might be updated at once, each of them triggering this method… their upsert might override each other
> 
>     * This was protected with Portfolio entity last time. So we might need some impl of optimistic locking here
>     
> 
> ‌

**Conditions and limits:**

- Two separate races remain: independent projection lag can pair new B2 with stale A1 despite per-event override, and concurrent instrument-triggered portfolio upserts can overwrite each other. Optimistic locking is proposed as entity replacement protection.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:718 · comment 524670185 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Evidence:** anon-2.jsonl:718 · comment 524670185 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0753 — SplitCashReservationsForFullRedemptionFeeChargeCmdHandler: It starts from None, and then capture the fee charge amount so far for the full redemption. It might have 2 fee charge...

**Source stance:** explanation

**Context:**

> PR 9750 ([INV-3155] feat(redemption): Idempotency for fee redemption of full redemption), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SplitCashReservationsForFullRedemptionFeeChargeCmdHandler.scala; original row 753.

**Concern stated in the source:** It starts from None, and then capture the fee charge amount so far for the full redemption. It might have 2 fee charges, for prev and current quarter.

Existing impl in `OverrideRedemptionCashReservationsCmdHandler` do lookup from state, but since we already protect the idempotency here, we can simply apply the incremental amount

**Source-preserving request, proposal, or question:**

> It starts from None, and then capture the fee charge amount so far for the full redemption. It might have 2 fee charges, for prev and current quarter.
> 
> Existing impl in `OverrideRedemptionCashReservationsCmdHandler` do lookup from state, but since we already protect the idempotency here, we can simply apply the incremental amount

**Conditions and limits:**

- Accrued fee-charge amount begins None and can include prior plus current quarter. Protected idempotency permits incremental application rather than re-reading current state.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:753 · comment 530672407 · PR 9750 · 2024-08-13

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SplitCashReservationsForFullRedemptionFeeChargeCmdHandler.scala`

**Evidence:** anon-2.jsonl:753 · comment 530672407 · PR 9750 · 2024-08-13

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SplitCashReservationsForFullRedemptionFeeChargeCmdHandler.scala`

**Explicit source context (pr_title):**

> [INV-3155] feat(redemption): Idempotency for fee redemption of full redemption

## A2-0788 — InstrumentPortfolioSubscribersDataRepository: Let’s not put repository yet in this PR. Do join between this and mc table so we can dedupe in DB

**Source stance:** suggestion

**Context:**

> PR 9689 (Feat/INV-3361 instrument price monthly changes jdbc migration), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala; original row 788.

**Concern stated in the source:** Let’s not put repository yet in this PR. Do join between this and mc table so we can dedupe in DB

**Source-preserving request, proposal, or question:**

> Let’s not put repository yet in this PR. Do join between this and mc table so we can dedupe in DB

**Conditions and limits:**

- Join in DB should deduplicate instrument/MC records before repository surface is added.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:788 · comment 526840443 · PR 9689 · 2024-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala`

**Evidence:** anon-2.jsonl:788 · comment 526840443 · PR 9689 · 2024-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala`

**Explicit source context (pr_title):**

> Feat/INV-3361 instrument price monthly changes jdbc migration

## A2-0792 — InstrumentPortfolioSubscribersDataJdbcHandler: Take VO instead of individual fields. Set updatedAt outside

**Source stance:** suggestion

**Context:**

> PR 9689 (Feat/INV-3361 instrument price monthly changes jdbc migration), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataJdbcHandler.scala; original row 792.

**Concern stated in the source:** Take VO instead of individual fields. Set updatedAt outside

**Source-preserving request, proposal, or question:**

> Take VO instead of individual fields. Set updatedAt outside

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:792 · comment 526840233 · PR 9689 · 2024-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataJdbcHandler.scala`

**Evidence:** anon-2.jsonl:792 · comment 526840233 · PR 9689 · 2024-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataJdbcHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3361 instrument price monthly changes jdbc migration

## A2-0793 — InstrumentMarketDataJdbcProjection: Consider skipping old events, and sync to db separately to save cost processing old events we don’t care

**Source stance:** suggestion

**Context:**

> PR 9689 (Feat/INV-3361 instrument price monthly changes jdbc migration), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataJdbcProjection.scala; original row 793.

**Concern stated in the source:** Consider skipping old events, and sync to db separately to save cost processing old events we don’t care

**Source-preserving request, proposal, or question:**

> Consider skipping old events, and sync to db separately to save cost processing old events we don’t care

**Conditions and limits:**

- Skipping costly historical events and syncing DB separately is a proposal, not a verified safe migration sequence.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:793 · comment 526841921 · PR 9689 · 2024-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataJdbcProjection.scala`

**Evidence:** anon-2.jsonl:793 · comment 526841921 · PR 9689 · 2024-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataJdbcProjection.scala`

**Explicit source context (pr_title):**

> Feat/INV-3361 instrument price monthly changes jdbc migration

## A2-0796 — InstrumentPortfolioSubscribersDataRepository: Just `streamInstrumentPortfolioSubscribers` ?

**Source stance:** suggestion

**Context:**

> PR 9689 (Feat/INV-3361 instrument price monthly changes jdbc migration), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala; original row 796.

**Source-preserving request, proposal, or question:**

> Just `streamInstrumentPortfolioSubscribers` ?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:796 · comment 528897605 · PR 9689 · 2024-08-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala`

**Evidence:** anon-2.jsonl:796 · comment 528897605 · PR 9689 · 2024-08-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala`

**Explicit source context (hunk):**

> +  private val instrumentPortfolioSubscribersDataTable = TableQuery[InstrumentPortfolioSubscribersDataTable]
> +
> +  def streamInstrumentPortfolioSubscribers(instrumentId: String): Source[InstrumentPortfolioSubscribersDataVo, NotUsed] = {
> +    Slick.source(
> +      instrumentPortfolioSubscribersDataTable
> +        .filter(_.instrumentId === instrumentId)
> +        .result

**Evidence:** anon-2.jsonl:796 · comment 528897605 · PR 9689 · 2024-08-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala`

**Explicit source context (pr_title):**

> Feat/INV-3361 instrument price monthly changes jdbc migration

## A2-0800 — InstrumentMarketDataJdbcProjection: Since we are skipping old events, just don’t handle this event anymore? Can just put a comment

**Source stance:** suggestion

**Context:**

> PR 9689 (Feat/INV-3361 instrument price monthly changes jdbc migration), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataJdbcProjection.scala; original row 800.

**Concern stated in the source:** Since we are skipping old events, just don’t handle this event anymore? Can just put a comment

**Source-preserving request, proposal, or question:**

> Since we are skipping old events, just don’t handle this event anymore? Can just put a comment

**Conditions and limits:**

- This event can be unhandled only because historical events are being skipped; document that choice.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:800 · comment 528898388 · PR 9689 · 2024-08-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataJdbcProjection.scala`

**Evidence:** anon-2.jsonl:800 · comment 528898388 · PR 9689 · 2024-08-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataJdbcProjection.scala`

**Explicit source context (pr_title):**

> Feat/INV-3361 instrument price monthly changes jdbc migration

## A2-0802 — PortfolioTopicSubscriber: Yea definitely bulkUpsert here

**Source stance:** suggestion

**Context:**

> PR 9689 (Feat/INV-3361 instrument price monthly changes jdbc migration), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/subscribers/PortfolioTopicSubscriber.scala; original row 802.

**Concern stated in the source:** Yea definitely bulkUpsert here

**Source-preserving request, proposal, or question:**

> Yea definitely bulkUpsert here

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:802 · comment 528901460 · PR 9689 · 2024-08-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/subscribers/PortfolioTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:802 · comment 528901460 · PR 9689 · 2024-08-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/subscribers/PortfolioTopicSubscriber.scala`

**Explicit source context (pr_title):**

> Feat/INV-3361 instrument price monthly changes jdbc migration

## A2-0806 — TopicSubscriber: We should also bake in the Kamon Context propagation in this processing flow \(with option to opt out maybe if needed\)

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala; original row 806.

**Concern stated in the source:** We should also bake in the Kamon Context propagation in this processing flow \(with option to opt out maybe if needed\)

See current impl for Lagom at `KamonUtils.runWithKamonContext` and `KamonUtils.propagateMessage`

**Source-preserving request, proposal, or question:**

> We should also bake in the Kamon Context propagation in this processing flow \(with option to opt out maybe if needed\)
> 
> See current impl for Lagom at `KamonUtils.runWithKamonContext` and `KamonUtils.propagateMessage`

**Conditions and limits:**

- Kamon propagation is proposed as built-in with possible opt-out, citing runWithKamonContext and propagateMessage.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:806 · comment 516350468 · PR 9440 · 2024-07-02

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

**Evidence:** anon-2.jsonl:806 · comment 516350468 · PR 9440 · 2024-07-02

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0811 — TopicSubscriber: We should use `topicSubscriberSettings.parallelism` here?

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala; original row 811.

**Concern stated in the source:** We should use `topicSubscriberSettings.parallelism` here?

**Source-preserving request, proposal, or question:**

> We should use `topicSubscriberSettings.parallelism` here?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:811 · comment 516347874 · PR 9440 · 2024-07-02

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

**Evidence:** anon-2.jsonl:811 · comment 516347874 · PR 9440 · 2024-07-02

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0812 — TopicSubscriber: I realize the `ScaladslKafkaSubscriber` additionally set the below

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala; original row 812.

**Concern stated in the source:** I realize the `ScaladslKafkaSubscriber` additionally set the below

```
// Consumer must have a unique clientId otherwise a javax.management.InstanceAlreadyExistsException is thrown
.withClientId(s"${info.serviceName}-$consumerId")
```

‌

**Source-preserving request, proposal, or question:**

> I realize the `ScaladslKafkaSubscriber` additionally set the below
> 
> ```
> // Consumer must have a unique clientId otherwise a javax.management.InstanceAlreadyExistsException is thrown
> .withClientId(s"${info.serviceName}-$consumerId")
> ```
> 
> ‌

**Conditions and limits:**

- Kafka consumers require distinct clientId to avoid javax.management.InstanceAlreadyExistsException; the proposed format is serviceName-consumerId.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:812 · comment 516352790 · PR 9440 · 2024-07-02

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

**Evidence:** anon-2.jsonl:812 · comment 516352790 · PR 9440 · 2024-07-02

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0813 — BrokerOrderTopicSubscriber: Lagom is using below by default

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/subscribers/BrokerOrderTopicSubscriber.scala; original row 813.

**Concern stated in the source:** Lagom is using below by default

```
lagom.broker.kafka {
  client {
    default {
      # Exponential backoff for failures
      failure-exponential-backoff {
        # minimum (initial) duration until processor is started again
        # after failure
        min = 3s

        # the exponential back-off is capped to this duration
        max = 30s

        # additional random delay is based on this factor
        random-factor = 0.2
      }
    }
  }
}
```

‌

**Source-preserving request, proposal, or question:**

> Lagom is using below by default
> 
> ```
> lagom.broker.kafka {
>   client {
>     default {
>       # Exponential backoff for failures
>       failure-exponential-backoff {
>         # minimum (initial) duration until processor is started again
>         # after failure
>         min = 3s
> 
>         # the exponential back-off is capped to this duration
>         max = 30s
> 
>         # additional random delay is based on this factor
>         random-factor = 0.2
>       }
>     }
>   }
> }
> ```
> 
> ‌

**Conditions and limits:**

- The quoted Lagom default is exponential-backoff min=3s, max=30s, random-factor=0.2.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:813 · comment 516353645 · PR 9440 · 2024-07-02

Source path: `timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/subscribers/BrokerOrderTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:813 · comment 516353645 · PR 9440 · 2024-07-02

Source path: `timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/subscribers/BrokerOrderTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0814 — TopicSubscriber: In the TaskTopicSubscribers, these are used to retry processing individual message \(before dropping them\). Here you’re using as config to restart the subscrip...

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala; original row 814.

**Concern stated in the source:** In the TaskTopicSubscribers, these are used to retry processing individual message \(before dropping them\). Here you’re using as config to restart the subscription when it terminates unexpectedly. Maybe we should rename these fields a bit.

**Source-preserving request, proposal, or question:**

> In the TaskTopicSubscribers, these are used to retry processing individual message \(before dropping them\). Here you’re using as config to restart the subscription when it terminates unexpectedly. Maybe we should rename these fields a bit.

**Conditions and limits:**

- Retrying an individual task message before dropping it differs from restarting a terminated subscription; configuration names should distinguish them.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:814 · comment 516348152 · PR 9440 · 2024-07-02

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

**Evidence:** anon-2.jsonl:814 · comment 516348152 · PR 9440 · 2024-07-02

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0816 — TopicSubscriber: [person] As discussed, it’s actually not safe to blindly increase `parallelism` here when consuming messages from same partition \(only safe for the task topic\).

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala; original row 816.

**Concern stated in the source:** [person] As discussed, it’s actually not safe to blindly increase `parallelism` here when consuming messages from same partition \(only safe for the task topic\).

Maybe we can be very opinionated about this:

* `TopicSubscriber` should force `parallelism = 1`
* And another flavor say TopicParallelSubscriber that support say parallel msg processing using the safeMapAsync

‌

**Source-preserving request, proposal, or question:**

> [person] As discussed, it’s actually not safe to blindly increase `parallelism` here when consuming messages from same partition \(only safe for the task topic\).
> 
> Maybe we can be very opinionated about this:
> 
> * `TopicSubscriber` should force `parallelism = 1`
> * And another flavor say TopicParallelSubscriber that support say parallel msg processing using the safeMapAsync
> 
> ‌

**Conditions and limits:**

- Normal same-partition topic delivery should force parallelism=1; only task-topic processing is described as safe to parallelize. Another TopicParallelSubscriber with safeMapAsync is proposed.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:816 · comment 516749511 · PR 9440 · 2024-07-03

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

> As discussed, it’s actually not safe to blindly increase `parallelism` here when consuming messages from same partition \(only safe for the task topic\).
> 
> Maybe we can be very opinionated about this:
> 
> * `TopicSubscriber` should force `parallelism = 1`
> * And another flavor say TopicParallelSubscriber that support say parallel msg processing using the safeMapAsync
> 
> ‌

**Evidence:** anon-2.jsonl:816 · comment 516749511 · PR 9440 · 2024-07-03

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0817 — ServiceClientConfig: typesafe config would already throw `ConfigException.Missing` if not set

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), akka-client-commons/src/main/scala/com/endowus/silver/client/ServiceClientConfig.scala; original row 817.

**Concern stated in the source:** typesafe config would already throw `ConfigException.Missing` if not set

```
public Missing(ConfigOrigin origin, String path) {
    this(origin, "No configuration setting found for key '" + path + "'", null);
}
```

‌

Do we need all these if else \+ throw with customised msg? Same for topic subscriber settings

**Source-preserving request, proposal, or question:**

> typesafe config would already throw `ConfigException.Missing` if not set
> 
> ```
> public Missing(ConfigOrigin origin, String path) {
>     this(origin, "No configuration setting found for key '" + path + "'", null);
> }
> ```
> 
> ‌
> 
> Do we need all these if else \+ throw with customised msg? Same for topic subscriber settings

**Conditions and limits:**

- Typesafe config already throws ConfigException.Missing with the missing path, so custom duplicated checks are questioned.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:817 · comment 525232408 · PR 9440 · 2024-07-26

Source path: `akka-client-commons/src/main/scala/com/endowus/silver/client/ServiceClientConfig.scala`

**Evidence:** anon-2.jsonl:817 · comment 525232408 · PR 9440 · 2024-07-26

Source path: `akka-client-commons/src/main/scala/com/endowus/silver/client/ServiceClientConfig.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0850 — AdvisedGoalCreateHelper: This should be Option. For those request that still have the `initialInvestmentAmount` sent from FE, they can resolve from there. For CoreEnhanced/Flags...

**Source stance:** suggestion

**Context:**

> PR 9605 ([INV-3236] feat(advisory): create advisory endpoints for goal create), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/AdvisedGoalCreateHelper.scala; original row 850.

**Concern stated in the source:** This should be Option. For those request that still have the `initialInvestmentAmount` sent from FE, they can resolve from there. For CoreEnhanced/FlagshipDpm, we should just use the `initialFundingInstructions: Option[FundingInstructionsRequest]` without additional resolve call.

‌

Then when we convert to `startingAmount`, that can default to 0 if not set. But eventually, projection svc should give better API that understands `FundingInstructionsRequest` instead

**Source-preserving request, proposal, or question:**

> This should be Option. For those request that still have the `initialInvestmentAmount` sent from FE, they can resolve from there. For CoreEnhanced/FlagshipDpm, we should just use the `initialFundingInstructions: Option[FundingInstructionsRequest]` without additional resolve call.
> 
> ‌
> 
> Then when we convert to `startingAmount`, that can default to 0 if not set. But eventually, projection svc should give better API that understands `FundingInstructionsRequest` instead

**Conditions and limits:**

- Initial funding request should remain Option; legacy initialInvestmentAmount resolves when present, CoreEnhanced/FlagshipDpm can pass Option[FundingInstructionsRequest] directly; startingAmount may default 0 while better projection API is future work.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:850 · comment 524907405 · PR 9605 · 2024-07-25

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/AdvisedGoalCreateHelper.scala`

**Evidence:** anon-2.jsonl:850 · comment 524907405 · PR 9605 · 2024-07-25

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/AdvisedGoalCreateHelper.scala`

**Explicit source context (pr_title):**

> [INV-3236] feat(advisory): create advisory endpoints for goal create

## A2-0855 — ProjectionServiceE4s: Use config instead so that we can switch by just updating manifest, instead of having to build image for projection or releasing caller services

**Source stance:** suggestion

**Context:**

> PR 9627 ([INV-3334] feat(projection): Added switch to default for on-the-fly), projection-api/src/main/scala/com/endowus/silver/projection/api/ProjectionServiceE4s.scala; original row 855.

**Concern stated in the source:** Use config instead so that we can switch by just updating manifest, instead of having to build image for projection or releasing caller services

**Source-preserving request, proposal, or question:**

> Use config instead so that we can switch by just updating manifest, instead of having to build image for projection or releasing caller services

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:855 · comment 524577938 · PR 9627 · 2024-07-24

Source path: `projection-api/src/main/scala/com/endowus/silver/projection/api/ProjectionServiceE4s.scala`

**Evidence:** anon-2.jsonl:855 · comment 524577938 · PR 9627 · 2024-07-24

Source path: `projection-api/src/main/scala/com/endowus/silver/projection/api/ProjectionServiceE4s.scala`

**Explicit source context (pr_title):**

> [INV-3334] feat(projection): Added switch to default for on-the-fly

## A2-0856 — ServiceLogicImpl: Move this as private val in `ServiceLogicImpl`

**Source stance:** suggestion

**Context:**

> PR 9627 ([INV-3334] feat(projection): Added switch to default for on-the-fly), projection-impl/src/main/scala/com/endowus/silver/projection/impl/logic/service/ServiceLogicImpl.scala; original row 856.

**Source-preserving request, proposal, or question:**

> Move this as private val in `ServiceLogicImpl`
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:856 · comment 525227971 · PR 9627 · 2024-07-26

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/logic/service/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:856 · comment 525227971 · PR 9627 · 2024-07-26

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-3334] feat(projection): Added switch to default for on-the-fly

## A2-0880 — ServiceLogicImpl: Should we add to FutureUtils… sth like `withTimer(timer: Timer, => T: Future[T])` and take care of proper start stop there? I suppose we don’t need to capture ...

**Source stance:** open-question

**Context:**

> PR 9525 ([INV-3185] feat(projection): Adhoc projection for queryPortfolioV4), projection-impl/src/main/scala/com/endowus/silver/projection/impl/logic/service/ServiceLogicImpl.scala; original row 880.

**Concern stated in the source:** Should we add to FutureUtils… sth like `withTimer(timer: Timer, => T: Future[T])` and take care of proper start stop there? I suppose we don’t need to capture for the `multiCcySimulationBatchManager.runAdHoc*Simulation` calls and not others?

**Source-preserving request, proposal, or question:**

> Should we add to FutureUtils… sth like `withTimer(timer: Timer, => T: Future[T])` and take care of proper start stop there? I suppose we don’t need to capture for the `multiCcySimulationBatchManager.runAdHoc*Simulation` calls and not others?

**Conditions and limits:**

- Timer helper needs by-name Future construction so it measures the intended work; the question also asks why only selected calls are timed.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:880 · comment 520053076 · PR 9525 · 2024-07-11

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/logic/service/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:880 · comment 520053076 · PR 9525 · 2024-07-11

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-3185] feat(projection): Adhoc projection for queryPortfolioV4

## A2-0881 — ServiceLogicImpl: A bit late to call with withTimer here cuz the future already started when you define above

**Source stance:** explanation

**Context:**

> PR 9525 ([INV-3185] feat(projection): Adhoc projection for queryPortfolioV4), projection-impl/src/main/scala/com/endowus/silver/projection/impl/logic/service/ServiceLogicImpl.scala; original row 881.

**Concern stated in the source:** A bit late to call with withTimer here cuz the future already started when you define above

**Source-preserving request, proposal, or question:**

> A bit late to call with withTimer here cuz the future already started when you define above

**Conditions and limits:**

- The future has already started before the shown withTimer use.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:881 · comment 520924007 · PR 9525 · 2024-07-15

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/logic/service/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:881 · comment 520924007 · PR 9525 · 2024-07-15

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-3185] feat(projection): Adhoc projection for queryPortfolioV4

## A2-0882 — EmailProviderData: All of these, in theory, would need to be optional. Cuz there might be existing message in the kafka topic without the fields, and communication svc starts ex...

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), communication-api/src/main/scala/com/endowus/silver/communication/api/v2/email/EmailProviderData.scala; original row 882.

**Concern stated in the source:** All of these, in theory, would need to be optional. Cuz there might be existing message in the kafka topic without the fields, and communication svc starts expecting new field to be required.

We will not release during the printing, but POps might still print adhoc statements every now and then. I think let’s play safe and make `statementType` optional.

**Source-preserving request, proposal, or question:**

> All of these, in theory, would need to be optional. Cuz there might be existing message in the kafka topic without the fields, and communication svc starts expecting new field to be required.
> 
> We will not release during the printing, but POps might still print adhoc statements every now and then. I think let’s play safe and make `statementType` optional.

**Conditions and limits:**

- Kafka may still contain messages without statementType even outside normal printing release windows because POps runs adhoc printing; source requests optionality.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:882 · comment 507791386 · PR 9240 · 2024-06-03

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/v2/email/EmailProviderData.scala`

**Evidence:** anon-2.jsonl:882 · comment 507791386 · PR 9240 · 2024-06-03

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/v2/email/EmailProviderData.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0888 — Semi-annual report rollout: include communication in services.list

**Source stance:** requested-change

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), kubernetes/services.list; original row 888.

**Source-preserving request, proposal, or question:**

> Will need to include `communication` svc as well

**Conditions and limits:**

- The inline path is kubernetes/services.list and the request explicitly adds communication service. It does not specify a new projection version or runtime API change.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:888 · comment 507791507 · PR 9240 · 2024-06-03

Source path: `kubernetes/services.list`

**Evidence:** anon-2.jsonl:888 · comment 507791507 · PR 9240 · 2024-06-03

Source path: `kubernetes/services.list`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0932 — InitiateFeeChargeCmdHandler: Maybe we can rearrange this logic a little

**Source stance:** suggestion

**Context:**

> PR 9546 ([EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/InitiateFeeChargeCmdHandler.scala; original row 932.

**Concern stated in the source:** Maybe we can rearrange this logic a little

```
1. if isFullRedemptionFeeChargeAlreadyRequested block: validate if duplicated full redemption fee charge
2. if noFeeChargeRequired block: always waive
3. pattern match on skip details to generate charge request or skip
```

‌

**Source-preserving request, proposal, or question:**

> Maybe we can rearrange this logic a little
> 
> ```
> 1. if isFullRedemptionFeeChargeAlreadyRequested block: validate if duplicated full redemption fee charge
> 2. if noFeeChargeRequired block: always waive
> 3. pattern match on skip details to generate charge request or skip
> ```
> 
> ‌

**Conditions and limits:**

- Preserve ordering: duplicate full-redemption charge check, noFeeChargeRequired waiver, then skip-details charge-or-skip match.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:932 · comment 520046307 · PR 9546 · 2024-07-11

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/InitiateFeeChargeCmdHandler.scala`

**Evidence:** anon-2.jsonl:932 · comment 520046307 · PR 9546 · 2024-07-11

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/InitiateFeeChargeCmdHandler.scala`

**Explicit source context (pr_title):**

> [EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles

## A2-0933 — Review: We also need to emit kafka msg for skipped fee charge and handle it on redemption svc side to complete the full redemption request

**Source stance:** explanation

**Context:**

> PR 9546 ([EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles), no inline path; original row 933.

**Concern stated in the source:** We also need to emit kafka msg for skipped fee charge and handle it on redemption svc side to complete the full redemption request

**Source-preserving request, proposal, or question:**

> We also need to emit kafka msg for skipped fee charge and handle it on redemption svc side to complete the full redemption request

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:933 · comment 520057404 · PR 9546 · 2024-07-11

**Evidence:** anon-2.jsonl:933 · comment 520057404 · PR 9546 · 2024-07-11

**Explicit source context (pr_title):**

> [EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles

## A2-0944 — FeeChargeRequestJdbcRepository: We also need to handle the skipped event in `FeeChargeRequestJdbcProjectionV6`

**Source stance:** explanation

**Context:**

> PR 9546 ([EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/feeCharge/jdbc/FeeChargeRequestJdbcRepository.scala; original row 944.

**Concern stated in the source:** We also need to handle the skipped event in `FeeChargeRequestJdbcProjectionV6`

**Source-preserving request, proposal, or question:**

> We also need to handle the skipped event in `FeeChargeRequestJdbcProjectionV6`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:944 · comment 520392380 · PR 9546 · 2024-07-12

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/feeCharge/jdbc/FeeChargeRequestJdbcRepository.scala`

**Evidence:** anon-2.jsonl:944 · comment 520392380 · PR 9546 · 2024-07-12

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/feeCharge/jdbc/FeeChargeRequestJdbcRepository.scala`

**Explicit source context (pr_title):**

> [EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles

## A2-0952 — BaseRedemptionCommunicationV2Projection: Can import `TraversableOnceUtils` and use it like this

**Source stance:** suggestion

**Context:**

> PR 9473 (Feat/INV-2450/sg hk retail redemption initiated email v2), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala; original row 952.

**Source-preserving request, proposal, or question:**

> Can import `TraversableOnceUtils` and use it like this
> 
> ```
> instruments
>   .flatMap(_.redemptionDetails.flatMap(_.dealingFrequency))
>   .maxByOption(identity)(DealingFrequencyOrdering)
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:952 · comment 516549655 · PR 9473 · 2024-07-02

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Evidence:** anon-2.jsonl:952 · comment 516549655 · PR 9473 · 2024-07-02

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> Feat/INV-2450/sg hk retail redemption initiated email v2

## A2-0981 — InvestmentTransferCommunicationV2ProjectionSg: Looks like we just need to return a result struct that contains the type of violation, then check if cka violation then send comms...

**Source stance:** suggestion

**Context:**

> PR 9265 (TT-4464 Trading calling checkCustomerTradingRestrictionV3), trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferCommunicationV2ProjectionSg.scala; original row 981.

**Concern stated in the source:** Looks like we just need to return a result struct that contains the type of violation, then check if cka violation then send comms, else we noop \(until product gives more details\)

**Source-preserving request, proposal, or question:**

> Looks like we just need to return a result struct that contains the type of violation, then check if cka violation then send comms, else we noop \(until product gives more details\)

**Conditions and limits:**

- Send communication only for CKA violation; other restriction types are noop until product specifies behavior.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:981 · comment 507983837 · PR 9265 · 2024-06-04

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferCommunicationV2ProjectionSg.scala`

**Evidence:** anon-2.jsonl:981 · comment 507983837 · PR 9265 · 2024-06-04

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferCommunicationV2ProjectionSg.scala`

**Explicit source context (pr_title):**

> TT-4464 Trading calling checkCustomerTradingRestrictionV3

## A2-0996 — package: Rename to `NotifyRebalanceTradeSettlementDetailsAmendedCmd`… do the same for event and kafka msg

**Source stance:** suggestion

**Context:**

> PR 9365 (Feat/INV-3015 rebalance trade settlement amended), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/ces/commands/package.scala; original row 996.

**Source-preserving request, proposal, or question:**

> Rename to `NotifyRebalanceTradeSettlementDetailsAmendedCmd`… do the same for event and kafka msg

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:996 · comment 513297484 · PR 9365 · 2024-06-26

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/ces/commands/package.scala`

**Evidence:** anon-2.jsonl:996 · comment 513297484 · PR 9365 · 2024-06-26

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/ces/commands/package.scala`

**Explicit source context (pr_title):**

> Feat/INV-3015 rebalance trade settlement amended

## A2-0997 — NotifyRebalanceTradeSettlementAmendedCmdHandler: This is very dangerous and potentially lead to wonky data state if not done properly by POps. In fact, if you check the entrypoi...

**Source stance:** suggestion

**Context:**

> PR 9365 (Feat/INV-3015 rebalance trade settlement amended), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala; original row 997.

**Concern stated in the source:** This is very dangerous and potentially lead to wonky data state if not done properly by POps. In fact, if you check the entrypoint for `TradeSettlementDetailsAmendedMsg` from trading svc, it comes from `AmendSettledOrderCmd` / `AmendSettledOrderCmdHandler` which doesn’t really update corresponding cash reservation of the order \(applicable for sell\)… and `handleCashReservationForTradeSettlement` in `PlanTraderProjection` doesn’t handle all cases…

**Source-preserving request, proposal, or question:**

> This is very dangerous and potentially lead to wonky data state if not done properly by POps. In fact, if you check the entrypoint for `TradeSettlementDetailsAmendedMsg` from trading svc, it comes from `AmendSettledOrderCmd` / `AmendSettledOrderCmdHandler` which doesn’t really update corresponding cash reservation of the order \(applicable for sell\)… and `handleCashReservationForTradeSettlement` in `PlanTraderProjection` doesn’t handle all cases…

**Conditions and limits:**

- AmendSettledOrderCmd does not update sell-order cash reservations, and PlanTraderProjection does not handle every cash-reservation amendment case.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:997 · comment 513320777 · PR 9365 · 2024-06-26

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Evidence:** anon-2.jsonl:997 · comment 513320777 · PR 9365 · 2024-06-26

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3015 rebalance trade settlement amended

## A2-0998 — TradeTopicSubscriber: Should we add similar check for settlementConfirmed\* fields, similar to `TradeSettlementConfirmedMsg`?

**Source stance:** open-question

**Context:**

> PR 9365 (Feat/INV-3015 rebalance trade settlement amended), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/TradeTopicSubscriber.scala; original row 998.

**Concern stated in the source:** Should we add similar check for settlementConfirmed\* fields, similar to `TradeSettlementConfirmedMsg`?

But actually it seems trading is reusing this msg to update just the rebalanceRequestId \(nothing to do with settlement details\)

**Source-preserving request, proposal, or question:**

> Should we add similar check for settlementConfirmed\* fields, similar to `TradeSettlementConfirmedMsg`?
> 
> But actually it seems trading is reusing this msg to update just the rebalanceRequestId \(nothing to do with settlement details\)

**Conditions and limits:**

- settlementConfirmed fields are questioned, but the source observes the message may only update rebalanceRequestId.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:998 · comment 513298523 · PR 9365 · 2024-06-26

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/TradeTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:998 · comment 513298523 · PR 9365 · 2024-06-26

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/TradeTopicSubscriber.scala`

**Explicit source context (pr_title):**

> Feat/INV-3015 rebalance trade settlement amended

## A2-1006 — RedemptionRequestTopicSubscriberV3: Not sure if we need all these validation in transaction svc. Maybe just dump directly with status = `SETTLEMENT_CONFIRMED`.

**Source stance:** suggestion

**Context:**

> PR 9388 (Feat/INV-3183 redemption amend settlement), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala; original row 1006.

**Concern stated in the source:** Not sure if we need all these validation in transaction svc. Maybe just dump directly with status = `SETTLEMENT_CONFIRMED`.

State validation should happen upstream, not here I think

**Source-preserving request, proposal, or question:**

> Not sure if we need all these validation in transaction svc. Maybe just dump directly with status = `SETTLEMENT_CONFIRMED`.
> 
> State validation should happen upstream, not here I think

**Conditions and limits:**

- Upstream state validation and direct SETTLEMENT_CONFIRMED transaction update is proposed, not established safe behavior.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1006 · comment 512144974 · PR 9388 · 2024-06-20

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1006 · comment 512144974 · PR 9388 · 2024-06-20

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> Feat/INV-3183 redemption amend settlement

## A2-1007 — package: Maybe following naming pattern of investment svc, e.g. `RedemptionRequestSettlementDetailsAmendedEvt`… update for Kafka msg too

**Source stance:** suggestion

**Context:**

> PR 9388 (Feat/INV-3183 redemption amend settlement), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/ces/events/package.scala; original row 1007.

**Source-preserving request, proposal, or question:**

> Maybe following naming pattern of investment svc, e.g. `RedemptionRequestSettlementDetailsAmendedEvt`… update for Kafka msg too
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1007 · comment 512144498 · PR 9388 · 2024-06-20

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/ces/events/package.scala`

**Evidence:** anon-2.jsonl:1007 · comment 512144498 · PR 9388 · 2024-06-20

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/ces/events/package.scala`

**Explicit source context (pr_title):**

> Feat/INV-3183 redemption amend settlement

## A2-1012 — RedemptionRequestTopicSubscriberV3: Do we need forceUpdate = true since it’s already completed?

**Source stance:** open-question

**Context:**

> PR 9388 (Feat/INV-3183 redemption amend settlement), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala; original row 1012.

**Concern stated in the source:** Do we need forceUpdate = true since it’s already completed?

**Source-preserving request, proposal, or question:**

> Do we need forceUpdate = true since it’s already completed?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1012 · comment 513299696 · PR 9388 · 2024-06-25

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1012 · comment 513299696 · PR 9388 · 2024-06-25

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> Feat/INV-3183 redemption amend settlement

## A2-1073 — PushNotificationProviderData: In theory these should be optional \(otherwise we might break serdes of there are lagged messages in the kafka topic\), but I guess this one is ok ...

**Source stance:** explanation

**Context:**

> PR 9257 (TT-4230 autofund upcoming recur inv comms), communication-api/src/main/scala/com/endowus/silver/communication/api/v2/pushNotitification/PushNotificationProviderData.scala; original row 1073.

**Concern stated in the source:** In theory these should be optional \(otherwise we might break serdes of there are lagged messages in the kafka topic\), but I guess this one is ok cuz we know this type of notification is only triggered in the morning

**Source-preserving request, proposal, or question:**

> In theory these should be optional \(otherwise we might break serdes of there are lagged messages in the kafka topic\), but I guess this one is ok cuz we know this type of notification is only triggered in the morning

**Conditions and limits:**

- Optionality is generally needed for lagged Kafka messages, but this morning-only notification is explicitly accepted as a narrow exception.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1073 · comment 508952279 · PR 9257 · 2024-06-07

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/v2/pushNotitification/PushNotificationProviderData.scala`

**Evidence:** anon-2.jsonl:1073 · comment 508952279 · PR 9257 · 2024-06-07

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/v2/pushNotitification/PushNotificationProviderData.scala`

**Explicit source context (pr_title):**

> TT-4230 autofund upcoming recur inv comms

## A2-1081 — ReportApplication: Just some notes here, yall are right about the trade-offs but manual start is not that bad, depending on use cases.

**Source stance:** suggestion

**Context:**

> PR 9306 (Feat/EN-3405 use tasktopicsubscriber in report for manual start/stop), report-impl/src/main/scala/com/endowus/silver/report/impl/ReportApplication.scala; original row 1081.

**Concern stated in the source:** Just some notes here, yall are right about the trade-offs but manual start is not that bad, depending on use cases.

In case of report, the svc itself is responsible for triggering of the topic producer side. So we can potentially just call start \(via distributed pubsub\) in the same trigger endpoint, i.e. `createMonthlyStatementsV2` first will trigger start, only then produce the message.

* the start is idempotent so if already started, it won’t cause any harm
* the distributed pubsub is at-most once tho, so it could still happen that maybe one of instance does not start… but I suppose this could be checked easily via logs or metrics.

‌

We can also make this pause/resume status persisted, and check upon startup :thumbsup: 

‌

**Source-preserving request, proposal, or question:**

> Just some notes here, yall are right about the trade-offs but manual start is not that bad, depending on use cases.
> 
> In case of report, the svc itself is responsible for triggering of the topic producer side. So we can potentially just call start \(via distributed pubsub\) in the same trigger endpoint, i.e. `createMonthlyStatementsV2` first will trigger start, only then produce the message.
> 
> * the start is idempotent so if already started, it won’t cause any harm
> * the distributed pubsub is at-most once tho, so it could still happen that maybe one of instance does not start… but I suppose this could be checked easily via logs or metrics.
> 
> ‌
> 
> We can also make this pause/resume status persisted, and check upon startup :thumbsup: 
> 
> ‌

**Conditions and limits:**

- Report may start TaskTopicSubscriber idempotently before producing in createMonthlyStatementsV2. Distributed pubsub is at-most-once and may miss an instance; logs/metrics can detect it. Persisted pause/resume is another option.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1081 · comment 508950934 · PR 9306 · 2024-06-07

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/ReportApplication.scala`

**Evidence:** anon-2.jsonl:1081 · comment 508950934 · PR 9306 · 2024-06-07

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/ReportApplication.scala`

**Explicit source context (pr_title):**

> Feat/EN-3405 use tasktopicsubscriber in report for manual start/stop

## A2-1097 — InstrumentJdbcEventProcessor: Let’s use Cassandra projection manager?

**Source stance:** open-question

**Context:**

> PR 9014 (Resolve INV-2980: BE changes needed for admin instrument screens), instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessor.scala; original row 1097.

**Source-preserving request, proposal, or question:**

> Let’s use Cassandra projection manager?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1097 · comment 499485542 · PR 9014 · 2024-05-09

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:1097 · comment 499485542 · PR 9014 · 2024-05-09

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessor.scala`

**Explicit source context (pr_title):**

> Resolve INV-2980: BE changes needed for admin instrument screens

## A2-1104 — ProjectionHelper: This doesn’t look right. We already match in `getIndicativeAmount`, we shouldn’t need to match again

**Source stance:** explanation

**Context:**

> PR 9129 ([EN-3272] Add autofx recurring investment support in advisory), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ProjectionHelper.scala; original row 1104.

**Concern stated in the source:** This doesn’t look right. We already match in `getIndicativeAmount`, we shouldn’t need to match again

**Source-preserving request, proposal, or question:**

> This doesn’t look right. We already match in `getIndicativeAmount`, we shouldn’t need to match again

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1104 · comment 501666990 · PR 9129 · 2024-05-17

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ProjectionHelper.scala`

**Evidence:** anon-2.jsonl:1104 · comment 501666990 · PR 9129 · 2024-05-17

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ProjectionHelper.scala`

**Explicit source context (pr_title):**

> [EN-3272] Add autofx recurring investment support in advisory

## A2-1105 — ProjectionHelper: Use `resolvedRecurringAmountInPlanCcy`?

**Source stance:** open-question

**Context:**

> PR 9129 ([EN-3272] Add autofx recurring investment support in advisory), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ProjectionHelper.scala; original row 1105.

**Source-preserving request, proposal, or question:**

> Use `resolvedRecurringAmountInPlanCcy`?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1105 · comment 505588536 · PR 9129 · 2024-05-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ProjectionHelper.scala`

**Evidence:** anon-2.jsonl:1105 · comment 505588536 · PR 9129 · 2024-05-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ProjectionHelper.scala`

**Explicit source context (hunk):**

> +    recurringInvestmentRequest: RecurringInvestmentRequest
> +  )(implicit executionContext: ExecutionContext): Future[Option[ProjectionRecurringInvestmentRequest]] = {
> +    val recurringAmountInPlanCcy = recurringInvestmentRequest.resolvedRecurringAmountInPlanCcy
> +    Option.whenOptFut(recurringAmountInPlanCcy > 0) {
> +      for {
> +        scheduleInFundingCcy <- getRecurrenceScheduleInFundingCcy(recurringInvestmentRequest)
> +      } yield

**Evidence:** anon-2.jsonl:1105 · comment 505588536 · PR 9129 · 2024-05-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ProjectionHelper.scala`

**Explicit source context (pr_title):**

> [EN-3272] Add autofx recurring investment support in advisory

## A2-1136 — CassandraProjectionManager: Due to this issue, currently all of these spans completes almost instantly \(~0.005s as per current metrics in both prod and staging env\)

**Source stance:** explanation

**Context:**

> PR 9219 ([INV-3090] feat(common): Manually finish the CassandraProjection spans), akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/CassandraProjectionManager.scala; original row 1136.

**Concern stated in the source:** Due to this issue, currently all of these spans completes almost instantly \(~0.005s as per current metrics in both prod and staging env\)

**Source-preserving request, proposal, or question:**

> Due to this issue, currently all of these spans completes almost instantly \(~0.005s as per current metrics in both prod and staging env\)

**Conditions and limits:**

- Observed prematurely completed CassandraProjection spans were about 0.005s in both prod and staging.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1136 · comment 504016232 · PR 9219 · 2024-05-27

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/CassandraProjectionManager.scala`

**Evidence:** anon-2.jsonl:1136 · comment 504016232 · PR 9219 · 2024-05-27

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/CassandraProjectionManager.scala`

**Explicit source context (pr_title):**

> [INV-3090] feat(common): Manually finish the CassandraProjection spans

## A2-1150 — HkRebalancePlanCommunicationV2Projection: Why is it a warn? Just info right? Same for sg

**Source stance:** suggestion

**Context:**

> PR 9202 (Feat/INV-3037 dpc started comms), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/hk/HkRebalancePlanCommunicationV2Projection.scala; original row 1150.

**Source-preserving request, proposal, or question:**

> Why is it a warn? Just info right? Same for sg

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1150 · comment 504022405 · PR 9202 · 2024-05-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/hk/HkRebalancePlanCommunicationV2Projection.scala`

**Evidence:** anon-2.jsonl:1150 · comment 504022405 · PR 9202 · 2024-05-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/hk/HkRebalancePlanCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> Feat/INV-3037 dpc started comms

## A2-1166 — TradingRestrictionLogic: No need to duplicate this whole comment right? Just put both threshold breach \+ portfolio version update into same line?

**Source stance:** suggestion

**Context:**

> PR 9142 (Feat/INV-3035 trading restriction dpc), compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala; original row 1166.

**Source-preserving request, proposal, or question:**

> No need to duplicate this whole comment right? Just put both threshold breach \+ portfolio version update into same line?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1166 · comment 501674283 · PR 9142 · 2024-05-17

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

**Evidence:** anon-2.jsonl:1166 · comment 501674283 · PR 9142 · 2024-05-17

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

**Explicit source context (hunk):**

> -          case _                                                  => false
> +          //For non dpm rebalances we assume customer's plan's cr and cra, pi and complex doesn't change due to rebalances
> +          case _: ThresholdBreachedRebalanceRestrictionRequest |
> +               _: PortfolioVersionUpdateRebalanceRestrictionRequest   => true
> +          case _                                                      => false
>          }
>        }

**Evidence:** anon-2.jsonl:1166 · comment 501674283 · PR 9142 · 2024-05-17

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-3035 trading restriction dpc

## A2-1171 — Review: Tested in SG staging with `charge` svc

**Source stance:** reported-verification

**Context:**

> PR 9178 ([INV-3074] Manual start/stop for TaskTopicSubscriber), no inline path; original row 1171.

**Concern stated in the source:** Tested in SG staging with `charge` svc

* auto init subscription on startup
* auto terminate subscription on shutdown
* NOOP \+ error log only if trigger start/stop with wrong task
* propagate start/stop to all instances of the service if trigger start/stop with correct task
* idempotency: 2nd consecutive start or stop are NOOP with expected logs
* verify kafka subscription correctly pauses in the midst of processing if stopped, and correctly resumes from last committed offset if started again

‌

**Source-preserving request, proposal, or question:**

> Tested in SG staging with `charge` svc
> 
> * auto init subscription on startup
> * auto terminate subscription on shutdown
> * NOOP \+ error log only if trigger start/stop with wrong task
> * propagate start/stop to all instances of the service if trigger start/stop with correct task
> * idempotency: 2nd consecutive start or stop are NOOP with expected logs
> * verify kafka subscription correctly pauses in the midst of processing if stopped, and correctly resumes from last committed offset if started again
> 
> ‌

**Conditions and limits:**

- Reported SG-staging charge test includes auto init/terminate, wrong-task NOOP+error log, all-instance propagation, repeated start/stop idempotency, and stop/resume from last committed Kafka offset.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1171 · comment 502171718 · PR 9178 · 2024-05-20

**Evidence:** anon-2.jsonl:1171 · comment 502171718 · PR 9178 · 2024-05-20

**Explicit source context (pr_title):**

> [INV-3074] Manual start/stop for TaskTopicSubscriber

## A2-1172 — TaskTopicManagementPubSub: This is only published to whoever subscribes to this akka Topic, i.e. the service instances only

**Source stance:** explanation

**Context:**

> PR 9178 ([INV-3074] Manual start/stop for TaskTopicSubscriber), silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TaskTopicManagementPubSub.scala; original row 1172.

**Concern stated in the source:** This is only published to whoever subscribes to this akka Topic, i.e. the service instances only

**Source-preserving request, proposal, or question:**

> This is only published to whoever subscribes to this akka Topic, i.e. the service instances only

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1172 · comment 502172172 · PR 9178 · 2024-05-20

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TaskTopicManagementPubSub.scala`

**Evidence:** anon-2.jsonl:1172 · comment 502172172 · PR 9178 · 2024-05-20

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TaskTopicManagementPubSub.scala`

**Explicit source context (pr_title):**

> [INV-3074] Manual start/stop for TaskTopicSubscriber

## A2-1174 — TaskTopicManagementPubSub: No issue if wrong task. I added error log for this in TaskTopicManager too.

**Source stance:** explanation

**Context:**

> PR 9178 ([INV-3074] Manual start/stop for TaskTopicSubscriber), silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TaskTopicManagementPubSub.scala; original row 1174.

**Concern stated in the source:** No issue if wrong task. I added error log for this in TaskTopicManager too.

**Source-preserving request, proposal, or question:**

> No issue if wrong task. I added error log for this in TaskTopicManager too.

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1174 · comment 502172261 · PR 9178 · 2024-05-20

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TaskTopicManagementPubSub.scala`

**Evidence:** anon-2.jsonl:1174 · comment 502172261 · PR 9178 · 2024-05-20

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TaskTopicManagementPubSub.scala`

**Explicit source context (pr_title):**

> [INV-3074] Manual start/stop for TaskTopicSubscriber

## A2-1176 — Review: That would be next step. Need to check w PM regarding where to store, and the query requirement for it. Likely we just need to stamp in productLineAndIntent… and build h...

**Source stance:** suggestion

**Context:**

> PR 9146 (feat(advisory): terms agreement ack for add goal flagship dpm simulation summary and confirmation endpoints), no inline path; original row 1176.

**Concern stated in the source:** That would be next step. Need to check w PM regarding where to store, and the query requirement for it. Likely we just need to stamp in productLineAndIntent… and build history projection for any historical query.

I have asked [person] to focus on getting the DTO and main logic done first, so that we unblock FE guys. Persistence can be done afterwards in BE only, since it’s not needed in FE to show existing acks

**Source-preserving request, proposal, or question:**

> That would be next step. Need to check w PM regarding where to store, and the query requirement for it. Likely we just need to stamp in productLineAndIntent… and build history projection for any historical query.
> 
> I have asked [person] to focus on getting the DTO and main logic done first, so that we unblock FE guys. Persistence can be done afterwards in BE only, since it’s not needed in FE to show existing acks

**Conditions and limits:**

- Ack persistence/query model is deferred pending PM; likely productLineAndIntent plus history projection. DTO/main flow first unblocks FE, which need not display prior acks.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1176 · comment 500935158 · PR 9146 · 2024-05-15

> That would be next step. Need to check w PM regarding where to store, and the query requirement for it. Likely we just need to stamp in productLineAndIntent… and build history projection for any historical query.
> 
> I have asked

**Evidence:** anon-2.jsonl:1176 · comment 500935158 · PR 9146 · 2024-05-15

> to focus on getting the DTO and main logic done first, so that we unblock FE guys. Persistence can be done afterwards in BE only, since it’s not needed in FE to show existing acks

**Evidence:** anon-2.jsonl:1176 · comment 500935158 · PR 9146 · 2024-05-15

**Explicit source context (pr_title):**

> feat(advisory): terms agreement ack for add goal flagship dpm simulation summary and confirmation endpoints

## A2-1223 — HkRebalancePlanCommunicationV2Projection: Should we change this to use `RebalanceCompletedThresholdBreachCommunicator`?

**Source stance:** open-question

**Context:**

> PR 9120 (Feat/INV-3034 add dpm flag threshold rebalancing comms), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/hk/HkRebalancePlanCommunicationV2Projection.scala; original row 1223.

**Source-preserving request, proposal, or question:**

> Should we change this to use `RebalanceCompletedThresholdBreachCommunicator`?
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1223 · comment 499779563 · PR 9120 · 2024-05-10

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/hk/HkRebalancePlanCommunicationV2Projection.scala`

**Evidence:** anon-2.jsonl:1223 · comment 499779563 · PR 9120 · 2024-05-10

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/hk/HkRebalancePlanCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> Feat/INV-3034 add dpm flag threshold rebalancing comms

## A2-1234 — InvestmentRequestTopicSubscriberV3: Should we also use `UpdateFundingInstructionsCmd` here?

**Source stance:** open-question

**Context:**

> PR 8959 (TT-4222 pass retry date time to investment and transaction svc), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala; original row 1234.

**Source-preserving request, proposal, or question:**

> Should we also use `UpdateFundingInstructionsCmd` here?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1234 · comment 499195387 · PR 8959 · 2024-05-08

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1234 · comment 499195387 · PR 8959 · 2024-05-08

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> TT-4222 pass retry date time to investment and transaction svc

## A2-1235 — InvestmentRequestTopicSubscriberV3: There can be eventual consistency delay here no? So might end up with stale version of transaction in the repository

**Source stance:** open-question

**Context:**

> PR 8923 (TT-4220 pass deposit tx id to investment and transaction), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala; original row 1235.

**Concern stated in the source:** There can be eventual consistency delay here no? So might end up with stale version of transaction in the repository

**Source-preserving request, proposal, or question:**

> There can be eventual consistency delay here no? So might end up with stale version of transaction in the repository

**Conditions and limits:**

- Repository transaction lookup may be stale because of eventual consistency.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1235 · comment 498410518 · PR 8923 · 2024-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1235 · comment 498410518 · PR 8923 · 2024-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> TT-4220 pass deposit tx id to investment and transaction

## A2-1236 — InvestmentRequestTopicSubscriberV3: Looks like we need separate cmd to update fxConversionRequestId / deposit transactionId without changing status?

**Source stance:** open-question

**Context:**

> PR 8923 (TT-4220 pass deposit tx id to investment and transaction), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala; original row 1236.

**Concern stated in the source:** Looks like we need separate cmd to update fxConversionRequestId / deposit transactionId without changing status?

Maybe make it a bit more generic to update `FundingInstructions` instead?

**Source-preserving request, proposal, or question:**

> Looks like we need separate cmd to update fxConversionRequestId / deposit transactionId without changing status?
> 
> Maybe make it a bit more generic to update `FundingInstructions` instead?

**Conditions and limits:**

- Separate funding-instructions update command should change fxConversionRequestId/depositTransactionId without changing status.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1236 · comment 498410939 · PR 8923 · 2024-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1236 · comment 498410939 · PR 8923 · 2024-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> TT-4220 pass deposit tx id to investment and transaction

## A2-1237 — InvestmentRequestTopicSubscriberV3: Are we missing a change for `InvestmentRequestHelper` to top up deposit transaction id?

**Source stance:** open-question

**Context:**

> PR 8923 (TT-4220 pass deposit tx id to investment and transaction), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala; original row 1237.

**Concern stated in the source:** Are we missing a change for `InvestmentRequestHelper` to top up deposit transaction id?

**Source-preserving request, proposal, or question:**

> Are we missing a change for `InvestmentRequestHelper` to top up deposit transaction id?

**Conditions and limits:**

- Missing helper top-up concern is corrected in row 1238 after seeing another PR; treat as historical question.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1237 · comment 498411005 · PR 8923 · 2024-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1237 · comment 498411005 · PR 8923 · 2024-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> TT-4220 pass deposit tx id to investment and transaction

## A2-1244 — BrokerCashTransactionTopicSubscriberV3: What will happen to normal deposit? They will flow straight from broker → transaction, without any records in TradingAccountEntity right?...

**Source stance:** open-question

**Context:**

> PR 8998 (TT-4221 add depositDetails in transaction), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV3.scala; original row 1244.

**Concern stated in the source:** What will happen to normal deposit? They will flow straight from broker → transaction, without any records in TradingAccountEntity right? So this cmd won’t work?

**Source-preserving request, proposal, or question:**

> What will happen to normal deposit? They will flow straight from broker → transaction, without any records in TradingAccountEntity right? So this cmd won’t work?

**Conditions and limits:**

- Normal broker→transaction deposit lacks TradingAccountEntity records, so applicability of the command is unresolved.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1244 · comment 498392655 · PR 8998 · 2024-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1244 · comment 498392655 · PR 8998 · 2024-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> TT-4221 add depositDetails in transaction

## A2-1245 — BrokerCashTransactionTopicSubscriberV3: Do we need handle the same for deleted/rejected? I suppose we don’t want to wipe out TradeDetails even for those statuses?

**Source stance:** open-question

**Context:**

> PR 8998 (TT-4221 add depositDetails in transaction), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV3.scala; original row 1245.

**Concern stated in the source:** Do we need handle the same for deleted/rejected? I suppose we don’t want to wipe out TradeDetails even for those statuses?

**Source-preserving request, proposal, or question:**

> Do we need handle the same for deleted/rejected? I suppose we don’t want to wipe out TradeDetails even for those statuses?

**Conditions and limits:**

- Deleted/rejected updates should not wipe TradeDetails; source asks whether those statuses need equivalent handling.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1245 · comment 498393863 · PR 8998 · 2024-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1245 · comment 498393863 · PR 8998 · 2024-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> TT-4221 add depositDetails in transaction

## A2-1308 — Review: In Invest, for new tables \+ projection, we typically include version in the name of the classes, so that there are clean code changes in the PR: 1st PR to add new versi...

**Source stance:** explanation

**Context:**

> PR 8961 ([EN-3099] feat(goal): Migrate to use new goal tables), no inline path; original row 1308.

**Concern stated in the source:** In Invest, for new tables \+ projection, we typically include version in the name of the classes, so that there are clean code changes in the PR: 1st PR to add new version, and 2nd PR to remove old version \(without touching new ones anymore\)

Goal svc has not been migrated with this yet, hence you don’t see same pattern. But here this PR would be half the size if we just remove the old version

**Source-preserving request, proposal, or question:**

> In Invest, for new tables \+ projection, we typically include version in the name of the classes, so that there are clean code changes in the PR: 1st PR to add new version, and 2nd PR to remove old version \(without touching new ones anymore\)
> 
> Goal svc has not been migrated with this yet, hence you don’t see same pattern. But here this PR would be half the size if we just remove the old version

**Conditions and limits:**

- Historical Invest convention uses explicit versioned table/projection classes: add new in first PR, remove old in second without touching new. This is a migration review convention, not universal naming law.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1308 · comment 494481304 · PR 8961 · 2024-04-22

**Evidence:** anon-2.jsonl:1308 · comment 494481304 · PR 8961 · 2024-04-22

**Explicit source context (pr_title):**

> [EN-3099] feat(goal): Migrate to use new goal tables

## A2-1310 — D56 abort rejected withdrawal dividend: 187.44 switches to cash balance; 12.56 reinvestment remains unchanged

**Source stance:** reported-verification

**Context:**

> PR 9037 ([INV-3016] feat(dividend)(timeseries)(transaction): Support aborting dividend stuck in WithdrawalRequested), no inline path; original row 1310.

**Source-preserving request, proposal, or question:**

> Tested in d56
> 
> ‌
> 
> Setup dividend \+ rejected withdrawal
> 
> * withdrawal with amount 187.44 is rejected
> * dividend has distribution withdrawal pref, amount = 187.44, stuck in Processing
> * another dividend with same distribution has distribution reinvested pref, amount = 12.56, in Processing \(not affected\)
> 
> ![](<url>
> dividend svc logs error as expected when received `WithdrawalRequestRejectedMsg` from trading svc
> 
> ‌
> 
> Trigger abort endpoint
> 
> Results:
> 
> * withdrawal with amount 187.44 is still rejected \(in tact\)
> * previously stuck dividend now has distribution cash balance pref, amount = 187.44, and is completed
> * the other dividend with same distribution is not affected
> 
> ![](<url>
> timeseries svc processes the new event and update distribution pref correctly
> 
> ‌
> 
> Inspection reports DividendWithdrawalRequestAbortedEvt with overridingDistributionPreference=DistributeCashBalance, and final Distributed state.

**Conditions and limits:**

- Reported D56 test affects only 187.44 withdrawal dividend; 12.56 reinvestment dividend in same distribution is a negative/control case. Incidental entity/account identifiers omitted.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> Tested in d56
> 
> ‌
> 
> Setup dividend \+ rejected withdrawal
> 
> * withdrawal with amount 187.44 is rejected
> * dividend has distribution withdrawal pref, amount = 187.44, stuck in Processing
> * another dividend with same distribution has distribution reinvested pref, amount = 12.56, in Processing \(not affected\)
> 
> ![](<url>
> dividend svc logs error as expected when received `WithdrawalRequestRejectedMsg` from trading svc
> 
> ‌
> 
> Trigger abort endpoint

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> Results:
> 
> * withdrawal with amount 187.44 is still rejected \(in tact\)
> * previously stuck dividend now has distribution cash balance pref, amount = 187.44, and is completed
> * the other dividend with same distribution is not affected
> 
> ![](<url>
> timeseries svc processes the new event and update distribution pref correctly
> 
> ‌

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> "eventName": "DividendWithdrawalRequestAbortedEvt"

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> "overridingDistributionPreference": "DistributeCashBalance"

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> "distributionPreference": "DistributeCashBalance"

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> "_type": "com.endowus.silver.dividend.impl.entities.dividend.ces.Distributed"

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

**Explicit source context (pr_title):**

> [INV-3016] feat(dividend)(timeseries)(transaction): Support aborting dividend stuck in WithdrawalRequested

## A2-1311 — DividendTopicSubscriberV3: Added comment for the AbortCmd… from transaction pov, it doesnt need to know about the possible cases of pref here. In future, we might support for ca...

**Source stance:** explanation

**Context:**

> PR 9037 ([INV-3016] feat(dividend)(timeseries)(transaction): Support aborting dividend stuck in WithdrawalRequested), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala; original row 1311.

**Concern stated in the source:** Added comment for the AbortCmd… from transaction pov, it doesnt need to know about the possible cases of pref here. In future, we might support for cases if required

**Source-preserving request, proposal, or question:**

> Added comment for the AbortCmd… from transaction pov, it doesnt need to know about the possible cases of pref here. In future, we might support for cases if required

**Conditions and limits:**

- AbortCmd is outside normal dividend workflow; transaction need not know all possible distribution preferences unless future cases require it.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1311 · comment 497612570 · PR 9037 · 2024-05-02

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1311 · comment 497612570 · PR 9037 · 2024-05-02

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> [INV-3016] feat(dividend)(timeseries)(transaction): Support aborting dividend stuck in WithdrawalRequested

## A2-1352 — RebalancerConfigJdbcProjection: Should we make this column required, and default to event timestamp if missing from evt?

**Source stance:** open-question

**Context:**

> PR 8969 (Resolve INV-2969: Add rebalance config readside.), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalconfig/processors/RebalancerConfigJdbcProjection.scala; original row 1352.

**Source-preserving request, proposal, or question:**

> Should we make this column required, and default to event timestamp if missing from evt?

**Conditions and limits:**

- Required column may fall back to event timestamp, but source phrases it as a proposal.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1352 · comment 494564288 · PR 8969 · 2024-04-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalconfig/processors/RebalancerConfigJdbcProjection.scala`

**Evidence:** anon-2.jsonl:1352 · comment 494564288 · PR 8969 · 2024-04-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalconfig/processors/RebalancerConfigJdbcProjection.scala`

**Explicit source context (pr_title):**

> Resolve INV-2969: Add rebalance config readside.

## A2-1395 — GoalModificationWithPortfolioSimulationRestrictionDpmSpec: Feels like lots of duplicated tests in here, while missing some other cases specific to DPM

**Source stance:** suggestion

**Context:**

> PR 8885 (Feat/INV-2852 goal modify trade restriction), compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalModificationWithPortfolioSimulationRestrictionDpmSpec.scala; original row 1395.

**Concern stated in the source:** Feels like lots of duplicated tests in here, while missing some other cases specific to DPM

Generally I think it’s ok to piggy-pack on the GoalCreate\*Spec for most of the CRA\+CR checks, and GoalModify\*Spec should just focus on the part specific to goal modify, e.g. portfolio lookup.

But if we want to more test cases, then I think for DPM we should cover these:

* Blocked

    * CraCat3
    * CraCat2WithDiscretionaryPortfolio \(no need so many cases like this current file\)
    * IneligibleForDiscretionaryPortfolio \(missing in this test\)
    * CraCat1WithConcentrationRiskBreach
    
* Permitted

    * Retail with PI funds
    * Aggressive complex
    * normal vanilla CraCat1
    

‌

**Source-preserving request, proposal, or question:**

> Feels like lots of duplicated tests in here, while missing some other cases specific to DPM
> 
> Generally I think it’s ok to piggy-pack on the GoalCreate\*Spec for most of the CRA\+CR checks, and GoalModify\*Spec should just focus on the part specific to goal modify, e.g. portfolio lookup.
> 
> But if we want to more test cases, then I think for DPM we should cover these:
> 
> * Blocked
> 
>     * CraCat3
>     * CraCat2WithDiscretionaryPortfolio \(no need so many cases like this current file\)
>     * IneligibleForDiscretionaryPortfolio \(missing in this test\)
>     * CraCat1WithConcentrationRiskBreach
>     
> * Permitted
> 
>     * Retail with PI funds
>     * Aggressive complex
>     * normal vanilla CraCat1
>     
> 
> ‌

**Conditions and limits:**

- Reuse GoalCreate CRA/CR coverage; GoalModify focuses portfolio lookup plus DPM-specific blocked CraCat3/CraCat2WithDiscretionaryPortfolio/IneligibleForDiscretionaryPortfolio/CraCat1WithConcentrationRiskBreach and permitted Retail-with-PI/aggressive-complex/vanilla-CraCat1.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1395 · comment 491268211 · PR 8885 · 2024-04-12

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalModificationWithPortfolioSimulationRestrictionDpmSpec.scala`

**Evidence:** anon-2.jsonl:1395 · comment 491268211 · PR 8885 · 2024-04-12

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalModificationWithPortfolioSimulationRestrictionDpmSpec.scala`

**Explicit source context (pr_title):**

> Feat/INV-2852 goal modify trade restriction

## A2-1408 — AdvisoryApplication: We should be able to move both this and `productPortfolioJdbcRepository` to base `ServiceComponents`. Can use wire instead of new keyword.

**Source stance:** suggestion

**Context:**

> PR 8792 (Feat/INV-2730/flagship dpm offerring min required amts), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala; original row 1408.

**Concern stated in the source:** We should be able to move both this and `productPortfolioJdbcRepository` to base `ServiceComponents`. Can use wire instead of new keyword.

Can we see if we can add `setupBaseSubscribers` for `ModelPortfolioTopicSubscriber` and `PortfolioPerformanceTopicSubscriber` too?

**Source-preserving request, proposal, or question:**

> We should be able to move both this and `productPortfolioJdbcRepository` to base `ServiceComponents`. Can use wire instead of new keyword.
> 
> Can we see if we can add `setupBaseSubscribers` for `ModelPortfolioTopicSubscriber` and `PortfolioPerformanceTopicSubscriber` too?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1408 · comment 488864717 · PR 8792 · 2024-04-04

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

**Evidence:** anon-2.jsonl:1408 · comment 488864717 · PR 8792 · 2024-04-04

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

**Explicit source context (pr_title):**

> Feat/INV-2730/flagship dpm offerring min required amts

## A2-1412 — AdvisoryApplication: I haven’t checked fully, but I think the pattern I’ve seen so far, the kafka subscribers are wired and started last. So we keep `setupBaseSubscribers` as la...

**Source stance:** suggestion

**Context:**

> PR 8792 (Feat/INV-2730/flagship dpm offerring min required amts), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala; original row 1412.

**Concern stated in the source:** I haven’t checked fully, but I think the pattern I’ve seen so far, the kafka subscribers are wired and started last. So we keep `setupBaseSubscribers` as lazy in base, but call them directly in each Hk/Sg\*Application

**Source-preserving request, proposal, or question:**

> I haven’t checked fully, but I think the pattern I’ve seen so far, the kafka subscribers are wired and started last. So we keep `setupBaseSubscribers` as lazy in base, but call them directly in each Hk/Sg\*Application

**Conditions and limits:**

- Subscriber-last startup pattern is observed but explicitly not fully checked; keep lazy base setup and invoke from regional Application.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1412 · comment 490870784 · PR 8792 · 2024-04-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

**Evidence:** anon-2.jsonl:1412 · comment 490870784 · PR 8792 · 2024-04-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

**Explicit source context (pr_title):**

> Feat/INV-2730/flagship dpm offerring min required amts

## A2-1414 — SubscriberHelpers: Avoid Option.get in general. I guess here you can write it as

**Source stance:** suggestion

**Context:**

> PR 8863 (Feat/INV-2784 transaction dpm goal related tagging), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/SubscriberHelpers.scala; original row 1414.

**Concern stated in the source:** Avoid Option.get in general. I guess here you can write it as

```
maybeExistingTransaction
  .map {
    case ...
  }
  .map(Future.successful)
  .getOrElse {
    advisoryClassification match ...
  }
```

‌

**Source-preserving request, proposal, or question:**

> Avoid Option.get in general. I guess here you can write it as
> 
> ```
> maybeExistingTransaction
>   .map {
>     case ...
>   }
>   .map(Future.successful)
>   .getOrElse {
>     advisoryClassification match ...
>   }
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1414 · comment 489255981 · PR 8863 · 2024-04-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/SubscriberHelpers.scala`

**Evidence:** anon-2.jsonl:1414 · comment 489255981 · PR 8863 · 2024-04-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/SubscriberHelpers.scala`

**Explicit source context (pr_title):**

> Feat/INV-2784 transaction dpm goal related tagging

## A2-1415 — SubscriberHelpers: Maybe return None here

**Source stance:** open-question

**Context:**

> PR 8863 (Feat/INV-2784 transaction dpm goal related tagging), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/SubscriberHelpers.scala; original row 1415.

**Source-preserving request, proposal, or question:**

> Maybe return None here

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Question concerns absent DPM flag while deriving transaction classification; hunk shows logging for missing goal.productLineAndIntent flag.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1415 · comment 489256033 · PR 8863 · 2024-04-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/SubscriberHelpers.scala`

**Evidence:** anon-2.jsonl:1415 · comment 489256033 · PR 8863 · 2024-04-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/SubscriberHelpers.scala`

**Explicit source context (hunk):**

> +          advisoryClassification match {
> +            case Some(Advisory) | Some(ExecutionOnly) => Future.successful(Some(false))
> +            case Some(Discretionary) | None => goalService.findGoalById(customerId, goalId, includePlans = false).invoke()
> +              .map(s => s.productLineAndIntent.map(_.isDiscretionaryPortfolio))
> +              .map(maybeGoalIsDpm => {
> +                if (maybeGoalIsDpm.isEmpty)
> +                  logger.error(s"GoalId ${goalId} has no dpm flag, please check goal product line and intent!")

**Evidence:** anon-2.jsonl:1415 · comment 489256033 · PR 8863 · 2024-04-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/SubscriberHelpers.scala`

**Explicit source context (pr_title):**

> Feat/INV-2784 transaction dpm goal related tagging

## A2-1447 — package: goal-api `OneTimeInvestmentRequestV2(fundingInstructions, Option[indicativeAmount])`

**Source stance:** suggestion

**Context:**

> PR 8568 ([EN-3050] Add initial funding instructions to plan models), goal-api/src/main/scala/com/endowus/silver/goal/api/requests/package.scala; original row 1447.

**Concern stated in the source:** goal-api `OneTimeInvestmentRequestV2(fundingInstructions, Option[indicativeAmount])`

V2Request → `OneTimeInvestmentRequestV2(planInstrument, amount)`

logic → both existing amount \+ new optional instruction → PlanDto \(instruction is not optional\) for projection

…

drop domain amount / `OneTimeInvestmentRequestV2` amount

‌

**Source-preserving request, proposal, or question:**

> goal-api `OneTimeInvestmentRequestV2(fundingInstructions, Option[indicativeAmount])`
> 
> V2Request → `OneTimeInvestmentRequestV2(planInstrument, amount)`
> 
> logic → both existing amount \+ new optional instruction → PlanDto \(instruction is not optional\) for projection
> 
> …
> 
> drop domain amount / `OneTimeInvestmentRequestV2` amount
> 
> ‌

**Conditions and limits:**

- Source sketches staged DTO/domain evolution rather than final schema: optional indicative amount then both amount/instructions, DTO required instruction, eventually drop old domain amount.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1447 · comment 483758507 · PR 8568 · 2024-03-21

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/requests/package.scala`

**Evidence:** anon-2.jsonl:1447 · comment 483758507 · PR 8568 · 2024-03-21

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/requests/package.scala`

**Explicit source context (pr_title):**

> [EN-3050] Add initial funding instructions to plan models

## A2-1454 — Review: Can we also delete the cassandra readside \+ projection too :pray:

**Source stance:** suggestion

**Context:**

> PR 8677 ([EN-3097] Remove cassandra readside dependency in goal svc), no inline path; original row 1454.

**Source-preserving request, proposal, or question:**

> Can we also delete the cassandra readside \+ projection too :pray:

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1454 · comment 481432330 · PR 8677 · 2024-03-13

**Evidence:** anon-2.jsonl:1454 · comment 481432330 · PR 8677 · 2024-03-13

**Explicit source context (pr_title):**

> [EN-3097] Remove cassandra readside dependency in goal svc

## A2-1473 — GoalCreationFromPortfolioSimulationRestrictionSpec: I’m thinking this test is quite big. Should we consider split into 2 files?

**Source stance:** suggestion

**Context:**

> PR 8820 (Feat/INV-2779 trading simulation restriction dpm compliance), compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalCreationFromPortfolioSimulationRestrictionSpec.scala; original row 1473.

**Concern stated in the source:** I’m thinking this test is quite big. Should we consider split into 2 files?

* GoalCreationFromPortfolioSimulationRestrictionSpec: just cover basic flow that we lookup TAA from portfolio.. no need to duplicate everything
* GoalCreationFromDpmPortfolioSimulationRestrictionSpec: cover stuff that are specific to DPM… again no need to duplicate everything

‌

**Source-preserving request, proposal, or question:**

> I’m thinking this test is quite big. Should we consider split into 2 files?
> 
> * GoalCreationFromPortfolioSimulationRestrictionSpec: just cover basic flow that we lookup TAA from portfolio.. no need to duplicate everything
> * GoalCreationFromDpmPortfolioSimulationRestrictionSpec: cover stuff that are specific to DPM… again no need to duplicate everything
> 
> ‌

**Conditions and limits:**

- Split common portfolio lookup coverage from DPM-specific restriction tests instead of duplicating everything.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1473 · comment 486032061 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalCreationFromPortfolioSimulationRestrictionSpec.scala`

**Evidence:** anon-2.jsonl:1473 · comment 486032061 · PR 8820 · 2024-03-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/tradingSimulationRestriction/GoalCreationFromPortfolioSimulationRestrictionSpec.scala`

**Explicit source context (pr_title):**

> Feat/INV-2779 trading simulation restriction dpm compliance

## A2-1487 — Review: Existing naming in `transaction` svc is a bit confusing \(introduced by the multiple versions of entity migration\)

**Source stance:** suggestion

**Context:**

> PR 8795 ([PLATFORM-1092] Postgres read side table migration: Stop writing to gcp readside table for transaction), no inline path; original row 1487.

**Concern stated in the source:** Existing naming in `transaction` svc is a bit confusing \(introduced by the multiple versions of entity migration\)

* I believe the `V3` in existing `TransactionJdbcRepositoryV3` / `TransactionJdbcEventProcessorV3` / `TransactionJdbcProjectionV3` refers to the entity V3, not the version of table or projection. I suppose we should have named them `TransactionV3XXX` instead of `TransactionXXXV3`
* Now that the entity migration has completed successfully, I think we can switch the naming as follow:

    * `TransactionV3JdbcRepositoryV4`: ideally we should split this into single repository and versioned dbHandler \(similar to other services\), but we will clean this next time
    * `TransactionV3JdbcProjectionV2`
    

‌

**Source-preserving request, proposal, or question:**

> Existing naming in `transaction` svc is a bit confusing \(introduced by the multiple versions of entity migration\)
> 
> * I believe the `V3` in existing `TransactionJdbcRepositoryV3` / `TransactionJdbcEventProcessorV3` / `TransactionJdbcProjectionV3` refers to the entity V3, not the version of table or projection. I suppose we should have named them `TransactionV3XXX` instead of `TransactionXXXV3`
> * Now that the entity migration has completed successfully, I think we can switch the naming as follow:
> 
>     * `TransactionV3JdbcRepositoryV4`: ideally we should split this into single repository and versioned dbHandler \(similar to other services\), but we will clean this next time
>     * `TransactionV3JdbcProjectionV2`
>     
> 
> ‌

**Conditions and limits:**

- Entity V3 and table/projection version numbers are independent. Proposed naming: TransactionV3JdbcRepositoryV4, TransactionV3JdbcProjectionV2; handler/repository split deferred.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1487 · comment 484744191 · PR 8795 · 2024-03-25

**Evidence:** anon-2.jsonl:1487 · comment 484744191 · PR 8795 · 2024-03-25

**Explicit source context (pr_title):**

> [PLATFORM-1092] Postgres read side table migration: Stop writing to gcp readside table for transaction

## A2-1488 — TransactionV3JdbcProjectionV2: It’s version numbers for 2 different things. Can let them be independent

**Source stance:** explanation

**Context:**

> PR 8795 ([PLATFORM-1092] Postgres read side table migration: Stop writing to gcp readside table for transaction), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionV3JdbcProjectionV2.scala; original row 1488.

**Source-preserving request, proposal, or question:**

> It’s version numbers for 2 different things. Can let them be independent

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1488 · comment 485150850 · PR 8795 · 2024-03-26

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionV3JdbcProjectionV2.scala`

**Evidence:** anon-2.jsonl:1488 · comment 485150850 · PR 8795 · 2024-03-26

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionV3JdbcProjectionV2.scala`

**Explicit source context (pr_title):**

> [PLATFORM-1092] Postgres read side table migration: Stop writing to gcp readside table for transaction

## A2-1489 — PlanTopicSubscriber: Rare but let’s change this to 1

**Source stance:** suggestion

**Context:**

> PR 8764 (Feat/INV-2777 invest systems subscriber tracing), investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/PlanTopicSubscriber.scala; original row 1489.

**Source-preserving request, proposal, or question:**

> Rare but let’s change this to 1

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Source requests parallelism 1 in PlanTopicSubscriber; keep separate from task/per-goal parallelism requests elsewhere.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1489 · comment 484186553 · PR 8764 · 2024-03-22

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/PlanTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:1489 · comment 484186553 · PR 8764 · 2024-03-22

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/PlanTopicSubscriber.scala`

**Explicit source context (hunk):**

> -      if (BigDecimalUtils.hasTooManyDigits(msg.plan.initialInvestmentAmount)) {
> -        logger.error(
> -          s"Initial investment amount [${msg.plan.initialInvestmentAmount}] for plan [${msg.plan.planId}] has too many digits for PlanCreatedMsg($msg)."
> -        )
> -        Future.successful(Done)
> -      } else if (msg.plan.recurringInvestmentSchedule.exists(schedule => BigDecimalUtils.hasTooManyDigits(schedule.amount))) {
> -        logger.error(

**Evidence:** anon-2.jsonl:1489 · comment 484186553 · PR 8764 · 2024-03-22

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/PlanTopicSubscriber.scala`

**Explicit source context (pr_title):**

> Feat/INV-2777 invest systems subscriber tracing

## A2-1490 — RedemptionRequestTopicSubscriber: Same here

**Source stance:** suggestion

**Context:**

> PR 8764 (Feat/INV-2777 invest systems subscriber tracing), investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/RedemptionRequestTopicSubscriber.scala; original row 1490.

**Source-preserving request, proposal, or question:**

> Same here

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- RedemptionRequestTopicSubscriber hunk explicitly has mapAsync(parallelism=1).
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1490 · comment 484186635 · PR 8764 · 2024-03-22

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/RedemptionRequestTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:1490 · comment 484186635 · PR 8764 · 2024-03-22

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/RedemptionRequestTopicSubscriber.scala`

**Explicit source context (hunk):**

> -
> -      case msg: RedemptionRequestCreatedMsg
> +    .withMetadata
> +    .atLeastOnce(Flow[Message[RedemptionRequestMsg]].mapAsync(parallelism = 1) {
> +      runWithKamonContext {
> +        case msg: RedemptionRequestCreatedMsg
>            if msg.request.isFullRedemption &&

**Evidence:** anon-2.jsonl:1490 · comment 484186635 · PR 8764 · 2024-03-22

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/RedemptionRequestTopicSubscriber.scala`

**Explicit source context (pr_title):**

> Feat/INV-2777 invest systems subscriber tracing

## A2-1491 — TradeTopicSubscriber: Hmm I’m surprised we have so many `parallelism` = 2 in investment svc without the safeMapAsync… [person] speed should be fine here, we should just change t...

**Source stance:** suggestion

**Context:**

> PR 8764 (Feat/INV-2777 invest systems subscriber tracing), investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/TradeTopicSubscriber.scala; original row 1491.

**Concern stated in the source:** Hmm I’m surprised we have so many `parallelism` = 2 in investment svc without the safeMapAsync… [person] speed should be fine here, we should just change to 1 for safety yeah?

**Source-preserving request, proposal, or question:**

> Hmm I’m surprised we have so many `parallelism` = 2 in investment svc without the safeMapAsync… [person] speed should be fine here, we should just change to 1 for safety yeah?

**Conditions and limits:**

- Investment subscribers with parallelism=2 lack safeMapAsync; source proposes parallelism=1 for safety.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1491 · comment 484186784 · PR 8764 · 2024-03-22

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/TradeTopicSubscriber.scala`

> Hmm I’m surprised we have so many `parallelism` = 2 in investment svc without the safeMapAsync…

**Evidence:** anon-2.jsonl:1491 · comment 484186784 · PR 8764 · 2024-03-22

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/TradeTopicSubscriber.scala`

> speed should be fine here, we should just change to 1 for safety yeah?

**Evidence:** anon-2.jsonl:1491 · comment 484186784 · PR 8764 · 2024-03-22

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/TradeTopicSubscriber.scala`

**Explicit source context (pr_title):**

> Feat/INV-2777 invest systems subscriber tracing

## A2-1493 — FlowUtils: ```

**Source stance:** suggestion

**Context:**

> PR 8764 (Feat/INV-2777 invest systems subscriber tracing), silver-commons/src/main/scala/com/endowus/silver/commons/utils/FlowUtils.scala; original row 1493.

**Concern stated in the source:** ```
.map(message => {
  val incomingContext = message
    .get(KafkaMetadataKeys.Headers)
    .flatMap(s =>
      Try(KafkaInstrumentation.settings.propagator.read(s, Context.Empty)).toOption
    )
    .getOrElse(Context.Empty)
  (incomingContext, message.payload)
})
```

this block is per msg, and it’s identical in all 3 methods… just extract a common method… no need voodoo

**Source-preserving request, proposal, or question:**

> ```
> .map(message => {
>   val incomingContext = message
>     .get(KafkaMetadataKeys.Headers)
>     .flatMap(s =>
>       Try(KafkaInstrumentation.settings.propagator.read(s, Context.Empty)).toOption
>     )
>     .getOrElse(Context.Empty)
>   (incomingContext, message.payload)
> })
> ```
> 
> this block is per msg, and it’s identical in all 3 methods… just extract a common method… no need voodoo

**Conditions and limits:**

- Extract identical per-message KafkaMetadataKeys.Headers/KafkaInstrumentation.propagator.read(...,Context.Empty) mapping, retaining Try-toOption fallback to Context.Empty.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1493 · comment 484249261 · PR 8764 · 2024-03-22

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/FlowUtils.scala`

**Evidence:** anon-2.jsonl:1493 · comment 484249261 · PR 8764 · 2024-03-22

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/utils/FlowUtils.scala`

**Explicit source context (pr_title):**

> Feat/INV-2777 invest systems subscriber tracing

## A2-1494 — PlanTimeSeriesTopicSubscriber: Do we really need the context for the payload \+ identifier mapping?

**Source stance:** open-question

**Context:**

> PR 8764 (Feat/INV-2777 invest systems subscriber tracing), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala; original row 1494.

**Source-preserving request, proposal, or question:**

> Do we really need the context for the payload \+ identifier mapping?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1494 · comment 485150070 · PR 8764 · 2024-03-26

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:1494 · comment 485150070 · PR 8764 · 2024-03-26

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala`

**Explicit source context (pr_title):**

> Feat/INV-2777 invest systems subscriber tracing

## A2-1565 — RebalanceTopicSubscriberV3: Why name this as `isForceDeleted` while its logic is just `isDeleted`?

**Source stance:** open-question

**Context:**

> PR 8122 (Feat/INV-2203 clean up transaction old entities), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebalanceTopicSubscriberV3.scala; original row 1565.

**Source-preserving request, proposal, or question:**

> Why name this as `isForceDeleted` while its logic is just `isDeleted`?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1565 · comment 478984416 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebalanceTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1565 · comment 478984416 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebalanceTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> Feat/INV-2203 clean up transaction old entities

## A2-1566 — TransactionJdbcProjectionV2: Let’s not mix the naming, it can be confusing for future readers:

**Source stance:** suggestion

**Context:**

> PR 8122 (Feat/INV-2203 clean up transaction old entities), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV2.scala; original row 1566.

**Concern stated in the source:** Let’s not mix the naming, it can be confusing for future readers:

* `transaction-jdbc-handler-v1` is projection on V2 entity
* `transaction-jdbc-handler-v2` is projection on V3 entity to pipe data to V2

‌

I think let’s just use a bit more descriptive name to indicate that it’s projection from v3 entity to v2 repo. Maybe `transaction-v3-projection-to-v2-repo-v1`… last v1 is the version of the projection

Do same for the v1\_3 projection.

**Source-preserving request, proposal, or question:**

> Let’s not mix the naming, it can be confusing for future readers:
> 
> * `transaction-jdbc-handler-v1` is projection on V2 entity
> * `transaction-jdbc-handler-v2` is projection on V3 entity to pipe data to V2
> 
> ‌
> 
> I think let’s just use a bit more descriptive name to indicate that it’s projection from v3 entity to v2 repo. Maybe `transaction-v3-projection-to-v2-repo-v1`… last v1 is the version of the projection
> 
> Do same for the v1\_3 projection.

**Conditions and limits:**

- Projection source entity version and target repository version must be explicit; example transaction-v3-projection-to-v2-repo-v1 keeps last v1 as projection version.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1566 · comment 479020069 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV2.scala`

**Evidence:** anon-2.jsonl:1566 · comment 479020069 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV2.scala`

**Explicit source context (pr_title):**

> Feat/INV-2203 clean up transaction old entities

## A2-1568 — TransactionJdbcProjectionV1_3: Do we want similar cutOff for the V2 projection? Or it’s ok cuz there’s not much data in HK?

**Source stance:** open-question

**Context:**

> PR 8122 (Feat/INV-2203 clean up transaction old entities), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV1_3.scala; original row 1568.

**Concern stated in the source:** Do we want similar cutOff for the V2 projection? Or it’s ok cuz there’s not much data in HK?

**Source-preserving request, proposal, or question:**

> Do we want similar cutOff for the V2 projection? Or it’s ok cuz there’s not much data in HK?

**Conditions and limits:**

- Whether V2 needs a cutoff or is acceptable for low HK volume remains a question.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1568 · comment 479055129 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV1_3.scala`

**Evidence:** anon-2.jsonl:1568 · comment 479055129 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV1_3.scala`

**Explicit source context (pr_title):**

> Feat/INV-2203 clean up transaction old entities

## A2-1569 — JdbcSchema: You still need to create V2 and V1\_3 until we completely remove the 2 projections right? Otherwise this will scream if we deploy to new dynamic env \(or if it’s res...

**Source stance:** suggestion

**Context:**

> PR 8122 (Feat/INV-2203 clean up transaction old entities), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/JdbcSchema.scala; original row 1569.

**Concern stated in the source:** You still need to create V2 and V1\_3 until we completely remove the 2 projections right? Otherwise this will scream if we deploy to new dynamic env \(or if it’s reset\)

**Source-preserving request, proposal, or question:**

> You still need to create V2 and V1\_3 until we completely remove the 2 projections right? Otherwise this will scream if we deploy to new dynamic env \(or if it’s reset\)

**Conditions and limits:**

- V2/V1_3 schemas must still be created while their projections exist, including fresh/reset dynamic environments.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1569 · comment 479078276 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/JdbcSchema.scala`

**Evidence:** anon-2.jsonl:1569 · comment 479078276 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/JdbcSchema.scala`

**Explicit source context (pr_title):**

> Feat/INV-2203 clean up transaction old entities

## A2-1572 — RebalanceTopicSubscriberV3: I mean this method derive the deleted status \(or not\) from txn data, nothing about force or not.

**Source stance:** suggestion

**Context:**

> PR 8122 (Feat/INV-2203 clean up transaction old entities), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebalanceTopicSubscriberV3.scala; original row 1572.

**Concern stated in the source:** I mean this method derive the deleted status \(or not\) from txn data, nothing about force or not.

The force is decided outside

```
forceUpdate = isDeleted && msg.forceDelete.getOrElse(false)
```

‌

**Source-preserving request, proposal, or question:**

> I mean this method derive the deleted status \(or not\) from txn data, nothing about force or not.
> 
> The force is decided outside
> 
> ```
> forceUpdate = isDeleted && msg.forceDelete.getOrElse(false)
> ```
> 
> ‌

**Conditions and limits:**

- Deleted status derives from transaction data; forceUpdate is decided separately as isDeleted && msg.forceDelete.getOrElse(false).
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1572 · comment 479096472 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebalanceTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1572 · comment 479096472 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebalanceTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> Feat/INV-2203 clean up transaction old entities

## A2-1580 — RebateDistributionRequestJdbcRepositoryTest: Is it duplicate test? It’s not mockDb btw, it’s real embedded pg

**Source stance:** open-question

**Context:**

> PR 8587 ([INV-1996] feat(rebate): dry run fixes), rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepositoryTest.scala; original row 1580.

**Source-preserving request, proposal, or question:**

> Is it duplicate test? It’s not mockDb btw, it’s real embedded pg

**Conditions and limits:**

- Test uses actual embedded Postgres, not mockDb; duplication is a question.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1580 · comment 479855723 · PR 8587 · 2024-03-08

Source path: `rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepositoryTest.scala`

**Evidence:** anon-2.jsonl:1580 · comment 479855723 · PR 8587 · 2024-03-08

Source path: `rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepositoryTest.scala`

**Explicit source context (pr_title):**

> [INV-1996] feat(rebate): dry run fixes

## A2-1585 — TransactionTypes: We can let the old `FxConversionDetails` having optional accounts, as we are migrating away from this v1 model.

**Source stance:** suggestion

**Context:**

> PR 8011 (TT-3566 Make broker account optional for FX transactions), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala; original row 1585.

**Concern stated in the source:** We can let the old `FxConversionDetails` having optional accounts, as we are migrating away from this v1 model.

For new `FxTransaction` model:

* Changing `debitBrokerAccount` and `creditBrokerAccount` to optional here makes sense. All existing fx conversion txn would have them populated, and hence still compatible with old FE.
* But I think it’s also good to capture the fact that broker accounts will be available when the txn is settled. Maybe we can consider the following:

    * Add new `SettledFxStatusDetailsV2` that is identical with `SettledFxStatusDetails` with additionally the 2 required broker account fields
    * Change kafka subscriber to populate transaction using V2 instead of V1
    * Add 2 required broker account fields into `SettledFxStatusDetailsDto`
    
        * If entity has V2, map as is
        * If entity has V1, require the outer optional broker account fields in `FxTransaction` to be defined
        
    

‌

**Source-preserving request, proposal, or question:**

> We can let the old `FxConversionDetails` having optional accounts, as we are migrating away from this v1 model.
> 
> For new `FxTransaction` model:
> 
> * Changing `debitBrokerAccount` and `creditBrokerAccount` to optional here makes sense. All existing fx conversion txn would have them populated, and hence still compatible with old FE.
> * But I think it’s also good to capture the fact that broker accounts will be available when the txn is settled. Maybe we can consider the following:
> 
>     * Add new `SettledFxStatusDetailsV2` that is identical with `SettledFxStatusDetails` with additionally the 2 required broker account fields
>     * Change kafka subscriber to populate transaction using V2 instead of V1
>     * Add 2 required broker account fields into `SettledFxStatusDetailsDto`
>     
>         * If entity has V2, map as is
>         * If entity has V1, require the outer optional broker account fields in `FxTransaction` to be defined
>         
>     
> 
> ‌

**Conditions and limits:**

- Old FxConversionDetails can retain optional accounts while new settled FX V2 status requires accounts; V1 DTO conversion must require populated outer accounts.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1585 · comment 475752183 · PR 8011 · 2024-02-26

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala`

**Evidence:** anon-2.jsonl:1585 · comment 475752183 · PR 8011 · 2024-02-26

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala`

**Explicit source context (pr_title):**

> TT-3566 Make broker account optional for FX transactions

## A2-1587 — FxConversionRequestTopicSubscriberV2: Let’s use `BrokerAccountId.fromFxWalletBrokerAccountDto`

**Source stance:** suggestion

**Context:**

> PR 8011 (TT-3566 Make broker account optional for FX transactions), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxConversionRequestTopicSubscriberV2.scala; original row 1587.

**Source-preserving request, proposal, or question:**

> Let’s use `BrokerAccountId.fromFxWalletBrokerAccountDto`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1587 · comment 476497109 · PR 8011 · 2024-02-28

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxConversionRequestTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:1587 · comment 476497109 · PR 8011 · 2024-02-28

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxConversionRequestTopicSubscriberV2.scala`

**Explicit source context (pr_title):**

> TT-3566 Make broker account optional for FX transactions

## A2-1601 — RebateDistributionJdbcEventProcessor: Should we use timestamp from the evt, and if not available use evt timestamp offset instead?

**Source stance:** open-question

**Context:**

> PR 8353 (Feat/INV-1996/automate trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/processors/RebateDistributionJdbcEventProcessor.scala; original row 1601.

**Source-preserving request, proposal, or question:**

> Should we use timestamp from the evt, and if not available use evt timestamp offset instead?

**Conditions and limits:**

- Use event-carried timestamp first, with envelope timestamp-offset fallback if absent; phrased as a question.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1601 · comment 476105822 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/processors/RebateDistributionJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:1601 · comment 476105822 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/processors/RebateDistributionJdbcEventProcessor.scala`

**Explicit source context (pr_title):**

> Feat/INV-1996/automate trailer rebate

## A2-1602 — RebateDistributionJdbcEventProcessor: Consider log full event and its offset maybe. That will help us identifying problematic event faster when this error happens.

**Source stance:** suggestion

**Context:**

> PR 8353 (Feat/INV-1996/automate trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/processors/RebateDistributionJdbcEventProcessor.scala; original row 1602.

**Concern stated in the source:** Consider log full event and its offset maybe. That will help us identifying problematic event faster when this error happens.

Similar for the below info log as well. Currently it tells very little info, as good as no logging…

**Source-preserving request, proposal, or question:**

> Consider log full event and its offset maybe. That will help us identifying problematic event faster when this error happens.
> 
> Similar for the below info log as well. Currently it tells very little info, as good as no logging…

**Conditions and limits:**

- Full event and offset improve locating problematic event; current messages lack context.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1602 · comment 476106177 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/processors/RebateDistributionJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:1602 · comment 476106177 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/processors/RebateDistributionJdbcEventProcessor.scala`

**Explicit source context (pr_title):**

> Feat/INV-1996/automate trailer rebate

## A2-1630 — Review: * advisory.corporate\_customer\_v2

**Source stance:** explanation

**Context:**

> PR 8480 ([INV-2529] feat(advisory)(marketdata)(rebalance)(transaction): Dual write for non-readside tables to both GCP and AWS), no inline path; original row 1630.

**Concern stated in the source:** * advisory.corporate\_customer\_v2

    * Dual write
    * Will add pg migration job to copy existing data
    * Will raise another PR to switch repository to aurora after migration job. Keep dual write until data team has migrate
    
* marketdata.instrument\_mstar\_data\_v1

    * Dual write
    * Will trigger endpoint to sync for all instruments
    * Will raise another PR to switch repository to aurora after sync, and also stop writing to GCP
    
* rebalance.rpc\_communication\_details\_table\_v1

    * Dual write
    * Will add pg migration job to copy existing data
    * Will raise another PR to switch repository to aurora after sync, and also stop writing to GCP
    
* rebalance.plan\_market\_value\_projection\_v1

    * Dual write
    * ~~Wait one day for timeseries to publish latest MV for all plans~~ Will add pg migration job to copy existing data, cuz the subscriber has filtering logic, so it would take longer than 1d to fully sync naturally
    * Will raise another PR to switch repository to aurora after sync, and also stop writing to GCP
    
* transaction.fx\_rates\_v1

    * Dual write
    * Will add pg migration job to copy existing data
    * Will raise another PR to switch repository to aurora after sync, and also stop writing to GCP
    

‌

**Source-preserving request, proposal, or question:**

> * advisory.corporate\_customer\_v2
> 
>     * Dual write
>     * Will add pg migration job to copy existing data
>     * Will raise another PR to switch repository to aurora after migration job. Keep dual write until data team has migrate
>     
> * marketdata.instrument\_mstar\_data\_v1
> 
>     * Dual write
>     * Will trigger endpoint to sync for all instruments
>     * Will raise another PR to switch repository to aurora after sync, and also stop writing to GCP
>     
> * rebalance.rpc\_communication\_details\_table\_v1
> 
>     * Dual write
>     * Will add pg migration job to copy existing data
>     * Will raise another PR to switch repository to aurora after sync, and also stop writing to GCP
>     
> * rebalance.plan\_market\_value\_projection\_v1
> 
>     * Dual write
>     * ~~Wait one day for timeseries to publish latest MV for all plans~~ Will add pg migration job to copy existing data, cuz the subscriber has filtering logic, so it would take longer than 1d to fully sync naturally
>     * Will raise another PR to switch repository to aurora after sync, and also stop writing to GCP
>     
> * transaction.fx\_rates\_v1
> 
>     * Dual write
>     * Will add pg migration job to copy existing data
>     * Will raise another PR to switch repository to aurora after sync, and also stop writing to GCP
>     
> 
> ‌

**Conditions and limits:**

- Five distinct migrations are preserved verbatim. corporate_customer_v2 keeps dual-write until data team migration; instrument_mstar_data_v1 syncs all instruments; other tables use jobs. plan_market_value_projection_v1 explicitly replaces the struck-through one-day natural-sync plan because subscriber filtering delays full sync.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1630 · comment 476601635 · PR 8480 · 2024-02-28

**Evidence:** anon-2.jsonl:1630 · comment 476601635 · PR 8480 · 2024-02-28

**Explicit source context (pr_title):**

> [INV-2529] feat(advisory)(marketdata)(rebalance)(transaction): Dual write for non-readside tables to both GCP and AWS

## A2-1631 — PlanTimeSeriesTopicSubscriber: Maybe 4 as well?

**Source stance:** suggestion

**Context:**

> PR 8468 (adds parallelism to timeseries subscribers), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala; original row 1631.

**Source-preserving request, proposal, or question:**

> Maybe 4 as well?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Parallelism=4 is suggested in timeseries plan-MV subscriber; the hunk excerpt does not establish partition-safety analysis.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1631 · comment 476502874 · PR 8468 · 2024-02-28

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:1631 · comment 476502874 · PR 8468 · 2024-02-28

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala`

**Explicit source context (hunk):**

> -              "Updating latest market value for plan. " +
> -                s"Plan: $planId, Ccy: $planCcy, Business date: ${marketValue.businessDate}, Instruments: ${getInstrumentIds(marketValue).distinct}"
> -            )
> -
> -            instrumentHoldingDao
> -              .batchUpsert(getHoldings(marketValue))
> -              .map(_ => Done)

**Evidence:** anon-2.jsonl:1631 · comment 476502874 · PR 8468 · 2024-02-28

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala`

**Explicit source context (pr_title):**

> adds parallelism to timeseries subscribers

## A2-1632 — PlanTimeSeriesTopicSubscriber: I think planId is available in trait `PlanMarketValueMsg`

**Source stance:** explanation

**Context:**

> PR 8468 (adds parallelism to timeseries subscribers), charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala; original row 1632.

**Source-preserving request, proposal, or question:**

> I think planId is available in trait `PlanMarketValueMsg`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1632 · comment 476502960 · PR 8468 · 2024-02-28

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:1632 · comment 476502960 · PR 8468 · 2024-02-28

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala`

**Explicit source context (pr_title):**

> adds parallelism to timeseries subscribers

## A2-1635 — RegionalCustomerTopicCustomer: Not sure if we should check holdings or ongoing transactions…. I think it’s manual check today by POps, but if they somehow miss it, it would be p...

**Source stance:** open-question

**Context:**

> PR 8215 ([INV-1959] feat(goal): Listen to customer deactivated msg), goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala; original row 1635.

**Concern stated in the source:** Not sure if we should check holdings or ongoing transactions…. I think it’s manual check today by POps, but if they somehow miss it, it would be problematic to unwind this? I don’t think we even support re-activate goals. Maybe we just stop the schedule for all plans, if any, but leave the goals intact?

Also can we make sure the goal deactivation will remove the recurring goal transfer too? I think full redemption remove both, but goal deactivation only remove recurring investment.

‌

**Source-preserving request, proposal, or question:**

> Not sure if we should check holdings or ongoing transactions…. I think it’s manual check today by POps, but if they somehow miss it, it would be problematic to unwind this? I don’t think we even support re-activate goals. Maybe we just stop the schedule for all plans, if any, but leave the goals intact?
> 
> Also can we make sure the goal deactivation will remove the recurring goal transfer too? I think full redemption remove both, but goal deactivation only remove recurring investment.
> 
> ‌

**Conditions and limits:**

- POps may miss holdings/ongoing transactions, and goals cannot easily reactivate. Proposed safer deactivation reaction is stop both investment and goal-transfer schedules, leave goals intact.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1635 · comment 467332191 · PR 8215 · 2024-02-01

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Evidence:** anon-2.jsonl:1635 · comment 467332191 · PR 8215 · 2024-02-01

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Explicit source context (pr_title):**

> [INV-1959] feat(goal): Listen to customer deactivated msg

## A2-1636 — RegionalCustomerTopicCustomer: Not possible as of now I think. I mean if any chance of mistake, at least on our side, we only touch the schedules, which are easy to reinstate. A...

**Source stance:** suggestion

**Context:**

> PR 8215 ([INV-1959] feat(goal): Listen to customer deactivated msg), goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala; original row 1636.

**Concern stated in the source:** Not possible as of now I think. I mean if any chance of mistake, at least on our side, we only touch the schedules, which are easy to reinstate. Active goals if any, just let them be, no harm for us.

**Source-preserving request, proposal, or question:**

> Not possible as of now I think. I mean if any chance of mistake, at least on our side, we only touch the schedules, which are easy to reinstate. Active goals if any, just let them be, no harm for us.

**Conditions and limits:**

- Schedules are easy to reinstate; touching active goals is avoided under uncertain manual checks.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1636 · comment 467661196 · PR 8215 · 2024-02-02

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Evidence:** anon-2.jsonl:1636 · comment 467661196 · PR 8215 · 2024-02-02

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Explicit source context (pr_title):**

> [INV-1959] feat(goal): Listen to customer deactivated msg

## A2-1637 — RegionalCustomerTopicCustomer: Update logging msg

**Source stance:** explanation

**Context:**

> PR 8215 ([INV-1959] feat(goal): Listen to customer deactivated msg), goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala; original row 1637.

**Source-preserving request, proposal, or question:**

> Update logging msg

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1637 · comment 473482270 · PR 8215 · 2024-02-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Evidence:** anon-2.jsonl:1637 · comment 473482270 · PR 8215 · 2024-02-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Explicit source context (hunk):**

> +                  } yield plan
> +                }
> +                .runWith(Sink.ignore)
> +                .map(_ => goalDto)
> +            } yield res
> +          }}
> +            .wireTap(v => logger.info(s"Goal ID [${v.goalId}] plans recurring schedules have been removed"))

**Evidence:** anon-2.jsonl:1637 · comment 473482270 · PR 8215 · 2024-02-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Explicit source context (pr_title):**

> [INV-1959] feat(goal): Listen to customer deactivated msg

## A2-1638 — RegionalCustomerTopicCustomer: Entity is keyed by goalId so would it be better to increase parallelism for goals to 4, keeping parallelism for plans at 1?

**Source stance:** open-question

**Context:**

> PR 8215 ([INV-1959] feat(goal): Listen to customer deactivated msg), goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala; original row 1638.

**Concern stated in the source:** Entity is keyed by goalId so would it be better to increase parallelism for goals to 4, keeping parallelism for plans at 1?

**Source-preserving request, proposal, or question:**

> Entity is keyed by goalId so would it be better to increase parallelism for goals to 4, keeping parallelism for plans at 1?

**Conditions and limits:**

- Goal entity is keyed goalId; proposed goals parallelism=4 but plans within each goal=1.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1638 · comment 473482567 · PR 8215 · 2024-02-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Evidence:** anon-2.jsonl:1638 · comment 473482567 · PR 8215 · 2024-02-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Explicit source context (pr_title):**

> [INV-1959] feat(goal): Listen to customer deactivated msg

## A2-1639 — RegionalCustomerTopicCustomer: Btw should we use jdbc readside instead? Eventually we want to get rid of these cassandra readside for general query needs

**Source stance:** open-question

**Context:**

> PR 8215 ([INV-1959] feat(goal): Listen to customer deactivated msg), goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala; original row 1639.

**Concern stated in the source:** Btw should we use jdbc readside instead? Eventually we want to get rid of these cassandra readside for general query needs

**Source-preserving request, proposal, or question:**

> Btw should we use jdbc readside instead? Eventually we want to get rid of these cassandra readside for general query needs

**Conditions and limits:**

- JDBC readside is preferred for general queries as Cassandra readside removal target.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1639 · comment 473484402 · PR 8215 · 2024-02-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Evidence:** anon-2.jsonl:1639 · comment 473484402 · PR 8215 · 2024-02-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Explicit source context (pr_title):**

> [INV-1959] feat(goal): Listen to customer deactivated msg

## A2-1649 — PreferredLocalLookupHelper: Can we add a base trait `PreferredLocalLookupHelper` too?

**Source stance:** suggestion

**Context:**

> PR 8242 ([EN-2895] feat(customer): PreferredLocalLookupHelper), customer-api/src/main/scala/com/endowus/silver/customer/api/commons/PreferredLocalLookupHelper.scala; original row 1649.

**Concern stated in the source:** Can we add a base trait `PreferredLocalLookupHelper` too?

```
trait PreferredLocalLookupHelper {
  def getPreferredLocale(customerId: UUID): Future[Locale]
}

trait SgPreferredLocalLookupHelper extends BaseHelper {
  def localConfig: LocalConfig
  final override def getPreferredLocale(customerId: UUID): Future[Locale] = ???
}

trait HkPreferredLocalLookupHelper extends BaseHelper {
  implicit def executionContext: ExecutionContext
  def regionalCustomerService: RegionalCustomerService
  final override def getPreferredLocale(customerId: UUID): Future[Locale] = ???
}
```

‌

This way we can use the base trait in those `Base*Projection` too

**Source-preserving request, proposal, or question:**

> Can we add a base trait `PreferredLocalLookupHelper` too?
> 
> ```
> trait PreferredLocalLookupHelper {
>   def getPreferredLocale(customerId: UUID): Future[Locale]
> }
> 
> trait SgPreferredLocalLookupHelper extends BaseHelper {
>   def localConfig: LocalConfig
>   final override def getPreferredLocale(customerId: UUID): Future[Locale] = ???
> }
> 
> trait HkPreferredLocalLookupHelper extends BaseHelper {
>   implicit def executionContext: ExecutionContext
>   def regionalCustomerService: RegionalCustomerService
>   final override def getPreferredLocale(customerId: UUID): Future[Locale] = ???
> }
> ```
> 
> ‌
> 
> This way we can use the base trait in those `Base*Projection` too

**Conditions and limits:**

- Base PreferredLocalLookupHelper enables shared Base*Projection use; SG and HK implementations retain their different dependencies.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1649 · comment 467668480 · PR 8242 · 2024-02-02

Source path: `customer-api/src/main/scala/com/endowus/silver/customer/api/commons/PreferredLocalLookupHelper.scala`

**Evidence:** anon-2.jsonl:1649 · comment 467668480 · PR 8242 · 2024-02-02

Source path: `customer-api/src/main/scala/com/endowus/silver/customer/api/commons/PreferredLocalLookupHelper.scala`

**Explicit source context (pr_title):**

> [EN-2895] feat(customer): PreferredLocalLookupHelper

## A2-1651 — Review: I mean we still have to write this same method in every communication projection x every service.

**Source stance:** suggestion

**Context:**

> PR 8242 ([EN-2895] feat(customer): PreferredLocalLookupHelper), no inline path; original row 1651.

**Concern stated in the source:** I mean we still have to write this same method in every communication projection x every service.

If both sg and hk are same, then I’m ok with keep this in each service also

**Source-preserving request, proposal, or question:**

> I mean we still have to write this same method in every communication projection x every service.
> 
> If both sg and hk are same, then I’m ok with keep this in each service also

**Conditions and limits:**

- Per-service duplication is accepted if SG/HK behavior is same; cross-service shared helper is only a possible consolidation.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1651 · comment 467676981 · PR 8242 · 2024-02-02

**Evidence:** anon-2.jsonl:1651 · comment 467676981 · PR 8242 · 2024-02-02

**Explicit source context (pr_title):**

> [EN-2895] feat(customer): PreferredLocalLookupHelper

## A2-1679 — RedemptionRequestTopicSubscriberV3: Let’s make this specific to fee redemption only, and move the `request.feeChargeDetails.isDefined` to require clause

**Source stance:** suggestion

**Context:**

> PR 8071 ([INV-1863] feat(transaction): Add cash reservation on assumed status for fee charge), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala; original row 1679.

**Concern stated in the source:** Let’s make this specific to fee redemption only, and move the `request.feeChargeDetails.isDefined` to require clause

Let’s not make assumption about single cash reservation. Today we support taking cash balance from single account, but in future we might not.

**Source-preserving request, proposal, or question:**

> Let’s make this specific to fee redemption only, and move the `request.feeChargeDetails.isDefined` to require clause
> 
> Let’s not make assumption about single cash reservation. Today we support taking cash balance from single account, but in future we might not.

**Conditions and limits:**

- Initial fee-only require proposal is corrected in row 1682 after realizing call also serves other flows. The warning against assuming one cash reservation still remains source-specific.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1679 · comment 463752982 · PR 8071 · 2024-01-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1679 · comment 463752982 · PR 8071 · 2024-01-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> [INV-1863] feat(transaction): Add cash reservation on assumed status for fee charge

## A2-1680 — RedemptionRequestTopicSubscriberV3: Hmm I don’t remember seeing this in prev version? I thought we said we only calculate the chargedByCash and chargedBySell amount without touc...

**Source stance:** open-question

**Context:**

> PR 8071 ([INV-1863] feat(transaction): Add cash reservation on assumed status for fee charge), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala; original row 1680.

**Concern stated in the source:** Hmm I don’t remember seeing this in prev version? I thought we said we only calculate the chargedByCash and chargedBySell amount without touching the assumed amount field? The A&B screenshot seems FE managed to show correct amount in L1

**Source-preserving request, proposal, or question:**

> Hmm I don’t remember seeing this in prev version? I thought we said we only calculate the chargedByCash and chargedBySell amount without touching the assumed amount field? The A&B screenshot seems FE managed to show correct amount in L1

**Conditions and limits:**

- Whether assumed amount should change is questioned; initial understanding was only chargedByCash/chargedBySell updates.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1680 · comment 464186594 · PR 8071 · 2024-01-24

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1680 · comment 464186594 · PR 8071 · 2024-01-24

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> [INV-1863] feat(transaction): Add cash reservation on assumed status for fee charge

## A2-1681 — RedemptionRequestTopicSubscriberV3: Isn’t your 1st screenshot showing 20.91 in L1?

**Source stance:** explanation

**Context:**

> PR 8071 ([INV-1863] feat(transaction): Add cash reservation on assumed status for fee charge), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala; original row 1681.

**Source-preserving request, proposal, or question:**

> Isn’t your 1st screenshot showing 20.91 in L1?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Screenshot-based amount 20.91 is an observation/question, not a verified calculation.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1681 · comment 464187184 · PR 8071 · 2024-01-24

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1681 · comment 464187184 · PR 8071 · 2024-01-24

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Explicit source context (hunk):**

>        val assumedOrdersStatusDetails = AssumedOrdersStatusDetails(
>          transactionStatus = TransactionStatus.SETTLEMENT_ASSUMED_AND_PENDING_FINAL_CONFIRMATION,
> -        assumedAmount = request.settlementAssumption.get.tradeSettlementAssumedAmount,
> +        assumedAmount = assumedAmount,
>          assumedAt = request.settlementAssumption.get.tradeSettlementAssumedAt,
>          orders = request.orders.map(mapRedemptionOrder)
>        )

**Evidence:** anon-2.jsonl:1681 · comment 464187184 · PR 8071 · 2024-01-24

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> [INV-1863] feat(transaction): Add cash reservation on assumed status for fee charge

## A2-1682 — RedemptionRequestTopicSubscriberV3: Right, sorry I missed that… somehow I thought we only call only for fee \(and hence even suggest making it specific with require clause :see_...

**Source stance:** explanation

**Context:**

> PR 8071 ([INV-1863] feat(transaction): Add cash reservation on assumed status for fee charge), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala; original row 1682.

**Concern stated in the source:** Right, sorry I missed that… somehow I thought we only call only for fee \(and hence even suggest making it specific with require clause :see_no_evil: \)

**Source-preserving request, proposal, or question:**

> Right, sorry I missed that… somehow I thought we only call only for fee \(and hence even suggest making it specific with require clause :see_no_evil: \)

**Conditions and limits:**

- Explicit correction: the helper was not fee-only, so earlier suggested require feeChargeDetails.isDefined should not become mandatory.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1682 · comment 464188269 · PR 8071 · 2024-01-24

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1682 · comment 464188269 · PR 8071 · 2024-01-24

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> [INV-1863] feat(transaction): Add cash reservation on assumed status for fee charge

## A2-1697 — BaseRedemptionCommunicationV2Projection: [person] can you check with [person] on how this TAA field is used? Feels very wasteful to lookup portfolio service here, while `planDto...

**Source stance:** open-question

**Context:**

> PR 7858 (Feat/INV-2276/alt emails), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala; original row 1697.

**Concern stated in the source:** [person] can you check with [person] on how this TAA field is used? Feels very wasteful to lookup portfolio service here, while `planDto.targetAssetAllocation` has almost all the data required \(except for the urls\). From the test evidence, it seems we only need the instruments' name

**Source-preserving request, proposal, or question:**

> [person] can you check with [person] on how this TAA field is used? Feels very wasteful to lookup portfolio service here, while `planDto.targetAssetAllocation` has almost all the data required \(except for the urls\). From the test evidence, it seems we only need the instruments' name

**Conditions and limits:**

- Portfolio lookup appears unnecessary if only instrument names are needed; planDto.targetAssetAllocation lacks URLs but contains almost everything else. FE usage confirmation remains open.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1697 · comment 456744467 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

> can you check with

**Evidence:** anon-2.jsonl:1697 · comment 456744467 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

> on how this TAA field is used? Feels very wasteful to lookup portfolio service here, while `planDto.targetAssetAllocation` has almost all the data required \(except for the urls\). From the test evidence, it seems we only need the instruments' name

**Evidence:** anon-2.jsonl:1697 · comment 456744467 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> Feat/INV-2276/alt emails

## A2-1698 — BaseRedemptionCommunicationV2Projection: Is it ok for us to change for this email too?

**Source stance:** open-question

**Context:**

> PR 7858 (Feat/INV-2276/alt emails), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala; original row 1698.

**Source-preserving request, proposal, or question:**

> Is it ok for us to change for this email too?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1698 · comment 456786341 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Evidence:** anon-2.jsonl:1698 · comment 456786341 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Explicit source context (hunk):**

> +          ),
> +          templateData = RedemptionCompletedData(
> +            DATE = FormatterUtils.dateFormatterDayFullMonthYear.format(request.timestamps.createdAt),
> +            ACCOUNT_NAME = TradingAccountType.tradingAccountToUserFriendlyNameMap(tradingAccountType),
> +            CALL_TO_ACTION_URL = uri"${localConfig.getSilverWebAppBaseUrl}/$Cta",
> +            GOAL_NAME = goal.name,
> +            WITHDRAW_TO_LINKED_BANK_ACCOUNT = request.withdrawToLinkedBankAccount,

**Evidence:** anon-2.jsonl:1698 · comment 456786341 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> Feat/INV-2276/alt emails

## A2-1699 — BaseRedemptionCommunicationV2Projection: We should just log error and move on instead of throwing and potentially block the projection here

**Source stance:** suggestion

**Context:**

> PR 7858 (Feat/INV-2276/alt emails), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala; original row 1699.

**Source-preserving request, proposal, or question:**

> We should just log error and move on instead of throwing and potentially block the projection here

**Conditions and limits:**

- Log and continue instead of throwing if that would block this projection.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1699 · comment 456786454 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Evidence:** anon-2.jsonl:1699 · comment 456786454 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> Feat/INV-2276/alt emails

## A2-1700 — BaseRedemptionCommunicationV2Projection: Can we confirm that it’s correct to use confirmedAt as trade date here? My understanding is Alts redemption settlement is extra long, so...

**Source stance:** open-question

**Context:**

> PR 7858 (Feat/INV-2276/alt emails), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala; original row 1700.

**Concern stated in the source:** Can we confirm that it’s correct to use confirmedAt as trade date here? My understanding is Alts redemption settlement is extra long, so the timestamp when we process the settlement \(confirmedAt\) could be very different from actual trade date

**Source-preserving request, proposal, or question:**

> Can we confirm that it’s correct to use confirmedAt as trade date here? My understanding is Alts redemption settlement is extra long, so the timestamp when we process the settlement \(confirmedAt\) could be very different from actual trade date

**Conditions and limits:**

- Alts redemption settlement delay means confirmedAt processing timestamp may differ substantially from actual trade date; proper choice is unresolved.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1700 · comment 456786909 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Evidence:** anon-2.jsonl:1700 · comment 456786909 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> Feat/INV-2276/alt emails

## A2-1701 — BaseRedemptionCommunicationV2Projection: Ah we already filter for this in the main handle method

**Source stance:** explanation

**Context:**

> PR 7858 (Feat/INV-2276/alt emails), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala; original row 1701.

**Source-preserving request, proposal, or question:**

> Ah we already filter for this in the main handle method

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1701 · comment 456787557 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Evidence:** anon-2.jsonl:1701 · comment 456787557 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> Feat/INV-2276/alt emails

## A2-1702 — BaseRedemptionCommunicationV2Projection: Not sure how this metrics field is used. Can you also confirm if we need new name for Alts?

**Source stance:** open-question

**Context:**

> PR 7858 (Feat/INV-2276/alt emails), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala; original row 1702.

**Source-preserving request, proposal, or question:**

> Not sure how this metrics field is used. Can you also confirm if we need new name for Alts?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- SendgridEmailMetrics RedemptionRequestInitiated naming for Alts remains unresolved.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1702 · comment 456789828 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Evidence:** anon-2.jsonl:1702 · comment 456789828 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Explicit source context (hunk):**

> +            ),
> +            sendgridKeyToLocaleSpecificData = Map(),
> +            metrics = SendgridEmailMetrics(List(RedemptionRequestInitiated))
> +          ),
> +          isTimeSensitive = false
> +        )
> +      )

**Evidence:** anon-2.jsonl:1702 · comment 456789828 · PR 7858 · 2023-12-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> Feat/INV-2276/alt emails

## A2-1704 — BaseRedemptionCommunicationV2Projection: It’s the same thing but we have some utils in OptionUtils to make this a bit more fluent \(I think\)

**Source stance:** suggestion

**Context:**

> PR 7858 (Feat/INV-2276/alt emails), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala; original row 1704.

**Concern stated in the source:** It’s the same thing but we have some utils in OptionUtils to make this a bit more fluent \(I think\)

```
val maybeAmount = request.settlementConfirmation
  .onNone(logger.error(...))
  .map(_.tradeSettlementConfirmAmount)
  .map(FormatterUtils.TwoMinDecimalPlaceNumberFormatter.format(_))
```

‌

**Source-preserving request, proposal, or question:**

> It’s the same thing but we have some utils in OptionUtils to make this a bit more fluent \(I think\)
> 
> ```
> val maybeAmount = request.settlementConfirmation
>   .onNone(logger.error(...))
>   .map(_.tradeSettlementConfirmAmount)
>   .map(FormatterUtils.TwoMinDecimalPlaceNumberFormatter.format(_))
> ```
> 
> ‌

**Conditions and limits:**

- OptionUtils.onNone logging plus map to tradeSettlementConfirmAmount and TwoMinDecimalPlaceNumberFormatter avoids blind get.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1704 · comment 457680821 · PR 7858 · 2024-01-02

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Evidence:** anon-2.jsonl:1704 · comment 457680821 · PR 7858 · 2024-01-02

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> Feat/INV-2276/alt emails

## A2-1709 — CustomerAdvisoryProfileDataV2: Identical to `CustomerAdvisoryProfileData` with extra 3 fields `annualIncome` / `liquidNetWorth` / `craQuestionnaire`. Same for the V2 tables.

**Source stance:** explanation

**Context:**

> PR 7935 ([INV-2418] feat(advisory): Add V2 for customer_advisory_profile tables with new columns for annualIncome/liquidNetWorth/craQuestionnaire), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileDataV2.scala; original row 1709.

**Concern stated in the source:** Identical to `CustomerAdvisoryProfileData` with extra 3 fields `annualIncome` / `liquidNetWorth` / `craQuestionnaire`. Same for the V2 tables.

New dbHandler and projection just switch to use V2 accordingly.

**Source-preserving request, proposal, or question:**

> Identical to `CustomerAdvisoryProfileData` with extra 3 fields `annualIncome` / `liquidNetWorth` / `craQuestionnaire`. Same for the V2 tables.
> 
> New dbHandler and projection just switch to use V2 accordingly.

**Conditions and limits:**

- New CustomerAdvisoryProfile V2 adds annualIncome/liquidNetWorth/craQuestionnaire; handler/projection switch to V2.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1709 · comment 455693187 · PR 7935 · 2023-12-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileDataV2.scala`

**Evidence:** anon-2.jsonl:1709 · comment 455693187 · PR 7935 · 2023-12-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileDataV2.scala`

**Explicit source context (pr_title):**

> [INV-2418] feat(advisory): Add V2 for customer_advisory_profile tables with new columns for annualIncome/liquidNetWorth/craQuestionnaire

## A2-1711 — CustomerAdvisoryProfileJdbcEventProjectionV2: Yea this should give us zero impact for now, cuz we don’t expect `ExpiryDateOverriddenEvt` or `CraExpiredEvt` in prod yet. And data...

**Source stance:** explanation

**Context:**

> PR 7935 ([INV-2418] feat(advisory): Add V2 for customer_advisory_profile tables with new columns for annualIncome/liquidNetWorth/craQuestionnaire), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileJdbcEventProjectionV2.scala; original row 1711.

**Concern stated in the source:** Yea this should give us zero impact for now, cuz we don’t expect `ExpiryDateOverriddenEvt` or `CraExpiredEvt` in prod yet. And data team can do a simple check between v1 and v2 table to identify missing records, if at all.

Going forward though, we will certainly start seeing `CraExpiredEvt`. We should look into handle this better, if we ever. need to upversion this table again - which in theory should be ok, cuz we already capture all the fields.

**Source-preserving request, proposal, or question:**

> Yea this should give us zero impact for now, cuz we don’t expect `ExpiryDateOverriddenEvt` or `CraExpiredEvt` in prod yet. And data team can do a simple check between v1 and v2 table to identify missing records, if at all.
> 
> Going forward though, we will certainly start seeing `CraExpiredEvt`. We should look into handle this better, if we ever. need to upversion this table again - which in theory should be ok, cuz we already capture all the fields.

**Conditions and limits:**

- No immediate impact depends on ExpiryDateOverriddenEvt/CraExpiredEvt not yet existing in prod; future upversions must handle CraExpiredEvt, and data-team V1/V2 diff may detect gaps.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1711 · comment 456731490 · PR 7935 · 2023-12-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileJdbcEventProjectionV2.scala`

**Evidence:** anon-2.jsonl:1711 · comment 456731490 · PR 7935 · 2023-12-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileJdbcEventProjectionV2.scala`

**Explicit source context (pr_title):**

> [INV-2418] feat(advisory): Add V2 for customer_advisory_profile tables with new columns for annualIncome/liquidNetWorth/craQuestionnaire

## A2-1776 — AltsLcoCalculationMatrix: Feels like this and the scoreCalculator can be refactor a bit more to remove duplicate code, but ok we can iterate on this later

**Source stance:** suggestion

**Context:**

> PR 7673 (Resolve INV-2277: Add alts suitability check for instruments using LCO match.), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/calculators/questionnaire/alts/suitability/AltsLcoCalculationMatrix.scala; original row 1776.

**Concern stated in the source:** Feels like this and the scoreCalculator can be refactor a bit more to remove duplicate code, but ok we can iterate on this later

**Source-preserving request, proposal, or question:**

> Feels like this and the scoreCalculator can be refactor a bit more to remove duplicate code, but ok we can iterate on this later

**Conditions and limits:**

- More duplicate-code refactor can wait.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1776 · comment 450195853 · PR 7673 · 2023-12-04

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/calculators/questionnaire/alts/suitability/AltsLcoCalculationMatrix.scala`

**Evidence:** anon-2.jsonl:1776 · comment 450195853 · PR 7673 · 2023-12-04

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/calculators/questionnaire/alts/suitability/AltsLcoCalculationMatrix.scala`

**Explicit source context (pr_title):**

> Resolve INV-2277: Add alts suitability check for instruments using LCO match.

## A3-0006 — InstrumentMStarAddMarketDataTable.scala: Miscomm then lol. I guess because you wanted to update annual yield via processor?

**Source stance:** open-question

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarAddMarketDataTable.scala; PR: Feat/INV-2229 marketdata ex dividend bond yield

**Concern stated in the source:** I guess because you wanted to update annual yield via processor?

**Source-preserving request, proposal, or question:**

> Miscomm then lol. I guess because you wanted to update annual yield via processor?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1812 · comment 442780745 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarAddMarketDataTable.scala`

**Evidence:** anon-2.jsonl:1812 · comment 442780745 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarAddMarketDataTable.scala`

**Explicit source context (hunk):**

> +  def instrumentId = column[String]("instrument_id")
> +  def instrumentMstarData = column[InstrumentMstarData]("instrument_mstar_data")
> +  def lastUpdated = column[Instant]("last_updated_at")
> +
> +  def pk = primaryKey(InstrumentMstarDataTable.PKName, instrumentId)
> +
> +  override def * : ProvenShape[InstrumentMstarDataVo] = (

## A3-0015 — ServiceLogicImpl.scala: will need your help to change this to use readside after yours are in

**Source stance:** requested-change

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; PR: [INV-2214] feat(advisory)(instrument): WIP FundSmart instrument details

**Source-preserving request, proposal, or question:**

> will need your help to change this to use readside after yours are in

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1823 · comment 442076880 · PR 7385 · 2023-11-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1823 · comment 442076880 · PR 7385 · 2023-11-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +    val filteredInstrumentIds = instrumentIds.split(",").toList.map(_.trim).filterNot(_.isEmpty)
> +    Source(filteredInstrumentIds)
> +      .mapAsync(2) { instrumentId =>
> +        getInstrumentAnnualYield(instrumentId, ccy)
> +          .map(instrumentId -> _)
> +      }
> +      .runWith(Sink.seq)

## A3-0016 — RecurringInvestmentScheduleHistoryDataEventProcessor.scala: Let’s also remove the existing `ReadSideId`?

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryDataEventProcessor.scala; PR: [PLATFORM-1071] Postgres read side table migration: Create aurora tables for goal

**Source-preserving request, proposal, or question:**

> Nit: Let’s also remove the existing `ReadSideId`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1824 · comment 440867048 · PR 7132 · 2023-11-01

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryDataEventProcessor.scala`

> Nit: Let’s also remove the existing `ReadSideId`?
> 
> ‌

**Evidence:** anon-2.jsonl:1824 · comment 440867048 · PR 7132 · 2023-11-01

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryDataEventProcessor.scala`

**Explicit source context (hunk):**

> private val migrator = new CassandraMigrator(session)
>  
> +  private val ProjectionId = s"recurring-investment-schedule-history-data-evt-handler-v${version}"
> +
>    def start(): CassandraProjectionManager[GoalEvt] = {
>      ProjectionBuilder

## A3-0024 — InstrumentJdbcEventProcessorV2.scala: use CassandraProjectionManager

**Source stance:** requested-change

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessorV2.scala; PR: Resolve INV-2127: New read side table instrument entity v2

**Source-preserving request, proposal, or question:**

> Let’s use CassandraProjectionManager

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:1832 · comment 439499446 · PR 7211 · 2023-10-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessorV2.scala`

## A3-0025 — InstrumentJdbcEventProcessorV2.scala: follow the pattern we have in other services with JdbcSchema

**Source stance:** requested-change

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessorV2.scala; PR: Resolve INV-2127: New read side table instrument entity v2

**Source-preserving request, proposal, or question:**

> Let’s follow the pattern we have in other services with JdbcSchema

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:1833 · comment 439499518 · PR 7211 · 2023-10-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessorV2.scala`

## A3-0026 — InstrumentV2JdbcDbHandler.scala: We don’t really need transaction for readside so we can inject db here, and return Future… it’s easier to use and mock in test if needed

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/db/jdbc/InstrumentV2JdbcDbHandler.scala; PR: Resolve INV-2127: New read side table instrument entity v2

**Source-preserving request, proposal, or question:**

> We don’t really need transaction for readside so we can inject db here, and return Future… it’s easier to use and mock in test if needed

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1834 · comment 439499719 · PR 7211 · 2023-10-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/db/jdbc/InstrumentV2JdbcDbHandler.scala`

**Evidence:** anon-2.jsonl:1834 · comment 439499719 · PR 7211 · 2023-10-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/db/jdbc/InstrumentV2JdbcDbHandler.scala`

**Explicit source context (hunk):**

> +  private val instruments = TableQuery[InstrumentV2Table]
> +
> +  def upsert(instrument: Instrument): Future[Unit] = {
> +    db.run(instruments.insertOrUpdate(instrument)).flatMap {
> +      case 0 | 1 => Future.unit
> +      case n     => Future.failed(new Exception(s"Expected 0 or 1 updated, but got $n"))
> +    }

## A3-0027 — InstrumentJdbcEventProcessorV2.scala: It’s just a bit cleaner to group them together, both those with event processor and those pure CRUD

**Source stance:** explanation

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessorV2.scala; PR: Resolve INV-2127: New read side table instrument entity v2

**Source-preserving request, proposal, or question:**

> It’s just a bit cleaner to group them together, both those with event processor and those pure CRUD

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:1835 · comment 439501224 · PR 7211 · 2023-10-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessorV2.scala`

## A3-0028 — InstrumentDbEventProcessorNew.scala: we can remove already. BQ is currently using pg instruments\_v4

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/InstrumentDbEventProcessorNew.scala; PR: Resolve INV-2127: New read side table instrument entity v2

**Source-preserving request, proposal, or question:**

> I think we can remove already. BQ is currently using pg instruments\_v4

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:1837 · comment 440529544 · PR 7211 · 2023-10-31

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/InstrumentDbEventProcessorNew.scala`

## A3-0033 — DailyMvPersistenceHelper.scala: Extract this logic out of `PlanTimeSeriesTopicSubscriber` and let it handle updating both dailyMV and dailyMVAuditEntry tables

**Source stance:** requested-change

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvPersistenceHelper.scala; PR: [INV-2015] feat(charge): Support estimated daily fee

**Source-preserving request, proposal, or question:**

> Extract this logic out of `PlanTimeSeriesTopicSubscriber` and let it handle updating both dailyMV and dailyMVAuditEntry tables

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1843 · comment 438139789 · PR 7266 · 2023-10-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvPersistenceHelper.scala`

**Evidence:** anon-2.jsonl:1843 · comment 438139789 · PR 7266 · 2023-10-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvPersistenceHelper.scala`

**Explicit source context (hunk):**

> +      .maximumSize(20000)
> +      .buildAsyncFuture { case (goalId, planId) => queryPlanProfileDetail(goalId, planId) }
> +
> +  def batchUpsert(
> +    customerId: UUID,
> +    goalId: UUID,
> +    planId: UUID,

## A3-0056 — BrokerCashTransactionTopicSubscriberV3.scala: transactionV3 is good enough I think… no need to repeat the topic in group name

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV3.scala; PR: Feat/INV-1972 v3 transaction subscriber

**Source-preserving request, proposal, or question:**

> transactionV3 is good enough I think… no need to repeat the topic in group name

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1870 · comment 439560556 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1870 · comment 439560556 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV3.scala`

**Explicit source context (hunk):**

> +}
> +
> +object BrokerCashTransactionTopicSubscriberV3 {
> +
> +  val groupId = "transaction-subscriber-v3"
> +
> +  def createDepositTransaction(

## A3-0057 — BrokerCashTransactionTopicSubscriberV3.scala: Can we add some log here, info is good enough I think, saying that we are skipping because txn is already deleted

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV3.scala; PR: Feat/INV-1972 v3 transaction subscriber

**Concern stated in the source:** Can we add some log here, info is good enough I think, saying that we are skipping because txn is already deleted

**Source-preserving request, proposal, or question:**

> Can we add some log here, info is good enough I think, saying that we are skipping because txn is already deleted

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1871 · comment 439561264 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1871 · comment 439561264 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV3.scala`

**Explicit source context (hunk):**

> +          Future.successful(Done)
> +        } else if (transaction.statusDetails.isInstanceOf[DeletedStatusDetails]) {
> +          logger.info(s"Transaction [${msg.transactionId}] is already in deleted status, skipping the message...")
> +          Future.successful(Done)
> +        } else {
> +          val cmd = UpdateTransactionCmd(_, transaction = deletedTransactionMaybe.get, forceUpdate = true)
> +          refProvider.getTransactionV3EntityRef(msg.transactionId).ask(cmd)

## A3-0086 — TransactionV2AccountSerializerRegistry.scala: I suppose we don’t migrate state because we only need events to move to V3?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala; PR: Feat/INV-2152 hk v2 v3 migration processor

**Concern stated in the source:** I suppose we don’t migrate state because we only need events to move to V3?

**Source-preserving request, proposal, or question:**

> I suppose we don’t migrate state because we only need events to move to V3?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1903 · comment 438080163 · PR 7261 · 2023-10-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala`

**Evidence:** anon-2.jsonl:1903 · comment 438080163 · PR 7261 · 2023-10-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala`

**Explicit source context (hunk):**

> +    classOf[TransactionUpdatedEvt].getName -> TransactionV2UpdatedEvtMigration1
> +}
> +
> +class TransactionV2UpdatedEvtMigrator
> +  extends JsonMigrationCapture2(TransactionV2AccountSerializerRegistry.TransactionV2UpdatedEvtMigration)
> +

## A3-0089 — Staging skips are temporary unblockers; remove default skips and observe issues

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RebalanceTopicSubscriber.scala; PR: [INV-1504] feat(goal)(rebalance): Avoid race condition for TAA update between goal modification vs RPC acceptance

**Concern stated in the source:** We shouldn’t skip by default like this, cuz we don’t always check Sentry in Staging

**Source-preserving request, proposal, or question:**

> Yeah let’s remove and observe what kind of issues we skip in Staging. Ideally these skips should be temporary only to unblock some known issue that we have no resource to fix. We shouldn’t skip by default like this, cuz we don’t always check Sentry in Staging

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1906 · comment 429841433 · PR 6953 · 2023-09-22

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RebalanceTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:1906 · comment 429841433 · PR 6953 · 2023-09-22

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RebalanceTopicSubscriber.scala`

**Explicit source context (hunk):**

> rebalanceService: RebalanceService,
>    portfolioService: PortfolioService,
>    localConfig: LocalConfig
> -)(implicit ec: ExecutionContext, mat: Materializer) {
> -
> -  private val log: Logger = LoggerFactory.getLogger(this.getClass.getCanonicalName)
> +)(implicit ec: ExecutionContext, mat: Materializer)
> +    extends StrictLogging {
>  
>    rebalanceService.rebalanceTopic.subscribe
>      .atLeastOnce(Flow[RebalanceMsg].mapAsync(parallelism = 1) {
> +      case msg: RebalanceRequestAcceptedAndPendingSellProcessMsg =>
> +        val rebalanceRequest = msg.rebalanceRequest
> +        rebalanceRequest.reason match {
> +          case RebalanceReason.THRESHOLD_BREACH =>
> +            notifyOtherRebalanceStarted(
> +

## A3-0095 — UpdateCurrentAssetAllocationCmdHandler.scala: For RPC, goal svc will send a TAA updated msg which will trigger this cmd. However, we will skip it, cuz we change the flow to trigger both RPC/Breach

**Source stance:** explanation

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/UpdateCurrentAssetAllocationCmdHandler.scala; PR: [INV-1504] feat(goal)(rebalance): Avoid race condition for TAA update between goal modification vs RPC acceptance

**Concern stated in the source:** However, we will skip it, cuz we change the flow to trigger both RPC/Breach rebalance using the rebalance started msg from goal.

**Source-preserving request, proposal, or question:**

> For RPC, goal svc will send a TAA updated msg which will trigger this cmd. However, we will skip it, cuz we change the flow to trigger both RPC/Breach rebalance using the rebalance started msg from goal. Hence this is info log.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1912 · comment 430383223 · PR 6953 · 2023-09-25

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/UpdateCurrentAssetAllocationCmdHandler.scala`

**Evidence:** anon-2.jsonl:1912 · comment 430383223 · PR 6953 · 2023-09-25

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/UpdateCurrentAssetAllocationCmdHandler.scala`

**Explicit source context (hunk):**

> +      cmd.rebalanceRequestId.contains(request.rebalanceRequestId)
> +    } match {
> +      case Some(existingRequest) if existingRequest.reason == RebalanceReason.PORTFOLIO_VERSION_UPDATE =>
> +        logger.info(s"""
> +        |RebalancePlanEntity [$entityId] is skipping UpdateCurrentAssetAllocationCmd for RPC request ${existingRequest.rebalanceRequestId}
> +        |which is in status ${existingRequest.status}. Rebalance will trigger via InitiateAcceptedRebalanceSuggestionCmdHandler instead.
> +        |""".fuse)

## A3-0108 — Estimated fee resend: forceResend plus customer include/exclude sets, not amount-derived comm ID

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeEstimateNotificationManager.scala; PR: [INV-2016] feat(communication)(charge): Email notification for estimated upcoming quarterly charge (support only NonAlts for now)

**Source-preserving request, proposal, or question:**

> Support `forceResend` flag with customerId include/exclude sets instead if we ever want to resend. I want to avoid logic to generate unique comm id based on the amount.
> 
> Since it’s estimation, I suppose we don’t typically resend anyway unless sth is very wrong

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1925 · comment 433290188 · PR 7106 · 2023-10-05

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeEstimateNotificationManager.scala`

**Evidence:** anon-2.jsonl:1925 · comment 433290188 · PR 7106 · 2023-10-05

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeEstimateNotificationManager.scala`

**Explicit source context (hunk):**

> +        year,
> +        quarter,
> +        feeType
> +      ) ++ forceResend.filter(identity).map(_ => UUID.randomUUID())
> +      tokens.mkString("|")
> +    }
> +

## A3-0116 — RPC endpoints intentionally differ: customer readside versus goal entity consistency

**Source stance:** requested-change

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: [INV-1988] feat(gateway, rebalance): migrate recommended portfolio changes endpoint from davinci

**Source-preserving request, proposal, or question:**

> Ah nevermind me lol. Let’s put a comment to explain that customer endpoint is using readside while goal endpoint is using entity for data consistency

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 1932, 1933: Struck-through shared-code suggestion is revised to explain customer-readside versus goal-entity behavior.

**Evidence:** anon-2.jsonl:1933 · comment 431718424 · PR 6874 · 2023-09-29

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1933 · comment 431718424 · PR 6874 · 2023-09-29

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +      plans = goal.plans.map(p => (p.planId, p.tradingAccountType, goal.name, goal.investmentGoalType))
> +      recommendedPortfolioChangeDtos <- Source(plans)
> +        .mapAsync(2) {
> +          case (planId, tradingAccountType, goalName, goalType) =>
> +            for {
> +              rebalanceRequestDtos <- getRebalanceRequestDtosForGoal(
> +                customerId = goal.customerId,

## A3-0145 — FeeManager.scala: We call per request here, so decide to consolidate tax details in the event processor instead by calling TaxHelper

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeManager.scala; PR: [INV-2014] feat(voucher)(charge): Support discount + tax simulation in fee query endpoint

**Source-preserving request, proposal, or question:**

> We call per request here, so decide to consolidate tax details in the event processor instead by calling TaxHelper

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1964 · comment 431721589 · PR 7042 · 2023-09-29

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeManager.scala`

**Evidence:** anon-2.jsonl:1964 · comment 431721589 · PR 7042 · 2023-09-29

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeManager.scala`

**Explicit source context (hunk):**

> strictEndDate = Some(initiatingSettlementDate)
>          )
>  
> -        shouldExemptTax <- taxExemptionManager.isCustomerExempted(customerId, previousQuarterStartDate, currentQuarterEndDate)
> -
>          feeChargeCommand = InitiateFeeChargeForFullRedemptionCmd(
>            _,
>            initiatingYear = year,

## A3-0148 — MV-before-plan-topic race creates planProfile with wrong planCcy; remove early creation

**Source stance:** observed-defect

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala; PR: [INV-2014] feat(voucher)(charge): Support discount + tax simulation in fee query endpoint

**Concern stated in the source:** Bug here causing planProfile in charge having wrong planCcy if somehow MV arrives before planProfile is created via kafka from plan topic.

Removed this code completely to avoid race condition.

**Source-preserving request, proposal, or question:**

> Bug here causing planProfile in charge having wrong planCcy if somehow MV arrives before planProfile is created via kafka from plan topic.
> 
> Removed this code completely to avoid race condition. PlanProfile will be eventually created, and here we simply need a goalType

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1967 · comment 431835256 · PR 7042 · 2023-09-29

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:1967 · comment 431835256 · PR 7042 · 2023-09-29

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala`

**Explicit source context (hunk):**

> )
>    }
>  
> -  private def getGoalTypeMayBeInitPlanProfile(d: DailyMarketValueDto, noCache: Boolean, goalId: UUID, planId: UUID) = {
> +  private def queryGoalType(d: DailyMarketValueDto, noCache: Boolean, goalId: UUID, planId: UUID) = {
>      val maybeFromCache = cache.getIfPresent(goalId)
> -    val goalTypeFut = if (!noCache && maybeFromCache.isDefined) {
> -      Future.successful(maybeFromCache.get)
> -    } else {
> -      for {
> -        maybePlanProfile <- refProvider.getFeeManagerEntity(planId).ask(GetPlanProfileCmd(_))
> -        goalType <- if (maybePlanProfile.isEmpty || maybePlanProfile.get.targetPortfolio.isEmpty) {
> -          for {
> -            goal <- goalService.getGoalById(goalId).in

## A3-0183 — CustomerTransactionMigrationEventProcessor.scala: Hmm I guess it’s ok, but we will lose the requestedBy and reason in these events

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala; PR: Feat/INV-1972 transaction migrator processor

**Source-preserving request, proposal, or question:**

> Hmm I guess it’s ok, but we will lose the requestedBy and reason in these events

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2003 · comment 426642760 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala`

**Evidence:** anon-2.jsonl:2003 · comment 426642760 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala`

**Explicit source context (hunk):**

> +        .map(_.transaction)
> +      transactionV2 <- convertTransaction(transaction, eventTimestamp)
> +      res <- refProvider.getTransactionEntityRef(transaction.transactionId)
> +        .ask(ForceOverrideTransactionCmd(
> +          _,
> +          transaction = transactionV2,
> +          expectedExistingTransaction = existingTransaction,

## A3-0228 — DetectExpiringRecurringInvestmentCmdHandler.scala: Why don’t we just send the communication directly from the scheduler? I’m thinking this is really not an event for GoalEntity - no logic in cmd handle

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/DetectExpiringRecurringInvestmentCmdHandler.scala; PR: [EN-1992] Add support for recurring investment expiring communications

**Source-preserving request, proposal, or question:**

> Why don’t we just send the communication directly from the scheduler? I’m thinking this is really not an event for GoalEntity - no logic in cmd handler, no state changes in entity…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2051 · comment 420897481 · PR 6715 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/DetectExpiringRecurringInvestmentCmdHandler.scala`

## A3-0229 — ExpiringRecurringInvestmentScheduleProcessor.scala: I suppose we can extract the communication bits to another class - which has Base containing the methods to send out various notification types, and S

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/schedulers/ExpiringRecurringInvestmentScheduleProcessor.scala; PR: [EN-1992] Add support for recurring investment expiring communications

**Source-preserving request, proposal, or question:**

> I suppose we can extract the communication bits to another class - which has Base containing the methods to send out various notification types, and SgImpl calling all 3 types while HkImpl calling only 2

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2052 · comment 422282264 · PR 6715 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/schedulers/ExpiringRecurringInvestmentScheduleProcessor.scala`

## A3-0243 — PlanCommunicationV2EventProcessor.scala: Can we extract this communication sending to separate method so it’s easier to follow? ``` event.removalReason match { case Some(RecurringInvestmentSc

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; PR: [EN-2017] Add support for recurring investment expired removal

**Source-preserving request, proposal, or question:**

> Nit: Can we extract this communication sending to separate method so it’s easier to follow?
> 
> ```
> event.removalReason match {
>   case Some(RecurringInvestmentScheduleRemovalReason.Expiration) | Some(RecurringInvestmentScheduleRemovalReason.Deactivation) =>
>     logger.info(
>       s"skipping to send email RECURRING_INVESTMENT_STOPPED for customer [${event.customerId}] due to [${event.removalReason}] removal reason!"
>     )
>     Future.successful(Done)
>   case Some(removalReason) =>
>     sendRecurringInvestmentStoppedCommunication(event, previousSchedule, removalReason)
>   case None =>
>     sendRecurringInvestmentStoppedCommunication(event, previousSchedule, RecurringInvestmentScheduleRemovalReason.IsOtherCancellation)
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2066 · comment 424832352 · PR 6804 · 2023-09-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

> Nit: Can we extract this communication sending to separate method so it’s easier to follow?
> 
> ```
> event.removalReason match {
>   case Some(RecurringInvestmentScheduleRemovalReason.Expiration) | Some(RecurringInvestmentScheduleRemovalReason.Deactivation) =>
>     logger.info(
>       s"skipping to send email RECURRING_INVESTMENT_STOPPED for customer [${event.customerId}] due to [${event.removalReason}] removal reason!"
>     )
>     Future.successful(Done)
>   case Some(removalReason) =>
>     sendRecurringInvestmentStoppedCommunication(event, previousSchedule, removalReason)
>   case None =>
>     sendRecurringInvestmentStoppedCommunication(event, previousSchedule, RecurringInvestmentScheduleRemovalReason.IsOtherCancellation)
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2066 · comment 424832352 · PR 6804 · 2023-09-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> -        } yield Done
> +            Future.successful(Done)
> +          case Some(removalReason) =>
> +            sendRecurringInvestmentStoppedCommunication(event, previousSchedule, removalReason)
> +          case None =>
> +            sendRecurringInvestmentStoppedCommunication(event, previousSchedule, RecurringInvestmentScheduleRemovalReason.Others)
> +        }

## A3-0256 — Schedule history without key duplicates on event retry

**Source stance:** observed-defect

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Concern stated in the source:** exception and retry\), we will insert multiple duplicate entries

**Source-preserving request, proposal, or question:**

> This history table doesn’t have key… if for whatever reason the event is replayed \(e.g. exception and retry\), we will insert multiple duplicate entries

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Related source rows 2080, 2086, 2089: History PK opinion evolves from broad composite suggestion to duplicate-tolerance or fakeUUID PK; do not flatten to mandatory wide composite key.

**Evidence:** anon-2.jsonl:2080 · comment 422183334 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

## A3-0257 — RecurringInvestmentScheduleJdbcEventProcessor.scala: `upsertPlanRecurringInvestmentSchedule` will skip if schedule is None? don’t we need another method to delete in dbHandler?

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Source-preserving request, proposal, or question:**

> `upsertPlanRecurringInvestmentSchedule` will skip if schedule is None? don’t we need another method to delete in dbHandler?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2081 · comment 422183564 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2081 · comment 422183564 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +        endingOnDate = scheduleEndingOnDate,
> +        recurrenceEndConfig = scheduleEndConfig,
> +        expiredOnDate = getExpiredOnDate(scheduleEndingOnDate, scheduleEndConfig),
> +        updatedAt = updatedAt
> +      )
> +      val resultFut = for {
> +        result <- scheduleJdbcDbHandler.upsert(schedule)

## A3-0259 — : Can we add tests too please, for both processor and repository

**Source stance:** requested-change

**Context:**

> None; PR: [EN-2021] Add readside table for plan recurring investment

**Source-preserving request, proposal, or question:**

> Can we add tests too please, for both processor and repository

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2083 · comment 422184060 · PR 6740 · 2023-08-25

## A3-0263 — Schedule deactivation domain events belong in command/PlanProjection; JDBC writes only

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryJdbcEventProcessor.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Source-preserving request, proposal, or question:**

> Ideally I’d prefer that either:
> 
> * `DeactivateGoalCmdHandler` should also check and emit `PlanRecurringInvestmentScheduleRemovedEvt`
> * or `PlanProjection` to handle `PlanDeactivatedEvt` and trigger cmd `StopRecurringInvestmentScheduleCmd`
> 
> Then in jdbc projections \(both history and latest\), we just perform purely db update.
> 
> 
> 
> Today we don’t have such logic, and the `RecurringInvestmentProcessor` only cares about active plans, and that’s why it works.
> 
> I think let’s add the above logic, and we can leave the old inactive plans with recurring schedule as is, or run a script to stop them. But let’s not mix the logic here.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Do not mix deactivation/schedule domain behavior into JDBC projections; preserves both command/event alternatives and historical inactive-plan options.

**Evidence:** anon-2.jsonl:2087 · comment 422617963 · PR 6740 · 2023-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryJdbcEventProcessor.scala`

> Ideally I’d prefer that either:
> 
> * `DeactivateGoalCmdHandler` should also check and emit `PlanRecurringInvestmentScheduleRemovedEvt`
> * or `PlanProjection` to handle `PlanDeactivatedEvt` and trigger cmd `StopRecurringInvestmentScheduleCmd`
> 
> Then in jdbc projections \(both history and latest\), we just perform purely db update.
> 
> ‌
> 
> Today we don’t have such logic, and the `RecurringInvestmentProcessor` only cares about active plans, and that’s why it works.
> 
> I think let’s add the above logic, and we can leave the old inactive plans with recurring schedule as is, or run a script to stop them. But let’s not mix the logic here.
> 
> ‌

## A3-0264 — Mutable endingOnDate/toBeExpiredOn indices: catch up projection before adding indices

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleJdbcRepositoryImpl.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Concern stated in the source:** Indices on customerId/goalId are generally ok because for a given planId \(pkey\), these fields do not change.

**Source-preserving request, proposal, or question:**

> Just something to note, index is not free, it has impact on writes. Indices on customerId/goalId are generally ok because for a given planId \(pkey\), these fields do not change. It’s just single insert/update for these indices.
> 
> However, endingOnDate / toBeExpiredOn fields can be updated a given planId. That would be a delete and then insert for these indices. It might be ok still for our usage, but just something to think about. I would suggest we release the projection to prod without these 2 indices first, let it catch up with all the events, then we make another release to add the indices.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve rollout: project without endingOnDate/toBeExpiredOn indices, catch up all events, release indices later; mutable indexed fields require delete+insert.

**Evidence:** anon-2.jsonl:2088 · comment 422619100 · PR 6740 · 2023-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleJdbcRepositoryImpl.scala`

**Evidence:** anon-2.jsonl:2088 · comment 422619100 · PR 6740 · 2023-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleJdbcRepositoryImpl.scala`

**Explicit source context (hunk):**

> +            .filter(_.endingOnDate === date)
> +            .result
> +        )
> +      )
> +  }
> +
> +  override def streamRecurringInvestmentSchedulesByExpiredOnDate(

## A3-0265 — UpdatedEvt old/new inserts and offset-commit failures: duplicate windows and PK alternatives

**Source stance:** explanation

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Concern stated in the source:** Even with separate processors, the chance of duplicated rows is still there because we perform 2 inserts for UpdatedEvt \(but yes, splitting the processors reduce this chance much further\)

Even for event with single insert, duplicates can happen if insert succeeds and offset commit fails.

If data side is able to handle the \(rare\) duplicates, I’d say we stick with no pk.

However, if data side insists we cannot have duplicates, then as  suggested, generate a fake UUID based on the fields, and use it as pk.

Let’s not add a composite key so many fields, as under the hood, pg would create index for them too - which is useless because we are not querying this table at all from application side?

**Source-preserving request, proposal, or question:**

> Even with separate processors, the chance of duplicated rows is still there because we perform 2 inserts for UpdatedEvt \(but yes, splitting the processors reduce this chance much further\)
> 
> Within the history processor itself, this can still happen for UpdatedEvt if:
> 
> * insert old succeeds, but insert new fails → retry for the event, which will insert old again
> * insert old succeeds, insert new also succeeds, but offset commit fails → retry for the event, which will insert both again
> 
> Even for event with single insert, duplicates can happen if insert succeeds and offset commit fails.
> 
> 
> 
> If data side is able to handle the \(rare\) duplicates, I’d say we stick with no pk. I’m skeptical with the amount of fields in this composite key too.
> 
> However, if data side insists we cannot have duplicates, then as  suggested, generate a fake UUID based on the fields, and use it as pk. Let’s not add a composite key so many fields, as under the hood, pg would create index for them too - which is useless because we are not querying this table at all from application side?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Retain all insert/offset-commit windows, tolerated-duplicate branch versus deterministic fake UUID PK alternative, and objection to wide composite index.
- Related source rows 2080, 2086, 2089: History PK opinion evolves from broad composite suggestion to duplicate-tolerance or fakeUUID PK; do not flatten to mandatory wide composite key.

**Evidence:** anon-2.jsonl:2089 · comment 422620412 · PR 6740 · 2023-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

> Even with separate processors, the chance of duplicated rows is still there because we perform 2 inserts for UpdatedEvt \(but yes, splitting the processors reduce this chance much further\)
> 
> Within the history processor itself, this can still happen for UpdatedEvt if:
> 
> * insert old succeeds, but insert new fails → retry for the event, which will insert old again
> * insert old succeeds, insert new also succeeds, but offset commit fails → retry for the event, which will insert both again
> 
> Even for event with single insert, duplicates can happen if insert succeeds and offset commit fails.
> 
> ‌
> 
> If data side is able to handle the \(rare\) duplicates, I’d say we stick with no pk. I’m skeptical with the amount of fields in this composite key too.
> 
> However, if data side insists we cannot have duplicates, then as

**Evidence:** anon-2.jsonl:2089 · comment 422620412 · PR 6740 · 2023-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

> suggested, generate a fake UUID based on the fields, and use it as pk. Let’s not add a composite key so many fields, as under the hood, pg would create index for them too - which is useless because we are not querying this table at all from application side?
> 
> ‌

## A3-0267 — RecurringInvestmentScheduleJdbcEventProcessor.scala: In theory again, since we don’t actually care about this table from application side, we should just add another topic producer that re-publish all me

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Concern stated in the source:** Creating a table in PG so that BQ can ingest from PG to BQ sounds a bit extra.

**Source-preserving request, proposal, or question:**

> In theory again, since we don’t actually care about this table from application side, we should just add another topic producer that re-publish all messages again for data side to consume, and populate the table in BQ directly.
> 
> Creating a table in PG so that BQ can ingest from PG to BQ sounds a bit extra. But I suppose we might not have bandwidth to do this yet.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Direct republish-to-BQ alternative is explicitly bandwidth constrained.

**Evidence:** anon-2.jsonl:2091 · comment 422622805 · PR 6740 · 2023-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

## A3-0268 — BaseInvestmentCommunicationEventProcessor.scala: Since we are already handling cancelled evt here, I think no need to go back to common method `getBrazeCampaignIdByRegion` to handle all event types a

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/BaseInvestmentCommunicationEventProcessor.scala; PR: [EN-1556] update (Investment) update investment request canceled email event to trigger push notification

**Source-preserving request, proposal, or question:**

> Since we are already handling cancelled evt here, I think no need to go back to common method `getBrazeCampaignIdByRegion` to handle all event types again.
> 
> If we want to split sg vs hk as hk doesn’t support pn, we can just add this `sendInvestmentCancelledPn` in base, implement it for sg, and simply return Done for hk.
> 
> Same approach was suggested for the expiring recurring schedule pn

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2092 · comment 423270640 · PR 6747 · 2023-08-30

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/BaseInvestmentCommunicationEventProcessor.scala`

## A3-0292 — Producer persistence offset versus consumer message timestamp metric naming

**Source stance:** open-question

**Context:**

> lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusTopicProducersMetrics.scala; PR: Support Kafka Migration

**Source-preserving request, proposal, or question:**

> So offset on producer side is the akka persistence event offset… but on consumer side, it’s the message timestamp, not kafka consumer offset… Should we name it a bit clearer?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2117 · comment 421522471 · PR 6565 · 2023-08-23

Source path: `lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusTopicProducersMetrics.scala`

**Evidence:** anon-2.jsonl:2117 · comment 421522471 · PR 6565 · 2023-08-23

Source path: `lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusTopicProducersMetrics.scala`

**Explicit source context (hunk):**

> +    MeasurementUnit.information.bytes,
> +    new DynamicRange(
> +      1,
> +      maxMessageBytes,
> +      2
> +    )
> +  )

## A3-0293 — Kafka CreatedTime lag includes Akka persistence delay and poll interval

**Source stance:** explanation

**Context:**

> lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusTopicProducersMetrics.scala; PR: Support Kafka Migration

**Concern stated in the source:** So this means our consumer offset metrics ~= our producer offset metrics \+ akka persistence eventual consistency delay \(contributed by the akka delay config \+ akka poll interval config\)

**Source-preserving request, proposal, or question:**

> Note: by default, kafka msg timestamp \(visible to consumer in ConsumerRecord\) is CreatedTime \(as opposed to AppendTime on kafka broker side\). So this means our consumer offset metrics ~= our producer offset metrics \+ akka persistence eventual consistency delay \(contributed by the akka delay config \+ akka poll interval config\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2118 · comment 421523004 · PR 6565 · 2023-08-23

Source path: `lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusTopicProducersMetrics.scala`

**Evidence:** anon-2.jsonl:2118 · comment 421523004 · PR 6565 · 2023-08-23

Source path: `lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusTopicProducersMetrics.scala`

**Explicit source context (hunk):**

> +    MeasurementUnit.information.bytes,
> +    new DynamicRange(
> +      1,
> +      maxMessageBytes,
> +      2
> +    )
> +  )

## A3-0309 — PlanCommunicationV2EventProcessor.scala: Fallback to event timestamp instead of now?

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; PR: [EN-1990] Email/PlatformNotification for recurring setup, modify, stop

**Source-preserving request, proposal, or question:**

> Fallback to event timestamp instead of now?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2134 · comment 420900518 · PR 6686 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2134 · comment 420900518 · PR 6686 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +        goalId = event.goalId,
> +        planId = event.planId,
> +        recurringInvestmentScheduleFromEvent = event.updatedSchedule,
> +        eventTimestamp = updatedAt
> +      )
> +    } else {
> +      sendRecurringInvestmentScheduleModifiedNotification(event)

## A3-0310 — PlanCommunicationV2EventProcessor.scala: So we’re ok to fire and forget here?

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; PR: [EN-1990] Email/PlatformNotification for recurring setup, modify, stop

**Source-preserving request, proposal, or question:**

> So we’re ok to fire and forget here?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2135 · comment 420900763 · PR 6686 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2135 · comment 420900763 · PR 6686 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +
> +        val emailRequest = new EmailRequest(
> +          customerId = plan.customerId,
> +          communicationId = communicationId,
> +          requestedAt = instantNow,
> +          providerData = SendgridData(
> +            localeToTemplateId = Map(Locale.EN_HK -> "

**Evidence:** anon-2.jsonl:2135 · comment 420900763 · PR 6686 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> ", Locale.EN_SG -> "

**Evidence:** anon-2.jsonl:2135 · comment 420900763 · PR 6686 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> "),

## A3-0313 — Old replayed events missing createdAt should use event timestamp to avoid fresh communication

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; PR: [EN-1990] Email/PlatformNotification for recurring setup, modify, stop

**Source-preserving request, proposal, or question:**

> Do we still have any flow that set `createdAt` = None? Maybe let’s fallback to event timestamp if not set?
> 
> If we ever replay old events that does not have `createdAt`, we wouldn’t want to send out those communication right?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2138 · comment 421230791 · PR 6686 · 2023-08-22

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2138 · comment 421230791 · PR 6686 · 2023-08-22

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +    ele: EventEnvelope[PlanCreatedEvt]
> +  ): Future[Done] = {
> +    val plan = ele.event.plan
> +    val recurringOpt = plan.recurringInvestmentSchedule
> +    if (recurringOpt.isEmpty || plan.createdAt.isBefore(dateTimeProvider.now.minusDays(2))) {
> +      Future.successful(Done)
> +    } else {

## A3-0314 — PlanCommunicationV2EventProcessor.scala: Same here, let’s also fallback to event timestamp

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; PR: [EN-1990] Email/PlatformNotification for recurring setup, modify, stop

**Source-preserving request, proposal, or question:**

> Same here, let’s also fallback to event timestamp

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2139 · comment 421231428 · PR 6686 · 2023-08-22

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2139 · comment 421231428 · PR 6686 · 2023-08-22

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +  def planRecurringInvestmentScheduleUpdatedEvtHandler(
> +    ele: EventEnvelope[PlanRecurringInvestmentScheduleUpdatedEvt]
> +  ): Future[Done] = {
> +    val event = ele.event
> +    val updatedAt = event.updatedAt.getOrElse(EventEnvelopeUtils.extractEventTimestamp(ele).atZone(dateTimeProvider.zoneId))
> +    if (updatedAt.isBefore(dateTimeProvider.now.minusDays(2))) {
> +      Future.successful(Done)

## A3-0316 — RecurringInvestmentScheduleHistoryJdbcEventProcessor.scala: Can we just use data from event itself?

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryJdbcEventProcessor.scala; PR: [EN-1361] Create read side history table for Recurring investment schedule

**Source-preserving request, proposal, or question:**

> Can we just use data from event itself?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2141 · comment 420917234 · PR 6668 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2141 · comment 420917234 · PR 6668 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +        customerId = event.customerId,
> +        tradingAccountType = event.tradingAccountType,
> +        schedule = Some(event.updatedSchedule)
> +      )
> +    } yield ()
> +  }
> +

## A3-0319 — Schedule history created/stopped rows have no link ID: data-team join expectations

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/PlanRecurringInvestmentScheduleHistory.scala; PR: [EN-1361] Create read side history table for Recurring investment schedule

**Source-preserving request, proposal, or question:**

> Did we confirm with data team that they will know how to read this table? For same schedule, when it’s stopped/cancelled, there will be 2 rows \(one for created, and one for cancelled/stopped\) without any obvious reference id to link them \(will need to link using data fields\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2144 · comment 421206881 · PR 6668 · 2023-08-22

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/PlanRecurringInvestmentScheduleHistory.scala`

**Evidence:** anon-2.jsonl:2144 · comment 421206881 · PR 6668 · 2023-08-22

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/PlanRecurringInvestmentScheduleHistory.scala`

**Explicit source context (hunk):**

> +  investmentAmount: BigDecimal,
> +  createdAt: Option[LocalDate],
> +  recurrenceEndDetails: Option[RecurrenceEndDetails],
> +  isCancelled: Boolean,
> +  isStopped: Boolean,
> +  updatedAt: ZonedDateTime,
> +)

## A3-0321 — BrokerMccyAccountCreatorProcessor.scala: using projection makes sense, cuz it’s all internal to broker svc. No need extra hop to Kafka. Other events would be filtered out anyway so it should 

**Source stance:** suggestion

**Context:**

> broker-impl/src/main/scala/com/endowus/silver/broker/impl/entities/account/processors/BrokerMccyAccountCreatorProcessor.scala; PR: [INV-1723]: feat(broker): SG - add create mccy brokers on base broker creation via event processor handler

**Concern stated in the source:** I think using projection makes sense, cuz it’s all internal to broker svc.

**Source-preserving request, proposal, or question:**

> I think using projection makes sense, cuz it’s all internal to broker svc. No need extra hop to Kafka. Other events would be filtered out anyway so it should be fast.
> 
> We can do double release with 1st one completely empty without any handler so it can catch up as fast as possible too.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Preserve optional two-release empty-handler catch-up then handlers, justified by broker-internal events and filtering.

**Evidence:** anon-2.jsonl:2146 · comment 415661836 · PR 6580 · 2023-07-31

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/entities/account/processors/BrokerMccyAccountCreatorProcessor.scala`

## A3-0323 — Three-MCCY-broker creation: partial success, retry and stale active-account readside

**Source stance:** open-question

**Context:**

> broker-impl/src/main/scala/com/endowus/silver/broker/impl/logic/service/BaseBrokerServiceLogicImpl.scala; PR: [INV-1723]: feat(broker): SG - add create mccy brokers on base broker creation via event processor handler

**Concern stated in the source:** * event processor catches exception and retries
* the flow queries active broker accounts - which might still not return 1st in the list yet due to eventual consistency
* we might invoke `CreateBrokerAccountCmd` again for 1st?

**Source-preserving request, proposal, or question:**

> Thinking out loud… say we are creating 3 mccy brokers, 1st succeeded, 2nd failed due to whatever reason
> 
> * event processor catches exception and retries
> * the flow queries active broker accounts - which might still not return 1st in the list yet due to eventual consistency
> * we might invoke `CreateBrokerAccountCmd` again for 1st? And it seems the cmd handler is not idempotent?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Keep exact three-MCCY-broker partial-success/retry/eventual-readside/non-idempotent-create scenario as an unresolved concern.

**Evidence:** anon-2.jsonl:2148 · comment 419067251 · PR 6580 · 2023-08-14

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/logic/service/BaseBrokerServiceLogicImpl.scala`

> Thinking out loud… say we are creating 3 mccy brokers, 1st succeeded, 2nd failed due to whatever reason
> 
> * event processor catches exception and retries
> * the flow queries active broker accounts - which might still not return 1st in the list yet due to eventual consistency
> * we might invoke `CreateBrokerAccountCmd` again for 1st? And it seems the cmd handler is not idempotent?
> 
> ‌

## A3-0324 — ServiceLogicImpl.scala: If topic producer also misses then we need to either republish the event, or also sync trading with rebalance. In the case I need right now, only read

**Source stance:** explanation

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: [INV-1939] feat(rebalance): Add endpoint to sync rebalance plan state to readside (due to missed events)

**Source-preserving request, proposal, or question:**

> If topic producer also misses then we need to either republish the event, or also sync trading with rebalance. In the case I need right now, only readside of rebalance is missing

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2149 · comment 421227458 · PR 6764 · 2023-08-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2149 · comment 421227458 · PR 6764 · 2023-08-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +  override def syncReadSideRebalancePlan(planId: UUID): Future[RebalancePlanDto] = {
> +    for {
> +      maybeRebalancePlan <- refProvider.getPlanRebalancerEntityRef(planId).ask(GetRebalancePlanCmd(_))
> +      result <- maybeRebalancePlan match {
> +        case Some(rebalancePlan) =>
> +          rebalancePlanJdbcRepository

## A3-0325 — TAA has four entities/two BQ copies; remove rebalance TAA entity and janitor remaining three

**Source stance:** explanation

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: [INV-1939] feat(rebalance): Add endpoint to sync rebalance plan state to readside (due to missed events)

**Source-preserving request, proposal, or question:**

> Yes. There are 4 entities having this TAA, only 2 have data in BQ. That’s why we didn’t add to the dashboard last time.
> 
> There are planned tasks to get rid of one useless entity \(TAA entity in rebalance\), and add janitor for the other 3 \(goal, rebalance, trading\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve four TAA entities, two in BQ, intended removal of rebalance TAA entity, janitors for goal/rebalance/trading.

**Evidence:** anon-2.jsonl:2150 · comment 421228601 · PR 6764 · 2023-08-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2150 · comment 421228601 · PR 6764 · 2023-08-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +  override def syncReadSideRebalancePlan(planId: UUID): Future[RebalancePlanDto] = {
> +    for {
> +      maybeRebalancePlan <- refProvider.getPlanRebalancerEntityRef(planId).ask(GetRebalancePlanCmd(_))
> +      result <- maybeRebalancePlan match {
> +        case Some(rebalancePlan) =>
> +          rebalancePlanJdbcRepository

## A3-0344 — Upstream optional fee fields remain optional for V1-to-V2 migration

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriberV2.scala; PR: [INV-1864] feat(transaction): v2 charge transaction

**Source-preserving request, proposal, or question:**

> Ok if upstream data \(redemption / withdrawal\) is optional, then we must keep these as Optional, even though we know it’s always available in charge.
> 
> We need to make sure we can migrate existing v1 model to v2 model via event processor.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2169 · comment 419070780 · PR 6671 · 2023-08-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:2169 · comment 419070780 · PR 6671 · 2023-08-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +
>  }
>  
>  object WithdrawalTopicSubscriberV2 {
> +  def buildFeeWithdrawalTransaction(
> +    customerId: UUID,
> +    tradingAccountType: TradingAccountType,

## A3-0362 — WithdrawalTopicSubscriberV2.scala: Log error and skip? There’s nothing you can do if data is wrong?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriberV2.scala; PR: [INV-1864] feat(transaction): v2 charge transaction

**Source-preserving request, proposal, or question:**

> Log error and skip? There’s nothing you can do if data is wrong?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2188 · comment 419688529 · PR 6671 · 2023-08-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:2188 · comment 419688529 · PR 6671 · 2023-08-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +            val transaction = buildFeeWithdrawalTransaction(
> +              customerId = customerId,
> +              tradingAccountType = tradingAccountType,
> +              request = request,
> +              statusDetails = statusDetails,
> +              feeChargeRequest = feeChargeDetails
> +            )

## A3-0364 — RebateDistributionTopicSubscriberV2.scala: just log error and move on right? why hard block here and get stuck on a poison msg?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebateDistributionTopicSubscriberV2.scala; PR: Feat/INV-1866 rebate v2 model

**Source-preserving request, proposal, or question:**

> just log error and move on right? why hard block here and get stuck on a poison msg?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2190 · comment 419085354 · PR 6687 · 2023-08-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebateDistributionTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:2190 · comment 419085354 · PR 6687 · 2023-08-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebateDistributionTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +                transactionStatus = TransactionStatus.DELETED,
> +                deletedAt = msg.deletedAt
> +              )
> +            )
> +            refProvider
> +              .getTransactionEntityRef(msg.rebateRequestId)
> +              .ask(UpdateTransactionCmd(_, updatedTransaction, forceUpdate = false))

## A3-0381 — Future schedule startingDate PK collision across01Aug/05Aug/15Aug updates tolerated for CKAE

**Source stance:** explanation

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodTable.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Since startingDate is in future at the point of schedule creation, it might not be unique enough
> 
> 1. 01Aug create monthly schedule on day 1, hence starting from 01Sep
> 2. 05Aug update monthly schedule to day 10, hence starting from 10Aug - row of \(1\) is now populated with endingDate = 05Aug
> 3. 15Aug update monthly schedule back to day 1, hence starting from 01Sep - we now update the row of \(1\) back to endingDate = None
> 
> 
> 
> This might be fine in context of the CKAE investigation task, but something to keep in mind. If we are fine with this \(as there won’t be any requestedDates populated for such scenario anyway\) and that we will remove this table once we are done with investigation, I guess it’s ok.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve exact 01Aug/05Aug/15Aug changing monthly day1/day10/day1 timeline; duplicate startingDate PK reuse is tolerated only for temporary CKAE investigation without requestedDates.

**Evidence:** anon-2.jsonl:2208 · comment 416495706 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodTable.scala`

> Since startingDate is in future at the point of schedule creation, it might not be unique enough
> 
> 1. 01Aug create monthly schedule on day 1, hence starting from 01Sep
> 2. 05Aug update monthly schedule to day 10, hence starting from 10Aug - row of \(1\) is now populated with endingDate = 05Aug
> 3. 15Aug update monthly schedule back to day 1, hence starting from 01Sep - we now update the row of \(1\) back to endingDate = None
> 
> ‌
> 
> This might be fine in context of the CKAE investigation task, but something to keep in mind. If we are fine with this \(as there won’t be any requestedDates populated for such scenario anyway\) and that we will remove this table once we are done with investigation, I guess it’s ok.
> 
> ‌

**Evidence:** anon-2.jsonl:2208 · comment 416495706 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodTable.scala`

**Explicit source context (hunk):**

> +  def endingDate = column[Option[LocalDate]]("ending_date")
> +  def requestedDates = column[List[LocalDate]]("requested_dates")
> +
> +  def pk = primaryKey(InvestmentScheduleActivePeriodTable.PkName, (planId, startingDate))
> +  def idxCustomerId = index(s"${InvestmentScheduleActivePeriodTable.TableName}_customer_id_idx_v${InvestmentScheduleActivePeriodTable.DbVersion}", customerId, unique = false)
> +
> +  override def * : ProvenShape[InvestmentScheduleActivePeriod] =

## A3-0388 — New updatedAt missing on old events: ele.timestamp rather than replay-now

**Source stance:** requested-change

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> updatedAt was a new field added, so old events would not have this field, so defaulting to current timestamp would mess up your data here.
> 
> Can you check if we fallback to use `ele.timestamp` instead?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2215 · comment 416497592 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2215 · comment 416497592 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +        )
> +      )
> +      .setFutureEventHandler[InvestmentPlanCreatedEvt](
> +        ele => createSchedule(UUID.fromString(ele.entityId), ele.event.investmentPlan)
> +      )
> +      .setFutureEventHandler[RecurringInvestmentScheduleRemovedEvt](
> +        ele => removeSchedule(UUID.fromString(ele.entityId), ele.event.removedAt)

## A3-0389 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Should we also handle `InvestmentPlanDeactivatedEvt`?

**Source stance:** open-question

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Should we also handle `InvestmentPlanDeactivatedEvt`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2216 · comment 416497726 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2216 · comment 416497726 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +        ele => insertRequestedDate(ele.event.planId, ele.event.request)
> +      )
> +      .build(READ_SIDE_ID, InvestmentPlanEvt.NumShards, LagomMigrator.tag(InvestmentPlanEvt.Tag), migrator, system)
> +  }
> +
> +  private def createSchedule(planId: UUID, investmentPlanFromEvt: InvestmentPlan): Future[Unit] = {
> +    for {

## A3-0390 — InvestmentScheduleActivePeriod.scala: Just a note, missing here might be caused by different issues, not just missing ack on CKAE

**Source stance:** explanation

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/models/InvestmentScheduleActivePeriod.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Concern stated in the source:** Just a note, missing here might be caused by different issues, not just missing ack on CKAE

**Source-preserving request, proposal, or question:**

> Just a note, missing here might be caused by different issues, not just missing ack on CKAE

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2217 · comment 416500109 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/models/InvestmentScheduleActivePeriod.scala`

**Evidence:** anon-2.jsonl:2217 · comment 416500109 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/models/InvestmentScheduleActivePeriod.scala`

**Explicit source context (hunk):**

> +  }
> +
> +  def deriveMissingRequestedDates(activePeriod: InvestmentScheduleActivePeriod, dateToday: LocalDate): List[LocalDate] = {
> +    deriveTransactedDates(activePeriod, dateToday).diff(activePeriod.requestedDates)
> +  }
> +}

## A3-0391 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Here we use latest data of investmentPlan, so you may see a schedule created here with an already deactivated plan. Not sure but now I’m thinking if w

**Source stance:** open-question

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Here we use latest data of investmentPlan, so you may see a schedule created here with an already deactivated plan. Not sure but now I’m thinking if we need the 3 timestamp fields at plan level at all?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2218 · comment 416500395 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2218 · comment 416500395 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +              planUpdatedAt = investmentPlanFromEvt.updatedAt,
> +              recurringAmount = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.investmentAmount).get,
> +              recurringInterval = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.interval).get,
> +              startingDate = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.startingFrom).get,
> +              endingDate = None,
> +              requestedDates = List()
> +            )

## A3-0392 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Better to check if `recurringInvestmentSchedule` exists then upsert, then recurringAmount/Interval won’t be optional

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Better to check if `recurringInvestmentSchedule` exists then upsert, then recurringAmount/Interval won’t be optional

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2219 · comment 416500485 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2219 · comment 416500485 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +    for {
> +      _ <- investmentPlanFromEvt.recurringInvestmentSchedule match {
> +        case Some(_) =>
> +          investmentScheduleActivePeriodJdbcRepository.upsert(
> +            InvestmentScheduleActivePeriod(
> +              customerId = investmentPlanFromEvt.customerId,
> +              tradingAccountType = investmentPlanFromEvt.tradingAccountType,

## A3-0393 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Same for customerId/tradingAccountType/ccy. If we can remove them and join on planId instead, then we can make this projection much faster as it doesn

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Same for customerId/tradingAccountType/ccy. If we can remove them and join on planId instead, then we can make this projection much faster as it doesn’t need to fetch entity

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2220 · comment 416500676 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2220 · comment 416500676 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +              planUpdatedAt = investmentPlanFromEvt.updatedAt,
> +              recurringAmount = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.investmentAmount).get,
> +              recurringInterval = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.interval).get,
> +              startingDate = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.startingFrom).get,
> +              endingDate = None,
> +              requestedDates = List()
> +            )

## A3-0395 — InvestmentScheduleActivePeriodJdbcRepository.scala: I see that `deActivatedAt` is at plan level, but `markDeletionByPlanId` is called when schedule is removed, nothing to do with plan deactivation

**Source stance:** observed-defect

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodJdbcRepository.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> I see that `deActivatedAt` is at plan level, but `markDeletionByPlanId` is called when schedule is removed, nothing to do with plan deactivation

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2222 · comment 416501187 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodJdbcRepository.scala`

**Evidence:** anon-2.jsonl:2222 · comment 416501187 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodJdbcRepository.scala`

**Explicit source context (hunk):**

> +      maybeActiveInvestmentSchedule <- findActiveInvestmentSchedule(planId)
> +      _ <- maybeActiveInvestmentSchedule match {
> +        case Some(investmentSchedule) => upsert(investmentSchedule.copy(endingDate = Some(deletedAt.toLocalDate)))
> +        case None =>
> +          logger.error(s"InvestmentScheduleActivePeriodJdbcRepository unable to find active planId $planId to delete")
> +          Future.successful()
> +      }

## A3-0396 — InvestmentScheduleActivePeriodTable.scala: \(3\) will override \(1\) because they have same pk - but ok, we establish it’s ok in context of CKAE

**Source stance:** explanation

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodTable.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Concern stated in the source:** \(3\) will override \(1\) because they have same pk - but ok, we establish it’s ok in context of CKAE

**Source-preserving request, proposal, or question:**

> \(3\) will override \(1\) because they have same pk - but ok, we establish it’s ok in context of CKAE

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2223 · comment 416506901 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodTable.scala`

**Evidence:** anon-2.jsonl:2223 · comment 416506901 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodTable.scala`

**Explicit source context (hunk):**

> +  def endingDate = column[Option[LocalDate]]("ending_date")
> +  def requestedDates = column[List[LocalDate]]("requested_dates")
> +
> +  def pk = primaryKey(InvestmentScheduleActivePeriodTable.PkName, (planId, startingDate))
> +  def idxCustomerId = index(s"${InvestmentScheduleActivePeriodTable.TableName}_customer_id_idx_v${InvestmentScheduleActivePeriodTable.DbVersion}", customerId, unique = false)
> +
> +  override def * : ProvenShape[InvestmentScheduleActivePeriod] =

## A3-0398 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Actually, here you should use the `recurringInvestmentSchedule` inside the investmentPlan of the event, instead of fetching latest from entity Also, i

**Source stance:** requested-change

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Actually, here you should use the `recurringInvestmentSchedule` inside the investmentPlan of the event, instead of fetching latest from entity
> 
> Also, if we store plan level fields, you still fetch from entity for every `upsertSchedule` call

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2225 · comment 416509831 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2225 · comment 416509831 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +              planUpdatedAt = investmentPlanFromEvt.updatedAt,
> +              recurringAmount = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.investmentAmount).get,
> +              recurringInterval = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.interval).get,
> +              startingDate = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.startingFrom).get,
> +              endingDate = None,
> +              requestedDates = List()
> +            )

## A3-0400 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Use `event.updatedAt` if available

**Source stance:** requested-change

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Use `event.updatedAt` if available

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2227 · comment 416513206 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2227 · comment 416513206 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +            UUID.fromString(ele.entityId),
> +            ele.event.updatedSchedule,
> +            ele.event.updatedAt.getOrElse(ZonedDateTime.ofInstant(Instant.ofEpochMilli(ele.timestamp), dateTimeProvider.zoneId))
> +        )
> +      )
> +      .setFutureEventHandler[InvestmentPlanCreatedEvt](
> +        ele => createSchedule(UUID.fromString(ele.entityId), ele.event.investmentPlan)

## A3-0401 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: the better syntax would be ``` _ <- investmentPlan.recurringInvestmentSchedule match { case Some(schedule) => repository.upsert(...) case None => Futu

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Nit: the better syntax would be
> 
> ```
> _ <- investmentPlan.recurringInvestmentSchedule match {
>   case Some(schedule) => repository.upsert(...)
>   case None => Future.successful(Done)
> }
> ```
> 
> This way you don’t need to call Option.get

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2228 · comment 416513540 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2228 · comment 416513540 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +      _ <- investmentPlanFromEvt.recurringInvestmentSchedule match {
> +        case Some(_) =>
> +          investmentScheduleActivePeriodJdbcRepository.upsert(
> +            InvestmentScheduleActivePeriod(
> +              customerId = investmentPlanFromEvt.customerId,
> +              tradingAccountType = investmentPlanFromEvt.tradingAccountType,
> +              planId = planId,

## A3-0431 — : WIP: * tested the backfill endpoint itself → works * pending: * wait for new version of readside → update query to filter * in prod it’s huge amount o

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1710] feat(amend-scripts): Add GST charge amend-scripts

**Source-preserving request, proposal, or question:**

> WIP:
> 
> * tested the backfill endpoint itself → works
> * pending:
> 
>     * wait for new version of readside → update query to filter
>     * in prod it’s huge amount of requests → slice the query / stream the result / kafka task topic?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Backfill endpoint tested; new readside/filter and production request slicing/streaming/Kafka task remain pending alternatives.

**Evidence:** anon-2.jsonl:2261 · comment 407560671 · PR 6328 · 2023-06-30

> WIP:
> 
> * tested the backfill endpoint itself → works
> * pending:
> 
>     * wait for new version of readside → update query to filter
>     * in prod it’s huge amount of requests → slice the query / stream the result / kafka task topic?
>     
> 
> ‌

## A3-0437 — ThresholdBreachJdbcEventProcessor.scala: Use cassandra projection

**Source stance:** requested-change

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/ThresholdBreachJdbcEventProcessor.scala; PR: Feat/INV-1663 migrate to readside rebalance

**Source-preserving request, proposal, or question:**

> Use cassandra projection

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2267 · comment 412993431 · PR 6482 · 2023-07-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/ThresholdBreachJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2267 · comment 412993431 · PR 6482 · 2023-07-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/ThresholdBreachJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +
> +class ThresholdBreachJdbcProjection(
> +  session: CassandraSession,
> +  dbHandler: ThresholdBreachJdbcHandler
> +)(implicit ec: ExecutionContext, system: ActorSystem) extends StrictLogging {
> +
> +  import ThresholdBreachJdbcProjection._

## A3-0438 — RebalancingProcessor.scala: This is used in two more places it seems… `ThresholdBreachReportGenerator` and `RebalancePlanProjection`. Why don’t we switch for them too?

**Source stance:** open-question

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/processors/RebalancingProcessor.scala; PR: Feat/INV-1663 migrate to readside rebalance

**Source-preserving request, proposal, or question:**

> This is used in two more places it seems… `ThresholdBreachReportGenerator` and `RebalancePlanProjection`. Why don’t we switch for them too?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2268 · comment 412994941 · PR 6482 · 2023-07-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/processors/RebalancingProcessor.scala`

**Evidence:** anon-2.jsonl:2268 · comment 412994941 · PR 6482 · 2023-07-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/processors/RebalancingProcessor.scala`

**Explicit source context (hunk):**

> class RebalancingProcessor(
>    refProvider: PersistentEntityRefProvider,
> -  rebalanceRequestRepository: RebalanceRequestRepository,
> +  rebalanceRequestRepository: RebalanceRequestJdbcRepository,
> +  //TODO @

**Evidence:** anon-2.jsonl:2268 · comment 412994941 · PR 6482 · 2023-07-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/processors/RebalancingProcessor.scala`

**Explicit source context (hunk):**

> change to jdbc after processor have catches up

## A3-0447 — Empty generated orders before/after Lagom removal: log+Done with no event preserves outcome

**Source stance:** explanation

**Context:**

> trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateMarketDataCmdHandler.scala; PR: [INV-1719] feat(charge)(trading): Fee charge leakage

**Source-preserving request, proposal, or question:**

> yeah I deliberately changed this code a bit as existing code is misleading, but effective behavior is same.
> 
> 
> 
> Existing code before Lagom removal:
> 
> * If generated order is empty, throw exception
> * Catch exception, log error and reply Done without any events
> 
> 
> 
> Existing code after Lagom removal:
> 
> * If generated order is empty, reply error
> * Catch exception is bypassed
> * Exception is caught in `PlanTraderEventProcessor#handleMarketDataRequestedEvt` , log error and return Done
> 
> 
> 
> New logic:
> 
> * If generated order is empty, log error and reply Done without any event

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Three historical branches preserve pre-removal throw/catch+Done, post-removal replyError caught in event processor, new local log+Done without event.

**Evidence:** anon-2.jsonl:2279 · comment 412644210 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateMarketDataCmdHandler.scala`

> yeah I deliberately changed this code a bit as existing code is misleading, but effective behavior is same.
> 
> ‌
> 
> Existing code before Lagom removal:
> 
> * If generated order is empty, throw exception
> * Catch exception, log error and reply Done without any events
> 
> ‌
> 
> Existing code after Lagom removal:
> 
> * If generated order is empty, reply error
> * Catch exception is bypassed
> * Exception is caught in `PlanTraderEventProcessor#handleMarketDataRequestedEvt` , log error and return Done
> 
> ‌
> 
> New logic:
> 
> * If generated order is empty, log error and reply Done without any event
> 
> ‌

**Evidence:** anon-2.jsonl:2279 · comment 412644210 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateMarketDataCmdHandler.scala`

**Explicit source context (hunk):**

> settlementConfirmedAmount = Some(reservedAmount),
>            settlementConfirmedAt = Some(currentTime)
>          )
> -        events += TradeSettlementConfirmedEvt(planProfile = profile, trade = settledTrade, forcedRepublish = None)
> -        return Effect.persist(events.toList).thenAck(cmd.replyTo)
> +        return Effect
> +          .persist[Event, State](TradeSettlementConfirmedEvt(planProfile = profile, trade = settledTrade, forcedRepublish = None))
> +          .thenAck(cmd.replyTo)
>        }
>      }
>  
> -    try {
> -      val generatedOrders = if (trade.buySell == BuySell.BUY) {
> -        if (trade.cashReservations.isEmpty) {
> -          logger.error(
> -            s"PlanTraderEntity [$enti

## A3-0453 — UpdateTradeWithManualOrdersCmdHandler.scala: I’m not changing the `UpdateMarketDataCmdHandler` side as it seems to “expect” it to happen in its info logging ``` (perhaps the events got replayed b

**Source stance:** explanation

**Context:**

> trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeWithManualOrdersCmdHandler.scala; PR: [INV-1719] feat(charge)(trading): Fee charge leakage

**Source-preserving request, proposal, or question:**

> I’m not changing the `UpdateMarketDataCmdHandler` side as it seems to “expect” it to happen in its info logging
> 
> ```
> (perhaps the events got replayed by the event processor)
> ```
> 
> ```
>     if (trade.status != TradeStatus.WAITING_FOR_MARKET_DATA) {
>       logger.info(
>         s"PlanTrader [$entityId] received the market data update for the trade [${cmd.tradeId}] but it is not in the [${TradeStatus.WAITING_FOR_MARKET_DATA}] status, it is in [${trade.status}] so ignoring it... (perhaps the events got replayed by the event processor)"
>       )
>       return Effect.ack(cmd.replyTo)
>     }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- UpdateMarketDataCmdHandler ignored non-WAITING_FOR_MARKET_DATA status before; source intentionally leaves expected replay behavior unchanged.

**Evidence:** anon-2.jsonl:2286 · comment 412688253 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeWithManualOrdersCmdHandler.scala`

> I’m not changing the `UpdateMarketDataCmdHandler` side as it seems to “expect” it to happen in its info logging
> 
> ```
> (perhaps the events got replayed by the event processor)
> ```
> 
> ```
>     if (trade.status != TradeStatus.WAITING_FOR_MARKET_DATA) {
>       logger.info(
>         s"PlanTrader [$entityId] received the market data update for the trade [${cmd.tradeId}] but it is not in the [${TradeStatus.WAITING_FOR_MARKET_DATA}] status, it is in [${trade.status}] so ignoring it... (perhaps the events got replayed by the event processor)"
>       )
>       return Effect.ack(cmd.replyTo)
>     }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2286 · comment 412688253 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeWithManualOrdersCmdHandler.scala`

**Explicit source context (hunk):**

> +    val taa = state.maybeTaa.get
> +
> +    if (trade.status != TradeStatus.WAITING_FOR_MARKET_DATA) {
> +      return Effect.replyMessage(cmd.replyTo)(s"$here - Trade [${cmd.tradeId}] is unable to handle UpdateTradeWithManualOrdersCmd as it is not in the [${TradeStatus.WAITING_FOR_MARKET_DATA}] status, it is in [${trade.status}]")
> +    }
> +
> +    tryGenerateManualOrders(profile, trade, taa, state, cmd) match {

## A3-0458 — WithdrawalTopicSubscriber.scala: Should we go to entity if not found in readside?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriber.scala; PR: [INV-1425] feat(report): Added tax details to instrumentTransactionDto and refactor accessFeeTax statement calculation

**Source-preserving request, proposal, or question:**

> Should we go to entity if not found in readside?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2291 · comment 407990288 · PR 6309 · 2023-07-03

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriber.scala`

## A3-0479 — package.scala: It’s called in projection… tmr we might go to a region that does not require tax for example.. it’s up to projection to decide…

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala; PR: Release/INV-1396 charge GST

**Source-preserving request, proposal, or question:**

> It’s called in projection… tmr we might go to a region that does not require tax for example.. it’s up to projection to decide…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2313 · comment 409187417 · PR 6378 · 2023-07-06

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala`

## A3-0507 — ChargeApplication.scala: Can we follow the naming convention to call it Projection?

**Source stance:** requested-change

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/ChargeApplication.scala; PR: Resolve INV-1688: Add new projection table with tax details.

**Source-preserving request, proposal, or question:**

> Can we follow the naming convention to call it Projection?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2343 · comment 408153486 · PR 6342 · 2023-07-03

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/ChargeApplication.scala`

**Evidence:** anon-2.jsonl:2343 · comment 408153486 · PR 6342 · 2023-07-03

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/ChargeApplication.scala`

**Explicit source context (hunk):**

> wire[FeeChargeRequestJdbcProjection].start()
>      wire[FeeChargeRequestJdbcProjectionV4].start()
> +    wire[FeeChargeRequestJdbcProjectionV5].start()
>  
>      kafkaTopic(KafkaTopicId(BaseChargeService.ChargeTopic))(wire[ChargeProjectionTopicProducer].start())
>    }

## A3-0509 — FeeChargeRequestJdbcEventProcessorV5.scala: Hmm so we also update these planProfile too. I guess it’s fine cuz this will look up latest planProfile, but still feel very expensive :sweat_smile:

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcEventProcessorV5.scala; PR: Resolve INV-1688: Add new projection table with tax details.

**Concern stated in the source:** I guess it’s fine cuz this will look up latest planProfile, but still feel very expensive :sweat_smile:

**Source-preserving request, proposal, or question:**

> Hmm so we also update these planProfile too. I guess it’s fine cuz this will look up latest planProfile, but still feel very expensive :sweat_smile:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2345 · comment 408154820 · PR 6342 · 2023-07-03

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcEventProcessorV5.scala`

## A3-0516 — Readside TAA retry proposal5s-to10s/3 retries assumes no repeated TAA-updated event

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala; PR: [INV-1303] feat(rebalance): Increase min backoff to 1.5s

**Source-preserving request, proposal, or question:**

> So this retry will wait at least minBackoff and at most maxBackoff between each attempts, for upto maxRetries.
> 
> I think we can go with
> 
> ```
>   minBackoff = 5.seconds,
>   maxBackoff = 10.seconds,
>   maxRetries = 3,
> ```
> 
> so after 2nd attempt or at most 3rd attempt, readside TAA would catch up with state TAA \(assuming we don’t have repeated TAA updated evt\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Proposed retry min5s/max10s/maxRetries3 expects readside TAA catch-up by second/third attempt only assuming no repeated TAA-updated event.
- Related source rows 2350, 2352: Retry-default concern500ms/5s/3 is followed by5s/10s/3 proposal with readside-catch-up assumption.

**Evidence:** anon-2.jsonl:2352 · comment 407029610 · PR 6313 · 2023-06-28

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2352 · comment 407029610 · PR 6313 · 2023-06-28

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Explicit source context (hunk):**

> },
> -              context = s"Trigger threshold breach check with retry for plan ID ${msg.planId}"
> +              context = s"Trigger threshold breach check with retry for plan ID ${msg.planId}",
> +              settings = DefaultFutureRetrySettings.copy(
> +                minBackoff = 5.seconds,
> +                maxBackoff = 10.seconds
> +              )

## A3-0529 — Idempotent fee projection handlers with noop-catch-up then new-flow second release

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/sg/SgFeeManagerProjection.scala; PR: [INV-1709] feat(charge): SG charge logic for GST

**Concern stated in the source:** * 1st release, just rollout the projection with noop handlers so that the projection fully catch up with all events without applying any logic
* 2nd release, add everything else to start consuming in new flow

**Source-preserving request, proposal, or question:**

> These handler method should be idempotent. On actual release, we can split into 2:
> 
> * 1st release, just rollout the projection with noop handlers so that the projection fully catch up with all events without applying any logic
> * 2nd release, add everything else to start consuming in new flow

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve idempotent-handler requirement and optional two-release noop-catch-up then new-flow handlers.

**Evidence:** anon-2.jsonl:2367 · comment 405842985 · PR 6283 · 2023-06-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/sg/SgFeeManagerProjection.scala`

> These handler method should be idempotent. On actual release, we can split into 2:
> 
> * 1st release, just rollout the projection with noop handlers so that the projection fully catch up with all events without applying any logic
> * 2nd release, add everything else to start consuming in new flow
> 
> ‌

**Evidence:** anon-2.jsonl:2367 · comment 405842985 · PR 6283 · 2023-06-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/sg/SgFeeManagerProjection.scala`

**Explicit source context (hunk):**

> +
> +  private val migrator = new CassandraMigrator(session)
> +
> +  def start(): CassandraProjectionManager[FeeManagerEvt] = {
> +    ProjectionBuilder
> +      .cassandra[FeeManagerEvt]
> +      .setEventHandler[FeeChargeDiscountAppliedEvt](ele => handleFeeChargeDiscountAppliedEvt(ele))

## A3-0530 — FeeManager.scala: integrate with your exemption logic here, and full redemption charge below

**Source stance:** requested-change

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeManager.scala; PR: [INV-1709] feat(charge): SG charge logic for GST

**Source-preserving request, proposal, or question:**

> integrate with your exemption logic here, and full redemption charge below

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2368 · comment 405843162 · PR 6283 · 2023-06-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeManager.scala`

**Evidence:** anon-2.jsonl:2368 · comment 405843162 · PR 6283 · 2023-06-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeManager.scala`

**Explicit source context (hunk):**

> +        endDate = endDate,
> +        reason = PlanFeeChargeReason.QUARTERLY_SCHEDULED_FEE_CHARGE,
> +        dailyFees = dailyFees,
> +        shouldExemptTax = None
>        )
>        refProvider.getFeeManagerEntity(planId).ask(cmd)
>      }

## A3-0531 — Tax calculation for lag spanning GST boundary: date-aware proposal explicitly deferred

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/sg/SgTaxCalculator.scala; PR: [INV-1709] feat(charge): SG charge logic for GST

**Concern stated in the source:** So that somehow we ever have a huge event lag crossing GST period, it would also work.

**Source-preserving request, proposal, or question:**

> Yeah in fact, I want to make the projection calling `calculateTaxOnDate` directly. So that somehow we ever have a huge event lag crossing GST period, it would also work.
> 
> But I want to think a bit more to make sure it’s safe to do so. Plus, the logic in `calculateTaxOnDate` is not finalized. I’ll revisit this

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Event-lag-crossing-GST-period taxDate correction is explicitly deferred pending safety and unfinished calculateTaxOnDate logic.

**Evidence:** anon-2.jsonl:2370 · comment 405917770 · PR 6283 · 2023-06-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/sg/SgTaxCalculator.scala`

**Evidence:** anon-2.jsonl:2370 · comment 405917770 · PR 6283 · 2023-06-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/sg/SgTaxCalculator.scala`

**Explicit source context (hunk):**

> +  case class TaxCalculationResult(baseAmount: BigDecimal, taxRate: BigDecimal, taxAmount: BigDecimal)
> +
> +  def calculateLatestTax(baseAmount: BigDecimal): TaxCalculationResult = {
> +    calculateTax(baseAmount, Gst8PctRate)
> +  }
> +
> +  def calculateTaxOnDate(baseAmount: BigDecimal, taxDate: LocalDate): Option[TaxCalculationResult] = {

## A3-0532 — commands.scala: Just to make sure we don’t wrongly override existing data in case the cmd is called twice, unless the force flag is set \(cuz it will be called via pr

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/commands/commands.scala; PR: [INV-1709] feat(charge): SG charge logic for GST

**Concern stated in the source:** Just to make sure we don’t wrongly override existing data in case the cmd is called twice, unless the force flag is set \(cuz it will be called via projection now\)

**Source-preserving request, proposal, or question:**

> Just to make sure we don’t wrongly override existing data in case the cmd is called twice, unless the force flag is set \(cuz it will be called via projection now\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2371 · comment 405918078 · PR 6283 · 2023-06-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/commands/commands.scala`

**Evidence:** anon-2.jsonl:2371 · comment 405918078 · PR 6283 · 2023-06-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/commands/commands.scala`

**Explicit source context (hunk):**

> finalizedFeeAmountAfterDiscount: BigDecimal,
> -    appliedDiscounts: List[AppliedDiscount]
> +    appliedDiscounts: List[AppliedDiscount],
> +    forceUpdate: Option[Boolean]
>    ) extends FeeManagerCmd
>        with ReplyType[Done]

## A3-0534 — InvestmentTransferEventProcessor.scala: We need to return Future to chain it here. Otherwise, event processor won’t wait for investOnce and `NotifyInvestmentProcessInitiatedCmd` to complete 

**Source stance:** requested-change

**Context:**

> trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferEventProcessor.scala; PR: TT-2498 Update InvestmentTransferProjection to skip RedemptionCompletedEvt if target plan is deactivated

**Concern stated in the source:** Otherwise, event processor won’t wait for investOnce and `NotifyInvestmentProcessInitiatedCmd` to complete before moving to next evt

**Source-preserving request, proposal, or question:**

> We need to return Future to chain it here. Otherwise, event processor won’t wait for investOnce and `NotifyInvestmentProcessInitiatedCmd` to complete before moving to next evt

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2374 · comment 406027382 · PR 6290 · 2023-06-23

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferEventProcessor.scala`

**Evidence:** anon-2.jsonl:2374 · comment 406027382 · PR 6290 · 2023-06-23

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferEventProcessor.scala`

**Explicit source context (hunk):**

> +      .invoke()
> +      .map(p => p.deactivatedAt.nonEmpty)
> +      .flatMap {
> +
> +        case true =>
> +          // 2023-06-23: For transfers between plans (whereby we do a redemption followed by investment), if
> +          // the target plan was deactivated before the investment request was created, log this error for manual

## A3-0571 — Only transient errors should throw in EventProcessor/TopicSubscriber to avoid stuck data errors

**Source stance:** requested-change

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala; PR: [INV-1354] feat(email):SG only, investment completed - update sendgrid payload to include investment request order details

**Concern stated in the source:** If data is wrong, this will cause the EventProcessor/TopicSubscriber to get stuck

**Source-preserving request, proposal, or question:**

> We should only throw if transient error that would go away after retry. If data is wrong, this will cause the EventProcessor/TopicSubscriber to get stuck

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2418 · comment 398531097 · PR 5978 · 2023-05-29

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

**Evidence:** anon-2.jsonl:2418 · comment 398531097 · PR 5978 · 2023-05-29

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

**Explicit source context (hunk):**

> +          confirmedPrice = order.confirmedPrice.map(price => FormatterUtils.FourDecimalPointNumberFormatter.format(price)),
> +          buySell = BuySell.BUY // Assumption that investment orders are always buy
> +        )
> +      }
> +    )
> +    view
> +  }

## A3-0592 — Investment owns pending-investment communication after broker virtual-account update

**Source stance:** suggestion

**Context:**

> broker-impl/src/main/scala/com/endowus/silver/broker/impl/entities/account/utils/EmailDataFactory.scala; PR: Feat/EN-982 migrate one time platform notification

**Source-preserving request, proposal, or question:**

> on 2nd thought, in spirit of communicationV2 in which domain svc is in charge of triggering the notification… does the below sound better to you?
> 
> * investment svc listens to `VirtualCashAccountDetailsUpdatedMsg` and perform the logic implement in this PR
> * as in, investment svc is the domain owner of pending investment requests, and it knows that it should send communication in reaction to this event from broker svc
> * this adds one more hop \(but communications are eventual consistent by design anyway\), but the domain boundary is cleaner \(broker does not need to know about communication requirement of investment\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2439 · comment 395408321 · PR 5862 · 2023-05-18

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/entities/account/utils/EmailDataFactory.scala`

> on 2nd thought, in spirit of communicationV2 in which domain svc is in charge of triggering the notification… does the below sound better to you?
> 
> * investment svc listens to `VirtualCashAccountDetailsUpdatedMsg` and perform the logic implement in this PR
> * as in, investment svc is the domain owner of pending investment requests, and it knows that it should send communication in reaction to this event from broker svc
> * this adds one more hop \(but communications are eventual consistent by design anyway\), but the domain boundary is cleaner \(broker does not need to know about communication requirement of investment\)
> 
> ‌

## A3-0597 — BrokerAccountTopicSubscriberHandlers.scala: 12 or 1? Also do you think it’s better to filter timestamp in the subscriber?

**Source stance:** open-question

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/BrokerAccountTopicSubscriberHandlers.scala; PR: Feat/EN-982 migrate one time platform notification

**Source-preserving request, proposal, or question:**

> 12 or 1? Also do you think it’s better to filter timestamp in the subscriber?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2444 · comment 398911501 · PR 5862 · 2023-05-30

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/BrokerAccountTopicSubscriberHandlers.scala`

## A3-0603 — FeeChargeRequestProjection.scala: If cash reservation fails, we will log this error and delete the fee charge request. We would have separate dashboard/admin screen to keep track of wh

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/FeeChargeRequestProjection.scala; PR: [INV-1300] feat(charge)(trading)(redemption): Cash reservation for Alts fee charge

**Source-preserving request, proposal, or question:**

> If cash reservation fails, we will log this error and delete the fee charge request. We would have separate dashboard/admin screen to keep track of which Alts plans have not been charge. I think this is sufficient.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2451 · comment 397444205 · PR 6057 · 2023-05-25

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/FeeChargeRequestProjection.scala`

## A3-0604 — Alts cash-reservation remote call in projection; Kafka request/result ideal lacks trading events

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/FeeChargeRequestProjection.scala; PR: [INV-1300] feat(charge)(trading)(redemption): Cash reservation for Alts fee charge

**Source-preserving request, proposal, or question:**

> It’s fine to have remote call in projection class \(not fine in cmd handler\)
> 
> In ideal workflow situation:
> 
> * charge to publish kafka msg `FeeCashReservationRequestedMsg`
> * trading listens to charge topic, handles that msg and reserve cash
> * trading to publish kafka msg about the cash reservation results
> 
>     * today it doesn’t publish any messages for cash reservation at all
>     * there is no event for cash reservation failure
>     
> * charge to consume these cash reservation messages, and continue to flow
> 
> 
> 
> For the scope of this ticket, I went with the approach in this PR

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Remote call in projection tolerated for scope; ideal request/result Kafka workflow cannot fully exist today because trading publishes neither reservation messages nor failure event.

**Evidence:** anon-2.jsonl:2452 · comment 397445492 · PR 6057 · 2023-05-25

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/FeeChargeRequestProjection.scala`

> It’s fine to have remote call in projection class \(not fine in cmd handler\)
> 
> In ideal workflow situation:
> 
> * charge to publish kafka msg `FeeCashReservationRequestedMsg`
> * trading listens to charge topic, handles that msg and reserve cash
> * trading to publish kafka msg about the cash reservation results
> 
>     * today it doesn’t publish any messages for cash reservation at all
>     * there is no event for cash reservation failure
>     
> * charge to consume these cash reservation messages, and continue to flow
> 
> ‌
> 
> For the scope of this ticket, I went with the approach in this PR

## A3-0617 — HkRedemptionCommunicationV2Projection.scala: This seems almost identical to SG, except for the templateId - which both can be set in same `localeToTemplateId` map as well. I guess we keep them du

**Source stance:** suggestion

**Context:**

> redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/HkRedemptionCommunicationV2Projection.scala; PR: [EN-1138] add (Redemption) add new email event in HK for redemption completed event

**Concern stated in the source:** I guess we keep them duplicated or add common code in `BaseRedemptionCommunicationV2Projection` similar to how we handle the createdEvt

**Source-preserving request, proposal, or question:**

> This seems almost identical to SG, except for the templateId - which both can be set in same `localeToTemplateId` map as well.
> 
> I guess we keep them duplicated or add common code in `BaseRedemptionCommunicationV2Projection` similar to how we handle the createdEvt

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2466 · comment 396742273 · PR 5990 · 2023-05-23

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/HkRedemptionCommunicationV2Projection.scala`

## A3-0622 — PlanTimeSeriesTopicSubscriber.scala: I can drop the cache For accountingCcy, making this subscriber aware of which ccy is a bit leaky I feel… basically, when we receive MV update from a p

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala; PR: [INV-1299] feat(charge): Support Atls Fee charge calculation & trigger

**Source-preserving request, proposal, or question:**

> I can drop the cache
> 
> For accountingCcy, making this subscriber aware of which ccy is a bit leaky I feel… basically, when we receive MV update from a plan, we need to check which feeManager/feeCalculator responsible for it, then use only the accountingCcy of that feeManager/feeCalculator. Doable but maybe not required yet, especially we would simple persist to pg and then query later?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2471 · comment 394471811 · PR 5977 · 2023-05-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2471 · comment 394471811 · PR 5977 · 2023-05-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala`

**Explicit source context (hunk):**

> } else {
>        val ccy = mvs.head.ccy
> -      mvs.find(_.ccy != ccy).map(_ => false).getOrElse(ccy == planCcy || ccy == accountingCcy)
> +      mvs.find(_.ccy != ccy).map(_ => false).getOrElse(ccy == planCcy || accountingCurrencies.contains(ccy))
>      }
>    }

## A3-0624 — PlanTimeSeriesTopicSubscriber.scala: Oh this cache is just to store the goalType by goalId - so that we avoid constantly looking up from DB or entity when we have MV updates. I think it’s

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala; PR: [INV-1299] feat(charge): Support Atls Fee charge calculation & trigger

**Concern stated in the source:** Oh this cache is just to store the goalType by goalId - so that we avoid constantly looking up from DB or entity when we have MV updates.

**Source-preserving request, proposal, or question:**

> Oh this cache is just to store the goalType by goalId - so that we avoid constantly looking up from DB or entity when we have MV updates. I think it’s ok to leave it for now.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2473 · comment 394723865 · PR 5977 · 2023-05-16

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2473 · comment 394723865 · PR 5977 · 2023-05-16

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala`

**Explicit source context (hunk):**

> } else {
>        val ccy = mvs.head.ccy
> -      mvs.find(_.ccy != ccy).map(_ => false).getOrElse(ccy == planCcy || ccy == accountingCcy)
> +      mvs.find(_.ccy != ccy).map(_ => false).getOrElse(ccy == planCcy || accountingCurrencies.contains(ccy))
>      }
>    }

## A3-0639 — JdbcSchema.scala: We can’t drop until data team has moved

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/JdbcSchema.scala; PR: [INV-1438] feat(transaction): Listen to trading messages for asset_transfer

**Source-preserving request, proposal, or question:**

> We can’t drop until data team has moved

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2488 · comment 391965345 · PR 5918 · 2023-05-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/JdbcSchema.scala`

## A3-0654 — ContractNoteNotificationManagerHK.scala: Ok this doesn’t look right. Contract note notification should be per order. So one `RebalanceRequestOrderSettlementAssumedMsg` should yield exactly 1 

**Source stance:** observed-defect

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/managers/ContractNoteNotificationManagerHK.scala; PR: [INV-1307] feat(transaction): Platform notification for order contract date

**Source-preserving request, proposal, or question:**

> Ok this doesn’t look right. Contract note notification should be per order. So one `RebalanceRequestOrderSettlementAssumedMsg` should yield exactly 1 notification

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2504 · comment 386712621 · PR 5709 · 2023-04-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/managers/ContractNoteNotificationManagerHK.scala`

> Ok this doesn’t look right. Contract note notification should be per order. So one `RebalanceRequestOrderSettlementAssumedMsg` should yield exactly 1 notification
> 
> ‌

## A3-0655 — ContractNoteNotificationManagerHK.scala: And if we just need 1 order, I think we can drop the instrument cache and just query instrumentSvc directly

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/managers/ContractNoteNotificationManagerHK.scala; PR: [INV-1307] feat(transaction): Platform notification for order contract date

**Source-preserving request, proposal, or question:**

> And if we just need 1 order, I think we can drop the instrument cache and just query instrumentSvc directly

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2505 · comment 386712755 · PR 5709 · 2023-04-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/managers/ContractNoteNotificationManagerHK.scala`

## A3-0656 — ContractNoteNotificationManagerHK.scala: If we throw on this corrupted msg, the subscriber will be stuck

**Source stance:** observed-defect

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/managers/ContractNoteNotificationManagerHK.scala; PR: [INV-1307] feat(transaction): Platform notification for order contract date

**Concern stated in the source:** If we throw on this corrupted msg, the subscriber will be stuck

**Source-preserving request, proposal, or question:**

> If we throw on this corrupted msg, the subscriber will be stuck

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2506 · comment 387256453 · PR 5709 · 2023-04-17

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/managers/ContractNoteNotificationManagerHK.scala`

## A3-0706 — Missing PlanSubscriber: inactive fine, active requires manual investigation/add-back

**Source stance:** explanation

**Context:**

> amend-scripts/src/main/scala/rebalance/PreRpcValidation.scala; PR: [INV-1432] feat(amend-scripts): Pre-RPC data consistency validation

**Source-preserving request, proposal, or question:**

> PlanSubscriber in rebalance keeps track of the planIds subscribing to a portfolioId \+ effectiveDate. This is how we trigger RPC for existing plans. If missing \+ deactivated, all good. If missing \+ active, figure why? If intentional, we should fix whatever required and add it back. Else, just add it back. Either way it needs manual investigation.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Missing subscriber+deactivated is fine; missing+active requires manual investigation and repair/add-back. Keep portfolioId+effectiveDate subscription meaning.

**Evidence:** anon-2.jsonl:2557 · comment 387563551 · PR 5762 · 2023-04-18

Source path: `amend-scripts/src/main/scala/rebalance/PreRpcValidation.scala`

**Evidence:** anon-2.jsonl:2557 · comment 387563551 · PR 5762 · 2023-04-18

Source path: `amend-scripts/src/main/scala/rebalance/PreRpcValidation.scala`

**Explicit source context (hunk):**

> +    planProfile: PlanProfileValidationData
> +  ): Future[PlanProfileInconsistencyActionItem] = {
> +    val obsoletePlanSubscriber = planProfile.symptoms match {
> +      case List(MissingSubscriberInRebalanceSvc) => false
> +      case List(MissingInGoalSvc, MissingInRebalanceSvc, MissingInTradingSvc) => true
> +    }
> +

## A3-0712 — PlanTimeseriesTopicSubscriber.scala: How about ``` _ <- maybeLatestStoredMV match { case Some(latestStoredMV) if latestStoredMV.updatedAt.isAfter(msg.updatedAt) => logger.info("Skipping..

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala; PR: Feat/INV-1151 rebalance entity refactor phase 2 projections

**Source-preserving request, proposal, or question:**

> How about
> 
> ```
> _ <- maybeLatestStoredMV match {
>   case Some(latestStoredMV) if latestStoredMV.updatedAt.isAfter(msg.updatedAt) =>
>     logger.info("Skipping.....")
>     Future.successful(Done)
>   case _ =>
>     // upsert
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2564 · comment 382583244 · PR 5603 · 2023-03-30

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

> How about
> 
> ```
> _ <- maybeLatestStoredMV match {
>   case Some(latestStoredMV) if latestStoredMV.updatedAt.isAfter(msg.updatedAt) =>
>     logger.info("Skipping.....")
>     Future.successful(Done)
>   case _ =>
>     // upsert
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2564 · comment 382583244 · PR 5603 · 2023-03-30

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Explicit source context (hunk):**

> +        ) {
> +          for {
> +            rebalancePlan <- logger.logTime(s"Loading rebalance plan entity for planId ${msg.planId}") {
> +              refProvider.getPlanRebalancerEntityRef(msg.planId).ask(GetRebalancePlanCmd(_))
> +            }
> +            _ <- if (rebalancePlan.isEmpty) {
> +              logger.error(s"${UpdateMarketValueCmd.getClass.getName} is skipped for planId [${msg.planId}] because rebalancePlan is empty")

## A3-0715 — ServiceLogicImpl.scala: it is added as part of FHC. Once we rewrite the logic, I think we should separate the concerns: 1. update the MV projection always 2. afterwards, chec

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: Feat/INV-1151 rebalance entity refactor phase 2 projections

**Source-preserving request, proposal, or question:**

> Yeah it is added as part of FHC. Once we rewrite the logic, I think we should separate the concerns:
> 
> 1. update the MV projection always
> 2. afterwards, check if eligible for auto-rebalance, if yes, check if threshold breaches, if yes, trigger cmd to attempt

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2567 · comment 382943984 · PR 5603 · 2023-03-31

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

> Yeah it is added as part of FHC. Once we rewrite the logic, I think we should separate the concerns:
> 
> 1. update the MV projection always
> 2. afterwards, check if eligible for auto-rebalance, if yes, check if threshold breaches, if yes, trigger cmd to attempt 
> 
> ‌

**Evidence:** anon-2.jsonl:2567 · comment 382943984 · PR 5603 · 2023-03-31

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +          for {
> +            maybeLatestStoredMV <- planMarketValueProjectionRepository.queryMarketValueByPlan(planId = planId)
> +
> +            _ <- maybeLatestStoredMV match {
> +              case Some(storedLatestMV) if storedLatestMV.updatedAt.isAfter(updatedAt) =>
> +                logger.info(s"Skipping upserting value due to stale message, stored timestamp ${storedLatestMV.updatedAt} vs incoming timestamp ${updatedAt}")
> +                Future.successful(Done)

## A3-0716 — PlanTimeseriesTopicSubscriber.scala: Yup, just normal upserting projection data

**Source stance:** explanation

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala; PR: Feat/INV-1151 rebalance entity refactor phase 2 projections

**Source-preserving request, proposal, or question:**

> Yup, just normal upserting projection data

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2568 · comment 382944048 · PR 5603 · 2023-03-31

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2568 · comment 382944048 · PR 5603 · 2023-03-31

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Explicit source context (hunk):**

> +        logger.logTime(
> +          s"""[DIGEST-LOG] Process market value updated message for planId ${msg.planId}
> +             |for message in flight for ${ChronoUnit.MILLIS.between(msg.updatedAt, dateTimeProvider.now)}ms
> +             |and sent at ${msg.updatedAt}""".fuse
> +        ) {
> +          for {
> +            rebalancePlan <- logger.logTime(s"Loading rebalance plan entity for planId ${msg.planId}") {

## A3-0717 — MV projection upserts every latest message before rebalance checks; same-group migration

**Source stance:** requested-change

**Context:**

> None; PR: Feat/INV-1151 rebalance entity refactor phase 2 projections

**Source-preserving request, proposal, or question:**

> FYI  , let’s revisit this PR when you’re back. Absolutely no rush to do now.
> 
>  and me discussed. Key takeaways:
> 
> 1. The goal of this PR stays the same: build MV projection from timeseries `LatestPlanMarketValueUpdatedMsg` and any manual overridden via REST api
> 2. However, we need to change a little to keep the projection concern separated from the threshold rebalance concern
> 
>     1. In same subscriber, we should handle all `LatestPlanMarketValueUpdatedMsg`, do the timestamp checks and upsert all latest MV from timeseries
>     2. We should use a new DTO, e.g. MarketValueProjectionData to capture not only the MV but also a flag indicating whether confirmedMV and assumedMV are in sync \(logic of `isValidLatestPlanMarketValueUpdatedMsg`, useful for migration logic later\)
>     3. After upsert, retain the checks on `isValidLatestPlanMarketValueUpdatedMsg` and proceed if existing logic \(which we will migrate later\)
>     4. We can use same subscriber \(same consumer group\) to help with migration later. If different consumer group, we would need to double-release, one to turn off the old subscriber with logic, follow ed by another release to include logic in new subscriber.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Preserve MV projection scope, timestamp-upsert of ALL messages, confirmed/assumed-sync flag, later rebalance checks, same-consumer-group migration versus two-release different-group rollout.

**Evidence:** anon-2.jsonl:2569 · comment 382951421 · PR 5603 · 2023-03-31

> FYI

**Evidence:** anon-2.jsonl:2569 · comment 382951421 · PR 5603 · 2023-03-31

> , let’s revisit this PR when you’re back. Absolutely no rush to do now.

**Evidence:** anon-2.jsonl:2569 · comment 382951421 · PR 5603 · 2023-03-31

> and me discussed. Key takeaways:
> 
> 1. The goal of this PR stays the same: build MV projection from timeseries `LatestPlanMarketValueUpdatedMsg` and any manual overridden via REST api
> 2. However, we need to change a little to keep the projection concern separated from the threshold rebalance concern
> 
>     1. In same subscriber, we should handle all `LatestPlanMarketValueUpdatedMsg`, do the timestamp checks and upsert all latest MV from timeseries
>     2. We should use a new DTO, e.g. MarketValueProjectionData to capture not only the MV but also a flag indicating whether confirmedMV and assumedMV are in sync \(logic of `isValidLatestPlanMarketValueUpdatedMsg`, useful for migration logic later\)
>     3. After upsert, retain the checks on `isValidLatestPlanMarketValueUpdatedMsg` and proceed if existing logic \(which we will migrate later\)
>     4. We can use same subscriber \(same consumer group\) to help with migration later. If different consumer group, we would need to double-release, one to turn off the old subscriber with logic, follow ed by another release to include logic in new subscriber.
>     
> 
> ‌

## A3-0718 — ProjectionMarketValueData.scala: we normally name `XXXProjectionData`

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/db/models/ProjectionMarketValueData.scala; PR: Feat/INV-1151 rebalance entity refactor phase 2 projections

**Source-preserving request, proposal, or question:**

> I think we normally name `XXXProjectionData`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2570 · comment 385713070 · PR 5603 · 2023-04-11

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/db/models/ProjectionMarketValueData.scala`

## A3-0740 — Rebalance cash-release timing: pending-MV double-count window until buy export

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala; PR: [INV-1191] feat(compliance): HK Earmark logic for Rebalance flow

**Source-preserving request, proposal, or question:**

> Since we do not have updates from `timeseries` yet, we can rely on rebalance updates itself. `timeseries` would already capture the pending order as soon as they are generated, however we only release when the buy trade is exported.
> 
> This is the double counting window. If timeseries lags too long behind, we might release before the pending amount is captured. Until we have updates from timeseries, exported event is practical enough \(somewhat safe since there are decent hours between order generation and trade export, and not days like settlement assumed/confirmed\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve order-generation-to-export double-count window, stale-timeseries early-release risk, and pragmatic export-event fallback while timeseries messages absent.

**Evidence:** anon-2.jsonl:2592 · comment 380318979 · PR 5530 · 2023-03-22

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala`

> Since we do not have updates from `timeseries` yet, we can rely on rebalance updates itself. `timeseries` would already capture the pending order as soon as they are generated, however we only release when the buy trade is exported.
> 
> This is the double counting window. If timeseries lags too long behind, we might release before the pending amount is captured. Until we have updates from timeseries, exported event is practical enough \(somewhat safe since there are decent hours between order generation and trade export, and not days like settlement assumed/confirmed\)
> 
> ‌

**Evidence:** anon-2.jsonl:2592 · comment 380318979 · PR 5530 · 2023-03-22

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala`

**Explicit source context (hunk):**

> +      // Hence, we use the order amount which is calculated using latest price available as approximation.
> +      // This amount can be further buffered if needed in future.
> +      val earmarkAmount = msg.rebalanceRequest.sellOrders.flatMap(_.orderAmount).sum
> +      createEarmark(
> +        msg.customerId,
> +        mapRebalanceBuyEarmarkId(msg.goalId, msg.planId, msg.rebalanceRequest.rebalanceRequestId),
> +        earmarkAmount,

## A3-0741 — HkRebalanceTopicSubscriber.scala: Contract note events if any should be at order level. We should not use the same message `RebalanceTradeSubmittedExternallyMsg` which is at whole trad

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala; PR: [INV-1191] feat(compliance): HK Earmark logic for Rebalance flow

**Source-preserving request, proposal, or question:**

> Contract note events if any should be at order level. We should not use the same message `RebalanceTradeSubmittedExternallyMsg` which is at whole trade level. Nevertheless, export will likely still happen at trade level. Only settlement assumed/confirmed will happen at order level

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2593 · comment 380319171 · PR 5530 · 2023-03-22

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2593 · comment 380319171 · PR 5530 · 2023-03-22

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala`

**Explicit source context (hunk):**

> +      // Hence, we use the order amount which is calculated using latest price available as approximation.
> +      // This amount can be further buffered if needed in future.
> +      val earmarkAmount = msg.rebalanceRequest.sellOrders.flatMap(_.orderAmount).sum
> +      createEarmark(
> +        msg.customerId,
> +        mapRebalanceBuyEarmarkId(msg.goalId, msg.planId, msg.rebalanceRequest.rebalanceRequestId),
> +        earmarkAmount,

## A3-0742 — HkRebalanceTopicSubscriber.scala: We might update to assumed/confirmed amount if we want to. However, the difference won’t be too huge. I don’t implement it here yet because as of toda

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala; PR: [INV-1191] feat(compliance): HK Earmark logic for Rebalance flow

**Concern stated in the source:** I don’t implement it here yet because as of today, we don’t have such messages published for rebalance flow \(I’m not sure why\).

**Source-preserving request, proposal, or question:**

> We might update to assumed/confirmed amount if we want to. However, the difference won’t be too huge. I don’t implement it here yet because as of today, we don’t have such messages published for rebalance flow \(I’m not sure why\). And it will likely will change in context of contract note requirements.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2594 · comment 380319505 · PR 5530 · 2023-03-22

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2594 · comment 380319505 · PR 5530 · 2023-03-22

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala`

**Explicit source context (hunk):**

> +
> +  def handle(message: RebalanceMsg): Future[Done] = message match {
> +    case msg: RebalanceTradeSubmittedExternallyMsg
> +        if msg.rebalanceRequest.status == RebalanceRequestStatus.SELL_TRADE_SUBMITTED_EXTERNALLY_PENDING_SETTLEMENT =>
> +      // Since we do not know exact amount to earmark until these sell orders are settled, however, it would be too late then.
> +      // Hence, we use the order amount which is calculated using latest price available as approximation.
> +      // This amount can be further buffered if needed in future.

## A3-0743 — HkRebalanceTopicSubscriber.scala: We “hope” timeseries would have increased the pending rebalance buy, not assumed MV

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala; PR: [INV-1191] feat(compliance): HK Earmark logic for Rebalance flow

**Source-preserving request, proposal, or question:**

> We “hope” timeseries would have increased the pending rebalance buy, not assumed MV

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2595 · comment 380319653 · PR 5530 · 2023-03-22

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2595 · comment 380319653 · PR 5530 · 2023-03-22

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala`

**Explicit source context (hunk):**

> +          Done
> +      }
> +
> +    case msg: RebalanceTradeSubmittedExternallyMsg if msg.rebalanceRequest.status == RebalanceRequestStatus.BUY_TRADE_SUBMITTED_EXTERNALLY_PENDING_SETTLEMENT =>
> +      releaseEarmark(msg.customerId, mapRebalanceBuyEarmarkId(msg.goalId, msg.planId, msg.rebalanceRequest.rebalanceRequestId), msg.getClass.getSimpleName)
> +    case msg: RebalanceCompletedMsg =>
> +      releaseEarmark(msg.customerId, mapRebalanceBuyEarmarkId(msg.goalId, msg.planId, msg.rebalanceRequest.rebalanceRequestId), msg.getClass.getSimpleName)

## A3-0744 — HkRebalanceTopicSubscriber.scala: the order level messages only applicable for contract notes change. For this CR flow, we care about the order level messages from timeseries. They are

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala; PR: [INV-1191] feat(compliance): HK Earmark logic for Rebalance flow

**Source-preserving request, proposal, or question:**

> I think the order level messages only applicable for contract notes change. For this CR flow, we care about the order level messages from timeseries. They are different and independent scopes, so it should be fine :thumbsup:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2596 · comment 381118975 · PR 5530 · 2023-03-24

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2596 · comment 381118975 · PR 5530 · 2023-03-24

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala`

**Explicit source context (hunk):**

> +      // Hence, we use the order amount which is calculated using latest price available as approximation.
> +      // This amount can be further buffered if needed in future.
> +      val earmarkAmount = msg.rebalanceRequest.sellOrders.flatMap(_.orderAmount).sum
> +      createEarmark(
> +        msg.customerId,
> +        mapRebalanceBuyEarmarkId(msg.goalId, msg.planId, msg.rebalanceRequest.rebalanceRequestId),
> +        earmarkAmount,

## A3-0746 — New consumer group starts latest and may miss lagged messages during rollout

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala; PR: [INV-1151] feat(rebalance): Added logging and up the timeout to 30s

**Source-preserving request, proposal, or question:**

> On the contrary, as per our current \(default\) config, it will start from latest if we subscribe with a new group. And we might miss messages if we roll out this change when there are consumer lags.
> 
> By default, we already use service name as the default groupId. Let’s just keep it like it like that?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2598 · comment 379643951 · PR 5524 · 2023-03-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2598 · comment 379643951 · PR 5524 · 2023-03-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Explicit source context (hunk):**

> -      case msg: LatestPlanMarketValueUpdatedMsg if PlanTimeseriesTopicSubscriber.isValidLatestPlanMarketValueUpdatedMsg(dateTimeProvider, msg) =>
> +  override val topic: Topic[PlanMarketValueMsg] = timeSeriesService.planMarketValueTopic
> +  override val groupId = "rebalance"
> +  override val messageHandler: PlanMarketValueMsg => Future[Unit] = {
> +    case msg: LatestPlanMarketValueUpdatedMsg if PlanTimeseriesTopicSubscriber.isValidLatestPlanMarketValueUpdatedMsg(dateTimeProvider, msg) =>
> +      logger.logTime(
> +        s"""[DIGEST-LOG] Process market value updated message for planId ${msg.planId}

## A3-0764 — TransactionFxConverter.scala: Can we change the logging to be clearer that “no fx rate found for ccypair \+ date”. Asking marketdata svc is fine, but more important is we need to f

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala; PR: Feat/INV-913 tech debt fx rates

**Concern stated in the source:** I think it’s ok error here, so that someone can check.

**Source-preserving request, proposal, or question:**

> Can we change the logging to be clearer that “no fx rate found for ccypair \+ date”. Asking marketdata svc is fine, but more important is we need to fix the projection table, if indeed its data is missing.
> 
> I think it’s ok error here, so that someone can check. Outcome is either the transaction has wonky dates or data is missing \(which we can trigger the sync with marketdata\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2617 · comment 370779668 · PR 5266 · 2023-02-17

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

## A3-0767 — Auto FX sync tradeoff: stale fallback cached for a day versus repeated missing-rate sync

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala; PR: Feat/INV-913 tech debt fx rates

**Source-preserving request, proposal, or question:**

> In case of missing date,
> 
> 1. if we call sync and put the fallback rate here, if the rate was indeed missing, and corrected after sync - we will continue to use the fallback rate for another day
> 2. if we don’t put the fallback rate, and if the rate cannot be found even if after sync call - we will keep calling sync over and over again
> 
> 
> 
> I’m not sure if we want to automatically sync without a human looking into it yet…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Fallback cached after sync may stay stale for another day; not caching can cause endless repeated sync if still absent. Automatic sync remains unresolved pending human inspection.

**Evidence:** anon-2.jsonl:2620 · comment 371373270 · PR 5266 · 2023-02-20

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

> In case of missing date,
> 
> 1. if we call sync and put the fallback rate here, if the rate was indeed missing, and corrected after sync - we will continue to use the fallback rate for another day
> 2. if we don’t put the fallback rate, and if the rate cannot be found even if after sync call - we will keep calling sync over and over again
> 
> ‌
> 
> I’m not sure if we want to automatically sync without a human looking into it yet…
> 
> ‌

**Evidence:** anon-2.jsonl:2620 · comment 371373270 · PR 5266 · 2023-02-20

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Explicit source context (hunk):**

> +  }
> +
> +  def completeAndFillFxRates(
> +    rates: Map[LocalDate, FxRateProjectionData]
> +  ): Map[LocalDate, CurrencyRate] = {
> +    if (rates.isEmpty) {
> +      throw new TransactionSvcException(

## A3-0781 — FxRateHelper.scala: Should we invalidate the cache after this sync so that we reload fresh rate?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala; PR: Feat/INV-913 tech debt fx rates

**Concern stated in the source:** Should we invalidate the cache after this sync so that we reload fresh rate?

**Source-preserving request, proposal, or question:**

> Should we invalidate the cache after this sync so that we reload fresh rate?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2636 · comment 379646566 · PR 5266 · 2023-03-20

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Evidence:** anon-2.jsonl:2636 · comment 379646566 · PR 5266 · 2023-03-20

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Explicit source context (hunk):**

> +    }
> +  }
> +
> +  def syncFxRatesWithMarketData(baseCcy: CurrencyUnit, quoteCcy: CurrencyUnit): Future[List[FxRateProjectionData]] = {
> +    for {
> +      marketDataRates <- marketDataService.getFxRates(baseCcy.toString, quoteCcy.toString).invoke()
> +      projectionData = marketDataRates.map(rate => FxRateProjectionData(

## A3-0791 — StatementMetadataForUobkhGenerationScheduler.scala: So if it runs successfully then restarts due to whatever reason within the 3hr window, we will run again?

**Source stance:** open-question

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementMetadataForUobkhGenerationScheduler.scala; PR: Feat/EN-870 sg auto generate report meta data

**Source-preserving request, proposal, or question:**

> So if it runs successfully then restarts due to whatever reason within the 3hr window, we will run again?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2646 · comment 377384654 · PR 5350 · 2023-03-13

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementMetadataForUobkhGenerationScheduler.scala`

**Evidence:** anon-2.jsonl:2646 · comment 377384654 · PR 5350 · 2023-03-13

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementMetadataForUobkhGenerationScheduler.scala`

**Explicit source context (hunk):**

> +    val startOfTheDay = TimeUtils.getStartOfTheDay(today, dateTimeProvider.zoneId)
> +    val startTimingInclusive = startOfTheDay.plusHours(16).plusMinutes(0)
> +    val endTimingExclusive = startOfTheDay.plusHours(19).plusMinutes(0)
> +    val shouldRun = computeShouldRun(
> +      windowStartTimingInclusive = startTimingInclusive,
> +      windowEndTimingExclusive = endTimingExclusive,
> +    )

## A3-0819 — RedemptionCommunicationV2EventProcessor.scala: In investment svc, it seems we added Base event processor for anything common. And hk/sg for region specific communication

**Source stance:** explanation

**Context:**

> redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/RedemptionCommunicationV2EventProcessor.scala; PR: [EN-1081] feat(redemption)(communication) migrate redemption completed email to v2

**Source-preserving request, proposal, or question:**

> In investment svc, it seems we added Base event processor for anything common. And hk/sg for region specific communication

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2675 · comment 374983170 · PR 5399 · 2023-03-06

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/RedemptionCommunicationV2EventProcessor.scala`

## A3-0820 — RedemptionCommunicationV2EventProcessor.scala: I suppose each region can has its own `*CommunicationV2Projection/EventProcessor`… so that the context is clear when one looks at the class. If there 

**Source stance:** suggestion

**Context:**

> redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/RedemptionCommunicationV2EventProcessor.scala; PR: [EN-1081] feat(redemption)(communication) migrate redemption completed email to v2

**Concern stated in the source:** I suppose each region can has its own `*CommunicationV2Projection/EventProcessor`… so that the context is clear when one looks at the class.

**Source-preserving request, proposal, or question:**

> I suppose each region can has its own `*CommunicationV2Projection/EventProcessor`… so that the context is clear when one looks at the class.
> 
> If there are good amount of common code for reuse, you can extract into a trait that both extends, or a helper that injected to both.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2676 · comment 375307382 · PR 5399 · 2023-03-07

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/RedemptionCommunicationV2EventProcessor.scala`

## A3-0822 — Recurring failure email: actual reason, event-domain coupling and direct-publish deferral

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/communication/hk/HkRecurringInvestmentFailureEmailComposer.scala; PR: Resolve INV-1135: Send email for failed recurring investments with state change info

**Concern stated in the source:** And if we add all applicable compliance block reasons \(so that we can evolve the email logic freely\), we would also bake the compliance domain to investment event domain.

* Since it might fail, we should retry, and add support to retry manually via endpoint, if needed
* You can add all the failure reasons here, but no need to think too hard, cuz it’s all on the fly - nothing is persisted
* If it gets too slow and starts impacting the main triggering flow, we can revisit moving to event processor \(or postpone further by dispatching to another kafka topic, and construct the email and publish to communication from there\)

**Source-preserving request, proposal, or question:**

> Yeah simulation only makes sense if we want to warn user about potential failure in the upcoming-recurring-investment email. For this jira, we want to include exactly the failure reason. This means the entry point to construct the email should already contain the failure reason, passed from the `RecurringInvestmentProcessor`.
> 
> 
> 
> This can be achieved via Cmd\+Evt like what you did here. However, I feel we might couple our event domain with the copy \(suitability VS risk breach\), e.g today we add CrBreach as reason, tmr copy wants to distinguish between Cat1 breach vs Cat2 breach. And if we add all applicable compliance block reasons \(so that we can evolve the email logic freely\), we would also bake the compliance domain to investment event domain. Not to mention, we would likely support this to SG too - in which case, do we want to handle SG vs HK failure reason in the event?
> 
> 
> 
> The above is not necessarily wrong, but I don’t think we know everything to decide it now. And there’s a way to postpone this decision: by publishing directly to communication in the `RecurringInvestmentProcessor`
> 
> * Since it might fail, we should retry, and add support to retry manually via endpoint, if needed
> * You can add all the failure reasons here, but no need to think too hard, cuz it’s all on the fly - nothing is persisted
> * If it gets too slow and starts impacting the main triggering flow, we can revisit moving to event processor \(or postpone further by dispatching to another kafka topic, and construct the email and publish to communication from there\)
> 
> 
> 
> `RecurringInvestmentRequestFailedEvent` with proper region-specific failure reason sounds like a good thing to me, I’m just not sure we’re ready to implement it yet.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Keep upcoming-warning simulation distinct from actual failure reason. Persisted region/compliance/copy coupling is unresolved; direct publish with bounded retry/manual endpoint is a deferral option, later task topic/event flow conditional on slowness.

**Evidence:** anon-2.jsonl:2679 · comment 369402726 · PR 5203 · 2023-02-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/communication/hk/HkRecurringInvestmentFailureEmailComposer.scala`

> Yeah simulation only makes sense if we want to warn user about potential failure in the upcoming-recurring-investment email. For this jira, we want to include exactly the failure reason. This means the entry point to construct the email should already contain the failure reason, passed from the `RecurringInvestmentProcessor`.
> 
> ‌
> 
> This can be achieved via Cmd\+Evt like what you did here. However, I feel we might couple our event domain with the copy \(suitability VS risk breach\), e.g today we add CrBreach as reason, tmr copy wants to distinguish between Cat1 breach vs Cat2 breach. And if we add all applicable compliance block reasons \(so that we can evolve the email logic freely\), we would also bake the compliance domain to investment event domain. Not to mention, we would likely support this to SG too - in which case, do we want to handle SG vs HK failure reason in the event?
> 
> ‌
> 
> The above is not necessarily wrong, but I don’t think we know everything to decide it now. And there’s a way to postpone this decision: by publishing directly to communication in the `RecurringInvestmentProcessor`
> 
> * Since it might fail, we should retry, and add support to retry manually via endpoint, if needed
> * You can add all the failure reasons here, but no need to think too hard, cuz it’s all on the fly - nothing is persisted
> * If it gets too slow and starts impacting the main triggering flow, we can revisit moving to event processor \(or postpone further by dispatching to another kafka topic, and construct the email and publish to communication from there\)
> 
> ‌
> 
> `RecurringInvestmentRequestFailedEvent` with proper region-specific failure reason sounds like a good thing to me, I’m just not sure we’re ready to implement it yet. 
> 
> ‌

## A3-0836 — : I guess this one we will add a sync to update existing plans?

**Source stance:** open-question

**Context:**

> None; PR: fix(goal): INV-1248 save dividend distribution preference to DB

**Source-preserving request, proposal, or question:**

> I guess this one we will add a sync to update existing plans?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2694 · comment 374537418 · PR 5410 · 2023-03-03

## A3-0863 — SgServiceLogicImpl.scala: Why don’t we read from entity here?

**Source stance:** open-question

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala; PR: [SILVER-14633] feat(charge): Refactor sync with redemption to account states

**Source-preserving request, proposal, or question:**

> Why don’t we read from entity here?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2721 · comment 371632173 · PR 5309 · 2023-02-21

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala`

## A3-0864 — SgServiceLogicImpl.scala: Ah this is just to compare between charge entity and charge readside? I think we can skip this, cuz we will anyhow fetch from entity and write again -

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala; PR: [SILVER-14633] feat(charge): Refactor sync with redemption to account states

**Concern stated in the source:** I think we can skip this, cuz we will anyhow fetch from entity and write again - which should upsert in readside

**Source-preserving request, proposal, or question:**

> Ah this is just to compare between charge entity and charge readside? I think we can skip this, cuz we will anyhow fetch from entity and write again - which should upsert in readside

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2722 · comment 371634458 · PR 5309 · 2023-02-21

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala`

## A3-0867 — SgServiceLogicImpl.scala: Ok I see same wrong logging in subscriber too :grimacing:

**Source stance:** observed-defect

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala; PR: [SILVER-14633] feat(charge): Refactor sync with redemption to account states

**Source-preserving request, proposal, or question:**

> Ok I see same wrong logging in subscriber too :grimacing:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2725 · comment 371643701 · PR 5309 · 2023-02-21

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2725 · comment 371643701 · PR 5309 · 2023-02-21

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +      } else {
> +        logger.info(s"will run sync complete redemption charge with planId $planId and redemption request id ${redemptionDto.redemptionRequestId}")
> +        Future.successful(Done)
> +      }
> +    }
> +
> +    def handleDeletedRedemptionChargeDiscrepancy(planId: UUID, redemptionDto: RedemptionRequestDto, forceSync: Boolean) = {

## A3-0882 — FxRatesTopicSubscriberV2.scala: We are writing to DB only, so I think we can just dump as in \(stay true to projection\). I think we have this logic last time because it was via enti

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala; PR: Feat/INV-913 fx rates projection

**Concern stated in the source:** I think we have this logic last time because it was via entity, we don’t want to spam events.

**Source-preserving request, proposal, or question:**

> We are writing to DB only, so I think we can just dump as in \(stay true to projection\). I think we have this logic last time because it was via entity, we don’t want to spam events.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2741 · comment 354168870 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:2741 · comment 354168870 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +    .fxRatesMarketDataTopic
> +    .subscribe
> +    .withGroupId(FxRatesProjection)
> +    .atLeastOnce(Flow[FxRatesMsg].mapAsync(parallelism = 1) {
> +
> +    case msg: FxRateUpdatedMsg =>
> +      fxRatesProjectionJdbcDbHandler.upsert(FxRateProjectionData(

## A3-0883 — FxRatesTopicSubscriberV2.scala: This the upsert call fails, the whole future will still error, and the subscriber will retry. The `.map(_ => Done)` purely means “we are ignoring the 

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala; PR: Feat/INV-913 fx rates projection

**Source-preserving request, proposal, or question:**

> This the upsert call fails, the whole future will still error, and the subscriber will retry. The `.map(_ => Done)` purely means “we are ignoring the result of the upsert, if it succeeds”

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2742 · comment 354168987 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala`

> This the upsert call fails, the whole future will still error, and the subscriber will retry. The `.map(_ => Done)` purely means “we are ignoring the result of the upsert, if it succeeds”
> 
> ‌

**Evidence:** anon-2.jsonl:2742 · comment 354168987 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +    .atLeastOnce(Flow[FxRatesMsg].mapAsync(parallelism = 1) {
> +
> +    case msg: FxRateUpdatedMsg =>
> +      fxRatesProjectionJdbcDbHandler.upsert(FxRateProjectionData(
> +        baseCcy = msg.baseCcy, quoteCcy = msg.quoteCcy, priceDate = msg.priceDate, rate = msg.fxRate
> +      )).map(_ => Done)
> +

## A3-0886 — AdvisoryApplication.scala: Don’t we need subscriber to customer/onboarding topic to populate the `customerProjectionDataJdbcRepository`?

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Don’t we need subscriber to customer/onboarding topic to populate the `customerProjectionDataJdbcRepository`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2745 · comment 365574347 · PR 5109 · 2023-01-31

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

**Evidence:** anon-2.jsonl:2745 · comment 365574347 · PR 5109 · 2023-01-31

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

**Explicit source context (hunk):**

> +  lazy val craExpiryDailyTriggerTopicProducerDirect: CRAExpiryDailyTriggerTopicProducerDirect = wire[CRAExpiryDailyTriggerTopicProducerDirect]
> +  lazy val vcStateChangeDailyTriggerTopicProducerDirect: VCStateChangeDailyTriggerTopicProducerDirect = wire[VCStateChangeDailyTriggerTopicProducerDirect]
> +  createCustomTopics().map(_ => for {
> +    //TODO(nate) Find better way to wire this subscribers...
> +    _ <- Future.unit
> +    _ = wire[CRAExpiryDailyTriggerTopicSubscriber]
> +    _ = wire[VCStateChangeDailyTriggerTopicSubscriber]

## A3-0891 — Macwire inside Future sometimes misses subscribers; possible SlickReadside relation unproven

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala; PR: Feat/INV-969 auto change VC

**Concern stated in the source:** 's testing shows that using just the above sometimes will not wire the subscribers correctly \(and now I’m wondering if the jdbc event processors using SlickReadside getting “stuck” related to this - they also follow similar pattern, i.e.

**Source-preserving request, proposal, or question:**

> Ok this looks weird, but I also don’t know why it doesn’t work with just
> 
> ```
> createCustomTopics().map(_ => {
>    wire[A]
>    wire[B]
> })
> ```
> 
>   
>  do you have any idea? 's testing shows that using just the above sometimes will not wire the subscribers correctly \(and now I’m wondering if the jdbc event processors using SlickReadside getting “stuck” related to this - they also follow similar pattern, i.e. run something first, then wire\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Intermittent macwire-in-Future initialization issue is unresolved; possible SlickReadside relation is speculation, not verified cause.

**Evidence:** anon-2.jsonl:2750 · comment 366320053 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

> Ok this looks weird, but I also don’t know why it doesn’t work with just
> 
> ```
> createCustomTopics().map(_ => {
>    wire[A]
>    wire[B]
> })
> ```

**Evidence:** anon-2.jsonl:2750 · comment 366320053 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

> do you have any idea?

**Evidence:** anon-2.jsonl:2750 · comment 366320053 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

> 's testing shows that using just the above sometimes will not wire the subscribers correctly \(and now I’m wondering if the jdbc event processors using SlickReadside getting “stuck” related to this - they also follow similar pattern, i.e. run something first, then wire\)

**Evidence:** anon-2.jsonl:2750 · comment 366320053 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

**Explicit source context (hunk):**

> +
> +  lazy val craExpiryDailyTriggerTopicProducerDirect: CRAExpiryDailyTriggerTopicProducerDirect = wire[CRAExpiryDailyTriggerTopicProducerDirect]
> +  lazy val vcStateChangeDailyTriggerTopicProducerDirect: VCStateChangeDailyTriggerTopicProducerDirect = wire[VCStateChangeDailyTriggerTopicProducerDirect]
> +  createCustomTopics().map(_ => for {
> +    //TODO(nate) Find better way to wire this subscribers...
> +    _ <- Future.unit
> +    _ = wire[CRAExpiryDailyTriggerTopicSubscriber]

## A3-0892 — Customer onboarding/projection assumptions behind expected advisory-profile existence

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Correct me if I misunderstand here… so we rely on the assumption that:
> 
> 1. customer must submit CRA during onboarding
> 2. customer must complete onboarding, in order to have data reflected in Customer entity
> 3. projection table only capture data from Customer entity
> 
> And hence, if data is returned from customer projection table, we expect advisory profile to exist?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2751 · comment 366320408 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

> Correct me if I misunderstand here… so we rely on the assumption that:
> 
> 1. customer must submit CRA during onboarding
> 2. customer must complete onboarding, in order to have data reflected in Customer entity
> 3. projection table only capture data from Customer entity
> 
> And hence, if data is returned from customer projection table, we expect advisory profile to exist?
> 
> ‌

**Evidence:** anon-2.jsonl:2751 · comment 366320408 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +        case (totalCustomers, _) =>
> +        totalCustomers + 1
> +      }
> +      .map { totalCustomers =>
> +        logger.info(
> +          s"""
> +             |[DIGEST-LOG] Ran VC re-assessment for execute date $executeDate,

## A3-0893 — Near-cutoff onboarding CRA without completion may cross VC age outside customer projection

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Since customer projection table don’t contain data for onboarding-in-progress customers, what about this scenario:
> 
> * customer is near VC cutoff age
> * customer submits CRA during onboarding, but never completes it
> * customer now crosses cutoff age, and their CRA should change to VC

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2752 · comment 366320585 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

> Since customer projection table don’t contain data for onboarding-in-progress customers, what about this scenario:
> 
> * customer is near VC cutoff age
> * customer submits CRA during onboarding, but never completes it
> * customer now crosses cutoff age, and their CRA should change to VC
> 
> ‌

**Evidence:** anon-2.jsonl:2752 · comment 366320585 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +        case (totalCustomers, _) =>
> +        totalCustomers + 1
> +      }
> +      .map { totalCustomers =>
> +        logger.info(
> +          s"""
> +             |[DIGEST-LOG] Ran VC re-assessment for execute date $executeDate,

## A3-0894 — CustomerProjectionDataJdbcRepository.scala: If this gets expensive, we should consider adding another readside table for advisory profile containing only the latest entry

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/customer/CustomerProjectionDataJdbcRepository.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> If this gets expensive, we should consider adding another readside table for advisory profile containing only the latest entry

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2753 · comment 366320781 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/customer/CustomerProjectionDataJdbcRepository.scala`

**Evidence:** anon-2.jsonl:2753 · comment 366320781 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/customer/CustomerProjectionDataJdbcRepository.scala`

**Explicit source context (hunk):**

> +  def findNonVCWithMaybeAdvisoryProfile(bornUpTo: LocalDate): Source[(CustomerProjectionData, Option[CustomerAdvisoryProfileData]), NotUsed] = {
> +    Slick.source(
> +      customerData
> +        .joinLeft(customerAdvisorProfiles)
> +        .on((customerData, customerAdvisoryProfile) => {
> +          customerData.customerId === customerAdvisoryProfile.customerId
> +        })

## A3-0895 — CustomerAdvisoryProfileJdbcRepository.scala: Hmm alright, maybe another readside table containing only latest is worth it :grimacing:

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileJdbcRepository.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Hmm alright, maybe another readside table containing only latest is worth it :grimacing:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2754 · comment 366321122 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileJdbcRepository.scala`

## A3-0896 — CustomerAdvisoryProfileJdbcRepository.scala: And in that new table, we can consider extract this field as an optional column, to make query simpler

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileJdbcRepository.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> And in that new table, we can consider extract this field as an optional column, to make query simpler

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2755 · comment 366321253 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileJdbcRepository.scala`

## A3-0902 — CustomerProjectionDataJdbcRepository.scala: Also do we want to return to Optional advisory profile? NonVc suggests profile is there

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/customer/CustomerProjectionDataJdbcRepository.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Also do we want to return to Optional advisory profile? NonVc suggests profile is there

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2761 · comment 366322659 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/customer/CustomerProjectionDataJdbcRepository.scala`

**Evidence:** anon-2.jsonl:2761 · comment 366322659 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/customer/CustomerProjectionDataJdbcRepository.scala`

**Explicit source context (hunk):**

> +    )
> +  }
> +
> +  def findNonVCWithMaybeAdvisoryProfile(bornUpTo: LocalDate): Source[(CustomerProjectionData, Option[CustomerAdvisoryProfileData]), NotUsed] = {
> +    Slick.source(
> +      customerData
> +        .joinLeft(customerAdvisorProfiles)

## A3-0905 — CustomerPersonalDetailsTopicSubscriber.scala: Can we keep this TODO, maybe adjust it a little - since we still want to trigger recalculation if DOB changes… As of now, it always triggers

**Source stance:** requested-change

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/subscribers/hk/CustomerPersonalDetailsTopicSubscriber.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Can we keep this TODO, maybe adjust it a little - since we still want to trigger recalculation if DOB changes… As of now, it always triggers

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2764 · comment 366323511 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/subscribers/hk/CustomerPersonalDetailsTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2764 · comment 366323511 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/subscribers/hk/CustomerPersonalDetailsTopicSubscriber.scala`

**Explicit source context (hunk):**

> -  craManager: CraManager
> +  craManager: CraManager,
> +  customerProjectionDataJdbcDbHandler: CustomerProjectionDataJdbcDbHandler,
> +  customerProjectionDataJdbcRepository: CustomerProjectionDataJdbcRepository
>  )(implicit executionContext: ExecutionContext)
>      extends StrictLogging {

## A3-0909 — CraManager.scala: Ok customer projection table will have data from onboarding entity, just no sync endpoint… So the sync needs to check customer status somehow

**Source stance:** explanation

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Ok customer projection table will have data from onboarding entity, just no sync endpoint… So the sync needs to check customer status somehow

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2768 · comment 366325780 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Evidence:** anon-2.jsonl:2768 · comment 366325780 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +        case (totalCustomers, _) =>
> +        totalCustomers + 1
> +      }
> +      .map { totalCustomers =>
> +        logger.info(
> +          s"""
> +             |[DIGEST-LOG] Ran VC re-assessment for execute date $executeDate,

## A3-0911 — CustomerProjectionDataJdbcRepository.scala: Keep Optional because readside might lag

**Source stance:** explanation

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/customer/CustomerProjectionDataJdbcRepository.scala; PR: Feat/INV-969 auto change VC

**Concern stated in the source:** Keep Optional because readside might lag

**Source-preserving request, proposal, or question:**

> Keep Optional because readside might lag

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2770 · comment 366326507 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/customer/CustomerProjectionDataJdbcRepository.scala`

**Evidence:** anon-2.jsonl:2770 · comment 366326507 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/customer/CustomerProjectionDataJdbcRepository.scala`

**Explicit source context (hunk):**

> +    )
> +  }
> +
> +  def findNonVCWithMaybeAdvisoryProfile(bornUpTo: LocalDate): Source[(CustomerProjectionData, Option[CustomerAdvisoryProfileData]), NotUsed] = {
> +    Slick.source(
> +      customerData
> +        .joinLeft(customerAdvisorProfiles)

## A3-0915 — Missing profile readside: warn and force inclusion, while expired stays until retake

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Yep CRA Expired stays there until customer retakes.
> 
> Alright we can make this logic a little clearer to explain the rationale please? For example
> 
> ```scala
> def isCustomerProfileDueForVcReassessment(profile: CustomerAdvisoryProfileData): Boolean = {
>   val isValid = ...
>   val isNotUpdatedSinceDobThisYear = ...
>   isValid && isNotUpdatedSinceDobThisYear
> }
> 
> repository.find(...).filter { case (customer, maybeProfile) =>
>   maybeProfile.map(isCustomerProfileDueForVcReassessment)
>     .getOrElse {
>     log.warn(<warn message explaining the force inclusion since profile is missing from readside>)
>     true
>     }
> }.map(_._1)
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 2773, 2774: Initial exists-versus-forall question is followed by deliberate missing-profile warn-and-force-inclusion policy.

**Evidence:** anon-2.jsonl:2774 · comment 367134361 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

> Yep CRA Expired stays there until customer retakes.
> 
> Alright we can make this logic a little clearer to explain the rationale please? For example
> 
> ```scala
> def isCustomerProfileDueForVcReassessment(profile: CustomerAdvisoryProfileData): Boolean = {
>   val isValid = ...
>   val isNotUpdatedSinceDobThisYear = ...
>   isValid && isNotUpdatedSinceDobThisYear
> }
> 
> repository.find(...).filter { case (customer, maybeProfile) =>
>   maybeProfile.map(isCustomerProfileDueForVcReassessment)
>     .getOrElse {
>     log.warn(<warn message explaining the force inclusion since profile is missing from readside>)
>     true
>     }
> }.map(_._1)
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2774 · comment 367134361 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +        bornUpTo = executeDate.minusYears(minCutoffAge)
> +      )
> +      .filter{ case (customer, maybeProfile) =>
> +        maybeProfile.map(isCustomerProfileDueForReassessment(customer.dateOfBirth, _))
> +          .getOrElse({
> +            logger.warn(s"Customer ID ${customer.customerId} profile is not available on read-side, read-side might be lagging")
> +            true

## A3-0919 — CraManager.scala: Hmm this will emit `ExpiryDateOverriddenEvt` which is not what happening here… I think we will need another pair of cmd/event

**Source stance:** observed-defect

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Hmm this will emit `ExpiryDateOverriddenEvt` which is not what happening here… I think we will need another pair of cmd/event

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2778 · comment 367135684 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Evidence:** anon-2.jsonl:2778 · comment 367135684 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +        case _: VulnerableCustomerProfile =>
> +          logger.warn(s"Customer $customerId is vulnerable")
> +          Future.successful(Done)
> +      }
> +    } yield Done
> +  }
> +

## A3-0920 — Stale onboarding DOB can overwrite newer customer DOB: version/timestamp TODO

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/subscribers/hk/CustomerPersonalDetailsTopicSubscriber.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Chance is low, but if somehow we have lag on onboarding svc side… we might run into situation that we write latest value of DOB from customer svc to the table, and then it got overridden with stale value from onboarding svc… Will need some version or timestamp to avoid it…
> 
> Let’s note a TODO for now

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Stale onboarding DOB can overwrite newer customer DOB; version/timestamp repair is left TODO, not implemented.

**Evidence:** anon-2.jsonl:2779 · comment 367136193 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/subscribers/hk/CustomerPersonalDetailsTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2779 · comment 367136193 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/subscribers/hk/CustomerPersonalDetailsTopicSubscriber.scala`

**Explicit source context (hunk):**

> case msg: RegionalPersonalDetailsUpdatedMsg =>
> -      recalculateVcStatus(msg.customerId, "CustomerService")
> +      handleCustomerInfoUpdated(
> +        CustomerProjectionData(
> +          customerId = msg.customerId,
> +          dateOfBirth = msg.regionalPersonalDetailsDto.genericPersonalDetailsDto.dateOfBirth,
> +          lastUpdated = msg.updatedAt.toInstant

## A3-0928 — CRA expiry override versus check: date-update event separate from expired-flag event

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> OverrideExpiryDateCmd\(customerId, expiryDate\)  
> CheckExpiryDateCmd\(customerId\)  
>   
> Entity:
> 
> * override cmd handler: emit ExpiryDateOverriddenEvt, and potentially CraExpiredEvt
> * check cmd handler: noop or CraExpiredEvt
> * ExpiryDateOverriddenEvt handler: update date
> * CraExpiredEvt handler: update flag
> 
> 
> 
> compliance: CraExpiredEvt

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Keep override command emits override+possibly expiration event while check emits noop/expiration; handlers update date versus flag separately; compliance consumes expiry event.

**Evidence:** anon-2.jsonl:2787 · comment 367146282 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

> OverrideExpiryDateCmd\(customerId, expiryDate\)  
> CheckExpiryDateCmd\(customerId\)  
>   
> Entity:
> 
> * override cmd handler: emit ExpiryDateOverriddenEvt, and potentially CraExpiredEvt
> * check cmd handler: noop or CraExpiredEvt
> * ExpiryDateOverriddenEvt handler: update date
> * CraExpiredEvt handler: update flag
> 
> ‌
> 
> compliance: CraExpiredEvt
> 
> ‌

**Evidence:** anon-2.jsonl:2787 · comment 367146282 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +        case _: VulnerableCustomerProfile =>
> +          logger.warn(s"Customer $customerId is vulnerable")
> +          Future.successful(Done)
> +      }
> +    } yield Done
> +  }
> +

## A3-0936 — SgDividendService.scala: I’m not really sure. But trading subscribes to it for old flow..

**Source stance:** explanation

**Context:**

> dividend-api/src/main/scala/com/endowus/silver/dividend/api/SgDividendService.scala; PR: [INV-1096] feat(dividend)(admin,broker,communication,investment,timeseries,trading,transaction): Region split for Dividend svc

**Source-preserving request, proposal, or question:**

> I’m not really sure. But trading subscribes to it for old flow..

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2796 · comment 366004361 · PR 5136 · 2023-02-01

Source path: `dividend-api/src/main/scala/com/endowus/silver/dividend/api/SgDividendService.scala`

**Evidence:** anon-2.jsonl:2796 · comment 366004361 · PR 5136 · 2023-02-01

Source path: `dividend-api/src/main/scala/com/endowus/silver/dividend/api/SgDividendService.scala`

**Explicit source context (hunk):**

> +object SgDividendService {
> +  val BrokerAccountDividendTopic = "dividendSvc-brokerAccountDividend-Topic-v1"
> +  val PlanDividendDistributionTopic = "dividendSvc-planDividendDistribution-Topic-v1"
> +  val PlanDividendDistributionTopicTemp = "dividendSvc-planDividendDistribution-Topic-Temp-v1"
> +}

## A3-0938 — DividendApplication.scala: The lags are tracked based on offsets only. So if offset table is not created, nothing will work…

**Source stance:** explanation

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/DividendApplication.scala; PR: [INV-1096] feat(dividend)(admin,broker,communication,investment,timeseries,trading,transaction): Region split for Dividend svc

**Source-preserving request, proposal, or question:**

> The lags are tracked based on offsets only. So if offset table is not created, nothing will work…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2798 · comment 366690569 · PR 5136 · 2023-02-03

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/DividendApplication.scala`

**Evidence:** anon-2.jsonl:2798 · comment 366690569 · PR 5136 · 2023-02-03

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/DividendApplication.scala`

**Explicit source context (hunk):**

> readSide.register(wire[BrokerAccountDividendCommunicationV2EventProcessor])
> -  readSide.register(wire[DividendCommunicationV2EventProcessor])
> +
> +  // register jdbc event processor only after offsets are created
> +  runCreateOffsetStore()
> +    .recover({
> +      case ex: AskTimeoutException =>

## A3-0940 — EmailProviderData.scala: I’m a little confused on this. Do we want to serialize `RecurringInvestmentModifiedData` directly, or via its sealed trait `SendgridTemplateData` ?

**Source stance:** open-question

**Context:**

> communication-api/src/main/scala/com/endowus/silver/communication/api/v2/email/EmailProviderData.scala; PR: [EN-448] feat(goal)(communication) publish RECURRING_INVESTMENT_MODIFIED emails for HK

**Source-preserving request, proposal, or question:**

> I’m a little confused on this. Do we want to serialize `RecurringInvestmentModifiedData` directly, or via its sealed trait `SendgridTemplateData` ?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2800 · comment 365576534 · PR 5100 · 2023-01-31

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/v2/email/EmailProviderData.scala`

**Evidence:** anon-2.jsonl:2800 · comment 365576534 · PR 5100 · 2023-01-31

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/v2/email/EmailProviderData.scala`

**Explicit source context (hunk):**

> }
>  
> +object RecurringInvestmentModifiedData {
> +  implicit val format: Format[RecurringInvestmentModifiedData] = Json.format
> +}
> +
>  /*

## A3-0982 — SgOnlyInvestmentCommunicationV2EventProcessor.scala: If we wire this for SG, then we will start sending email for 2 days worth of confirmed investment requests…

**Source stance:** explanation

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/SgOnlyInvestmentCommunicationV2EventProcessor.scala; PR: EN-120 Handle Investment Completed and Upcoming Recurring Investment emails using Comms V2

**Source-preserving request, proposal, or question:**

> If we wire this for SG, then we will start sending email for 2 days worth of confirmed investment requests…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2842 · comment 354163645 · PR 4890 · 2022-12-16

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/SgOnlyInvestmentCommunicationV2EventProcessor.scala`

## A3-0983 — Missing broker virtual-account data blocks tag and may age communication past2days

**Source stance:** open-question

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala; PR: EN-120 Handle Investment Completed and Upcoming Recurring Investment emails using Comms V2

**Source-preserving request, proposal, or question:**

> we throw if `brokerAccount` has missing data for `virtualAccountNumber`, event processor is stuck until someone fix on broker svc side? And this would delay communication for all other events in same tag, potentially beyond the `dateTimeProvider.now.minusDays(2)` ?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2843 · comment 354939478 · PR 4890 · 2022-12-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2843 · comment 354939478 · PR 4890 · 2022-12-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +                  Locale.EN_HK -> "

**Evidence:** anon-2.jsonl:2843 · comment 354939478 · PR 4890 · 2022-12-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> ",
> +                  Locale.EN_SG -> "

**Evidence:** anon-2.jsonl:2843 · comment 354939478 · PR 4890 · 2022-12-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> "
> +                ),
> +                templateData = UpcomingRecurringInvestmentData(
> +                  GOAL_NAME = goal.name,
> +                  STOCK_PERCENTAGE = ratioPercentages._1.toString,
> +                  BOND_PERCENTAGE = ratioPercentages._2.toString,

## A3-0995 — SG/HK investment communication trigger ownership and deferred SG migration

**Source stance:** suggestion

**Context:**

> None; PR: EN-613 Handle One Time Investment Created and Investment In Progress emails using Comms V2

**Source-preserving request, proposal, or question:**

> As chatted offline
> 
> In Singapore, we need email to trigger from:
> 
> 1. investment \(this PR\)
> 2. broker: on some virtual account msg → query customer’s investment requests → trigger email
> 
> In the meantime, let’s keep SG as in. In HK, we implement \(1\) in this PR, following v2 convention.
> 
> For \(2\), in HK, if needed, the flow should be:
> 
> * broker svc publishes the virtual account msg
> * investment svc subscribes to broker topic, handle that message → query customer’s investment requests → trigger email
> 
> This way, we can reuse code \+ keep communication svc free of domain logic. SG can be ported to follow v2 approach in near future

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Preserve currentSG dual-trigger flow and HK investment-owned communication via broker-message subscription; SG migration is deferred.

**Evidence:** anon-2.jsonl:2856 · comment 353920697 · PR 4891 · 2022-12-15

## A3-1000 — CustomerAdvisoryProfileTopicSubscriber.scala: we can remove this groupId now, since we will use only 1 group. Otherwise maybe rename it

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/CustomerAdvisoryProfileTopicSubscriber.scala; PR: Feat/INV-891 cancel investment pi to retail

**Concern stated in the source:** Otherwise maybe rename it

**Source-preserving request, proposal, or question:**

> Maybe we can remove this groupId now, since we will use only 1 group. Otherwise maybe rename it

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2861 · comment 353198866 · PR 4867 · 2022-12-13

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/CustomerAdvisoryProfileTopicSubscriber.scala`

## A3-1001 — HkCustomerTopicSubscriber.scala: If you want to name the group, at least put `compliance` in there so we can tell easily which service is the subscriber

**Source stance:** requested-change

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkCustomerTopicSubscriber.scala; PR: Feat/INV-891 cancel investment pi to retail

**Source-preserving request, proposal, or question:**

> If you want to name the group, at least put `compliance` in there so we can tell easily which service is the subscriber

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2862 · comment 353198940 · PR 4867 · 2022-12-13

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkCustomerTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2862 · comment 353198940 · PR 4867 · 2022-12-13

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkCustomerTopicSubscriber.scala`

**Explicit source context (hunk):**

> +}
> +
> +object HkCustomerTopicSubscriber {
> +  val CustomerStateChange = "compliance-customer-state-change"
> +}

## A3-1031 — HkInvestmentTopicSubscriber.scala: We don’t have any timestamp field from `InvestmentRequestDto` ? what if this subscriber lags and we will use wrong timestamp?

**Source stance:** open-question

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkInvestmentTopicSubscriber.scala; PR: Feat/INV-676 cancel investment vc expired

**Concern stated in the source:** what if this subscriber lags and we will use wrong timestamp?

**Source-preserving request, proposal, or question:**

> We don’t have any timestamp field from `InvestmentRequestDto` ? what if this subscriber lags and we will use wrong timestamp?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2895 · comment 349397695 · PR 4789 · 2022-11-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkInvestmentTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2895 · comment 349397695 · PR 4789 · 2022-11-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkInvestmentTopicSubscriber.scala`

**Explicit source context (hunk):**

> -          upsertInvestmentRequest(msg.customerId)(msg.goalId, msg.planId, msg.request)
> +          upsertInvestmentRequest(msg.customerId)(msg.goalId, msg.planId, msg.request, msg.request.confirmedAt)
>          case _ =>
>            Future.successful(Done)
>        }
>      }

## A3-1034 — Investment projection timestamps differ by OrdersGenerated/Cancellation/ExternalSubmitted message

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkInvestmentTopicSubscriber.scala; PR: Feat/INV-676 cancel investment vc expired

**Source-preserving request, proposal, or question:**

> Let’s use:
> 
> * `InvestmentRequestOrdersGeneratedMsg`: max order’s createdAt
> * `InvestmentRequestCancellationFlowInitiatedMsg`: `initiatedAt`
> * `InvestmentRequestSubmittedExternallyMsg`: no good field here but I guess status is already not cancellable, so maybe we can max order’s createdAt for now

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Per-message timestamps retained separately: OrdersGenerated=maxcreatedAt; CancellationFlowInitiated=initiatedAt; SubmittedExternally temporary maxcreatedAt because not cancellable.

**Evidence:** anon-2.jsonl:2898 · comment 349491361 · PR 4789 · 2022-11-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkInvestmentTopicSubscriber.scala`

> Let’s use:
> 
> * `InvestmentRequestOrdersGeneratedMsg`: max order’s createdAt
> * `InvestmentRequestCancellationFlowInitiatedMsg`: `initiatedAt`
> * `InvestmentRequestSubmittedExternallyMsg`: no good field here but I guess status is already not cancellable, so maybe we can max order’s createdAt for now
> 
> ‌

**Evidence:** anon-2.jsonl:2898 · comment 349491361 · PR 4789 · 2022-11-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkInvestmentTopicSubscriber.scala`

**Explicit source context (hunk):**

> +          upsertInvestmentRequest(msg.customerId)(msg.goalId, msg.planId, msg.request, Some(msg.request.createdAt))
>          case msg: InvestmentRequestOrdersGeneratedMsg =>
> -          upsertInvestmentRequest(msg.customerId)(msg.goalId, msg.planId, msg.request)
> +          upsertInvestmentRequest(msg.customerId)(msg.goalId, msg.planId, msg.request, Some(msg.request.orders
> +            .map(_.createdAt)
> +            .maxBy(_.toInstant)
> +          ))

## A3-1036 — HkInvestmentTopicSubscriber.scala: Use max order’s createdAt?

**Source stance:** open-question

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkInvestmentTopicSubscriber.scala; PR: Feat/INV-676 cancel investment vc expired

**Source-preserving request, proposal, or question:**

> Use max order’s createdAt?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2900 · comment 349786025 · PR 4789 · 2022-11-30

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkInvestmentTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2900 · comment 349786025 · PR 4789 · 2022-11-30

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkInvestmentTopicSubscriber.scala`

**Explicit source context (hunk):**

> -          upsertInvestmentRequest(msg.customerId)(msg.goalId, msg.planId, msg.request)
> +          upsertInvestmentRequest(msg.customerId)(msg.goalId, msg.planId, msg.request, Some(msg.request.orders
> +            .map(_.createdAt)
> +            .maxBy(_.toInstant)
> +          ))
>          case msg: InvestmentRequestCancellationFlowInitiatedMsg =>
> -          upsertInvestmentRequest(msg.customerId)(msg.goalId, msg.planId, msg.request)

## A3-1037 — HkInvestmentTopicSubscriber.scala: Use max order’s createdAt?

**Source stance:** open-question

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkInvestmentTopicSubscriber.scala; PR: Feat/INV-676 cancel investment vc expired

**Source-preserving request, proposal, or question:**

> Use max order’s createdAt?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2901 · comment 349786058 · PR 4789 · 2022-11-30

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkInvestmentTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2901 · comment 349786058 · PR 4789 · 2022-11-30

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkInvestmentTopicSubscriber.scala`

**Explicit source context (hunk):**

> +          upsertInvestmentRequest(msg.customerId)(msg.goalId, msg.planId, msg.request, msg.request.amendedAt)
>          case msg: InvestmentRequestSubmittedExternallyMsg =>
> -          upsertInvestmentRequest(msg.customerId)(msg.goalId, msg.planId, msg.request)
> +          //TODO Note here we are using order max createdAt as timestamp, there is submittedAt in invest but not exposed to DTO
> +          upsertInvestmentRequest(msg.customerId)(msg.goalId, msg.planId, msg.request, Some(msg.request.orders
> +            .map(_.createdAt)
> +            .maxBy(_.toInstant)

## A3-1040 — CustomerCraUpdatedLogic.scala: Ah I should have added the timestamp in the event :see_no_evil:

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/CustomerCraUpdatedLogic.scala; PR: Feat/INV-676 cancel investment vc expired

**Source-preserving request, proposal, or question:**

> Ah I should have added the timestamp in the event :see_no_evil:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2904 · comment 350429242 · PR 4789 · 2022-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/CustomerCraUpdatedLogic.scala`

**Evidence:** anon-2.jsonl:2904 · comment 350429242 · PR 4789 · 2022-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/CustomerCraUpdatedLogic.scala`

**Explicit source context (hunk):**

> +
> +  override def handleCustomerExpiryDateChange(customerId: UUID, isCraExpired: Boolean): Future[Done] = {
> +    if (isCraExpired) {
> +      cancelAllPendingInvestments(customerId, Instant.now())
> +    } else {
> +      Future.successful(Done)
> +    }

## A3-1089 — : I understand we can potentially reuse existing event processor because: * in HK, it’s brand new so we start from scratch * in SG, we don’t process old

**Source stance:** suggestion

**Context:**

> None; PR: [EN-311] feat(dividend) publish new email request for dividend

**Concern stated in the source:** I understand we can potentially reuse existing event processor because:

But on 2nd thought, I think it’s cleaner to have separate event processor, cuz it is for completely different purpose.

**Source-preserving request, proposal, or question:**

> I understand we can potentially reuse existing event processor because:
> 
> * in HK, it’s brand new so we start from scratch
> * in SG, we don’t process old events, and new events will be published to a dormant topic \(communication doesn’t subscribe to it yet\)
> 
> But on 2nd thought, I think it’s cleaner to have separate event processor, cuz it is for completely different purpose. We can potentially add some timestamp check on the message, and drop if event is too old?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Separate communication processor preferred despite technically reusableHK-new/SG-no-history-dormant-topic flow; timestamp-old-event drop remains proposal.

**Evidence:** anon-2.jsonl:2955 · comment 339564950 · PR 4506 · 2022-10-21

> I understand we can potentially reuse existing event processor because:
> 
> * in HK, it’s brand new so we start from scratch
> * in SG, we don’t process old events, and new events will be published to a dormant topic \(communication doesn’t subscribe to it yet\)
> 
> But on 2nd thought, I think it’s cleaner to have separate event processor, cuz it is for completely different purpose. We can potentially add some timestamp check on the message, and drop if event is too old?
> 
> ‌

## A3-1090 — Projection transient retryWARN versus persistent lag threshold1hr and Sentry flooding

**Source stance:** explanation

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/brokerAccount/processors/AutoSellDownDividendProcessor.scala; PR: [EN-311] feat(dividend) publish new email request for dividend

**Concern stated in the source:** Retry is successful, and no one would bother about it
* persistent: exception will keep throwing and event processor would be stuck and keep retrying.

**Source-preserving request, proposal, or question:**

> Imagine if exception happens:
> 
> * one-off: exception will be thrown normally, and event processor retries by itself. Event processor would log a WARN log I believe. Retry is successful, and no one would bother about it
> * persistent: exception will keep throwing and event processor would be stuck and keep retrying. We should set up monitoring for event processor lag \(with appropriate lag threshold, currently it’s 1hr for all\) to catch it. If we log error here, sentry will be flooded

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- One-off retry/WARN versus persistent-stuck lag monitoring (then1hr threshold); error log would flood Sentry. Preserve as scoped logging/monitoring rationale.

**Evidence:** anon-2.jsonl:2956 · comment 339565318 · PR 4506 · 2022-10-21

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/brokerAccount/processors/AutoSellDownDividendProcessor.scala`

> Imagine if exception happens:
> 
> * one-off: exception will be thrown normally, and event processor retries by itself. Event processor would log a WARN log I believe. Retry is successful, and no one would bother about it
> * persistent: exception will keep throwing and event processor would be stuck and keep retrying. We should set up monitoring for event processor lag \(with appropriate lag threshold, currently it’s 1hr for all\) to catch it. If we log error here, sentry will be flooded
> 
> ‌

## A3-1091 — DividendCommunicationV2EventProcessor.scala: It’s legit to distribute dividend with infoDate in the distant past. Why don’t we filter using createdAt field instead? Also, just to confirm, we want

**Source stance:** open-question

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/processors/DividendCommunicationV2EventProcessor.scala; PR: [EN-311] feat(dividend) publish new email request for dividend

**Concern stated in the source:** Also, just to confirm, we want to filter here so that we don’t unnecessarily reprocess old events, then spam the messages in the new kafka topic right?

**Source-preserving request, proposal, or question:**

> It’s legit to distribute dividend with infoDate in the distant past. Why don’t we filter using createdAt field instead?
> 
> Also, just to confirm, we want to filter here so that we don’t unnecessarily reprocess old events, then spam the messages in the new kafka topic right? We would need to remove this filter after this event processor has caught up with latest offset?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2957 · comment 342936192 · PR 4506 · 2022-11-04

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/processors/DividendCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2957 · comment 342936192 · PR 4506 · 2022-11-04

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/processors/DividendCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +  }
> +
> +  def handleDividendDistributedEvt(ele: EventStreamElement[DividendDistributedEvt]): Future[List[BoundStatement]] = {
> +    val event = ele.event
> +    if (event.createdAt.isAfter(dateTimeProvider.now.minusDays(7))) {
> +      val communicationIdSeed = DividendDistributionReceived + "|" + event.dividendId.toString + "|" + event.createdAt.toString
> +      val communicationId = UUID.nameUUIDFromBytes(communicationIdSeed.getBytes())

## A3-1093 — AutoSellDownDividendCommunicationV2EventProcessor.scala: AutoSellDown is a different requirement \(automatically redeem the dividend, due to plan already empty for example\) Can we name this `BrokerAccountDi

**Source stance:** requested-change

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/brokerAccount/processors/AutoSellDownDividendCommunicationV2EventProcessor.scala; PR: [EN-311] feat(dividend) publish new email request for dividend

**Source-preserving request, proposal, or question:**

> AutoSellDown is a different requirement \(automatically redeem the dividend, due to plan already empty for example\)
> 
> Can we name this `BrokerAccountDividendCommunicationV2EventProcessor`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2959 · comment 342947489 · PR 4506 · 2022-11-04

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/brokerAccount/processors/AutoSellDownDividendCommunicationV2EventProcessor.scala`

## A3-1094 — DividendCommunicationV2EventProcessor.scala: Meaning if somehow this event processor lags long enough, we don’t need to inform customer? Also do we have requirement to use infoDate too? Why can’t

**Source stance:** open-question

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/processors/DividendCommunicationV2EventProcessor.scala; PR: [EN-311] feat(dividend) publish new email request for dividend

**Source-preserving request, proposal, or question:**

> Meaning if somehow this event processor lags long enough, we don’t need to inform customer? Also do we have requirement to use infoDate too? Why can’t we use createdAt which is more relevant to processing timestamp?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2960 · comment 343448122 · PR 4506 · 2022-11-07

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/processors/DividendCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2960 · comment 343448122 · PR 4506 · 2022-11-07

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/processors/DividendCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +  }
> +
> +  def handleDividendDistributedEvt(ele: EventStreamElement[DividendDistributedEvt]): Future[List[BoundStatement]] = {
> +    val event = ele.event
> +    if (event.createdAt.isAfter(dateTimeProvider.now.minusDays(7))) {
> +      val communicationIdSeed = DividendDistributionReceived + "|" + event.dividendId.toString + "|" + event.createdAt.toString
> +      val communicationId = UUID.nameUUIDFromBytes(communicationIdSeed.getBytes())

## A3-1101 — PlanCommunicationV2EventProcessor.scala: If we throw here, the event processor will get stuck. And given we can’t practically modify event, should we just log error and move on?

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; PR: Feat/EN-312 comm v2 for redemption investment

**Concern stated in the source:** If we throw here, the event processor will get stuck.

**Source-preserving request, proposal, or question:**

> If we throw here, the event processor will get stuck. And given we can’t practically modify event, should we just log error and move on?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2968 · comment 344067505 · PR 4602 · 2022-11-09

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2968 · comment 344067505 · PR 4602 · 2022-11-09

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +        )
> +        Future.successful(List())
> +      } { previousSchedule =>
> +        val commIdSeed = "RECURRING_INVESTMENT_STOPPED" + "|" + event.planId.toString + "|" + event.removedAt.toString
> +        val communicationId = UUID.nameUUIDFromBytes(commIdSeed.getBytes)
> +
> +        for {

## A3-1120 — Ack compensation/recon alternative tolerates eventual correction unlike CR earmark

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala; PR: Feat/INV-558 CR audit

**Concern stated in the source:** But then, we still need to carefully check before applying because of concurrent requests.

And it’s ok because this only affects recurring flow, unlike earmark which will affect CR calculation.

**Source-preserving request, proposal, or question:**

> So for acks, it’s somewhat tricky to correctly reverse it unless we inspect the old events. We might potentially return the old state as part of command, so one can use it as \(manual\) compensating saga. But then, we still need to carefully check before applying because of concurrent requests.
> 
> OTOH, most of the time it’s harmless to leave the ack there. We can build recon logic for ack too, e.g. CAT1 goals with persisted CAT2 ack, goals with recurring investment with persisted recurring ack. This way, we can eventually fix the acks without building complicated workflow logic. And it’s ok because this only affects recurring flow, unlike earmark which will affect CR calculation.
> 
> I can update the logging message here a bit to indicate that we will have recon for it, instead of just purely “can ignore”.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Ack rollback needs prior events/state and concurrent-request checks; proposed reconciliation accepted as eventual alternative because recurring ack less critical than CR earmark. Preserve examples and uncertainty.

**Evidence:** anon-2.jsonl:2991 · comment 344062610 · PR 4628 · 2022-11-09

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

**Evidence:** anon-2.jsonl:2991 · comment 344062610 · PR 4628 · 2022-11-09

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

**Explicit source context (hunk):**

> } yield response
>    }
>  
>    private def doCraChecks(
>      request: TradingRestrictionRequest,
>      customerId: UUID,
> +    referenceId: UUID,

## A3-1149 — EdgeQueryTradingRestrictionLogic.scala: This one is good example to check because we use data returned from timeseries

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeQueryTradingRestrictionLogic.scala; PR: [INV-669] State change impacted plans

**Concern stated in the source:** This one is good example to check because we use data returned from timeseries

**Source-preserving request, proposal, or question:**

> This one is good example to check because we use data returned from timeseries

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:3020 · comment 343434601 · PR 4577 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeQueryTradingRestrictionLogic.scala`

## A3-1156 — : Will do the following in separate PR: * scheduling to trigger recon endpoint * Slack integration * add timestamp to BuyEarmark to help reduce prematur

**Source stance:** explanation

**Context:**

> None; PR: Feat/INV-557 buy earmark recon

**Source-preserving request, proposal, or question:**

> Will do the following in separate PR:
> 
> * scheduling to trigger recon endpoint
> * Slack integration
> * add timestamp to BuyEarmark to help reduce premature alert

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:3028 · comment 342571900 · PR 4597 · 2022-11-03

> Will do the following in separate PR:
> 
> * scheduling to trigger recon endpoint
> * Slack integration
> * add timestamp to BuyEarmark to help reduce premature alert
> 
> ‌

## A3-1161 — DocumentTopicSubscriber.scala: So the only thing we need from document service is this documentId? Should report service just publish to communicate in `StatementDataGenerator#creat

**Source stance:** open-question

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/subscribers/DocumentTopicSubscriber.scala; PR: [EN-313] publish v2 email request for monthly statements

**Source-preserving request, proposal, or question:**

> So the only thing we need from document service is this documentId? Should report service just publish to communicate in `StatementDataGenerator#createStatementDataAndGeneratePdf` then?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:3034 · comment 339338119 · PR 4547 · 2022-10-20

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/subscribers/DocumentTopicSubscriber.scala`

## A3-1162 — StatementDataGenerator has documentId+statement after PDF; avoid topic relookup for comm

**Source stance:** suggestion

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/subscribers/DocumentTopicSubscriber.scala; PR: [EN-313] publish v2 email request for monthly statements

**Source-preserving request, proposal, or question:**

> Report’s service StatementDataGenerator has the following:
> 
> ```scala
> for {
>   documentId <- createPdfFileWithAppServer(statementInfo)
>   maybeDocumentId = Some(UUID.fromString(documentId))
>   _ <- statementDbHandler.insert(statementInfo.copy(documentId = maybeDocumentId)).recover {
>     case ex =>
>       throw UnsafeForRetryException(s"Statement insert for customer ${request.customerId} failed!!", ex)
>   }
> 
>   fileCreatedResponse = CreateCustomerStatementResponse(
>     status = StatementStatusEnum.CREATED,
>     documentId = maybeDocumentId,
>     statementInfo = Some(statementInfo)
>   )
>   _ = {
>     logger.info(s"Finished creating statement of type [${request.statementType}] for customer [${statementInfo.customerId}]...")
>   }
> } yield fileCreatedResponse
> ```
> 
> 
> 
> documentId in L2 is only returned after document is created I believe. That means here we have both the documentId \+ statement data. I think we can just publish to communication svc from here, rather than another than another `DocumentTopicSubscriber` in report, and lookup the statement again

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Document ID is returned only after PDF creation; proposed communication publish in StatementDataGenerator reuses ID+statement rather than DocumentTopicSubscriber relookup. Preserve UnsafeForRetryException on statement insert.

**Evidence:** anon-2.jsonl:3035 · comment 339340137 · PR 4547 · 2022-10-20

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/subscribers/DocumentTopicSubscriber.scala`

> Report’s service StatementDataGenerator has the following:
> 
> ```scala
> for {
>   documentId <- createPdfFileWithAppServer(statementInfo)
>   maybeDocumentId = Some(UUID.fromString(documentId))
>   _ <- statementDbHandler.insert(statementInfo.copy(documentId = maybeDocumentId)).recover {
>     case ex =>
>       throw UnsafeForRetryException(s"Statement insert for customer ${request.customerId} failed!!", ex)
>   }
> 
>   fileCreatedResponse = CreateCustomerStatementResponse(
>     status = StatementStatusEnum.CREATED,
>     documentId = maybeDocumentId,
>     statementInfo = Some(statementInfo)
>   )
>   _ = {
>     logger.info(s"Finished creating statement of type [${request.statementType}] for customer [${statementInfo.customerId}]...")
>   }
> } yield fileCreatedResponse
> ```
> 
> ‌
> 
> documentId in L2 is only returned after document is created I believe. That means here we have both the documentId \+ statement data. I think we can just publish to communication svc from here, rather than another than another `DocumentTopicSubscriber` in report, and lookup the statement again

## A3-1176 — RedemptionRequestTopicSubscriberV2.scala: Hmm if this validation fails, the kafka subscriber will forever stuck..

**Source stance:** observed-defect

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala; PR: Feat/INV-671 redemption transaction

**Concern stated in the source:** Hmm if this validation fails, the kafka subscriber will forever stuck..

**Source-preserving request, proposal, or question:**

> Hmm if this validation fails, the kafka subscriber will forever stuck..

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3049 · comment 341783756 · PR 4574 · 2022-10-31

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:3049 · comment 341783756 · PR 4574 · 2022-10-31

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +  redemptionService.redemptionRequestTopic.subscribe.atLeastOnce(Flow[RedemptionRequestMsg].mapAsync(parallelism = 1) {
> +    case msg: RedemptionRequestWaitingForFeeChargeMsg =>
> +      val request = msg.request
> +      validateRequestStatus(RedemptionRequestStatus.PENDING_FEE_COLLECTION, request.status)
> +      val requestedAmountStatusDetails = RequestedAmountStatusDetails(
> +        transactionStatus = TransactionStatus.CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION,
> +        requestedAmount = request.requestedAmount,

## A3-1270 — BrokerCashTransactionTopicSubscriberV2.scala: I guess it doesn’t happen at all, hence we never run into this stuck issue. Let’s log error and move on - since there’s nothing `transaction` service 

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV2.scala; PR: INV-553 feat: Deposit and InterestReceived Transaction Subscriber

**Concern stated in the source:** Generally, when we refactor, let’s try to understand existing behaviour and make better version of it, rather than just follow :thumbsup: Following existing code in cases like this is quite dangerous, because `git blame` is now tag to our names :rofl:

**Source-preserving request, proposal, or question:**

> Yeah I guess it doesn’t happen at all, hence we never run into this stuck issue. Let’s log error and move on - since there’s nothing `transaction` service can do about this anyway.
> 
> Generally, when we refactor, let’s try to understand existing behaviour and make better version of it, rather than just follow :thumbsup: Following existing code in cases like this is quite dangerous, because `git blame` is now tag to our names :rofl:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3151 · comment 334806414 · PR 4360 · 2022-10-03

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:3151 · comment 334806414 · PR 4360 · 2022-10-03

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +        }
> +
> +        _ <- if (deletedTransactionMaybe.isEmpty) {
> +          logger.error(s"Transaction [${msg.transactionId}] is not of the expected type [${expectedTxType}]...")
> +          Future.successful(Done)
> +        } else if (transaction.statusDetails.isInstanceOf[DeletedStatusDetails]) {
> +          Future.successful(Done)

## A3-1284 — ChargeApplication.scala: This one looks strange. How is it possible that this one is lazy val in SG today :open_mouth: I guess because it’s wired in `ServiceLogicImpl` ? Seem 

**Source stance:** open-question

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/ChargeApplication.scala; PR: splits charge into sg vs hk

**Concern stated in the source:** I guess because it’s wired in `ServiceLogicImpl` ?

**Source-preserving request, proposal, or question:**

> This one looks strange. How is it possible that this one is lazy val in SG today :open_mouth: 
> 
> I guess because it’s wired in `ServiceLogicImpl` ? Seem dangerous to me… I think we should not use lazy here, since we definitely want to listen to timeseries always?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3166 · comment 333447633 · PR 4347 · 2022-09-27

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/ChargeApplication.scala`

**Evidence:** anon-2.jsonl:3166 · comment 333447633 · PR 4347 · 2022-09-27

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/ChargeApplication.scala`

**Explicit source context (hunk):**

> -  lazy val feeEstimator = wire[CustomerFeeEstimator]
> +  val planTopicSubscriber: PlanTopicSubscriber = wire[PlanTopicSubscriber]
> +  val goalTopicSubscriber: GoalTopicSubscriber = wire[GoalTopicSubscriber]
> +  lazy val planTimeSeriesTopicSubscriber: PlanTimeSeriesTopicSubscriber = wire[PlanTimeSeriesTopicSubscriber]
> +  val fxRatesTopicSubscriber: FxRatesTopicSubscriber = wire[FxRatesTopicSubscriber]
> +  val voucherWalletTopicSubscriber: VoucherWalletTopicSubscriber = wire[VoucherWalletTopicSubscriber]
> +  val redemptionTopicSubscriber: RedemptionTopicSubscriber = wire[RedemptionTopicSubscriber]

## A3-1332 — Measure goal-readside lookups before adding local eventually-consistent projections

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/InvestmentValueCalculator.scala; PR: [INV-485] feat(compliance): Initial CR validation logic

**Source-preserving request, proposal, or question:**

> This API queries readside table of goal service. We can change to streaming, but should be ok for now?
> 
> All lookup performed here and the CRA class are actually can be done from local DB, if we build the projection. But let’s measure first, before we dive into the eventual consistence hole.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Streaming/local projections are options; source says measure before adding eventual consistency and currently tolerates goal readside lookup.

**Evidence:** anon-2.jsonl:3217 · comment 330804569 · PR 4189 · 2022-09-15

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/InvestmentValueCalculator.scala`

**Evidence:** anon-2.jsonl:3217 · comment 330804569 · PR 4189 · 2022-09-15

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/InvestmentValueCalculator.scala`

**Explicit source context (hunk):**

> +    taaModificationEarmarks: Map[PlanId, TaaModificationEarmark]
> +  ): Future[Map[RiskLevel, BigDecimal]] = {
> +    for {
> +      allPlanTaas <- queryAllPlanTaas(customerId)
> +      effectivePlanTaas = allPlanTaas.map {
> +        case (planId, currentInstrumentWeights) =>
> +          val effectivePlanTaa = taaModificationEarmarks.get(planId).map(_.instrumentWeights).getOrElse(currentInstrumentWeights)

## A3-1355 — transactionTypes.scala: on point \(3\), it’s not about losing data. Old data is still there in events, we just want latest snapshot in State \(ideally\). From readside point 

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/transactionTypes.scala; PR: [WIP] INV-235 Transaction Service v2 models

**Source-preserving request, proposal, or question:**

> Yeah on point \(3\), it’s not about losing data. Old data is still there in events, we just want latest snapshot in State \(ideally\). From readside point of view, we can always have a read model providing snapshot, and potentially another read model providing all data, if needed. But as you pointed out, we don’t need this old data today. In fact, we store all fields, and then have to introduce object level fields like amount and statusUpdatedAt to merge the them again.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3241 · comment 329769641 · PR 4217 · 2022-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/transactionTypes.scala`

**Evidence:** anon-2.jsonl:3241 · comment 329769641 · PR 4217 · 2022-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/transactionTypes.scala`

**Explicit source context (hunk):**

> +    goalId: UUID,
> +    planId: UUID,
> +    requestedAmount: BigDecimal,
> +    assumedAmount: Option[BigDecimal] = None,
> +    settledAmount: Option[BigDecimal] = None,
> +    recurringTransactionId: Option[String] = None,
> +    assumedAt: Option[ZonedDateTime] = None,

## A3-1366 — ReadSidePersistenceComponentsWithKamon already wraps CassandraReadSide

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cka/processors/CkaEventProcessor.scala; PR: [WIP] IAO-378: Split HK vs SG for compliance service

**Source-preserving request, proposal, or question:**

> `ReadSidePersistenceComponentsWithKamon` correctly wraps Lagom’s `CassandraReadSide` with our `CassandraReadSideWithKamonWrapper` already
> 
> 
> 
> All our event processors do not need to expect `CassandraReadSideWithKamonWrapper` explicitly. It should just work out of the box. I change this to make Application a little simpler

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3254 · comment 324077272 · PR 4040 · 2022-08-17

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cka/processors/CkaEventProcessor.scala`

> `ReadSidePersistenceComponentsWithKamon` correctly wraps Lagom’s `CassandraReadSide` with our `CassandraReadSideWithKamonWrapper` already
> 
> ‌
> 
> All our event processors do not need to expect `CassandraReadSideWithKamonWrapper` explicitly. It should just work out of the box. I change this to make Application a little simpler

**Evidence:** anon-2.jsonl:3254 · comment 324077272 · PR 4040 · 2022-08-17

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cka/processors/CkaEventProcessor.scala`

**Explicit source context (hunk):**

> class CkaEventProcessor(
> -  readSide: CassandraReadSideWithKamonWrapper,
> +  readSide: CassandraReadSide,
>    refProvider: PersistentEntityRefProvider,
>    repo: CkaExemptionAcknowledgementRepository,
>    handler: CkaExemptionAcknowledgementDbHandler

## A3-1373 — RecommendedPortfolioChangePageLoader.scala: When would this be not found? If there are legit cases, then we need to determine how to handle them instead of throwing exception…

**Source stance:** open-question

**Context:**

> gateway-impl/src/main/scala/com/endowus/silver/gateway/impl/managers/bffs/RecommendedPortfolioChangePageLoader.scala; PR: INV-403: Use charge API to estimate access fee for RPC summary

**Source-preserving request, proposal, or question:**

> When would this be not found? If there are legit cases, then we need to determine how to handle them instead of throwing exception…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3262 · comment 323330364 · PR 4052 · 2022-08-15

Source path: `gateway-impl/src/main/scala/com/endowus/silver/gateway/impl/managers/bffs/RecommendedPortfolioChangePageLoader.scala`

**Evidence:** anon-2.jsonl:3262 · comment 323330364 · PR 4052 · 2022-08-15

Source path: `gateway-impl/src/main/scala/com/endowus/silver/gateway/impl/managers/bffs/RecommendedPortfolioChangePageLoader.scala`

**Explicit source context (hunk):**

> +            .map(
> +              planFeeEstimation =>
> +                FeeEstimation(
> +                  totalAumAmount = planFeeEstimation.latestAumInAccountingCcy,
> +                  endowusAccessFeeAmount = planFeeEstimation.estimatedAnnualFeeAmount,
> +                  endowusAccessFeeRatio = planFeeEstimation.estimatedAnnualFeeRatio
> +              )

## A3-1376 — InstrumentMarketDataEventProcessor.scala: Just thinking out loud… if we plan to migrate to use Kafka for all events in this processor, do we maybe want to use TopicProducer instead?

**Source stance:** open-question

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessor.scala; PR: wip

**Source-preserving request, proposal, or question:**

> Just thinking out loud… if we plan to migrate to use Kafka for all events in this processor, do we maybe want to use TopicProducer instead?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3265 · comment 319673741 · PR 3873 · 2022-07-29

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessor.scala`

**Evidence:** anon-2.jsonl:3265 · comment 319673741 · PR 3873 · 2022-07-29

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessor.scala`

**Explicit source context (hunk):**

> import scala.concurrent.{ExecutionContext, Future}
>  
> -class InstrumentMarketDataEventProcessor(readSide: CassandraReadSide, refProvider: PersistentEntityRefProvider)(
> +class InstrumentMarketDataEventProcessor(
> +  readSide: CassandraReadSide,
> +  refProvider: PersistentEntityRefProvider,
> +  marketDataTaskTopicProducer: MarketDataTaskTopicProducer,

## A3-1417 — CraManager.scala: I’ll add the Jdbc event processor \+ repository to query for this bit separately… PR is getting too fat now

**Source stance:** explanation

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: HK CRA changes

**Source-preserving request, proposal, or question:**

> I’ll add the Jdbc event processor \+ repository to query for this bit separately… PR is getting too fat now

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3313 · comment 311998249 · PR 3754 · 2022-06-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Evidence:** anon-2.jsonl:3313 · comment 311998249 · PR 3754 · 2022-06-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +        case Some(state) =>
> +          Future.successful(
> +            CraDetailsResponse(
> +              craQuestionnaireVersion = state.craQuestionnaireVersion,
> +              advisoryProfile = toDto(state.advisoryProfile),
> +              annualIncome = state.annualIncome,
> +              liquidNetWorth = state.liquidNetWorth,

## R-3314 — Exclude the latest CRA submission from past results while readside may still lag

**Source stance:** requested-change

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileJdbcRepository.scala; PR 3754: HK CRA changes

**Source-preserving request, proposal, or question:**

> We want to exclude the latest in the past result. It might or might not have arrived in readside yet if you query after a submission - don’t want to confuse FE with this

**Evidence:** anon-2.jsonl:3314 · comment 315797799 · PR 3754 · 2022-07-13

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileJdbcRepository.scala`

## R-3336 — PlanTimeSeriesSubscriber: proposed mapAsync(1) without throttle before finding the unawaited simulation

**Source stance:** suggestion

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/subscribers/PlanTimeSeriesSubscriberForLatestPlanMvTable.scala; PR 3767: projection service kafka message throttling optimization

**Source-preserving request, proposal, or question:**

> [incidental identifier omitted] [incidental identifier omitted] 
> 
> Did we check the execution speed for the jdbc persistence? I would think the main bottleneck for consumption speed from kafka here is due to this throttling, not because we were calling mapAsync with parallelism = 1 previously.
> 
> ‌
> 
> From what I observed so far, I reckon we should be able to use mapAsync with parallelism = 1, but remove the throttling, and it would be much faster without any extra complication.
> 
> ‌
> 
> We would not overly spam the pg, since mapAsync will only move on next message after current jdbc persistence returns. And kafka topic is backpressured by nature - messages only arrive if consumer calls poll.
> 
> ‌

**Conditions and limits:**

- Read together: the throttle-removal suggestion is followed by discovery of an unawaited simulation call and a separate-topic proposal. It is not a settled rule to remove throttling. Source rows: anon-2.jsonl:3336, anon-2.jsonl:3337, anon-2.jsonl:3338.
- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3336 · comment 313172358 · PR 3767 · 2022-07-01

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/subscribers/PlanTimeSeriesSubscriberForLatestPlanMvTable.scala`

>  
> 
> Did we check the execution speed for the jdbc persistence? I would think the main bottleneck for consumption speed from kafka here is due to this throttling, not because we were calling mapAsync with parallelism = 1 previously.
> 
> ‌
> 
> From what I observed so far, I reckon we should be able to use mapAsync with parallelism = 1, but remove the throttling, and it would be much faster without any extra complication.
> 
> ‌
> 
> We would not overly spam the pg, since mapAsync will only move on next message after current jdbc persistence returns. And kafka topic is backpressured by nature - messages only arrive if consumer calls poll.
> 
> ‌

## R-3337 — safeRenewProjectionForCustomer is started with a value binding and not awaited

**Source stance:** explanation

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/subscribers/PlanTimeSeriesSubscriberForLatestPlanMvTable.scala; PR 3767: projection service kafka message throttling optimization

**Source-preserving request, proposal, or question:**

> Ah I missed this line in the processing logic - which does not wait for simulation call to return
> 
> ```
> _ = multiCcySimulationBatchManager.safeRenewProjectionForCustomer(msg.customerId) 
> ```
> 
> ‌
> 
> Ok this makes sense now :thumbsup: 

**Conditions and limits:**

- Read together: the throttle-removal suggestion is followed by discovery of an unawaited simulation call and a separate-topic proposal. It is not a settled rule to remove throttling. Source rows: anon-2.jsonl:3336, anon-2.jsonl:3337, anon-2.jsonl:3338.

**Evidence:** anon-2.jsonl:3337 · comment 313175068 · PR 3767 · 2022-07-01

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/subscribers/PlanTimeSeriesSubscriberForLatestPlanMvTable.scala`

## R-3338 — Decouple MV draining from simulation with a separate retry/throttle/conflate topic proposal

**Source stance:** open-question

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/subscribers/PlanTimeSeriesSubscriberForLatestPlanMvTable.scala; PR 3767: projection service kafka message throttling optimization

**Source-preserving request, proposal, or question:**

> Ah good find. Without your provided context, I thought we want parallel as much as possible, but do not want to spam the simulation service, hence the throttling to protect.
> 
> ‌
> 
> If we care about draining the MV messages fast, and ok to have projection out of sync with MV , does it make sense to dispatch the simulation service call to a separate topic? Then we can retry, throttle, conflate it independently?
> 
> For example, throttle idk X messages per Y seconds \(Y is appropriate to processing time of simulation\), and then conflate the planIds in that batch, so that we don’t unnecessarily renew, etc

**Conditions and limits:**

- Read together: the throttle-removal suggestion is followed by discovery of an unawaited simulation call and a separate-topic proposal. It is not a settled rule to remove throttling. Source rows: anon-2.jsonl:3336, anon-2.jsonl:3337, anon-2.jsonl:3338.

**Evidence:** anon-2.jsonl:3338 · comment 313179722 · PR 3767 · 2022-07-01

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/subscribers/PlanTimeSeriesSubscriberForLatestPlanMvTable.scala`

## R-3376 — At some point, I guess we should split PlanProfile out of Entity. Local cache built from Kafka should just be updated directly, no need to maintain event t

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/GoalTopicSubscriber.scala; PR 3524: adds product line and intent on charge and adds isAlternativeInvestment on fundsmart

**Source-preserving request, proposal, or question:**

> At some point, I guess we should split PlanProfile out of Entity. Local cache built from Kafka should just be updated directly, no need to maintain event traces I think

**Evidence:** anon-2.jsonl:3376 · comment 301716280 · PR 3524 · 2022-05-17

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/GoalTopicSubscriber.scala`

## R-3402 — PlanEventProcessor ServiceClient dependency moves wiring from Components to Application

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanEventProcessor.scala; PR 3398: Feat/IAO-93 block goal modification

**Source-preserving request, proposal, or question:**

> Yes this is fine. But you would have to move the wiring of this processor into \*Application, if it’s not already there.
> 
> By default, most of them will be wired in \*Components.
> 
> We need to move because it now depends on InstrumentService which is declared via `ServiceClient`. This is again available only in `LagomServiceClientComponents` which is extended by `LagomApplication`

**Evidence:** anon-2.jsonl:3402 · comment 295785007 · PR 3398 · 2022-04-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanEventProcessor.scala`

## R-3403 — Why did we add this error logging only for `PlanRecurringTransferScheduleCreatedEvt`? This should be blocked by the changes in GoalServiceImpl already righ

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanEventProcessor.scala; PR 3398: Feat/IAO-93 block goal modification

**Source-preserving request, proposal, or question:**

> Why did we add this error logging only for `PlanRecurringTransferScheduleCreatedEvt`? This should be blocked by the changes in GoalServiceImpl already right?

**Evidence:** anon-2.jsonl:3403 · comment 295822858 · PR 3398 · 2022-04-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanEventProcessor.scala`

## R-3419 — Since `dailyFeeJdbcRepository` is deprecated, I’ll skip updating it here to keep the response of `FeeGenerator#generatePlanFeeForFullRedemption` simpler

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/RedemptionTopicSubscriber.scala; PR 3227: Access fee fixes

**Source-preserving request, proposal, or question:**

> Since `dailyFeeJdbcRepository` is deprecated, I’ll skip updating it here to keep the response of `FeeGenerator#generatePlanFeeForFullRedemption` simpler

**Evidence:** anon-2.jsonl:3419 · comment 287420659 · PR 3227 · 2022-03-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/RedemptionTopicSubscriber.scala`

## R-3420 — `FeeGenerator#generatePlanFeeForFullRedemption` is not “safe” and would propagate any exception. Unlike `FeeGenerator#safeGeneratePlansFeeForCustomer` whic

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/RedemptionTopicSubscriber.scala; PR 3227: Access fee fixes

**Source-preserving request, proposal, or question:**

> `FeeGenerator#generatePlanFeeForFullRedemption` is not “safe” and would propagate any exception. Unlike `FeeGenerator#safeGeneratePlansFeeForCustomer` which would catch all exception, and return an error response, then this code would check and throw exception again.

**Evidence:** anon-2.jsonl:3420 · comment 287421009 · PR 3227 · 2022-03-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/RedemptionTopicSubscriber.scala`

## R-3423 — Yep, `RedemptionRequestWaitingForFeeChargeMsg` only arrived after when `ConfirmSettlementCmdHandler` handled the order\(s\) confirm settlement

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/RedemptionTopicSubscriber.scala; PR 3227: Access fee fixes

**Source-preserving request, proposal, or question:**

> Yep, `RedemptionRequestWaitingForFeeChargeMsg` only arrived after when `ConfirmSettlementCmdHandler` handled the order\(s\) confirm settlement

**Evidence:** anon-2.jsonl:3423 · comment 287438645 · PR 3227 · 2022-03-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/RedemptionTopicSubscriber.scala`

## R-3424 — Replayed fee must match the already charged period; conflicting extra fee needs investigation

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/InitiateFeeChargeCmdHandler.scala; PR 3227: Access fee fixes

**Source-preserving request, proposal, or question:**

> Yep, so message replay is a common expected thing with Kafka. We simply log info here, in case we want “proof” to show it happens and how often it happens.
> 
> ‌
> 
> BUT when it is replayed, we expect the fee to be identical - i.e whole period has been charged. If until here, and we see more fees again, we can’t simply ignore \(can’t charge with same id again, but maybe also can’t ignore the fee completely\)… hence log error below and we check case-by-case

**Evidence:** anon-2.jsonl:3424 · comment 292162917 · PR 3227 · 2022-04-04

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/InitiateFeeChargeCmdHandler.scala`

## R-3445 — PDF upload sends email before documentId persistence; SFTP widens the duplicate window

**Source stance:** open-question

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/StatementDataGenerator.scala; PR 3217: moves to generate metadata separately

**Source-preserving request, proposal, or question:**

> Something to think about. This app server call to create PDF will actually do 2 things:
> 
> * create the PDF
> * call document service to upload the file to GCP → this will trigger eventually trigger communication to send email
> 
> Existing code, right after this, will persist the documentId to report’s cassandra table - which will be used to determine if reprint is required later on.
> 
> If the pod crashes between these 2 steps, report generation is not idempotent, i.e. duplicate documents created / duplicate emails sent to user.
> 
> ‌
> 
> With this change, we somewhat widen the gap with another step to upload to SFTP. Should we consider uploading to SFTP after we persist? If fail to upload, we can retry? Or the generate metadata file part can also attempt uploading if documentId is in csv data, but not found in SFTP? Or we simply log error, which raise sentry and we manually drop the file - should be infrequent enough?
> 
> ‌

**Evidence:** anon-2.jsonl:3445 · comment 286831687 · PR 3217 · 2022-03-11

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/StatementDataGenerator.scala`

## R-3455 — Maybe we don’t need parallelism = 2 here, since it’s always same entity

**Source stance:** suggestion

**Context:**

> rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/processors/RebateDistributionEventProcessor.scala; PR 3103: Fix Rebate service

**Source-preserving request, proposal, or question:**

> Maybe we don’t need parallelism = 2 here, since it’s always same entity

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3455 · comment 282166672 · PR 3103 · 2022-02-23

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/processors/RebateDistributionEventProcessor.scala`

## R-3475 — Initial proposal keeps old Plan writes while a separate new Plan processor populates V1

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessor.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> Existing `GoalJdbcEventProcessor` handles both goal and plan events to persist to JDBC - even though they are independent.
> 
> ‌
> 
> Keep `PlanJdbcDbHandler` in here so that it continue to populate existing table.
> 
> Add `PlanJdbcEventProcessor` handling only plan events, and persist via `PlanJdbcDbHandlerV1` to new table.
> 
> Once switch, we can remove plan events from `GoalJdbcEventProcessor`

**Conditions and limits:**

- PR3029 changes direction: the initial preferences-only and split-processor plan is corrected for missing fields and replaced with jointly updating Goal/Plan for consistency. Preserve the old-table/new-table and offset-store details as historical rollout choices. Source rows: anon-2.jsonl:3473, anon-2.jsonl:3474, anon-2.jsonl:3475, anon-2.jsonl:3476, anon-2.jsonl:3477, anon-2.jsonl:3478, anon-2.jsonl:3479, anon-2.jsonl:3480.

**Evidence:** anon-2.jsonl:3475 · comment 278839281 · PR 3029 · 2022-02-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessor.scala`

## R-3477 — Identical to `GoalTable` except for version bump. We want to ensure consistency between Goal and Plan tables, hence update them together in same JdbcEventP

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalTableV1.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> Identical to `GoalTable` except for version bump. We want to ensure consistency between Goal and Plan tables, hence update them together in same JdbcEventProcessor

**Conditions and limits:**

- PR3029 changes direction: the initial preferences-only and split-processor plan is corrected for missing fields and replaced with jointly updating Goal/Plan for consistency. Preserve the old-table/new-table and offset-store details as historical rollout choices. Source rows: anon-2.jsonl:3473, anon-2.jsonl:3474, anon-2.jsonl:3475, anon-2.jsonl:3476, anon-2.jsonl:3477, anon-2.jsonl:3478, anon-2.jsonl:3479, anon-2.jsonl:3480.

**Evidence:** anon-2.jsonl:3477 · comment 279569847 · PR 3029 · 2022-02-14

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalTableV1.scala`

## R-3478 — Initial processor split is withdrawn so Goal and Plan update together for consistency

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessor.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> We no longer follow the above approach to split `GoalJdbcEventProcessor` into separate processors for Goal and Plan - because we want to update them together to ensure consistency \(e.g. avoid scenarios that we somehow update plans but not goals, and vice versa, due to some stuck event processor\)

**Conditions and limits:**

- PR3029 changes direction: the initial preferences-only and split-processor plan is corrected for missing fields and replaced with jointly updating Goal/Plan for consistency. Preserve the old-table/new-table and offset-store details as historical rollout choices. Source rows: anon-2.jsonl:3473, anon-2.jsonl:3474, anon-2.jsonl:3475, anon-2.jsonl:3476, anon-2.jsonl:3477, anon-2.jsonl:3478, anon-2.jsonl:3479, anon-2.jsonl:3480.

**Evidence:** anon-2.jsonl:3478 · comment 279569999 · PR 3029 · 2022-02-14

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessor.scala`

## R-3479 — Identical to `GoalJdbcEventProcessor` except using V1 DBHandler \+ V1 readsideId

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessorV1.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> Identical to `GoalJdbcEventProcessor` except using V1 DBHandler \+ V1 readsideId

**Conditions and limits:**

- PR3029 changes direction: the initial preferences-only and split-processor plan is corrected for missing fields and replaced with jointly updating Goal/Plan for consistency. Preserve the old-table/new-table and offset-store details as historical rollout choices. Source rows: anon-2.jsonl:3473, anon-2.jsonl:3474, anon-2.jsonl:3475, anon-2.jsonl:3476, anon-2.jsonl:3477, anon-2.jsonl:3478, anon-2.jsonl:3479, anon-2.jsonl:3480.
- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3479 · comment 279570105 · PR 3029 · 2022-02-14

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessorV1.scala`

## R-3480 — We also switch to use CassandraReadSide instead of SlickReadSide for the offsetstore for more reliability.

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessorV1.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> We also switch to use CassandraReadSide instead of SlickReadSide for the offsetstore for more reliability.

**Conditions and limits:**

- PR3029 changes direction: the initial preferences-only and split-processor plan is corrected for missing fields and replaced with jointly updating Goal/Plan for consistency. Preserve the old-table/new-table and offset-store details as historical rollout choices. Source rows: anon-2.jsonl:3473, anon-2.jsonl:3474, anon-2.jsonl:3475, anon-2.jsonl:3476, anon-2.jsonl:3477, anon-2.jsonl:3478, anon-2.jsonl:3479, anon-2.jsonl:3480.

**Evidence:** anon-2.jsonl:3480 · comment 280376612 · PR 3029 · 2022-02-16

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessorV1.scala`

## R-3500 — Yup as long as readiness probe fails by then, pod won’t receive any more traffic. However, for event processor flow, I’m not sure if Lagom knows to re-assi

**Source stance:** open-question

**Context:**

> kubernetes/kustomize/generate_scripts/base/deployment.sh; PR 3020: Use startupProbe instead of initial delay

**Source-preserving request, proposal, or question:**

> [incidental identifier omitted] Yup as long as readiness probe fails by then, pod won’t receive any more traffic.
> 
> However, for event processor flow, I’m not sure if Lagom knows to re-assign the tags to other pods. But I guess this would just increase the lag for \(10 \+ 10\) \* 10 = 200s before pod is killed

**Conditions and limits:**

- PR3020 probe timing proposals are followed by an explicit decision to revert the unrelated change and only remove the initial delay. Do not adopt the discussed timings as a final tuning policy. Source rows: anon-2.jsonl:3496, anon-2.jsonl:3497, anon-2.jsonl:3498, anon-2.jsonl:3499, anon-2.jsonl:3500.
- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3500 · comment 278711448 · PR 3020 · 2022-02-10

Source path: `kubernetes/kustomize/generate_scripts/base/deployment.sh`

>  Yup as long as readiness probe fails by then, pod won’t receive any more traffic.
> 
> However, for event processor flow, I’m not sure if Lagom knows to re-assign the tags to other pods. But I guess this would just increase the lag for \(10 \+ 10\) \* 10 = 200s before pod is killed

## R-3501 — Proposal to recover force-rebalance failure after successful TAA update because a later topic message can trigger rebalance

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/GoalModifyConfirmationBehaviour.scala; PR 3019: SILVER-11923: Factors goal modify summary/confirmation

**Source-preserving request, proposal, or question:**

> This force rebalance thing - if it fails, do we really want to return error to FE, even though goal’s TAA is actually successfully updated?  
>   
> I’m thinking we probably should recover this future, to log and silent the error…
> 
> Rebalance service will eventually receive `PlanTargetAssetAllocationUpdatedMsg`  and trigger rebalance then \(if still not trigger by this force call\)

**Evidence:** anon-2.jsonl:3501 · comment 278484200 · PR 3019 · 2022-02-09

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/GoalModifyConfirmationBehaviour.scala`

## R-3517 — Added `Deleted` to the cases in `deleteRelatedTransaction` I see `DeleteCmd` is already handled correctly by the entity if in `Deleted` state

**Source stance:** reported-verification

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/common/DividendDeleter.scala; PR 2835: SILVER-11314: Fetch DividendState from entity before deleting to handle lag between DividendJdbcEventProcessor and DividendEventProcessor

**Source-preserving request, proposal, or question:**

> Added `Deleted` to the cases in `deleteRelatedTransaction`
> 
> I see `DeleteCmd` is already handled correctly by the entity if in `Deleted` state

**Evidence:** anon-2.jsonl:3517 · comment 272457921 · PR 2835 · 2022-01-13

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/common/DividendDeleter.scala`

## R-3527 — I mark this deprecated, and will remove after we verify everything is fixed in prod. For same reason, I will reuse existing `DividendReinvestedEvt` since t

**Source stance:** requested-change

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/DividendServiceImpl.scala; PR 2833: SILVER-11229: Fix settlement date for dividend reinvestment

**Source-preserving request, proposal, or question:**

> I mark this deprecated, and will remove after we verify everything is fixed in prod.
> 
> For same reason, I will reuse existing `DividendReinvestedEvt` since this is only temporary.
> 
> We can consider adding an OverrideDividendStateEvt in future, if the need to sync with Investment service comes back. But then, we should implement all cases properly, rather than just Reinvested state

**Conditions and limits:**

- PR2833 preserves separate historical migration, Confirmed-only sync, date/timestamp meanings, and optional-field alternatives. Naming evolves through priceDate to settlementDate. The final comment defers optional-forever versus mandatory-plus-migration to a later decision. Source rows: anon-2.jsonl:3522, anon-2.jsonl:3523, anon-2.jsonl:3524, anon-2.jsonl:3525, anon-2.jsonl:3526, anon-2.jsonl:3527, anon-2.jsonl:3528, anon-2.jsonl:3531, anon-2.jsonl:3533, anon-2.jsonl:3535, anon-2.jsonl:3536, anon-2.jsonl:3537, anon-2.jsonl:3538.

**Evidence:** anon-2.jsonl:3527 · comment 272781190 · PR 2833 · 2022-01-14

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/DividendServiceImpl.scala`

## R-3528 — No we sync only Confirmed ones. Assumed dividends \(if any\) would eventually be confirmed, and get processed by new logic

**Source stance:** requested-change

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/ces/DividendCommands.scala; PR 2833: SILVER-11229: Fix settlement date for dividend reinvestment

**Source-preserving request, proposal, or question:**

> No we sync only Confirmed ones. Assumed dividends \(if any\) would eventually be confirmed, and get processed by new logic

**Conditions and limits:**

- PR2833 preserves separate historical migration, Confirmed-only sync, date/timestamp meanings, and optional-field alternatives. Naming evolves through priceDate to settlementDate. The final comment defers optional-forever versus mandatory-plus-migration to a later decision. Source rows: anon-2.jsonl:3522, anon-2.jsonl:3523, anon-2.jsonl:3524, anon-2.jsonl:3525, anon-2.jsonl:3526, anon-2.jsonl:3527, anon-2.jsonl:3528, anon-2.jsonl:3531, anon-2.jsonl:3533, anon-2.jsonl:3535, anon-2.jsonl:3536, anon-2.jsonl:3537, anon-2.jsonl:3538.

**Evidence:** anon-2.jsonl:3528 · comment 272788902 · PR 2833 · 2022-01-14

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/ces/DividendCommands.scala`

## R-3555 — I think it’s better to let consumer\(s\) have to chance to decide what to do with missing data - rather than throwing

**Source stance:** suggestion

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/portfolioStats/PortfolioStatsJdbcRepository.scala; PR 2807: Feat/projection svc portfolio stats jdbc

**Source-preserving request, proposal, or question:**

> I think it’s better to let consumer\(s\) have to chance to decide what to do with missing data - rather than throwing

**Evidence:** anon-2.jsonl:3555 · comment 270149129 · PR 2807 · 2021-12-30

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/portfolioStats/PortfolioStatsJdbcRepository.scala`

## R-3556 — If you prefer Exception instead, because say you expect caller to always call with valid ID… then code is little cleaner to read if we return Future.failed

**Source stance:** open-question

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/portfolioStats/PortfolioStatsJdbcRepository.scala; PR 2807: Feat/projection svc portfolio stats jdbc

**Source-preserving request, proposal, or question:**

> If you prefer Exception instead, because say you expect caller to always call with valid ID… then code is little cleaner to read if we return Future.failed\(NotFound\(\)\)

**Evidence:** anon-2.jsonl:3556 · comment 270149593 · PR 2807 · 2021-12-30

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/portfolioStats/PortfolioStatsJdbcRepository.scala`

## R-3557 — The method signature returns List of stats, so maybe it is semantically better to return empty list instead throw exception if not found?

**Source stance:** suggestion

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala; PR 2807: Feat/projection svc portfolio stats jdbc

**Source-preserving request, proposal, or question:**

> The method signature returns List of stats, so maybe it is semantically better to return empty list instead throw exception if not found?

**Evidence:** anon-2.jsonl:3557 · comment 270160989 · PR 2807 · 2021-12-30

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala`

## R-3558 — Portfolio stats exact-ID lookup and filter lookup both produce a List response

**Source stance:** suggestion

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala; PR 2807: Feat/projection svc portfolio stats jdbc

**Source-preserving request, proposal, or question:**

> Maybe something like this?
> 
> ```scala
> for {
>   stats <- (portfolioId, effectiveDate, statsCcy) match {
>     case (Some(pid), Some(date), Some(ccy)) => portfolioStatsJdbcRepository.findById(pid, date, ccy).map(_.toSeq)
>     case _ => portfolioStatsJdbcRepository.findByFilter(portfolioId, effectiveDate, statsCcy)
>   }
> } yield stats.map(PortfolioStats.toDto).toList
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:3558 · comment 270161114 · PR 2807 · 2021-12-30

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala`

## R-3560 — Question… do we need to change the consumer group / reset current group’s offset so that we re-process the kafka messages again? Or is there a way to re-pu

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriber.scala; PR 2804: [SILVER-11115] Fix dividend transaction payout date when dividend reinvestment is assumed

**Source-preserving request, proposal, or question:**

> Question… do we need to change the consumer group / reset current group’s offset so that we re-process the kafka messages again? Or is there a way to re-publish them?

**Evidence:** anon-2.jsonl:3560 · comment 270107509 · PR 2804 · 2021-12-30

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriber.scala`

## R-3578 — Hmm.. this `event` is used as `event.Tag.forEntityId(entityId).tag` which refer to this singleton ``` object CustomerTransactionManagerEvt { val NumShards 

**Source stance:** open-question

**Context:**

> amend-scripts/src/main/scala/tools/FindEventsMissingTagAndRebuildTagViews.scala; PR 2773: SILVER-10952: FindEventsMissingTagAndRebuildTagViews improvements

**Source-preserving request, proposal, or question:**

> Hmm.. this `event` is used as `event.Tag.forEntityId(entityId).tag`  
>   
> which refer to this singleton
> 
> ```
>   object CustomerTransactionManagerEvt {
>     val NumShards = 4
>     val Tag = AggregateEventTag.sharded[CustomerTransactionManagerEvt](NumShards)
>   }
> ```
> 
>   
> `Class.forName()` won’t help here right?

**Evidence:** anon-2.jsonl:3578 · comment 268922338 · PR 2773 · 2021-12-22

Source path: `amend-scripts/src/main/scala/tools/FindEventsMissingTagAndRebuildTagViews.scala`

