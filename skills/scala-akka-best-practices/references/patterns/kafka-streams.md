# Partition keys, subscribers, streams, and consumer groups

167 source-specific cases. Statements retain their historical scope and source stance. Read related PR cases for corrections or alternatives.

## Cases

- A1-1295 — Consider internal repartitioned Kafka topic rather than sequential DB locking
- A2-0200 — InitiateCancellationFlowCmdHandler: This `INVALID_CANCEL_ATTEMPT` is mapped to NotFound right now. It seems not used, so maybe change it to BadRequest instead?
- A2-0236 — InvestmentPlanTableV8: This index is too much I would think. So most of the use cases of recurring investment, I think index on the `NextUpcomingDate` is sufficient. Other condi...
- A2-0250 — package: Let’s keep this for now, but looks like if we ever add another type of feeConfig that does not have exact feeRate, it would be responsibility of charge svc to understan...
- A2-0259 — Review: RBAC validation previously failed because ResourceAction.newInstance(resource) defaulted resourceId to `_NEW_` while CheckResult lookup used resource kind. After resourc...
- A2-0320 — MarketDataUploader: Let’s use `runWithReporting` which gives some utility around logging / allowing to capture individual error and move on instead of blocking the stream
- A2-0347 — GoalSupportingDataTableV1: `GoalActionContext` covers `CREATION_APPROVED, MODIFICATION_APPROVED` which is initiated from goal svc
- A2-0414 — BaseAdvisoryServiceE4s: Should we create another API object for all these tenant specific endpoints? Their logic should extract the tenant from tracing context, and use it for c...
- A2-0423 — SgInstrumentFilterManager: With this structure, `getInstrumentsAndFiltersForCustomer` and `getInstrumentsAndFiltersForTenantFa` can be used directly in the upstream manager
- A2-0441 — InvestorTypeFixForNonSgdInstrumentWithCpfAndSrs: better to use `Source(instrumentsToUpdate).mapAsync(...)` so that we can control the parallelism
- A2-0713 — PortfolioMonthlyChangesHelper: Let’s make this method handing the subscriber lookup \+ streaming the task \(in next task\), and keep the instrument projection simple.
- A2-0742 — InstrumentMonthlyChangesJdbcRepository: Maybe rename:
- A2-0796 — InstrumentPortfolioSubscribersDataRepository: Just `streamInstrumentPortfolioSubscribers` ?
- A2-0801 — ServiceLogicImpl: Maybe source the instruments and flatMapConCat inside to avoid bloating the memory here
- A2-0806 — TopicSubscriber: We should also bake in the Kamon Context propagation in this processing flow \(with option to opt out maybe if needed\)
- A2-0811 — TopicSubscriber: We should use `topicSubscriberSettings.parallelism` here?
- A2-0812 — TopicSubscriber: I realize the `ScaladslKafkaSubscriber` additionally set the below
- A2-0813 — BrokerOrderTopicSubscriber: Lagom is using below by default
- A2-0814 — TopicSubscriber: In the TaskTopicSubscribers, these are used to retry processing individual message \(before dropping them\). Here you’re using as config to restart the subscrip...
- A2-0816 — TopicSubscriber: [person] As discussed, it’s actually not safe to blindly increase `parallelism` here when consuming messages from same partition \(only safe for the task topic\).
- A2-0821 — ProductPortfolioRepository: Maybe we can keep this method generic, but only handle for CoreEnhanced for now…
- A2-0882 — EmailProviderData: All of these, in theory, would need to be optional. Cuz there might be existing message in the kafka topic without the fields, and communication svc starts ex...
- A2-0933 — Review: We also need to emit kafka msg for skipped fee charge and handle it on redemption svc side to complete the full redemption request
- A2-0996 — package: Rename to `NotifyRebalanceTradeSettlementDetailsAmendedCmd`… do the same for event and kafka msg
- A2-1006 — RedemptionRequestTopicSubscriberV3: Not sure if we need all these validation in transaction svc. Maybe just dump directly with status = `SETTLEMENT_CONFIRMED`.
- A2-1007 — package: Maybe following naming pattern of investment svc, e.g. `RedemptionRequestSettlementDetailsAmendedEvt`… update for Kafka msg too
- A2-1073 — PushNotificationProviderData: In theory these should be optional \(otherwise we might break serdes of there are lagged messages in the kafka topic\), but I guess this one is ok ...
- A2-1116 — RecurringInvestmentProcessor: You can import OptionUtils and use onNone and make this a bit nicer… also better to extract schedule here, so that we don’t have to blindly call ge...
- A2-1171 — Review: Tested in SG staging with `charge` svc
- A2-1172 — TaskTopicManagementPubSub: This is only published to whoever subscribes to this akka Topic, i.e. the service instances only
- A2-1174 — TaskTopicManagementPubSub: No issue if wrong task. I added error log for this in TaskTopicManager too.
- A2-1197 — InstrumentExportScheduler: You can just batch it here
- A2-1229 — HkComplianceHelperImpl: mapAsync\(2\)
- A2-1324 — EdgeWarningAndRestrictionQueryLogic: If no remote calls, no need to use multiple threads for this. It should be fast enough with normal `.map`. No need akka stream as well
- A2-1366 — MarketDataUploader: Nit: no need to start a Source from beginning I think
- A2-1367 — MarketDataUploader: If we propagate the failure in these places, it will stop the whole flow processing. I suppose we just want to skip?
- A2-1412 — AdvisoryApplication: I haven’t checked fully, but I think the pattern I’ve seen so far, the kafka subscribers are wired and started last. So we keep `setupBaseSubscribers` as la...
- A2-1491 — TradeTopicSubscriber: Hmm I’m surprised we have so many `parallelism` = 2 in investment svc without the safeMapAsync… [person] speed should be fine here, we should just change t...
- A2-1493 — FlowUtils: ```
- A2-1585 — TransactionTypes: We can let the old `FxConversionDetails` having optional accounts, as we are migrating away from this v1 model.
- A2-1593 — package: FYI [person] , [person] will create another set of `FundingInstructions` that is more suitable for upstream of investment svc… particularly, there will be no `fxConvers...
- A2-1612 — RebateDistributionCommunicationsManager: Just Source and mapAsync these
- A2-1616 — RebateDistributionCommunicationsManager: We will put all these data in memory, and it will only grow. Better to aggregate the data as part of the processing stream
- A2-1619 — RebateDistributionCommunicationsManager: Just Source the `customerRebates` and mapAsync to lookup instruments
- A2-1731 — SgFundSmartManagerV3: At this point we don’t have any remote calls anymore, can do mapAsync\(4\) I think
- A3-0055 — PortfolioOfferingResponseV2 sealed-trait concern and product-specific MAA card flow
- A3-0056 — BrokerCashTransactionTopicSubscriberV3.scala: transactionV3 is good enough I think… no need to repeat the topic in group name
- A3-0057 — BrokerCashTransactionTopicSubscriberV3.scala: Can we add some log here, info is good enough I think, saying that we are skipping because txn is already deleted
- A3-0058 — DividendTopicSubscriberV3.scala: The problem with this is it’s a bit harder to unit test just the logic, cuz you will need to mock the topic.subscriber chain We can potentially add a 
- A3-0059 — DividendTopicSubscriberV3.scala: Existing code even in v1, but why would this need force…
- A3-0060 — DividendTopicSubscriberV3.scala: Confirm defined for SG? If yes, let’s remove this to avoid confusion
- A3-0061 — DividendTopicSubscriberV3.scala: late but why do we even need this wrapper? Just mark Transaction with `PlayJsonSerializable`?
- A3-0062 — InvestmentRequestTopicSubscriberV3.scala: Should be able to remove this throttle?
- A3-0063 — RedemptionRequestTopicSubscriberV3.scala: This should be confirmed
- A3-0064 — DividendTopicSubscriberV3.scala: but you will need to mock the whole chain… doable but just boiler plate ``` dividendService .dividendTopic .subscribe .withGroupId(groupId) .atLeastOn
- A3-0065 — Dividend forceUpdate comment: deletion then redistribution context
- A3-0071 — ServiceLogicImplV2.scala: This one is old code, but I think better to mapAsync so that we can control the parallelism instead of blind run with throttle… we can ignore the resu
- A3-0107 — Quarterly fee estimate avoids Kafka task: no OOMKilled and idle partition/consumer cost
- A3-0108 — Estimated fee resend: forceResend plus customer include/exclude sets, not amount-derived comm ID
- A3-0233 — PlanRecurringInvestmentScheduleExpiringDailyTriggerTopicProducerDirect.scala: name this `GoalKafkaTaskTopicProducerDirect` and just put all the task topics here. Name gets too long..
- A3-0234 — Goal/plan-not-found handler exception can poison task topic
- A3-0235 — Expiring-schedule Kafka lag/replay must not notify a replacement schedule
- A3-0237 — package.scala: No need sealed trait if we are using separate topic per msg type
- A3-0267 — RecurringInvestmentScheduleJdbcEventProcessor.scala: In theory again, since we don’t actually care about this table from application side, we should just add another topic producer that re-publish all me
- A3-0286 — EndowusKafkaConfig.scala: consumer
- A3-0287 — EndowusTopicConsumerMetrics.scala: ~~Should we capture this on producer side instead?~~ We already captured this on producer side. Our kafka topics are all internal, so in theory, produ
- A3-0288 — EndowusTopicConsumerMetrics.scala: consumer. Same for below
- A3-0289 — kafka.conf: Do we set topic level config `max.message.bytes` or broker level config `message.max.bytes`?
- A3-0290 — ConsumerTopicFactory.scala: The fact that we’re using producer config here means this msg size metric should really be on producer side no? :stuck_out_tongue:
- A3-0291 — EndowusTopicProducers.scala: `max.request.size`?
- A3-0292 — Producer persistence offset versus consumer message timestamp metric naming
- A3-0293 — Kafka CreatedTime lag includes Akka persistence delay and poll interval
- A3-0294 — kafka.conf: [<url> data-inline-card='' } Default is 2MB, can be overridden up to 8MB, but we would need to override ourselves if we want higher
- A3-0321 — BrokerMccyAccountCreatorProcessor.scala: using projection makes sense, cuz it’s all internal to broker svc. No need extra hop to Kafka. Other events would be filtered out anyway so it should 
- A3-0323 — Three-MCCY-broker creation: partial success, retry and stale active-account readside
- A3-0324 — ServiceLogicImpl.scala: If topic producer also misses then we need to either republish the event, or also sync trading with rebalance. In the case I need right now, only read
- A3-0364 — RebateDistributionTopicSubscriberV2.scala: just log error and move on right? why hard block here and get stuck on a poison msg?
- A3-0420 — Risk-target performance example uses mapAsync2 over risks and mapAsync1 over plans
- A3-0499 — services.list: And you would need to release all services listening to redemption topic.
- A3-0571 — Only transient errors should throw in EventProcessor/TopicSubscriber to avoid stuck data errors
- A3-0592 — Investment owns pending-investment communication after broker virtual-account update
- A3-0597 — BrokerAccountTopicSubscriberHandlers.scala: 12 or 1? Also do you think it’s better to filter timestamp in the subscriber?
- A3-0598 — BrokerAccountTopicSubscriberHandlers.scala: If we rethrow here, and it’s not transient error… the subscriber will get stuck
- A3-0604 — Alts cash-reservation remote call in projection; Kafka request/result ideal lacks trading events
- A3-0642 — : Will trading release this for HK too? If yes, we would need to handle in V2 entity?
- A3-0643 — : AFAICS, trading add this new topic `InvestmentTransferTopic` to BaseTradingService… so ideally we should handle for both region You can discuss this w
- A3-0644 — HK investment-transfer handler deferred under coordinated blocked rollout
- A3-0656 — ContractNoteNotificationManagerHK.scala: If we throw on this corrupted msg, the subscriber will be stuck
- A3-0702 — PortfolioVersionUpgradeRebalanceRequestsGenerator.scala: Good point. Added the runFold back
- A3-0707 — : Kafka [ProducerConfig](<url> is now logged :stuck_out_tongue: ``` batch.size = 16384 linger.ms = 0 ``` I think we will need to at least setting non-ze
- A3-0717 — MV projection upserts every latest message before rebalance checks; same-group migration
- A3-0724 — Kafka logger override in conf-reference, then Vault/config-map per-service level
- A3-0726 — Referral SG-only investment-topic subscriber requires separate SG/HK release tags
- A3-0728 — UpdateRebalanceRequestWithSettlementAssumedOrderCmdHandler.scala: Feels like concern of trading or even broker svc. The msg contract from trading svc has all these optional fields. Do we start logging for all of them
- A3-0740 — Rebalance cash-release timing: pending-MV double-count window until buy export
- A3-0741 — HkRebalanceTopicSubscriber.scala: Contract note events if any should be at order level. We should not use the same message `RebalanceTradeSubmittedExternallyMsg` which is at whole trad
- A3-0742 — HkRebalanceTopicSubscriber.scala: We might update to assumed/confirmed amount if we want to. However, the difference won’t be too huge. I don’t implement it here yet because as of toda
- A3-0744 — HkRebalanceTopicSubscriber.scala: the order level messages only applicable for contract notes change. For this CR flow, we care about the order level messages from timeseries. They are
- A3-0746 — New consumer group starts latest and may miss lagged messages during rollout
- A3-0753 — SubscriberMetricsWithKamon.scala: even for Lagom-removed services today, we still use Lagom for kafka subscriber flow. This is added just to monitor the performance difference when we 
- A3-0754 — SubscriberMetricsWithKamon.scala: The `kafka_consumergroup_group_lag_seconds` is estimated by the lag exporter using `endOffsets` and `listConsumerGroupOffsets` without actually consum
- A3-0758 — Transaction FX conversion Futures: bounded Source.mapAsync2 proposed
- A3-0804 — SftpMetadataChecker.scala: Do we need to throttle and `parallelism` = 1? I think it’s ok to just query with `parallelism` = 2 without throttling here
- A3-0811 — AdvisedPortfolioOfferingsManager.scala: You can write this as ``` .mapAsyncUnordered(parallelism = 2) { case (portfolioId, effectiveDate) => ```
- A3-0821 — Independent dividend files: BadRequest nonretry and bounded TCP/unknown retry
- A3-0822 — Recurring failure email: actual reason, event-domain coupling and direct-publish deferral
- A3-0849 — NotificationManager.scala: You can do ``` .mapAsync(2) { case (customerData, profileData) => ... } ```
- A3-0854 — NotificationManager.scala: Then you can `.collect { case Some(customerData) => customerData }` to flatten the flow
- A3-0880 — FxRatesProjectionRepository.scala: If no streaming, then don’t need SlickSession I think
- A3-0886 — AdvisoryApplication.scala: Don’t we need subscriber to customer/onboarding topic to populate the `customerProjectionDataJdbcRepository`?
- A3-0906 — CRAExpiryDailyTriggerTopicProducerDirect.scala: Why do we partition using date? Wouldn’t that mean all messages of same trigger will go to only 1 instance?
- A3-0907 — CRAExpiryDailyTriggerTopicProducerDirect.scala: Oh this one is just to trigger the whole batch, not individual customer… Using one whole kafka topic for just 1 message a day seems a little overkille
- A3-0908 — Daily cron queries eligible customers; customerId-keyed Kafka tasks process individually
- A3-0921 — CraManagerTest.scala: assert `vcStateChangeDailyTriggerTopicProducerDirect` not called?
- A3-0924 — CraManager.scala: If we throw, we block Kafka..
- A3-0931 — HkServiceLogicImpl.scala: Oh bulk upsert for whole set of customers would be too large… either batch the source, or just upsert one by one I think…
- A3-0932 — HkServiceLogicImpl.scala: I didn’t realize getPaginatedSource already concat all the page previously..
- A3-0936 — SgDividendService.scala: I’m not really sure. But trading subscribes to it for old flow..
- A3-0937 — PlanDividendDistributionTopicSubscriber.scala: for old flow, I keep them in SgDividendService
- A3-0993 — : can we also make sure the subscriber for new model doesn’t have the same bug? Then we can add services.list and release :thumbsup:
- A3-0995 — SG/HK investment communication trigger ownership and deferred SG migration
- A3-1000 — CustomerAdvisoryProfileTopicSubscriber.scala: we can remove this groupId now, since we will use only 1 group. Otherwise maybe rename it
- A3-1001 — HkCustomerTopicSubscriber.scala: If you want to name the group, at least put `compliance` in there so we can tell easily which service is the subscriber
- A3-1089 — : I understand we can potentially reuse existing event processor because: * in HK, it’s brand new so we start from scratch * in SG, we don’t process old
- A3-1091 — DividendCommunicationV2EventProcessor.scala: It’s legit to distribute dividend with infoDate in the distant past. Why don’t we filter using createdAt field instead? Also, just to confirm, we want
- A3-1117 — RebalanceApplication.scala: customer preference is not implemented in HK yet. So currently this just scream `UNKNOWN_TOPIC_OR_PARTITION` - I’ll remove the wiring for HK. Good cat
- A3-1176 — RedemptionRequestTopicSubscriberV2.scala: Hmm if this validation fails, the kafka subscriber will forever stuck..
- A3-1248 — HkInvestmentTopicSubscriber.scala: `investmentRequestId` will always be available in Kafka messages from `investment` service - because they are materialized requests. You can see it is
- A3-1264 — Release-earmark subscriber serial1 is conservative preference, not required ordering proof
- A3-1268 — BrokerCashTransactionTopicSubscriberV2.scala: If we throw here, this subscriber will stuck on this message
- A3-1270 — BrokerCashTransactionTopicSubscriberV2.scala: I guess it doesn’t happen at all, hence we never run into this stuck issue. Let’s log error and move on - since there’s nothing `transaction` service 
- A3-1358 — CustomerAdvisoryProfileEntity.scala: Yup. Switched to another exception type for concurrent modification, and retry on it in the subscriber
- A3-1375 — common.conf: use the common `kafka-custom-task.conf`?
- A3-1376 — InstrumentMarketDataEventProcessor.scala: Just thinking out loud… if we plan to migrate to use Kafka for all events in this processor, do we maybe want to use TopicProducer instead?
- A3-1379 — InstrumentMarketDataEventProcessor.scala: I mean the Lagom broker dsl TopicProducer
- R-3317 — Not Kibana. These Kamon metrics will be collected by Prometheus, and made available in Grafana You still need to build your Grafana dashboard / alert to vi
- R-3318 — Not compliance. Shall we make this a parameter and set by looking up `silver.service.name` instead?
- R-3319 — `StatementDataGenerator` knows nothing about Kafka… I’d prefer to keep the exception in the service domain.. and we add a predicate to the kafka helper, so
- R-3320 — FYI this one uses Cassandra repository with IN clause. Not sure if anyone would create a FundSmart goal with 25 instruments though
- R-3336 — PlanTimeSeriesSubscriber: proposed mapAsync(1) without throttle before finding the unawaited simulation
- R-3337 — safeRenewProjectionForCustomer is started with a value binding and not awaited
- R-3338 — Decouple MV draining from simulation with a separate retry/throttle/conflate topic proposal
- R-3358 — It should throw `TopicExistsException` as usual. Increasing partitions needs to be called via `adminClient.createPartions` And decreasing partitions is not
- R-3365 — If topic is not available yet, `UnknownTopicOrPartitionException` will be throw when we call `adminClient#alterConfigs` ‌ `UnknownTopicOrPartitionException
- R-3366 — The newer API for this is `incrementalAlterConfigs` which is only applicable for Kafka broker v2.3.0 onwards Our Kafka brokers are on v2.0.0
- R-3376 — At some point, I guess we should split PlanProfile out of Entity. Local cache built from Kafka should just be updated directly, no need to maintain event t
- R-3379 — Message ordering needs the partition key and sequential processing within that partition
- R-3380 — Question: use goalId to preserve ordering between goal and plan messages
- R-3381 — Looking at the consumers of this topic, looks like we want only instrumentId as partition key
- R-3382 — Why do we need this extra field?
- R-3383 — Yeah I guess this won’t matter too much then. Kafka partition key does not have to be at the most granular level - i.e. we don’t have to use entity id alwa
- R-3384 — This is another example of not using most granular level as partition key. Using goalId as partition key, all messages \(goal \+ plans\) will be sent in sa
- R-3385 — Of course, all plans under same goal will have same goalId
- R-3413 — Yep, dynamic env is not on dedicated Confluent Cloud cluster, hence auto topic creation is disabled. Other dev/staging/prod envs are using self-managed Kaf
- R-3423 — Yep, `RedemptionRequestWaitingForFeeChargeMsg` only arrived after when `ConfirmSettlementCmdHandler` handled the order\(s\) confirm settlement
- R-3424 — Replayed fee must match the already charged period; conflicting extra fee needs investigation
- R-3425 — Only dynamic environment needs this as of now I tested in `dev` and the topic is auto created by Kafka broker
- R-3475 — Initial proposal keeps old Plan writes while a separate new Plan processor populates V1
- R-3478 — Initial processor split is withdrawn so Goal and Plan update together for consistency
- R-3488 — Don’t we need to deploy goal first to create the topic?
- R-3501 — Proposal to recover force-rebalance failure after successful TAA update because a later topic message can trigger rebalance
- R-3533 — That’s right, but event processor would still retry \(and fail\) until all pods are successfully deployed.
- R-3550 — Just to confirm, here we set this to be explicit, but we have been using the default value \(all\) already? i.e. no actual change
- R-3552 — Kafka producer default assumption is corrected by akka-client override behavior
- R-3554 — We don’t need this? As parallelism is local to mapAsync only
- R-3560 — Question… do we need to change the consumer group / reset current group’s offset so that we re-process the kafka messages again? Or is there a way to re-pu
- R-3578 — Hmm.. this `event` is used as `event.Tag.forEntityId(entityId).tag` which refer to this singleton ``` object CustomerTransactionManagerEvt { val NumShards 

## Full source cases

## A1-1295 — Consider internal repartitioned Kafka topic rather than sequential DB locking

**Source stance:** open-question

**Context:**

> component: timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/logic/marketdata/impl/MarketDataLock.scala; operation: [NE-356] (timeseries) add locking support for marketdata processing; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Lock throw restarts subscription and rebalances all instances; DB lock loses graceful backpressure

**Source-preserving request, proposal, or question:**

> Inside we call lockOnce which will throw if unable to lock. We might change to some other flavour of locking method to enable retry etc, but eventually it will still throw. This will propagate the exception to the caller. If caller is akka projection / kafka subscriber, we would then restart the event by tag query / consumer subscription.
> 
> In your use case, it would be kafka consumer. And restarting a consumer in our current usage would cause a partition rebalance across all instances too.
> 
> Current approach \+ this new impl still restrict us to process everything sequentially. With db lock, we somewhat lost the graceful backpressure too. Have we considered using some sort of “internal” Kafka topic within timeseries that we rewrite the message’s partition key to ensure the messages in the sequence that we can control?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1310 · comment 712357504 · PR 12875 · 2025-11-11

Source path: `timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/logic/marketdata/impl/MarketDataLock.scala`

**Explicit source context (pr_title):**

> [NE-356] (timeseries) add locking support for marketdata processing

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

## A2-0236 — InvestmentPlanTableV8: This index is too much I would think. So most of the use cases of recurring investment, I think index on the `NextUpcomingDate` is sufficient. Other condi...

**Source stance:** suggestion

**Context:**

> PR 10251 (Resolve INV-3613: Goal/investment ceate new read side tables), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentPlanTableV8.scala; original row 236.

**Concern stated in the source:** NextUpcomingDate is considered sufficient indexing for recurring investment use cases; other filters can stream/process in memory.

**Source-preserving request, proposal, or question:**

> This index is too much I would think. So most of the use cases of recurring investment, I think index on the `NextUpcomingDate` is sufficient. Other condition, I feel we can just stream and process in stream/memory. No need to expose other columns here

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:236 · comment 560694743 · PR 10251 · 2024-11-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentPlanTableV8.scala`

**Evidence:** anon-2.jsonl:236 · comment 560694743 · PR 10251 · 2024-11-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentPlanTableV8.scala`

**Explicit source context (pr_title):**

> Resolve INV-3613: Goal/investment ceate new read side tables

## A2-0250 — package: Let’s keep this for now, but looks like if we ever add another type of feeConfig that does not have exact feeRate, it would be responsibility of charge svc to understan...

**Source stance:** suggestion

**Context:**

> PR 10425 ([INV-3508] Add goal flow advisory logic), goal-api/src/main/scala/com/endowus/silver/goal/api/models/plan/package.scala; original row 250.

**Concern stated in the source:** Future fee configs may lack an exact feeRate and need interpretation inside charge service.

**Source-preserving request, proposal, or question:**

> Let’s keep this for now, but looks like if we ever add another type of feeConfig that does not have exact feeRate, it would be responsibility of charge svc to understand this sealed trait and handle accordingly \(rather than upstream resolving the fee rate and charge purely do the maths that could have been static utils\)

**Conditions and limits:**

- Existing behavior may remain for now; future feeConfig interpretation belongs in charge.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:250 · comment 570872893 · PR 10425 · 2024-11-27

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/models/plan/package.scala`

**Evidence:** anon-2.jsonl:250 · comment 570872893 · PR 10425 · 2024-11-27

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/models/plan/package.scala`

**Explicit source context (pr_title):**

> [INV-3508] Add goal flow advisory logic

## A2-0259 — Review: RBAC validation previously failed because ResourceAction.newInstance(resource) defaulted resourceId to `_NEW_` while CheckResult lookup used resource kind. After resourc...

**Source stance:** reported-verification

**Context:**

> PR 10536 ([INV-3751] feat(bff): Set+Matching using resourceId), no inline path; original row 259.

**Concern stated in the source:** ResourceAction.newInstance defaulted resourceId to _NEW_ while CheckResult lookup used resource kind, causing validation failure.

**Source-preserving request, proposal, or question:**

> RBAC validation previously failed because ResourceAction.newInstance(resource) defaulted resourceId to `_NEW_` while CheckResult lookup used resource kind. After resourceId matching changes, the reported positive CREATE CUSTOMER:GOAL case allows the FA roles; removing FINANCIAL_ADVISOR_AGENT gives the negative EFFECT_DENY case.

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:259 · comment 573158087 · PR 10536 · 2024-12-03

> Before resourceId is defaulted to `_NEW_` by `ResourceAction.newInstance(resource)`
> 
> RBAC validation always fail, since we use resource kind when we lookup CheckResult

**Evidence:** anon-2.jsonl:259 · comment 573158087 · PR 10536 · 2024-12-03

> After it works as expected.

**Evidence:** anon-2.jsonl:259 · comment 573158087 · PR 10536 · 2024-12-03

> Positive case:

**Evidence:** anon-2.jsonl:259 · comment 573158087 · PR 10536 · 2024-12-03

> "id": "_NEW_"

**Evidence:** anon-2.jsonl:259 · comment 573158087 · PR 10536 · 2024-12-03

> "resourceId": "_NEW_"

**Evidence:** anon-2.jsonl:259 · comment 573158087 · PR 10536 · 2024-12-03

> "kind": "CUSTOMER:GOAL"

**Evidence:** anon-2.jsonl:259 · comment 573158087 · PR 10536 · 2024-12-03

> "FINANCIAL_ADVISOR_AGENT"

**Evidence:** anon-2.jsonl:259 · comment 573158087 · PR 10536 · 2024-12-03

> "FINANCIAL_ADVISOR_MANAGER"

**Evidence:** anon-2.jsonl:259 · comment 573158087 · PR 10536 · 2024-12-03

> "effect": "EFFECT_ALLOW"

**Evidence:** anon-2.jsonl:259 · comment 573158087 · PR 10536 · 2024-12-03

> Remove the role for negative case

**Evidence:** anon-2.jsonl:259 · comment 573158087 · PR 10536 · 2024-12-03

> "effect": "EFFECT_DENY"

**Evidence:** anon-2.jsonl:259 · comment 573158087 · PR 10536 · 2024-12-03

**Explicit source context (pr_title):**

> [INV-3751] feat(bff): Set+Matching using resourceId

## A2-0320 — MarketDataUploader: Let’s use `runWithReporting` which gives some utility around logging / allowing to capture individual error and move on instead of blocking the stream

**Source stance:** requested-change

**Context:**

> PR 10400 ([INV-3609] feat(marketdata, instrument): improve marketdata monthly changes reliability), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 320.

**Concern stated in the source:** runWithReporting can capture a per-item error and continue the stream.

**Source-preserving request, proposal, or question:**

> Let’s use `runWithReporting` which gives some utility around logging / allowing to capture individual error and move on instead of blocking the stream

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:320 · comment 568223418 · PR 10400 · 2024-11-20

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:320 · comment 568223418 · PR 10400 · 2024-11-20

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-3609] feat(marketdata, instrument): improve marketdata monthly changes reliability

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

## A2-0414 — BaseAdvisoryServiceE4s: Should we create another API object for all these tenant specific endpoints? Their logic should extract the tenant from tracing context, and use it for c...

**Source stance:** suggestion

**Context:**

> PR 10182 ([INV-3430] feat(bff, advisory): Portfolio Builder Fund List), advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala; original row 414.

**Concern stated in the source:** Tenant-specific APIs can use tenant tracing context after BFF auth/RBAC; faId is unnecessary until any future FA-specific RF need.

**Source-preserving request, proposal, or question:**

> Should we create another API object for all these tenant specific endpoints? Their logic should extract the tenant from tracing context, and use it for corp profile lookup.
> 
> This means for now, we do not need to have `faId` in the query params. On BFF, it would be an authenticated proxy endpoints with appropriate RBAC resource. Once that passes, `advisory` just need to proceed with the tenantId.
> 
> In future, if we ever need to support fa specific RF, an optional `faId` can be added?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:414 · comment 558075298 · PR 10182 · 2024-10-28

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Evidence:** anon-2.jsonl:414 · comment 558075298 · PR 10182 · 2024-10-28

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Explicit source context (pr_title):**

> [INV-3430] feat(bff, advisory): Portfolio Builder Fund List

## A2-0423 — SgInstrumentFilterManager: With this structure, `getInstrumentsAndFiltersForCustomer` and `getInstrumentsAndFiltersForTenantFa` can be used directly in the upstream manager

**Source stance:** suggestion

**Context:**

> PR 10182 ([INV-3430] feat(bff, advisory): Portfolio Builder Fund List), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgInstrumentFilterManager.scala; original row 423.

**Source-preserving request, proposal, or question:**

> With this structure, `getInstrumentsAndFiltersForCustomer` and `getInstrumentsAndFiltersForTenantFa` can be used directly in the upstream manager

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:423 · comment 561783944 · PR 10182 · 2024-11-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgInstrumentFilterManager.scala`

**Evidence:** anon-2.jsonl:423 · comment 561783944 · PR 10182 · 2024-11-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgInstrumentFilterManager.scala`

**Explicit source context (pr_title):**

> [INV-3430] feat(bff, advisory): Portfolio Builder Fund List

## A2-0441 — InvestorTypeFixForNonSgdInstrumentWithCpfAndSrs: better to use `Source(instrumentsToUpdate).mapAsync(...)` so that we can control the parallelism

**Source stance:** requested-change

**Context:**

> PR 9436 ([INV-3011] feat(instrument): fix wrong investor type mapping with instrument (cpf and srs)), amend-scripts/src/main/scala/instrument/InvestorTypeFixForNonSgdInstrumentWithCpfAndSrs.scala; original row 441.

**Concern stated in the source:** Source.mapAsync allows controlled parallelism.

**Source-preserving request, proposal, or question:**

> better to use `Source(instrumentsToUpdate).mapAsync(...)` so that we can control the parallelism

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:441 · comment 513369127 · PR 9436 · 2024-06-25

Source path: `amend-scripts/src/main/scala/instrument/InvestorTypeFixForNonSgdInstrumentWithCpfAndSrs.scala`

**Evidence:** anon-2.jsonl:441 · comment 513369127 · PR 9436 · 2024-06-25

Source path: `amend-scripts/src/main/scala/instrument/InvestorTypeFixForNonSgdInstrumentWithCpfAndSrs.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(instrument): fix wrong investor type mapping with instrument (cpf and srs)

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

## A2-0742 — InstrumentMonthlyChangesJdbcRepository: Maybe rename:

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala; original row 742.

**Source-preserving request, proposal, or question:**

> Maybe rename:
> 
> * `UpdatedInstrumentMonthlyChangesPortfolio` as `PortfolioIdWithCcy`
> * `streamUpdatedInstrumentMonthlyChangesFrom` as `streamPortfoliosHavingUpdatedInstrumentMonthlyChanges`
> * `instrumentMonthlyChangesUpdatedAt` as `instrumentMonthlyChangesUpdatedFrom`
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:742 · comment 531597177 · PR 9603 · 2024-08-16

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala`

**Evidence:** anon-2.jsonl:742 · comment 531597177 · PR 9603 · 2024-08-16

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

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

## A2-0801 — ServiceLogicImpl: Maybe source the instruments and flatMapConCat inside to avoid bloating the memory here

**Source stance:** suggestion

**Context:**

> PR 9689 (Feat/INV-3361 instrument price monthly changes jdbc migration), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; original row 801.

**Concern stated in the source:** Maybe source the instruments and flatMapConCat inside to avoid bloating the memory here

**Source-preserving request, proposal, or question:**

> Maybe source the instruments and flatMapConCat inside to avoid bloating the memory here

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:801 · comment 528901287 · PR 9689 · 2024-08-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:801 · comment 528901287 · PR 9689 · 2024-08-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

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

## A2-0821 — ProductPortfolioRepository: Maybe we can keep this method generic, but only handle for CoreEnhanced for now…

**Source stance:** suggestion

**Context:**

> PR 9605 ([INV-3236] feat(advisory): create advisory endpoints for goal create), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala; original row 821.

**Concern stated in the source:** Maybe we can keep this method generic, but only handle for CoreEnhanced for now…

```
def findProductPortfolio(
  advisoryTag: AdvisoryTag,
  riskTarget: ModelPortfolioRiskTarget,
  tradingAccountType: TradingAccountType
): Future[ProductPortfolio] = {
  findAllActiveForAdvisoryTag(advisoryTag)
    .filter(p => filterForTradingAccountType(advisoryTag, tradingAccountType, p))
    .filter(p => filterForRiskTarget(advisoryTag, riskTarget, p))
    .runWith(Sink.headOption)
    .flatMap({
      case Some(productPortfolio) => Future.successful(productPortfolio)
      case None =>
        Future
          .failed(BadRequest(s"Unable to find $advisoryTag portfolio for trading account $tradingAccountType with risk target of $riskTarget"))
    })
}

private def filterForRiskTarget(advisoryTag: AdvisoryTag, riskTarget: ModelPortfolioRiskTarget, p: ProductPortfolio): Boolean = {
  advisoryTag match {
    case AdvisoryTag.CORE_ENHANCED =>
      ProductPortfolio.extractCoreEnhancedMetaData(p).exists(_.riskTarget == riskTarget)
    case _ => false
  }
}
```

‌

I want to keep the method signature as close to the lookup by targetStockRatio one so it’s easier to switch later for Flagship/Esg/Factors/FlagshipDpm

**Source-preserving request, proposal, or question:**

> Maybe we can keep this method generic, but only handle for CoreEnhanced for now…
> 
> ```
> def findProductPortfolio(
>   advisoryTag: AdvisoryTag,
>   riskTarget: ModelPortfolioRiskTarget,
>   tradingAccountType: TradingAccountType
> ): Future[ProductPortfolio] = {
>   findAllActiveForAdvisoryTag(advisoryTag)
>     .filter(p => filterForTradingAccountType(advisoryTag, tradingAccountType, p))
>     .filter(p => filterForRiskTarget(advisoryTag, riskTarget, p))
>     .runWith(Sink.headOption)
>     .flatMap({
>       case Some(productPortfolio) => Future.successful(productPortfolio)
>       case None =>
>         Future
>           .failed(BadRequest(s"Unable to find $advisoryTag portfolio for trading account $tradingAccountType with risk target of $riskTarget"))
>     })
> }
> 
> private def filterForRiskTarget(advisoryTag: AdvisoryTag, riskTarget: ModelPortfolioRiskTarget, p: ProductPortfolio): Boolean = {
>   advisoryTag match {
>     case AdvisoryTag.CORE_ENHANCED =>
>       ProductPortfolio.extractCoreEnhancedMetaData(p).exists(_.riskTarget == riskTarget)
>     case _ => false
>   }
> }
> ```
> 
> ‌
> 
> I want to keep the method signature as close to the lookup by targetStockRatio one so it’s easier to switch later for Flagship/Esg/Factors/FlagshipDpm

**Conditions and limits:**

- Initial proposed generic signature handles only CoreEnhanced and otherwise returns false; row 837 proposes completing other productlines via ProductPortfolio.riskTarget.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:821 · comment 523845974 · PR 9605 · 2024-07-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala`

**Evidence:** anon-2.jsonl:821 · comment 523845974 · PR 9605 · 2024-07-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala`

**Explicit source context (pr_title):**

> [INV-3236] feat(advisory): create advisory endpoints for goal create

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

## A2-1116 — RecurringInvestmentProcessor: You can import OptionUtils and use onNone and make this a bit nicer… also better to extract schedule here, so that we don’t have to blindly call ge...

**Source stance:** suggestion

**Context:**

> PR 9091 ([EN-3271] Add autofx recurring support in investment), investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala; original row 1116.

**Concern stated in the source:** You can import OptionUtils and use onNone and make this a bit nicer… also better to extract schedule here, so that we don’t have to blindly call get later

```
.map { investmentPlan =>
  investmentPlan.recurringInvestmentSchedule
    .onNone(logger.error("blah"))
    .map((investmentPlan, _))
    .toList
}
.flatMapConcat(Source(_))
```

‌

**Source-preserving request, proposal, or question:**

> You can import OptionUtils and use onNone and make this a bit nicer… also better to extract schedule here, so that we don’t have to blindly call get later
> 
> ```
> .map { investmentPlan =>
>   investmentPlan.recurringInvestmentSchedule
>     .onNone(logger.error("blah"))
>     .map((investmentPlan, _))
>     .toList
> }
> .flatMapConcat(Source(_))
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1116 · comment 505575550 · PR 9091 · 2024-05-29

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Evidence:** anon-2.jsonl:1116 · comment 505575550 · PR 9091 · 2024-05-29

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (pr_title):**

> [EN-3271] Add autofx recurring support in investment

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

## A2-1197 — InstrumentExportScheduler: You can just batch it here

**Source stance:** suggestion

**Context:**

> PR 9073 (TT-4242 Automate export of Broker transactions for alts), broker-impl/src/main/scala/com/endowus/silver/broker/impl/utils/exportscheduler/InstrumentExportScheduler.scala; original row 1197.

**Concern stated in the source:** You can just batch it here

```
Source(instruments)
  .grouped(10)
  .map(_.toSet)
  .mapAsync(2) { instrumentIds =>
    instrumentSvc.getInstrumentV2ByIds(instrumentIds.mkString(",")).invoke().map(_.toList)
  }
  .flatMapConcat(Source(_))
  .runWith(Sink.seq)
```

‌

**Source-preserving request, proposal, or question:**

> You can just batch it here
> 
> ```
> Source(instruments)
>   .grouped(10)
>   .map(_.toSet)
>   .mapAsync(2) { instrumentIds =>
>     instrumentSvc.getInstrumentV2ByIds(instrumentIds.mkString(",")).invoke().map(_.toList)
>   }
>   .flatMapConcat(Source(_))
>   .runWith(Sink.seq)
> ```
> 
> ‌

**Conditions and limits:**

- Exact batching proposal: grouped(10), toSet, mapAsync(2), getInstrumentV2ByIds comma list, flatMapConcat, Sink.seq.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1197 · comment 500780169 · PR 9073 · 2024-05-14

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/utils/exportscheduler/InstrumentExportScheduler.scala`

**Evidence:** anon-2.jsonl:1197 · comment 500780169 · PR 9073 · 2024-05-14

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/utils/exportscheduler/InstrumentExportScheduler.scala`

**Explicit source context (pr_title):**

> TT-4242 Automate export of Broker transactions for alts

## A2-1229 — HkComplianceHelperImpl: mapAsync\(2\)

**Source stance:** suggestion

**Context:**

> PR 9082 (Feat/INV-2598 duplicate goal name handling), goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/hk/HkComplianceHelperImpl.scala; original row 1229.

**Source-preserving request, proposal, or question:**

> mapAsync\(2\)

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Source requests mapAsync(2) specifically in HkComplianceHelperImpl; do not apply it to ordered same-partition Kafka subscribers.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1229 · comment 498860347 · PR 9082 · 2024-05-07

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/hk/HkComplianceHelperImpl.scala`

**Evidence:** anon-2.jsonl:1229 · comment 498860347 · PR 9082 · 2024-05-07

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/hk/HkComplianceHelperImpl.scala`

**Explicit source context (hunk):**

>  import scala.collection.immutable
>  import scala.concurrent.{ExecutionContext, Future}
>  
> -class HkComplianceValidatorImpl(val complianceService: HkComplianceService)(
> +class HkComplianceHelperImpl(val complianceService: HkComplianceService)(
>    implicit val ec: ExecutionContext,
>    val mat: Materializer,

**Evidence:** anon-2.jsonl:1229 · comment 498860347 · PR 9082 · 2024-05-07

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/hk/HkComplianceHelperImpl.scala`

**Explicit source context (pr_title):**

> Feat/INV-2598 duplicate goal name handling

## A2-1324 — EdgeWarningAndRestrictionQueryLogic: If no remote calls, no need to use multiple threads for this. It should be fast enough with normal `.map`. No need akka stream as well

**Source stance:** suggestion

**Context:**

> PR 9009 (Feat/INV-2972 dpm blocked edge endpoint), compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeWarningAndRestrictionQueryLogic.scala; original row 1324.

**Source-preserving request, proposal, or question:**

> If no remote calls, no need to use multiple threads for this. It should be fast enough with normal `.map`. No need akka stream as well

**Conditions and limits:**

- With no remote calls, normal map is considered sufficient; threads/streams add no benefit in this local operation.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1324 · comment 496508214 · PR 9009 · 2024-04-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeWarningAndRestrictionQueryLogic.scala`

**Evidence:** anon-2.jsonl:1324 · comment 496508214 · PR 9009 · 2024-04-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeWarningAndRestrictionQueryLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-2972 dpm blocked edge endpoint

## A2-1366 — MarketDataUploader: Nit: no need to start a Source from beginning I think

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1366.

**Concern stated in the source:** Nit: no need to start a Source from beginning I think

```
for {
  instruments <- instrumentIds match {
    ...
  }
  _ <- Source(instruments)
    .filter(... check pricing source)
    .mapAsync(...)
    .run() // consider using SourceUtils.RunWithReportingExt (it has some basic logging for progress/completion)
} yield Done
```

‌

**Source-preserving request, proposal, or question:**

> Nit: no need to start a Source from beginning I think
> 
> ```
> for {
>   instruments <- instrumentIds match {
>     ...
>   }
>   _ <- Source(instruments)
>     .filter(... check pricing source)
>     .mapAsync(...)
>     .run() // consider using SourceUtils.RunWithReportingExt (it has some basic logging for progress/completion)
> } yield Done
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1366 · comment 494946679 · PR 8931 · 2024-04-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1366 · comment 494946679 · PR 8931 · 2024-04-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1367 — MarketDataUploader: If we propagate the failure in these places, it will stop the whole flow processing. I suppose we just want to skip?

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1367.

**Concern stated in the source:** If we propagate the failure in these places, it will stop the whole flow processing. I suppose we just want to skip?

If we use `runWithReporting`, we can potentially write sth like this

```
Source(instrument)
  .mapAsync(parallelism) { instrument =>
    reconcilePrices(instrument) // extract this whole pricing fetching + compare into a method
      .map(_ => Right(Done))
      .recover {
        case ex =>
          logger.error("meaningful log message", ex)
          Left(instrument.id)
      }
  }
  .runWithReporting("meaningful context")
```

‌

**Source-preserving request, proposal, or question:**

> If we propagate the failure in these places, it will stop the whole flow processing. I suppose we just want to skip?
> 
> If we use `runWithReporting`, we can potentially write sth like this
> 
> ```
> Source(instrument)
>   .mapAsync(parallelism) { instrument =>
>     reconcilePrices(instrument) // extract this whole pricing fetching + compare into a method
>       .map(_ => Right(Done))
>       .recover {
>         case ex =>
>           logger.error("meaningful log message", ex)
>           Left(instrument.id)
>       }
>   }
>   .runWithReporting("meaningful context")
> ```
> 
> ‌

**Conditions and limits:**

- Per-instrument failures should produce Left(instrument.id) and continue under runWithReporting, rather than fail whole reconciliation.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1367 · comment 494949025 · PR 8931 · 2024-04-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1367 · comment 494949025 · PR 8931 · 2024-04-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

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

## A2-1593 — package: FYI [person] , [person] will create another set of `FundingInstructions` that is more suitable for upstream of investment svc… particularly, there will be no `fxConvers...

**Source stance:** suggestion

**Context:**

> PR 7947 (TT-3480 Add funding instructions to investment request), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/ces/commands/package.scala; original row 1593.

**Concern stated in the source:** FYI [person] , [person] will create another set of `FundingInstructions` that is more suitable for upstream of investment svc… particularly, there will be no `fxConversionRequestId` field.

**Source-preserving request, proposal, or question:**

> FYI [person] , [person] will create another set of `FundingInstructions` that is more suitable for upstream of investment svc… particularly, there will be no `fxConversionRequestId` field.

**Conditions and limits:**

- The upstream FundingInstructions variant excludes fxConversionRequestId, unlike the downstream investment-service model.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1593 · comment 478122302 · PR 7947 · 2024-03-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/ces/commands/package.scala`

> FYI

**Evidence:** anon-2.jsonl:1593 · comment 478122302 · PR 7947 · 2024-03-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/ces/commands/package.scala`

> ,

**Evidence:** anon-2.jsonl:1593 · comment 478122302 · PR 7947 · 2024-03-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/ces/commands/package.scala`

> will create another set of `FundingInstructions` that is more suitable for upstream of investment svc… particularly, there will be no `fxConversionRequestId` field.

**Evidence:** anon-2.jsonl:1593 · comment 478122302 · PR 7947 · 2024-03-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/ces/commands/package.scala`

**Explicit source context (pr_title):**

> TT-3480 Add funding instructions to investment request

## A2-1612 — RebateDistributionCommunicationsManager: Just Source and mapAsync these

**Source stance:** suggestion

**Context:**

> PR 8353 (Feat/INV-1996/automate trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala; original row 1612.

**Source-preserving request, proposal, or question:**

> Just Source and mapAsync these

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1612 · comment 476109463 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala`

**Evidence:** anon-2.jsonl:1612 · comment 476109463 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala`

**Explicit source context (hunk):**

> +          val mandatoryAltRebateInstruments = brokerRebates.flatMap(rebate => {
> +            altsRebatesMap
> +              .get(rebate.instrumentId)
> +              .flatMap(altsMandatoryRebate => instrumentMap.get(altsMandatoryRebate.instrumentId))
> +              .map { instrumentInfo =>
> +                MandatoryAltRebateInstrumentEmailView(
> +                  instrumentId = instrumentInfo.id,

**Evidence:** anon-2.jsonl:1612 · comment 476109463 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala`

**Explicit source context (pr_title):**

> Feat/INV-1996/automate trailer rebate

## A2-1616 — RebateDistributionCommunicationsManager: We will put all these data in memory, and it will only grow. Better to aggregate the data as part of the processing stream

**Source stance:** explanation

**Context:**

> PR 8353 (Feat/INV-1996/automate trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala; original row 1616.

**Concern stated in the source:** We will put all these data in memory, and it will only grow. Better to aggregate the data as part of the processing stream

**Source-preserving request, proposal, or question:**

> We will put all these data in memory, and it will only grow. Better to aggregate the data as part of the processing stream

**Conditions and limits:**

- Aggregating whole growing dataset in memory should be replaced with stream-stage aggregation.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1616 · comment 478114078 · PR 8353 · 2024-03-04

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala`

**Evidence:** anon-2.jsonl:1616 · comment 478114078 · PR 8353 · 2024-03-04

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala`

**Explicit source context (pr_title):**

> Feat/INV-1996/automate trailer rebate

## A2-1619 — RebateDistributionCommunicationsManager: Just Source the `customerRebates` and mapAsync to lookup instruments

**Source stance:** suggestion

**Context:**

> PR 8353 (Feat/INV-1996/automate trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala; original row 1619.

**Source-preserving request, proposal, or question:**

> Just Source the `customerRebates` and mapAsync to lookup instruments

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1619 · comment 478115107 · PR 8353 · 2024-03-04

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala`

**Evidence:** anon-2.jsonl:1619 · comment 478115107 · PR 8353 · 2024-03-04

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala`

**Explicit source context (pr_title):**

> Feat/INV-1996/automate trailer rebate

## A2-1731 — SgFundSmartManagerV3: At this point we don’t have any remote calls anymore, can do mapAsync\(4\) I think

**Source stance:** suggestion

**Context:**

> PR 7719 (Resolve INV-2348: support bulk look up of performance), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala; original row 1731.

**Source-preserving request, proposal, or question:**

> At this point we don’t have any remote calls anymore, can do mapAsync\(4\) I think

**Conditions and limits:**

- mapAsync(4) suggestion applies after no remote calls remain, distinct from ordered Kafka subscriber parallelism limits.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1731 · comment 451514621 · PR 7719 · 2023-12-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala`

**Evidence:** anon-2.jsonl:1731 · comment 451514621 · PR 7719 · 2023-12-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala`

**Explicit source context (pr_title):**

> Resolve INV-2348: support bulk look up of performance

## A3-0055 — PortfolioOfferingResponseV2 sealed-trait concern and product-specific MAA card flow

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgAdvisedPortfolioMaaManager.scala; PR: Feat/INV-634/migrate refactor maa endpoints

**Source-preserving request, proposal, or question:**

> Not sure if it’s worth adding this sealed trait `PortfolioOfferingResponseV2` just for this purpose or not. We also go against the common pattern of sealed trait, in which we just use it for pattern matching, but data sent back in endpoints is still specific type.
> 
> 
> 
> I feel splitting code like below is still ok
> 
> ```
> def getMaaCards(productLine, tradingAccountType, displayCcy) = {
>   productLine match {
>     case Flagship => getFlagshipMaaCards(tradingAccountType, displayCcy)
>     ...
>   }
> }
> 
> def getFlagshipMaaCards(tradingAccountType, displayCcy) = {
>   for {
>     portfolioOfferings <- getFlagshipOfferings(Some(accountType))
>     cards <- Source(portfolioOfferings.toList)
>       .mapAsync(2) { portfolioOffering =>
>         maaAdditionalDetailsCache.get(portfolioOffering.portfolioId, portfolioOffering.effectiveDate, displayCcy)
>           .map { case (performance, composition) =>
>             PortfolioMaaCard.fromFlagshipPortfolioOffering(...)
>           }
>       }
>       .runWith(Sink.seq)
>       .map(_.toList)
>   } yields cards
> }
> 
> def getEsgMaaCards / getIncomeMaaCards / etc.
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1868 · comment 438181785 · PR 7274 · 2023-10-23

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgAdvisedPortfolioMaaManager.scala`

> Not sure if it’s worth adding this sealed trait `PortfolioOfferingResponseV2` just for this purpose or not. We also go against the common pattern of sealed trait, in which we just use it for pattern matching, but data sent back in endpoints is still specific type.
> 
> ‌
> 
> I feel splitting code like below is still ok
> 
> ```
> def getMaaCards(productLine, tradingAccountType, displayCcy) = {
>   productLine match {
>     case Flagship => getFlagshipMaaCards(tradingAccountType, displayCcy)
>     ...
>   }
> }
> 
> def getFlagshipMaaCards(tradingAccountType, displayCcy) = {
>   for {
>     portfolioOfferings <- getFlagshipOfferings(Some(accountType))
>     cards <- Source(portfolioOfferings.toList)
>       .mapAsync(2) { portfolioOffering =>
>         maaAdditionalDetailsCache.get(portfolioOffering.portfolioId, portfolioOffering.effectiveDate, displayCcy)
>           .map { case (performance, composition) =>
>             PortfolioMaaCard.fromFlagshipPortfolioOffering(...)
>           }
>       }
>       .runWith(Sink.seq)
>       .map(_.toList)
>   } yields cards
> }
> 
> def getEsgMaaCards / getIncomeMaaCards / etc.
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:1868 · comment 438181785 · PR 7274 · 2023-10-23

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgAdvisedPortfolioMaaManager.scala`

**Explicit source context (hunk):**

> +            response = portfolioOffering,
> +            underlyingPage = underlyingPage,
> +            performance = performance,
> +            displayCcy = displayCcy
> +          )
> +        }
> +        }.runWith(Sink.seq).map(s => s.toList)

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

## A3-0058 — DividendTopicSubscriberV3.scala: The problem with this is it’s a bit harder to unit test just the logic, cuz you will need to mock the topic.subscriber chain We can potentially add a 

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala; PR: Feat/INV-1972 v3 transaction subscriber

**Concern stated in the source:** The problem with this is it’s a bit harder to unit test just the logic, cuz you will need to mock the topic.subscriber chain

**Source-preserving request, proposal, or question:**

> The problem with this is it’s a bit harder to unit test just the logic, cuz you will need to mock the topic.subscriber chain
> 
> We can potentially add a `start` method to make it lazy, and only call it in Application class, similar to `SubscriberMetricsWithKamon`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1872 · comment 439563077 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1872 · comment 439563077 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Explicit source context (hunk):**

> +import scala.concurrent.{ExecutionContext, Future}
> +
> +class DividendTopicSubscriberV3(
> +  dividendService: DividendService,
> +  dateTimeProvider: DateTimeProvider,
> +  refProvider: PersistentEntityRefProvider
> +)(

## A3-0059 — DividendTopicSubscriberV3.scala: Existing code even in v1, but why would this need force…

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala; PR: Feat/INV-1972 v3 transaction subscriber

**Source-preserving request, proposal, or question:**

> Existing code even in v1, but why would this need force…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 1873, 1880: Force-update question has later comment request; deleted-then-redistributed justification appears in1880 hunk and is context-only.

**Evidence:** anon-2.jsonl:1873 · comment 439563823 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1873 · comment 439563823 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Explicit source context (hunk):**

> +    )
> +
> +    //Force updating here since it's possible for a dividend distribution to be deleted then redistributed
> +    refProvider.getTransactionV3EntityRef(tx.id).ask(UpdateTransactionCmd(_, tx, forceUpdate = true))
> +  }
> +
> +  def handleDividendReinvestmentRequestedMsg(msg: DividendReinvestmentRequestedMsg): Future[Done] = {

## A3-0060 — DividendTopicSubscriberV3.scala: Confirm defined for SG? If yes, let’s remove this to avoid confusion

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala; PR: Feat/INV-1972 v3 transaction subscriber

**Source-preserving request, proposal, or question:**

> Confirm defined for SG? If yes, let’s remove this to avoid confusion

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1874 · comment 439565002 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1874 · comment 439565002 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Explicit source context (hunk):**

> +      settledAt = msg.settledAt,
> +      settledPrice = msg.price,
> +      settledDate = msg.settlementDate.get,
> +      contractDate = msg.contractDate,
> +      settledPriceDate = msg.priceDate.get,
> +      isAssumed = true
> +    )

## A3-0061 — DividendTopicSubscriberV3.scala: late but why do we even need this wrapper? Just mark Transaction with `PlayJsonSerializable`?

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala; PR: Feat/INV-1972 v3 transaction subscriber

**Source-preserving request, proposal, or question:**

> Maybe late but why do we even need this wrapper? Just mark Transaction with `PlayJsonSerializable`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1876 · comment 439566198 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1876 · comment 439566198 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Explicit source context (hunk):**

> +      tx <- refProvider
> +        .getTransactionV3EntityRef(transactionId)
> +        .ask(GetTransactionCmd(_))
> +        .map(_.transaction)
> +      distributionTx = tx match {
> +        case t: DistributionTransaction => t
> +        case _ => throw new Exception(s"Transaction [${getTransactionId(msg.dividendId)}] is not of the type [$DIVIDEND_RECEIVED]..")

## A3-0062 — InvestmentRequestTopicSubscriberV3.scala: Should be able to remove this throttle?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala; PR: Feat/INV-1972 v3 transaction subscriber

**Source-preserving request, proposal, or question:**

> Should be able to remove this throttle?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1877 · comment 439569394 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1877 · comment 439569394 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Explicit source context (hunk):**

> +    .subscribe
> +    .withGroupId(groupId)
> +    .atLeastOnce(Flow[InvestmentRequestMsg]
> +    .mapAsync(parallelism = 1) {
> +      case msg: InvestmentRequestedMsg if isNotDividendReinvestment(msg.request.reason) =>
> +        val request = msg.request
> +        logMessage(msg, request.investmentRequestId)

## A3-0063 — RedemptionRequestTopicSubscriberV3.scala: This should be confirmed

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala; PR: Feat/INV-1972 v3 transaction subscriber

**Source-preserving request, proposal, or question:**

> This should be confirmed

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1878 · comment 439573483 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1878 · comment 439573483 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Explicit source context (hunk):**

> +      val request = msg.request
> +      logMessage(msg, request.redemptionRequestId)
> +      validateRequestStatus(RedemptionRequestStatus.COMPLETED, request.status)
> +      val confirmedOrdersStatusDetails = ConfirmedOrdersStatusDetails(
> +        transactionStatus = TransactionStatus.SETTLEMENT_CONFIRMED,
> +        confirmedAmount = request.settlementConfirmation.map(_.tradeSettlementConfirmAmount).getOrElse({
> +          logger.warn(s"Redemption ${request.redemptionRequestId} has no settlement confirmation, defaulting to requested amount")

## A3-0064 — DividendTopicSubscriberV3.scala: but you will need to mock the whole chain… doable but just boiler plate ``` dividendService .dividendTopic .subscribe .withGroupId(groupId) .atLeastOn

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala; PR: Feat/INV-1972 v3 transaction subscriber

**Source-preserving request, proposal, or question:**

> Yes but you will need to mock the whole chain… doable but just boiler plate
> 
> ```
> dividendService
>     .dividendTopic
>     .subscribe
>     .withGroupId(groupId)
>     .atLeastOnce
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1879 · comment 439593281 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

> Yes but you will need to mock the whole chain… doable but just boiler plate
> 
> ```
> dividendService
>     .dividendTopic
>     .subscribe
>     .withGroupId(groupId)
>     .atLeastOnce
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:1879 · comment 439593281 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Explicit source context (hunk):**

> +import scala.concurrent.{ExecutionContext, Future}
> +
> +class DividendTopicSubscriberV3(
> +  dividendService: DividendService,
> +  dateTimeProvider: DateTimeProvider,
> +  refProvider: PersistentEntityRefProvider
> +)(

## A3-0065 — Dividend forceUpdate comment: deletion then redistribution context

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala; PR: Feat/INV-1972 v3 transaction subscriber

**Concern stated in the source:** Let’s put a comment for this, cuz I think it’s not obvious from subscriber code

**Source-preserving request, proposal, or question:**

> Nice good catch. Let’s put a comment for this, cuz I think it’s not obvious from subscriber code

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 1873, 1880: Force-update question has later comment request; deleted-then-redistributed justification appears in1880 hunk and is context-only.

**Evidence:** anon-2.jsonl:1880 · comment 440194921 · PR 7303 · 2023-10-30

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1880 · comment 440194921 · PR 7303 · 2023-10-30

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Explicit source context (hunk):**

> +    )
> +
> +    //Force updating here since it's possible for a dividend distribution to be deleted then redistributed
> +    refProvider.getTransactionV3EntityRef(tx.id).ask(UpdateTransactionCmd(_, tx, forceUpdate = true))
> +  }
> +
> +  def handleDividendReinvestmentRequestedMsg(msg: DividendReinvestmentRequestedMsg): Future[Done] = {

## A3-0071 — ServiceLogicImplV2.scala: This one is old code, but I think better to mapAsync so that we can control the parallelism instead of blind run with throttle… we can ignore the resu

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImplV2.scala; PR: Resolve INV-2049: New instrument events, event handlers, v2 logic split.

**Concern stated in the source:** This one is old code, but I think better to mapAsync so that we can control the parallelism instead of blind run with throttle… we can ignore the result Future easily afterwards

**Source-preserving request, proposal, or question:**

> This one is old code, but I think better to mapAsync so that we can control the parallelism instead of blind run with throttle… we can ignore the result Future easily afterwards

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1887 · comment 437292455 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImplV2.scala`

**Evidence:** anon-2.jsonl:1887 · comment 437292455 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImplV2.scala`

**Explicit source context (hunk):**

> +
> +      // Fire and forget as caller doesn't need to wait for everything to be successful
> +      _ <- Source(instruments)
> +        .throttle(2, 250.millisecond, 1, ThrottleMode.Shaping)
> +        .mapAsync(parallelism = 1) { instrument =>
> +          instrumentEntity.ref(instrument.id).ask(PublishInstrumentCmd(_))
> +        }

## A3-0107 — Quarterly fee estimate avoids Kafka task: no OOMKilled and idle partition/consumer cost

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeEstimateNotificationManager.scala; PR: [INV-2016] feat(communication)(charge): Email notification for estimated upcoming quarterly charge (support only NonAlts for now)

**Source-preserving request, proposal, or question:**

> Not using Kafka task for this, for now:
> 
> * we don’t have OOMKilled problem, and this process should be fast to complete
> * we only have this exercise once a quarter, so it’s wasteful to have kafka topic created \(charged per partitions\) and idle kafka consumers

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1924 · comment 433289502 · PR 7106 · 2023-10-05

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeEstimateNotificationManager.scala`

> Not using Kafka task for this, for now:
> 
> * we don’t have OOMKilled problem, and this process should be fast to complete
> * we only have this exercise once a quarter, so it’s wasteful to have kafka topic created \(charged per partitions\) and idle kafka consumers
> 
> ‌

**Evidence:** anon-2.jsonl:1924 · comment 433289502 · PR 7106 · 2023-10-05

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeEstimateNotificationManager.scala`

**Explicit source context (hunk):**

> +          chargeDate = chargeDate,
> +          forceResend = request.forceResend
> +        )
> +        sendCustomerFeeEstimateNotification(customerRequest, simulateOnly = None)
> +          .map(_ => Right(Done))
> +          .recover {
> +            case ex =>

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

## A3-0233 — PlanRecurringInvestmentScheduleExpiringDailyTriggerTopicProducerDirect.scala: name this `GoalKafkaTaskTopicProducerDirect` and just put all the task topics here. Name gets too long..

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/task/producer/PlanRecurringInvestmentScheduleExpiringDailyTriggerTopicProducerDirect.scala; PR: [EN-1992] Add support for recurring investment expiring communications

**Source-preserving request, proposal, or question:**

> Let’s name this `GoalKafkaTaskTopicProducerDirect` and just put all the task topics here. Name gets too long..

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2056 · comment 424828578 · PR 6715 · 2023-09-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/task/producer/PlanRecurringInvestmentScheduleExpiringDailyTriggerTopicProducerDirect.scala`

## A3-0234 — Goal/plan-not-found handler exception can poison task topic

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala; PR: [EN-1992] Add support for recurring investment expiring communications

**Concern stated in the source:** Nit: We should handle exception here otherwise it will stuck and block other messages, e.g.

**Source-preserving request, proposal, or question:**

> Nit: We should handle exception here otherwise it will stuck and block other messages, e.g. what if goal/plan not found?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2057 · comment 424829389 · PR 6715 · 2023-09-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala`

**Evidence:** anon-2.jsonl:2057 · comment 424829389 · PR 6715 · 2023-09-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala`

**Explicit source context (hunk):**

> +          )
> +          Done
> +        }
> +    }
> +  }
> +
> +  def publishDailyPlanRecurringInvestmentScheduleExpiredTriggerMsg(overrideExecuteDate: Option[LocalDate]): Future[Done] = {

## A3-0235 — Expiring-schedule Kafka lag/replay must not notify a replacement schedule

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala; PR: [EN-1992] Add support for recurring investment expiring communications

**Source-preserving request, proposal, or question:**

> Should we validate if schedule is still expiring here, before sending comm? In case the we kafka messages got stuck too long / replayed somehow, and queried plan here actually has another schedule?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2058 · comment 424829675 · PR 6715 · 2023-09-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala`

**Evidence:** anon-2.jsonl:2058 · comment 424829675 · PR 6715 · 2023-09-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala`

**Explicit source context (hunk):**

> +
> +  def publishDailyPlanRecurringInvestmentScheduleExpiredTriggerMsg(overrideExecuteDate: Option[LocalDate]): Future[Done] = {
> +    val executeDate = overrideExecuteDate.getOrElse(dateTimeProvider.localDateNow)
> +
> +    logger.logTime(s"streaming expired recurring investment schedules") {
> +      planRecurringInvestmentScheduleJdbcRepository
> +        .streamRecurringInvestmentSchedulesByExpiredOnDate(

## A3-0237 — package.scala: No need sealed trait if we are using separate topic per msg type

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/task/package.scala; PR: [EN-1992] Add support for recurring investment expiring communications

**Source-preserving request, proposal, or question:**

> No need sealed trait if we are using separate topic per msg type

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2060 · comment 424831046 · PR 6715 · 2023-09-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/task/package.scala`

**Evidence:** anon-2.jsonl:2060 · comment 424831046 · PR 6715 · 2023-09-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/task/package.scala`

**Explicit source context (hunk):**

> +
> +package object task {
> +
> +  sealed trait PlanRecurringInvestmentScheduleDailyTriggerMsg {
> +    def goalId: UUID
> +    def planId: UUID
> +    def schedule: RecurringTransactionSchedule

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

## A3-0286 — EndowusKafkaConfig.scala: consumer

**Source stance:** requested-change

**Context:**

> lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusKafkaConfig.scala; PR: Support Kafka Migration

**Source-preserving request, proposal, or question:**

> Nit: consumer

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2111 · comment 421518992 · PR 6565 · 2023-08-23

Source path: `lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusKafkaConfig.scala`

**Evidence:** anon-2.jsonl:2111 · comment 421518992 · PR 6565 · 2023-08-23

Source path: `lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusKafkaConfig.scala`

**Explicit source context (hunk):**

> +  }
> +
> +  def consumerConfig(config: Config): KafkaConfig = {
> +    // get the base broker configuration, then enrich it with the consumer endpoints
> +    val consumerBrokerConfig = withEndpoints(config, getEndpoints(config, "consumer"))
> +    KafkaConfig(consumerBrokerConfig)
> +  }

## A3-0287 — EndowusTopicConsumerMetrics.scala: ~~Should we capture this on producer side instead?~~ We already captured this on producer side. Our kafka topics are all internal, so in theory, produ

**Source stance:** explanation

**Context:**

> lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusTopicConsumerMetrics.scala; PR: Support Kafka Migration

**Source-preserving request, proposal, or question:**

> ~~Should we capture this on producer side instead?~~
> 
> We already captured this on producer side. Our kafka topics are all internal, so in theory, producer side is enough.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Producer-side question is struck through; revised source says internal topics already capture the metric there.

**Evidence:** anon-2.jsonl:2112 · comment 421519272 · PR 6565 · 2023-08-23

Source path: `lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusTopicConsumerMetrics.scala`

**Evidence:** anon-2.jsonl:2112 · comment 421519272 · PR 6565 · 2023-08-23

Source path: `lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusTopicConsumerMetrics.scala`

**Explicit source context (hunk):**

> +}
> +
> +case class EndowusTopicConsumerMetrics[Payload](metricsPrefix: String, groupId: String, maxMessageBytes: Int) {
> +
> +  private val consumedMessagesCount = Kamon.counter(
> +    s"${metricsPrefix}_msg",
> +    "Number of messages consumed by this consumer"

## A3-0288 — EndowusTopicConsumerMetrics.scala: consumer. Same for below

**Source stance:** requested-change

**Context:**

> lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusTopicConsumerMetrics.scala; PR: Support Kafka Migration

**Source-preserving request, proposal, or question:**

> Nit: consumer. Same for below

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2113 · comment 421519555 · PR 6565 · 2023-08-23

Source path: `lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusTopicConsumerMetrics.scala`

**Evidence:** anon-2.jsonl:2113 · comment 421519555 · PR 6565 · 2023-08-23

Source path: `lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusTopicConsumerMetrics.scala`

**Explicit source context (hunk):**

> +  private val msgSizeGauge = Kamon.gauge(
> +    s"${metricsPrefix}_last_msg_size",
> +    "The size of the last message consumed in bytes",
> +    MeasurementUnit.information.bytes
> +  )
> +  // histogram with a minimum value of 2 bytes (denotes the json {})
> +  // with maximum value as the maxMessageBytes configured for the consumer client

## A3-0289 — kafka.conf: Do we set topic level config `max.message.bytes` or broker level config `message.max.bytes`?

**Source stance:** open-question

**Context:**

> conf-reference/src/main/resources/kafka/kafka.conf; PR: Support Kafka Migration

**Source-preserving request, proposal, or question:**

> Do we set topic level config `max.message.bytes` or broker level config `message.max.bytes`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2114 · comment 421521383 · PR 6565 · 2023-08-23

Source path: `conf-reference/src/main/resources/kafka/kafka.conf`

**Evidence:** anon-2.jsonl:2114 · comment 421521383 · PR 6565 · 2023-08-23

Source path: `conf-reference/src/main/resources/kafka/kafka.conf`

**Explicit source context (hunk):**

> # Properties for akka.kafka.ProducerSettings
> -  max.request.size = 10000000
> +  # this is the max that confluent based kafka clusters can use
> +  max.request.size = 8000000
> +  # this should never be > 8000000
>    max.request.size = ${?KAFKA_PRODUCERS_MAX_SIZE_BYTES}
>    # Pick a safe default value so messages don't get lost after they've been acknowledged. Unfortunately `akka-clients` picked a less safe default.

## A3-0290 — ConsumerTopicFactory.scala: The fact that we’re using producer config here means this msg size metric should really be on producer side no? :stuck_out_tongue:

**Source stance:** open-question

**Context:**

> lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/ConsumerTopicFactory.scala; PR: Support Kafka Migration

**Source-preserving request, proposal, or question:**

> The fact that we’re using producer config here means this msg size metric should really be on producer side no? :stuck_out_tongue:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2115 · comment 421521678 · PR 6565 · 2023-08-23

Source path: `lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/ConsumerTopicFactory.scala`

**Evidence:** anon-2.jsonl:2115 · comment 421521678 · PR 6565 · 2023-08-23

Source path: `lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/ConsumerTopicFactory.scala`

**Explicit source context (hunk):**

> +
> +  // we use 10mb here because this is the max configured value for our kafka brokers
> +  // this is only used for bucketing the histogram metrics
> +  private val MaxMessageBytes = 10000000
> +
> +  override def subscribe: Subscriber[Message] =
> +    new ScaladslKafkaSubscriber[Message, Message](

## A3-0291 — EndowusTopicProducers.scala: `max.request.size`?

**Source stance:** open-question

**Context:**

> lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusTopicProducers.scala; PR: Support Kafka Migration

**Source-preserving request, proposal, or question:**

> `max.request.size`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2116 · comment 421521743 · PR 6565 · 2023-08-23

Source path: `lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusTopicProducers.scala`

**Evidence:** anon-2.jsonl:2116 · comment 421521743 · PR 6565 · 2023-08-23

Source path: `lagom-kafka/src/main/scala/com/lightbend/lagom/scaladsl/broker/kafka/endowus/EndowusTopicProducers.scala`

**Explicit source context (hunk):**

> +  // implementation. We can only change the source of the config, which at least we can enrich
> +  // takes the value of the brokers from the producer config if it exists, otherwise, on the configured lagom.broker.kafka.brokers
> +  private val producerKafkaConfig = EndowusKafkaConfig.producerConfig(actorSystem.settings.config)
> +  // we use 10mb here because this is the max configured value for our kafka brokers
> +  // this is only used for bucketing the histogram metrics
> +  private val MaxMessageBytes = 10000000
> +

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

## A3-0294 — kafka.conf: [<url> data-inline-card='' } Default is 2MB, can be overridden up to 8MB, but we would need to override ourselves if we want higher

**Source stance:** explanation

**Context:**

> conf-reference/src/main/resources/kafka/kafka.conf; PR: Support Kafka Migration

**Source-preserving request, proposal, or question:**

> [<url> data-inline-card='' } 
> 
> Default is 2MB, can be overridden up to 8MB, but we would need to override ourselves if we want higher

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Numeric configuration statement: default 2MB, override to 8MB, higher requires own override. Redacted linked source is not independently checked.

**Evidence:** anon-2.jsonl:2119 · comment 421854171 · PR 6565 · 2023-08-24

Source path: `conf-reference/src/main/resources/kafka/kafka.conf`

**Evidence:** anon-2.jsonl:2119 · comment 421854171 · PR 6565 · 2023-08-24

Source path: `conf-reference/src/main/resources/kafka/kafka.conf`

**Explicit source context (hunk):**

> # Properties for akka.kafka.ProducerSettings
> -  max.request.size = 10000000
> +  # this is the max that confluent based kafka clusters can use
> +  max.request.size = 8000000
> +  # this should never be > 8000000
>    max.request.size = ${?KAFKA_PRODUCERS_MAX_SIZE_BYTES}
>    # Pick a safe default value so messages don't get lost after they've been acknowledged. Unfortunately `akka-clients` picked a less safe default.

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

## A3-0420 — Risk-target performance example uses mapAsync2 over risks and mapAsync1 over plans

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala; PR: Feat/INV-1633/goal perf across risk targets

**Source-preserving request, proposal, or question:**

> I give it a go…
> 
> ```
> riskTargetPerformanceMetricsMap <- Source(riskTargets)
>   .mapAsync(2) { riskTarget =>
>     val riskToleranceLevel = RiskToleranceUtils.riskToleranceLevelForUsage(riskTarget)
>     val targetStockRatio = RiskToleranceUtils.mapToTargetStockRatioForGeneralInvesting(riskToleranceLevel).getOrElse(...)
>     for {
>       planRiskTargetPortfolioTaaMap <- Source(validPlans)
>         .mapAsync(1) { plan =>
>           lookupProductPortfolioTaa(advisoryTag, targetStockRatio, plan.tradingAccountType).map(plan.planId -> _)
>         }
>         .runWith(Sink.seq)
>         .map(_.toMap)
> 
>       riskTargetGoalTaa = generateCombinedTaa(planMarketValues, planRiskTargetPortfolioTaaMap)
> 
>       performanceMetrics <- getPerformanceMetrics(taa = riskTargetGoalTaa, ccy = planCcy, period = PerformanceMetricsPeriodEnum.COMMON)
>         .map(response => response.performanceMetrics)
>     } yield riskTarget -> performanceMetrics
>   }
>   .runWith(Sink.seq)
>   .map(_.toMap)
> 
> goalRiskTarget = ModelPortfolioRiskTarget.calculateRiskTargetFromStockRatio(goal.targetStockRatio)
> goalPerformanceMetrics = riskTargetPerformanceMetricsMap.find(goalRiskTarget).getOrElse(...)
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve nested mapAsync parallelism 2 over riskTargets and 1 over validPlans, risk ratio mapping, common-period performance, and goal risk lookup.

**Evidence:** anon-2.jsonl:2250 · comment 411332427 · PR 6389 · 2023-07-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

> I give it a go…
> 
> ```
> riskTargetPerformanceMetricsMap <- Source(riskTargets)
>   .mapAsync(2) { riskTarget =>
>     val riskToleranceLevel = RiskToleranceUtils.riskToleranceLevelForUsage(riskTarget)
>     val targetStockRatio = RiskToleranceUtils.mapToTargetStockRatioForGeneralInvesting(riskToleranceLevel).getOrElse(...)
>     for {
>       planRiskTargetPortfolioTaaMap <- Source(validPlans)
>         .mapAsync(1) { plan =>
>           lookupProductPortfolioTaa(advisoryTag, targetStockRatio, plan.tradingAccountType).map(plan.planId -> _)
>         }
>         .runWith(Sink.seq)
>         .map(_.toMap)
> 
>       riskTargetGoalTaa = generateCombinedTaa(planMarketValues, planRiskTargetPortfolioTaaMap)
> 
>       performanceMetrics <- getPerformanceMetrics(taa = riskTargetGoalTaa, ccy = planCcy, period = PerformanceMetricsPeriodEnum.COMMON)
>         .map(response => response.performanceMetrics)
>     } yield riskTarget -> performanceMetrics
>   }
>   .runWith(Sink.seq)
>   .map(_.toMap)
> 
> goalRiskTarget = ModelPortfolioRiskTarget.calculateRiskTargetFromStockRatio(goal.targetStockRatio)
> goalPerformanceMetrics = riskTargetPerformanceMetricsMap.find(goalRiskTarget).getOrElse(...)
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2250 · comment 411332427 · PR 6389 · 2023-07-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +          )
> +        advisoryTag = getAdvisoryTagFromProductLineAndIntent(product = productLineAndIntent)
> +        riskTargetPerformanceMetricsMap <- Source(riskTargets)
> +          .mapAsync(2) { riskTarget =>
> +            val riskToleranceLevel = RiskToleranceUtils.riskToleranceLevelForUsage(riskTarget)
> +            val targetStockRatio = RiskToleranceUtils.mapToTargetStockRatioForGeneralInvesting(riskToleranceLevel)
> +              .getOrElse(throw BadRequest(

## A3-0499 — services.list: And you would need to release all services listening to redemption topic.

**Source stance:** requested-change

**Context:**

> kubernetes/services.list; PR: Feat/INV-1710 redemption transaction backfill absrobed

**Source-preserving request, proposal, or question:**

> And you would need to release all services listening to redemption topic.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2335 · comment 409097373 · PR 6357 · 2023-07-06

Source path: `kubernetes/services.list`

**Evidence:** anon-2.jsonl:2335 · comment 409097373 · PR 6357 · 2023-07-06

Source path: `kubernetes/services.list`

**Explicit source context (hunk):**

> -charge redemption voucher
> +charge redemption voucher transaction trading 
> \ No newline at end of file

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

## A3-0598 — BrokerAccountTopicSubscriberHandlers.scala: If we rethrow here, and it’s not transient error… the subscriber will get stuck

**Source stance:** observed-defect

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/BrokerAccountTopicSubscriberHandlers.scala; PR: Feat/EN-982 migrate one time platform notification

**Concern stated in the source:** If we rethrow here, and it’s not transient error… the subscriber will get stuck

**Source-preserving request, proposal, or question:**

> If we rethrow here, and it’s not transient error… the subscriber will get stuck

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2445 · comment 398911839 · PR 5862 · 2023-05-30

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/BrokerAccountTopicSubscriberHandlers.scala`

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

## A3-0642 — : Will trading release this for HK too? If yes, we would need to handle in V2 entity?

**Source stance:** open-question

**Context:**

> None; PR: [INV-1438] feat(transaction): Listen to trading messages for asset_transfer

**Source-preserving request, proposal, or question:**

> Will trading release this for HK too? If yes, we would need to handle in V2 entity?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2491 · comment 391965757 · PR 5918 · 2023-05-05

## A3-0643 — : AFAICS, trading add this new topic `InvestmentTransferTopic` to BaseTradingService… so ideally we should handle for both region You can discuss this w

**Source stance:** explanation

**Context:**

> None; PR: [INV-1438] feat(transaction): Listen to trading messages for asset_transfer

**Source-preserving request, proposal, or question:**

> AFAICS, trading add this new topic `InvestmentTransferTopic` to BaseTradingService… so ideally we should handle for both region
> 
> You can discuss this with trading team to confirm

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2492 · comment 391966217 · PR 5918 · 2023-05-05

## A3-0644 — HK investment-transfer handler deferred under coordinated blocked rollout

**Source stance:** suggestion

**Context:**

> None; PR: [INV-1438] feat(transaction): Listen to trading messages for asset_transfer

**Source-preserving request, proposal, or question:**

> Nah it’s ok. As long as it’s blocked, and will be a coordinated effort to roll out in HK, we don’t need to add

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Coordinated HK-blocked rollout justifies not adding handling yet, revising preceding both-region query.

**Evidence:** anon-2.jsonl:2493 · comment 391966951 · PR 5918 · 2023-05-05

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

## A3-0702 — PortfolioVersionUpgradeRebalanceRequestsGenerator.scala: Good point. Added the runFold back

**Source stance:** explanation

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala; PR: feat(rebalance): RPC improvements

**Source-preserving request, proposal, or question:**

> Good point. Added the runFold back

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2553 · comment 388288323 · PR 5776 · 2023-04-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala`

**Evidence:** anon-2.jsonl:2553 · comment 388288323 · PR 5776 · 2023-04-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala`

**Explicit source context (hunk):**

> -                  skippedCountForExistentRequest,
> -                  failedCount
> -                  ) if result.proceed =>
> +        .runFold((0L, 0L, Map.empty[SkippedReason, Long])) {
> +          case ((totalCount, successfulCount, skippedReasonBreakdown), result) =>
> +            result match {
> +              case Left(skippedReason) =>

## A3-0707 — : Kafka [ProducerConfig](<url> is now logged :stuck_out_tongue: ``` batch.size = 16384 linger.ms = 0 ``` I think we will need to at least setting non-ze

**Source stance:** suggestion

**Context:**

> None; PR: PLATFORM-823 Set Kafka producer messages batch compression

**Source-preserving request, proposal, or question:**

> Kafka [ProducerConfig](<url> is now logged :stuck_out_tongue: 
> 
> ```
> batch.size = 16384
> linger.ms = 0
> ```
> 
> I think we will need to at least setting non-zero for linger time for batching to kick in

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Producer defaults batch.size16384 and linger.ms0; nonzero linger proposed for batching.

**Evidence:** anon-2.jsonl:2558 · comment 387645610 · PR 5772 · 2023-04-18

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

## A3-0724 — Kafka logger override in conf-reference, then Vault/config-map per-service level

**Source stance:** suggestion

**Context:**

> report-impl/src/main/resources/logback.xml; PR: [EN-1248] chore(report): custom log config

**Source-preserving request, proposal, or question:**

> If it’s urgent, I guess we can go ahead with this change for now. However, the better way I think is to change the logback.xml in conf-reference instead
> 
> 
> 
> You can make this override-able by:
> 
> ```
> <logger name="org.apache.kafka" level="${org.apache.kafka.log.level:-WARN}"/>
> ```
> 
> 
> 
> Then in the service you want to override, provide the custom log config as
> 
> ```
> <included>
>   <property name="org.apache.kafka.log.level" value="INFO" />
> </included>
> ```
> 
>   
> This custom file will then be set in Vault in old SG setup, or mount via some config-map in the new kustomize setup

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Urgent local change tolerated; preferred conf-reference override org.apache.kafka.log.level defaultWARN, per-serviceINFO via Vault/config-map.

**Evidence:** anon-2.jsonl:2576 · comment 384897580 · PR 5640 · 2023-04-06

Source path: `report-impl/src/main/resources/logback.xml`

> If it’s urgent, I guess we can go ahead with this change for now. However, the better way I think is to change the logback.xml in conf-reference instead
> 
> ‌
> 
> You can make this override-able by:
> 
> ```
> <logger name="org.apache.kafka" level="${org.apache.kafka.log.level:-WARN}"/>
> ```
> 
> ‌
> 
> Then in the service you want to override, provide the custom log config as
> 
> ```
> <included>
>   <property name="org.apache.kafka.log.level" value="INFO" />
> </included>
> ```
> 
>   
> This custom file will then be set in Vault in old SG setup, or mount via some config-map in the new kustomize setup

**Evidence:** anon-2.jsonl:2576 · comment 384897580 · PR 5640 · 2023-04-06

Source path: `report-impl/src/main/resources/logback.xml`

**Explicit source context (hunk):**

> +    <logger name="org.apache.cassandra" level="ERROR"/>
> +    <logger name="com.datastax.driver" level="ERROR"/>
> +
> +    <logger name="org.apache.kafka" level="INFO"/>
> +
> +    <logger name="com.endowus" level="INFO"/>
> +

## A3-0726 — Referral SG-only investment-topic subscriber requires separate SG/HK release tags

**Source stance:** suggestion

**Context:**

> kubernetes/services.list; PR: [INV-1361] feat(investment)(redemption)(rebalance)(transaction): Consume order level assumed settlement msg and update trade request + transaction accordingly

**Concern stated in the source:** Ok we need `referral` here too because it also subscribes to investment topic.

**Source-preserving request, proposal, or question:**

> Ok we need `referral` here too because it also subscribes to investment topic. However it is not deployed in HK. So maybe we do 2 tags, first one is this PR to both SG and HK, and second one containing only services.list with referral to SG only

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2578 · comment 383716505 · PR 5651 · 2023-04-03

Source path: `kubernetes/services.list`

**Evidence:** anon-2.jsonl:2578 · comment 383716505 · PR 5651 · 2023-04-03

Source path: `kubernetes/services.list`

**Explicit source context (hunk):**

> -advisory charge transaction
> \ No newline at end of file
> +advisory charge communication compliance dividend goal investment projection rebalance redemption referral trading transaction
> \ No newline at end of file

## A3-0728 — UpdateRebalanceRequestWithSettlementAssumedOrderCmdHandler.scala: Feels like concern of trading or even broker svc. The msg contract from trading svc has all these optional fields. Do we start logging for all of them

**Source stance:** open-question

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/UpdateRebalanceRequestWithSettlementAssumedOrderCmdHandler.scala; PR: [INV-1361] feat(investment)(redemption)(rebalance)(transaction): Consume order level assumed settlement msg and update trade request + transaction accordingly

**Source-preserving request, proposal, or question:**

> Feels like concern of trading or even broker svc. The msg contract from trading svc has all these optional fields. Do we start logging for all of them, e.g. settlement confirmed but missing confirmed fields etc?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2580 · comment 384589267 · PR 5651 · 2023-04-05

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/UpdateRebalanceRequestWithSettlementAssumedOrderCmdHandler.scala`

**Evidence:** anon-2.jsonl:2580 · comment 384589267 · PR 5651 · 2023-04-05

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/UpdateRebalanceRequestWithSettlementAssumedOrderCmdHandler.scala`

**Explicit source context (hunk):**

> +      .thenAck(cmd.replyTo)
> +  }
> +
> +  private def shouldIgnoreLateSettlementAssumedOrder(buySell: BuySell, status: RebalanceRequestStatus): Boolean = {
> +    buySell match {
> +      case BuySell.BUY =>
> +        status == RebalanceRequestStatus.REBALANCING_COMPLETED

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

## A3-0753 — SubscriberMetricsWithKamon.scala: even for Lagom-removed services today, we still use Lagom for kafka subscriber flow. This is added just to monitor the performance difference when we 

**Source stance:** explanation

**Context:**

> silver-commons/src/main/scala/com/endowus/silver/commons/kafka/SubscriberMetricsWithKamon.scala; PR: [INV-1151] feat(rebalance): Added logging and up the timeout to 30s

**Source-preserving request, proposal, or question:**

> Yeah even for Lagom-removed services today, we still use Lagom for kafka subscriber flow. This is added just to monitor the performance difference when we optimize the rebalance flow. We can revist the non-Lagom version when the time comes. This trait doesn’t do much, so should be able to support non-Lagom \(I think we might be even able to use the Kamon instrumentation for Kafka consumer\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2605 · comment 380344965 · PR 5524 · 2023-03-22

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/SubscriberMetricsWithKamon.scala`

**Evidence:** anon-2.jsonl:2605 · comment 380344965 · PR 5524 · 2023-03-22

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/SubscriberMetricsWithKamon.scala`

**Explicit source context (hunk):**

> + * and therefore not suitable for batch processing.
> + * @tparam Payload
> + */
> +trait SubscriberMetricsWithKamon[Payload]
> +  extends StrictLogging {
> +
> +  implicit val executionContext: ExecutionContext

## A3-0754 — SubscriberMetricsWithKamon.scala: The `kafka_consumergroup_group_lag_seconds` is estimated by the lag exporter using `endOffsets` and `listConsumerGroupOffsets` without actually consum

**Source stance:** explanation

**Context:**

> silver-commons/src/main/scala/com/endowus/silver/commons/kafka/SubscriberMetricsWithKamon.scala; PR: [INV-1151] feat(rebalance): Added logging and up the timeout to 30s

**Source-preserving request, proposal, or question:**

> The `kafka_consumergroup_group_lag_seconds` is estimated by the lag exporter using `endOffsets` and `listConsumerGroupOffsets` without actually consuming the messages. Here we already consume, and if would give a little more accurate metrics.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2606 · comment 380345381 · PR 5524 · 2023-03-22

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/SubscriberMetricsWithKamon.scala`

**Evidence:** anon-2.jsonl:2606 · comment 380345381 · PR 5524 · 2023-03-22

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/SubscriberMetricsWithKamon.scala`

**Explicit source context (hunk):**

> +
> +/**
> + * This trait will add metrics for the following
> + * - Inflight kafka message time until received by consumer (will be using kafka's timestamp metadata)
> + * - Processing metric for a single time
> + * - Logging received message key
> + *

## A3-0758 — Transaction FX conversion Futures: bounded Source.mapAsync2 proposed

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala; PR: Feat/INV-913 tech debt fx rates

**Source-preserving request, proposal, or question:**

> I’m a little skeptical with spawning all the futures at once here. We would be capped by the number of cores anyway. Maybe the usual Source\(transactions\).mapAsync\(2\) \{….\} ?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2610 · comment 370756717 · PR 5266 · 2023-02-17

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

**Evidence:** anon-2.jsonl:2610 · comment 370756717 · PR 5266 · 2023-02-17

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

**Explicit source context (hunk):**

> +        .runWith(Sink.seq)
> +        .map(_.toList)
>      }
>    }
>  
> -  private def fetchFxRatesAndRefreshCache(baseCcy: CurrencyUnit, quoteCcy: CurrencyUnit): Future[List[(LocalDate, BigDecimal)]] = {
> -    logger.info(s"fetchFxRatesAndRefreshCache started for [$baseCcy$quoteCcy]...")

## A3-0804 — SftpMetadataChecker.scala: Do we need to throttle and `parallelism` = 1? I think it’s ok to just query with `parallelism` = 2 without throttling here

**Source stance:** open-question

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala; PR: Feat/EN-870 sg auto generate report meta data

**Source-preserving request, proposal, or question:**

> Do we need to throttle and `parallelism` = 1? I think it’s ok to just query with `parallelism` = 2 without throttling here

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2659 · comment 379043482 · PR 5350 · 2023-03-17

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala`

**Evidence:** anon-2.jsonl:2659 · comment 379043482 · PR 5350 · 2023-03-17

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala`

**Explicit source context (hunk):**

> +        } yield info
> +      }
> +      .runWith(Sink.seq)
> +  }
> +
> +  private[sftp] def generateMessageCompareFileNamesInMetadataAndFilesInFolder(
> +    documentIdsInCsvFile: Seq[String],

## A3-0811 — AdvisedPortfolioOfferingsManager.scala: You can write this as ``` .mapAsyncUnordered(parallelism = 2) { case (portfolioId, effectiveDate) => ```

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/AdvisedPortfolioOfferingsManager.scala; PR: [INV-1116] feat(advisory, invest.20): Recommended core portfolios

**Source-preserving request, proposal, or question:**

> You can write this as
> 
> ```
> .mapAsyncUnordered(parallelism = 2) { case (portfolioId, effectiveDate) =>
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2666 · comment 373500037 · PR 5295 · 2023-02-28

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/AdvisedPortfolioOfferingsManager.scala`

> You can write this as
> 
> ```
> .mapAsyncUnordered(parallelism = 2) { case (portfolioId, effectiveDate) =>
> ```
> 
> ‌

## A3-0821 — Independent dividend files: BadRequest nonretry and bounded TCP/unknown retry

**Source stance:** explanation

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/subscribers/HongKongEntitlementDividendTopicSubscriber.scala; PR: TT-1732 change dividendTopic to dividendFileTopic

**Concern stated in the source:** Since we can’t reliably reproduce and fix them, we want to limit the number of retries to avoid blocking the whole topic.

**Source-preserving request, proposal, or question:**

> The ServiceLogic in dividend svc alreadymaps the scenarios it cannot handle the file to BadRequest. So we don’t want to waste time retrying for those case \(’s intention\).
> 
> There could potentially still be other exceptions that not caught by ServiceLogic itself, e.g. the case of big file and the tcp connection got cut during file processing. Since we can’t reliably reproduce and fix them, we want to limit the number of retries to avoid blocking the whole topic. Each dividend file should be independent, so we don’t care about their ordering \(unlike events in other normal topic subscribers\).
> 
> I updated the PR to reflect this change :pray:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- BadRequest is intentionally non-retry; other file/TCP failures get bounded retries because dividend files are independent and whole-topic blocking is worse.

**Evidence:** anon-2.jsonl:2678 · comment 374518385 · PR 5391 · 2023-03-03

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/subscribers/HongKongEntitlementDividendTopicSubscriber.scala`

> The ServiceLogic in dividend svc alreadymaps the scenarios it cannot handle the file to BadRequest. So we don’t want to waste time retrying for those case \(

**Evidence:** anon-2.jsonl:2678 · comment 374518385 · PR 5391 · 2023-03-03

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/subscribers/HongKongEntitlementDividendTopicSubscriber.scala`

> ’s intention\).
> 
> There could potentially still be other exceptions that not caught by ServiceLogic itself, e.g. the case of big file and the tcp connection got cut during file processing. Since we can’t reliably reproduce and fix them, we want to limit the number of retries to avoid blocking the whole topic. Each dividend file should be independent, so we don’t care about their ordering \(unlike events in other normal topic subscribers\).
> 
> I updated the PR to reflect this change :pray: 
> 
> ‌

**Evidence:** anon-2.jsonl:2678 · comment 374518385 · PR 5391 · 2023-03-03

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/subscribers/HongKongEntitlementDividendTopicSubscriber.scala`

**Explicit source context (hunk):**

> +            msg.fileDetails match {
> +              case BucketBasedFileDetails(_, objectName) =>
> +                logic
> +                  .triggerProcessingOfDividendDistribution(ProcessDividendDistributionRequest(objectName))
> +                  .withRetry({
> +                    case _: BadRequest => false
> +                    case ex =>

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

## A3-0849 — NotificationManager.scala: You can do ``` .mapAsync(2) { case (customerData, profileData) => ... } ```

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala; PR: Resolve INV-896: Changes to publish email/platform notifs for upcoming customer vc warnings.

**Source-preserving request, proposal, or question:**

> You can do
> 
> ```
> .mapAsync(2) { case (customerData, profileData) =>
>   ...
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2707 · comment 372348538 · PR 5329 · 2023-02-23

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala`

> You can do
> 
> ```
> .mapAsync(2) { case (customerData, profileData) =>
>   ...
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2707 · comment 372348538 · PR 5329 · 2023-02-23

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala`

**Explicit source context (hunk):**

> +    val customersToNotify = customerProjectionDataJdbcRepository
> +      .findValidNonVCWithAdvisoryProfile(birthdaysBasedOnCutoffAge)
> +      .mapAsync(2) { case(customerData, profileData) =>
> +        profileData.advisoryProfile match {
> +          case NonVulnerableCustomerProfile(_, RiskProfileStatus.Valid, _, _) =>
> +            for {
> +              craSimulationResult <- simulateCraWithVcCutOffAge(customerData.customerId)

## A3-0854 — NotificationManager.scala: Then you can `.collect { case Some(customerData) => customerData }` to flatten the flow

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala; PR: Resolve INV-896: Changes to publish email/platform notifs for upcoming customer vc warnings.

**Source-preserving request, proposal, or question:**

> Then you can `.collect { case Some(customerData) => customerData }` to flatten the flow

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2712 · comment 372608592 · PR 5329 · 2023-02-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala`

**Evidence:** anon-2.jsonl:2712 · comment 372608592 · PR 5329 · 2023-02-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala`

**Explicit source context (hunk):**

> +      }}
> +      .collect {
> +        case Some(customerData) => customerData
> +      }
> +
> +    def sendUpcomingCustomerVCNotifications(data: CustomerProjectionData): Future[UUID] = {
> +      for {

## A3-0880 — FxRatesProjectionRepository.scala: If no streaming, then don’t need SlickSession I think

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/FxRatesProjectionRepository.scala; PR: Feat/INV-913 fx rates projection

**Source-preserving request, proposal, or question:**

> If no streaming, then don’t need SlickSession I think

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2739 · comment 354168399 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/FxRatesProjectionRepository.scala`

**Evidence:** anon-2.jsonl:2739 · comment 354168399 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/FxRatesProjectionRepository.scala`

**Explicit source context (hunk):**

> +
> +class FxRatesProjectionRepository (database: Database)(implicit ctx: ExecutionContext) {
> +
> +  private val fxRatesProjectionTable = TableQuery[FxRatesProjectionTable]
> +
> +  def findCcyPairRateByPriceDate(baseCcy: CurrencyUnit, quoteCcy: CurrencyUnit, priceDate: LocalDate): Future[Option[FxRateProjectionData]] = {
> +    database.run {

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

## A3-0906 — CRAExpiryDailyTriggerTopicProducerDirect.scala: Why do we partition using date? Wouldn’t that mean all messages of same trigger will go to only 1 instance?

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/task/hk/CRAExpiryDailyTriggerTopicProducerDirect.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Why do we partition using date? Wouldn’t that mean all messages of same trigger will go to only 1 instance?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2765 · comment 366323629 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/task/hk/CRAExpiryDailyTriggerTopicProducerDirect.scala`

**Evidence:** anon-2.jsonl:2765 · comment 366323629 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/task/hk/CRAExpiryDailyTriggerTopicProducerDirect.scala`

**Explicit source context (hunk):**

> +  }
> +}
> +
> +object CRAExpiryDailyTriggerTopicProducerDirect {
> +  val Partition: MsgPartitioning[CRAExpiryDailyTriggerMsg] = MsgPartitioning[CRAExpiryDailyTriggerMsg](_.customerId.toString)
> +}

## A3-0907 — CRAExpiryDailyTriggerTopicProducerDirect.scala: Oh this one is just to trigger the whole batch, not individual customer… Using one whole kafka topic for just 1 message a day seems a little overkille

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/task/hk/CRAExpiryDailyTriggerTopicProducerDirect.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Oh this one is just to trigger the whole batch, not individual customer… Using one whole kafka topic for just 1 message a day seems a little overkilled… I personally think we can just keep them in the REST endpoint itself… if the cron fails, we can raise alert and trigger again

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2766 · comment 366324068 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/task/hk/CRAExpiryDailyTriggerTopicProducerDirect.scala`

**Evidence:** anon-2.jsonl:2766 · comment 366324068 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/task/hk/CRAExpiryDailyTriggerTopicProducerDirect.scala`

**Explicit source context (hunk):**

> +  }
> +}
> +
> +object CRAExpiryDailyTriggerTopicProducerDirect {
> +  val Partition: MsgPartitioning[CRAExpiryDailyTriggerMsg] = MsgPartitioning[CRAExpiryDailyTriggerMsg](_.customerId.toString)
> +}

## A3-0908 — Daily cron queries eligible customers; customerId-keyed Kafka tasks process individually

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> This part, on the other hand, is good candidate to move to Kafka. So the idea is:
> 
> * the REST endpoint triggered via cron should query all eligible customers, for each dispatch a kafka task - keyed by customerId
> * a subscriber processing each customer independently to check and recalculate their status

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2767 · comment 366324376 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

> This part, on the other hand, is good candidate to move to Kafka. So the idea is:
> 
> * the REST endpoint triggered via cron should query all eligible customers, for each dispatch a kafka task - keyed by customerId
> * a subscriber processing each customer independently to check and recalculate their status
> 
> ‌

**Evidence:** anon-2.jsonl:2767 · comment 366324376 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +      }}
> +      .map(_._1)
> +      .mapAsync(2) { customerData =>
> +        vcStateChangeDailyTriggerTopicProducerDirect.publish(
> +          VCStateChangeDailyTriggerMsg(
> +            customerId = customerData.customerId,
> +            executeDate = executeDate,

## A3-0921 — CraManagerTest.scala: assert `vcStateChangeDailyTriggerTopicProducerDirect` not called?

**Source stance:** suggestion

**Context:**

> advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/hk/CraManagerTest.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Maybe assert `vcStateChangeDailyTriggerTopicProducerDirect` not called?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2780 · comment 367136755 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/hk/CraManagerTest.scala`

**Evidence:** anon-2.jsonl:2780 · comment 367136755 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/hk/CraManagerTest.scala`

**Explicit source context (hunk):**

> +        when(customerProjectionDataJdbcRepository.findNonVCWithMaybeAdvisoryProfile(currentDate(ZoneHongKong).minusYears(65)))
> +          .thenReturn(Source(List((customerProjectionData, Some(profileDataUpdated)))))
> +
> +        service.publishDailyCustomerVCTriggerMsg(Some(currentDate(ZoneHongKong))).map(res => {
> +          verify(vcStateChangeDailyTriggerTopicProducerDirect, times(0)).publish(any())
> +          res shouldBe akka.Done
> +        })

## A3-0924 — CraManager.scala: If we throw, we block Kafka..

**Source stance:** observed-defect

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> If we throw, we block Kafka..

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2783 · comment 367143068 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Evidence:** anon-2.jsonl:2783 · comment 367143068 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +              dob = dob,
> +              latestTS = latestTS,
> +              executeDate = executeDate
> +            )
> +            _ <- if (customerExceedVCGracePeriod && customerNotRetakenCRAAfterBirthday)
> +                reassessVulnerableStatus(customerId, "SYSTEM", "State Change VC Trigger")
> +              else

## A3-0931 — HkServiceLogicImpl.scala: Oh bulk upsert for whole set of customers would be too large… either batch the source, or just upsert one by one I think…

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Oh bulk upsert for whole set of customers would be too large… either batch the source, or just upsert one by one I think…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2790 · comment 367471398 · PR 5109 · 2023-02-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2790 · comment 367471398 · PR 5109 · 2023-02-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +              Future.successful(None)
> +          }
> +      }
> +      .grouped(10)
> +      .map(customers => customerProjectionDataJdbcDbHandler.bulkUpsert(customers.flatten))
> +      .runWith(Sink.ignore)
> +      .onComplete({

## A3-0932 — HkServiceLogicImpl.scala: I didn’t realize getPaginatedSource already concat all the page previously..

**Source stance:** explanation

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> I didn’t realize getPaginatedSource already concat all the page previously..

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2791 · comment 367471585 · PR 5109 · 2023-02-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2791 · comment 367471585 · PR 5109 · 2023-02-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +              Future.successful(None)
> +          }
> +      }
> +      .grouped(10)
> +      .map(customers => customerProjectionDataJdbcDbHandler.bulkUpsert(customers.flatten))
> +      .runWith(Sink.ignore)
> +      .onComplete({

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

## A3-0937 — PlanDividendDistributionTopicSubscriber.scala: for old flow, I keep them in SgDividendService

**Source stance:** explanation

**Context:**

> communication-impl/src/main/scala/com/endowus/silver/communication/impl/subscribers/PlanDividendDistributionTopicSubscriber.scala; PR: [INV-1096] feat(dividend)(admin,broker,communication,investment,timeseries,trading,transaction): Region split for Dividend svc

**Source-preserving request, proposal, or question:**

> Yeah for old flow, I keep them in SgDividendService

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2797 · comment 366004412 · PR 5136 · 2023-02-01

Source path: `communication-impl/src/main/scala/com/endowus/silver/communication/impl/subscribers/PlanDividendDistributionTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2797 · comment 366004412 · PR 5136 · 2023-02-01

Source path: `communication-impl/src/main/scala/com/endowus/silver/communication/impl/subscribers/PlanDividendDistributionTopicSubscriber.scala`

**Explicit source context (hunk):**

> class PlanDividendDistributionTopicSubscriber(
>    val refProvider: PersistentEntityRefProvider,
> -  dividendService: DividendService,
> +  dividendService: SgDividendService,
>    goalService: GoalService,
>    instrumentService: InstrumentService
>  )(implicit ec: ExecutionContext, mat: Materializer)

## A3-0993 — : can we also make sure the subscriber for new model doesn’t have the same bug? Then we can add services.list and release :thumbsup:

**Source stance:** requested-change

**Context:**

> None; PR: INV-654 Fix TradeTopicSubscriber.convertToSellOrder for assumedPrice

**Source-preserving request, proposal, or question:**

> can we also make sure the subscriber for new model doesn’t have the same bug? Then we can add services.list and release :thumbsup:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Related source row2854 corrects the affected service to redemption svc, not transaction svc. Keep this target correction when checking the new-model subscriber and services.list release.

**Evidence:** anon-2.jsonl:2853 · comment 348070050 · PR 4765 · 2022-11-23

> can we also make sure the subscriber for new model doesn’t have the same bug? Then we can add services.list and release :thumbsup: 
> 
> ‌

**Evidence:** anon-2.jsonl:2854 · comment 348072799 · PR 4765 · 2022-11-23

> Ah yeah my bad. It’s redemption svc, not transaction svc :pray: 

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

## A3-1117 — RebalanceApplication.scala: customer preference is not implemented in HK yet. So currently this just scream `UNKNOWN_TOPIC_OR_PARTITION` - I’ll remove the wiring for HK. Good cat

**Source stance:** requested-change

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala; PR: [INV-751] feat(investment)(redemption)(rebalance)(trading): Instrument tradability check + Basic region service split

**Source-preserving request, proposal, or question:**

> Yeah customer preference is not implemented in HK yet. So currently this just scream `UNKNOWN_TOPIC_OR_PARTITION`  - I’ll remove the wiring for HK. Good catch

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2988 · comment 343896073 · PR 4551 · 2022-11-08

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala`

**Evidence:** anon-2.jsonl:2988 · comment 343896073 · PR 4551 · 2022-11-08

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala`

**Explicit source context (hunk):**

> +}
> +
> +abstract class SgRebalanceApplication(context: LagomApplicationContext) extends BaseRebalanceApplication(context) with StrictLogging {
> +  lazy val lagomServer = serverFor[RebalanceService](wire[RebalanceServiceImpl])
> +
> +  lazy val tradabilityChecker: BaseTradabilityChecker = wire[SgTradabilityChecker]
> +

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

## A3-1248 — HkInvestmentTopicSubscriber.scala: `investmentRequestId` will always be available in Kafka messages from `investment` service - because they are materialized requests. You can see it is

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala; PR: Feat/INV-551 release earmark

**Concern stated in the source:** `investmentRequestId` will always be available in Kafka messages from `investment` service - because they are materialized requests.

**Source-preserving request, proposal, or question:**

> `investmentRequestId` will always be available in Kafka messages from `investment` service - because they are materialized requests. You can see it is required field in `InvestmentRequestDto`
> 
> 
> 
> Only way to distinguish the initial investment is by checking `InvestmentRequestDto#reason` I think

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3129 · comment 334801901 · PR 4377 · 2022-10-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala`

> `investmentRequestId` will always be available in Kafka messages from `investment` service - because they are materialized requests. You can see it is required field in `InvestmentRequestDto`
> 
> ‌
> 
> Only way to distinguish the initial investment is by checking `InvestmentRequestDto#reason` I think

**Evidence:** anon-2.jsonl:3129 · comment 334801901 · PR 4377 · 2022-10-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala`

**Explicit source context (hunk):**

> +
> +    case msg: InvestmentRequestRejectedMsg =>
> +      processEarmarkRelease(msg.customerId)(
> +        msg.goalId,
> +        msg.planId,
> +        msg.request.investmentRequestId,
> +        msg.request.reason,

## A3-1264 — Release-earmark subscriber serial1 is conservative preference, not required ordering proof

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala; PR: Feat/INV-551 release earmark

**Source-preserving request, proposal, or question:**

> In this subscriber, we only care to release earmark, and once released, we don’t care about it anymore. So parallelism here should be ok I think, but I guess to be on safe side \(since it won’t be significantly better anyway\), we can stick to processing 1 at a time

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Earmark-release subscriber ordering not semantically needed after release, but serial1 preferred conservatively for little performance benefit; do not generalize serial requirement.

**Evidence:** anon-2.jsonl:3145 · comment 335700694 · PR 4377 · 2022-10-06

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:3145 · comment 335700694 · PR 4377 · 2022-10-06

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala`

**Explicit source context (hunk):**

> +  implicit ec: ExecutionContext,
> +  mat: Materializer
> +) extends LazyLogging {
> +  investmentService.investmentRequestTopic.subscribe.atLeastOnce(Flow[InvestmentRequestMsg].mapAsync(parallelism = 1) {
> +    case msg: InvestmentRequestSubmittedExternallyMsg =>
> +      processEarmarkRelease(msg.customerId)(
> +        msg.goalId,

## A3-1268 — BrokerCashTransactionTopicSubscriberV2.scala: If we throw here, this subscriber will stuck on this message

**Source stance:** observed-defect

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV2.scala; PR: INV-553 feat: Deposit and InterestReceived Transaction Subscriber

**Concern stated in the source:** If we throw here, this subscriber will stuck on this message

**Source-preserving request, proposal, or question:**

> If we throw here, this subscriber will stuck on this message

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3149 · comment 334763362 · PR 4360 · 2022-10-03

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:3149 · comment 334763362 · PR 4360 · 2022-10-03

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +        }
> +
> +        _ <- if (deletedTransactionMaybe.isEmpty) {
> +          logger.error(s"Transaction [${msg.transactionId}] is not of the expected type [${expectedTxType}]...")
> +          Future.successful(Done)
> +        } else if (transaction.statusDetails.isInstanceOf[DeletedStatusDetails]) {
> +          Future.successful(Done)

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

## A3-1358 — CustomerAdvisoryProfileEntity.scala: Yup. Switched to another exception type for concurrent modification, and retry on it in the subscriber

**Source stance:** explanation

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileEntity.scala; PR: [INV-349] feat(advisory): Trigger CRA VC status reassessment when customer update PersonalDetails

**Source-preserving request, proposal, or question:**

> Yup. Switched to another exception type for concurrent modification, and retry on it in the subscriber

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3244 · comment 329773426 · PR 4209 · 2022-09-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileEntity.scala`

**Evidence:** anon-2.jsonl:3244 · comment 329773426 · PR 4209 · 2022-09-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileEntity.scala`

**Explicit source context (hunk):**

> +              ctx.done
> +
> +            case initializedState: Initialized =>
> +              if (
> +                initializedState.craQuestionnaireVersion != cmd.craQuestionnaireVersion ||
> +                  initializedState.craCalculationMatrixVersion != cmd.craCalculationMatrixVersion ||
> +                  initializedState.annualIncome != cmd.annualIncome ||

## A3-1375 — common.conf: use the common `kafka-custom-task.conf`?

**Source stance:** open-question

**Context:**

> marketdata-impl/src/main/resources/common.conf; PR: wip

**Source-preserving request, proposal, or question:**

> Let’s use the common `kafka-custom-task.conf`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3264 · comment 319673343 · PR 3873 · 2022-07-29

Source path: `marketdata-impl/src/main/resources/common.conf`

**Evidence:** anon-2.jsonl:3264 · comment 319673343 · PR 3873 · 2022-07-29

Source path: `marketdata-impl/src/main/resources/common.conf`

**Explicit source context (hunk):**

> autoCreateTables = true
> +
> +silver.daily-price {
> +  queue.kafka-configs {
> +    retention-ms = 259200000
> +    retention-ms = ${?SILVER_DAILY_PRICE_QUEUE_KAFKA_RETENTION_MS}

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

## A3-1379 — InstrumentMarketDataEventProcessor.scala: I mean the Lagom broker dsl TopicProducer

**Source stance:** explanation

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessor.scala; PR: wip

**Source-preserving request, proposal, or question:**

> I mean the Lagom broker dsl TopicProducer

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3268 · comment 319678152 · PR 3873 · 2022-07-29

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessor.scala`

**Evidence:** anon-2.jsonl:3268 · comment 319678152 · PR 3873 · 2022-07-29

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessor.scala`

**Explicit source context (hunk):**

> import scala.concurrent.{ExecutionContext, Future}
>  
> -class InstrumentMarketDataEventProcessor(readSide: CassandraReadSide, refProvider: PersistentEntityRefProvider)(
> +class InstrumentMarketDataEventProcessor(
> +  readSide: CassandraReadSide,
> +  refProvider: PersistentEntityRefProvider,
> +  marketDataTaskTopicProducer: MarketDataTaskTopicProducer,

## R-3317 — Not Kibana. These Kamon metrics will be collected by Prometheus, and made available in Grafana You still need to build your Grafana dashboard / alert to vi

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/task/CkaTaskTopicSubscriber.scala; PR 3722: Feat/CE-441 cka status table

**Source-preserving request, proposal, or question:**

> [incidental identifier omitted] [incidental identifier omitted] Not Kibana. These Kamon metrics will be collected by Prometheus, and made available in Grafana  
>   
> You still need to build your Grafana dashboard / alert to view and/or monitor them of course

**Conditions and limits:**

- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3317 · comment 313175578 · PR 3722 · 2022-07-01

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/task/CkaTaskTopicSubscriber.scala`

>  Not Kibana. These Kamon metrics will be collected by Prometheus, and made available in Grafana  
>   
> You still need to build your Grafana dashboard / alert to view and/or monitor them of course

## R-3318 — Not compliance. Shall we make this a parameter and set by looking up `silver.service.name` instead?

**Source stance:** suggestion

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/task/ReportTaskTopicSubscriber.scala; PR 3722: Feat/CE-441 cka status table

**Source-preserving request, proposal, or question:**

> Not compliance. Shall we make this a parameter and set by looking up `silver.service.name` instead?

**Evidence:** anon-2.jsonl:3318 · comment 313176045 · PR 3722 · 2022-07-01

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/task/ReportTaskTopicSubscriber.scala`

## R-3319 — `StatementDataGenerator` knows nothing about Kafka… I’d prefer to keep the exception in the service domain.. and we add a predicate to the kafka helper, so

**Source stance:** open-question

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/StatementDataGenerator.scala; PR 3722: Feat/CE-441 cka status table

**Source-preserving request, proposal, or question:**

> `StatementDataGenerator` knows nothing about Kafka… I’d prefer to keep the exception in the service domain.. and we add a predicate to the kafka helper, so that service can tell which one is safe to retry or not

**Evidence:** anon-2.jsonl:3319 · comment 313176276 · PR 3722 · 2022-07-01

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/StatementDataGenerator.scala`

## R-3320 — FYI this one uses Cassandra repository with IN clause. Not sure if anyone would create a FundSmart goal with 25 instruments though

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/goalcreate/GoalCreateConfirmationBehaviour.scala; PR 3721: Feat/IA productLine/FundSmartCreate

**Source-preserving request, proposal, or question:**

> FYI [incidental identifier omitted] this one uses Cassandra repository with IN clause. Not sure if anyone would create a FundSmart goal with 25 instruments though

**Conditions and limits:**

- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3320 · comment 313763140 · PR 3721 · 2022-07-05

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/goalcreate/GoalCreateConfirmationBehaviour.scala`

>  this one uses Cassandra repository with IN clause. Not sure if anyone would create a FundSmart goal with 25 instruments though

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

## R-3358 — It should throw `TopicExistsException` as usual. Increasing partitions needs to be called via `adminClient.createPartions` And decreasing partitions is not

**Source stance:** requested-change

**Context:**

> conf-reference/src/main/resources/kafka/kafka.conf; PR 3572: Add config parameter to overwrite default number of partitions per topic

**Source-preserving request, proposal, or question:**

> It should throw `TopicExistsException` as usual.
> 
> Increasing partitions needs to be called via `adminClient.createPartions`
> 
> And decreasing partitions is not supported

**Evidence:** anon-2.jsonl:3358 · comment 303835085 · PR 3572 · 2022-05-25

Source path: `conf-reference/src/main/resources/kafka/kafka.conf`

## R-3365 — If topic is not available yet, `UnknownTopicOrPartitionException` will be throw when we call `adminClient#alterConfigs` ‌ `UnknownTopicOrPartitionException

**Source stance:** explanation

**Context:**

> silver-commons/src/main/scala/com/endowus/silver/commons/kafka/CustomKafkaTopicConfigs.scala; PR 3370: IAO-109: Add CustomKafkaTopicConfigs cluster task to update Kafka topic configs

**Source-preserving request, proposal, or question:**

> If topic is not available yet, `UnknownTopicOrPartitionException` will be throw when we call `adminClient#alterConfigs`
> 
> ‌
> 
> `UnknownTopicOrPartitionException` is a subclass of Kafka `RetriableException`

**Evidence:** anon-2.jsonl:3365 · comment 293882884 · PR 3370 · 2022-04-11

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/CustomKafkaTopicConfigs.scala`

## R-3366 — The newer API for this is `incrementalAlterConfigs` which is only applicable for Kafka broker v2.3.0 onwards Our Kafka brokers are on v2.0.0

**Source stance:** explanation

**Context:**

> silver-commons/src/main/scala/com/endowus/silver/commons/kafka/KafkaTopicCreator.scala; PR 3370: IAO-109: Add CustomKafkaTopicConfigs cluster task to update Kafka topic configs

**Source-preserving request, proposal, or question:**

> The newer API for this is `incrementalAlterConfigs` which is only applicable for Kafka broker v2.3.0 onwards
> 
> Our Kafka brokers are on v2.0.0

**Evidence:** anon-2.jsonl:3366 · comment 304707670 · PR 3370 · 2022-05-30

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/KafkaTopicCreator.scala`

## R-3376 — At some point, I guess we should split PlanProfile out of Entity. Local cache built from Kafka should just be updated directly, no need to maintain event t

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/GoalTopicSubscriber.scala; PR 3524: adds product line and intent on charge and adds isAlternativeInvestment on fundsmart

**Source-preserving request, proposal, or question:**

> At some point, I guess we should split PlanProfile out of Entity. Local cache built from Kafka should just be updated directly, no need to maintain event traces I think

**Evidence:** anon-2.jsonl:3376 · comment 301716280 · PR 3524 · 2022-05-17

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/GoalTopicSubscriber.scala`

## R-3379 — Message ordering needs the partition key and sequential processing within that partition

**Source stance:** explanation

**Context:**

> dividend-api/src/main/scala/com/endowus/silver/dividend/api/DividendService.scala; PR 3078: Fix/SILVER-11385 fix ordering msgs

**Source-preserving request, proposal, or question:**

> Hmm I feel this comment is a bit misleading. Message ordering is only guarantee at partition level, that’s why we want to add partition key. Not because of how consumers consume the messages.  
>   
> If we don’t add partition key AND consumers consume with single thread, they will still run into out-of-order issue, because messages of same entity are spread to multiple partitions.
> 
> If we add partition key, BUT consumers still consume with multiple threads, they will still run into out-of-order issue, because of multiple threads in same partition.  
>   
> So we need to add partition key \+ consumers using parallelism = 1 if we really want to maintain the message ordering

**Conditions and limits:**

- PR3078 distinguishes partition-key scope, goal-plus-plan ordering, and sequential consumption within a partition; it does not require the most granular entity ID as every partition key. Source rows: anon-2.jsonl:3379, anon-2.jsonl:3380, anon-2.jsonl:3381, anon-2.jsonl:3383, anon-2.jsonl:3384, anon-2.jsonl:3385.

**Evidence:** anon-2.jsonl:3379 · comment 281494629 · PR 3078 · 2022-02-21

Source path: `dividend-api/src/main/scala/com/endowus/silver/dividend/api/DividendService.scala`

## R-3380 — Question: use goalId to preserve ordering between goal and plan messages

**Source stance:** open-question

**Context:**

> goal-api/src/main/scala/com/endowus/silver/goal/api/GoalService.scala; PR 3078: Fix/SILVER-11385 fix ordering msgs

**Source-preserving request, proposal, or question:**

> Do we want to maintain the message ordering between a goal and its plan\(s\)? If so, maybe we should use goalId as partition key even for plan messages?

**Conditions and limits:**

- PR3078 distinguishes partition-key scope, goal-plus-plan ordering, and sequential consumption within a partition; it does not require the most granular entity ID as every partition key. Source rows: anon-2.jsonl:3379, anon-2.jsonl:3380, anon-2.jsonl:3381, anon-2.jsonl:3383, anon-2.jsonl:3384, anon-2.jsonl:3385.

**Evidence:** anon-2.jsonl:3380 · comment 281495146 · PR 3078 · 2022-02-21

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/GoalService.scala`

## R-3381 — Looking at the consumers of this topic, looks like we want only instrumentId as partition key

**Source stance:** suggestion

**Context:**

> marketdata-api/src/main/scala/com/endowus/silver/marketdata/api/MarketDataService.scala; PR 3078: Fix/SILVER-11385 fix ordering msgs

**Source-preserving request, proposal, or question:**

> Looking at the consumers of this topic, looks like we want only instrumentId as partition key

**Conditions and limits:**

- PR3078 distinguishes partition-key scope, goal-plus-plan ordering, and sequential consumption within a partition; it does not require the most granular entity ID as every partition key. Source rows: anon-2.jsonl:3379, anon-2.jsonl:3380, anon-2.jsonl:3381, anon-2.jsonl:3383, anon-2.jsonl:3384, anon-2.jsonl:3385.

**Evidence:** anon-2.jsonl:3381 · comment 281495677 · PR 3078 · 2022-02-21

Source path: `marketdata-api/src/main/scala/com/endowus/silver/marketdata/api/MarketDataService.scala`

## R-3382 — Why do we need this extra field?

**Source stance:** open-question

**Context:**

> portfolio-api/src/main/scala/com/endowus/silver/portfolio/api/msgs/ModelPortfolioMsg.scala; PR 3078: Fix/SILVER-11385 fix ordering msgs

**Source-preserving request, proposal, or question:**

> Why do we need this extra field?

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3382 · comment 281496205 · PR 3078 · 2022-02-21

Source path: `portfolio-api/src/main/scala/com/endowus/silver/portfolio/api/msgs/ModelPortfolioMsg.scala`

## R-3383 — Yeah I guess this won’t matter too much then. Kafka partition key does not have to be at the most granular level - i.e. we don’t have to use entity id alwa

**Source stance:** suggestion

**Context:**

> marketdata-api/src/main/scala/com/endowus/silver/marketdata/api/MarketDataService.scala; PR 3078: Fix/SILVER-11385 fix ordering msgs

**Source-preserving request, proposal, or question:**

> Yeah I guess this won’t matter too much then. Kafka partition key does not have to be at the most granular level - i.e. we don’t have to use entity id always.
> 
> But yeah, effect is same. See `PriceTopicSubscriber` in `trading` service. Their entity is using instrumentId only, and the subscriber has logic to filter ccy.

**Conditions and limits:**

- PR3078 distinguishes partition-key scope, goal-plus-plan ordering, and sequential consumption within a partition; it does not require the most granular entity ID as every partition key. Source rows: anon-2.jsonl:3379, anon-2.jsonl:3380, anon-2.jsonl:3381, anon-2.jsonl:3383, anon-2.jsonl:3384, anon-2.jsonl:3385.

**Evidence:** anon-2.jsonl:3383 · comment 281665558 · PR 3078 · 2022-02-22

Source path: `marketdata-api/src/main/scala/com/endowus/silver/marketdata/api/MarketDataService.scala`

## R-3384 — This is another example of not using most granular level as partition key. Using goalId as partition key, all messages \(goal \+ plans\) will be sent in sa

**Source stance:** suggestion

**Context:**

> goal-api/src/main/scala/com/endowus/silver/goal/api/GoalService.scala; PR 3078: Fix/SILVER-11385 fix ordering msgs

**Source-preserving request, proposal, or question:**

> This is another example of not using most granular level as partition key.
> 
> Using goalId as partition key, all messages \(goal \+ plans\) will be sent in same kafka partition, and hence ordering among them is maintained.

**Conditions and limits:**

- PR3078 distinguishes partition-key scope, goal-plus-plan ordering, and sequential consumption within a partition; it does not require the most granular entity ID as every partition key. Source rows: anon-2.jsonl:3379, anon-2.jsonl:3380, anon-2.jsonl:3381, anon-2.jsonl:3383, anon-2.jsonl:3384, anon-2.jsonl:3385.

**Evidence:** anon-2.jsonl:3384 · comment 281669632 · PR 3078 · 2022-02-22

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/GoalService.scala`

## R-3385 — Of course, all plans under same goal will have same goalId

**Source stance:** explanation

**Context:**

> goal-api/src/main/scala/com/endowus/silver/goal/api/GoalService.scala; PR 3078: Fix/SILVER-11385 fix ordering msgs

**Source-preserving request, proposal, or question:**

> Of course, all plans under same goal will have same goalId

**Conditions and limits:**

- PR3078 distinguishes partition-key scope, goal-plus-plan ordering, and sequential consumption within a partition; it does not require the most granular entity ID as every partition key. Source rows: anon-2.jsonl:3379, anon-2.jsonl:3380, anon-2.jsonl:3381, anon-2.jsonl:3383, anon-2.jsonl:3384, anon-2.jsonl:3385.
- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3385 · comment 281704264 · PR 3078 · 2022-02-22

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/GoalService.scala`

## R-3413 — Yep, dynamic env is not on dedicated Confluent Cloud cluster, hence auto topic creation is disabled. Other dev/staging/prod envs are using self-managed Kaf

**Source stance:** explanation

**Context:**

> silver-commons/src/main/scala/com/endowus/silver/commons/kafka/CustomKafkaTopicCreation.scala; PR 3332: SILVER-12449: Report service improments

**Source-preserving request, proposal, or question:**

> Yep, dynamic env is not on dedicated Confluent Cloud cluster, hence auto topic creation is disabled.
> 
> Other dev/staging/prod envs are using self-managed Kafka clusters as of now, and they all have the config enabled.

**Evidence:** anon-2.jsonl:3413 · comment 292733245 · PR 3332 · 2022-04-06

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/CustomKafkaTopicCreation.scala`

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

## R-3425 — Only dynamic environment needs this as of now I tested in `dev` and the topic is auto created by Kafka broker

**Source stance:** reported-verification

**Context:**

> silver-commons/src/main/scala/com/endowus/silver/commons/kafka/CustomKafkaTopicCreation.scala; PR 3115: [DO NOT MERGE] SILVER-12449: Use kafka as queue to store the customer report generation tasks

**Source-preserving request, proposal, or question:**

> Only dynamic environment needs this as of now
> 
> I tested in `dev` and the topic is auto created by Kafka broker

**Evidence:** anon-2.jsonl:3425 · comment 282013071 · PR 3115 · 2022-02-23

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/CustomKafkaTopicCreation.scala`

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

## R-3488 — Don’t we need to deploy goal first to create the topic?

**Source stance:** open-question

**Context:**

> kubernetes/services.list; PR 3059: Feat/SILVER-11759 jdbc readside plan mv

**Source-preserving request, proposal, or question:**

> Don’t we need to deploy goal first to create the topic?

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3488 · comment 280644436 · PR 3059 · 2022-02-17

Source path: `kubernetes/services.list`

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

## R-3533 — That’s right, but event processor would still retry \(and fail\) until all pods are successfully deployed.

**Source stance:** observed-defect

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/ces/DividendEvents.scala; PR 2833: SILVER-11229: Fix settlement date for dividend reinvestment

**Source-preserving request, proposal, or question:**

> That’s right, but event processor would still retry \(and fail\) until all pods are successfully deployed.

**Conditions and limits:**

- PR2833 preserves separate historical migration, Confirmed-only sync, date/timestamp meanings, and optional-field alternatives. Naming evolves through priceDate to settlementDate. The final comment defers optional-forever versus mandatory-plus-migration to a later decision. Source rows: anon-2.jsonl:3522, anon-2.jsonl:3523, anon-2.jsonl:3524, anon-2.jsonl:3525, anon-2.jsonl:3526, anon-2.jsonl:3527, anon-2.jsonl:3528, anon-2.jsonl:3531, anon-2.jsonl:3533, anon-2.jsonl:3535, anon-2.jsonl:3536, anon-2.jsonl:3537, anon-2.jsonl:3538.

**Evidence:** anon-2.jsonl:3533 · comment 272794260 · PR 2833 · 2022-01-14

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/ces/DividendEvents.scala`

## R-3550 — Just to confirm, here we set this to be explicit, but we have been using the default value \(all\) already? i.e. no actual change

**Source stance:** open-question

**Context:**

> conf-reference/src/main/resources/kafka/kafka.conf; PR 2726: D2/SILVER-9967 support dynamic env

**Source-preserving request, proposal, or question:**

> Just to confirm, here we set this to be explicit, but we have been using the default value \(all\) already? i.e. no actual change

**Conditions and limits:**

- The question assuming Kafka producer defaults already used all is followed by the discovery that akka-client overrides the default. Preserve this correction. Source rows: anon-2.jsonl:3550, anon-2.jsonl:3552.

**Evidence:** anon-2.jsonl:3550 · comment 270856298 · PR 2726 · 2022-01-05

Source path: `conf-reference/src/main/resources/kafka/kafka.conf`

## R-3552 — Kafka producer default assumption is corrected by akka-client override behavior

**Source stance:** reported-verification

**Context:**

> conf-reference/src/main/resources/kafka/kafka.conf; PR 2726: D2/SILVER-9967 support dynamic env

**Source-preserving request, proposal, or question:**

> Thanks! I was thinking about default config of kafka producer. Didn’t know akka-client would override that to a less-safe value

**Conditions and limits:**

- The question assuming Kafka producer defaults already used all is followed by the discovery that akka-client overrides the default. Preserve this correction. Source rows: anon-2.jsonl:3550, anon-2.jsonl:3552.

**Evidence:** anon-2.jsonl:3552 · comment 272165048 · PR 2726 · 2022-01-12

Source path: `conf-reference/src/main/resources/kafka/kafka.conf`

## R-3554 — We don’t need this? As parallelism is local to mapAsync only

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebateDistributionTopicSubscriber.scala; PR 2798: changes endpoint to fix the rebate transactions and changes transaction service to consume in sequence

**Source-preserving request, proposal, or question:**

> We don’t need this? As parallelism is local to mapAsync only

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3554 · comment 270244198 · PR 2798 · 2021-12-31

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebateDistributionTopicSubscriber.scala`

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

